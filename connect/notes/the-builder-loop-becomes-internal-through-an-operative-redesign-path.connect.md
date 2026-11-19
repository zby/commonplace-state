---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: kb/notes/the-builder-loop-becomes-internal-through-an-operative-redesign-path.md
source_has_frontmatter: true
date: "2026-08-03"
depth: standard
---

# Connection Report: The builder loop becomes internal through an operative redesign path

**Source:** [The builder loop becomes internal through an operative redesign path](../../../../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md)

## Discovery Trace

**Authorisation and breadth:**

- Read `kb/notes/COLLECTION.md` before prospecting. It authorises `notes`, `reference`, `agent-memory-systems`, `sources`, and `instructions`, plus the reserved `external` destination; it excludes `kb/work/`. The source's `foundations` and `self-improving-systems` tags triggered the two matching tag heads. `external` was not prospected: no user-supplied external target was in scope.
- Read the curated heads `kb/notes/README.md`, `kb/notes/foundations-README.md`, `kb/notes/self-improving-systems-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. Neither tag head declares `complete: true`, so no by-tag sweep was skipped.
- Generated the complete title surfaces with `rg -N --no-heading -m1 '^# ' kb/{notes,reference,agent-memory-systems,sources,instructions}/ --glob '*.md'`; ran `rg '^description:' kb/<destination>/ --glob '*.md'` for every authorised local destination. The source's existing footer and inline links were then checked so the report does not recommend duplicates.

**Body search:**

- `rg -l -i 'builder loop' kb/notes kb/reference kb/agent-memory-systems kb/sources kb/instructions --glob '*.md'` returned only the source; the phrase is new rather than a separate link cluster.
- `rg -l -i 'operative redesign' kb/notes kb/reference kb/agent-memory-systems kb/sources kb/instructions --glob '*.md'` returned only the source.
- `rg -l -i 'retained.*revision|revision.*retained' kb/notes kb/reference kb/agent-memory-systems kb/sources kb/instructions --glob '*.md'` surfaced `only-explicit-retention-is-durable-writable-and-addressable.md`, `reflection-makes-retained-lessons-second-order.md`, and several system reviews. The explicit-retention note was retained as a premise candidate; the lesson note was rejected because the source already links the more direct addressability claim.
- `rg -l -i 'self-improv' kb/notes kb/reference kb/agent-memory-systems kb/sources kb/instructions --glob '*.md'` surfaced the two Commonplace trace accounts, the casebook, Auto Harness, Meta-Harness, and the source's already cited ingests. `rg -l -i 'reflective.*(path|loop|change)' ...` additionally surfaced the proposal-selection loop and `machinery-persists-by-warrant-not-position-in-a-reflective-loop.md`.
- `rg -l -i 'acceptance rule|update rule|evaluator' kb/notes kb/reference kb/agent-memory-systems kb/sources kb/instructions --glob '*.md'` was used to test the source's protected-evaluator and authority boundary. It confirmed the proposal-selection note and the two code-grounded harness reviews as substantive, rather than keyword-only, cases.

**Candidate evaluation and link following:**

- Read [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): its local closure conditions stop at one accepted change, while this source supplies the distinct test that the builder machinery itself stays challengeable. Kept as `extends`.
- Read [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md): its explicit-artifact premise explains why the source's sixth obligation can be inspectable and selectively revisable. Kept as `grounds`.
- Read [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md): its rows independently delimit the same supplied objectives, evaluators, and acceptance rules for Continual Harness, Autogenesis, Self-Harness, and Darwin Gödel Machine. Kept as `evidenced-by` rather than repeating individual source ingests.
- Followed the Commonplace trace cluster from [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) to [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md). Both describe the particular change path but do not yet cite this source's builder-level test; retained as reverse edges and the trace as outbound evidence.
- Read [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) and [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md). Each shows evidence → gate → retained executable scaffold, while its harness/gate policy remains supplied; these are useful independently code-grounded boundary cases. Kept as outbound evidence and reverse `is-evidence-for` candidates.
- Read [Machinery persists by warrant, not position in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) and [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../../../../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md). Both overlap on governance, but neither provides a reader a more direct next step than the source's existing links to addressability, frozen functions, closure/allocation, and leverage; rejected.
- Searched `kb/instructions/` for `builder loop|operative redesign|retained.*revision|self-improv`. The full-improvement-pass procedure names this skill but is not an operative redesign path for the builder machinery claimed here, so no rare `operationalized-from` edge is proposed.
- `kb/sources/` was searched through ingest reports rather than snapshots, per its authored-surface contract. The six ingests used by the source already carry its empirical evidence; no additional source-side candidate survived.

## Connections Found

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **extends**: its three-function loop explains a single accepted operative change; this source adds the non-equivalent condition that the organization selecting and installing that change is itself represented, used, and revisable in a later episode.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) -- **grounds**: the source's sixth obligation needs a retained object that later actors can inspect and selectively challenge; this note supplies the current representational premise for that addressability.
- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) -- **evidenced-by**: its independent placements expose the same aspect-specific limits -- fixed Refiner, objective, evaluator, acceptance rule, or population policy -- across the source's empirical cases.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) -- **evidenced-by**: the traced Commonplace episode supplies a concrete represented-evidence-authority-installation-use chain, with its remaining human gate and objective boundary explicitly identified.
- [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) -- **evidenced-by**: its code-grounded trace-to-agent-code and regression-suite promotion path is an additional control: accepted agent edits become operative, while the file guard, benchmark, and promotion rule remain supplied.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) -- **evidenced-by**: it shows an evaluation-gated path from retained traces to a later-running harness, while preserving a useful question for the source's test -- whether its proposer, evaluation, and frontier machinery are themselves within the revisable redesign class.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) → source -- **rests-on**: its classification reports a reflective pathway and uneven coverage; the source supplies the stricter builder-loop criterion needed to state which Commonplace organizational aspects are demonstrably internal rather than merely editable.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) → source -- **rests-on**: the trace's search/evaluation/retention mapping would gain an explicit test for whether the adopted tag-README machinery remains available for later challenge.
- [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) → source -- **is-evidence-for**: its fixed gate and allowed-edit set bear directly on the source's distinction between a local operative update path and builder-loop reach over the policy governing it.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) → source -- **is-evidence-for**: the review's separation of proposer creativity from evaluator/frontier authority is a code-grounded boundary case for the source's aspect-by-aspect criterion.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Machinery persists by warrant, not position in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) -- shares the moving-boundary and governance concern, but its reader is choosing what licenses persistence; the source's existing frozen-function, authority, and leverage links provide the direct traversal path for operative redesign.
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../../../../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) -- useful neighbouring theory, but it frames how far a methodology settles decisions, not whether a particular redesign path was installed, used, and reopened; an added edge would be broad topical overlap.
- [run-full-improvement-pass-on-note](../../../../instructions/run-full-improvement-pass-on-note.md) -- its ordered workflow includes connection discovery, but it does not add ordering or stopping conditions for builder-loop redesign itself, so it is not an `operationalized-from` witness.

## Index Membership

None -- the source already appears in the self-improving-systems curated head; `foundations-README.md` supplies only selective coverage and does not require another entry.

## Synthesis Opportunities

- The source, the proposal-selection decomposition, and the two code-grounded harness reviews suggest a possible cross-system synthesis: **a promotion loop becomes a builder loop only when its evaluator, candidate representation, and scope policy each have a represented, authorized later revision path**. The source establishes the general criterion; the reviews could test it against executable harnesses rather than reported papers.

## Maintenance Observations

None

## Flags

None
