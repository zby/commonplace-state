---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/sakana-mass-multi-agent-self-supervision.ingest.md"
source_has_frontmatter: true
date: "2026-10-24"
depth: standard
---

# Connection Report: Ingest: Multi-Agent Self-Supervision (MASS)

**Source:** [Ingest: Multi-Agent Self-Supervision (MASS)](../../../../sources/sakana-mass-multi-agent-self-supervision.ingest.md)

The ingest already carries 15 inline links in `## Connections Found`, `## Learning Claims` and `## Limitations`. All 15 resolve: error-correction, false-positive-generation, boundary-of-automation, open-ended-improvement, proposal-selection loop, self-improving-system definition, orchestration design space, coordination guarantees, representational-form coevolution, learning-inside-a-fixed-decomposition, and the Mismanaged Geniuses, Co-Harness, Terminal-RSI, ADAS and Autoreason ingests. This report lists only candidates beyond those links.

## Discovery Trace

**Outbound rules read:** `kb/sources/COLLECTION.md` § Outbound links. Destinations: theory, reference, agent-memory-systems, agentic-systems, tags and other sources. Excluded: `kb/work/` and `kb/instructions/`. Labels: `is-evidence-for` (theory, agent-memory-systems), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `rests-on`/`abstracted-from` (theory), `see-also` (sparingly). The `external` destination is limited to `derived-from` for the original source, so no external prospecting was done.

**Description listing scan:**
- `rg -m1 '^description:'` over 25 shortlisted theory and sources files (below). Flagged: compounding-is-tested-in-later-improvement, missing-rationale-...-weights-do-across-runs, computationally-directed-self-improvement-is-a-reallocation, reviewers-share-the-fields-prior, readable-artifact-loop-is-the-tractable-unit, automated-synthesis-is-missing-good-oracles, brainstorming-how-to-test-whether-pairwise-comparison-can-harden; and among sources, harness-updating-is-not-harness-benefit, s3gym, on-the-fragility-of-self-improving-agents and position-bias.

**Topic indexes:**
- `kb/tags/` listing read. `kb/tags/COLLECTION.md` `participating:` excludes `sources`, so the ingest cannot carry tags and the by-tag rg was skipped. The ingest also has no `tags:` field.

**Body search** (theory, sources, agentic-systems, agent-memory-systems, reference, tags; excluding the source):
- `rg -l -i 'self-distill|distill.*trajector|trajector.*distill'` -- about 50 hits, mostly agent-memory-systems reviews about memory distillation. Kept none; the overlap was keyword-only. Language-models-need-sleep (self-distillation into weights) was noted but rejected (below).
- `rg -l -i 'self-judg|self-evaluat|same model.*judg|judge.*same model|self-preference'` -- surfaced s3gym (kept), program-theory-sustains-search (rejected) and a-better-factory-claim (rejected).
- `rg -l -i 'LLM.as.a?.?judge|LLM judge'` -- surfaced position-bias and does-an-llm-keep-the-same-judgment. Kept position-bias as the primary benchmark ingest; the Mazur announcement ingest duplicates it.
- `rg -l -i 'correlated (error|blind|judg|failure)|shared blind spot|common.mode'` -- surfaced reviewers-share-the-fields-prior (kept) and synthesis-is-not-error-correction (rejected).
- `rg -l -i 'recursive self-improvement'` -- many RSI ingests. Kept none beyond those already linked; none shares a specific axis beyond the RSI label.
- `rg -l -i 'workflow search|AFlow|meta-agent'` -- surfaced the theory/evidence casebooks (reverse-edge candidates) and hyperagents (rejected, since ADAS is already linked on the same axis).
- `rg -n -i 'aflow|\badas\b|sakana|co-harness|terminal-rsi'` over agentic-systems, agent-memory-systems, theory and tags -- found readable-artifact-loop-is-the-tractable-unit (kept), the-deployed-system-not-the-model (rejected) and the-bitter-lesson-selects-production-methods (rejected). No AFlow/ADAS review exists in agentic-systems.
- `rg -l -i 'pairwise'`, `'champion|incumbent'`, `'output contract'`, `'into the weights'`, `'optimizer.*bottleneck|generation.*bottleneck|proposal quality'` over kb/theory -- kept automated-synthesis-is-missing-good-oracles and the pairwise brainstorming note. The rest matched on vocabulary only.
- `rg -n -i 'position|swap|order|length bias|both orders'` over the MASS snapshot -- the capture reports no order-swap control for the pairwise self-judge, which supports the position-bias comparison.
- `rg -l 'sakana-mass'` over kb (excluding work) -- no inbound links yet.

**Link following:**
- the-deployed-system-not-the-model footer -> Co-Harness, Meta-Harness and Machine Studying evidence lines (the same neighbourhood as the existing Co-Harness link).
- readable-artifact-loop § "Why natural-language + symbolic" -> its pairing rows; it lacks a parametric-plus-readable case that discards the readable form.
- oracle-strength-spectrum -> pairwise brainstorming note.

## Connections Found

- [Compounding is tested in later improvement, not by the accepting metric](../../../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- **is-evidence-for**: MASS's role-generalization result is a candidate compounding observation. After round-1 training, the untrained optimizer and evaluator improve, and the evaluator's agreement with the external judges rises from 73% to 93%. That is later improvement machinery getting better, measured by withheld external judges rather than the self-judge that accepted the change. The note's third requirement is unmet: no causal trace links the round-2 gains to the round-1 retention as opposed to general task-family gains.
- [Missing rationale does not exclude a theory builder; weight-only retention excludes one across runs](../../../../theory/evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs.md) -- **is-evidence-for**: MASS is a clean further case of the note's split. Within a run, the workflow is a localized, criticized unit. Across rounds, only LoRA weights persist, because the workflow is deliberately stripped. The ingest's "the theory builder stops at each freeze" judgment applies this note's condition-1 argument directly.
- [Computationally directed self-improvement is a reallocation](../../../../theory/computationally-directed-self-improvement-is-a-reallocation.md) -- **is-evidence-for**: MASS moves the evaluator function inside the model, so no external judge is in the loop. It leaves the three-role split, the workflow schema, the optimizer prompt and the 12-task suite with the humans. This is a concrete answer to "which decision-bearing functions humans still supply."
- [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../../../theory/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) -- **is-evidence-for**: the rise in self-evaluator agreement with external judges (73% to 93%) across rounds is a measured trajectory for a pairwise soft oracle. The evidence is weak: it measures agreement with other LLMs, not discrimination against ground truth, and the capture shows no order-swap stability check.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../theory/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: MASS couples natural-language workflow search with parametric distillation, which is the distributed-parametric + natural-language pairing that note says has only a narrow boundary case. Its 0.94-0.96x results on SWE-bench and Terminal-Bench illustrate the note's "validation radius" point: the parametric update affected behaviour outside the trained task family, and the update procedure had no bounded check that would have caught it.
- [Automated synthesis is missing good oracles](../../../../theory/automated-synthesis-is-missing-good-oracles.md) -- **compares-with**: on which function is the binding constraint. That note holds that generation is easy and evaluation hard. MASS's role-swap ablation reports the reverse within its decomposition: a stronger optimizer mattered more than a stronger evaluator. This pairs with the existing boundary-of-automation link; see Flags.
- [Ingest: Harness-updating is not harness-benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) -- **compares-with**: on separating the producer of improvements from the executor that benefits from them. Both hold the executor fixed and vary the proposer. That paper finds that evolver identity changes the harness-updating gain by at most 3.1 points. MASS finds that a stronger optimizer helps a lot. The gap may come from task type (verifiable coding vs non-verifiable research) or from the update surface (persistent harness vs per-task workflow).
- [Ingest: S3Gym](../../../../sources/s3gym-self-testing-self-judging-self-improvement.ingest.md) -- **compares-with**: on self-judgment as the improvement signal. S3Gym finds that local self-score accuracy is nearly uncorrelated with later verified improvement. MASS trains on self-judged rankings and reports external-judge gains. Each bounds how much weight the other's self-judging result can carry.
- [Ingest: LLM Position Bias Benchmark (Swapped-Order Pairwise Judging)](../../../../sources/position-bias.ingest.md) -- **compares-with**: on the reliability of pairwise LLM judgment. MASS's champion replacement and Bradley-Terry ranking both rest on pairwise whole-workspace comparisons, and the capture reports no order-swap control. That benchmark's median 44.8% winner-flip rate is the size of confound MASS leaves unaddressed.
- [Ingest: On the fragility of self-improving agents](../../../../sources/on-the-fragility-of-self-improving-agents.ingest.md) -- **compares-with**: on evaluator-mistake retention and run-to-run variance. That paper shows accepted memories that generalize from evaluator mistakes, and gains that reverse under shuffled task order. MASS retains self-judged winners and reports no repeated runs. That paper's controls (repeated runs, shuffled order) are the ones MASS lacks.
- [Decorrelated reviewers still share the field's prior](../../../../theory/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) -- **see-also**: this note states the mechanism behind the ingest's first limitation. GPT-5.5 and Claude Opus 4.8 are decorrelated from the trained Qwen model but share the frontier-LLM prior, so rising agreement may reflect convergence on that prior rather than on research correctness.

## Bidirectional Candidates

- [Automated synthesis is missing good oracles](../../../../theory/automated-synthesis-is-missing-good-oracles.md) <-> source -- **compares-with**: the theory note would gain a scoped counter-case in which generation, not evaluation, limited improvement.

## Reverse-edge Candidates

- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) → source -- **evidence** (qualifying counter-case): this is already the ingest's Recommended Next Action. The theory note would cite the optimizer-versus-evaluator ablation together with its scope limits.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) → source -- **evidence**: correlated self-judgment compounding across training rounds, as opposed to only capping a vote (Extractable Value 2).
- [Treat continual learning as representational-form coevolution](../../../../theory/treat-continual-learning-as-representational-form-coevolution.md) → source -- **evidence**: MASS's Table 2 workflow-transfer control isolates part of what that note says Co-Harness "does not isolate." It also gives a case that moves organization from readable text into weights and then deletes the text.
- [Six reported self-improvement paths expose bounded redesign surfaces](../../../../theory/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) → source -- **evidence**: MASS is a candidate seventh path. Its retained machinery (the model's weights) is the same machinery that optimizes and evaluates the next round, while the outer loop stays fixed.
- [Real self-improving systems occupy combinations no rung captures](../../../../theory/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) → source -- **evidence**: a candidate casebook placement, combining a self-judged evaluator, weight retention that changes the evaluator, and an external LLM-judge evidential limit.
- [Agent orchestration occupies a multi-dimensional design space](../../../../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md) → source -- **evidence**: the distributed-parametric decomposition-policy row currently rests on a proposal. MASS is a reported acquisition path for that row (Extractable Value 5).

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Language models need sleep](../../../../sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md) -- self-distillation into weights is shared, but its axis (scheduling of offline consolidation) is not one MASS informs. Keyword match only.
- [HyperAgents ingest](../../../../sources/hyperagents.ingest.md) -- the meta-agent outer-loop comparison is already carried by the ADAS link. A second link on the same axis adds nothing.
- [Does an LLM keep the same judgment when you swap the answer](../../../../sources/does-an-llm-keep-the-same-judgment-when-you-swap-the-answer.ingest.md) -- an announcement-level duplicate of the position-bias ingest, which is the stronger target.
- [The deployed system, not the model, is the unit of learning](../../../../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- MASS does search a system component, but it then deliberately collapses the result into the model. The link would mainly restate the representational-form coevolution link already present.
- [The bitter lesson selects production methods, not representational forms](../../../../theory/the-bitter-lesson-selects-production-methods-not-representational.md) -- related through workflow search, but MASS gives no evidence on cross-artifact credit assignment, the note's decisive open problem.
- [A better factory claim compares operative states](../../../../theory/a-better-factory-claim-compares-operative-states.md) -- evaluator-location vocabulary fits, but the compounding and reallocation candidates already carry the concrete payoff.
- [Synthesis is not error correction](../../../../theory/synthesis-is-not-error-correction.md) -- matched on "correlated"; MASS selects a champion and does not merge outputs, so the mechanism does not apply.
- [Program theory sustains search under delayed feedback](../../../../theory/program-theory-sustains-search-under-delayed-feedback.md) -- matched on self-evaluation only.

## Index Membership

None -- `sources` is not a tag-participating collection, and source ingests are not hand-indexed in tag heads.

## Synthesis Opportunities

- The admission-oracle conjecture (Extractable Value 4): MASS (self-judged), [Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) (harness-validated) and [Terminal-RSI](../../../../sources/terminal-rsi-recursive-self-improving-terminal-agents.ingest.md) (protected verifier) together suggest that the trajectory-admission oracle bounds how far harness-then-weights loops transfer. [S3Gym](../../../../sources/s3gym-self-testing-self-judging-self-improvement.ingest.md) adds a data point on the weakness of self-scores. This would be a candidate theory note; it is not established.
- The binding constraint between generation and evaluation: MASS (optimizer-bound), [harness-updating-is-not-harness-benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) (evolver identity barely matters) and [automated synthesis is missing good oracles](../../../../theory/automated-synthesis-is-missing-good-oracles.md) (evaluation-bound) disagree. A note could state when proposal quality, not oracle quality, binds.

## Maintenance Observations

- The ingest's Extractable Value 1 says MASS is "the first source the connection discovery found that separates generation from evaluation as the binding constraint." [harness-updating-is-not-harness-benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) also varies the proposer with the executor fixed. That claim should be qualified or checked.

## Flags

- Tension: MASS's optimizer-bottleneck result conflicts with [automated synthesis is missing good oracles](../../../../theory/automated-synthesis-is-missing-good-oracles.md) and the [boundary-of-automation](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) framing. It also conflicts with the harness-updating finding that evolver identity matters little. The tension is not resolved here; the scopes differ (non-verifiable research tasks with a whole-workspace pairwise judge, vs verifiable benchmarks).
- Not a split candidate: the ingest is a single-source analysis by type, so its breadth is expected.
