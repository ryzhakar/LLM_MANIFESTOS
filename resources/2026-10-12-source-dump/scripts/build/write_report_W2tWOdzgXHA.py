import json
import os
import subprocess
import sys

SCRATCH = os.environ.get("SOURCE_PULL_SCRATCH", "/tmp/source-pull")
META = SCRATCH + "/meta/W2tWOdzgXHA.json"
AUDIO = SCRATCH + "/audio/W2tWOdzgXHA.m4a"
VIDEO = SCRATCH + "/video/W2tWOdzgXHA.mp4"
CAPS = [
    SCRATCH + "/captions/W2tWOdzgXHA.en-orig.vtt",
]
OUT = SCRATCH + "/reports/video-W2tWOdzgXHA.md"
FFPROBE = "/opt/homebrew/bin/ffprobe"

with open(META, encoding="utf-8") as f:
    d = json.load(f)

def g(k):
    v = d.get(k)
    return "null" if v is None else v

def fmt_list(v):
    if not v:
        return "none"
    return ", ".join(str(x) for x in v)

def ffprobe(path):
    out = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration,size:stream=codec_type,codec_name,width,height",
         "-of", "default=nw=1", path],
        capture_output=True, text=True,
    )
    return out.stdout.strip() or out.stderr.strip()

chapters = d.get("chapters") or []
if chapters:
    ch_lines = "\n".join(f"- {c.get('start_time')} — {c.get('title')}" for c in chapters)
else:
    ch_lines = "none"

desc = d.get("description") or ""
desc_lines = desc.splitlines()[:40]
desc_block = "\n".join(desc_lines)

def fsize(p):
    return os.path.getsize(p) if os.path.exists(p) else "MISSING"

lines = []
lines.append("# Download report: W2tWOdzgXHA")
lines.append("")
lines.append("## Metadata (copied from yt-dlp JSON)")
for k in ["id", "title", "fulltitle", "channel", "uploader", "channel_url", "upload_date", "release_date",
          "duration", "duration_string", "view_count", "webpage_url", "license", "availability"]:
    lines.append(f"- {k}: {g(k)}")
lines.append(f"- chapters:\n{ch_lines}")
lines.append("- description (first 40 lines, verbatim):")
lines.append("")
lines.append("```")
lines.append(desc_block)
lines.append("```")
lines.append(f"- tags: {fmt_list(d.get('tags'))}")
lines.append(f"- categories: {fmt_list(d.get('categories'))}")
lines.append(f"- live_status: {g('live_status')}")
lines.append("")
lines.append("## Files")
lines.append(f"- audio: {AUDIO} ({fsize(AUDIO)} bytes)")
lines.append(f"- video: {VIDEO} ({fsize(VIDEO)} bytes)")
for c in CAPS:
    lines.append(f"- caption: {c} ({fsize(c)} bytes)")
lines.append("")
lines.append("## ffprobe")
lines.append("audio:")
lines.append("```")
lines.append(ffprobe(AUDIO))
lines.append("```")
lines.append("video:")
lines.append("```")
lines.append(ffprobe(VIDEO))
lines.append("```")
lines.append("")
lines.append("## Errors")
lines.append("- Captions: `en` track returned HTTP 429 on first attempt and again after a 30-second wait; only `en-orig` (en-orig.vtt) was written. Captions are supplementary, not a transcript.")
lines.append("- No other errors. Audio and video downloads succeeded on first attempt.")
lines.append("")
lines.append(f"Metadata JSON (full): {SCRATCH}/meta/W2tWOdzgXHA.json")
lines.append("")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("wrote", OUT)
