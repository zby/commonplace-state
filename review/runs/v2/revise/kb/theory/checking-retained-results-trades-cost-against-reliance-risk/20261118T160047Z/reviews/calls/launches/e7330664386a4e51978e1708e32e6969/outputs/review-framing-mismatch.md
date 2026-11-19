---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A stale copy can also hide its own error"
    reason: "The suppression mechanism needs only a copy that is incomplete and treated as exhaustive. Staleness is not required: a copy that was wrong when it was produced suppresses the fallback search in the same way. The sentence names only the stale case. It does not say that only stale copies can do this, and the note's framing elsewhere ('stale or wrong content') covers the other case, so the sentence emphasizes one case without excluding the other."
    level: info
outcome: pass
---

# Review

## Summary

The note's mechanism statements are framed at the right level of generality. These were checked and hold:

- Staleness comes from separate update paths for the source and the copy.
- The trade-off is check cost against reliance risk.
- A check that recomputes on every use defeats the saving, unless verification is cheaper than derivation.
- A defined check on a stop-authorizing claim makes enforcement attractive.
- Rerunning discovery is hard because its dependency set is broad.
- The absence of a known change is evidence of freshness only if every relevant change reaches the checker.

The only framing note is minor. One sentence ties the hidden-error mechanism to staleness, although the mechanism covers any incomplete copy. The surrounding text already says "stale or wrong," so this is recorded as INFO only.
