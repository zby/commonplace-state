---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A reader using a knowledge base alternates between broad views that expose possible
    routes and narrower views that supply detail.
  reason: The opening premise is stated as a behavioural observation about readers
    generally, with no evidence or derivation. The normative 'should' rests on it.
    The claim is qualitative and plausible, and the later 'Fluidity is relative to
    the task' softens it, so a reader can recover it as the note's framing premise.
    It still reads more like a reported observation than an assumption.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
note-sha256: 0519683dd2a2ad488108c956b1c1a59791f57be492893178645772a263c8257f
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/86b40ed780de218f2ce18478/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/86b40ed780de218f2ce18478/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: bc277cf6d61d4be6914a3ce31a323912
completed-at: '2026-11-16T22:32:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/bc277cf6d61d4be6914a3ce31a323912/outputs/review-epistemic-status-blur.md
raw-output-sha256: 2dca8ab3ef748504720a23d135734dda3411b8687b367cb3c88bc28b7b7bfac6
format: 2
---

# Review

## Summary

The note labels its central construction honestly. The criterion is "a qualitative design criterion, not yet a metric". The four questions "identify possible friction" and "do not yet supply a scoring rule or universal threshold". Measurement choices are deferred to Open questions. These markers sit next to the claims they govern.

The mechanism paragraphs describe how existing Commonplace surfaces expose different scope or detail. Where they depend on another note, such as title-as-claim traversal or pointer trade-offs, that note is cited for its own claim. The note does not let that support stand in for a different claim. The Discovery section explicitly limits what switching achieves: "it does not perform the recognition or guarantee a discovery." The contrast with retrieval accuracy is phrased as a possibility ("a system may retrieve...").

The only soft spot is the opening alternation premise, which is stated as an observation and not as an assumption (INFO). No load-bearing mechanism or conjecture reads as established, and no well-supported finding is over-hedged.
