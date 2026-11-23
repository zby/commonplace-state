---
description: "Where readers need the 1987 PRODIGY rule derivation rather than the later retention experiments."
type: types/connect-report.md
source: kb/sources/minton-carbonell-learning-search-control-rules.ingest.md
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Minton and Carbonell on learning search control rules

**Source:** [Published ingest](../../../../sources/minton-carbonell-learning-search-control-rules.ingest.md)

## Discovery Trace

Scanned the README heads and generated titles in sources, theory, reference, agent-memory-systems, agentic-systems and tags. Filtered titles by `failure explanation|utility of explanation|fixed decomposition|search control rules`; searched descriptions with `^description:.*(winning or losing|failed branch|PRODIGY)` and bodies with `PICKUP.{1,12}UNSTACK|AvrMatchCost`. No source tags. The agent-memory trace-learning comparison and improvement-loop tag span more mechanisms than this worked example needs. Reference and agentic-systems yielded no closer source for the derivation. Followed the ingest’s links to the failure note, Minton 1988 and the fixed-decomposition note. The last has evidence about restricted update spaces; the 1987 paper does not test what happens when those spaces are wrong. No external prospecting.

### Candidate origins

- kb/theory/failure-explanation-changes-later-branch-decisions.md — known, titles, descriptions, link-following
- kb/sources/minton-utility-of-ebl-aaai88.ingest.md — known, titles, descriptions, body-search, link-following

## Connections Found

- [1988 utility study](../../../../sources/minton-utility-of-ebl-aaai88.ingest.md) — **compares-with**: retain the existing distinction between the stated utility criterion and later measured retention outcomes.
- [Failure and subsequent choices](../../../../theory/failure-explanation-changes-later-branch-decisions.md) — **compares-with**: the worked failure proof changes the conditions under which the solver chooses an operator.

## Bidirectional Candidates

- [Failure and subsequent choices](../../../../theory/failure-explanation-changes-later-branch-decisions.md) — **evidenced-by** (qualifies): a reader can distinguish excluding PICKUP for a reason that generalizes from merely explaining how UNSTACK succeeded. This is a worked case of changing a decision, not evidence of net speedup. Cite the ingest with `(snapshot required)` unless the supporting passage is retained.
- [1988 utility study](../../../../sources/minton-utility-of-ebl-aaai88.ingest.md) — **compares-with**: readers of its cost measurements need the earlier worked derivation to see why which branch is explained affects the scope of the rule being priced.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

No return link from the fixed-decomposition note: the unchanged proof schemas delimit this learner, but the worked case does not expose a mistake outside its update space.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
