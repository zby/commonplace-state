---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/frontmatter/description-discrimination.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 8f816a5a078affd7a592e56caafa8cb63e0fda8f06c7fec930cced01c2fd048a
criterion: kb/instructions/review-gates/frontmatter/description-discrimination.md
criterion-sha256: 17cbbd1fca45e6be71ce6750fe85980667f4958045e3610c4bb9378b13702bcf
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 203afe73cbd44d0185433c6a6520fe02
completed-at: '2026-11-18T16:01:30Z'
findings:
- scope: document
  quotes: []
  reason: 'The description is a topic inventory rather than a statement of the note''s
    claim, so it does not restate the title''s thesis that a pass is bounded by the
    compared evidence. It still discriminates: it names the three check kinds (wording,
    occurrence, source identity), the relativity of a pass to its evidence, and the
    three things left unverified, none of which the title carries.'
  level: info
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/54d649d0215dba129fb479e6/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/54d649d0215dba129fb479e6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/203afe73cbd44d0185433c6a6520fe02/outputs/review-description-discrimination.md
raw-output-sha256: 19cdf217d3fb4fa7f3f52457173c9d891727d1e3d3e66d325f7bc1a7d5ff73e7
---

# Review

The title states a thesis about fidelity being bounded by the capture. The description does not paraphrase it. It adds mechanism (wording, occurrence and source-identity checks and what each establishes), scope ("quote checking in general") and implication (attribution upstream, contextual support and truth stay unverified). An agent choosing from a short result list could tell this note apart from neighbouring notes on grounding, retained-result reliance or snapshot pinning by those specifics.

The description lists topics instead of stating a claim. This is a minor retrieval weakness, not a gate failure.
