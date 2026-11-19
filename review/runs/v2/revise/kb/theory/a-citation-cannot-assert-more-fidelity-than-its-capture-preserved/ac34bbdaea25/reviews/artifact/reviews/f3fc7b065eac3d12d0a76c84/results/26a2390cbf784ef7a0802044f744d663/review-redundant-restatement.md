---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The temptation is to fix provenance downstream — a richer citation format, a structured
    span locator, a stricter gate. It cannot work
  reason: The section opening repeats the introduction's list ("no citation syntax,
    no locator type, no review gate can promote a passage"). Here it is a one-sentence
    setup leading straight into the section's own mechanism (the derived-copy rule),
    not a full re-explanation. The opening paragraph cannot be deleted without losing
    the argument. This is setup restating a thesis, so it is info.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/prose/redundant-restatement.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/prose/redundant-restatement.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 8ac83c3a221e55a6ece3b99917f2f96f145c07d525fd6743b90df87afc272d67
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/f3fc7b065eac3d12d0a76c84/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/f3fc7b065eac3d12d0a76c84/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 26a2390cbf784ef7a0802044f744d663
completed-at: '2026-11-16T22:09:35Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/26a2390cbf784ef7a0802044f744d663/outputs/review-redundant-restatement.md
raw-output-sha256: f0fdd9980361b0cc40a8883f327e675a0ea6eccaebbbcf765f83d50bb788eb6e
format: 2
---

# Review

## Summary

Checking the first paragraph of each section: "Capture is layered because it is forced to be" opens with its own argument for why layering is forced (finite context, copyright), not with a recap. "Why notation cannot repair it" briefly echoes the introduction's list of downstream fixes before giving the new mechanism. That echo is a transition sentence, recorded as info. The corollary section starts directly with its consequence for locators. Scope opens with the short-source case, which is new material.

Checking the last paragraph before each heading: the introduction ends on the fidelity/authority composition, which no later section develops again. The layering section ends with its enumeration. The notation section ends by linking the general "one chance" rule. The corollary ends with "Any locator design must encode the layer." None previews the next section's content. The note restates its thesis at its close ("the debt is fixed at ingest"), but that is inside a section, not at a boundary, so it falls outside this test.
