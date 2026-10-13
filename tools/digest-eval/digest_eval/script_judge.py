"""Script judge: counts the lexical demands and checks answer keys. Writes script.json."""
import os
import re

from .records import read_key, reply_for, save_json, verdict_record

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
    out = []
    for rid, k in read_key(run_dir).items():
        rec = reply_for(run_dir, k)
        if not rec:
            continue
        demands = {d["id"]: count(d, rec["text"]) for d in scripted}
        done = None if k.get("turn") is not None else done_by_key(by_task.get(k["task"]), rec["text"])
        out.append(verdict_record(rid, sum(demands.values()), done, "script", demands))
    save_json(os.path.join(run_dir, "script.json"), out)
    return out
