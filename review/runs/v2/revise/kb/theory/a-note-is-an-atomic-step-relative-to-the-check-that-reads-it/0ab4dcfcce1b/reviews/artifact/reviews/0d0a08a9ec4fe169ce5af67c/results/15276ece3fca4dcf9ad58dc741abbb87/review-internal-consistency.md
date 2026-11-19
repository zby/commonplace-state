---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - into a check that costs the reviewer nothing
  reason: The closing summary says the validator turns 'this passage says this' into
    a check that costs the reviewer nothing. Earlier, the note says the reviewer still
    has the support judgment after quoting ('It costs attention, and nine quoted passages
    cost more than one'), and that occurrence is not representativeness. The closing
    sentence is true only if 'says this' means bare occurrence. Read as support, which
    is how the earlier sections use 'this passage ... this claim', it contradicts
    them and drops a tension the body keeps.
  level: warn
- scope: passage
  quotes:
  - for two reasons that have nothing to do with each other
  reason: The opening says the two bounds have nothing to do with each other. The
    mechanism section later says they are 'independent as constraints but coupled
    through this remedy', because quoting spends against the co-loading bound. The
    later qualification is consistent with independence as constraints, but the opening
    wording is stronger than the body supports.
  level: info
- scope: passage
  quotes:
  - The two placements differ in their failure mode, not in the constraint they express.
  reason: 'The step-size section then names a second difference: a small artifact-side
    step buys auditability ''that a well-calibrated reviewer budget does not''. The
    constraint the two placements express may therefore also differ (a per-note bound
    versus a per-review reading limit). This may be definition drift and needs the
    author to confirm.'
  level: info
- scope: passage
  quotes:
  - They are not atomic steps for the grounding check, because checking one means
    opening six to nine artifacts
  reason: The mechanism section counts only unquoted sources against the step. This
    paragraph counts every cited source and assumes each must be opened. The two agree
    only if none of the eight notes quotes its sources, which the paragraph does not
    say.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/0d0a08a9ec4fe169ce5af67c/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/0d0a08a9ec4fe169ce5af67c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 15276ece3fca4dcf9ad58dc741abbb87
completed-at: '2026-11-16T22:40:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/15276ece3fca4dcf9ad58dc741abbb87/outputs/review-internal-consistency.md
raw-output-sha256: bfae0bbe7d977b98e7fed09c5297611dfdd061e37fbb0b950bd882b436282a38
format: 2
---

# Review

The note's main claims are consistent with one another:

- the two bounds are distinct;
- atomicity is relative to a check;
- the grounding check's unit is the unquoted source;
- the artifact-side placement fails loudly;
- N is a convention, while the note leaves its value undecided.

The Scope section matches the body. Calling N "a convention" is consistent with "does not decide N", because the note fixes what kind of number N is, not its value.

The clearest inconsistency is in the closing sentence of the precedent paragraph, which works as a summary of what the knowledge-base case adds. It says the validator makes the common step free for the reviewer. The body instead says that the validator removes the finding step, and that a support judgment remains which costs attention. The other findings concern wording drift that the body partly resolves: the bounds' independence, what differs between the two placements, and how sources are counted in the corpus example.
