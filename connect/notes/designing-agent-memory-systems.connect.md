---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/designing-agent-memory-systems.md"
source_has_frontmatter: true
date: "2026-04-24"
depth: standard
---

# Connection Report: Designing Agent Memory Systems

**Source:** [Designing Agent Memory Systems](../../../../notes/designing-agent-memory-systems.md)

## Discovery Trace

**Source and rules read:**
- Read the source note fully. The current claim is a needs map for ideal-but-realistic agent memory systems: direct memory creation first, trace-derived extraction as meta-learning, activation before mistakes, promotion by future value, authority, lifecycle, and evaluation by effects.
- Read [notes collection rules](../../../../notes/COLLECTION.md). Authorised destinations are `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/sources/`, and `kb/instructions/`; links into `kb/work/` are excluded. Authorised labels for note-to-note edges include `grounds`, `extends`, `mechanism`, `contrasts`, and related note labels. Authorised labels for sources and agent-memory reviews include `evidence`, `derived-from`, and `see-also`.

**Indexes read:**
- Read [notes directory index](../../../notes/dir-index.md). Kept candidates around deploy-time learning, source tracking, artifact placement, always-loaded context, quality signals, and specification strategy.
- Read [learning theory index](../../../notes/learning-theory-index.md). Kept [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md), [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md), and [System-definition artifacts are crystallized reasoning under context scarcity](../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context-scarcity.md).
- Read [architecture index](../../../notes/architecture-index.md). Kept [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) as a mechanism for activation and compiled behavior-shaping surfaces.
- Read [observability index](../../../notes/observability-index.md). Confirmed the source already carries the silent-failure and behavioral-evaluation thread through existing links and prose; kept [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) as a broader evaluation companion.
- The existing source footer already links the most relevant external evidence from `kb/sources/` and the aggregate trace-derived systems survey in `kb/agent-memory-systems/`.

**Body searches run:**
- `rg -n "direct author|direct.*memory|memory creation|meta-learning|missed memory|trace-derived|session.*extract|proceduralization|procedural memory|compiled view|source of truth|behavioral faithfulness|WITH/WITHOUT|promotion|retirement|lifecycle" kb/notes kb/agent-memory-systems kb/sources --glob '*.md'`
- `rg -n "AGENTS\\.md|always-loaded|control plane|generated instruction|instruction generation|skill|plugin|runtime extension|guardrail|guard" kb/notes kb/reference kb/agent-memory-systems --glob '*.md'`
- `rg -n "quality score|stale|retire|superseded|source tracking|Distilled into|compiled|regeneration|provenance" kb/notes kb/reference kb/agent-memory-systems --glob '*.md'`

**Candidate reads and link following:**
- Read [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md), [System-definition artifacts are crystallized reasoning under context scarcity](../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context-scarcity.md), [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), [Distilled artifacts need source tracking at the source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md), [Capability placement should follow autonomy readiness](../../../../notes/capability-placement-should-follow-autonomy-readiness.md), [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md), and [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md).
- Followed the source's existing links through deploy-time learning, readable-artifact continual learning, scheduler/LLM separation, spec mining, trace-derived techniques, and the agent-memory crosscutting note. These already cover the base argument; the useful additions are the more specific mechanism notes below.

## Connections Found

- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **grounds**: the source treats memory as behavior change across prose, symbolic, and possibly opaque substrates; this note gives the substrate-level frame.
- [System-definition artifacts are crystallized reasoning under context scarcity](../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context-scarcity.md) -- **grounds**: the source's procedural-memory framing depends on the idea that tips, playbooks, instructions, tests, and tools are pre-compiled reasoning that changes future action under bounded context.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) -- **mechanism**: the source's direct-memory versus trace-derived meta-learning split maps to when understanding is available: before execution, during execution, or only after observing runs.
- [Capability placement should follow autonomy readiness](../../../../notes/capability-placement-should-follow-autonomy-readiness.md) -- **mechanism**: the source's promotion destinations need a placement rule for deciding whether a learned capability belongs as a note, instruction, skill, script, plugin, or guardrail.
- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- **mechanism**: the source's activation and authority needs depend on knowing which behavior-shaping surfaces are always loaded, invoked by capability, injected by configuration, or generated from memory.
- [Distilled artifacts need source tracking at the source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md) -- **mechanism**: the source's source-of-truth and compiled-view drift section needs the source-side tracking rule for derived cues, instructions, generated reminders, and other distilled memory surfaces.
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) -- **extends**: the source evaluates memory by effects; this note develops weak composite signals that could support lifecycle, promotion, and maintenance decisions when perfect usage oracles are absent.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Capability placement should follow autonomy readiness](../../../../notes/capability-placement-should-follow-autonomy-readiness.md) -> source -- **extends**: a future revision could cite the memory-system note as a larger application of the autonomy-readiness placement rule to memory promotion.
- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -> source -- **extends**: a future revision could cite the memory-system note as the lifecycle and authority problem created when always-loaded surfaces become compiled memory.
- [Distilled artifacts need source tracking at the source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md) -> source -- **exemplifies**: a future revision could cite the memory-system note as a case where source-side tracking prevents generated memory surfaces from becoming independent policy.

## Off-authorisation Candidates

- Workshop artifacts under `kb/work/` are relevant because this note came from a workshop pass, but `kb/notes/COLLECTION.md` explicitly excludes links into the workshop layer. No work links proposed.

## Raw Text Candidates

None

## Rejected Candidates

- [Stale indexes reduce discovery when they suppress fallback search](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) -- relevant to lifecycle and drift, but narrower than [Distilled artifacts need source tracking at the source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md) for this note's compiled-memory concern.
- [AGENTS.md should be organized as a control plane](../../../../notes/agents-md-should-be-organized-as-a-control-plane.md) -- relevant to one possible behavior-shaping surface, but [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) covers the broader activation surface family.
- [Instruction specificity should match loading frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md) -- relevant to procedural memory quality, but too specific for the current needs map.
- Individual external memory-system reviews were not added because [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) is already linked and is the cleaner aggregate traversal target.

## Index Membership

None. The note already appears in the generated learning-theory index. The new links do not require a tag change or generated index update.

## Synthesis Opportunities

- **Direct memory creation as the base case, trace mining as meta-learning:** the source, [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md), and [Capability placement should follow autonomy readiness](../../../../notes/capability-placement-should-follow-autonomy-readiness.md) together imply a focused note on choosing the artifact destination at the moment understanding becomes available.
- **Compiled memory surfaces need source authority:** the source, [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), and [Distilled artifacts need source tracking at the source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md) imply a focused note on generated reminders, cues, instructions, and guards as compiled views rather than independent policy.

## Maintenance Observations

None.

## Flags

- Load-bearing candidate relationships point to `status: seedling` notes: [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md), [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), and [Distilled artifacts need source tracking at the source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md). Use them as mechanism links with awareness that they are still developing.
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) is `status: speculative`, so it is recommended as an `extends` edge rather than a grounding premise.
