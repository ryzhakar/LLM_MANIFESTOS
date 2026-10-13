import hashlib
ROOT = "/Users/ryzhakar/LLM_MANIFESTOS/resources/2026-10-12-source-dump"
MAN = ROOT + "/index/MANIFEST.sha256"

def h(rel):
    with open(ROOT + "/" + rel[2:], "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

OLD = "./interleaved/extractions/_checks/extraction-check2-S-05.md"
NEW = "./interleaved/extractions/_checks/extraction-check2-S-05-stale.md"
CHECK3 = "./interleaved/extractions/_checks/extraction-check3-S-05.md"
SCRIPTS = [
    "./interleaved/scripts/build_interleaved.py",
    "./interleaved/scripts/check_extractions.py",
    "./interleaved/scripts/verify_interleaved.py",
]

out = []
hit = 0
for line in open(MAN).read().splitlines():
    digest, path = line.split("  ", 1)
    if path == OLD:
        hit += 1
        out.append(f"{h(NEW)}  {NEW}")
        out.append(f"{h(CHECK3)}  {CHECK3}")
    else:
        out.append(line)
assert hit == 1
for p in SCRIPTS:
    out.append(f"{h(p)}  {p}")
open(MAN, "w").write("\n".join(out) + "\n")
print(len(out), "lines")
