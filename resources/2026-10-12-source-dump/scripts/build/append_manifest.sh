#!/bin/bash
set -e
R=/Users/ryzhakar/LLM_MANIFESTOS/resources/2026-10-12-source-dump
SCRATCH=${SOURCE_PULL_SCRATCH:-/tmp/source-pull}
W=$SCRATCH/work
cd "$R"
echo "before lines: $(wc -l < index/MANIFEST.sha256)"
find ./interleaved -type f | LC_ALL=C sort > "$W/interleaved-list.txt"
echo "files under interleaved: $(wc -l < "$W/interleaved-list.txt")"
xargs shasum -a 256 < "$W/interleaved-list.txt" > "$W/interleaved-append.txt"
echo "append lines: $(wc -l < "$W/interleaved-append.txt")"
head -2 "$W/interleaved-append.txt"
cat index/MANIFEST.sha256 "$W/interleaved-append.txt" > "$W/MANIFEST.new"
cp "$W/MANIFEST.new" index/MANIFEST.sha256
echo "after lines: $(wc -l < index/MANIFEST.sha256)"
cd "$W"
diff <(head -n "$(wc -l < MANIFEST.before)" "$R/index/MANIFEST.sha256") MANIFEST.before && echo "DIFF1 empty"
cd "$R"
echo "shasum failures: $(shasum -a 256 -c index/MANIFEST.sha256 | grep -v ': OK$' | wc -l)"
echo "shasum OK: $(shasum -a 256 -c index/MANIFEST.sha256 | grep -c ': OK$')"
