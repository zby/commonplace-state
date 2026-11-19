---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The bound does not fix its own N
  reason: 'N appears here for the first time and is never defined. The heading ("What
    kind of number a step size is") lets the reader guess that N is the step-size
    limit, but not what it counts: unquoted sources per note, artifacts opened, or
    something else. The note uses no formal arguments, so plain language such as "the
    maximum number of unquoted sources a note may cite" would serve better than the
    symbol.'
  level: warn
- scope: passage
  quotes:
  - Does not decide N, a validator rule that would enforce it
  reason: N is reused in Scope and in the Lamport paragraph ("any particular N").
    Each of these sentences only makes sense if the reader has inferred N's meaning
    from the earlier section. Replacing the symbol with a plain-language phrase throughout
    would remove the dependency.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/accessibility/notation-opacity.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/accessibility/notation-opacity.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: 1169b01cde2019fc32462be33de88364d0eebd8a030621ab4fd4143257dc17fe
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/1bbc6bed613a9216294347a0/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/1bbc6bed613a9216294347a0/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 4ed1fb58a1664f69922ea8d551eb75d5
completed-at: '2026-11-16T22:36:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/4ed1fb58a1664f69922ea8d551eb75d5/outputs/review-notation-opacity.md
raw-output-sha256: bae16a7c53f4c97856573fc9db3ac9ed5b5eeab516cab4c18e3450a22688138c
format: 2
---

# Review

## Summary

The note's only formal notation is the variable N, which names the step-size limit in the section "What kind of number a step size is", in the Lamport paragraph and in Scope. It is not given a local definition. The reader has to infer from the heading and the earlier argument that N counts unquoted sources per note. Since the note makes no equation or pseudocode argument, the gate prefers plain language over the symbol.

The inline code markers `verbatim` and `(snapshot required)` are not opaque notation: each is explained in its own sentence (substring match against the linked file; a source with no bounded passage that counts fully against the step).
