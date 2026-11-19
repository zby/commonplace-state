---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/parnas-1972-criteria-decomposing-systems-modules.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: On the Criteria To Be Used in Decomposing Systems into Modules

**Source:** [On the Criteria To Be Used in Decomposing Systems into Modules](../../../../sources/.snapshots/parnas-1972-criteria-decomposing-systems-modules.md)

## Discovery Trace

**Description listing scan:**

- Read title and description surfaces across `kb/notes/`, `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`. The retained candidates were notes that directly use the KWIC comparison or generalize its change-localization criterion.

**Topic indexes:**

- Read `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The learning-theory route contains the substantive destinations; the other curated heads did not expose a stronger destination.

**Body search:**

- `rg -n -i "Parnas|KWIC|information[- ]hiding|decisions likely to change|flowchart" kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md' --glob '!*.connect.md'` found direct uses in [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md), [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md), and [First-principles analysis maps a design space before selecting within it](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md).
- The search also found brief invocations in the composable-notes and soft-bound-traditions notes; those were evaluated but rejected as too broad for a direct source edge.

**Link following:**

- Followed the three retained notes and their decomposition neighbors. The paper supplies two distinct facts: the same working KWIC behavior underdetermines the better decomposition, and hiding likely-to-change design decisions localizes later change and enables reuse.
- Checked the limits stated by the localized-retention note. Parnas supports matching module boundaries to anticipated change; it does not by itself establish that the dependency closure or regression-validation radius is small.

## Connections Found

- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- **is-evidence-for**: the two functioning KWIC decompositions produce the same result while differing in change and reuse consequences, showing why execution alone cannot reveal the force that warrants a seam.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- **is-evidence-for**: Parnas's information-hiding criterion is the inherited case for matching retained boundaries to decisions expected to change.
- [First-principles analysis maps a design space before selecting within it](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md) -- **is-evidence-for**: the rival KWIC modularizations demonstrate that one familiar decomposition cannot certify its own axes and that alternatives expose different consequences.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) → source -- **evidenced-by**: replace or supplement its direct external citation with the ingest that owns the captured paper and its limitations.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) → source -- **evidenced-by**: use the ingest for the inherited change-localization result while preserving the note's explicit bounded-impact extension.
- [First-principles analysis maps a design space before selecting within it](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md) → source -- **evidenced-by**: ground its KWIC rival-decomposition example in the captured primary paper.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Short composable notes maximize combinatorial discovery](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md) -- rejected because it invokes modular design only as a broad analogy and does not use the paper's discriminating KWIC evidence.
- [Soft-bound traditions as sources for context-engineering strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- rejected because its table records Parnas as a tradition-level precedent; the focused notes already provide the useful traversal destinations.

## Index Membership

None

## Synthesis Opportunities

None. The retained notes already separate local execution sufficiency, transfer rationale, and change-localization consequences.

## Maintenance Observations

- Several notes cite the PDF URL directly. The new ingest can become the local analytical owner without requiring immediate replacement of those source citations.

## Flags

- Preserve the paper's boundary: information hiding predicts modification and reuse advantages, not automatically a bounded validation radius for every downstream dependency graph.
