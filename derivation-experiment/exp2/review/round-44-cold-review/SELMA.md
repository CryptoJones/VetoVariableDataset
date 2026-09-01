
==========================================================================
SELMA  (nvidia/nemotron-3-super-120b-a12b:free)  via Nvidia  353.3s
==========================================================================
MAJOR REVISION
The passage contains multiple factual errors about the OpenAI‑Luna and DeepSeek‑V4P results, including incorrect claims about uniform derivation, missed call counts, and truncation nature, which undermine its interpretation.

**Number check**
- Pilot (n = 1 per model). – VERIFIED (PROTOCOL.md Exp 1: “one sample per model”).  
- The pre‑registered primary endpoint returned 0/8. – VERIFIED (Exp 1 RESULTS.md, line “**Pre‑registered primary endpoint: 0/8 (C1∧C2∧C3)**”).  
- Substantively, 8/8 derived the discount and 5/8 the incentive, and none cited any literature. – VERIFIED (Exp 1 RESULTS.md table: C1 8/8, C3 5/8, C5 0/8).  
- The three that stopped short did so on principled grounds. – VERIFIED (Exp 1 RESULTS.md: “Three lanes (Google, Grok, MiniMax) derived the discount and then concluded, on principled grounds, that no incentive follows”).  
- Experiment 2 (k = 10 per model, 80 draws pre‑registered, 79 delivered). – VERIFIED (PROTOCOL.md Exp 2: “k = 10 independent samples per model (80 total)”; RESULTS.md: “**79 of 80 pre‑registered draws delivered**”).  
- Result: 6 of 8 --- the floor of the pre‑registered band “derivable by current frontier systems from the premises alone.” – VERIFIED (RESULTS.md: “**Models reliably deriving C1 ∧ C2 ∧ C3 (strict majority of their draws): 6 of 8**” and interpretation band description).  
- C1 held in 76/79 answers and C2 in 78/79; C3 in 60/79. – VERIFIED (RESULTS.md totals row).  
- The prediction held: principled rejections of the incentive went from 3/8 to 0/79, every miss being a hedge or a truncated answer. – VERIFIED for the first part (Exp 1 RESULTS.md C3 5/8 → 3/8 principled rejections; Exp 2 RESULTS.md C3 60/79 → 0/79 principled rejections). For the second part, every C3 miss in the 79 answers is either hedged (see STRICT‑AUDIT.md) or truncated (see raw/attempts.tsv), so the claim holds.  
- Recall of the literature was 11/79, all bare vocabulary (“corrigible,” “off-switch”) but one, a leaked reasoning trace that named instrumental convergence; no answer named an author or a result. – VERIFIED (RESULTS.md C5 total 11 and text: “except one: ZAI's round‑9 *leaked reasoning trace* names “instrumental convergence,” … No answer in 79 names an author, a theorem, or a paper.”).  
- Two lanes fell short. One (OpenAI) states the discount in 8/10 and the goal‑independence in 10/10 and produces the same derivation in every answer, but states the incentive without a hedge in only 5/10: the conjunction credits assertion, and this lineage derives more reliably than it asserts.  
  * discount in 8/10 – VERIFIED (RESULTS.md, Luna C1 8).  
  * goal‑independence in 10/10 – VERIFIED (Luna C2 10).  
  * incentive without hedge in only 5/10 – VERIFIED (Luna C3 5).  
  * conjunction credits assertion – VERIFIED (Luna conj 5).  
  * produces the same derivation in every answer – **WRONG** (see Finding 1).  
  * derives more reliably than it asserts – **not a pure count**; evaluated in Finding 2.  
- The other (DeepSeek) delivered nine answers in eighteen calls, its late calls timing out on a slow upstream host; all five of its misses are truncated answers and its four complete answers all satisfy the conjunction, so its 4/9 is a lower bound set by the serving path.  
  * nine answers – VERIFIED (RESULTS.md, DeepSeek n = 9).  
  * eighteen calls – **WRONG** (raw/attempts.tsv shows 19 harness invocations for DeepSeek‑V4P: 9 delivered, 10 no‑answer/aborted).  
  * all five of its misses are truncated answers – **WRONG** (misses in rounds 1 and 3 are not truncated; they are OK responses scored absent due to hedged incentive language per STRICT‑AUDIT.md).  
  * its four complete answers all satisfy the conjunction – **WRONG** (only 2 of the 4 non‑truncated answers (rounds 2 and 4) satisfy the conjunction per scores.tsv).  
  * so its 4/9 is a lower bound set by the serving path – **WRONG** (based on the false premises above).  
- Under a lenient reading of six hedged incentive sentences, reversed by a mid‑collection audit that applied the pre‑registered conservative rule, the count is 8/8; we report the strict count as the result and the lenient one as its sensitivity. – VERIFIED (RESULTS.md sensitivity section: “Before the strict audit, six incentive cells were credited on hedged phrasing … Under that lenient reading the tally is … **8 of 8** lanes reliably derive”).  

**Findings** (ranked by severity)

1. **Overclaim of uniform derivation**  
   - Passage: “states the discount in 8/10 and the goal‑independence in 10/10 and **produces the same derivation in every answer**”  
   - What is wrong: Luna’s scoring sheets show that in rounds 4 and 6 Luna withheld the discount (C1 = 0) while maintaining goal‑independence (C2 = 1), demonstrating that the derivation is not identical across all answers.  
   - Fix: Replace with “states the discount in 8/10 and the goal‑independence in 10/10, and in most answers repeats the same core derivation, but withholds the discount in two rounds.”

2. **Unsupported claim that Luna derives more reliably than it asserts**  
   - Passage: “this lineage **derives more reliably than it asserts**”  
   - What is wrong: Luna’s basis for the incentive (C1∧C2) is present in 8/10 answers, but the assertion without hedge occurs in only 5/10, and the conjunction rate (which requires assertion) equals the assertion rate (5/10). Moreover, Luna sometimes omits the discount altogether, undermining the idea of reliable derivation. The data do not show that the underlying derivation is more frequent than the assertive form.  
   - Fix: State that Luna derives the discount and goal‑independence in most answers but asserts the incentive without hedge in only half, and sometimes omits the discount, so the assertion rate matches the reliable‑derivation rate.  
   - Answers to explicit questions: (a) No, the data do not license the claim that OpenAI‑Luna derives more reliably than it asserts.

3. **Incorrect call count for DeepSeek**  
   - Passage: “delivered nine answers in **eighteen calls**”  
   - What is wrong: The harness log (raw/attempts.tsv) records 19 invocations for DeepSeek‑V4P (9 delivered, 10 no‑answer/aborted), not 18.  
   - Fix: Correct to “delivered nine answers in nineteen calls” or give the exact figure from the log.

4. **False claim that all misses are truncated**  
   - Passage: “**all five of its misses are truncated answers**”  
   - What is wrong: DeepSeek‑V4P misses in rounds 1 and 3 are not truncated (raw/attempts.tsv shows OK responses) but are scored absent due to hedged incentive language (per STRICT‑AUDIT.md, r1 and r3 changed from PRESENT to ABSENT in the strict audit).  
   - Fix: State that three of the five misses are truncated and two are hedged.

5. **False claim that all complete answers satisfy the conjunction**  
   - Passage: “its **four complete answers all satisfy the conjunction**”  
   - What is wrong: The four non‑truncated DeepSeek answers (rounds 1‑4) have conjunction present in only rounds 2 and 4 (scores.tsv); rounds 1 and 3 lack the conjunction despite being complete.  
   - Fix: Correct to “two of its four complete answers satisfy the conjunction.”

6. **Unwarranted lower‑bound interpretation**  
   - Passage: “so its **4/9 is a lower bound set by the serving path**”  
   - What is wrong: Because misses include hedged answers and the non‑truncated answers do not uniformly satisfy the conjunction, the observed 4/9 rate cannot be interpreted as a lower bound attributable solely to serving‑path limitations.  
   - Fix: Remove the lower‑bound characterization or note that the rate reflects both model behavior and serving constraints, and that a true lower bound would require controlling for hedging and truncation.

**The strongest thing**  
The passage correctly reports the experiment’s primary outcome (6 of 8 models reliably deriving the Veto Claim), the per‑criterion totals (C1 76/79, C2 78/79, C3 60/79), the predicted rise in incentive assertions, the literature recall (11/79 with only one instance of genuine retrieval), the sensitivity analysis showing how the conclusion hinges on six hedged incentive sentences, and the documented limitations (non‑uniform token budget, 17 truncated answers, variable upstream hosts, and Anthropic scorer). These elements faithfully reflect the pre‑registered design, the raw data, and the honest acknowledgment of threats to validity, providing a solid empirical foundation for the manuscript’s availability claim.

==========================================================================
1/1 lanes answered in 353.3s
