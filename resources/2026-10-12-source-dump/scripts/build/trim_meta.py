import json
import sys

DROP_KEYS = {
    "formats",
    "thumbnails",
    "automatic_captions",
    "subtitles",
    "heatmap",
    "requested_formats",
    "requested_downloads",
    "http_headers",
}

in_path, out_path = sys.argv[1], sys.argv[2]

with open(in_path, encoding="utf-8") as f:
    data = json.load(f)

for key in DROP_KEYS:
    data.pop(key, None)

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write("\n")
