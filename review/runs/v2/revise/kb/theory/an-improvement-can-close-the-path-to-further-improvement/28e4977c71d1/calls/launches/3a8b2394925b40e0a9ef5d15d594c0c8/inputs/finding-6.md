---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
note-sha256: 0366cb851ef44475ed808292e3919e8d5559c86b5d72261a6cdd8d5c82ee0aab
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews
launch: 7f6000a8c1de4c2587cba8c5a0619c7b
completed-at: '2026-11-17T07:23:39Z'
findings:
- scope: passage
  quotes:
  - disables a mechanism needed to select or install later revisions
  reason: 'The mechanism the note describes is the whole revision path: evidence leads
    to a proposed change, an adoption decision, installation and later use. Framing
    the loss as a mechanism needed to ''select or install'' excludes cases the mechanism
    covers. Examples are a change that disables proposing revisions, or one that leaves
    installed changes unconsumed. The note itself counts the second case as loss when
    it says that kept files do not preserve the capability ''if the successor no longer
    permits or consumes their changes''. Wording such as ''a mechanism needed to carry
    later revisions through to use'' would match the mechanism.'
  level: warn
contract: verdict
target-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/6b3ee30e5514b3fa7a4b877b/inputs/target/kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/6b3ee30e5514b3fa7a4b877b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/calls/launches/7f6000a8c1de4c2587cba8c5a0619c7b/outputs/review-framing-mismatch.md
raw-output-sha256: c506155671575ec9775945af1bc0c05dfa01a05198194d553f6d5305e62f6077
---

# Review

## Summary

Most mechanism statements are framed at the right level. Non-regression protects whatever is in its checked scope. The example's comparison checked task performance while the change removed a different capability. Preservation attaches to the function, not to a component.

The opening paragraph is the exception. It names only selection and installation as the disabled functions. Later, the note defines the relevant question as the full chain from evidence to later use. Its replacement criterion is whether a revision can be carried "through to use". A reader of the opening alone would miss losses at the proposal or later-use stages. The later text corrects this, so the narrowing is local, but it does exclude covered cases.
