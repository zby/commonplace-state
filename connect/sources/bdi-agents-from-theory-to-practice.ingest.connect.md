---
description: "Inbound and outbound candidate comparisons for the OASIS schedule-retention example."
type: types/connect-report.md
source: kb/sources/bdi-agents-from-theory-to-practice.ingest.md
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: BDI Agents: From Theory to Practice (ingest)

**Source:** [Rao and Georgeff ingest](../../../../sources/bdi-agents-from-theory-to-practice.ingest.md)

## Discovery Trace

Used the sources, theory, reference, agentic-systems and historical agent-memory-systems README heads from the snapshot pass. The ingest carries no topic tags. Filtered fresh title listings across those destinations for `resource-bounded|\bBDI\b|retaining a decision|intention maintenance` and description listings for `intention reconsideration|reconsideration|\bBDI\b`. IRMA addresses why to reconsider; the reference vocabulary ledger uses reconsideration for a different job. Neither systems collection supplied a specific counterpart. No external prospecting.

Searched bodies for `OASIS sequencer|intention reconsideration|revising plans from outcomes`. This recovered Bratman, Israel and Pollack and Wooldridge and Jennings. Followed the ingest's BDI survey link: its discussion of plan selection versus learning is already reachable. Checked the survey's Intelligent Agents link: that paper offers a broader architecture classification rather than another implemented retention test.

### Candidate origins

- kb/sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md — known, titles, descriptions, body-search

## Connections Found

- [Plans and Resource-Bounded Practical Reasoning](../../../../sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md) — **compares-with**: IRMA's filter asks whether a new option merits deliberation despite a current plan. OASIS checks whether the current schedule can still be met. These tests can disagree when an alternative looks better but the existing schedule remains feasible.

## Bidirectional Candidates

- [Plans and Resource-Bounded Practical Reasoning](../../../../sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md) → Rao and Georgeff — **compares-with**: IRMA readers looking for a concrete reconsideration policy can inspect what evidence releases the OASIS sequencer from its commitment. The example illustrates a policy, not a measured gain over IRMA.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

The vocabulary collision ledger's conditions for reconsidering a writing decision are unrelated to runtime intention maintenance. A return link from the BDI survey is not needed merely because the ingest already cites it.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
