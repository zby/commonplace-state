---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: e7bbf405145449998c8cf63c9b9a41ae
completed-at: '2026-11-18T16:03:04Z'
findings:
- scope: passage
  quotes:
  - A model may need several reads to check a source that exceeds its context budget.
  reason: 'This paragraph sits under ''Which evidence a pass is relative to'' but
    concerns the context question, which the note has already assigned to a reader
    rather than to the wording check. Its first point supports the main claim: an
    exact excerpt can still omit the context needed to judge use, so a wording pass
    does not establish support. The closing procedural rule (the checker must retrieve
    context; the full source can stay outside the model''s context) describes how
    to run a support-judging checker. That is a different mechanism and needs different
    evidence. Consider keeping only the bounding point, perhaps next to the four-questions
    section, and rehoming the procedure. Where the procedure should go is unclear.'
  level: info
- scope: passage
  quotes:
  - 'Semantic hops compound instead: checking a paraphrase against a paraphrase adds
    a judgment at each hop, and rewording at either hop can change the proposition.'
  reason: 'The provenance-chain paragraph supports the main claim: an exact check
    verifies only its own pair, and exactness is independent of second-hand provenance.
    The contrast with semantic hops, and the recommendation to check against verified
    source extracts, concern paraphrase checking. The note''s opening places paraphrase
    outside what the check can match. The contrast briefly sharpens why exact hops
    do not compound, so it can stay. The recommendation is a branch, and its destination
    is unclear.'
  level: info
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/6d6a55a60a429f226731588c/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/6d6a55a60a429f226731588c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/e7bbf405145449998c8cf63c9b9a41ae/outputs/review.md
raw-output-sha256: 7d3bfcc334b78ccec49d527f4614fcb29246d8550e7d0efbdc137ccc54c91e8f
---

# Review

The main claim, taken from the title, description and section structure, is that a quote check establishes only wording agreement with the specific evidence it compared. A pass is relative to that capture or extract. Attribution upstream of the capture, contextual support and truth stay unverified.

Most side material supports this claim in place:

- The four-questions list separates what the check answers from what it does not.
- The cost-versus-risk sentence bounds when a mismatch may count as a failure.
- The normalization and uniqueness paragraphs say what "exact" means.
- The paragraphs on identity binding, and on retained versus accessible material, show what a pass is relative to.
- The scope bullets set boundary conditions.

None of these is a removable branch.

Two passages go beyond the main claim, into how a checker should judge context or paraphrase. Each has a sentence that bounds the main claim and is worth keeping. Each also has procedural or recommendatory content whose destination is unclear. Neither competes with the main claim strongly enough to warrant a WARN, so both are recorded as INFO.
