---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md"
source_has_frontmatter: true
date: "2026-07-16"
depth: standard
---

# Connection Report: Formal systems assess reach only through causal and proof obligations

**Source:** [Formal systems assess reach only through causal and proof obligations](../../../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md)

## Discovery Trace

**Description listing scan:**
- Ran `rg -n '^description:' kb/notes/ --glob '*.md'`; screened for reach, causal/proof, formal/symbolic, oracle, verification, and self-improvement descriptions. Kept oracle-theory and evaluation-neighbor candidates; rejected broad symbolic-substrate hits that did not speak to assessing claimed generality.
- Ran `rg -n '^description:' kb/reference/ --glob '*.md'`; kept no outbound candidates. `commonplace-as-a-reflective-system.md` and tag-readme trace docs mention oracle-bounded autonomy, but their useful theoryward target is already [warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), not this source.
- Ran `rg -n '^description:' kb/instructions/ --glob '*.md'`; flagged `review-gates/prose/pseudo-formalism.md` for reverse-edge review because its test asks whether formal-looking material derives a consequence.
- Ran `rg -n '^description:' kb/sources/ --glob '*.md'`; source matches were mostly broad hard-oracle or symbolic-benchmark evidence. Existing causal and proof sources are already linked from the target. Additional benchmark ingests were rejected as hard-oracle examples rather than reach-assessment evidence.
- Ran `rg -n '^description:' kb/agent-memory-systems/ --glob '*.md'`; flagged Decapod because its description names proof gates. Most other "oracle" hits describe extraction or reward oracles and do not help a reader understand formal reach assessment.
- Ran `rg -n '^description:' kb/agentic-systems/ --glob '*.md'`; no kept candidates.

**Topic indexes:**
- Read `kb/notes/README.md`, `kb/notes/foundations-README.md`, `kb/notes/computational-model-README.md`, and `kb/notes/self-improving-systems-README.md`. `self-improving-systems-README.md` declares `complete: true`, so the by-tag `rg` pass for `self-improving-systems` was skipped. It already links the source with the context phrase "reach assessment isn't LLM-exclusive."
- Ran `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`; kept already-linked reach, warranted-autonomy, and Goedel-machine neighbors as encoded context, not new candidates.
- Ran `rg -l '^tags:.*\bcomputational-model\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`; kept `semantic-review-catches-content-errors-that-structural-validation.md` and `systematic-prompt-variation-serves-verification-and-diagnosis-not.md` as evaluation contrasts.
- Read `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/instructions/README.md` for destination orientation. Read `kb/instructions/COLLECTION.md`, `kb/reference/COLLECTION.md`, `kb/sources/COLLECTION.md`, `kb/agent-memory-systems/COLLECTION.md`, and `kb/agentic-systems/COLLECTION.md` for likely reverse-edge labels and destination posture where needed.
- Read `kb/notes/evaluation-README.md`, `kb/notes/llm-interpretation-errors-README.md`, `kb/notes/constraining-README.md`, and `kb/notes/learning-theory-README.md` while evaluating index membership. `evaluation-README.md` and `computational-model-README.md` are plausible future heads for this source; `self-improving-systems-README.md` already includes it.

**Body search:**
- `rg -n 'formal|reach|causal|proof|invariant|symbolic|oracle|warrant|theorem|Gödel|Godel|generalization|counterfactual|intervention' kb/notes/ --glob '*.md'` -- found the existing immediate neighborhood: reach assessment, representational form, Goedel machines, reflection under structured shifts, and warranted autonomy. Kept broader oracle/evaluation candidates for body reading.
- `rg -n 'formal|reach|causal|proof|invariant|symbolic|oracle|warrant|theorem|Gödel|Godel|generalization|counterfactual|intervention' kb/reference/ --glob '*.md'` -- found reference docs about reflection, review, and ADRs; rejected as shipped-system descriptions unless an inverse rationale edge was clearly needed.
- `rg -n 'formal|reach|causal|proof|invariant|symbolic|oracle|warrant|theorem|Gödel|Godel|generalization|counterfactual|intervention' kb/instructions/ --glob '*.md'` -- surfaced `semantic/explanatory-reach`, `semantic/grounding-alignment`, `semantic/load-bearing-qualifiers`, and `prose/pseudo-formalism`; kept only pseudo-formalism as a target-side rationale candidate.
- `rg -n 'reach assessment|proof obligations|proof obligation|causal invariance|causal mechanism|formal obligation|formal consequence|symbolic systems|symbolic system|causal/proof|causal and proof|prose remains LLM-mediated' kb/notes kb/reference kb/instructions kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` -- confirmed existing inbound links from `definitions/reach-assessment.md`, `goedel-machines-are-a-proof-governed-case-of-self-modification.md`, `self-improving-systems-README.md`, and the causal-source ingest reports; no new source-evidence edge exceeded the existing source set.
- `rg -n 'oracle domain|verification cost|hard oracle|soft oracle|proof-gated|formal model|formal semantics|symbolic artifact' kb/notes kb/reference kb/instructions --glob '*.md'` -- found the oracle-strength cluster and codification cluster. Kept oracle-strength, automation-boundary, codify-vs-LLM, semantic-review, prompt-variation, and known-target-discovery candidates; rejected error-correction and reliability-dimensions as too broad.
- `rg -n 'reach assessment|causal reach|proof obligation|proof-gated|causal inference|invariant prediction|formal symbolic|formal route|checkable obligation|oracle|verification cost|hard oracle|formal verifier|causal discovery|counterfactual generalization' kb/sources/ --glob '*.md'` -- reviewed `agentic-code-reasoning.ingest.md`, `can-llm-agents-infer-world-models-agentic-automata-learning.ingest.md`, `superarc-ait-benchmark-llm-compression-abstraction.ingest.md`, and `pathway-beyond-transformers-sudoku-bench.ingest.md`; all were rejected as hard-oracle or structured-reasoning evidence rather than direct causal/proof reach-assessment grounding.
- `rg -n 'reach assessment|causal reach|proof obligation|proof-gated|causal inference|invariant prediction|formal symbolic|formal route|checkable obligation|oracle|verification cost|hard oracle|formal verifier|causal discovery|counterfactual generalization' kb/agent-memory-systems/ --glob '*.md'` -- kept Decapod as a sparse `see-also` candidate because it implements proof gates in a reviewed governance system; rejected extraction-oracle hits.

**Link following:**
- Followed existing target links to [Reach assessment](../../../../notes/definitions/reach-assessment.md), [Goedel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md), [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), and the causal/proof source ingests. These are already encoded and were not repeated as new connections.
- Followed oracle-cluster links through [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), and [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md). These passed because the source supplies the reach-assessment instance those broader notes need: a judgment becomes automatable only after the claimed generality is represented as a checkable consequence.
- Followed evaluation-neighbor links through [Semantic review catches content errors that structural validation cannot](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md), [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md), [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md), and [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md). Kept the first three; rejected reasoning-production because its route-inspection warning is about LLM evaluators, not formal causal/proof obligations.
- Followed the instruction-side candidates [Explanatory reach gate](../../../../instructions/review-gates/semantic/explanatory-reach.md), [Grounding alignment gate](../../../../instructions/review-gates/semantic/grounding-alignment.md), [Pseudo-formalism gate](../../../../instructions/review-gates/prose/pseudo-formalism.md), and [Composition friction gate](../../../../instructions/composition-friction-gate.md). Kept only pseudo-formalism as a reverse-edge candidate; the others should point first to reach-assessment or their existing rationale notes rather than this narrower formal route.
- Followed Decapod from the agent-memory description listing. Kept as `see-also` because its workunit/proof-gate governance is a concrete external companion for proof-obligation authority, while noting it is not evidence that Decapod performs reach assessment.

## Connections Found

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **exemplifies**: the source is a worked instance of oracle hardening for reach judgments; causal invariance and proof obligations move "does this generalize?" toward checkable consequences.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **exemplifies**: the source shows the positive case where a judgment-heavy task becomes partly automatable only after the candidate's claimed generality has a verifier.
- [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) -- **exemplifies**: the source is a specific evaluation-side case of the codify-vs-LLM split: leave prose reach to semantic judgment, but route causal/proof obligations to symbolic machinery once the obligation is explicit.
- [Semantic review catches content errors that structural validation cannot](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md) -- **contrasts**: semantic review covers the prose case where no causal/proof obligation has been reduced to a formal check; the source names the boundary where symbolic machinery can take over part of that work.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- **contrasts**: both separate verification from explanatory reach, but the prompt-variation note varies prompts or explanations, while the source asks what causal/proof consequence must hold if the generalization is genuine.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -- **contrasts**: known-target benchmarks manufacture retrospective reachability oracles; the source covers prospective formal reach assessment through causal assumptions or proof obligations.
- [Decapod](../../../../agent-memory-systems/reviews/decapod.md) -- **see-also**: code-reviewed external governance system with proof gates and VERIFIED workunit transitions; useful as a practical companion for proof-obligation authority, though not evidence that Decapod assesses explanatory reach.

## Bidirectional Candidates

- [Semantic review catches content errors that structural validation cannot](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md) <-> source -- **contrasts**: the return path would help readers distinguish LLM-mediated content review from cases where the content claim has been represented as a formal obligation.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) <-> source -- **contrasts**: the return path would keep three "variation" regimes separate: prompt variation, Deutsch-style explanation variation, and formal causal/proof consequence checking.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) <-> source -- **contrasts**: the return path would prevent "reachable under a known target" from being confused with "warranted across a stated causal/proof domain."

## Reverse-edge Candidates

- [Pseudo-formalism gate](../../../../instructions/review-gates/prose/pseudo-formalism.md) -> source -- **rationale**: the gate asks whether notation or formal-looking decomposition derives a non-obvious consequence; this source supplies the theory-side account of what non-decorative formalization buys when it creates causal or proof obligations.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reach assessment](../../../../notes/definitions/reach-assessment.md) -- already bidirectionally encoded: the source links to the definition and the definition links back to the developed formal-route argument.
- [Goedel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) -- already encoded from both sides; no new candidate beyond the existing proof-gated placement.
- [Codification](../../../../notes/definitions/codification.md) -- conceptual overlap, but the source does not use the codification vocabulary directly and already links [Representational form](../../../../notes/definitions/representational-form.md); adding this would import a broader learning-theory frame without a reader need specific to the source's claim.
- [Constraining](../../../../notes/definitions/constraining.md) -- rejected for the same reason as codification: formal reach obligations can be read as constraining, but the source's active distinction is reach-assessment route by representational form.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- broad oracle machinery; the source does not discuss repeated checks, decorrelation, or amplification.
- [Reliability dimensions map to oracle-hardening stages](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) -- broad oracle-hardening taxonomy; no specific connection to causal/proof reach obligations beyond shared "oracle" vocabulary.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- useful evaluation warning, but it concerns LLM reviewers substituting answer reconstruction for route inspection, not formal systems assessing reach.
- [Agentic Code Reasoning ingest](../../../../sources/agentic-code-reasoning.ingest.md) -- semi-formal LLM verification evidence, not a formal symbolic reach-assessment route; it remains better connected through oracle-strength and structured-reasoning notes.
- [Can LLM Agents Infer World Models ingest](../../../../sources/can-llm-agents-infer-world-models-agentic-automata-learning.ingest.md) -- hard-oracle automata benchmark with exact feedback, but it tests interactive world-model inference rather than the source's causal/proof assessment of a claim's generality.
- [SuperARC ingest](../../../../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) -- hard-oracle symbolic-method benchmark; relevant to transformer limits and adaptive-fit-vs-reach, but not specific enough to formal reach assessment.
- [Pathway/Sudoku Bench ingest](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) -- constraint-satisfaction benchmark and vendor evidence for symbolic/architectural limits; too distant from causal/proof obligations over retained claims.

## Index Membership

- [Evaluation](../../../../tags/evaluation-README.md) -- candidate curated-head membership: the source supplies the formal reach-assessment side that complements the current prompt-variation and soft-oracle evaluation entries.
- [Computational model](../../../../tags/computational-model-README.md) -- candidate curated-head membership: the source is already tagged `computational-model` and would fit as a bridge from representational form to which substrate can perform which evaluation work.
- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- already present; no action required.

## Synthesis Opportunities

The source, [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md), [Semantic review catches content errors that structural validation cannot](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md), and [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) imply a useful evaluator taxonomy: formal-obligation verifiers, retrospective target oracles, and semantic-judgment oracles answer different "does this generalize?" questions and should not be treated as one reach-assessment capability.

## Maintenance Observations

None

## Flags

None
