---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "LLM recompute cost inverts the store-vs-recompute default"
    reason: "The link text promises that LLM recompute cost inverts the default, so that storing becomes the default. The target's current title is 'LLM recompute cost shifts the store-vs-recompute balance'. Its body says that 'Expensive model-side derivation does not by itself justify persistence': code may derive the narrow answer on demand, and persistence pays only when its total expected cost beats the alternatives. A reader who does not follow the link gets a stronger claim than the target makes. The annotation 'why recomputation is costly enough for retained results to be worth keeping' repeats that overstatement. The link text should use the target's current title, and the annotation should say that the target shifts the balance under stated conditions."
    level: warn
outcome: warn
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
