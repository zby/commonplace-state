---
description: "Candidate connections distinguishing JPL edit scope from revision order and decision ownership."
type: types/connect-report.md
source: kb/sources/.snapshots/levels-of-edit-1980.md
source_has_frontmatter: true
date: "2026-11-13"
depth: standard
---

# Connection Report: The Levels of Edit, Second Edition

**Source:** The Levels of Edit, Second Edition (immutable local snapshot; future authored surface is its paired ingest).

## Discovery Trace

- Read the source fully and `kb/sources/COLLECTION.md`; snapshots are immutable, and suggestions belong to a future ingest, not the snapshot.
- Read curated heads for theory, reference, sources, agent-memory-systems and agentic-systems. The two system-survey collections have no plausible trigger: this is an editorial specification, not an agent-system account. Skip their further prospecting. Sources permits no outbound label to tags; no tag assigned to this snapshot, so skip tag prospecting. Work and instructions are excluded destinations.
- Generated and scanned complete fresh H1 listings for theory, reference and sources using `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'`. The terminal truncated the combined listing; recovered its missing beginning from the saved command output.
- Scoped description/title query: `rg -n -i '^(description:.*(editorial|revision|commission|degrees.of.freedom|substantive)|# .*?(edit|revision|author|freedom))' kb/theory kb/reference kb/sources --glob '*.md'` (first 100 hits inspected). The executor-boundary and constrained-search notes match distinct comparison axes. Numerous machine-learning revision hits do not concern editorial scope and were rejected.
- Body query: `rg -n -i 'levels.of.edit|substantive.edit|commission.*edit' kb/theory kb/reference kb/sources --glob '*.md'`. No prior Levels of Edit ingest found. Write-brief retention evidence concerns preserving commissioned content, not choosing an edit level; do not conflate them.
- Fully read the low-degree-of-freedom, author/executor and narrowing notes plus the one-improvement proposal. Read theory's collection contract for possible return edges.
- Link following: the low-degree note links the author/executor note, independently confirming the ownership/timing distinction. The proposal points to this workshop's open ordering question, but workshops are excluded from source outbound links. No external prospecting; only the source URL already captured is in hand.

### Candidate origins

- kb/theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md — known, titles, descriptions
- kb/theory/fix-what-the-executor-cant-determine-not-what-it-will.md — known, titles, descriptions, link-following
- kb/reference/proposals/one-improvement-procedure-over-atomic-instructions.md — known, titles

## Connections Found

- [Solve low-degree-of-freedom subproblems first](../../../../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) — **compares-with**: JPL's cumulative levels specify the work commissioned, whereas the note orders choices by remaining alternatives. This comparison prevents treating an ordered scope taxonomy as a temporal sequencing rule.
- [An author should fix what the executor can't determine](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) — **compares-with**: JPL distinguishes institutional minimums, author options, editor tasks and production responsibilities; the note explicitly separates decision ownership from timing. The reader gains a way to distinguish commissioning from ordering.
- [One improvement procedure over atomic instructions](../../../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md) — **see-also**: the proposal orders higher-order concerns before expendable wording work; JPL provides an adjacent editorial task taxonomy, not an established attribution for that ordering mechanism.

## Bidirectional Candidates

None. No published ingest exists yet; reciprocal value must be reassessed after the accepted analysis is available.

## Reverse-edge Candidates

None. Do not propose a theory citation to an unpublished ingest or an immutable private snapshot. Theory's contract permits source links, but no such edge can yet resolve to an accepted report.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Narrowing bought to survive review](../../../../theory/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — the source does not address analytic narrowing or content loss under review pressure. A broad substantive/language distinction does not independently warrant this connection.
- [Sources](../../../../sources/README.md) — a generic landing link adds no source-specific reader value.

## Index Membership

None.

## Synthesis Opportunities

None established. The distinction between edit scope, ownership and temporal order is a comparison to carry into drafting, not yet a new warranted theory claim.

## Maintenance Observations

None.

## Flags

- Pre-ingest discovery only. The source's numerical levels must not be read as an instruction to execute editorial tasks in that order.
- Historical dispatch error recovered: the initial `worker` name was not a project-agent lookup. A fresh `commonplace-worker` with `agentScope: project` subsequently drafted the accepted ingest at `kb/sources/levels-of-edit-1980.ingest.md`. This report remains the pre-ingest discovery observation; post-ingest discovery is separate. No suggested edges have been installed by connect.
