---
description: Retention and reuse comparisons for Aamodt and Plaza's CBR survey.
type: types/connect-report.md
source: kb/sources/.snapshots/aamodt-plaza-1994-case-based-reasoning.md
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Aamodt and Plaza on case-based reasoning

**Source:** [Aamodt's full-text PDF](https://www.idi.ntnu.no/~agnar/publications/aicom-94.pdf)

## Discovery Trace

Scanned the theory, reference, sources, agent-memory-systems, agentic-systems and tags README headings, then searched titles for `case-based|deliberative learning|reasoningbank|dynamic cheatsheet|learning from experience`. The memory reviews supplied a direct modern comparison. Description search for `reasoningbank|case-based reasoning|deliberative learning` confirmed its scope. Body query `failure cases|case-based reasoning` also found source reports and type/placement rules; incidental failure examples do not explain retention. Dynamic Cheatsheet was less specific to outcome-conditioned extraction. Followed ReasoningBank's link to the trace-extraction requirement and checked its treatment of updates to existing items. No source tags to traverse; no external prospecting.

### Candidate origins

- kb/agent-memory-systems/reviews/reasoning-bank.md — titles, descriptions
- kb/theory/agent-memory-requirements/use-trace-extraction-as-meta-learning.md — link-following

## Connections Found

- [ReasoningBank](../../../../agent-memory-systems/reviews/reasoning-bank.md) — **compares-with**: both success and failure can supply later advice, but this benchmark system extracts text and selects a prior query by embedding rather than revising a case index using feedback.
- [Use trace extraction as meta-learning](../../../../theory/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) — **compares-with**: the requirement asks whether learning can modify existing memory; CBR includes changes to the features that retrieve existing cases even without adding a case.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

The content-routing ADR addresses placement in Commonplace, not choosing which features will retrieve a failure later.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
