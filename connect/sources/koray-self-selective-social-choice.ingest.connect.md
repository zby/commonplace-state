---
description: "Discovery for the Koray ingest comparing formal uses of a rule at two levels."
type: types/connect-report.md
source: "kb/sources/koray-self-selective-social-choice.ingest.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Self-Selective Social Choice Functions

**Source:** [The published Koray ingest](../../../../sources/koray-self-selective-social-choice.ingest.md).

## Discovery Trace

- Scanned the sources, theory, reference, agent-memory-systems, agentic-systems and tags landings. The evaluation tag provides general orientation. No topic tag on the ingest.
- Generated the titles across these collections with `rg -N --no-filename -m1 '^# (.*)' -r '$1'`. Filtering for `voting|aggregation|on.balance|meta.criter|objective|deliberat|social choice` surfaced the note on revising an improvement objective and the note on local improvement judgments.
- Searched bodies for `social choice|self.selectivity|irrelevant alternatives|voting rule`; no earlier social-choice study appeared. Read descriptions of the theory notes with “objective” in their filename. Followed the objective revision note to its parent on declaring objectives and inspected the on-balance note's treatment of different comparisons.
- The memory and agentic system reviews deal with operational mechanisms. No alternative-selection rule operating on induced preferences surfaced there or in reference. Source provenance uses the supplied PDF; external sources were not prospected.

- Repeated the titles scan after publication using `self.select|reflective equilibrium|revising an improvement objective|on.balance`. Searched bodies for `preferences over rules|induced preferences|self.ratification|fixed point`. The new reflective-equilibrium ingest surfaced in both passes. Read it to check what remains fixed in each model, and followed Koray’s authored link back to the objective revision note. The note concerns terminal ends and does not require a return citation to a social-choice theorem.

### Candidate origins

- `kb/theory/revising-an-improvement-objective-is-licensed-from-outside-it.md` — titles, descriptions.

- `kb/sources/making-reflective-equilibrium-precise.ingest.md` — titles, body-search.

## Connections Found

- [Revising an improvement objective](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) — **compares-with**: Koray derives rankings of competing rules from the outcomes they select under a fixed preference profile. The note asks what would license changing the ends themselves. Readers can distinguish a discriminating self-selection test with supplied preferences from a successor objective's assessment of itself.

- [Making Reflective Equilibrium Precise](../../../../sources/making-reflective-equilibrium-precise.ingest.md) — **compares-with**: Koray asks whether applying a rule once to an induced choice of rules selects that same rule. The reflective-equilibrium paper iterates revisions of principles and commitments under a fixed score until neither changes. The second model explains what convergence would require in a question prompted by the first.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [On-balance judgments](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) assesses gains and losses across uses. Koray assumes strict voter rankings and supplies no way to estimate unknown costs or aggregate them into those rankings.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
