#!/bin/bash
SP=/private/tmp/claude-501/-Users-akclark/a8c643ef-cf7c-426f-81f3-9e7bf7a7b3ca/scratchpad
BRIEF=/Users/akclark/source/repos/TheVetoVariable/derivation-experiment/exp2/BRIEF.md
cd ~/source/repos/FlatlineRoundtable
for i in $(seq 1 10); do
  for lane in OpenAI-Luna Google-G37F DeepSeek-V4P Qwen-24T Moonshot-K3 ZAI-GLM53 xAI-Grok46 MiniMax-M3; do
    out=$SP/exp2/r${i}-${lane}.out
    if [ ! -s "$out" ] || ! grep -q "1/1 lanes answered" "$out"; then
      ./roundtable --config $SP/derivpanel.yaml --lanes $lane --no-transcript - < $BRIEF > "$out" 2>&1
      grep -q "1/1 lanes answered" "$out" && echo "r${i} $lane OK" || echo "r${i} $lane FAIL"
    fi
  done
done
echo EXP2-ALL-DONE
