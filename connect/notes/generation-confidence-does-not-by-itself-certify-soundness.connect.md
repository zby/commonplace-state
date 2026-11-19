---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/generation-confidence-does-not-by-itself-certify-soundness.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Generation confidence does not by itself certify soundness

**Source:** [Generation confidence does not by itself certify soundness](../../../../notes/generation-confidence-does-not-by-itself-certify-soundness.md)

## Discovery Trace

### Authorisation and source framing

- Read `kb/notes/COLLECTION.md`. It authorises prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; it excludes `kb/work/`. `external` is authorised but is not a prospecting surface. Labels were filtered per source→destination pair. The instruction collection's usual inverse direction was treated as a first-class reverse-edge pass.
- Read the source in full after copyediting. Its deductive claim is that next-token probability and factual or inferential soundness are different properties, so the former does not certify the latter. Its empirical claims are narrower: their association can have any direction over a declared population; confidence can support triage after task-specific calibration and discrimination are established; and the reliability of separately trained probes remains open.
- Existing source links were recorded rather than re-proposed: [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md), [Reliability dimensions map to oracle-hardening stages](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md), and [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md).

### Notes

- Curated heads read: `kb/notes/README.md`, `kb/notes/learning-theory-README.md`, `kb/notes/failure-modes-README.md`, and `kb/notes/llm-reliability-README.md`. None of the three tag heads declares `complete: true`; `learning-theory-README.md` declares `covered_by`, not completeness, so no tag scan was skipped.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/notes --glob '*.md'` — 354 titles inspected. Full description surface: `rg '^description:' kb/notes --glob '*.md'` — 351 description lines inspected.
- By-tag scans: `rg -l '^tags:.*\blearning-theory\b' kb/notes --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` (116 tagged files); the same query was run for `failure-modes` (9 files) and `llm-reliability` (31 files). These promoted the calibration/discrimination, reasoning-evaluation, oracle-strength, and fluent-failure neighborhoods.
- Body searches: `rg -n -i '(generation confidence|token probability|next-token|logit|likelihood)' kb/notes --glob '*.md'`; `rg -n -i '(calibrat|discriminat).*(confidence|probab|correct|wrong)|(confidence|probab).*(calibrat|discriminat|correct|wrong)' kb/notes --glob '*.md'`; `rg -n -i '(soundness|factual truth|inferential validity|validity check|fluent.*false|false.*fluent)' kb/notes --glob '*.md'`; and `rg -n -i '(self-assess|internal probe|verbal.*confidence|verifier|oracle)' kb/notes --glob '*.md'`.
- Candidate evaluation: kept [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) because it develops the precise operational consequence of the source's calibration/discrimination condition; kept [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) because it develops the inferential-soundness half into a verifier-design rule; kept [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) as the neighboring distinction between an observed performance gain and identification of its cause; and kept [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) as a concrete application that already cites the source as its mechanism.
- Reverse-edge evaluation: kept [Reach-assessment](../../../../notes/definitions/reach-assessment.md) because its explicit exclusion of confidence presently asserts the source's premise without a link. No other unlinked note passed a stronger inbound articulation test.

### Types

- Curated head read: `kb/types/README.md`. Full title surface: `rg -N --no-heading -m1 '^# ' kb/types --glob '*.md'` — 10 titles inspected. Full description surface: `rg '^description:' kb/types --glob '*.md'` — 13 description lines inspected.
- Body queries `rg -l -i 'next-token|token probability|generation confidence|logit|likelihood' kb/types --glob '*.md'`, `rg -l -i 'calibrat|discriminat' kb/types --glob '*.md'`, and `rg -l -i 'soundness|inferential validity|factual truth|self-assess|internal probe' kb/types --glob '*.md'` found no contract that serves as evidence or a case for the claim. No candidate passed the `evidenced-by` trigger.

### Reference

- Curated head read: `kb/reference/README.md`. Full title surface: `rg -N --no-heading -m1 '^# ' kb/reference --glob '*.md'` — 135 titles inspected. Full description surface: `rg '^description:' kb/reference --glob '*.md'` — 133 description lines inspected.
- The same three body queries recorded under Types were run over `kb/reference`. Calibration proposals and review-system documentation describe Commonplace mechanisms; they do not test generation confidence against factual or inferential soundness. No reference candidate passed the articulation test.

### Agent-memory systems

- Curated head read: `kb/agent-memory-systems/README.md`. Full title surface: `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems --glob '*.md'` — 173 titles inspected. Full description surface: `rg '^description:' kb/agent-memory-systems --glob '*.md'` — 171 description lines inspected.
- The same three body queries recorded under Types were run over `kb/agent-memory-systems`. Reviews using uncertainty, contradiction, or confidence filters implement separate constructed signals; they do not establish what next-token probability means or when it discriminates soundness. No candidate passed the articulation test.

### Agentic systems

- Curated head read: `kb/agentic-systems/README.md`. Full title surface: `rg -N --no-heading -m1 '^# ' kb/agentic-systems --glob '*.md'` — 12 titles inspected. Full description surface: `rg '^description:' kb/agentic-systems --glob '*.md'` — 10 description lines inspected.
- The same three body queries recorded under Types were run over `kb/agentic-systems`. The only calibration/discrimination hit was an unrelated GBrain evaluation passage. No candidate passed the articulation test.

### Sources

- Curated head read: `kb/sources/README.md`; there are no matching tag READMEs. Full title surface: `rg -N --no-heading -m1 '^# ' kb/sources --glob '*.md'` — 504 titles inspected. Full description surface: `rg '^description:' kb/sources --glob '*.md'` — 440 description lines inspected.
- Body searches: `rg -l -i 'next-token|token probability|generation confidence|logit|likelihood' kb/sources --glob '*.md'`; `rg -l -i 'calibrat|discriminat' kb/sources --glob '*.md'`; `rg -l -i 'soundness|inferential validity|factual truth|self-assess|internal probe' kb/sources --glob '*.md'`; and the tighter `rg -n -i '(token[- ]level confidence|token probabilit|next[- ]token probabilit|sequence likelihood|logit.*correct|probability.*(correct|truth|valid)|likelihood.*(correct|truth|valid)|confidence.*(correct|wrong|truth|valid)|verbalized confidence)' kb/sources --glob '*.md'`.
- Candidate evaluation: kept [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../../../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.md) because it directly measures answer log-probability margins against logical correctness and belief-consistency; kept [An Enigma of Artificial Reason](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) because its controlled validity benchmark and probe failures bound the source's internal-probe possibility. Rejected the Rabanser snapshot as a direct source edge because its confidence measure is post-hoc verbal self-assessment rather than generation probability, and the source already reaches the useful calibration/discrimination result through its authored reliability-dimensions link.

### Instructions and reverse-edge pass

- Curated head and contract read: `kb/instructions/README.md` and `kb/instructions/COLLECTION.md`. Full title surface: `rg -N --no-heading -m1 '^# ' kb/instructions --glob '*.md'` — 44 titles inspected. Full description surface: `rg '^description:' kb/instructions --glob '*.md'` — 97 description lines inspected.
- The same three body queries recorded under Types were run over `kb/instructions`. [Reconstruct a note's composition friction](../../../../instructions/composition-friction-gate.md) was evaluated under the exceptional inverse `rests-on` posture, but its existing dependency on the hidden-relaxation note already supplies the procedure-specific rationale. Adding another meta-reader edge would not improve execution or review enough to justify an exceptional instruction link.

### Link following

- Followed the source's existing links. The hidden-relaxation note already links back and leads to error correction; the reliability-dimensions and verification-boundary notes both lead to the augmentation-automation, oracle-strength, and external-verifier cluster. This made oracle strength and error correction useful one-hop context but redundant direct targets.
- Followed augmentation-automation → reliability dimensions, oracle strength, error correction, and verification boundary. The focused augmentation consequence passed; its broader neighbors did not add a distinct source-reader need.
- Followed reasoning-production/evaluation → process/output structure, semantic review, composition friction, and the VAIR ingest. The reasoning-production note and VAIR ingest passed; process/output structure was rejected as a more general intervention-surface distinction.
- Followed generality → boundary abstraction, explanatory-reach, narrowing, recognition, and reverse compression. Only generality uses this source as a load-bearing mechanism and warrants the reciprocal source-side application edge.
- Followed the two source candidates' neighborhoods. The content-effects snapshot has no ingest companion; VAIR's ingest routes to oracle and reasoning-evaluation notes, confirming it is the authored, caveat-bearing surface for the probe result.

### External

- `external` is authorised but not prospectable. No user-supplied or already-loaded external target distinct from repo-local snapshots was evaluated; open-web prospecting was skipped.

## Connections Found

- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — **extends**: develops the operational consequence of the source's validation condition, distinguishing aggregate calibration from the per-instance discrimination needed for confidence-gated automation and separating self-assessment from external oracles.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) — **extends**: develops the inferential-soundness case into a verifier-design rule, showing why producing a plausible or correct answer does not establish that the model checked the supplied reasoning path.
- [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) — **contrasts**: an observed structured-prompt gain does not identify the mechanism that produced it, just as a high-probability continuation does not certify the soundness of that individual output.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — **extends**: supplies a concrete application in which careful-sounding abstract prose is typical of the register while failing to preserve claim content; that note already cites this source as the mechanism.
- [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../../../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.md) — **evidenced-by**: the study finds answer log-probability margins tend to be higher for correct answers but also rise when semantic beliefs support the presented conclusion, directly illustrating a positive yet task- and content-dependent confidence–soundness association.
- [An Enigma of Artificial Reason](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) — **evidenced-by**: VAIR separates answer correctness from reasoning validity and finds validity probes work on concordant cases but collapse on correct-answer/invalid-reasoning cases, bounding rather than resolving the possibility of a reliably probeable internal soundness signal.

## Bidirectional Candidates

- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) → source — **contrasts**: a return edge would distinguish the post-hoc verbal self-assessment measured by its Rabanser evidence from the next-token probability defined here, preventing evidence about one confidence surface from being silently generalized to the other.
- [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) → source — **contrasts**: a return edge would pair two non-certification results: prompt performance does not identify training-distribution selection, and generation probability does not certify output soundness.

## Reverse-edge Candidates

- [Reach-assessment](../../../../notes/definitions/reach-assessment.md) → source — **grounds**: its exclusion “reach-assessment is not confidence” depends on confidence and correctness coming apart; this source supplies the explicit property distinction and the requirement for separate validation.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reliability dimensions map to oracle-hardening stages](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — genuine and already linked from the source at the exact calibration/discrimination sentence; no candidate edge remains to author.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — genuine and already linked from the source's conclusion; proposing it again would duplicate graph state.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) — relevant but broader than the kept augmentation candidate and already reachable through both the reliability-dimensions and verification-boundary links.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — its TPR/FPR condition is useful only after confidence has become a validated oracle; the kept augmentation note carries that implication and links onward to error correction.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../notes/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — classifies where wrong output originates but does not further explain the relation between generation probability and soundness.
- [Towards a Science of AI Agent Reliability](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) — directly relevant to calibration and discrimination, but its post-hoc verbal confidence is not the source's defined next-token probability; the existing reliability-dimensions link already carries the qualified empirical result.
- [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — measures probability-aware performance and confidence miscalibration under prompt perturbations, not whether generation probability discriminates factual truth or inferential validity.
- [Self-training Large Language Models through Knowledge Detection](../../../../sources/self-training-large-language-models-through-knowledge-detection.ingest.md) — uses consistency, contradiction, and source-grounded filters as constructed signals; it does not test next-token confidence as a soundness signal.
- [Why You Should Almost Never Use AI to Write Anything Substantive](../../../../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) — its expert audit is a useful fluent-error case and already links to the source, but it does not measure generation probability, so it is not direct evidence for the source's central distinction.
- [Language Models Don't Always Say What They Think](../../../../sources/language-models-dont-always-say-what-they-think.ingest.md) — establishes explanation unfaithfulness under controlled biases, not a confidence–soundness relation; the kept reasoning-production note supplies the closer conceptual route.
- [Reconstruct a note's composition friction](../../../../instructions/composition-friction-gate.md) — its ban on fluent self-grading is relevant, but its existing `rests-on` edge to the hidden-relaxation note is more procedure-specific and the instruction collection requires exceptional, shallow outbound links.
- [Confidence miscalibration](../../../../instructions/review-gates/prose/confidence-miscalibration.md) — “confidence” names the assertion force of authored prose here, not token probability or model self-assessment; the match is terminological.

## Index Membership

- [LLM reliability](../../../../tags/llm-reliability-README.md) — the note supplies the base distinction beneath confidence calibration, discrimination, and external-verifier design, so it belongs in the Oracle Theory grouping.
- [Failure modes](../../../../tags/failure-modes-README.md) — the note already carries the tag and explains why fluent factual and inferential errors cannot be screened by generation confidence alone; a curated entry would make that failure mechanism navigable.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- None
