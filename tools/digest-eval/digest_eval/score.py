"""Join and score: rows per reply, means per condition, paired differences with bootstrap
confidence intervals against baselines and the previous run, drift as a per-turn slope."""
import math
import os
import random
from statistics import NormalDist, pstdev

from .records import canonical_demands, is_session, load_json, read_key, read_script_verdicts, read_verdicts, reply_for, save_json

BOOT = 2000
SEED = 20261012


def paired_diffs(rows, a="digest", b="none", field="violations"):
    """Per (task, rep) differences in `field` between two conditions over single tasks."""
    pick = lambda c: {(r["task"], r["rep"]): r[field] for r in rows if not r["session"] and r["cond"] == c and r.get(field) is not None}
    xa, xb = pick(a), pick(b)
    return [xa[k] - xb[k] for k in sorted(xa) if k in xb]


def reps_needed(spread, tasks, min_cut, level=0.95):
    """Repeats per task so the interval half-width at this spread (sd of paired differences)
    is at most half of min_cut: z*sd/sqrt(tasks*reps) <= min_cut/2."""
    if min_cut <= 0 or tasks <= 0:
        raise ValueError("min_cut and tasks must be positive")
    z = NormalDist().inv_cdf((1 + level) / 2)
    return max(1, math.ceil((2 * z * spread / min_cut) ** 2 / tasks))


def mean(xs):
    return sum(xs) / len(xs) if xs else None


def rnd(x, k=3):
    return None if x is None else round(x, k)


def bootstrap_ci(xs, level, rng):
    """Percentile confidence interval of the mean."""
    if len(xs) < 2:
        return None, None
    n = len(xs)
    means = sorted(sum(rng.choice(xs) for _ in range(n)) / n for _ in range(BOOT))
    lo = int((1 - level) / 2 * BOOT)
    hi = int((1 + level) / 2 * BOOT) - 1
    return rnd(means[lo]), rnd(means[hi])


def slope(points):
    """Least-squares slope of y over x; None with fewer than two points."""
    if len(points) < 2:
        return None
    xs, ys = zip(*points)
    mx, my = mean(xs), mean(ys)
    den = sum((x - mx) ** 2 for x in xs)
    return None if den == 0 else sum((x - mx) * (y - my) for x, y in points) / den


def join(run_dir, judged_ids=()):
    """One row per keyed reply: origin, judge verdict, script verdict, cost. A judged demand the
    verdict omits counts zero."""
    key = read_key(run_dir)
    judged = read_verdicts(run_dir)
    scripted = read_script_verdicts(run_dir)
    rows = []
    for rid, k in key.items():
        v = judged.get(rid)
        s = scripted.get(rid)
        r = reply_for(run_dir, k)
        if v is None and s is None:
            continue
        row = dict(k, id=rid)
        row["violations"] = v["violations"] if v else None
        row["done"] = v["done"] if v else None
        row["notes"] = v.get("notes", "") if v else ""
        zeros = {d: 0 for d in judged_ids} if v else {}
        judged_demands = canonical_demands((v or {}).get("demands", {}), judged_ids)
        row["demands"] = dict(zeros, **judged_demands, **(s or {}).get("demands", {}))
        row["script_violations"] = s["violations"] if s else None
        row["done_script"] = s["done"] if s else None
        row["words"] = r.get("words", len(r.get("text", "").split()))
        row["secs"] = r.get("secs")
        row["session"] = is_session(k)
        rows.append(row)
    return rows


def completion(row):
    """Verifiable completion wins over the judge's opinion when a key exists."""
    return row["done_script"] if row["done_script"] is not None else row["done"]


def summarize(rows, conds, level, rng, previous_rows=None):
    singles = [r for r in rows if not r["session"] and r["violations"] is not None]
    sessions = [r for r in rows if r["session"] and r["violations"] is not None]
    by_cond = {}
    for c in conds:
        s = [r for r in singles if r["cond"] == c]
        if not s:
            continue
        dem = {}
        for d in sorted({k for r in s for k in r["demands"]}):
            dem[d] = rnd(mean([r["demands"][d] for r in s if d in r["demands"]]))
        done = [completion(r) for r in s if completion(r) is not None]
        by_cond[c] = {
            "n": len(s),
            "mean_violations": rnd(mean([r["violations"] for r in s])),
            "mean_script_violations": rnd(mean([r["script_violations"] for r in s if r["script_violations"] is not None])),
            "done": sum(done), "done_rate": rnd(mean(done)) if done else None,
            "mean_words": rnd(mean([r["words"] for r in s]), 1),
            "mean_secs": rnd(mean([r["secs"] for r in s if r["secs"] is not None]), 1),
            "leak_rate": rnd(mean([1 if r.get("leak") else 0 for r in s])),
            "per_demand": dem,
        }

    def paired(a_rows, b_rows):
        a = {(r["task"], r["rep"]): r["violations"] for r in a_rows}
        b = {(r["task"], r["rep"]): r["violations"] for r in b_rows}
        diffs = [a[k] - b[k] for k in sorted(a) if k in b]
        lo, hi = bootstrap_ci(diffs, level, rng)
        return {"n": len(diffs), "mean_diff": rnd(mean(diffs)), "ci_low": lo, "ci_high": hi}

    digest = [r for r in singles if r["cond"] == "digest"]
    vs = {}
    for c in conds:
        if c != "digest" and c in by_cond:
            vs[c] = paired(digest, [r for r in singles if r["cond"] == c])
    previous = None
    if previous_rows is not None:
        prev = [r for r in previous_rows if not r["session"] and r["cond"] == "digest" and r["violations"] is not None]
        previous = paired(digest, prev)
    drift = {}
    for c in conds:
        s = [r for r in sessions if r["cond"] == c]
        if not s:
            continue
        per_session = []
        for sid in sorted({r["task"] for r in s}):
            k = slope([(r["turn"], r["violations"]) for r in s if r["task"] == sid])
            if k is not None:
                per_session.append(k)
        lo, hi = bootstrap_ci(per_session, level, rng)
        drift[c] = {"sessions": len(per_session), "slope": rnd(mean(per_session)), "ci_low": lo, "ci_high": hi,
                    "mean_violations": rnd(mean([r["violations"] for r in s]))}
    return {"by_condition": by_cond, "digest_vs": vs, "digest_vs_previous": previous, "drift": drift}


def score(spec, run_dir, previous_run_dir=None, baselines_run_dir=None):
    """baselines_run_dir: a run of the same series whose rows for conditions other than
    `digest` stand in for the ones this run did not re-run."""
    judged_ids = [d["id"] for d in spec["demands"] if d["check"] == "judge"]
    rows = join(run_dir, judged_ids)
    if baselines_run_dir:
        have = {r["cond"] for r in rows}
        rows += [r for r in join(baselines_run_dir, judged_ids) if r["cond"] != "digest" and r["cond"] not in have]
    prev_rows = None
    if previous_run_dir:
        prev_path = os.path.join(previous_run_dir, "scores.json")
        prev_rows = load_json(prev_path)["rows"] if os.path.exists(prev_path) else join(previous_run_dir, judged_ids)
    level = spec["gate"].get("ci", 0.95)
    conds = ["none", "digest"] + [c for c in sorted({r["cond"] for r in rows}) if c not in ("none", "digest")]
    rng = random.Random(SEED)
    splits = {"all": rows}
    for name in ("dev", "test"):
        part = [r for r in rows if r.get("split") == name]
        if part:
            splits[name] = part
    out = {"splits": {k: summarize(v, conds, level, rng, prev_rows) for k, v in splits.items()}, "rows": rows}
    save_json(os.path.join(run_dir, "scores.json"), out)
    return out
