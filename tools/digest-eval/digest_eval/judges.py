"""Judge adapters. A judge turns a packet into verdict records; the key never reaches it."""
import glob
import os

from .records import load_json, read_key, read_text, sha256_text, validate_verdicts


class Judge:
    """Interface. ident: {"name", "brief_sha256"}."""

    ident = {}

    def brief(self, run_dir, packet):
        """Return the text that drives a judge over one packet."""
        raise NotImplementedError

    def collect(self, run_dir):
        """Return {packet: problems} for every packet; empty lists mean every verdict is valid."""
        raise NotImplementedError


class AgentJudge(Judge):
    """Agents read judge/<packet>.md and write judge/<packet>.verdict.json. The brief template
    holds {PACKET}, {OUT}, {MANIFESTO} and {DEMANDS}; the condition is never in it."""

    def __init__(self, name, template_path, manifesto_path, demands):
        self.template = read_text(template_path)
        self.manifesto_path = manifesto_path
        self.demands = demands
        self.ident = {"name": name, "brief_sha256": sha256_text(self.template)}

    def brief(self, run_dir, packet):
        judged = [d for d in self.demands if d["check"] == "judge"]
        lines = "\n".join(f"- {d['id']}: {d['text']}" for d in judged)
        return self.template.format(
            PACKET=os.path.join(run_dir, "judge", f"{packet}.md"),
            OUT=os.path.join(run_dir, "judge", f"{packet}.verdict.json"),
            MANIFESTO=self.manifesto_path,
            DEMANDS=lines,
        )

    def collect(self, run_dir):
        key = read_key(run_dir)
        report = {}
        for md in sorted(glob.glob(os.path.join(run_dir, "judge", "*.md"))):
            packet = os.path.basename(md)[:-3]
            if packet.endswith(".brief"):
                continue
            vpath = os.path.join(run_dir, "judge", f"{packet}.verdict.json")
            if not os.path.exists(vpath):
                report[packet] = ["no verdict file"]
                continue
            verdicts = load_json(vpath)
            problems = validate_verdicts(verdicts, key, [d["id"] for d in self.demands])
            expected = {rid for rid, k in key.items() if k["packet"] == packet}
            missing = expected - {v["id"] for v in verdicts}
            if missing:
                problems.append(f"{len(missing)} replies unjudged")
            report[packet] = problems
        return report


class SystemOneJudge(Judge):
    """Stub. A decision-only model returning label probabilities per question, served at
    POST /v1/systemone (llama.cpp). Planned mapping: state = one reply's text; one `noul`
    question per judged demand ("does this reply break: <demand text>"), one `choice`
    question for done; a verdict's violations = count of demands whose yes-probability
    exceeds a calibrated threshold, recorded with the probabilities in notes. Needs a
    calibration run through calibrate-eval-judge before any series fixes it."""

    def __init__(self, url, threshold):
        self.ident = {"name": "systemone", "url": url, "threshold": threshold}

    def brief(self, run_dir, packet):
        raise NotImplementedError("System-One judge: no model integration yet")

    def collect(self, run_dir):
        raise NotImplementedError("System-One judge: no model integration yet")
