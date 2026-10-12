"""Condition builder: writes conditions/<cond>.txt for every condition but `none`."""
import os
import re

from .records import read_text

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")


def strip_frontmatter(text):
    return FRONTMATTER.sub("", text, count=1).lstrip("\n")


def sentences(text):
    """Split a digest into its sentences, keeping paragraph breaks out of the count."""
    out = []
    for para in text.split("\n\n"):
        out += [s for s in SENTENCE_END.split(para.strip()) if s]
    return out


def placebo(source_text, words):
    """Length-matched placebo: the source's words, cycled to the digest's word count."""
    src = source_text.split()
    if not src:
        raise ValueError("placebo source is empty")
    return " ".join(src[i % len(src)] for i in range(words))


def build(spec, run_dir, digest_text, full_texts):
    """Return {cond: path or None}. full_texts: the manifesto texts, concatenated with their
    frontmatter stripped. Order: none, digest, baselines, ablations."""
    conf = spec["conditions"]
    baselines = conf.get("baselines", [])
    texts = {"digest": digest_text}
    if "full" in baselines:
        texts["full"] = "\n\n".join(strip_frontmatter(t).strip() for t in full_texts)
    if "terse" in baselines:
        texts["terse"] = conf["terse_line"]
    if "placebo" in baselines:
        texts["placebo"] = placebo(read_text(conf["placebo_source"]), len(digest_text.split()))
    if conf.get("ablations"):
        sents = sentences(digest_text)
        for i in range(len(sents)):
            texts[f"ablation-{i + 1:02d}"] = " ".join(sents[:i] + sents[i + 1:])
    paths = {"none": None}
    cdir = os.path.join(run_dir, "conditions")
    os.makedirs(cdir, exist_ok=True)
    for cond, text in texts.items():
        path = os.path.join(cdir, f"{cond}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text.rstrip("\n") + "\n")
        paths[cond] = path
    return paths


def load(run_dir):
    """Conditions already built in a run dir."""
    cdir = os.path.join(run_dir, "conditions")
    paths = {"none": None}
    if os.path.isdir(cdir):
        for name in sorted(os.listdir(cdir)):
            if name.endswith(".txt"):
                paths[name[:-4]] = os.path.join(cdir, name)
    return paths
