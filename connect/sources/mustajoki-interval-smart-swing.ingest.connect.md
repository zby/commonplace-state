---
description: "Candidate connections for Decision Support by Interval SMART/SWING and Commonplace judgments about improvement."
type: types/connect-report.md
source: "kb/sources/mustajoki-interval-smart-swing.ingest.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Decision Support by Interval SMART/SWING

**Source:** [Published ingest](../../../../sources/mustajoki-interval-smart-swing.ingest.md).

## Discovery Trace

- Reviewed the theory, sources, reference, agent-memory-systems, agentic-systems and tags landings. Evaluation includes judgments about improvements. The system reviews address implementation; no analogous formal comparison was located.
- Generated titles across the six destinations with `rg -N --no-filename -m1 '^# (.*)' -r '$1'` and filtered for `trade.off|on.balance|criterion|reflective equilibrium|aggregation`. Searched bodies for `reasonable weights|weight settings|preference relation|declared objective|global measure`. The on-balance note and reflective equilibrium ingest offered distinct interpretations of leaving a measure unspecified.
- Followed the on-balance note to its parent about a declared objective. This establishes whose objectives are being considered but gives no technique for resolving disagreements among the alternatives. The source collection excludes the active workshop from authored links.

- Read the published ingest, searched neighboring collections again for `dominance|pairwise score difference|interval judgments`, and checked the transfer against the limitations in the ingest. Both systems must be compared under the same weights. Independently optimizing their scores may hide dominance. This makes the pairwise difference a useful calculation for the on-balance note.

### Candidate origins

- `kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md` — titles, body search.
- `kb/sources/making-reflective-equilibrium-precise.ingest.md` — titles, body search.

## Connections Found

- [On-balance judgments](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) — **compares-with**: The source formalizes ratio intervals and tests which alternatives are dominated over permitted weights. This targets the cost comparison when a precise compromise is unavailable.
- [Making Reflective Equilibrium Precise](../../../../sources/making-reflective-equilibrium-precise.ingest.md) — **compares-with**: One paper tests elicitation of permitted ratio ranges, while the reflective-equilibrium model holds the admissible weight region given and studies stability within it.

## Bidirectional Candidates

- [On-balance judgments](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) — **evidenced-by**: The study provides a worked case in which one can rule out options despite leaving trade-offs within intervals; its measured discrimination depends on reference attribute and elicitation conditions.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Declared objective](../../../../theory/self-improvement-is-relative-to-a-declared-objective.md) deals with prior identification of an objective; it does not discuss how a family of functions can express a comparison.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
