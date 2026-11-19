---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: 38f8db3bc86fa1eaa16a1a1fa1652779f9371be9baa68043c721172d2bcd8543
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 8ea50ee87b254f939a325dc78bb9d397
completed-at: '2026-11-16T17:38:10Z'
findings:
- scope: passage
  quotes:
  - This note uses "test record" where it earlier used "warrant". "Warrant" covered
    both truth and support, and the first two questions need to be kept apart.
  reason: This terminology-history paragraph sits between the three-question frame
    and the first argued section. It records a revision of the note rather than serving
    the claim. The reader passes through it at the point where the core claim should
    carry straight into its support. Cutting it, or moving the terminology rationale
    to the commit history, would keep the opening tight. The rationale that truth
    and support must be kept apart is already carried by the next section.
  level: info
contract: verdict
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/bbdf143c56b0b566cb06ffa2/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/bbdf143c56b0b566cb06ffa2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/8ea50ee87b254f939a325dc78bb9d397/outputs/review.md
raw-output-sha256: 80eca87ccaf027e5ed84f3dd920d7ad08940a58b7912cd1819f75824d0c96e56
---

# Review

## Core claim

In one sentence: a claim's truth, its test record of independent tests survived, and its fit in a working theory are three separate standings, and agreement with the theory adds to the test record only where the claim could have failed.

## Prominence

The title states the test-record/fit half of the claim. The first paragraph states the full three-way separation ("no answer to one settles another"). The three bullets then define each standing compactly. Each later section argues one separation or one consequence: test record vs truth, test record vs fit, fit vs test, their interaction, and contradiction repair. The Scope section limits the claim without burying it. The apparatus therefore serves the claim in order, and the claim is easy to restate after one reading.

One small piece of apparatus does not serve the claim. The paragraph about the earlier term "warrant" is revision history placed directly after the frame. It is short and does not hide the claim, so this is INFO rather than WARN. The simplest fix is to delete it.

The title names only one of the three separations, and the description carries the fuller claim. This is a reasonable title-as-claim choice. It does not obscure the note's main point.
