
==========================================================================
Neuromancer  (deepseek/deepseek-v4-flash)  via StreamLake  140.4s
==========================================================================
## 1. VERDICT

**MAJOR REVISION** — the passage contains factual errors about DeepSeek’s misses and OpenAI-Luna’s derivation consistency that misrepresent the strict-scored results.

## 2. NUMBER CHECK

| Claim in passage | Verified? | Source |
|---|---|---|
| Pilot 0/8 primary endpoint | VERIFIED | Exp1 RESULTS.md |
| Pilot 8/8 derived discount (C1) | VERIFIED | Exp1 RESULTS.md |
| Pilot 5/8 derived incentive (C3) | VERIFIED | Exp1 RESULTS.md |
| Pilot 0/8 cited literature (C5) | VERIFIED | Exp1 RESULTS.md |
| Pilot 3 stopped on principled grounds | VERIFIED | Exp1 RESULTS.md |
| Exp2: k=10 per model, 80 draws pre-registered, 79 delivered | VERIFIED | PROTOCOL.md, RESULTS.md, RUNLOG.md §8 |
| Exp2 primary endpoint: 6 of 8 models | VERIFIED | RESULTS.md |
| C1: 76/79 | VERIFIED | scores.tsv (sum=76) |
| C2: 78/79 | VERIFIED | scores.tsv (sum=78) |
| C3: 60/79 | VERIFIED | scores.tsv (sum=60) |
| Principled rejections: 3/8 → 0/79 | VERIFIED | Exp1 RESULTS.md, RESULTS.md |
| Recall: 11/79, all bare vocab but one naming instrumental convergence | VERIFIED | scores.tsv C5 column, scoring/r9.md |
| OpenAI-Luna: discount 8/10, goal-independence 10/10, incentive 5/10 | VERIFIED | scores.tsv Luna rows |
| DeepSeek: 9 answers delivered | VERIFIED | RESULTS.md (n=9) |
| DeepSeek: “eighteen calls” | **WRONG** — 16 harness invocations counted in `raw/attempts.tsv` | attempts.tsv shows 16 DeepSeek lines |
| DeepSeek: “all five of its misses are truncated answers” | **WRONG** for strict count — misses r1 and r3 are complete, not truncated | scores.tsv r1 and r3 DeepSeek; raw/attempts.tsv shows OK for r1, r3 |
| DeepSeek: “its four complete answers all satisfy the conjunction” | **WRONG** for strict count — r1 and r3 have conj=0 | scores.tsv r1 and r3 DeepSeek |
| “its 4/9 is a lower bound set by the serving path” | **NOT LICENSED** for strict count — two misses (r1, r3) are not truncation-driven | scores.tsv, STRICT-AUDIT.md |
| Lenient reading: 8/8 models | VERIFIED | STRICT-AUDIT.md §D (lenient pre-audit) |
| Six hedged incentive sentences reversed by audit | VERIFIED | STRICT-AUDIT.md (6 cells changed) |
| 17 truncated answers | VERIFIED | RESULTS.md (Truncated column sum=17) |
| Two lanes served by several upstream hosts | VERIFIED | RUNLOG.md §2 (Qwen 5, DeepSeek 4 hosts) |

## 3. FINDINGS (ranked by severity)

### FINDING 1 (SEVERE) — DeepSeek miss characterization is factually wrong for the strict count

**Passage sentence:** *“all five of its misses are truncated answers and its four complete answers all satisfy the conjunction, so its 4/9 is a lower bound set by the serving path.”*

**What is wrong:** Under the strict scoring that the passage reports as the result, DeepSeek’s five misses are: r1 (complete, conj=0), r3 (complete, conj=0), r8 (truncated, conj=0), r9 (truncated, conj=0), r10 (truncated, conj=0). Two misses are complete, not truncated. Only two of the four complete answers (r2, r4) satisfy

  !! TRUNCATED — hit max_tokens; raise it for this lane

==========================================================================
1/1 lanes answered in 140.4s
spend: $0.0048 actual  (est. worst case $0.0135)
