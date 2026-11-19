---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Discoverable, composable, trusted agent memory

**Source:** [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md)

## Discovery Trace

**Scope and authorisation:**

- Read the source, `kb/cache/types/connect-report.md`, and `kb/notes/COLLECTION.md` in full before discovery. The source has frontmatter and makes a minimum-artifact-quality claim with three interdependent properties: discoverability, composability, and calibrated trust under bounded context.
- The source collection authorises prospecting in `kb/notes/`, `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`; it excludes `kb/work/`. The reserved `external` destination is authorised but was skipped because no already-known external target was supplied and open-web prospecting is forbidden.
- Read the destination heads `kb/notes/README.md`, `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. Also read the source-tag heads `kb/notes/agent-memory-README.md`, `kb/notes/context-engineering-README.md`, and `kb/notes/learning-theory-README.md`. None declares `complete: true`; `learning-theory-README.md` declares `covered_by`, not completeness, so all three by-tag searches were run.
- Read each non-source destination's `COLLECTION.md` before labeling reverse edges. No scored semantic search was used, so no candidate scores were available.

**Complete title and description surfaces:**

- Notes: `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`; `rg '^description:' kb/notes/ --glob '*.md'`.
- Types: `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'`; `rg '^description:' kb/types/ --glob '*.md'`.
- Reference: `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`; `rg '^description:' kb/reference/ --glob '*.md'`.
- Agent-memory systems: `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`; `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`.
- Agentic systems: `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`; `rg '^description:' kb/agentic-systems/ --glob '*.md'`.
- Sources: `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`; `rg '^description:' kb/sources/ --glob '*.md'`.
- Instructions: `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`; `rg '^description:' kb/instructions/ --glob '*.md'`.

**Tag description scans:**

- `rg -l '^tags:.*\bagent-memory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` surfaced the memory requirements, trace-authority, accumulation, activation, and system-design cluster.
- `rg -l '^tags:.*\bcontext-engineering\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` surfaced selection signals, retained payload, operational axes, and effect-based evaluation.
- `rg -l '^tags:.*\blearning-theory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` surfaced short composable notes, authority maturation, and the bounded-context learning frame.

**Notes body search and evaluation:**

- `rg -n -i 'discoverab|findab|addressab|usable memory|inert memory|isolated memory' kb/notes/ --glob '*.md'` kept [A retrieval miss is a local reflective-path failure](../../../../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) because it gives the path-level mechanism by which undiscovered memory becomes inert. It rejected [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) because addressability of an editable retained object is not task-time discoverability.
- `rg -n -i 'composab|combine with|coherent unit|scope.*relation' kb/notes/ --glob '*.md'` kept [Short composable notes maximize combinatorial discovery](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md) because it develops composability into a bounded-context artifact-size mechanism. It rejected [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) as a narrower retention-boundary application already reachable through the short-note and activation neighborhood.
- `rg -n -i 'trusted|trust signal|calibrated reliance|provenance|authority|warrant|lineage' kb/notes/ --glob '*.md'` kept [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) because it develops calibrated trust into an epistemic-maturity ladder. It rejected [Make Authority Explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md) because that note governs who may perform memory operations, whereas the source's trust property is calibrated epistemic reliance; a direct edge would invite role conflation.
- `rg -n -i 'bounded context|context economy|action capacity|behavior-changing|downstream effects' kb/notes/ --glob '*.md'` kept [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) because it turns the source's future-action criterion into observable tests. [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) was kept because it develops the surrounding capture, activation, authority, lifecycle, and evaluation machinery that the source explicitly separates from its artifact-quality basis.
- A focused follow-up on deterministic selection kept [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md): it explains which handles make rule-based discoverability possible and what must happen when no such signal exists.
- `rg -n -i 'loadability|artifact-level property|activation is a system-level|usable route into context|calibrated reliance|isolated memory|inert memory|access burden|transformation burden' kb/notes/ --glob '*.md'` rejected [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md): its query-system diagnostic separates finding inputs from producing an answer, while this source concerns the retained artifact's ability to enter and participate in work. Equating transformation burden with composability would blur those units of analysis.

**Other-destination body search and evaluation:**

- Types: `rg -n -i 'discoverab|composab|trusted|trust signal|provenance|authority|activation|bounded context|context economy' kb/types/ --glob '*.md'` and `rg -n -i 'title|description|tag|link|validation|review' kb/types/ --glob '*.md'` identified [Note](../../../../types/note.md). Its description, title, links, body context, review traits, and verification field concretely realize the triad, but no source→types label describes implementation; it is therefore off-authorisation in that direction and an authorised `rests-on` reverse-edge candidate. [Tag README](../../../../types/tag-readme.md) was rejected as a narrower discoverability/trusted-cache mechanism already better reached through the note type and retrieval-miss note.
- Reference: `rg -n -i 'discoverab|composab|trusted|trust signal|provenance|authority|activation|bounded context|context economy' kb/reference/ --glob '*.md'` and `rg -n -i 'agent memory|memory requirements|progressive routing|artifact quality' kb/reference/ --glob '*.md'` kept [Agent memory coverage](../../../../reference/agent-memory-coverage.md), whose coverage table explicitly maps all three properties to shipped mechanisms and limits. [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) was rejected as future design work rather than evidence of the current artifact-quality basis.
- Agent-memory systems: `rg -n -i 'discoverab|composab|trusted|trust gate|trust signal|provenance|authority|activation|bounded context' kb/agent-memory-systems/ --glob '*.md'` and `rg -n -i 'retrieval.*behavior|activation.*faith|review.*trust|trust.*review|memory quality|usable memory' kb/agent-memory-systems/ --glob '*.md'` kept [What the matrix shows across 148 agent memory systems](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) as the strongest collection-level evidence that activation and verification, not storage alone, divide systems. [sage-wiki](../../../../agent-memory-systems/reviews/sage-wiki.md) was retained only as a reverse edge because its addressable wiki, compositional ontology, and trust quarantine make the source a useful evaluation lens for that review. Individual examples such as [Cortex](../../../../agent-memory-systems/reviews/cortex.md) were rejected to avoid a broad system-review spray when the comparative analysis carries stronger aggregate signal. Existing inbound links from Pal, Phantom, Archie, A-mem, G-Memory, WeKnora, and LACP were detected and not proposed again.
- Agentic systems: `rg -n -i 'discoverab|composab|trusted|trust signal|provenance|authority|activation|bounded context|context economy' kb/agentic-systems/ --glob '*.md'` and `rg -n -i 'memory|retrieval|activation|knowledge|context' kb/agentic-systems/ --glob '*.md'` found no new candidate. [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) was rejected because it is explicitly a pre-review corpus workbench, and its retrieval-without-activation boundary is already named by its existing link to the more precise activation note.
- Sources: `rg -n -i 'discoverab|composab|trusted|trustworthiness|trust signal|inert memory|isolated memory|bounded context|action capacity' kb/sources/ --glob '*.md'` and `rg -n -i 'retrieval.*behavior|activation.*faith|review.*trust|trust.*review|memory quality|usable memory' kb/sources/ --glob '*.md'` kept [Ingest: Memory Scaling for AI Agents](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md): its reported gains are conditioned on reusable distillation, selective retrieval, freshness, and governance, directly exercising the three properties while retaining explicit vendor-report caveats. The Second Brain Trap, Cognee, and Agentic Note-Taking ingests already link the source and were not proposed again.
- Instructions: `rg -n -i 'discoverab|composab|trusted|trust signal|provenance|authority|activation|bounded context|context economy' kb/instructions/ --glob '*.md'` and `rg -n -i 'index|link|connection|memory|review gate|validation' kb/instructions/ --glob '*.md'` kept [Connect — Discovery Only](../../../../instructions/cp-skill-connect/SKILL.md) as an `operationalized-from` candidate: it adds ordered prospecting, articulation, authorised-label selection, and path verification to the source's high-level quality basis. Curated-index maintenance was rejected because its rationale is only the discoverability slice and is better grounded by the retrieval-miss and stale-index notes.

**Backlinks and one-hop link following:**

- `rg -n 'agent-memory-needs-discoverable-composable-trusted-knowledge-under' kb/ --glob '*.md'` found existing inbound edges from Claw learning loops, raw accumulation, Designing a Memory System, Charting the knowledge-access problem, Agent memory is crosscutting, Short composable notes, two curated heads, seven system reviews, and three source ingests. Existing edges were excluded from candidate counts.
- Followed the neighborhoods of the retrieval-miss note into stale-index enforcement and behavioral authority; the short-composable note into recognition, resolution-switching, and holistic-rewrite tension; the trace-authority note into activation and verification; the operational-axes note into detailed memory requirements; Agent memory coverage into shipped routing/review mechanisms; the comparative review into its activation and lifecycle cohorts; and the Databricks ingest into its retrieval, distillation, freshness, and governance caveats. These traversals strengthened the kept candidates above and did not produce an additional authorised destination. The stale-index hop also exposed obsolete `areas:` and `docs/indexes.md` implementation references, recorded under Maintenance Observations.
- Every path named below was checked with `test -f` before inclusion.

## Connections Found

- [A retrieval miss is a local reflective-path failure](../../../../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) — **mechanism**: explains how a discovery route that misses relevant remembered knowledge makes that represented aspect inert for the affected task while other routes can remain intact.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) — **mechanism**: develops discoverability into the structural requirement that a deterministic selector needs a path, type, tag, event, or other rule-ready signal, otherwise relevance must be inferred or loaded broadly.
- [Short composable notes maximize combinatorial discovery](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md) — **extends**: develops composability into an artifact-size rule under bounded context, where short independent claims increase the surface available for co-loading and synthesis.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — **extends**: develops calibrated trust into a maturation ladder whose verification, abstraction, and consultation operations license progressively stronger reliance.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — **extends**: turns the source's future-action criterion into separable tests for discovery, navigability, activation, uptake, context efficiency, lineage, and lifecycle health.
- [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) — **extends**: develops the capture, derivation, activation, authority, lifecycle, and evaluation machinery that the source explicitly places around its minimum artifact-quality basis.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) — **evidenced-by**: Commonplace is a worked implementation case whose coverage map realizes discoverability, composability, and trust through concrete routing, linking, validation, and review surfaces while naming their current limits.
- [What the matrix shows across 148 agent memory systems](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) — **evidenced-by**: the code-grounded comparison shows that activation and verification practices distinguish systems more than storage substrate, corroborating and bounding the source's artifact-quality frame.
- [Ingest: Memory Scaling for AI Agents](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md) — **evidenced-by**: the practitioner experiments report gains only when retained material is distilled into reusable form, selectively retrieved, kept current, and governed, while the ingest preserves important evidence and oracle limitations.
- [Connect — Discovery Only](../../../../instructions/cp-skill-connect/SKILL.md) — **operationalized-from**: the procedure adds prospecting order, articulation tests, authorised relationship labels, reverse-edge handling, and path verification for making one artifact discoverable and composable without directly mutating the library.

## Bidirectional Candidates

- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) → source — **extends**: the source already points to the general scarcity claim; a return edge would give that claim's reader the memory-specific consequence that retained material must be findable, combinable, and cheap enough to trust and carry.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source — **extends**: the source already uses the activation gap as a premise; a return edge would broaden that note's storage-to-action failure into the additional composability and calibrated-trust conditions on useful memory.

## Reverse-edge Candidates

- [Note](../../../../types/note.md) → source — **rests-on**: the type's discriminating description, compressed title handle, adjacent links, body-context requirement, review traits, and verification semantics are a concrete artifact contract for discoverability, composability, and calibrated trust.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) → source — **rests-on**: its coverage table directly uses the source's three-property basis to organize shipped Commonplace mechanisms and gaps; the current page names only the broader Designing a Memory System note.
- [sage-wiki](../../../../agent-memory-systems/reviews/sage-wiki.md) → source — **rests-on**: the review's pull-addressable wiki, ontology/link composition, and generated-output trust quarantine can be read more coherently against the source's three-property lens.
- [Ingest: Memory Scaling for AI Agents](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md) → source — **is-evidence-for**: the reported memory gains and caveats materially bear on the need for selective discovery, reusable shaping, freshness, and governance rather than storage growth alone.
- [Connect — Discovery Only](../../../../instructions/cp-skill-connect/SKILL.md) → source — **rests-on**: for meta-readers, the source explains why the skill pays for active discovery, explicit relationship articulation, and verified link targets; executing readers do not need to follow the edge.

## Off-authorisation Candidates

- [Note](../../../../types/note.md) — the source connects to this type contract because its retrieval description, title handle, links, context, review traits, and verification semantics implement the triad. Notes→types authorisation offers only `evidenced-by` and sparse `see-also`; neither accurately names implementation. Prefer the authorised reverse `Note → source — rests-on` edge above. Extend the source collection's notes→types set only if this implementation-direction reader need recurs across multiple notes.

## Raw Text Candidates

None

## Rejected Candidates

- [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) — useful but narrower than the source: it applies composability and trust to one linked-note retention boundary and is already reachable through the short-composable and activation neighborhood.
- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — close at the vocabulary level, but it diagnoses work remaining in a query-system state rather than properties of retained knowledge; treating transformation burden as composability would collapse distinct levels.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) — addressability for governed revision is not the same as discoverability for a future task; linking them directly would blur two distinct handles.
- [Make Authority Explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md) — governs actors and permissions over memory operations, while the source's trust property governs a reader's calibrated epistemic reliance on remembered material.
- [Tag README](../../../../types/tag-readme.md) — a strong local example of discoverability plus enforced trust, but too implementation-specific for a direct source edge and already reachable from the note-type and retrieval-miss mechanisms.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) — repeats the triad while planning future work; the shipped Agent memory coverage page is the more useful evidence target.
- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) — its explicit pre-review staging role illustrates retrieval without activation, but the existing link to the activation note already carries that precise boundary and avoids misclassifying the workbench as agent memory.
- [Cortex](../../../../agent-memory-systems/reviews/cortex.md) — supplies a useful individual trust/retrieval case, but the aggregate comparative review carries stronger evidence and avoids spraying the same general theory edge across system reviews.
- [Stale indexes reduce discovery when they suppress fallback search](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — its trusted-shortcut mechanism is already carried by the retrieval-miss candidate, so a direct edge would duplicate that route.

## Index Membership

- [Context engineering](../../../../tags/context-engineering-README.md) — candidate for the selective Core Claims section: the source states the minimum properties remembered knowledge must retain while routing, loading, and scoping it under bounded context. The source is already present in Agent memory and Foundations; Learning theory's validated `covered_by` route already reaches it through Agent memory, so no additional entry is proposed there.

## Synthesis Opportunities

None

## Maintenance Observations

None.

## Flags

- **Split candidate:** the artifact asserts three separately developable properties plus a boundary between artifact quality and surrounding system machinery. This standard pass found more than five genuine candidates across discovery/routing, artifact composition, epistemic authority, evaluation, and implementation evidence. A future writer should test whether the current note should remain the triad's synthesis/router while property-specific arguments move into separate notes; do not split merely to reduce its link count.
