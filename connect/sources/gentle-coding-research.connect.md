---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/gentle-coding-research.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: Comparative Research: Emotional Prompting, Stress & Sycophancy

**Source:** [Comparative Research: Emotional Prompting, Stress & Sycophancy](../../../../sources/.snapshots/gentle-coding-research.md)

## Discovery Trace

**Collection contract and authored-surface reads:**

- Read `kb/sources/COLLECTION.md`: snapshots are immutable local inputs, and their active outbound surface is normally the matching ingest. The current companion is [Gentle-Coding](../../../../sources/gentle-coding.ingest.md), a three-snapshot ingest that explicitly includes `gentle-coding-research.md`. For source-to-note candidates the relevant authorised labels are `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, and sparse `see-also`; source-to-source and source-to-agentic-system comparisons may use `compares-with` or sparse `see-also`; reference accepts only sparse `see-also`.
- Read `kb/notes/COLLECTION.md` for reverse-edge rules. Notes may point to a durable source ingest with `evidenced-by`, `derived-from`, `abstracted-from`, or sparse `see-also`, but they must not author durable links to `.snapshots/`.
- Read `kb/cache/types/connect-report.md` for the report contract and template.
- The source has frontmatter but no `tags:` field, so no tag README or by-tag `rg` pass applied.

**Curated heads and full title surfaces:**

- Read [notes README](../../../../notes/README.md), [reference README](../../../../reference/README.md), [agent-memory systems README](../../../../agent-memory-systems/README.md), [agentic systems README](../../../../agentic-systems/README.md), and [sources README](../../../../sources/README.md).
- Generated each complete destination title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources` (360, 141, 173, 12, and 296 headings respectively at discovery time).
- The title scan surfaced prompt-variation, evaluation, context-contamination, human/LLM-transfer, and sibling-source candidates in notes and sources. Reference titles described Commonplace itself, agent-memory titles described retained-memory implementations, and agentic-system titles described harnesses; none matched the source's emotional-prompting or sycophancy claim closely enough to justify broad prospecting there.

**Description listing scan:**

- Ran `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'emotion|prompt|sycoph|pressure|stress|anxi|human[- ]in[- ]the[- ]loop|runaway|over[- ]?reason|compliance|framing|dialog|robust|reliab|judge|bias|underspec'` separately over all five authorised local destinations.
- In notes this flagged [context contamination operates below an agent's compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md), [evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md), prompt-variation notes, and the psychology-transfer note. The first two were kept as new comparisons; the prompt-variation and psychology-transfer links were already represented in the authored companion or failed the source-strength test.
- In sources this flagged [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md), [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md), semantic leakage, chain-of-thought faithfulness, and evaluator-calibration sources. The human/LLM content-effects study was kept as a methodological comparator. Prompt Stability is the closest substantive counterpart but is already linked from the companion ingest.
- The reference and agentic-system description passes returned no plausible direct candidate. Agent-memory descriptions only surfaced ordinary prompt injection and emotional metadata in memory systems, not emotional framing or sycophancy as an interaction failure, so that destination was rejected at the collection level.

**Body search:**

- `rg -n -i 'sycoph|agreement pressure|user agreement|opinion flip|adulation|user beliefs|social bias' kb/notes/ --glob '*.md'` returned no note-body match. This confirmed that the KB has no dedicated sycophancy claim to receive an evidence edge.
- `rg -n -i 'emotional prompt|emotion(al)? framing|prompt tone|prompt framing|authoritarian|coerc|warm prompt|low-stakes|safety-token|fallback token' kb/notes/ --glob '*.md'` surfaced prompt variation, PromptSE citations, and adjacent context-pressure notes. The direct PromptSE-backed note already cites the primary paper and does not benefit from this unverified bibliography as an additional source.
- `rg -n -i 'human[- ]in[- ]the[- ]loop|automated (benchmark|evaluation|evaluator)|llm[- ]as[- ]a[- ]judge|evaluator model|judge calibration|human perception|peer pressure|group dynamics|multi-agent.*bias' kb/notes/ --glob '*.md'` identified the evaluation-comprehension note as the closest local interpretation of the source's “missing human-in-the-loop” and evaluator-model-bias entries.
- The same three query families over `kb/sources/` surfaced Prompt Stability, semantic leakage, human/LLM content effects, chain-of-thought faithfulness, and the existing Gentle-Coding ingest. Searches over `kb/reference/`, `kb/agentic-systems/`, and `kb/agent-memory-systems/` produced no more specific candidate than the note/source cluster.
- `rg -n -i 'over[- ]?thinking|over[- ]?reason|infinite (validation|loop)|commitment failure|path[- ]finding failure|reasoning breakdown|hallucination.*pressure|factual drift' kb/notes/ kb/sources/ --glob '*.md'` found the over-reasoning/fallback formulation only in the companion Gentle-Coding ingest, not in an independent local target.

**Candidates loaded and evaluated:**

- Loaded [context contamination operates below an agent's compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) -- kept as `compares-with`: the source's agreement-pressure and context-window-sycophancy leads describe a social/relational route to stance drift, while the note gives a controlled local case where stance influence survived detection and refusal. The comparison is useful precisely because it does not assert that both share a proven mechanism.
- Loaded [evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- kept as `compares-with`: the source flags missing human perception and potentially sycophantic evaluator models; the note explains why observed failure analysis and judge calibration must precede automated optimization.
- Loaded [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) -- kept as `compares-with`: it is a grounded human/LLM comparison with explicit convergences and divergences, providing a methodological counterpoint to this source's broad three-layer human/LLM mapping.
- Loaded [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) -- not repeated as a new connection because the companion Gentle-Coding ingest already authors this exact controlled-counterpart comparison.
- Loaded [psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) and [systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- both are already linked and discussed in the companion ingest; the Research snapshot itself is a lead list and does not add evidence for either claim.
- Loaded [prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md), [out-of-spec output is a failure of the interpreter, not the spec](../../../../notes/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md), [Semantic Leakage in Language Models](../../../../sources/semantic-leakage-lms-gonen.ingest.md), and [REM](../../../../agent-memory-systems/reviews/REM.md) -- rejected for the reasons recorded below.

**Link following:**

- Followed the context-contamination note to semantic leakage, human/LLM content effects, flat-context composition, and orchestration/isolation notes. This established the controlled stance-drift cluster but did not license treating the bibliography's sycophancy summaries as evidence for the mechanism.
- Followed the evaluation-comprehension note to oracle discrimination, error correction, automation boundaries, and its calibrated-evaluator sources. These supported a comparison edge but showed why an `is-evidence-for` edge would overstate an unverified bibliography.
- Followed the Prompt Stability and human/LLM content-effects ingests through their existing note connections. Prompt Stability remained the closest empirical counterpart but is already present in the companion ingest; content effects remained the strongest new source-to-source comparison.

**External destination:**

- Open-web prospecting was skipped as required. The original Gentle-Coding URL and the bibliography's external links are already embedded in the snapshot; no additional external target was supplied. The existing links are leads to verify independently, not candidate edges to re-author from an immutable snapshot.

## Connections Found

- [context contamination operates below an agent's compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) -- **compares-with**: the bibliography's agreement-pressure and long-context sycophancy leads describe relational routes to stance drift, while the note records a controlled case of fine-grained stance influence that persisted despite explicit detection and refusal; comparison helps distinguish social agreement pressure from generic non-selective context integration.
- [evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- **compares-with**: the bibliography's multi-agent layer flags missing human perception in sycophancy benchmarks and evaluator models that may reproduce the bias they judge, while the note explains the need for observed-failure analysis and calibrated judges before automated evaluation can be trusted.
- [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) -- **compares-with**: both organize model behavior against human cognitive phenomena, but the peer-reviewed content-effects study explicitly measures where human and model patterns converge and diverge, providing a grounded methodological comparator for this bibliography's broader human/LLM layer mapping.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) -- strongest empirical comparison, but already explicitly authored in the companion [Gentle-Coding ingest](../../../../sources/gentle-coding.ingest.md); repeating it would leave no future action.
- [psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) -- already mapped from the companion ingest, and the target's human/LLM parallels are unverified summaries rather than per-principle failure-mode evidence.
- [systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- already mapped from the companion ingest; the bibliography lists studies but does not itself run or report a controlled prompt-variation protocol.
- [prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) -- the source catalogs prompt effects; it does not select a framing against a fixed, human-verified target or isolate framing as the only varied factor.
- [out-of-spec output is a failure of the interpreter, not the spec](../../../../notes/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) -- already cites the controlled PromptSE paper directly; routing through this secondary, unverified bibliography would reduce evidentiary fidelity.
- [Semantic Leakage in Language Models](../../../../sources/semantic-leakage-lms-gonen.ingest.md) -- both involve contextual influence, but semantic leakage tests unrelated prompt-to-generation associations, whereas the source catalogs social agreement and emotional framing; the shared mechanism is not established by this artifact.
- [REM](../../../../agent-memory-systems/reviews/REM.md) -- its stored `emotion` signal is extracted metadata for ranking and consolidation, not evidence about emotional prompts, model stress, or sycophancy.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- The source-preserved tables contain malformed rows: “Controllable Emotion Generation via Emotion Vectors” lacks a closing table delimiter, and “Hallucination to Truth: Fact-Checking Review” lacks the opening delimiter. The snapshot is immutable; a future recapture should verify whether these defects remain upstream rather than repairing them locally.

## Flags

- This artifact is an annotated lead list, not verified evidence. The companion ingest explicitly warns that several citations may be future-dated, implausible, or otherwise unconfirmed. Accordingly, all retained candidates use `compares-with`; no `is-evidence-for`, `abstracted-from`, or reverse `evidenced-by` candidate is warranted until an underlying primary source is independently captured and checked.
