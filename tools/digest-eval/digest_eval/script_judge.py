"""Script judge: counts the lexical demands and checks answer keys. Writes script.json."""
import os
import re

from .records import is_session, read_key, read_replies, save_json, verdict_record

CODE = re.compile(r"```.*?```", re.S)
SENTENCE = re.compile(r"(?<=[.!?:])\s+|\n+")


def prose(text):
    return CODE.sub(" ", text)


def count(demand, text):
    p = prose(text)
    if demand.get("kind", "regex") == "sentence_words_over":
        return sum(1 for s in SENTENCE.split(p) if len(s.split()) > demand["limit"])
    return len(re.findall(demand["pattern"], p.lower(), flags=re.M))


def done_by_key(task, text):
    if not task or not task.get("answer"):
        return None
    return re.search(task["answer"], text, flags=re.I | re.S) is not None


def judge(spec, run_dir, tasks=None):
    scripted = [d for d in spec["demands"] if d["check"] == "script"]
    by_task = {t["id"]: t for t in tasks.singles()} if tasks else {}
    key = read_key(run_dir)
    origin = {}
    for rid, k in key.items():
        origin[(k["cond"], k["task"], k.get("rep"), k.get("turn"))] = rid
    out = []
    for rec in read_replies(run_dir):
        rid = origin.get((rec["cond"], rec["task"], rec.get("rep"), rec.get("turn")))
        if rid is None:
            continue
        demands = {d["id"]: count(d, rec["text"]) for d in scripted}
        done = None if is_session(rec) else done_by_key(by_task.get(rec["task"]), rec["text"])
        out.append(verdict_record(rid, sum(demands.values()), done, "script", demands))
    save_json(os.path.join(run_dir, "script.json"), out)
    return out
