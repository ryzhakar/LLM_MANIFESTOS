#!/bin/bash
M=/Users/ryzhakar/Applications/MacWhisper.app/Contents/MacOS/mw
SCRATCH=${SOURCE_PULL_SCRATCH:-/tmp/source-pull}
A=$SCRATCH/audio
T=$SCRATCH/transcripts
W=$SCRATCH/work
MODEL=parakeet-pro:nvidia_parakeet-v3
run() { # id fmt
  local id=$1 fmt=$2 log=$W/mw_${1}_${2}.log
  local s=$(date +%s)
  echo "START $id $fmt $(date +%T)" >> $W/progress.log
  $M transcribe $A/$id.m4a --format $fmt --language en --model $MODEL -o $T/$id.$fmt --overwrite > $log 2>&1
  local rc=$?
  local e=$(date +%s)
  echo "EXIT=$rc" >> $log
  echo "ELAPSED $id $fmt $((e-s)) rc=$rc" >> $W/progress.log
}
run 2OMRWPOSw9s txt
run W2tWOdzgXHA srt
run W2tWOdzgXHA txt
run b4p_tcLYDV0 srt
run b4p_tcLYDV0 txt
echo ALLDONE >> $W/progress.log
