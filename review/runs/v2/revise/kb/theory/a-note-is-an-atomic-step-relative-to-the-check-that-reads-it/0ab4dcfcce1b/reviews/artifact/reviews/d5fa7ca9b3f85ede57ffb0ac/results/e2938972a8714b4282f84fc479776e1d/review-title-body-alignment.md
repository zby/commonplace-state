---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - when the claim, the material it cites, and the inference from that material to
    the claim can be checked in one pass by the check that will be applied to it
  - a note can satisfy one and fail the other
  reason: 'Claim drift. The H1 reads as an unconditional statement that a note is
    an atomic step, qualified only by which check is meant. The body defines atomicity
    as a condition a note may fail: a note is an atomic step only when its claim,
    cited material and inference fit one pass of the applied check. It then shows
    notes that fail it, such as the eight single-claim notes citing six to nine sources.
    What the body establishes is that whether a note is an atomic step depends on
    the check that reads it, and that a note can fail that bound while satisfying
    the co-loading bound. A title such as ''Whether a note is an atomic step depends
    on the check that reads it'' would match.'
  level: warn
- scope: passage
  quotes:
  - This note states the rule for one check, Commonplace's grounding check, because
    that is where the unit of cost is clear
  reason: 'Scope drift, minor. The title states the general relativity claim. Most
    of the body argues narrower and prescriptive claims for the grounding check: the
    size bound belongs on the artifact rather than as a review budget; the unit of
    cost is the unquoted source; and N is a convention chosen for auditability. The
    body asserts the general relativity and backs it by linking to the oracle-domain
    and automation-verification notes. The description signals the grounding-check
    focus, so this is informational, not a mismatch.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: 807525e249f2e9eb743b80728b60f2d5a3c29a5f61921fd8949a65d2bebf5712
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/d5fa7ca9b3f85ede57ffb0ac/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/d5fa7ca9b3f85ede57ffb0ac/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: e2938972a8714b4282f84fc479776e1d
completed-at: '2026-11-16T22:36:28Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/e2938972a8714b4282f84fc479776e1d/outputs/review-title-body-alignment.md
raw-output-sha256: 98c8b524670f154ea7776eb06b63c01e397011f0c575cb2cb9d46e1e6d0dc6b5
format: 2
---

# Review

## Summary

The title "A note is an atomic step relative to the check that reads it" is broadly supported. The body says explicitly that "a step is atomic relative to a particular check". Two alignment issues remain.

First, the title's wording asserts that a note *is* an atomic step. The body treats atomic-step status as a conditional property that a note may lack, and the corpus section rests on notes that are not atomic steps for the grounding check. A reader linking the title as a premise could take it to say that every note is one step for its check. The body denies that. This is a warn-level claim drift, fixable by rephrasing the title around dependence ("whether a note is an atomic step depends on…").

Second, most of the body develops grounding-check-specific and prescriptive claims (artifact-side placement, the unquoted source as unit, N as an auditability convention). The general title does not foreshadow them. The note scopes itself explicitly and the description carries the grounding-check focus, so this is recorded only as information.
