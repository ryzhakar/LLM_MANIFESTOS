import os, re, sys
SCRATCH = os.environ.get("SOURCE_PULL_SCRATCH", "/tmp/source-pull")
path = SCRATCH + "/transcripts/sc1guyo5Rso.srt"
txt = open(path, encoding="utf-8", errors="replace").read()
blocks = [b for b in re.split(r"\n\s*\n", txt.strip()) if b.strip()]
TS = re.compile(r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})[,.](\d{3})")
def secs(h,m,s,ms): return int(h)*3600+int(m)*60+int(s)+int(ms)/1000
cues = []
bad = 0
for b in blocks:
    lines = b.split("\n")
    m = None
    idx = None
    for i,l in enumerate(lines):
        m = TS.search(l)
        if m: idx = i; break
    if not m:
        bad += 1; continue
    start = secs(*m.groups()[:4]); end = secs(*m.groups()[4:])
    text = " ".join(lines[idx+1:]).strip()
    cues.append((start,end,text))
print("blocks", len(blocks), "cues", len(cues), "unparsed_blocks", bad)
print("first_start", round(cues[0][0],3), "last_end", round(cues[-1][1],3))
print("non_monotonic_starts", sum(1 for a,b in zip(cues,cues[1:]) if b[0] < a[0]))
print("empty_text_cues", sum(1 for c in cues if not c[2]))
print("unk_count", txt.count("<unk>"))
print("speaker_prefix_count", len(re.findall(r"Speaker \d+:", txt)))
# longest run of identical consecutive cue texts
best=(0,None,None); run=1
for i in range(1,len(cues)+1):
    if i < len(cues) and cues[i][2] == cues[i-1][2] and cues[i][2]:
        run += 1
    else:
        if run > best[0]: best=(run, i-run, cues[i-1][2])
        run = 1
print("longest_identical_run", best[0], "starting_cue_index", best[1])
if best[2] is not None: print("  run_text_sample:", best[2][:120])
# runs of >=3 identical
print("runs_gt3", sum(1 for _ in []))
print("FIRST 3 CUES")
for s,e,t in cues[:3]: print(f"  [{s:.2f}-{e:.2f}] {t[:200]}")
print("LAST 3 CUES")
for s,e,t in cues[-3:]: print(f"  [{s:.2f}-{e:.2f}] {t[:200]}")
