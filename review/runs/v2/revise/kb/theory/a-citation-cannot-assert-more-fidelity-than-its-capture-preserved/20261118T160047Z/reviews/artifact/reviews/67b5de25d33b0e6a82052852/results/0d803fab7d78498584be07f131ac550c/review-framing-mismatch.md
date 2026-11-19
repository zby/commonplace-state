---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A model may need several reads to check a source that exceeds its context budget.
  reason: The mechanism the paragraph identifies — an excerpt can preserve wording
    exactly while omitting the context needed to judge use — applies to any excerpt-based
    check (a search hit, an intermediary extract), not only to sources larger than
    a model's context budget. The framing emphasizes the oversized-source case without
    excluding others, so this is emphasis rather than exclusion.
  level: info
- scope: passage
  quotes:
  - A citation cannot assert more fidelity than its capture preserved
  reason: 'The title frames the fidelity ceiling as the capture, while the body''s
    mechanism is more general: a pass is relative to whatever evidence the check used,
    which may be the original, a capture, an intermediary''s extract, or nothing.
    The capture is the central case rather than an excluding frame, since the body
    states the general relation explicitly.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/67b5de25d33b0e6a82052852/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/67b5de25d33b0e6a82052852/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 0d803fab7d78498584be07f131ac550c
completed-at: '2026-11-18T16:03:05Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/0d803fab7d78498584be07f131ac550c/outputs/review-framing-mismatch.md
raw-output-sha256: c24cece2dcc5f567b8eb4354aeea9a86f84d0d37d9f8ae5558b6ff096d291405
format: 2
---

# Review

The note's mechanism sentences are generally at the right level of generality. The four-question split, the cost and determinism argument for running wording checks on every pass, the normalization trade-off, the occurrence-versus-location distinction and the evidence-relativity of a pass each name their mechanism directly.

Two framings emphasize one case of a broader mechanism. Neither excludes cases the body covers, so both are INFO: the context-budget framing of the excerpt problem, and the title's use of "capture" where the body's operative concept is "the evidence this check used".
