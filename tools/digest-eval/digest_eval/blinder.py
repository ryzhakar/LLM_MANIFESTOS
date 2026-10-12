"""Blinder: packets with random reply ids; the key stays at the run dir root, never under judge/."""
import os
import random

from .records import is_session, read_replies, save_json

ALPHABET = "abcdefghjkmnpqrstuvwxyz23456789"


def build_packets(run_dir, seed=20261012):
    rng = random.Random(seed)
    used = set()

    def new_id():
        while True:
            i = "".join(rng.choice(ALPHABET) for _ in range(5))
            if i not in used:
                used.add(i)
                return i

    recs = read_replies(run_dir)
    singles = [r for r in recs if not is_session(r)]
    sessions = [r for r in recs if is_session(r)]
    out = os.path.join(run_dir, "judge")
    os.makedirs(out, exist_ok=True)
    key = {}
    packets = []
    for task in sorted({r["task"] for r in singles}):
        group = [r for r in singles if r["task"] == task]
        rng.shuffle(group)
        lines = [f"# Packet {task}", "", "## The request every reply below answers", "", group[0]["message"], ""]
        for rec in group:
            rid = new_id()
            key[rid] = {"packet": task, "cond": rec["cond"], "task": task, "rep": rec["rep"],
                        "leak": rec["leak"], "split": rec.get("split")}
            lines += [f"## Reply {rid}", "", rec["text"] or "(empty reply)", ""]
        packets.append(task)
        with open(os.path.join(out, f"{task}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    for sid in sorted({r["task"] for r in sessions}):
        by_cond = {}
        for r in sessions:
            if r["task"] == sid:
                by_cond.setdefault(r["cond"], []).append(r)
        conds = sorted(by_cond)
        rng.shuffle(conds)
        lines = [f"# Packet {sid}", "", "Separate conversations, each with the same user messages in the same order. Judge each reply on its own.", ""]
        for n, cond in enumerate(conds, 1):
            lines += [f"## Conversation {n}", ""]
            for rec in sorted(by_cond[cond], key=lambda r: r["turn"]):
                rid = new_id()
                key[rid] = {"packet": sid, "cond": cond, "task": sid, "turn": rec["turn"],
                            "leak": rec["leak"], "split": rec.get("split")}
                lines += [f"### Turn {rec['turn']} user", "", rec["message"], "",
                          f"### Turn {rec['turn']} reply {rid}", "", rec["text"] or "(empty reply)", ""]
        packets.append(sid)
        with open(os.path.join(out, f"{sid}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    save_json(os.path.join(run_dir, "key.json"), key)
    return packets, key
