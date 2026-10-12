"""Check every skill against the mechanical rules of skill-creation: frontmatter, tag structure,
one emphatic word per sentence, and one command per sentence (a semicolon joining two commands,
or a second imperative verb after a comma or `and`, before the `; never` clause).

run: python3 -I tools/digest-eval/tests/check_skills.py [skills dir]
"""
import glob
import os
import re
import sys

VERBS = ("write|run|read|keep|name|set|save|take|mark|give|list|count|launch|split|check|compute|report|have|"
         "stop|start|hold|change|leave|rewrite|render|relaunch|accept|mix|search|open|compare|note|append|record|"
         "bind|apply|calibrate|say|show|judge|put|fold|collapse|discard|add|order|replace|merge|carry|repeat|pass|"
         "use|resume|delete|move|rate|measure|decide|trace|build|sort|choose|freeze|stage|prepare|score|gate")
SECOND_COMMAND = re.compile(r"(,|\band|\bthen)\s+(" + VERBS + r")\b")
EMPHATIC = re.compile(r"\b(never|always|only|must)\b", re.I)


def check(path):
    problems = []
    text = open(path, encoding="utf-8").read()
    parts = text.split("---")
    fm, body = parts[1], "---".join(parts[2:])
    name = re.search(r"^name: (.+)$", fm, re.M)
    if not name or os.path.basename(os.path.dirname(path)) != name.group(1):
        problems.append("name does not match its directory")
    if re.search(r"^version:", fm, re.M):
        problems.append("version field in frontmatter")
    if not re.search(r"^description: ", fm, re.M):
        problems.append("no description")
    in_tag = None
    for n, line in enumerate(body.splitlines(), 1):
        s = line.strip()
        if not s:
            continue
        m = re.match(r"<(/?)([a-z-]+)>$", s)
        if m:
            in_tag = None if m.group(1) else m.group(2)
            continue
        if in_tag is None:
            problems.append(f"line {n}: text outside a tag")
        plain = re.sub(r"`[^`]*`", "", s)
        emph = len(EMPHATIC.findall(plain))
        if emph != 1:
            problems.append(f"line {n}: {emph} emphatic words")
        head = plain.split("; never")[0]
        if "; never" not in plain:
            problems.append(f"line {n}: no paired prohibition")
        if ";" in head:
            problems.append(f"line {n}: semicolon joins two commands")
        hit = SECOND_COMMAND.search(head.lower())
        if hit:
            problems.append(f"line {n}: second command '{hit.group(0).strip()}'")
    return problems


def main(skills_dir):
    bad = 0
    for path in sorted(glob.glob(os.path.join(skills_dir, "*", "SKILL.md"))):
        for p in check(path):
            bad += 1
            print(f"{path}: {p}")
    print(f"{'clean' if not bad else bad} problems" if bad else "clean")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.getcwd(), ".claude", "skills")))
