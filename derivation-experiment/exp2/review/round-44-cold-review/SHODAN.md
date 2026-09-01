
==========================================================================
SHODAN  (openai/gpt-oss-120b)  via AkashML  60.4s
==========================================================================
**VERDICT** — DO NOT SHIP — the passage makes two factual claims about what the data‑license permits that are not supported by any provided licensing documentation.  

---

### NUMBER CHECK  

| Claim in passage | Verified / Wrong | Source (file & line) |
|------------------|------------------|----------------------|
| Pilot primary endpoint 0/8 | VERIFIED | `Experiment 1 RESULTS.md` line 1 |
| Pilot C1 8/8 | VERIFIED | `Experiment 1 RESULTS.md` table, row “C1” |
| Pilot C3 5/8 | VERIFIED | `Experiment 1 RESULTS.md` table, row “C3” |
| Experiment 2 pre‑registered draws 80, delivered 79 | VERIFIED | `RESULTS.md` first paragraph, line 2 |
| Experiment 2 primary endpoint 6/8 models | VERIFIED | `RESULTS.md` “Pre‑registered primary endpoint” line 4 |
| C1 total 76/79 | VERIFIED | `RESULTS.md` table, “All” row, C1 column |
| C2 total 78/79 | VERIFIED | `RESULTS.md` table, “All” row, C2 column |
| C3 total 60/79 | VERIFIED | `RESULTS.md` table, “All” row, C3 column |
| Literature recall C5 11/79 | VERIFIED | `RESULTS.md` table, “All” row, C5 column |
| OpenAI‑Luna C1 8/10, C2 10/10, C3 5/10 | VERIFIED | `RESULTS.md` row “OpenAI‑Luna” |
| DeepSeek‑V4P total draws 9, conjunction 4/9 | VERIFIED | `RESULTS.md` row “DeepSeek‑V4P” |
| DeepSeek truncated answers 5 | VERIFIED | `RESULTS.md` row “DeepSeek‑V4P” (Truncated 5) |
| Total truncated answers 17 | VERIFIED | `RESULTS.md` “All” row, Truncated 17 |
| Qwen‑24T hosts 5 distinct upstream providers | VERIFIED | `RUNLOG.md` line 32 (Qwen‑24T host list) |
| DeepSeek hosts 4 distinct upstream providers | VERIFIED | `RUNLOG.md` line 30 (DeepSeek‑V4P host list) |
| Scorer is an Anthropic model (Claude Fable 5.1) | VERIFIED | `RUNLOG.md` §5 “scoring — … Claude Fable 5.1” |
| Convening assistant is an Anthropic model (Claude Opus 5) | VERIFIED | `RUNLOG.md` §3 “Session 1 … Claude Opus 5” |
| “Derives more reliably than it asserts” (OpenAI‑Luna) – claim of data‑license permission | **WRONG (unsupported)** | No license file or terms are provided in the repository; the claim cannot be verified. |
| “4/9 is a lower bound set by the serving path” (DeepSeek) – claim of data‑license permission | **WRONG (unsupported)** | No license file or terms are provided; the claim cannot be verified. |

---

### FINDINGS (ranked by severity)

1. **Unsupported licensing claim for OpenAI‑Luna** – The passage states that “the scorer’s characterization … ‘this lineage derives more reliably than it asserts’” is licensed by the data. No license document (e.g., `LICENSE`, `DATA_LICENSE.md`) is included in the dataset repository, so the claim cannot be substantiated. *Fix*: Remove the licensing justification or provide the explicit license clause that permits such a claim.

2. **Unsupported licensing claim for DeepSeek lower‑bound** – Similarly, the statement that “its 4/9 is a lower bound set by the serving path” is presented as a data‑license‑backed fact, yet no licensing text is available to confirm that the dataset author grants permission to interpret the result as a lower bound. *Fix*: Delete the licensing reference or attach the relevant license excerpt.

3. **Minor wording inconsistency about C2 scoring in the pilot** – The passage describes the pilot’s C2 failure as “required an explicit remark that the reasoning was content‑independent,” which matches the original pilot protocol (Experiment 1). However, the later “structural” C2 definition applies only to Experiment 2. The text could mislead readers into thinking the pilot used the structural rule. *Fix*: Clarify that the pilot used the original C2 definition, while Experiment 2 used the structural version.

4. **Potential over‑statement of “principled grounds”** – The passage claims the three pilot dissenters “read … ‘outside A’s control’ … correctly as foreclosing any action on intervention probability.” While the raw scores show those three models indeed omitted C3, the term “correctly” is an interpretive judgment not directly evidenced in the scoring sheets. *Fix*: Replace “correctly” with a neutral description (e.g., “interpreted the premise as precluding any incentive step”).

5. **Ambiguous reference to “the brief had collapsed §4.1’s distinction”** – This is an interpretive claim about the brief’s wording, not a data‑driven fact. It does not affect the quantitative results but could be seen as speculation. *Fix*: Cite the exact wording from `BRIEF.md` if the claim is essential, or remove the speculation.

6. **Inconsistent use of “strict majority” vs. “≥ 6/8”** – The passage says the primary endpoint is “the number of models reliably deriving … in a strict majority of their draws.” Strict majority of 10 draws is ≥ 6, which matches the interpretation band “≥ 6/8”. The wording is correct but could be tightened to avoid confusion. *Fix*: State explicitly “≥ 6 of 10 draws (strict majority) per model”.

7. **Unclear attribution of “lenient reading” count** – The passage reports “the lenient reading gives 8/8” without specifying which six modal‑verb changes are included. While the data in `STRICT‑AUDIT.md` support this, the manuscript should reference that file for transparency. *Fix*: Add a citation to `scoring/STRICT-AUDIT.md` when mentioning the lenient count.

8. **Minor typographical error** – In the “Limitations” paragraph the phrase “two lanes were served by several upstream hosts; the scorer, like the convening assistant, is an Anthropic model.” repeats “Anthropic model” twice in close proximity. *Fix*: Rephrase to avoid redundancy (e.g., “both the scorer and the convening assistant are Anthropic models”).

---

### LICENSE QUESTIONS  

a) **Does the data license permit the claim “this lineage derives more reliably than it asserts” for OpenAI‑Luna?** – *Insufficient evidence.* No license file is provided; therefore we cannot confirm that such a claim is allowed.  

b) **Does the data license permit the claim “its 4/9 is a lower bound set by the serving path” for DeepSeek?** – *Insufficient evidence.* As above, the repository contains no licensing terms that would endorse this interpretation.

---

### THE STRONGEST THING  

The passage accurately reports the core quantitative findings of the pre‑registered derivation experiments: the pilot’s 0/8 primary endpoint, the corrected premise leading to a strict‑majority success rate of 6 / 8 models in Experiment 2, and the per‑criterion tallies (C1 = 76/79, C2 = 78/79, C3 = 60/79, C5 = 11/79). All these numbers are directly traceable to the `RESULTS.md` table, the per‑round scoring sheets, and the raw attempt logs, demonstrating a high level of transparency and reproducibility. The authors correctly flag the impact of truncation, heterogeneous token caps, and upstream‑host variability, and they disclose the scoring agent’s conservative bias, thereby preserving the integrity of the empirical claim that the Veto Claim is derivable by current frontier systems under the stipulated premises.

==========================================================================
1/1 lanes answered in 60.4s
spend: $0.0021 actual  (est. worst case $0.0062)
