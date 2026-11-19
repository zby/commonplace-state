---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.md"
source_has_frontmatter: true
date: "2026-06-17"
depth: standard
---

# Connection Report: An Enigma of Artificial Reason

**Source:** [An Enigma of Artificial Reason](../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.md)

## Discovery Trace

**Description listing scan:**
- Read `kb/sources/COLLECTION.md`; snapshots are immutable and active links belong in the matching ingest report. Authorised destinations scanned: `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`; `work` and `instructions` are excluded.
- Read destination heads: `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The notes collection is the primary fit; reference and related-system collections had no durable-system target for this paper.
- Ran `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md' | rg -i 'reason|evaluat|judge|faithful|verification|validation|critic|review|rubric|bias|harness|agent|memory|learning'`. Kept the evaluation/oracle cluster; rejected broad memory-system reviews and shipped-reference docs as scope-adjacent but not claim-bearing targets for this source.

**Topic indexes:**
- Read `kb/notes/evaluation-README.md`; the paper belongs near prompt/judge evaluation work because it supplies a benchmark where evaluator models miss reasoning flaws behind valid answers.
- Identified `kb/notes/llm-interpretation-errors-README.md` and `kb/notes/learning-theory-README.md` as possible index memberships from tag naming and description search. Did not edit either index.

**Body search:**
- `rg -n "production-evaluation|generation-verification|verification|evaluation|judge|reasoning evaluation|answer confirmation|confirmation bias|process reward|outcome|valid answer|invalid reasoning|epistemic vigilance|critique|critic|oracle" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'` surfaced the oracle-strength, error-correction, automation-boundary, semantic-review, topology/isolation/verification, and agentic-system judge-loop clusters.
- `rg -n "GSM-DC|distracted|irrelevant context|reasoning.*content|human.*reasoning|content effects|process structure|output structure|validity|rubric|judge" kb/notes kb/sources --glob '*.md'` surfaced `process-structure-and-output-structure-are-independent-levers.md` and `human-writing-structures-transfer-to-llms-because-failure-modes.md` as stronger fits than generic reasoning notes.
- `rg -n "quality.*gate|review.*gate|semantic.*review|accepted edit|judge calibration|manual error analysis|automation|oracle" kb/notes kb/reference kb/instructions --glob '*.md'` surfaced the Commonplace review/evaluation loop. Kept semantic-review and evaluation-automation notes; rejected implementation-specific review architecture docs because the paper does not describe Commonplace internals.

**Link following:**
- Followed from [oracle-strength-spectrum](../../../../notes/oracle-strength-spectrum.md) to [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), and [the-boundary-of-automation-is-the-boundary-of-verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md). These form the cleanest landing area: the paper supplies empirical evidence that answer validity can destroy evaluator discrimination even when generation is strong.
- Followed from [process-structure-and-output-structure-are-independent-levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) to [human-writing-structures-transfer-to-llms-because-failure-modes](../../../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md). The paper adds a human-vs-LRM comparison where humans retain more reasoning-evaluation ability, while LRMs lean on answer production.
- Followed source-to-source through [Autoreason ingest](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md): Autoreason frames a generation-evaluation gap in self-refinement, while this paper isolates a sharper reasoning-production/evaluation gap.

## Connections Found

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **evidence**: the VAIR benchmark is a concrete soft-oracle failure where answer correctness looks like a verifier but lacks reasoning-validity discrimination.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **evidence**: the paper demonstrates a correlated judge failure mode: LRMs and PRMs can share answer-validity bias, so repeating or training evaluators around answer-reaching signals may not decorrelate checks.
- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- **evidence**: VAIR separates high production accuracy from poor per-instance evaluation discrimination, directly supporting the note's accuracy-vs-discrimination distinction.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **evidence**: the source shows why stronger generation alone cannot automate reasoning assessment; verification needs its own training/evaluation surface.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- **evidence**: the paper isolates final-answer validity from step-validity, giving a clean example where output correctness and process correctness diverge.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **evidence**: the source both supports and limits the human-overlap claim: humans and LRMs can share some evaluation biases, but humans show a much smaller production-evaluation gap.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- **evidence**: the PRM appendix warns that process-supervision labels derived from answer-reaching rollouts can automate the wrong evaluator unless failure modes are understood first.
- [Semantic review catches content errors that structural validation cannot](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md) -- **evidence**: VAIR's missing-reasoning and shuffled-reasoning cases are the math analogue of structurally plausible content whose semantic invalidity requires step-level review.
- [Autoreason ingest](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md) -- **compares-with**: both sources examine generation-evaluation gaps, but Autoreason contributes a comparative judging architecture while this paper contributes a benchmark and mechanistic account of answer-confirmation bias.

## Bidirectional Candidates

- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) <-> source -- **evidence**: the note should cite this source as a direct empirical case where capability/accuracy and evaluator discrimination split.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) <-> source -- **evidence**: the note should cite VAIR as a cleaner example than GSM-DC for separating answer/output validity from reasoning/process validity.

## Reverse-edge Candidates

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -> source -- **evidence**: add as a concrete example of a misleading soft oracle: final-answer validity is cheap but not faithful to reasoning validity.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -> source -- **evidence**: add under correlated-error sources because answer-confirmation bias appears in LRMs and PRMs.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -> source -- **evidence**: add as scientific-paper support for the warning that automated judge labels can inherit generator failure modes.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Agent memory systems comparative review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) -- rejected: the paper is about reasoning evaluation, not memory architecture; any relevance is through evaluation policy notes already captured.
- [Review architecture](../../../../reference/review-architecture.md) -- rejected: Commonplace's review subsystem is an implementation surface, while the source supplies theory/evidence for verifier design.
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) -- rejected as a direct connection: the paper strengthens judge-discrimination concerns, but it does not propose KB-quality signals or graph-neighborhood evaluation.
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) -- rejected as a direct connection: the source is compatible with the verification-decorrelation argument, but does not test context isolation or task topology.

## Index Membership

- [Evaluation](../../../../tags/evaluation-README.md) -- the source is useful evidence for judge reliability and evaluation design.
- [LLM interpretation errors](../../../notes/llm-interpretation-errors-README.md) -- the answer-confirmation mechanism is a model reasoning/evaluation error.
- [Learning theory](../../../../tags/learning-theory-README.md) -- the PRM appendix is relevant to learning signals and outcome-biased evaluator training.

## Synthesis Opportunities

- A possible note: "Reasoning production is not reasoning evaluation." It would connect VAIR to the automation-boundary, process/output split, and semantic-review notes, arguing that systems must explicitly train or construct evaluators for process validity rather than relying on answer production as a proxy.
- A possible update to the oracle cluster: final-answer validity can be a high-accuracy, zero-discrimination oracle for reasoning validity. This sharpens the existing TPR/FPR vocabulary with a concrete failure mode.

## Maintenance Observations

None

## Flags

- The source is a strong promotion candidate for the evaluation/oracle cluster, but the snapshot is an arXiv HTML conversion and should be treated as preprint-tier evidence.
