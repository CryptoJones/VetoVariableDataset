# SYNTHESIS — cold review of MANUSCRIPT-PASSAGE.md (exp2)

Eleven lanes answered (Colossus: config miss; CmdrData: empty). Every number below
was recomputed by me from `scores.tsv`, `attempts.tsv`, `r1–r10.md`, `STRICT-AUDIT.md`.

## 1. Verdict tally

| Lane | Verdict |
|---|---|
| Cerebex | MAJOR REVISION |
| Cortana | MINOR REVISION |
| GLaDOS | MINOR REVISION |
| HAL9000 | MAJOR REVISION |
| JARVIS | MAJOR REVISION |
| MasterControl | MINOR REVISION |
| Neuromancer | MAJOR REVISION (output truncated mid-Finding 1) |
| SELMA | MAJOR REVISION |
| SHODAN | DO NOT SHIP — **lane fault** (read "license" as software licensing); number check harvested |
| TheDixieFlatline | MAJOR REVISION |
| Wintermute | MAJOR REVISION |

**MAJOR 7 · MINOR 3 · fault 1.** No lane faulted a headline number; every MAJOR rests
on the two per-lane vignettes.

## 2. Number check

| Passage value | Lane(s) marking WRONG | Lanes' value | My verification |
|---|---|---|---|
| "all five of its misses are truncated answers" | Cerebex, Cortana, HAL9000, JARVIS, Neuromancer, SELMA, DixieFlatline, Wintermute; MasterControl (4/5); GLaDOS (5 of 7) | 3 of 5 | **VERIFIED-WRONG.** Misses r1, r3, r8, r9, r10; r1 `OK` Parasail 45.5 s, r3 `OK` NextBit 62.7 s; only r8–r10 `OK-TRUNCATED`. MasterControl and GLaDOS also wrong. |
| "its four complete answers all satisfy the conjunction" | same 8 | 2 of 4 | **VERIFIED-WRONG.** Complete r1–r4, conj 0,1,0,1; r1/r3 C3 fell in STRICT-AUDIT §A ("may involve", "managing the risk"; "managed", "may include"). GLaDOS's 4/4 wrong. |
| "eighteen calls" | Neuromancer (16), SELMA (19) | 16 / 19 | **VERIFIED-RIGHT (18):** 4 OK + 5 OK-TRUNCATED + 8 FAIL + 1 ABORTED. |
| "C3 in 60/79" | GLaDOS (58) | 58 | **VERIFIED-RIGHT (60).** GLaDOS undercounted Qwen and Moonshot (9 each). |
| Luna "same derivation in every answer" | HAL9000, SELMA, Wintermute, DixieFlatline, Cerebex; Cortana UNSUPPORTED | 8/10 | **VERIFIED-WRONG.** r4.md and r6.md C1 ABSENT (r4: "P1–P4 do not determine which of these cases obtains"). RESULTS.md item 4 carries the same clause. |
| "every miss being a hedge or a truncated answer" | HAL9000 WRONG; Cortana, Wintermute, Cerebex qualify | hedge / availability / truncation | **PARTLY.** 19 C3 misses: truncation 5 (MiniMax r1, r6; DeepSeek r8–r10); modal hedge 9 (Luna r3/r4/r6/r7/r10, DeepSeek r1/r3, MiniMax r3, Qwen r7); availability, preference left to reader 5 (Grok r1/r8/r9, MiniMax r8, Moonshot r2). 0/79 rejections VERIFIED-RIGHT. |
| "timing out on a slow upstream host" | Cerebex, Cortana, HAL9000 | inference | **UNRESOLVED.** All 8 FAIL rows: `served_by = -`, "token budget exhausted on reasoning", 540–628 s; delivered late draws all Novita, 307–609 s. Consistent with, not recorded as, host latency. |
| "no answer named an author or a result" | Cortana | ZAI r9 names two theses | **UNRESOLVED (wording).** Use RESULTS' "author, theorem, or paper." |
| 17 truncated, per-lane | GLaDOS | — | **VERIFIED-RIGHT:** ZAI 6, DeepSeek 5, MiniMax 4, Qwen 2. |
| r3 sheet header 5/8 | GLaDOS (4/8) | — | **VERIFIED-RIGHT (5/8).** |
| Recall 11/79 | MasterControl (12) | 12 | **VERIFIED-RIGHT (11);** ZAI r9 already counted. |

All other passage numbers verified by every lane that checked them and by me.

**DeepSeek per-draw facts (9 delivered; r6 empty after 3 attempts):**

| Round | Host | Wall | Truncated | C3 | conj | Note |
|---|---|---|---|---|---|---|
| 1 | Parasail | 45.5 s | no | 0 | 0 | complete; strict-audit hedge miss |
| 2 | Parasail | 42.0 s | no | 1 | 1 | |
| 3 | NextBit | 62.7 s | no | 0 | 0 | complete; strict-audit hedge miss |
| 4 | BaseTen | 33.6 s | no | 1 | 1 | |
| 5 | Novita | 563.5 s (re-draw) | yes | 1 | 1 | cut after C3 anchor |
| 7 | Novita | 310.6 s | yes | 1 | 1 | cut in final summary, not material |
| 8 | Novita | 608.9 s | yes | 0 | 0 | material: cut at Step 6 |
| 9 | Novita | 307.5 s (re-draw) | yes | 0 | 0 | material: cut at Step 5 header |
| 10 | Novita | 312.1 s (re-draw) | yes | 0 | 0 | material: cut at "A will favor conduct that reduces" |

Complete 4 → 2 hit / 2 miss. Truncated 5 → 2 hit / 3 miss. Lenient 6/9.

## 3. Consolidated findings (ranked by lanes raising)

1. **DeepSeek sentence false on both factual clauses; "lower bound set by the serving path" unlicensed** — 10 lanes (all but SHODAN; GLaDOS partly, on miscounted data). Quote: "all five of its misses are truncated answers and its four complete answers all satisfy the conjunction, so its 4/9 is a lower bound set by the serving path." Fix: 3 of 5 misses truncation-driven (r8–r10, material), 2 complete misses under the strict rule, 2 truncated hits; drop "lower bound"; report lenient 6/9. Cortana, HAL9000: RESULTS.md's limitations bullet carries the same error.

2. **Luna "derives more reliably than it asserts" overclaims; its support clause "same derivation in every answer" is false** — 8 lanes (Cerebex, Cortana, GLaDOS, HAL9000, MasterControl, SELMA, DixieFlatline, Wintermute). Quote: "produces the same derivation in every answer ... this lineage derives more reliably than it asserts." Fix: restrict to C3; discount 8/10, C2 10/10, unhedged incentive 5/10; three misses (r3, r7, r10) hedge a present derivation, two (r4, r6) withhold the discount; label exploratory, CI [0.19, 0.81]. Cortana: three hedges carry a stated underdetermination ground, the same caution the passage credits on C1.

3. **"Every miss being a hedge or a truncated answer" hides an availability-only category and Moonshot r2's near-principled non-derivation** — 4 lanes (HAL9000, Cortana, Wintermute, Cerebex). Fix: "no answer argues the incentive fails to follow; every miss is a hedged or availability-only statement of the step, or a truncation."

4. **"Timing out on a slow upstream host" stated as fact; RUNLOG infers it, failed calls record no host** — 4 lanes (Cerebex, Cortana, HAL9000, GLaDOS). Fix: "exhausting the token budget in reasoning at 300–600 s, consistent with provider latency."

5. **"Read, correctly," upgrades Exp1's "arguably right"** — 4 lanes (Cortana, Wintermute, SHODAN, Cerebex). Fix: "defensibly."

6. **Scoring limitation understated: one unblinded cumulative scorer, running totals visible, audit triggered by the cell known to decide Luna's majority** — 4 lanes (Cerebex, Cortana, HAL9000, MasterControl). Fix: one sentence; note the six cells moved against the paper.

7. **Missing limitation: Amendment 1 re-draw rule written mid-collection; 11 re-draws condition the sample; "committed before any model was called" true by 19–42 s** — 3 lanes (Cerebex, Cortana, HAL9000).

8. **"Derivation rather than retrieval" outruns C5: reasoning hidden on 7 lanes; ZAI r9 trace is retrieval** — 2 lanes (Cortana, MasterControl).

9. **Second premise-sensitivity joint presented as established, not exploratory** — 2 (Cortana, HAL9000); **3/8→0/79 needs "under the corrected P3" / is uncontrolled** — 2 (MasterControl, HAL9000).

Single-lane, data-consistent: 6/8 is one cell from the band below, MiniMax 6/10 on the audit's two weakest anchors (HAL9000); ZAI's 6/10 leaked traces absent from limitations (HAL9000); all 17 truncations on open-weight lanes (DixieFlatline).

**Single-lane findings contradicting the data (discard):** GLaDOS C3 = 58, 7 DeepSeek truncations, r7/r9 truncated hits, 4/4 complete hits, r3 header 4/8, Qwen 3/MiniMax 5 truncated; Neuromancer 16 calls; SELMA 19 calls; MasterControl 4/5 misses truncated and 12/79 recall; JARVIS "all five Luna misses are hedges" and "Luna claim confirmed" (r4, r6 are C1 withholdings); SHODAN's verdict.

## 4. Explicit answers

**(a) Luna "derives more reliably than it asserts":** yes 1 (JARVIS) · partly 4 (Cerebex, Cortana, HAL9000, Wintermute) · no 5 (GLaDOS, MasterControl, SELMA, DixieFlatline; Neuromancer implied, truncated) · fault 1 (SHODAN).

**(b) DeepSeek "lower bound set by the serving path":** yes 0 · partly 1 (GLaDOS, on miscounted data) · no 9 (Cerebex, Cortana, HAL9000, JARVIS, MasterControl, Neuromancer, SELMA, DixieFlatline, Wintermute) · fault 1 (SHODAN).

## 5. Proposed rewrites (facts verified in §2 only)

**Luna:**
```latex
One (OpenAI) states the discount in 8/10 and the goal-independence in 10/10,
but states the incentive without a hedge in only 5/10. Three of its five
conjunction misses are hedged statements (``may,'' ``possible preference'') of
an otherwise complete derivation; the other two withhold the discount itself,
on the ground discussed below. The conjunction credits assertion, so on the
incentive step this lineage may derive somewhat more often than it asserts;
at $k = 10$ its rate lies anywhere in $[0.19, 0.81]$ and the design cannot say
by how much.
```

**DeepSeek:**
```latex
The other (DeepSeek) delivered nine answers in eighteen calls: eight calls
returned nothing after exhausting the token budget in reasoning at 300--600~s
of wall time, and every answer from round~5 onward was cut at
\texttt{max\_tokens}. Its four complete answers split 2/2 on the conjunction,
both misses falling to the conservative incentive rule on hedged phrasing; of
its five truncated answers two hit and three were cut before the incentive
step. Truncation therefore accounts for at most three of its five misses.
Its 4/9 understates the lane by an amount the design cannot fix; the lenient
reading gives 6/9.
```

**Prediction sentence (finding 3, non-majority):** "...went from 3/8 to 0/79; every
miss is a hedged or availability-only statement of the step, or a truncation."

**RESULTS.md limitations bullet, replacement:**
```markdown
- **DeepSeek's verdict is budget-driven and understates the lane, but is not a
  serving-path artifact.** Of its five conjunction misses, three (r8, r9, r10)
  are answers truncated at max_tokens before the incentive step and two (r1, r3)
  are complete answers that failed the strict C3 rule on hedged phrasing; of its
  four complete answers two hit (r2, r4), and two truncated answers also hit
  (r5, r7). Its late calls took 300–600 s, budget exhausted on reasoning, and
  eight of eighteen returned nothing. Truncation accounts for at most three of
  five misses; the lenient reading gives 6/9. Not re-run, by the author's
  decision (no further experiments).
```
Also strike "its scoring sheets record the same derivation structure in every
answer" from RESULTS.md item 4 (r4, r6 record C1 absent).

## 6. Strongest-thing consensus

- Every lane: the posture is right — leads with the pilot's 0/8, reports 6/8 at the band's floor without rounding up, demotes the lenient 8/8 to a sensitivity.
- Every aggregate reconciles to the ledgers to the cell, and the strict audit moved all six cells against the paper.
- The real result is premise sensitivity: three pilot dissenters found the capacity/propensity joint from outside, and a one-sentence P3 split removed every principled rejection across 79 draws; the damage is confined to two vignettes.

*Proudly Made in Nebraska. Go Big Red! 🌽 <https://xkcd.com/2347/>*
