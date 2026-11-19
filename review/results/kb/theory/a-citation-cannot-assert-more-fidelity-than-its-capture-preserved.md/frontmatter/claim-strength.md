---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: f0c584e0d37c1358bc0c771f0f367626578aa1df7c434bf040a085edef8f46cd
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
criterion-sha256: 8e4666d11f54dfcb2ef8de2c1942bb8fa7d77bd1fb54fec00bb5794bf4642367
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 2b0b48af273645b5b65754ed36a6ff44
completed-at: '2026-11-16T22:08:51Z'
findings:
- scope: document
  quotes: []
  reason: Read loosely as 'downstream work cannot recover what capture lost', the
    title is close to a garbage-in-garbage-out truism. The contestable content is
    that no notation, locator type or review gate can raise fidelity and only re-capture
    can. An informed designer could reasonably argue the opposite, for example that
    a richer span locator or a stricter verification gate repairs provenance. The
    title implies this through 'cannot assert' and 'capture preserved', but does not
    state it outright.
  level: info
contract: verdict
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/422f2e36132209216f3938e2/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/422f2e36132209216f3938e2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/2b0b48af273645b5b65754ed36a6ff44/outputs/review-claim-strength.md
raw-output-sha256: 48dadb677b424bc20d19c7f801abd435d1799cba48305dd4fcda6597214b7e00
---

# Review

The title makes a contestable claim. Someone informed could reasonably hold the opposing view: that downstream citation machinery can improve a citation's provenance grade. Examples are structured locators, `verbatim` markers checked by gates, and post-capture verification. The note argues against exactly that position, and the title commits to the side that can be disputed.

The weakest reading of the title is the general principle that a derived artifact cannot exceed the quality of its input. That reading is hard to dispute. The title still goes beyond it by placing the bound at capture and by denying that a citation's own assertion can move it. That gives the title enough contestable content to pass. The info finding records that adding "only re-capture raises it" to the title would make the sharper point explicit.
