"""Gate: the thresholds live in the spec, fixed before any run; this applies them."""
import os

from .records import save_json


def check(name, ok, value, threshold):
    return {"name": name, "pass": bool(ok), "value": value, "threshold": threshold}


def gate(spec, scores):
    g = spec["gate"]
    split = g.get("split", "test")
    s = scores["splits"].get(split) or scores["splits"]["all"]
    by = s["by_condition"]
    vs = s["digest_vs"]
    checks = []
    none = vs.get("none")
    if none:
        checks.append(check("cut vs none: paired mean difference at or below the threshold and its interval excludes zero",
                            none["mean_diff"] is not None and none["mean_diff"] <= -g["min_cut_vs_none"]
                            and none["ci_high"] is not None and none["ci_high"] < 0,
                            none, -g["min_cut_vs_none"]))
    full = vs.get("full")
    if full:
        checks.append(check("near full: digest minus full at or below the margin",
                            full["mean_diff"] is not None and full["mean_diff"] <= g["margin_vs_full"],
                            full, g["margin_vs_full"]))
    for ctrl in ("terse", "placebo"):
        c = vs.get(ctrl)
        if c:
            checks.append(check(f"beats {ctrl}: interval of digest minus {ctrl} lies below zero",
                                c["ci_high"] is not None and c["ci_high"] < 0, c, 0))
    d = by.get("digest", {})
    floor = max([by[c]["done_rate"] for c in ("none", "full") if c in by and by[c]["done_rate"] is not None] or [0])
    if d.get("done_rate") is not None:
        checks.append(check("completion: digest done rate within the margin of the best baseline",
                            d["done_rate"] >= floor - g["completion_margin"], d["done_rate"], floor - g["completion_margin"]))
    drift = s["drift"]
    if "digest" in drift and "full" in drift and drift["digest"]["slope"] is not None and drift["full"]["slope"] is not None:
        diff = drift["digest"]["slope"] - drift["full"]["slope"]
        checks.append(check("drift: digest slope minus full slope at or below the margin",
                            diff <= g["drift_margin"], round(diff, 3), g["drift_margin"]))
    prev = s.get("digest_vs_previous")
    changed = None
    if prev and prev["ci_low"] is not None:
        changed = not (prev["ci_low"] <= 0 <= prev["ci_high"])
    return {"split": split, "pass": bool(checks) and all(c["pass"] for c in checks),
            "checks": checks, "changed_vs_previous": changed}


def write_gate(spec, run_dir, scores):
    result = gate(spec, scores)
    save_json(os.path.join(run_dir, "gate.json"), result)
    return result
