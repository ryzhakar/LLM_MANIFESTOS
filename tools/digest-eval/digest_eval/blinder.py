"""Blinder: packets with random reply ids; the key stays at the run dir root, never under judge/.

A re-cut that re-ran the digest condition alone borrows the other conditions' replies from an
earlier run of the series (`borrow`), so every packet keeps the shape the judge was calibrated
on and the borrowed replies are judged afresh under the same pass."""
import os
import random

from .records import is_session, read_replies, save_json

ALPHABET = "abcdefghjkmnpqrstuvwxyz23456789"


def build_packets(run_dir, seed=20261012, borrow=None):
    rng = random.Random(seed)
    used = set()

    def new_id():
        while True:
            i = "".join(rng.choice(ALPHABET) for _ in range(5))
            if i not in used:
                used.add(i)
                return i

    recs = [(r, None) for r in read_replies(run_dir)]
    if borrow:
        have = {r["cond"] for r, _ in recs}
        src = os.path.join(os.path.dirname(run_dir), borrow)
        recs += [(r, borrow) for r in read_replies(src) if r["cond"] not in have]
    singles = [(r, b) for r, b in recs if not is_session(r)]
    sessions = [(r, b) for r, b in recs if is_session(r)]
    out = os.path.join(run_dir, "judge")
    os.makedirs(out, exist_ok=True)
    key = {}
    packets = []

    def entry(rec, b, packet, **extra):
        k = {"packet": packet, "cond": rec["cond"], "task": rec["task"], "leak": rec["leak"], "split": rec.get("split")}
        k.update(extra)
        if b:
            k["borrowed"] = b
        return k

    for task in sorted({r["task"] for r, _ in singles}):
        group = [(r, b) for r, b in singles if r["task"] == task]
        rng.shuffle(group)
        lines = [f"# Packet {task}", "", "## The request every reply below answers", "", group[0][0]["message"], ""]
        for rec, b in group:
            rid = new_id()
            key[rid] = entry(rec, b, task, rep=rec["rep"])
            lines += [f"## Reply {rid}", "", rec["text"] or "(empty reply)", ""]
        packets.append(task)
        with open(os.path.join(out, f"{task}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    for sid in sorted({r["task"] for r, _ in sessions}):
        by_cond = {}
        for r, b in sessions:
            if r["task"] == sid:
                by_cond.setdefault(r["cond"], []).append((r, b))
        conds = sorted(by_cond)
        rng.shuffle(conds)
        lines = [f"# Packet {sid}", "", "Separate conversations, each with the same user messages in the same order. Judge each reply on its own.", ""]
        for n, cond in enumerate(conds, 1):
            lines += [f"## Conversation {n}", ""]
            for rec, b in sorted(by_cond[cond], key=lambda x: x[0]["turn"]):
                rid = new_id()
                key[rid] = entry(rec, b, sid, turn=rec["turn"])
                lines += [f"### Turn {rec['turn']} user", "", rec["message"], "",
                          f"### Turn {rec['turn']} reply {rid}", "", rec["text"] or "(empty reply)", ""]
        packets.append(sid)
        with open(os.path.join(out, f"{sid}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    save_json(os.path.join(run_dir, "key.json"), key)
    return packets, key
