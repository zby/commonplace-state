---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Removing that stop requires deciding whether its check can be automated or is
    unnecessary
  reason: The linked routine-approvals note says removing an approval stop while preserving
    its protection requires automating the exceptional check or reliably excluding
    those cases from permitted work. It does not discuss judging the check unnecessary.
    The link is attached to the following clause about routine approvals, which matches
    the target, so the extra alternative is the note's own and is not load-bearing
    on the citation.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
note-sha256: 32c9c946ad8092a20aa5d4cfe1aa0e58bc5f9bfe61100f236c18efc78f6c479b
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
target-sha256: c3b814e077eaa68b1c25e9a772e98ac41b6b9bb452044d02fd88b442ed7f747f
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/acc834001d83f9c8862ba82f/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/acc834001d83f9c8862ba82f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews
launch: de7fc372ee05456c90ebf8e8b77b15fa
completed-at: '2026-11-17T07:56:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/calls/launches/de7fc372ee05456c90ebf8e8b77b15fa/outputs/review-grounding-alignment.md
raw-output-sha256: f2453bd1526d97ef6c2b235d492e48b22100b40b302b8196545c024a5325305e
format: 2
---

# Review

## Summary

The note links two library artifacts.

**Routine approvals.** The link text "routine approvals do not establish that human judgment is dispensable" matches the target's title claim and scope: repeated acceptance can conceal an exceptional-case check that has not been exercised. The note uses it for exactly that point in the "Required approval" case. The adjacent sentence's "or is unnecessary" alternative goes slightly beyond the target, recorded as INFO.

**Comparison of operative states.** The note says it "complements" the better-factory comparison and draws a non-entailment: a judgment that the system improved does not by itself show whether human evaluation was required to operate it. The target compares a predecessor and an adopted successor under an antecedent assessment relation and separates improvement from attribution. The note does not claim the target makes its point; it positions its own distinction beside the target's. This is a contextual, not evidential, use and is fairly represented.

No source ingests or quoted sources are cited.
