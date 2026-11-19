---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the author, who knows which passages
  reason: If the author is an agent, 'knows' attributes a mental state the note does
    not defend. The sentence only needs the author to have the passage-to-claim mapping
    at hand, which 'the author, who selected the passages that jointly carry the claim'
    states without the cognition claim. Low impact because the author may equally
    be a human maintainer.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/prose/anthropomorphic-framing.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: 292f7c4bfb6506b864f941203c574f8d8fd7e0ecf63ad5d4bc27d6c4405907e3
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/3b066312ec0540aabfdf979f/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/3b066312ec0540aabfdf979f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: be5d160b4a174e6cb56e033b12532e2d
completed-at: '2026-11-16T22:37:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/be5d160b4a174e6cb56e033b12532e2d/outputs/review-anthropomorphic-framing.md
raw-output-sha256: 1801adf9e2e296d91212af8b34406f95e0d44fd87f464732d5fdd9122126bfc9
format: 2
---

# Review

The note's agents are reviewers, validators and authors, and it describes them almost entirely through observable behaviour: a reviewer "stops at its limit and returns a pass", "had opened" artifacts, "honoured its cap"; verdicts "disagree with themselves on unchanged input". These are behavioural descriptions or conventional software metonymy and make no claim about model internals. "A model's context is finite" is technical, not anthropomorphic.

The one cognition verb is "knows" in the joint-support paragraph. It is mild and the author role in this KB can be human or agent, so it is recorded as INFO only.
