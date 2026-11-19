---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: e7330664386a4e51978e1708e32e6969
completed-at: '2026-11-18T16:03:33Z'
findings:
- scope: passage
  quotes:
  - LLM recompute cost inverts the store-vs-recompute default
  reason: 'The link text promises that LLM recompute cost inverts the default, so
    that storing becomes the default. The target''s current title is ''LLM recompute
    cost shifts the store-vs-recompute balance''. Its body says that ''Expensive model-side
    derivation does not by itself justify persistence'': code may derive the narrow
    answer on demand, and persistence pays only when its total expected cost beats
    the alternatives. A reader who does not follow the link gets a stronger claim
    than the target makes. The annotation ''why recomputation is costly enough for
    retained results to be worth keeping'' repeats that overstatement. The link text
    should use the target''s current title, and the annotation should say that the
    target shifts the balance under stated conditions.'
  level: warn
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/07f8d7122a15f1a239642529/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/07f8d7122a15f1a239642529/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/e7330664386a4e51978e1708e32e6969/outputs/review-misleading-link-text.md
raw-output-sha256: 530bbc0a7fb6684871a1f133a1d9f0583434a9383e926fdf28f428a7a2718e29
---

# Review

## Summary

All seven links resolve. Six match what their link text and context lead the reader to expect:

- `frontloading-spares-execution-context.md` presents frontloading as sparing a later call's discovery and derivation.
- `indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md` states the suppression mechanism the note describes.
- `../types/tag-readme.md`, linked as "mark", defines the `complete` mark.
- `../types/connect-report.md` defines the connect report as candidate-only.
- `an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md` now has the title "combines a MOC pattern with checked membership". The substance still matches: it develops the validator-checked completeness relation and its bounded stopping shortcut.
- `history-has-one-chance-to-become-checkable.md` says that unrecorded history cannot be checked later. That fits the stated contrast that condition 3 fails.

The recompute link does not match. Its text carries a superseded title that claims an inversion. The target now makes a hedged, conditional claim that the balance shifts.
