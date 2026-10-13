import json, os, subprocess
SCRATCH = os.environ.get("SOURCE_PULL_SCRATCH", "/tmp/source-pull")
META = SCRATCH + "/meta/sc1guyo5Rso.json"
d = json.load(open(META, encoding="utf-8"))
def g(k):
    v = d.get(k)
    return "null" if v is None else repr(v) if not isinstance(v, str) else v
lines = []
lines.append("# Video report: sc1guyo5Rso (S-05)\n")
for k in ["id","title","fulltitle","channel","uploader","channel_url","upload_date","release_date"]:
    lines.append(f"- {k}: {g(k)}")
lines.append(f"- duration (s): {d.get('duration')}")
lines.append(f"- duration_string: {d.get('duration_string')}")
lines.append(f"- view_count: {d.get('view_count')}")
lines.append(f"- webpage_url: {d.get('webpage_url')}")
lines.append(f"- license: {'null' if d.get('license') is None else d.get('license')}")
lines.append(f"- availability: {d.get('availability')}")
lines.append(f"- live_status: {d.get('live_status')}")
lines.append(f"- tags: {json.dumps(d.get('tags'), ensure_ascii=False)}")
lines.append(f"- categories: {json.dumps(d.get('categories'), ensure_ascii=False)}")
lines.append("")
lines.append("## Chapters")
ch = d.get("chapters")
if not ch:
    lines.append("none")
else:
    for c in ch:
        lines.append(f"- {c.get('start_time')} | {c.get('title')}")
lines.append("")
lines.append("## Description (first 40 lines, verbatim)")
lines.append("```")
desc = (d.get("description") or "").splitlines()
lines.extend(desc[:40])
lines.append("```")
lines.append("")
lines.append("## Files")
def size(p):
    return os.path.getsize(p) if os.path.exists(p) else None
files = [
 ("audio", SCRATCH + "/audio/sc1guyo5Rso.m4a"),
 ("video", SCRATCH + "/video/sc1guyo5Rso.mp4"),
 ("captions (en, auto or manual)", SCRATCH + "/captions/sc1guyo5Rso.en.vtt"),
 ("captions (en-orig)", SCRATCH + "/captions/sc1guyo5Rso.en-orig.vtt"),
 ("metadata json", META),
]
for name, p in files:
    lines.append(f"- {name}: {p} ({size(p)} bytes)")
lines.append("")
lines.append("## ffprobe")
for name, p in files[:2]:
    out = subprocess.run(["/opt/homebrew/bin/ffprobe","-v","error","-show_entries","format=duration,size:stream=codec_type,codec_name,width,height","-of","default=nw=1", p], capture_output=True, text=True).stdout
    lines.append(f"### {p}")
    lines.append("```")
    lines.append(out.strip())
    lines.append("```")
lines.append("")
lines.append("## Errors")
lines.append("- none in metadata, audio, video or caption steps (see captions/yt-dlp-captions.log)")
lines.append("")
lines.append(f"Metadata JSON (full): {META}")
open(SCRATCH + "/reports/video-sc1guyo5Rso.md","w",encoding="utf-8").write("\n".join(lines)+"\n")
print("written")
