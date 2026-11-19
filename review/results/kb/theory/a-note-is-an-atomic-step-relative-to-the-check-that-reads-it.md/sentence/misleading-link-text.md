---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: bdb15b9082614770b69f37ba9041d8ae
completed-at: '2026-11-16T22:39:20Z'
findings: []
contract: verdict
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/f495e8250d2ac08d5a34f05a/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/f495e8250d2ac08d5a34f05a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/bdb15b9082614770b69f37ba9041d8ae/outputs/review-misleading-link-text.md
raw-output-sha256: 9a1ebc8bc1a42fc6e5e87903ce6bcb6587c292a4251c69659b1ef5e6b404eb30
---

# Review

I checked every inline Markdown link in the body against its target's title and opening:

- `short-composable-notes-maximize-combinatorial-discovery.md`: the link text is the target's title, used for the co-loading argument the target opens with.
- `warranted-autonomy-is-bounded-by-oracle-domain.md` and `the-boundary-of-automation-is-the-boundary-of-verification.md`: the link text is each title, used for the claim each title states.
- ADR 046: the target decides that `verbatim` quotations are validated against their linked source, which the sentence describes.
- ADR 073: the target requires retained verbatim quotes in ingests and a marked snapshot-required route, which matches the sentence's description of source-side material.
- `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`, `a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md` and `a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md`: each link text is the target's title claim, used in that sense.
- `a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md`: the link text "four findings appeared only in the uncapped arm" matches the report's opening, which says four divergences appeared only under fuller reading.
- Descartes ingest (Part II, twice) and Lamport ingest (sections 3 and 5): the link texts are work titles and locators, and the ingests retain the quoted passages at those locations.

All targets resolved. No link text promises something its target does not provide.
