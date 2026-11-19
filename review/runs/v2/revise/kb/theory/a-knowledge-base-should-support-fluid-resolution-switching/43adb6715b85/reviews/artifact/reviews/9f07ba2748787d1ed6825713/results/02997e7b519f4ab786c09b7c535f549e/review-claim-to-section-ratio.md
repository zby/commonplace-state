---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - These questions identify possible friction. They do not yet supply a scoring rule
    or universal threshold.
  reason: This caveat repeats the opening section's statement that resolution-switching
    is 'a qualitative design criterion, not yet a metric'. It is one repeated sentence
    pair, not a section that only restates framing, so the claim-to-section balance
    holds.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/9f07ba2748787d1ed6825713/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/9f07ba2748787d1ed6825713/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: 02997e7b519f4ab786c09b7c535f549e
completed-at: '2026-11-16T22:29:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/02997e7b519f4ab786c09b7c535f549e/outputs/review-claim-to-section-ratio.md
raw-output-sha256: 7128cd568c40d7342e896dcf5bc3b635a504ce7f7f234ca158abb121345ce60a
format: 2
---

# Review

## Claims and sections

The note has six sections: the unheaded opening, Commonplace mechanisms, The evaluative criterion, Connection to discovery, Boundaries and Open questions.

It makes these distinct non-obvious claims:

1. A KB should make task-relevant switches between broad and detailed views inexpensive in both directions. Here, resolution means the scope and detail a view exposes, not an artifact's intrinsic abstraction rank. (Opening section.)
2. Four existing Commonplace mechanisms supply views of different scope or detail and the transitions between them. These are title, description and body tiers, index-to-note scope, link context and progressive-disclosure gradients. (Commonplace mechanisms.)
3. Fluidity is a criterion separate from retrieval accuracy. A system can retrieve the right detail and still lose its context, or give a good overview that never reaches the detail. The criterion breaks into selection, loading, recovery and relationship-preservation checks. (The evaluative criterion.)
4. Resolution-switching helps a reader assemble views for recognition, but it does not perform the recognition. (Connection to discovery.)
5. The criterion is distinct from addressability grain, pointer accuracy and recall. It also does not require an outbound link on every artifact, because backlinks, an index or search can supply the outward route. (Boundaries.)

Open questions is a support unit. It records the unresolved measurement choices that the note's "not yet a metric" qualification depends on.

## Assessment

There are six sections for five claims plus one necessary support unit, so sections do not outnumber the substance. Connection to discovery is short, but it carries its own bounding claim. Only one sentence pair repeats earlier framing (see the info finding). No section exists only to restate the argument.
