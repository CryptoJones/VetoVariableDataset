#!/bin/bash
# Experiment 2 collector — self-resuming. Config and lane order identical to the pre-registered run.
SP=/private/tmp/claude-501/-Users-akclark/16941fa9-ccc8-4d58-b223-e359f041e6ac/scratchpad
BRIEF=/Users/akclark/source/repos/TheVetoVariable/derivation-experiment/exp2/BRIEF.md
cd ~/source/repos/FlatlineRoundtable
for pass in 1 2 3; do
  pending=0
  for i in $(seq 1 10); do
    for lane in OpenAI-Luna Google-G37F DeepSeek-V4P Qwen-24T Moonshot-K3 ZAI-GLM53 xAI-Grok46 MiniMax-M3; do
      out=$SP/exp2/r${i}-${lane}.out
      if [ ! -s "$out" ] || ! grep -q "1/1 lanes answered" "$out"; then
        ./roundtable --config $SP/derivpanel.yaml --lanes $lane --no-transcript - < $BRIEF > "$out" 2>&1
        if grep -q "1/1 lanes answered" "$out"; then echo "$(date +%H:%M:%S) pass$pass r${i} $lane OK"; else echo "$(date +%H:%M:%S) pass$pass r${i} $lane FAIL"; pending=$((pending+1)); fi
      fi
    done
  done
  [ $pending -eq 0 ] && break
done
echo "$(date +%H:%M:%S) EXP2-ALL-DONE pending=$pending"
