---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 03f8ecc957f3412aa4a0e3220de09847
completed-at: '2026-11-16T22:38:45Z'
findings:
- scope: passage
  quotes:
  - Stated for Commonplace's grounding check. The relativity claim is general; the
    unit — the unquoted source — is derived from that check's cost structure and would
    have to be re-derived for any other check.
  reason: This Scope bullet restates the opening section's sentence 'This note states
    the rule for one check, Commonplace's grounding check, because that is where the
    unit of cost is clear; the same argument would need its own unit for any other
    check.' It adds no boundary case, condition or consequence. Cut the bullet, or
    cut the earlier sentence and keep the scope statement only here.
  level: warn
- scope: passage
  quotes:
  - Does the artifact-side bound have a cost the review-side one avoids
  reason: 'The mechanism section already states this cost and its resolution: a claim
    whose joint support cannot be quoted within a co-loadable note ''has only the
    snapshot route or a split left''. Framing the same point as an open question repeats
    what the body admits, and it makes the body''s answer look unsettled. Cut the
    question, or narrow it to what is still open, such as how often such claims occur.'
  level: warn
- scope: passage
  quotes:
  - whether a passage was lifted out of a qualifying context still costs a trip to
    the source, so the audit the bound buys is of the step the validator did not do,
    not of the one it cannot
  reason: Defensive redundancy. The mechanism section already says 'Occurrence is
    not representativeness' and that a reader who suspects lifting 'has to open the
    source after all'. Restating that limit inside the auditability argument pre-empts
    an objection the note has already closed, and it slows the paragraph's main point.
    Keep at most a short pointer back to the earlier limit.
  level: warn
contract: verdict
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/e9c5fa6e39bdd9ad23c0d71a/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/e9c5fa6e39bdd9ad23c0d71a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/03f8ecc957f3412aa4a0e3220de09847/outputs/review.md
raw-output-sha256: 66ec8dacbf59228913be82cc83773ce841288801c854dff6819d6c0f0371fc6e
---

# Review

The note mostly earns its length. It separates the two bounds, gives the artifact-side placement its own failure-mode argument, explains why quoted sources drop out of the grounding cost, rereads the corpus and experiment evidence, and uses the precedents to support checker-relative sizing. Several passages restate earlier material but do new work, so they were not flagged:

- "The bounds are independent as constraints but coupled through this remedy" adds the coupling.
- The Lamport paragraph's limit on the analogy blocks a real overreach about carrying N over.
- The paragraph ending in auditability adds the self-disagreement justification.

Three chunks do not earn their current form:

- The first Scope bullet duplicates the opening section's statement that the note covers only the grounding check and that the unit must be re-derived for other checks.
- The second Open Question asks about a cost that the joint-support paragraph has already stated and resolved.
- In the section on what kind of number a step size is, a hedge about passages lifted out of context restates the earlier "occurrence is not representativeness" limit. It defends against an objection the note has already answered.

The other Scope bullets pass. The validator dependency states the counterfactual "without that validator", the N bullet adds what is left undecided, and the corpus bullet bounds how far the evidence generalizes.
