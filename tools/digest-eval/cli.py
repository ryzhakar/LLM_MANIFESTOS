"""digest-eval command line. Run as `digest-eval <command> ...` through the launcher beside this
file (or `python3 -I tools/digest-eval/cli.py`).

Every command takes <slug>, which resolves evals/<slug>/ under the current directory, the project
that holds the digest, and most take <run-dir>, a directory under it (cut-3, cut-3-big, pilot-1).
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from digest_eval import blinder, conditions, gate, judges, ledger, readers, runner, score, script_judge  # noqa: E402
from digest_eval.records import read_text  # noqa: E402
from digest_eval.spec import JsonTaskSource, load_spec  # noqa: E402

ROOT = os.getcwd()


def eval_dir(slug):
    return os.path.join(ROOT, "evals", slug)


def load(slug):
    d = eval_dir(slug)
    return d, load_spec(os.path.join(d, "spec.json")), JsonTaskSource(os.path.join(d, "tasks.json"))


def run_dir(slug, name):
    return os.path.join(eval_dir(slug), name)


def emit(obj):
    print(json.dumps(obj, indent=1, ensure_ascii=False))


def cmd_conditions(a):
    _, spec, _ = load(a.slug)
    paths = conditions.build(spec, run_dir(a.slug, a.run), read_text(a.digest), [read_text(m) for m in a.manifesto])
    emit({c: (os.path.relpath(p, ROOT) if p else None) for c, p in paths.items()})


def cmd_run(a):
    _, spec, tasks = load(a.slug)
    rd = run_dir(a.slug, a.run)
    reader = readers.get_reader(spec, rd, a.reader_model)
    conds = conditions.load(rd)
    if a.only:
        conds = {c: p for c, p in conds.items() if c in a.only}
    runner.run(rd, reader, tasks, conds, a.reps or spec["reps"], a.split, sessions=not a.no_sessions)
    print("DONE", rd)


def cmd_blind(a):
    packets, key = blinder.build_packets(run_dir(a.slug, a.run), a.seed)
    emit({"packets": packets, "ids": len(key)})


def judge_for(d, spec, manifesto):
    return judges.AgentJudge(spec["judge"]["name"], os.path.join(d, spec["judge"]["brief"]), manifesto, spec["demands"])


def cmd_brief(a):
    d, spec, _ = load(a.slug)
    print(judge_for(d, spec, a.manifesto).brief(run_dir(a.slug, a.run), a.packet))


def cmd_collect(a):
    d, spec, _ = load(a.slug)
    report = judge_for(d, spec, "").collect(run_dir(a.slug, a.run))
    emit(report)
    sys.exit(1 if any(report.values()) else 0)


def cmd_script_judge(a):
    _, spec, tasks = load(a.slug)
    out = script_judge.judge(spec, run_dir(a.slug, a.run), tasks)
    emit({"verdicts": len(out)})


def cmd_score(a):
    _, spec, _ = load(a.slug)
    prev = run_dir(a.slug, a.previous) if a.previous else None
    base = run_dir(a.slug, a.baselines) if a.baselines else None
    out = score.score(spec, run_dir(a.slug, a.run), prev, base)
    emit(out["splits"])


def cmd_gate(a):
    _, spec, _ = load(a.slug)
    rd = run_dir(a.slug, a.run)
    scores = json.load(open(os.path.join(rd, "scores.json"), encoding="utf-8"))
    emit(gate.write_gate(spec, rd, scores))


def cmd_ledger(a):
    d, spec, tasks = load(a.slug)
    rd = run_dir(a.slug, a.run)
    scores = json.load(open(os.path.join(rd, "scores.json"), encoding="utf-8"))
    result = json.load(open(os.path.join(rd, "gate.json"), encoding="utf-8"))
    reader = {"adapter": spec["reader"]["adapter"], "model": a.reader_model or spec["reader"]["model"]}
    judge = judge_for(d, spec, "").ident
    cut_path = os.path.join(rd, "cut.json")
    cut_rec = json.load(open(cut_path, encoding="utf-8")) if os.path.exists(cut_path) else {}
    e = ledger.entry(spec, d, rd, a.cut if a.cut is not None else cut_rec["cut"], a.kind, a.digest, a.manifesto,
                     reader, judge, tasks.raw, scores, result,
                     a.hypothesis or cut_rec.get("hypothesis", ""), a.change or cut_rec.get("change", ""), a.member)
    ledger.record(d, e)
    emit(e)


def cmd_reps(a):
    """Spread from judged digest/none pairs; falls back to the script judge's counts when
    no judged pairs exist (an unjudged or partial run) and says so."""
    _, spec, tasks = load(a.slug)
    rows = json.load(open(os.path.join(run_dir(a.slug, a.run), "scores.json"), encoding="utf-8"))["rows"]
    source = "violations"
    diffs = score.paired_diffs(rows)
    if len(diffs) < 2:
        source = "script_violations"
        diffs = score.paired_diffs(rows, field=source)
    if len(diffs) < 2:
        sys.exit("reps: the run holds fewer than two digest/none pairs; no spread to estimate from")
    spread = score.pstdev(diffs)
    n_tasks = len(tasks.singles(spec["gate"].get("split", "test")))
    emit({"source": source, "spread": round(spread, 3), "pairs": len(diffs), "tasks": n_tasks,
          "reps": score.reps_needed(spread, n_tasks, spec["gate"]["min_cut_vs_none"], spec["gate"].get("ci", 0.95))})


def cmd_stale(a):
    emit(ledger.stale(eval_dir(a.slug), a.digest))


def main(argv=None):
    p = argparse.ArgumentParser(prog="digest-eval")
    sub = p.add_subparsers(dest="command", required=True)

    def add(name, fn, *args):
        sp = sub.add_parser(name)
        sp.add_argument("slug")
        for flags, kw in args:
            sp.add_argument(*flags, **kw)
        sp.set_defaults(fn=fn)

    RUN = (("run",), {})
    add("conditions", cmd_conditions, RUN, (("--digest",), {"required": True}), (("--manifesto",), {"nargs": "+", "required": True}))
    add("run", cmd_run, RUN, (("--reps",), {"type": int, "default": None}), (("--split",), {"default": None}),
        (("--reader-model",), {}), (("--only",), {"nargs": "*"}), (("--no-sessions",), {"action": "store_true"}))
    add("blind", cmd_blind, RUN, (("--seed",), {"type": int, "default": 20261012}))
    add("brief", cmd_brief, RUN, (("packet",), {}), (("--manifesto",), {"required": True}))
    add("collect", cmd_collect, RUN)
    add("script-judge", cmd_script_judge, RUN)
    add("score", cmd_score, RUN, (("--previous",), {}), (("--baselines",), {}))
    add("gate", cmd_gate, RUN)
    add("ledger", cmd_ledger, RUN, (("--cut",), {"type": int}),
        (("--kind",), {"default": "cut", "choices": ["cut", "transfer", "pilot"]}),
        (("--digest",), {"required": True}), (("--manifesto",), {"nargs": "+", "required": True}),
        (("--member",), {"nargs": "*", "default": []}), (("--reader-model",), {}),
        (("--hypothesis",), {"default": ""}), (("--change",), {"default": ""}))
    add("stale", cmd_stale, (("--digest",), {"required": True}))
    add("reps", cmd_reps, RUN)
    a = p.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
