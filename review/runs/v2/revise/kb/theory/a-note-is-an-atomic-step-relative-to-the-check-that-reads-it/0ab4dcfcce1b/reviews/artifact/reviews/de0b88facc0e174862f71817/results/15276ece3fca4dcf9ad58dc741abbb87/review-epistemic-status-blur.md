---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - an absence of that kind is a validator's result rather than a reviewer's finding
  reason: This is stated as an established fact about the system, but the only validator
    the note describes (ADR 046) resolves quotations that are present and marked verbatim;
    it does not detect that a claim lacks a retained passage. The sentence carries
    the counterfactual of a proposed artifact-side bound with the confidence of the
    reported experimental findings next to it, so those findings appear to show more
    than they do.
  level: warn
- scope: passage
  quotes:
  - on this evidence it is not a reviewer capacity exhausted at current corpus sizes
  reason: The observation (uncapped reviewers read up to 22 artifacts and the three
    largest offers passed) is presented as supporting a conclusion about reviewer
    capacity. A PASS on the largest notes has no ground truth to compare against,
    so the observation cannot distinguish 'no loss' from 'undetected loss'. 'On this
    evidence' marks the source but not the gap, so support for one claim is presented
    as covering another.
  level: warn
- scope: passage
  quotes:
  - the bound is held by a validator that fails the note, not by a reviewer that stops
    reading
  reason: The artifact-side bound and its enforcing validator are the note's own proposal
    (the Scope section says it decides neither N nor a validator rule), but this section
    describes them in a present-tense declarative register. A reader can recover the
    proposal status only from the distant Scope section.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
note-sha256: 93d1bb6d6123b6874693cda7fb7f196669f4741d3d823e54b124df0bb4ef25af
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/de0b88facc0e174862f71817/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/de0b88facc0e174862f71817/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 15276ece3fca4dcf9ad58dc741abbb87
completed-at: '2026-11-16T22:40:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/15276ece3fca4dcf9ad58dc741abbb87/outputs/review-epistemic-status-blur.md
raw-output-sha256: 65a5f3d29c615c1c8d0b576c1f59a7a176247b0e03bbee562cc1a98185410c00
format: 2
---

# Review

Much of the note keeps its statuses recoverable. Corpus counts and the paired experiment are reported observations and are bounded in Scope. The relativity claim is derived from linked premises. The Descartes and Lamport material is marked as analogy, and the open questions are labelled.

Two passages blur status. In the first, the remark about the four uncapped findings goes beyond reinterpreting them: it states that an absence of retained support "is a validator's result". That presents a capability the described validator lacks, as if it followed from the experiment. In the second, the absence of divergence among the largest-offer notes is presented as evidence about reviewer capacity, but the experiment could not observe loss in those cases. The artifact-side bound is written in present tense throughout its section. Because Scope marks it as undecided, that is informational only.
