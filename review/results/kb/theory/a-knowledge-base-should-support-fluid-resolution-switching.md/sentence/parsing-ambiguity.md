---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: 02a0da1552d64a10a5644fda428e405a
completed-at: '2026-11-16T22:30:40Z'
findings:
- scope: passage
  quotes:
  - How should a test distinguish a genuine dead end from a route intentionally supplied
    by search or backlinks rather than an authored outbound link?
  reason: 'The phrase ''rather than an authored outbound link'' can attach to ''supplied
    by'' (intended: a route supplied by search or backlinks instead of by an authored
    link). It can also attach to ''distinguish ... from'' (distinguish a dead end
    from a search route rather than from an authored link). The intended reading is
    the likelier one. Writing ''a route that search or backlinks supply instead of
    an authored outbound link'' would settle the attachment.'
  level: info
contract: verdict
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/63f170f211276dcd4d4e6b40/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/63f170f211276dcd4d4e6b40/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/02a0da1552d64a10a5644fda428e405a/outputs/review-parsing-ambiguity.md
raw-output-sha256: 0a39d64ed2035b1477c8428fd6549ec642f2455a4ffce38d9d36f6154f910a62
---

# Review

Negation scope is clear throughout. "not an intrinsic abstraction rank", "not yet a metric", "does not by itself determine", "does not perform the recognition" and "Nor does every task need" each negate the intended constituent.

Pronoun references resolve from local context. "its role" in the link-context paragraph most naturally refers to the link's relation, and either antecedent (the link or its relation) gives the same meaning. "Those properties" refers to pointer accuracy and retrieval recall, and "both" refers to search and link-following.

The only attachment question is the INFO finding in the open questions.
