"""Serial resumable runner. One reader per invocation, so reader blocks never interleave."""
import os
import time

from .records import reply_path, reply_record, save_json


def log(run_dir, msg):
    os.makedirs(run_dir, exist_ok=True)
    with open(os.path.join(run_dir, "progress.log"), "a", encoding="utf-8") as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + msg + "\n")


def rotate(conds, rep):
    k = rep % len(conds)
    return conds[k:] + conds[:k]


def run(run_dir, reader, tasks, conditions, reps, split=None, sessions=True):
    """conditions: {cond: append path or None}. A reply whose file exists is skipped."""
    conds = list(conditions)
    log(run_dir, f"start reader={reader.ident} reps={reps} split={split} conds={conds}")
    for rep in range(1, reps + 1):
        for task in tasks.singles(split):
            for cond in rotate(conds, rep):
                path = reply_path(run_dir, cond, task["id"], rep=rep)
                if os.path.exists(path):
                    continue
                out = reader.reply(conditions[cond], task["message"])
                rec = reply_record(cond, task["id"], task["message"], out, reader.ident, task.get("split"), rep=rep)
                save_json(path, rec)
                log(run_dir, f"single {cond} {task['id']} r{rep} {out['secs']}s leak={out['leak']} words={rec['words']}")
    if not sessions:
        log(run_dir, "DONE")
        return
    for cond in conds:
        for sess in tasks.sessions(split):
            sdir = os.path.join(run_dir, "sessions", cond, sess["id"])
            os.makedirs(sdir, exist_ok=True)
            for i, message in enumerate(sess["turns"], 1):
                path = reply_path(run_dir, cond, sess["id"], turn=i)
                if os.path.exists(path):
                    continue
                out = reader.reply(conditions[cond], message, session=(sdir, f"{sess['id']}-{cond}"))
                rec = reply_record(cond, sess["id"], message, out, reader.ident, sess.get("split"), turn=i)
                save_json(path, rec)
                log(run_dir, f"session {cond} {sess['id']} t{i:02d} {out['secs']}s leak={out['leak']} words={rec['words']}")
    log(run_dir, "DONE")
