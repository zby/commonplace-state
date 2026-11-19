---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - which is an instance of the general rule that
  reason: The sentence that states the title claim (a step is atomic relative to a
    particular check) continues through two inline related-note links and a gloss
    of oracle domain before the paragraph returns to its example. The relativity claim
    is the note's thesis, but here it reads as one clause in a chain of supporting
    citations. Ending the sentence at 'relative to a particular check' and moving
    the two grounding links to the footer, or to a short follow-on sentence, would
    let the thesis stand alone.
  level: info
- scope: passage
  quotes:
  - The bounds are independent as constraints but coupled through this remedy
  reason: 'One paragraph carries three separate points: quote jointly supported claims
    rather than split them, quoting spends against the co-loading bound, and links
    to other notes are not sources. The coupling point qualifies the opening''s claim
    that the two bounds ''have nothing to do with each other'', so it should be easy
    to find. Here it sits between the archived-proposal aside and the links-are-not-sources
    point. Splitting the paragraph, and moving the links-are-not-sources sentence
    to the start of the mechanism section where the source unit is defined, would
    make the coupling easier to see.'
  level: info
- scope: passage
  quotes:
  - The value is not that the reviewer copes, but that the review becomes auditable
  reason: The note's answer to why the bound belongs on the artifact is split. The
    placement section gives the silent-failure argument early, but auditability, the
    payoff the note values most, appears only near the end in the section about what
    kind of number N is. A reader can state the title claim after one reading but
    may not keep the reason it matters. One sentence in the placement section that
    previews auditability would connect the two.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/5919a3bb645bf2b400f20b6a/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/5919a3bb645bf2b400f20b6a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 340887a3a52e40c6b80772c6c9cb1005
completed-at: '2026-11-16T22:38:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/340887a3a52e40c6b80772c6c9cb1005/outputs/review.md
raw-output-sha256: 9b6dfa9b14930ee9228b1423ed2323c2a8d83fbd88bed263653fd06717c4e54f
format: 2
---

# Review

## Core claim

In one sentence, the note's strongest claim is this: a note is bounded twice, independently. The first bound is one claim sized to the reader's co-loading context. The second is one inference that the check applied to it can verify in a single pass. For Commonplace's grounding check, the unit of that pass is the unquoted source, because validated verbatim quotes move the work of finding support into code.

## Prominence

The note mostly keeps this claim in view. The title states the relativity claim. The first four paragraphs introduce the two bounds, define the atomic step, and state that the bounds differ and that atomicity depends on the check. Later sections serve the claim in a clear order. Placement argues for the artifact-side bound. Mechanism derives the unit. The corpus section shows that the bounds diverge. The "kind of number" section sets what N measures. The precedents are kept to analogy, and the Scope section limits the claim's reach. None of this material buries the thesis, so the result is not WARN.

## What makes it less memorable

Three local shapes weaken uptake:

- The relativity claim reaches the reader in the same sentence as two inline links to supporting notes.
- The coupling between the bounds, which qualifies the opening's "nothing to do with each other", is buried in a paragraph that makes three separate points.
- Auditability, the main reason the artifact-side placement matters, appears only near the end.

Each fix is small: end the sentence at the claim, split the dense paragraph, and preview auditability in the placement section. None of these fixes requires restructuring the note.

I could not infer a stronger claim than the one the note makes.
