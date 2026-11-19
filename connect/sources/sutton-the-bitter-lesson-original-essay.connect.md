---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/sutton-the-bitter-lesson-original-essay.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: The Bitter Lesson (Sutton, 2019) — original essay

**Source:** [The Bitter Lesson (Sutton, 2019) — original essay](../../../../sources/.snapshots/sutton-the-bitter-lesson-original-essay.md)

## Discovery Trace

**Description listing scan:**

- Read title and description surfaces for `kb/notes/`, `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`. The dense Bitter Lesson note cluster was narrowed to claims that depend directly on Sutton's contrast or his meta-methods passage.

**Topic indexes:**

- Read `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The learning-theory and foundations routes were relevant; no reference or system-review index destination needs to own the primary essay evidence.

**Body search:**

- `rg -n -i "Sutton|Bitter Lesson|search and learning|meta-methods|human[- ]knowledge|production method" kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md' --glob '!*.connect.md'` retained [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md), [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md), and [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
- The same search exposed many downstream notes that merely link to the two canonical interpretations; those were not retained as redundant source edges.

**Link following:**

- Followed the canonical interpretation notes, the machinery note, and the existing [Wikipedia Bitter Lesson ingest](../../../../sources/wikipedia-bitter-lesson.ingest.md). The original essay is the primary source for the hand-crafted-human-knowledge versus computation-through-search-and-learning contrast and for the instruction to build meta-methods rather than discoveries.
- Compared the original with the Wikipedia capture. The latter adds reception and citation context; it should not replace the original as evidence for Sutton's exact argumentative carve.

## Connections Found

- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **is-evidence-for**: Sutton explicitly opposes hand-built domain knowledge to methods that leverage computation through search and learning, supporting the note's production-method reading while not itself establishing form orthogonality.
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- **is-evidence-for**: the historical cases and scaling claim supply the source phenomenon that the note interprets as selection against human-imposed generalization beyond tested scope.
- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) -- **is-evidence-for**: Sutton's closing meta-methods passage distinguishes retained discovering machinery from built-in discoveries, directly motivating the note's non-exemption test for reflective machinery.
- [Wikipedia Bitter Lesson ingest](../../../../sources/wikipedia-bitter-lesson.ingest.md) -- **compares-with**: the original essay supplies primary argumentative evidence, while the Wikipedia capture adds secondary reception, examples, and attribution context.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) → source -- **evidenced-by**: point its original-essay citation through the local ingest when the analytical provenance is useful.
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) → source -- **evidenced-by**: retain the primary essay as the source phenomenon, while making clear that the unearned-reach mechanism is the note's interpretation.
- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) → source -- **evidenced-by**: ground the note's quoted meta-methods distinction in the captured original.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- Downstream notes that cite one of the two canonical Bitter Lesson interpretation notes -- rejected because the canonical note already supplies the appropriate traversal edge and a direct source edge would duplicate it.
- Agentic-system reviews applying the Bitter Lesson to one harness -- rejected because those analyses rest on the KB interpretation rather than on a new reading of Sutton's essay.

## Index Membership

None

## Synthesis Opportunities

None. The production-method, unearned-reach, and reflective-machinery interpretations are already represented as distinct notes.

## Maintenance Observations

- The existing Wikipedia ingest and this original-essay snapshot share a topic but not a source identity. Separate ingests preserve the primary/secondary distinction and allow each checksum to remain independently auditable.

## Flags

- Sutton's essay does not itself claim that all durable structure must live in weights, nor does it prove the KB's unearned-reach mechanism; those are downstream interpretations whose added premises must remain visible.
