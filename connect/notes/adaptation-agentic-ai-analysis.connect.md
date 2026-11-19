---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/research/adaptation-agentic-ai-analysis.md"
source_has_frontmatter: true
date: "2026-06-23"
depth: standard
---

# Connection Report: Adaptation Signals and Retained Surfaces

**Source:** [Adaptation signals choose pressure; artifact analysis chooses the retained surface](../../../../notes/research/adaptation-agentic-ai-analysis.md)

## Discovery Trace

**Source and contract reads:**
- Read `kb/instructions/cp-skill-connect/SKILL.md`, [connect-report](../../../../types/connect-report.md), [notes collection contract](../../../../notes/COLLECTION.md), and the source note.
- Source collection authorizes note-to-note labels `extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts`, and `defined-in`; note-to-reference/source labels include `evidence`, `derived-from`, and `see-also`.

**Topic indexes:**
- `rg --files kb/notes --glob '*README.md'` -- identified [artifact-analysis](../../../../tags/artifact-analysis-README.md), [agent-memory](../../../../tags/agent-memory-README.md), [context-engineering](../../../../tags/context-engineering-README.md), [learning-theory](../../../../tags/learning-theory-README.md), and [deploy-time-learning](../../../../tags/deploy-time-learning-README.md).
- Read [artifact-analysis](../../../../tags/artifact-analysis-README.md). It declares `complete: true`; skipped a by-tag `artifact-analysis` sweep and treated the curated head as authoritative. The source has the tag but is not listed there.
- Read [agent-memory](../../../../tags/agent-memory-README.md) and [context-engineering](../../../../tags/context-engineering-README.md). Neither declares `complete: true`; both are sparse curated heads, so missing membership is an index candidate rather than a contradiction.
- Read [learning-theory](../../../../tags/learning-theory-README.md). It declares `covered_by: [deploy-time-learning, constraining, distillation, discovery, artifact-analysis, agent-memory, llm-interpretation-errors]`; because the source already carries child tags, direct listing in this parent is not needed.
- Read [deploy-time-learning](../../../../tags/deploy-time-learning-README.md). The source is relevant to deploy-time learning but does not carry that tag; no index candidate was kept for that page.

**Body search:**
- `rg -n "adaptation|artifact analysis|retained surface|retained artifact|behavioral authority|representational form|codification|relaxing|verification|WITH/WITHOUT|oracle|signal" kb/notes kb/reference kb/agent-memory-systems kb/instructions --glob '*.md'` -- broad scan was noisy but surfaced the oracle/spec-mining, readable-artifact-loop, diagnostic-richness, and memory-requirement neighborhoods.
- `rg --no-ignore -n "adaptation-agentic-ai-analysis|Adaptation signals choose pressure|Adaptation of Agentic AI|artifact-analysis|retained surface" kb --glob '*.md'` -- found existing inbound links from [storing LLM outputs is constraining](../../../../notes/selecting-an-llm-output-fixes-a-result-not-its-interpretation.md), [operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md), and [automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md); also confirmed the source is missing from the `complete: true` artifact-analysis index.
- `rg -n "accepted edit|accepted edits|user override|WITH/WITHOUT|component-counterfactual|counterfactual|adaptation event|retrieval ablation" kb/notes kb/reference kb/instructions --glob '*.md'` -- surfaced accepted-edit oracle notes, behavior-changing memory activation, the gate-learning proposal, and existing Commonplace gap-plan language around WITH/WITHOUT cue tests.

**Link following and candidate evaluation:**
- Followed source's existing artifact-analysis links to [axes of artifact analysis](../../../../notes/axes-of-artifact-analysis.md) and [memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md). Existing links cover the core taxonomy; no duplicate definition links are needed.
- Followed source's constraining/relaxing neighborhood to [spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md), [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), [codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md), and [operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md). Kept spec mining and verification-boundary as highest-value additions; rejected oracle spectrum and codification/relaxing as mostly covered by existing nearby links unless a future writer wants more theory density.
- Followed memory-evaluation candidates to [evaluate memory by effects](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md), [activate behavior-changing memory before the mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md), [use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md), and [trace-derived memory earns authority per operation, not at capture](../../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md). Kept the effect/activation notes for evaluation and the trace-authority note for signal-to-authority maturation; rejected trace-derived extraction as the broader parent already represented by the requirement comparison.
- Followed accepted-edit candidates to [an accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) and [gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md). Kept both: the note explains the signal's oracle boundary; the proposal is a concrete Commonplace design surface.
- Read [diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) and [the readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md). Kept diagnostic richness because it sharpens the report/evidence fields; rejected readable-artifact loop as a broad parent already covered through artifact-analysis and deploy-time-learning context.

## Connections Found

- [Spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md) -- **mechanism**: the source says stable adaptation pressure can move from prose reminders into validators, normalizers, schemas, and tests; spec mining is the named operation that extracts those deterministic artifacts from observed behavior.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **grounds**: the source's promotion rule depends on whether an adaptation signal has review evidence strong enough to support automation; this note grounds why verifier availability, not just update pressure, decides the viable retained surface.
- [Evaluate memory by effects, not by existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) -- **extends**: the source applies effect-based memory evaluation to adaptation events by requiring a counterfactual over the retained operative part, not merely evidence that memory was written.
- [Activate behavior-changing memory before the mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) -- **extends**: the source's cue/skill/retriever row and WITH/WITHOUT evidence requirement are the adaptation-event version of this requirement's activation-and-uptake test.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **grounds**: the source separates observed signal from retained artifact fields; diagnostic richness explains why selection signals alone are insufficient evidence for later artifact-learning loops.
- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) -- **grounds**: the source names accepted edits as distillation signals; this seedling note explains the oracle asymmetry that makes the edit strong evidence for one instance but weak evidence for a generalized rule. Flag: target is `status: seedling`, so this load-bearing label should be reviewed before authoring.
- [Trace-derived memory earns authority per operation, not at capture](../../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md) -- **grounds**: the source requires recording signal, retained surface, lineage, authority, and counterfactual; this seedling note supplies the maturation ladder that prevents captured traces from gaining rule authority before verification/distillation. Flag: target is `status: seedling`, so this load-bearing label should be reviewed before authoring.
- [Gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md) -- **see-also**: the source's accepted-edit adaptation signal has a concrete Commonplace design proposal in the review subsystem, where accepted diffs become candidate gates with promotion and rollback.

## Bidirectional Candidates

- [The adaptation survey corroborates memory requirements but misses artifact governance](../../../../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) <-> source -- **extends** from the requirement-comparison note back to this source: the comparison states the governance gap at the requirements-map level; the source supplies the operational signal-to-retained-surface table that a reader may need next.
- [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) <-> source -- **exemplifies** from the memory-design note back to this source: the source is a worked instance of applying capture, derivation, activation, authority, lifecycle, and evaluation policies after an adaptation signal fires.

## Reverse-edge Candidates

- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) -> source -- existing inline link should remain, but a future edit could update its context from "data-driven triggers for when to constrain versus relax" to "signal-to-retained-surface vocabulary for deciding what artifact changes and how it is evaluated." This is a context-refresh candidate rather than a missing edge.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- relevant background, but the source already links more directly to exact-spec/proxy-theory and relaxing-signal notes; adding both oracle spectrum and verification-boundary would likely over-densify the same reader path.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- strong conceptual neighbor, but the source already links the more actionable pair: [fixed artifacts split into exact specs and proxy theories](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) and [operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md).
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- broad parent framing; the source's specific contribution is signal-to-artifact bookkeeping, already better served by artifact-analysis and memory-evaluation links.
- [Make authority explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md) -- topical match on authority, but the source already links the behavioral-authority definition and the memory-requirements comparison; a direct link would mostly duplicate existing paths.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) -- relevant parent requirement, but the more precise source-side connection is to [trace-derived memory earns authority per operation, not at capture](../../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md).
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) -- shares oracle-hardening vocabulary, but it addresses corpus-quality signals for KB mutation loops, not adaptation-event records for retained behavior-shaping surfaces.

## Index Membership

- [artifact-analysis](../../../../tags/artifact-analysis-README.md) -- source carries `artifact-analysis`, and the README declares `complete: true`; add this note under Applications or a new "Adaptation" grouping so the completeness claim remains true.
- [agent-memory](../../../../tags/agent-memory-README.md) -- source bridges adaptation survey taxonomy to memory-system retained surfaces; consider listing it near the memory-system design entry or expanding the README's sparse "Notes" section.
- [context-engineering](../../../../tags/context-engineering-README.md) -- source explains the T2/frozen-model pattern as improvement of surrounding context artifacts: retrievers, cues, indexes, skills, validators, and prompt assembly paths.

## Synthesis Opportunities

- The source, [memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md), [trace-derived memory earns authority per operation, not at capture](../../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md), and [evaluate memory by effects](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) imply a possible "adaptation event record" design: signal, retained artifact, operative part, artifact axes, operational memory axis, authority rung, and counterfactual evaluation. This is already an open question in the source; if it recurs, promote it as a proposal rather than burying it in prose.

## Maintenance Observations

- [artifact-analysis](../../../../tags/artifact-analysis-README.md) declares `complete: true` but does not list this retagged source. This should be fixed in a future authoring pass, because agents are instructed to trust complete tag heads.
- [storing LLM outputs is constraining](../../../../notes/selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) has an existing inbound link whose context says the source "provides data-driven triggers ... for when to make the constraining decision." That is still broadly true, but it undersells the revised note's retained-surface and review-evidence frame.
- [operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) has an existing inbound link that says the source catalogues signals "in llm-do context." The revised source is no longer primarily an `llm-do` feature sketch; update the phrase when that note is next touched.
- [automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) still points to the source as "data-driven triggers for when to constrain versus when to relax." The current note is stronger: it supplies artifact-analysis bookkeeping for what retained surface changes after a learning signal.

## Flags

- The source is `status: seedling`; any new footer links should be authored conservatively.
- Two candidate targets are also `status: seedling` and are proposed with load-bearing `grounds` labels: [an accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) and [trace-derived memory earns authority per operation, not at capture](../../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md). Review target maturity before committing those as hard dependencies.
