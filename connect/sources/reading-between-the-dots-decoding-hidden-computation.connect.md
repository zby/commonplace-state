---
description: "Discovery report for connections from the filler-token hidden-computation paper"
type: kb/cache/types/connect-report.md
source: "kb/sources/reading-between-the-dots-decoding-hidden-computation.md"
source_has_frontmatter: true
date: "2026-07-18"
depth: standard
---

# Connection Report: Reading Between the Dots

**Source:** [Reading Between the Dots: Decoding Hidden Computation across Filler Tokens](../../../sources/reading-between-the-dots-decoding-hidden-computation.md)

## Discovery Trace

**Description listing scan:**
- Scoped `rg "^description:.*(reason|oracle|verif|process|monitor|observ|interpret)" kb/notes --glob '*.md'` -- retained `oracle-strength-spectrum.md`, `reasoning-production-is-not-reasoning-evaluation.md`, `diagnostic-richness-constrains-outer-loop-learning-quality.md`, and `an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md`; rejected broader interpretation-error notes whose claims concern prompt compliance rather than internal computation.

**Topic indexes:**
- Read `kb/notes/observability-README.md`, `kb/notes/evaluation-README.md`, and `kb/notes/llm-interpretation-errors-README.md`. The observability index is the strongest prospective membership because the paper recovers hidden execution state; the oracle index supplies the verification framing. The evaluation index is too operationally focused for direct membership.

**Body search:**
- `rg -i "chain.of.thought|cot monitor|faithful|hidden computation|filler token|pause token|residual stream|mechanistic interpret" ...` -- found the close source companion `verbalizable-representations-global-workspace-llms.ingest.md` and broad faithfulness material; retained only the former because it studies causally relevant, verbalizable residual-stream state.
- `rg --files kb/notes | rg '(reasoning|oracle|verification|process-structure|automation-boundary|observability|interpret)'` -- identified the candidate note cluster and exposed `process-structure-and-output-structure-are-independent-levers.md`; rejected that note as a direct edge because its distinction concerns authored constraints, not observability of a latent process.
- `rg -i "filler.token|hidden reasoning|hidden computation|chain.of.thought monitor|mechanistic interpretability|residual stream" kb/sources --glob '*.md'` -- found no prior filler-token source, but found the J-space paper and its ingest.

**Link following:**
- Followed the neighborhoods of `oracle-strength-spectrum.md`, `reasoning-production-is-not-reasoning-evaluation.md`, and `diagnostic-richness-constrains-outer-loop-learning-quality.md`. The paper supplies a new observation channel for process verification and richer failure diagnosis, but does not show that its monitor can verify free-form arguments or adversarial intent.
- Read `verbalizable-representations-global-workspace-llms.ingest.md`. Both sources decode and causally intervene on verbalizable hidden state; this paper adds filler-position ordering and a label-free aggregation pipeline, while using a coarser logit-lens instrument on narrower tasks.

## Connections Found

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **evidence**: the paper manufactures a discriminative soft oracle by changing the observation surface from content-free output tokens to internal residual states, recovering named intermediates at 80-95% accuracy on its tested tasks.
- [An outcome check licenses replay; a rule needs the process verified](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -- **evidence**: residual decoding separates retrieval failures from composition failures even when both produce the same outcome class, demonstrating the additional discrimination available from process-level evidence.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **evidence**: hidden-state traces reveal which intermediate was present or absent, providing diagnostic information that final-answer correctness cannot supply.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- **see-also**: the paper supplies a possible mechanistic observation channel for route inspection, but only for discrete, nameable intermediates rather than the free-form entailment failures that note addresses.
- [Ingest: Verbalizable Representations Form a Global Workspace in Language Models](../../../../sources/verbalizable-representations-global-workspace-llms.ingest.md) -- **compares-with**: both studies read causally relevant verbalizable content from residual states; J-space uses a Jacobian-derived lens across broader concepts, while this paper localizes task intermediates across filler positions and aggregates logit-lens readouts without labels.

## Bidirectional Candidates

- [Ingest: Verbalizable Representations Form a Global Workspace in Language Models](../../../../sources/verbalizable-representations-global-workspace-llms.ingest.md) <-> source -- **compares-with**: readers of either interpretability source benefit from seeing the trade between broader concept readout and narrower temporal localization.

## Reverse-edge Candidates

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -> source -- **evidence**: add the paper as a worked example of oracle manufacturing by instrumenting a previously opaque execution substrate.
- [An outcome check licenses replay; a rule needs the process verified](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -> source -- **evidence**: add empirical support that internal process evidence can distinguish retrieval from composition failure beyond an outcome check.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -> source -- **evidence**: add a model-internal case where richer traces identify the stage of failure.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- rejected as a direct edge: content-free output coexisting with structured latent computation resembles the title, but the note is specifically about independently constraining authored process and result formats.
- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- rejected as direct evidence: the decoder has useful task-level accuracy, but the paper does not report the per-instance TPR/FPR or escalation behavior needed to ground that note's discrimination claim.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) -- rejected because the paper partially instruments a distributed-parametric artifact rather than making it inspectable in the stable, diffable sense claimed by the note.

## Index Membership

- [Observability](../../../../tags/observability-README.md) -- a future promoted note about representation-relative monitorability would belong here; the immutable source itself is not a note-index member.
- [LLM interpretation errors](../../../notes/llm-interpretation-errors-README.md) -- the source strengthens the process-oracle branch, especially where outcome checks cannot diagnose the failing intermediate.

## Synthesis Opportunities

Together, this paper, [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), and the [J-space ingest](../../../../sources/verbalizable-representations-global-workspace-llms.ingest.md) imply that monitorability is relative to an observation surface: an explanation channel may be opaque while an internal-state channel remains discriminative. This is narrower than claiming that hidden reasoning is generally auditable, because both interpretability methods are partial and require white-box access.

## Maintenance Observations

None

## Flags

- The synthesis must retain the open-weight and discrete-intermediate boundary; neither paper establishes robust monitoring of deceptive, adversarially obfuscated, or non-verbal computation.
