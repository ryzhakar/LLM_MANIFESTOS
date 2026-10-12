"""Ledger entries and the staleness check against manifesto versions and member digests."""
import os
import re
import time

from . import TOOL_VERSION
from .records import append_ledger, read_ledger, read_text, sha256_file, sha256_text

VERSION = re.compile(r"^version:\s*\"?([^\"\n]+)\"?\s*$", re.M)


def manifesto_version(path):
    m = VERSION.search(read_text(path))
    return m.group(1).strip() if m else None


def entry(spec, eval_dir, run_dir, cut, kind, digest_path, manifesto_paths, reader, judge,
          tasks_raw, scores, gate_result, hypothesis, change, members=()):
    digest = read_text(digest_path)
    split = gate_result["split"]
    s = scores["splits"].get(split) or scores["splits"]["all"]
    return {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "slug": spec["slug"], "cut": cut, "kind": kind, "run_dir": os.path.relpath(run_dir, eval_dir),
        "digest_path": digest_path, "digest_sha256": sha256_text(digest), "digest_words": len(digest.split()),
        "manifestos": [{"path": p, "version": manifesto_version(p)} for p in manifesto_paths],
        "members": [{"path": p, "sha256": sha256_file(p)} for p in members],
        "reader": reader, "judge": judge,
        "spec_sha256": sha256_file(os.path.join(eval_dir, "spec.json")),
        "tasks_sha256": sha256_text(tasks_raw),
        "tool_version": TOOL_VERSION,
        "hypothesis": hypothesis, "change": change,
        "numbers": {"split": split, "by_condition": {c: v["mean_violations"] for c, v in s["by_condition"].items()},
                    "done_rate": {c: v["done_rate"] for c, v in s["by_condition"].items()},
                    "digest_vs": s["digest_vs"], "digest_vs_previous": s["digest_vs_previous"],
                    "drift": {c: v["slope"] for c, v in s["drift"].items()}},
        "gate": {"pass": gate_result["pass"], "checks": [(c["name"], c["pass"]) for c in gate_result["checks"]],
                 "changed_vs_previous": gate_result["changed_vs_previous"]},
    }


def record(eval_dir, e):
    append_ledger(eval_dir, e)
    return e


def latest(eval_dir, kind="cut"):
    entries = [e for e in read_ledger(eval_dir) if e.get("kind") == kind]
    return entries[-1] if entries else None


def stale(eval_dir, digest_path):
    """Compare the latest cut entry with the manifesto versions, the digest, and the members now on disk."""
    last = latest(eval_dir)
    if last is None:
        return {"stale": True, "reasons": ["no cut in the ledger"], "entry": None}
    reasons = []
    if os.path.exists(digest_path):
        if sha256_file(digest_path) != last["digest_sha256"]:
            reasons.append("digest changed since the last cut")
    else:
        reasons.append("digest missing")
    for m in last["manifestos"]:
        now = manifesto_version(m["path"]) if os.path.exists(m["path"]) else None
        if now != m["version"]:
            reasons.append(f"{m['path']} version {m['version']} -> {now}")
    for m in last["members"]:
        now = sha256_file(m["path"]) if os.path.exists(m["path"]) else None
        if now != m["sha256"]:
            reasons.append(f"member digest changed: {m['path']}")
    return {"stale": bool(reasons), "reasons": reasons, "entry": {"cut": last["cut"], "ts": last["ts"]}}
