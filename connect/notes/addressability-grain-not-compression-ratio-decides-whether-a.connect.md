---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/addressability-grain-not-compression-ratio-decides-whether-a.md"
source_has_frontmatter: true
date: "2026-08-23"
depth: standard
---

# Connection Report: Addressability grain, not compression ratio, sets a matched selective-read floor

**Source:** [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md)

## Discovery Trace

### `kb/notes/`

**Curated heads and tag scans:**

- Read [`README.md`](../../../../notes/README.md), [`document-system-README.md`](../../../../tags/document-system-README.md), and [`context-engineering-README.md`](../../../../tags/context-engineering-README.md). Neither tag README declares `complete: true`, so neither by-tag fallback was skipped.
- Ran `rg -l '^tags:.*\bdocument-system\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the equivalent query for `context-engineering`. The scans recovered the source's existing cache-economics, access-cost, pointer, and sufficiency neighborhood.

**Title and description listings:**

- Generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and enumerated descriptions with `rg '^description:' kb/notes/ --glob '*.md'`.
- Kept [`Access burden and transformation burden are distinct query dimensions`](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) because the source supplies a concrete lower bound inside its access-burden axis. Kept [`Rule-based context selection needs a pre-existing signal`](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) because it establishes the discriminating-key prerequisite the source assumes.

**Body search:**

- Ran `rg -n -i 'addressab(le|ility)|addressability grain|retrieval floor|selective read|one-unit|smallest unit' kb/notes/ --glob '*.md'`.
- Ran `rg -n -i 'compression ratio|summary layer|summary.*source|source.*summary|per-module|description index' kb/notes/ --glob '*.md'`.
- Ran `rg -n -i 'search key|discriminating key|query-time|symbol search|heading|retrieval unit|chunk granularity|granularity' kb/notes/ --glob '*.md'`.
- These searches also surfaced the existing links to the sufficiency, access-mode, cache-ledger, pointer-design, frontloading, materialization, recovery, and ADR-025 notes. They were not re-proposed as outbound candidates because the stable source already authors those edges.

**Link following:**

- Followed all eight existing source links one hop and inspected the neighborhoods of the access-burden, rule-based-selection, sufficiency, pointer-design, and access-mode candidates.
- Ran `rg -n 'addressability-grain-not-compression-ratio-decides-whether-a|Addressability grain, not compression ratio' kb --glob '*.md'` to check existing inbound edges. The sufficiency and LLM-recompute notes already link back; the broad access-burden note and rule-based-selection note do not.
- Rejected [`Localized retention pays when sparse changes have bounded impact in a matching decomposition`](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) after its scope explicitly separated revision cost from retrieval. Rejected reflection-addressability hits because they concern inspectable and revisable commitments rather than the smallest unit loaded by a query.

### `kb/types/`

**Curated head and listings:**

- Read [`README.md`](../../../../types/README.md), generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'`, and ran `rg '^description:' kb/types/ --glob '*.md' | rg -i 'address|retriev|summary|abstract|compression|context|navigation|search|select|granul|chunk|routing|pointer|index'`.
- Ran `rg -n -i 'addressability grain|retrieval floor|selective read|compression ratio|summary layer|smallest (addressable |selectable )?unit|discriminating key|symbol search|per-module|description index|chunk granularity|retrieval granularity' kb/types/ --glob '*.md'`; it returned no direct match.
- [`note.md`](../../../../types/note.md) requires descriptions and treats them as retrieval filters, but the source already reaches that contract through the more explanatory “Types give agents structural hints before opening documents” edge. A direct type-spec edge would duplicate the route.

### `kb/reference/`

**Curated head and listings:**

- Read [`README.md`](../../../../reference/README.md), generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`, and ran `rg '^description:' kb/reference/ --glob '*.md' | rg -i 'address|retriev|summary|abstract|compression|context|navigation|search|select|granul|chunk|routing|pointer|index'`.
- The listing surfaced ADR 025, Navigation, and the library module reference. ADR 025 is already linked from the stable source; Navigation and the reference collection contract are more useful in the inverse direction.

**Body search and link following:**

- Ran `rg -n -i 'addressability grain|retrieval floor|selective read|compression ratio|summary layer|smallest (addressable |selectable )?unit|discriminating key|symbol search|per-module|description index|chunk granularity|retrieval granularity' kb/reference/ --glob '*.md'`.
- Read [`lib-modules.md`](../../../reference/lib-modules.md) and its module-section/symbol surface. It is the concrete coarse prose reference used by the source's harmful Commonplace case, so it passes the articulation test as a bounded witness rather than as general theory.
- Followed [`ADR 025`](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) to Navigation and the connect procedure. ADR 025 already records the helpful scoped-description case but lacks a return link to the sharper smallest-selectable-unit rationale.

### `kb/agent-memory-systems/`

**Curated head and listings:**

- Read [`README.md`](../../../../agent-memory-systems/README.md), generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`, and ran the scoped description query `rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg -i 'address|retriev|summary|abstract|compression|context|navigation|search|select|granul|chunk|routing|pointer|index'`.
- Ran the same focused body expression used for reference artifacts, then broadened it with `rg -n -i 'selective (read|access)|filesystem-native search|search, slicing|chunk granularity|retrieval granularity|hierarchical retrieval|progressive.*abstract|L0|L1|L2|description index|summary layer|abstract tier|fine-grained.*retriev|coarse.*retriev' kb/agent-memory-systems/ --glob '*.md'`.

**Candidate evaluation and link following:**

- Kept [`pi-self-learning`](../../../../agent-memory-systems/reviews/pi-self-learning.md) only as a reverse edge: its Commonplace comparison explicitly identifies retrieval granularity as the main divergence, and the source supplies the theoretical criterion for that comparison.
- Followed [`OpenViking`](../../../../agent-memory-systems/reviews/openviking.md), [`AI-Context-OS`](../../../../agent-memory-systems/reviews/AI-Context-OS.md), and [`ACE`](../../../../agent-memory-systems/reviews/ace.md). Their URI/L0-L2 tiers or coarse whole-playbook loading are relevant testbeds, but none fixes a matched question and compares the smallest answer-bearing unit on both paths. They therefore failed the articulation or evidence-strength test for a direct source edge.

### `kb/agentic-systems/`

**Curated head and searches:**

- Read [`README.md`](../../../../agentic-systems/README.md), generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`, and ran the scoped description and focused body expressions used above.
- No whole-system analysis plausibly matched the one-unit retrieval-floor trigger. The relevant results were memory/context-engineering subsystem reviews, so this destination yielded no candidate.

### `kb/sources/`

**Curated head and listings:**

- Read [`README.md`](../../../../sources/README.md), generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`, and ran `rg '^description:' kb/sources/ --glob '*.md' | rg -i 'address|retriev|summary|abstract|compression|context|navigation|search|select|granul|chunk|routing|pointer|index'`.
- Ran the focused body expression used above plus `rg -n -i 'selective (read|access)|filesystem-native search|search, slicing|chunk granularity|retrieval granularity|hierarchical retrieval|progressive.*abstract|L0|L1|L2|description index|summary layer|abstract tier|fine-grained.*retriev|coarse.*retriev' kb/sources/ --glob '*.md'`.

**Candidate evaluation and link following:**

- Kept [`Coding Agents are Effective Long-Context Processors`](../../../../sources/coding-agents-are-effective-long-context-processors.ingest.md) as qualified evidence: its comparative benchmark shows filesystem-native search and slicing changing how much material an agent loads, while its own limitations prevent attributing the gains solely to grain.
- Followed [`Harness Handbook`](../../../../sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md) to its L1-L3 behavior maps and source-backed function/file cards. Its token and localization gains bundle organization, source locators, and progressive disclosure, and the paper lacks an equal-cost representation ablation, so it does not isolate the source's one-unit mechanism.
- Rejected DeLM's intermediate-summary ablation because verification, shared-state scheduling, and coarse-to-fine recoverability vary with the representation layer; the result does not identify addressability grain.

### `kb/instructions/`

**Curated head and searches:**

- Read [`README.md`](../../../../instructions/README.md), generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`, and ran the scoped description and focused body expressions used above.
- Read [`Connect — Discovery Only`](../../../../instructions/cp-skill-connect/SKILL.md) fully. Its curated-head → title → description → body progression depends on cheaper addressable routing units, but instruction links are exceptional; the useful direction is a meta-reader `rests-on` edge from the procedure to the theory note.

### `external`

The notes contract authorizes `external` under `evidenced-by`, but no external target supplied by the user or already loaded was specific enough to pass the articulation test. Open-web prospecting was skipped as required; the relevant paper was evaluated through its tracked local ingest.

## Connections Found

- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **exemplifies**: addressability grain supplies a measurable selective-read floor inside the broader access-burden axis while leaving transformation burden, semantic reconstruction, and answer sufficiency separate.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) — **grounds**: the source's matched comparison assumes a known discriminating key, and this target explains why a selector cannot isolate one answer-bearing unit unless its inputs already encode or infer that distinction.
- [Commonplace library (`commonplace.lib`)](../../../reference/lib-modules.md) — **evidenced-by**: the per-module prose sections are the concrete coarse reference surface in the source's harmful Commonplace witness, while the same artifact exposes named functions that can be located more narrowly in code.
- [Coding Agents are Effective Long-Context Processors](../../../../sources/coding-agents-are-effective-long-context-processors.ingest.md) — **evidenced-by**: the benchmark corroborates that filesystem-native search and slicing can change the material loaded for long-context questions; its bundled tooling and task comparisons bound the evidence because they do not isolate addressability grain alone.

## Bidirectional Candidates

- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) → source — **extends**: readers of the broad two-burden decomposition gain a concrete lower-bound relation for one matched selective-access case.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) → source — **extends**: once a signal can target a case, the source adds the independent cost condition that the selected unit must actually be finer than the source-side unit.
- [ADR 025 — Complete generated indexes are build-time only](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) → source — **rests-on**: ADR readers need the general one-unit rationale for why scoped path-plus-description reads can beat complete generated inventories; the source already links ADR 025 as its implemented helping case.
- [Coding Agents are Effective Long-Context Processors](../../../../sources/coding-agents-are-effective-long-context-processors.ingest.md) → source — **is-evidence-for**: the ingest's search-and-slicing result bears on the source's access-path-relative claim without asserting that the benchmark isolates or proves the one-unit relation.

## Reverse-edge Candidates

- [Navigation](../../../../reference/navigation.md) → source — **rests-on**: the shipped description-as-filter and scoped-listing stack depends on the claim that its intermediate surface exposes a cheaper selectable unit than opening each full artifact.
- [Reference collection contract](../../../../reference/COLLECTION.md) → source — **rests-on**: the economy test already states the symbol-versus-prose and smallest-selected-unit rule almost verbatim; a theory link would expose the argument and scope behind this binding writing rule.
- [Connect — Discovery Only](../../../../instructions/cp-skill-connect/SKILL.md) → source — **rests-on**: the procedure's title-first, description-second, body-last discovery order depends on successively more expensive addressable units, and this meta-reader edge would not become an executing-agent dependency.
- [pi-self-learning](../../../../agent-memory-systems/reviews/pi-self-learning.md) → source — **rests-on**: the review's claim that pi-self-learning and Commonplace chiefly diverge in retrieval granularity needs the source's path-relative grain criterion to make that comparison precise.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) — “addressability” refers to independently editable and checkable revision units; its scope explicitly excludes retrieval cost.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) — concerns retrieving, criticizing, revising, and rescoping a represented commitment as an object, not the byte/token floor of one selective read.
- [Link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md) — explains why descriptions help long-range routing, but the source already links the closer mechanism note about types and descriptions; another route would add topical overlap rather than a new premise.
- [A knowledge base should support fluid resolution-switching](../../../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) — concerns movement among abstraction levels and navigation dead ends, not a matched question with one answer-bearing unit on each access path.
- [OpenViking](../../../../agent-memory-systems/reviews/openviking.md) and [AI-Context-OS](../../../../agent-memory-systems/reviews/AI-Context-OS.md) — implement layered summaries and retrieval, but neither review measures the smallest unit selected on matched summary/source paths or tests the resulting behavioral effect.
- [ACE](../../../../agent-memory-systems/reviews/ace.md) — establishes coarse whole-playbook loading, not a matched comparison between a summary unit and its source unit.
- [Harness Handbook](../../../../sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md) — reports localization and token gains, but organization, source locators, generated descriptions, and progressive disclosure move together; the study does not identify grain as the mechanism.
- [DeLM shared-context ingest](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md) — its summary-layer ablation bundles verification, coordination, and hierarchical recoverability, so it cannot support the one-unit claim.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- [`document-system-README.md`](../../../../tags/document-system-README.md) and [`context-engineering-README.md`](../../../../tags/context-engineering-README.md) still use the earlier link text “Addressability grain, not compression ratio, decides whether a summary layer helps” and describe grain as deciding whether the layer helps or pays. The stable source now makes the narrower claim that finer grain is necessary to lower a matched one-unit retrieval floor but does not guarantee net value. A future index-maintenance pass should update both context phrases without changing membership.

## Flags

None
