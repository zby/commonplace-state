---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/an-assumption-based-tms.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: An Assumption-based TMS

**Source:** [An Assumption-based TMS](../../../../sources/.snapshots/an-assumption-based-tms.md)

## Discovery Trace

**Description listing scan:** Scoped description and H1 scans over every source-authorised local destination highlighted atomic claims, provenance/lineage, and truth-maintenance comparisons.

**Topic indexes:** Read the notes, reference, agent-memory, and agentic-system indexes. Agent-memory reviews offered implementation comparisons, but methodology notes provide the clearer authored landing surface.

**Body search:** `rg -n -i "belief base|belief revision|contraction|dependency|dependencies|assumption set|truth maintenance|warrant" ...` found claim-level checking and multiple memory-system truth-maintenance discussions. `rg -l -i "dependency|assumption|warrant" kb/notes` narrowed the theory candidates.

**Link following:** Followed the atomic-step note through grounding and oracle-domain links. The kept candidates concern explicit dependency records and their limits; database systems using “dependency” only operationally were rejected.

## Connections Found

- [A note is an atomic step relative to the check that reads it](../../../../notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) -- **compares-with**: ATMS labels maintain conclusions relative to assumption environments, a formal comparison point for Commonplace's claim-level source and check dependencies.
- [A claim's warrant does not determine its fit in a working theory](../../../../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md) -- **compares-with**: ATMS records inferential dependence and consistency across contexts but does not establish whether assumptions or derived claims are empirically warranted.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [A note is an atomic step relative to the check that reads it](../../../../notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) → future ingest -- **external source support**: ATMS provides a canonical formal case of explicitly recording which assumptions support a conclusion.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Many-to-many edge state is where files yield to a database](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) -- rejected because shared vocabulary around dependencies does not establish a useful architectural comparison without an ATMS implementation target.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Keep the source's scope narrow: dependency maintenance establishes conclusions relative to assumptions, not the truth or empirical warrant of those assumptions.

