---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/first-principles-analysis-maps-design-space-before-selection.md"
source_has_frontmatter: true
date: "2026-08-08"
depth: standard
---

# Connection Report: First-principles analysis maps a design space before selecting within it

**Source:** [First-principles analysis maps a design space before selecting within it](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md)

## Discovery Trace

### Notes

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/foundations-README.md`, and `kb/notes/artifact-analysis-README.md`. The source is already curated under both of its tags.
- `artifact-analysis-README.md` declares `complete: true`, so the by-tag `rg` description sweep for `artifact-analysis` was skipped. `foundations-README.md` has no completeness mark, so `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` was run.

**Listings and body searches:**

- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` generated the complete 342-title surface; `rg '^description:' kb/notes/ --glob '*.md'` generated the path-and-description surface.
- `rg -n -i 'design[- ]space|premature closure|rival (map|decomposition)|fixed decomposition' kb/notes/ --glob '*.md'` surfaced the orchestration map, the fixed-decomposition cluster, and existing inbound links from the human-analogy note.
- `rg -n -i 'independent (axis|axes|dimension)|cross[- ]product|primitive axes|choice dimensions' kb/notes/ --glob '*.md'` surfaced orchestration and memory-axis candidates.
- `rg -n -i 'first[- ]princip|boundary constraint|solution categor|inherited (package|seam)' kb/notes/ --glob '*.md'` and `rg -n -i 'decomposition.*(selection|search|closure)|selection.*decomposition' kb/notes/ --glob '*.md'` checked the constraint/choice split and the ordering claim.

**Candidate evaluations:**

- Kept `human-analogies-suggest-functions-not-component-boundaries.md`: it applies rival-decomposition analysis to inherited human component seams and already authors the independently useful return link.
- Kept `agent-orchestration-occupies-a-multi-dimensional-design-space.md`: it replaces a one-dimensional scheduler ladder with consequence-bearing axes and explicitly leaves its map open to revision.
- Kept `use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md`: it develops what happens after selection by showing why retained constraints, requirements, and free choices are needed to test transfer.
- Kept `task-fitted-structure-costs-cross-task-reuse.md`: it develops the lifecycle cost of hardening a task-derived position as though it were constraint-derived.
- Kept `memory-design-adds-operational-axes-to-artifact-analysis.md` as a reverse-edge candidate: its provisional six-axis map needs the source's independence, consequence, counterexample, and rival-map tests.
- Rejected `scenario-decomposition-drives-architecture.md`: it derives one architecture from current user stories but does not expose rival maps before selection.
- Rejected `solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md`: it orders commitments inside an already understood constrained search, rather than constructing or criticizing that search space.

### Reference

**Curated head and searches:**

- Read `kb/reference/README.md` in full.
- `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` generated the complete 130-title surface; `rg '^description:' kb/reference/ --glob '*.md'` generated the full description surface.
- `rg -n -i 'design[- ]space|alternatives before|premature closure|rival (map|decomposition)|fixed decomposition' kb/reference/ --glob '*.md'`, `rg -n -i 'independent (axis|axes|dimension)|cross[- ]product|choice dimensions|separable dimensions' kb/reference/ --glob '*.md'`, and the companion `first-princip|boundary constraint|inherited constraint|free choice` search flagged ADR 021's appendix, design-rationale management, proposal contracts, and behavioral-authority revision work.

**Candidate evaluations:**

- Kept `adr/021-shipping-model-design-space.md`: it enumerates option axes, keeps couplings visible, and records a path audit reversing the initial preference.
- Rejected `design-rationale-management.md` as a source-side target: it describes retention surfaces, while the `use-tests...` note supplies the sharper transferable continuation from map construction to later transfer testing.
- Rejected `types/design-proposal.md` and `proposals/README.md`: their option-space contract operationalizes the posture locally but adds less traversal value than the concrete ADR 021 case.

### Agent-memory systems

**Curated head and searches:**

- Read `kb/agent-memory-systems/README.md` in full.
- `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` generated the complete 172-title surface; `rg '^description:' kb/agent-memory-systems/ --glob '*.md'` generated the full description surface.
- `rg -n -i 'design[- ]space|premature closure|rival (map|decomposition)|fixed decomposition' kb/agent-memory-systems/ --glob '*.md'`, `rg -n -i 'independent (axis|axes|dimension)|cross[- ]product|choice dimensions|separable dimensions' kb/agent-memory-systems/ --glob '*.md'`, and the focused `taxonomy|classification|matrix.*(axis|axes)|axis.*matrix` query flagged the comparative review, the review-framework rationale, and the review type's write/read split.

**Candidate evaluations:**

- Kept `review-framework-design.md`: corpus counterexamples forced `mixed` buckets to split, a timing axis to disappear, and a duplicate targeting field to be removed.
- Kept `agentic-memory-systems-comparative-review.md`: the 148-system comparison shows substrate packages hiding independently varying capture, activation, lifecycle, and verification choices.
- Rejected individual system reviews: they populate cells, but none adds more map-quality evidence than the framework revisions and cross-system comparison.

### Agentic systems

**Curated head and searches:**

- Read `kb/agentic-systems/README.md` and generated its complete 11-title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` and `rg '^description:' kb/agentic-systems/ --glob '*.md'`.
- The `design[- ]space|premature closure|rival...|fixed decomposition`, `independent axis...|cross-product`, and `first-princip|boundary constraint|solution categor|decomposition` searches kept Autogenesis; other hits described runtime decompositions without showing the map itself being revised.

**Candidate evaluations:**

- Kept `autogenesis.md`: its paper taxonomy and current implementation differ because operational distinctions forced new resource types and contracts. It already links to the source as `rests-on`, so only the missing source-side evidence edge is proposed.
- Rejected `agno-agentos.md`: it exposes where a leader model chooses decomposition, but it does not test or revise the decomposition as directly as Autogenesis.

### Sources

**Curated head and searches:**

- Read `kb/sources/README.md` and generated the complete 449-title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` and `rg '^description:' kb/sources/ --glob '*.md'`.
- `rg -n -i 'design[- ]space|premature closure|rival (map|decomposition)|fixed decomposition' kb/sources/ --glob '*.md'`, `rg -n -i 'independent (axis|axes|dimension)|cross[- ]product|choice dimensions|separable dimensions' kb/sources/ --glob '*.md'`, and the companion first-principles/taxonomy queries surfaced Build Systems à la Carte, Parnas, the Rosebud memory map, and broad survey taxonomies.

**Candidate evaluations:**

- `build-systems-a-la-carte.ingest.md` and `parnas-1972-criteria-decomposing-systems-modules.md` are the two strongest source cases, but both are already linked in the source and were excluded from the candidate sections.
- Rejected `everything-you-need-to-know-about-llm-memory.ingest.md`: its anonymous conceptual taxonomy admits axis coupling and is already absorbed by the stronger `memory-design-adds-operational-axes...` theory note; another direct evidence link would duplicate that route.
- Rejected broad adaptation and human-memory taxonomies whose axes catalogue existing systems without showing constraint-derived generation or refutation by consequences.

### Instructions

**Curated head, reverse-edge posture, and searches:**

- Read `kb/instructions/README.md` and the full outbound section of `kb/instructions/COLLECTION.md`. The collection frontloads execution and permits theory links only as exceptional meta-reader `rests-on` edges.
- `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'` generated the complete 42-title surface; `rg '^description:' kb/instructions/ --glob '*.md'` generated the description surface.
- The `design-space|premature closure|rival map|fixed decomposition`, `independent axis|cross-product`, and `first-princip|boundary constraint|solution-shaped|alternative fram` searches kept `invert-solution-shaped-requests.md` and rejected scenario evaluation and full-pass review procedures.

**Candidate evaluations:**

- The source already authors the permitted `operationalized-from` footer edge to `invert-solution-shaped-requests.md`, so no duplicate outbound candidate is reported.
- Kept the inverse `invert-solution-shaped-requests.md` → source as a reverse edge: maintainers need the theory behind recovering the problem and generating rival framings before implementation commitment.

### Global types and external

- `kb/types/` has no `README.md`. Its complete nine-title surface, full description listing, and `rg -n -i 'design[- ]space|decomposition|independent (axis|axes|dimension)|cross[- ]product|first[- ]princip|boundary constraint|option space' kb/types/ --glob '*.md'` produced no plausible evidence target.
- `external` is authorised through `evidenced-by`, but no user-supplied or already-loaded external target was present. Open-web prospecting was skipped.

### Link following

- Followed all nine existing source links and excluded them from new outbound candidates. This removed the already-authored Build Systems, Parnas, and solution-inversion edges from the candidate pool.
- Followed the human-analogy note and Autogenesis back to their existing links into the source; both return edges are already authored.
- Followed the orchestration map through its policy-form, coordination-guarantee, Tracecraft, and Claude Code dynamic-workflow neighborhood. These confirmed the map as a domain application and did not expose a stronger replacement candidate.
- Followed `use-tests...` through Parnas and design-rationale management, and `task-fitted-structure...` through scenario decomposition and the universal-taxonomy note. The resulting evaluations are recorded above.
- Followed the agent-memory comparison into `review-framework-design.md`, where the axis-revision decisions and their consequences are retained.

## Connections Found

- [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md) -- **extends**: applies rival-decomposition analysis to inherited human component seams while preserving the functions those analogies suggest.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **extends**: develops the method in orchestration by replacing a familiar scheduler ladder with independently variable dimensions and an explicitly revisable map.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- **extends**: continues past selection to show what rationale must survive so a chosen decomposition's transfer claim can later be tested.
- [Task-fitted structure costs cross-task reuse](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) -- **extends**: develops the lifecycle consequence of confusing a task-selected position inside the design space with structure forced by its boundary constraints.
- [ADR 021 appendix: shipped-content namespacing design space](../../../reference/adr/021-shipping-model-design-space.md) -- **evidenced-by**: a Commonplace decision enumerated option axes and then reversed its initial preference when a path-invariance audit discriminated among combinations.
- [Review framework and comparison matrix: design and decisions](../../../../agent-memory-systems/review-framework-design.md) -- **evidenced-by**: observed corpus failures forced comparison axes to split, disappear, or be removed instead of preserving inherited buckets.
- [What the matrix shows across 148 agent memory systems](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) -- **evidenced-by**: the cross-system spread shows that storage packages conceal independently varying capture, activation, lifecycle, and verification choices.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- **evidenced-by**: its implementation revised the paper's resource taxonomy when skills, connectors, and workflows proved operationally distinct.

## Bidirectional Candidates

- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) → source -- **exemplifies**: its orchestration axes are a domain-specific instance of generating a revisable map rather than accepting a one-dimensional inherited taxonomy.

## Reverse-edge Candidates

- [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) → source -- **grounds**: its provisional six-axis map needs the source's tests for consequence-bearing distinctions, counterexamples, empty cells, and rival derivations.
- [Invert solution-shaped requests](../../../../instructions/invert-solution-shaped-requests.md) → source -- **rests-on**: meta-readers maintaining the procedure need the theory explaining why a proposed solution must not close the design before rival framings are exposed.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Scenario decomposition drives architecture](../../../../notes/scenario-decomposition-drives-architecture.md) -- derives one architecture from current user stories but does not expose or compare rival decompositions before selection.
- [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) -- orders commitments after the feasible choices are known; it does not construct the space in which those choices were found.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) -- useful descriptive context, but the `use-tests...` candidate carries the sharper transferable continuation for source readers.
- [Ingest: Everything you need to know about LLM memory](../../../../sources/everything-you-need-to-know-about-llm-memory.ingest.md) -- a conceptual, acknowledgedly coupled taxonomy already absorbed by the stronger memory-design theory note.

## Index Membership

None. The source is already curated in `foundations-README.md` and the complete `artifact-analysis-README.md`.

## Synthesis Opportunities

None. The kept cases instantiate or extend tests already stated by the source; they do not jointly imply a separate higher-order claim.

## Maintenance Observations

- [Review framework and comparison matrix: design and decisions](../../../../agent-memory-systems/review-framework-design.md) says under D4 that parser wiring for curation-operation columns is pending, while `Open follow-ons` later marks that work done. Reconcile the stale local status wording in a separate maintenance task.

## Flags

None
