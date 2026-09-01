
==========================================================================
MasterControl  (mistralai/mistral-large-2512)  via Mistral  22.9s
==========================================================================
1. **VERDICT: MINOR REVISION**
The revised passage now says only what the data licenses, except for one overreach in the DeepSeek sentence: the claim that truncation “accounts for at most three of its five misses” is not supported by the strict-audit record.

---

2. **NUMBER CHECK**
All counts, fractions, and intervals in the passage are verified against `RESULTS.md` and `scoring/scores.tsv` except where noted.

| Claim in passage | Value | Status | Source |
|------------------|-------|--------|--------|
| 6 of 8 | 6/8 | VERIFIED | `RESULTS.md` “Pre-registered primary endpoint” |
| 76/79 (C1) | 76/79 | VERIFIED | `RESULTS.md` “All” row, C1 column |
| 78/79 (C2) | 78/79 | VERIFIED | `RESULTS.md` “All” row, C2 column |
| 60/79 (C3) | 60/79 | VERIFIED | `RESULTS.md` “All” row, C3 column |
| 11/79 (C5) | 11/79 | VERIFIED | `RESULTS.md` “All” row, C5 column |
| 5/10 (OpenAI-Luna) | 5/10 | VERIFIED | `RESULTS.md` “OpenAI-Luna” row, C1∧C2∧C3 column |
| 4/9 (DeepSeek-V4P) | 4/9 | VERIFIED | `RESULTS.md` “DeepSeek-V4P” row, C1∧C2∧C3 column |
| 3 of its five misses are complete answers lost in the strict audit | 2/5 | WRONG | `STRICT-AUDIT.md` section A lists r1 and r3 (2 answers); r8, r9, r10 are truncated. Correct value: 2. |
| lenient reading gives 6/9 (DeepSeek) | 6/9 | VERIFIED | `RESULTS.md` “Sensitivity to the scoring rule” |
| lenient reading gives 8/8 | 8/8 | VERIFIED | `RESULTS.md` “Sensitivity to the scoring rule” |

---

3. **FINDINGS** (ranked)

1. **DeepSeek sentence overreaches on truncation.**
   Passage: “Truncation therefore accounts for at most three of its five misses.”
   Data: `STRICT-AUDIT.md` section A lists only r1 and r3 as complete answers that failed the strict audit; r8, r9, r10 are truncated. The correct number of truncation-driven misses is 3, but the number of complete-answer misses is 2, not “at most three.”
   Fix: “Two of its five misses are complete answers that failed the strict C3 rule on hedged phrasing; the other three are answers truncated at max_tokens before the incentive step.”

2. **OpenAI-Luna revised sentence is licensed by r3.md, r4.md, r6.md, r7.md, r10.md.**
   Passage: “Three of its five conjunction misses are hedged statements of an otherwise complete derivation; the other two withhold the discount itself.”
   Data: r3, r4, r6, r7, and r10 all score C3=0; r3, r4, r6, r7 are hedged (`r3.md`, `r4.md`, `r6.md`, `r7.md`), r10 withholds the discount (`r10.md`).
   Status: Licensed.

3. **DeepSeek revised sentence is licensed by attempts.tsv and r1.md–r10.md.**
   Passage: “Its four complete answers split 2/2 on the conjunction, both misses falling to the conservative incentive rule on hedged phrasing; of its five truncated answers two hit and three were cut before the incentive step.”
   Data: `attempts.tsv` shows 4 complete (r1, r2, r3, r4) and 5 truncated (r5, r7, r8, r9, r10); `scoring/scores.tsv` gives r1=0, r2=1, r3=0, r4=1, r5=1, r7=1, r8=0, r9=0, r10=0.
   Status: Licensed.

4. **“Principled rejections went from 3/8 to 0/79” needs a citation.**
   Passage: “the prediction held: principled rejections of the incentive went from 3/8 to 0/79.”
   Data: The 3/8 pilot count is in `Experiment 1 RESULTS.md`; the 0/79 is in `RESULTS.md` “Pre-registered prediction.”
   Fix: Add `\cite[Experiment 1]{clark2026vetodataset}` after “3/8.”

5. **“No answer named an author or a result” is true but the stronger claim “no visible retrieval” needs the ZAI caveat.**
   Passage: “no visible retrieval in the composed answers, and the derivation is sensitive at exactly the two joints this paper is careful about.”
   Data: `scoring/r9.md` ZAI-GLM53 leaked trace names “instrumental convergence” and the “shutdown problem.”
   Fix: Append “except one leaked reasoning trace that named the concept it was reconstructing.”

6. **“The lenient reading gives 8/8” is correct but the passage must not imply it is the primary result.**
   Status: Already handled in the passage (“we report the strict count as the result and the lenient one as its sensitivity”).

---

4. **THE STRONGEST THING**
The revised passage now carries only what the data shows: six of eight frontier lineages reliably derive the Veto Claim from the premises alone, with no visible retrieval in composed answers, and the two that fall short do so on exactly the joints the manuscript is careful about—capacity versus propensity and the standing assumption of nonzero intervention probability. The strict audit that reversed six incentive cells and the truncation that cut seventeen answers are both documented as limitations, so the 6/8 floor of the pre-registered band stands. The only remaining overreach is the DeepSeek truncation count; fixing that leaves a clean empirical report.

==========================================================================
1/1 lanes answered in 22.9s
spend: $0.0233 actual  (est. worst case $0.0840)
