---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: 5f41ee7d471648bd8dc2062fcd7cd9df
completed-at: '2026-11-21T19:29:47Z'
findings:
- scope: passage
  quotes:
  - Adaptation takes effect immediately at deployment time without waiting for a retraining
    run
  reason: 'The sentence presents immediate deployment-time adaptation as a payoff
    of storing retained content in readable, addressable artifacts. The mechanism
    is the update path: artifact revision run within the deployed system''s operating
    cadence. The linked note explicitly separates lifecycle phase, update latency
    and representational form, and says ''during deployment'' does not by itself make
    a change fast. Readability is neither necessary nor sufficient for this payoff
    (online weight training also updates during deployment), so the framing misattributes
    the mechanism and overstates the speed.'
  level: warn
- scope: passage
  quotes:
  - cheap to revert
  reason: The worked example frames reversibility as how cheaply the line can be reverted,
    and the later on-balance paragraph cites this example as the use of 'reversibility
    to limit future loss'. The linked reversibility note says the time to edit an
    instruction does not bound how long it remains in use. What bounds the loss is
    how soon a mistake is detected and corrected, which losses stop at correction,
    and what has come to depend on the change. Framing the bound as revert cost points
    the reader at the wrong mechanism, using the note's own routing-instruction case.
  level: warn
- scope: passage
  quotes:
  - the bottleneck was always
  reason: The section claims that the bottleneck in all three precedents was what
    played the value-function role. Its own EURISKO paragraph, however, credits EURISKO
    with double-loop criterion revision and attributes its limit to brittle symbolic
    heuristics and repeated human intervention, which are problems of representation
    and credit assignment. 'Always' frames every precedent through the judge slot,
    which excludes mechanisms the section itself reports.
  level: warn
- scope: passage
  quotes:
  - Deployment time, taking effect on the next task that reads the store
  reason: 'The table presents update timing as a structural axis separating deliberative
    learning from weight training. Timing is a lifecycle property: weights can be
    updated online during deployment, and a store can be edited offline. The row emphasizes
    the typical case rather than a defining contrast.'
  level: info
- scope: passage
  quotes:
  - weights-only continual learning wins those domains
  reason: Failure of automated language-model judgment would defeat this bet. It would
    not by itself establish that weights-only learning wins, since human-judged or
    hybrid loops would remain. The conclusion is framed as a two-way contest that
    the stated test does not decide.
  level: info
contract: verdict
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/5f41ee7d471648bd8dc2062fcd7cd9df/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/c93c705ebe56c662d5bb094d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/5f41ee7d471648bd8dc2062fcd7cd9df/outputs/review-framing-mismatch.md
raw-output-sha256: 527b6782cc7fb171f0f3389f43c9009757ba7f68a3dc620145c84ef1fc53d820
---

# Review

## Summary

Three passages misidentify the mechanism behind a claim. The first payoff of readable storage credits form with a speed benefit that comes from the update path. The routing-line example, reused as the article's illustration of reversibility, frames reversibility as cheap reverting rather than as bounded detection and correction. That is the mistake the linked reversibility note warns against. The precedents section says the value-function role was "always" the bottleneck, but its own EURISKO paragraph points to brittle representation and human intervention. Two further framings emphasize one case without strictly excluding others and are recorded as info.
