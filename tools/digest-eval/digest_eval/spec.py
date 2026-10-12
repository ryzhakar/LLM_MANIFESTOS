"""Spec and task sources.

spec.json:
  {"slug", "demands": [{"id", "text", "check": "script"|"judge",
                        "kind": "regex"|"sentence_words_over", "pattern", "limit"}],
   "conditions": {"baselines": [...], "terse_line", "placebo_source", "ablations": bool},
   "reader": {"adapter": "pi", "model": "long"},
   "judge": {"name", "brief"}, "reps": int,
   "gate": {"split", "ci", "min_cut_vs_none", "margin_vs_full", "completion_margin", "drift_margin"}}
tasks.json:
  {"singles": [{"id", "family", "split": "dev"|"test", "message", "answer": regex|null}],
   "sessions": [{"id", "split", "turns": [str, ...]}]}
"""
import json
import re

from .records import load_json

CHECKS = ("script", "judge")
KINDS = ("regex", "sentence_words_over")


def load_spec(path):
    spec = load_json(path)
    problems = []
    ids = set()
    for d in spec.get("demands", []):
        if d.get("id") in ids:
            problems.append(f"demand id {d.get('id')} repeated")
        ids.add(d.get("id"))
        if d.get("check") not in CHECKS:
            problems.append(f"demand {d.get('id')} check must be one of {CHECKS}")
        if d.get("check") == "script":
            kind = d.get("kind", "regex")
            if kind not in KINDS:
                problems.append(f"demand {d['id']} kind must be one of {KINDS}")
            if kind == "regex":
                try:
                    re.compile(d.get("pattern", ""))
                except re.error as e:
                    problems.append(f"demand {d['id']} pattern: {e}")
            if kind == "sentence_words_over" and not isinstance(d.get("limit"), int):
                problems.append(f"demand {d['id']} needs an integer limit")
    for k in ("slug", "demands", "conditions", "reader", "judge", "reps", "gate"):
        if k not in spec:
            problems.append(f"spec lacks {k}")
    if not isinstance(spec.get("reps"), int) or spec.get("reps", 0) < 1:
        problems.append("reps must be a positive integer")
    if problems:
        raise ValueError("; ".join(problems))
    return spec


class TaskSource:
    """Interface: singles(split) -> [task], sessions(split) -> [session]."""

    def singles(self, split=None):
        raise NotImplementedError

    def sessions(self, split=None):
        raise NotImplementedError


class JsonTaskSource(TaskSource):
    def __init__(self, path):
        self.data = load_json(path)
        self.raw = json.dumps(self.data, sort_keys=True)

    def _pick(self, items, split):
        return [t for t in items if split in (None, "all") or t.get("split") == split]

    def singles(self, split=None):
        return self._pick(self.data.get("singles", []), split)

    def sessions(self, split=None):
        return self._pick(self.data.get("sessions", []), split)
