---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/sentence/stock-phrases.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 6e2bd9a71d2685b71fc1641640e684574da24f3115f005263a75367c0dc6c29c
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T132933Z/artifact/reviews/3870487350f9a4b6d7cbc816/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T132933Z/artifact/reviews/3870487350f9a4b6d7cbc816/observation.json
contract-sha256: 9969d7db1b8228822ac807fdc50483981fc6d62c7effbe601a7de3fac2e131a0
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T132933Z
launch: b0f93e5dc5ce4f45adf47dc34c8dccd2
completed-at: '2026-11-15T13:29:58Z'
raw-output: kb/reports/state/review/runs/v2/20261115T132933Z/calls/launches/b0f93e5dc5ce4f45adf47dc34c8dccd2/outputs/review.md
raw-output-sha256: 4765d2b27e813fd4e5f40ecbbcebb9693bf77cbb03241f88f908c4728cacd9ee
format: 2
---

# Review

## Summary

No sentence in the body uses a listed stock pattern ("not just X — it is Y", "It's worth noting", "In other words", "At its core", "The key insight here is"). I also gave the deletion test to the sentences that come closest to stock framing, and each one keeps content the paragraph needs.

## Sentences tested

- "The two failure modes are not symmetric, and the rule rides entirely on that." This is a topic sentence that the section heading partly anticipates. It still asserts that the rule depends *entirely* on the asymmetry, and no later sentence states that dependence. Deleting it would remove that claim.
- "A bounded, recoverable downside on one side; a silent, unbounded one on the other — that is why hand-maintained-and-trusted is *forbidden* rather than merely risky." The first clause restates the previous paragraph. The sentence then draws the conclusion "forbidden rather than merely risky", which appears nowhere else.
- "This looks like it reopens the regress, but it doesn't: ..." This raises an objection and answers it with specific mechanisms (centralization, versioning, amortization). It is not filler.
- "The spread is what shows it generalizes" and "It is the general form of 'a cache must never be the only copy'..." Each makes a specific claim: the first ties the four instances to generality, and the second links the rule to a familiar caching principle.
- "Two things change." This is a short signpost before an enumeration. It counts the items and adds no stock content.

None of these sentences fails the deletion test, so there are no findings.
