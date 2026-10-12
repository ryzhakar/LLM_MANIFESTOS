"""Reader adapters. A reader turns (system text file, message) into a reply."""
import os
import subprocess
import time

THINK_END = "</think>"


def clean(raw):
    """Keep the text after the last </think>; report whether one leaked."""
    if THINK_END in raw:
        return raw.rsplit(THINK_END, 1)[-1].strip(), True
    return raw.strip(), False


class Reader:
    """Interface. ident: {"adapter", "model"}. reply(...) -> {raw, text, leak, secs, rc, attempt}."""

    ident = {}

    def reply(self, append_path, message, session=None):
        """session: None for a single reply, else (session_dir, session_id) held across calls."""
        raise NotImplementedError


class PiReader(Reader):
    BASE = ["pi", "-p", "--no-tools", "--no-context-files", "--no-skills", "--no-extensions",
            "--no-mcp", "--no-prompt-templates", "--no-themes"]

    def __init__(self, model, cwd, timeout=900, attempts=2):
        self.ident = {"adapter": "pi", "model": model}
        self.cwd = cwd
        self.timeout = timeout
        self.attempts = attempts
        os.makedirs(cwd, exist_ok=True)

    def command(self, append_path, message, session=None):
        cmd = list(self.BASE) + ["--model", self.ident["model"]]
        cmd += ["--no-session"] if session is None else ["--session-dir", session[0], "--session-id", session[1]]
        if append_path:
            cmd += ["--append-system-prompt", append_path]
        return cmd + [message]

    def reply(self, append_path, message, session=None):
        cmd = self.command(append_path, message, session)
        out, rc, secs = "", -1, 0.0
        for attempt in range(1, self.attempts + 1):
            t0 = time.time()
            try:
                p = subprocess.run(cmd, cwd=self.cwd, capture_output=True, text=True,
                                   timeout=self.timeout, stdin=subprocess.DEVNULL)
                out, rc = p.stdout, p.returncode
            except subprocess.TimeoutExpired:
                out, rc = "", -9
            secs = round(time.time() - t0, 1)
            text, leak = clean(out)
            if text:
                return {"raw": out, "text": text, "leak": leak, "secs": secs, "rc": rc, "attempt": attempt}
        return {"raw": out, "text": "", "leak": False, "secs": secs, "rc": rc, "attempt": self.attempts}


ADAPTERS = {"pi": PiReader}


def get_reader(spec, run_dir, model=None):
    conf = spec["reader"]
    cls = ADAPTERS[conf["adapter"]]
    return cls(model or conf["model"], cwd=os.path.join(run_dir, "cwd"))
