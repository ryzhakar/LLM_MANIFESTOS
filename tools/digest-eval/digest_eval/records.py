"""Record shapes and where each is written. One home for every shape the skills share.

run dir layout (a cut, a transfer run, or the pilot):
  conditions/<cond>.txt            condition text (none has no file)
  runs/<cond>/<task>/r<rep>.json   reply record, single task
  runs/<cond>/<session>/t<turn>.json  reply record, session turn
  key.json                         reply id -> origin; never inside judge/
  judge/<packet>.md                blind packet
  judge/<packet>.verdict.json      verdict records, a list
  script.json                      verdict records from the script judge
  scores.json                      joined rows and summaries
  gate.json                        gate result
eval dir layout (evals/<slug>/):
  spec.json  tasks.json  judge_brief.md  ledger.jsonl  <run dirs>
"""
import glob
import hashlib
import json
import os

REPLY_FIELDS = ("cond", "task", "message", "raw", "text", "leak", "secs", "rc", "attempt")
VERDICT_FIELDS = ("id", "violations", "done", "notes")


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(path, obj):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)
        f.write("\n")


def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path):
    return sha256_text(read_text(path))


def reply_record(cond, task, message, out, reader, split=None, rep=None, turn=None):
    """out: dict from a reader adapter (raw, text, leak, secs, rc, attempt)."""
    rec = {"cond": cond, "task": task, "message": message, "split": split, "reader": reader}
    rec.update({k: out[k] for k in ("raw", "text", "leak", "secs", "rc", "attempt")})
    rec["words"] = len(out["text"].split())
    if turn is None:
        rec["rep"] = rep
    else:
        rec["turn"] = turn
    return rec


def reply_path(run_dir, cond, task, rep=None, turn=None):
    name = f"t{turn:02d}.json" if turn is not None else f"r{rep}.json"
    return os.path.join(run_dir, "runs", cond, task, name)


def read_replies(run_dir):
    paths = sorted(glob.glob(os.path.join(run_dir, "runs", "*", "*", "*.json")))
    return [load_json(p) for p in paths]


def reply_for(run_dir, k):
    """The reply record a key entry points at; a borrowed entry points into another run dir."""
    base = os.path.join(os.path.dirname(run_dir), k["borrowed"]) if k.get("borrowed") else run_dir
    path = reply_path(base, k["cond"], k["task"], rep=k.get("rep"), turn=k.get("turn"))
    return load_json(path) if os.path.exists(path) else {}


def is_session(rec):
    return rec.get("turn") is not None


def verdict_record(reply_id, violations, done, notes="", demands=None):
    rec = {"id": reply_id, "violations": int(violations), "done": done, "notes": notes}
    if demands is not None:
        rec["demands"] = {k: int(v) for k, v in demands.items()}
    return rec


def canonical_demands(demands, demand_ids):
    """Map a judge's demand keys onto the spec's ids: an exact id, or a key that is the part
    before the first hyphen of exactly one id (judges shorten `d07-exact` to `d07`)."""
    short = {}
    for d in demand_ids:
        short.setdefault(d.split("-")[0], []).append(d)
    out = {}
    for k, v in demands.items():
        if k in demand_ids:
            target = k
        elif len(short.get(k, [])) == 1:
            target = short[k][0]
        else:
            target = k
        out[target] = out.get(target, 0) + int(v)
    return out


def validate_verdicts(verdicts, key, demand_ids=None):
    """Return a list of problems; empty means every verdict is well formed and keyed."""
    problems = []
    seen = set()
    for v in verdicts:
        missing = [f for f in VERDICT_FIELDS if f not in v]
        if missing:
            problems.append(f"verdict {v.get('id')} lacks {missing}")
            continue
        if v["id"] not in key:
            problems.append(f"verdict id {v['id']} not in key")
        if v["id"] in seen:
            problems.append(f"verdict id {v['id']} repeated")
        seen.add(v["id"])
        if not isinstance(v["violations"], int) or v["violations"] < 0:
            problems.append(f"verdict {v['id']} violations not a count")
        if v["done"] not in (True, False, None):
            problems.append(f"verdict {v['id']} done not a bool or null")
        if demand_ids is not None and "demands" in v:
            unknown = [k for k in canonical_demands(v["demands"], demand_ids) if k not in demand_ids]
            if unknown:
                problems.append(f"verdict {v['id']} names unknown demands {unknown}")
    return problems


def read_key(run_dir):
    return load_json(os.path.join(run_dir, "key.json"))


def read_verdicts(run_dir):
    """Agent verdicts from judge/*.verdict.json, keyed by reply id."""
    out = {}
    for path in sorted(glob.glob(os.path.join(run_dir, "judge", "*.verdict.json"))):
        for v in load_json(path):
            out[v["id"]] = v
    return out


def read_script_verdicts(run_dir):
    path = os.path.join(run_dir, "script.json")
    return {v["id"]: v for v in load_json(path)} if os.path.exists(path) else {}


def ledger_path(eval_dir):
    return os.path.join(eval_dir, "ledger.jsonl")


def append_ledger(eval_dir, entry):
    with open(ledger_path(eval_dir), "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def read_ledger(eval_dir):
    path = ledger_path(eval_dir)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]
