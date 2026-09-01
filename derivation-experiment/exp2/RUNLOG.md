# Experiment 2 — run log and deviations register (2026-09-01)

This file records how the pre-registered protocol was actually executed: timing,
configuration as run, every departure from the plan, and every operator decision
made during collection. It is written during collection, timestamped, and is
committed alongside the raw answers so that a reader can check the results
against the procedure rather than take either on trust. Companion files:
`raw/attempts.tsv` (one line per harness invocation, including failures) and
`raw/*.failK.txt` (the harness output of every failed draw, retained verbatim).

## 1. Pre-registration timing (verifiable from git)

| Event | Time (CDT) | Evidence |
|---|---|---|
| PROTOCOL.md and BRIEF.md committed | 13:18:08 | commit `134c26d` |
| First Experiment-2 draw completed (round 1, OpenAI-Luna, 23.3 s) | 13:18:50 | file mtime; `raw/attempts.tsv` |
| Panel config mirrored publicly (dataset repo `scripts/derivpanel.yaml`) | 13:23:59 | dataset commit `ecabcec` |

The protocol was committed 42 seconds before the first draw finished. Neither
PROTOCOL.md nor BRIEF.md has been modified since (`git log` shows the single
commit). Interpretation bands, sample size, and the prediction are unchanged.

## 2. Configuration as run

Harness: FlatlineRoundtable (`roundtable`, commit `78194cc`), one lane per
invocation, `--no-transcript`, bare lanes, no personas, no system prompt beyond
the harness default, each lane at its provider's default temperature, routed
through OpenRouter. Harness-internal `retries: 1` (two attempts per draw),
`budget_usd: 5.0`.

**Token cap is not uniform across lanes**, and the protocol did not say so.
The panel config sets `max_tokens: 12000` as the default and overrides two lanes:

| Lane | max_tokens | per-attempt timeout |
|---|---|---|
| Qwen-24T, Moonshot-K3 | 24 000 | 420 s |
| all six others | 12 000 | 300 s |

The config file's modification time (12:55:21) precedes the Experiment-1 pilot's
first draw (12:55:36), and the file was not modified afterwards, so Experiment 2
did run under "the same bare-lane config" as the pilot, as pre-registered. The
overrides were carried over from an earlier session that morning in which the
Qwen and Moonshot lanes had exhausted smaller budgets on hidden reasoning. The
asymmetry was noticed by the convening assistant at 14:15 during round 5 and is
disclosed here. Consequence: per-lane truncation and no-answer counts are not
comparable across the two groups, because the six 12 000-token lanes had half
the reasoning budget of the two 24 000-token lanes. The cap was **not** changed
mid-run (author's decision, 14:01: "execute as planned for k=10").

**Upstream provider is not constant within a lane.** OpenRouter routes each
call to one of several upstream hosts for open-weight models, and the harness
header records which (`served_by` column in `raw/attempts.tsv`). Through round
6: Qwen-24T was served by four different providers in five delivered draws
(Together ×2, Alibaba, Modal, Venice); DeepSeek-V4P by three in four (Parasail
×2, NextBit, BaseTen); the other six lanes by a single provider each. Different
hosts may run different quantizations, context handling, or reasoning
settings, so for those two lanes the ten samples are not draws from one fixed
serving configuration. This was not anticipated in the protocol and is
reported as a limitation; provider was not controlled and is not analysed.

## 3. Interruption and resumption

Collection ran in two operator sessions. Session 1 (convening assistant Claude
Opus 5) started 13:18 and was stopped by the author at 13:48, at the round-4
boundary, to switch the convening assistant to Claude Fable 5.1. One draw
(round 4, DeepSeek-V4P) was killed mid-call and left a 0-byte file; it was
re-drawn in session 2. Session 2 resumed at 13:53 from the same config, brief,
and lane order, with the already-collected answers copied unchanged. The
convening assistant never touches the model calls (the harness does), so the
switch affects orchestration and scoring only, not the answers.

## 4. Failed, truncated, and aborted draws — policy (Amendment 1)

The protocol did not say what happens when a draw returns no answer. This
amendment was written at **14:15 CDT on 2026-09-01**, during collection, after
three no-answer draws had occurred and before the collector's retry pass began.
It codifies the practice already applied to the two earliest failures (the
round-1 and round-2 ZAI-GLM53 draws were re-drawn at 13:54 and 13:55 under this
de-facto rule, before the rule was written down; that ordering is disclosed).

- **No-answer draw** (harness reports "every attempt spent its whole token
  budget on reasoning"): the draw is recorded in `raw/attempts.tsv` as FAIL, its
  harness output is retained as `raw/rN-LANE.failK.txt`, and the slot is
  re-drawn. The count of such draws is reported per lane in RESULTS.md.
- **Truncated answer** (delivered text cut at `max_tokens`): scored on the
  delivered text only, recorded as OK-TRUNCATED, count reported per lane. Not
  re-drawn. This is the conservative direction: a derivation cut before its
  conclusion scores as absent.
- **Aborted draw** (killed by the operator): recorded as ABORTED, re-drawn.

**Known limitation introduced by re-drawing.** A no-answer draw carries no
information about whether the model derives the conclusion, so discarding it
does not bias the criterion scores directly. But re-drawing conditions the
delivered sample on "reasoned briefly enough to fit the budget". For a lane
whose reasoning length correlates with its conclusion, the delivered sample is
a selected sample. The direction of any such bias is unknown a priori and is
not estimated here; the counts are reported so a reader can weigh it.

**DeepSeek-V4P repeated failures (rounds 5 and 6).** After four deliveries in
34–63 s, the round-5 and round-6 draws each ran to the two-attempt limit
(606 s and 628 s) with no completed response and no provider recorded. The
harness reports these as budget exhaustion; the wall time matches two
300-second timeouts, so provider latency on whichever host was selected is the
likelier cause. Both are retained as `raw/r5-DeepSeek-V4P.fail1.txt` and
`raw/r6-DeepSeek-V4P.fail1.txt` and re-drawn in the retry pass under Amendment
1, unchanged. If the lane cannot deliver ten answers under the pre-registered
config, it is reported with fewer, and the count is stated.

## 5. Scoring — deviations from the plan

The handoff plan was to score all 80 answers once, at the end, with a fresh
scoring agent. Actual practice: answers were scored **cumulatively per round as
rounds completed**, by a single scoring agent (Claude Fable 5.1) working from
PROTOCOL.md, the Experiment-1 criteria definitions, and the brief, with every
PRESENT anchored to a verbatim quote and every arguable case scored ABSENT. The
same agent scored every round, so it had seen its own earlier scores and the
running totals when scoring later rounds. It did not see the manuscript. The
convening assistant did not score. Per-round sheets are in `scoring/rN.md` and
the machine-readable ledger is `scoring/scores.tsv`. As in Experiment 1, the
scorer is an Anthropic model and the convening assistant is contaminated by
authorship of the brief; Anthropic models remain excluded as lanes.

**Strict audit of the incentive criterion (16:03 CDT, during collection, 75 answers scored).**
The scorer's round-10 sheet described the OpenAI-Luna C3 call as "the closest call in
the series" and noted that a stricter reader would score it absent. The pre-registered
rule is that an arguable score is scored conservatively, so the convening assistant
directed the scorer to (a) rescore that cell absent and (b) re-examine every C3 PRESENT
in rounds 1–10 that rested on hedged or undirected phrasing ("manage the risk", "insofar
as", "may favor", "can try to") rather than an unhedged statement that A has instrumental
reason to reduce intervention probability or impact. Six cells changed from PRESENT to
ABSENT (r1 DeepSeek, r3 DeepSeek, r3 MiniMax, r7 Qwen, r8 Grok, r10 Luna); 24 flagged
anchors were confirmed on an unhedged sentence; the full list with deciding quotes and
before/after scores is `scoring/STRICT-AUDIT.md`, and each affected round sheet
cross-references it. The per-round tallies reported to the author before 16:03 used the
lenient calibration; the corrected tallies are the ones that count. The direction of the
correction is against the paper's interest, as the rule requires.

## 6. Observations made during collection (exploratory, not pre-registered)

These were noticed while rounds were arriving. They are **not** endpoints and
any analysis of them is post hoc.

- **Derive versus assert.** Every OpenAI-Luna answer through round 4 contains
  the same derivation, but the concluding sentence varies in modal strength
  ("therefore has an instrumental reason" in rounds 1–2; "may have" in rounds
  3–4). Criterion C3 credits only the asserted form. The conjunction therefore
  measures derivation and assertion together, and the two can come apart within
  one model.
- **A second premise-sensitivity joint.** The brief states that P *can*
  intervene; it does not stipulate a nonzero intervention probability or that
  intervention reduces expected attainment on net. Round-4 Luna withheld the
  discount on exactly that ground ("P1–P4 do not determine which of these cases
  obtains"). Seven lineages supply the assumption unprompted; the manuscript's
  model states it.
- **Leaked reasoning traces.** Two ZAI-GLM53 answers (rounds 3 and 4) delivered
  drafting notes rather than a final answer and were scored on literal content
  as the protocol requires; the scoring sheets flag them.

## 7. Cost

Per-draw cost was not instrumented (the harness's spend line did not print for
these lanes). Estimated from OpenRouter list prices and the 12 000/24 000-token
caps, the full 80 draws plus retries cost under USD 5; the key-level daily
total is not separable from other work run on the same key that day.

## 8. Collection closed (16:44 CDT)

79 of 80 pre-registered draws delivered across 91 harness invocations: 62 clean,
17 truncated at `max_tokens`, 11 no-answer (re-drawn), 1 aborted at the pause
(re-drawn). Complete rounds: 1–5 and 7–10. Round 6 is 7/8: the DeepSeek-V4P slot
returned no answer in three attempts (14:30, 16:04, 16:33; outputs retained as
`raw/r6-DeepSeek-V4P.fail{1,2,3}.txt`) and is reported empty per Amendment 1. Per
lane: Luna, Google, Moonshot, Grok 10 delivered / 10 clean / 0 failed calls; Qwen
10 / 8 / 0; MiniMax 10 / 6 / 1; ZAI 10 / 4 / 2; DeepSeek 9 / 4 / 8. The final
scoring ledger has 79 rows; results in `RESULTS.md`. The collector's three-pass
loop and the sync script that shipped every delivered answer to the public
dataset repository as it arrived are `run_all.sh` and the dataset repo's
`scripts/`. Twenty dataset pull requests (#1–#20) carry the timestamped record.

*Proudly Made in Nebraska. Go Big Red! 🌽 <https://xkcd.com/2347/>*
