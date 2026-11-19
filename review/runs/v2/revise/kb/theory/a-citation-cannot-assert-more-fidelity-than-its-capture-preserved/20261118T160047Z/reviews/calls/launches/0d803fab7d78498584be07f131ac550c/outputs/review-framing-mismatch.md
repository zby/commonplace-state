---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A model may need several reads to check a source that exceeds its context budget."
    reason: "The mechanism the paragraph identifies — an excerpt can preserve wording exactly while omitting the context needed to judge use — applies to any excerpt-based check (a search hit, an intermediary extract), not only to sources larger than a model's context budget. The framing emphasizes the oversized-source case without excluding others, so this is emphasis rather than exclusion."
    level: info
  - scope: passage
    quotes:
      - "A citation cannot assert more fidelity than its capture preserved"
    reason: "The title frames the fidelity ceiling as the capture, while the body's mechanism is more general: a pass is relative to whatever evidence the check used, which may be the original, a capture, an intermediary's extract, or nothing. The capture is the central case rather than an excluding frame, since the body states the general relation explicitly."
    level: info
outcome: pass
---

# Review

The note's mechanism sentences are generally at the right level of generality. The four-question split, the cost and determinism argument for running wording checks on every pass, the normalization trade-off, the occurrence-versus-location distinction and the evidence-relativity of a pass each name their mechanism directly.

Two framings emphasize one case of a broader mechanism. Neither excludes cases the body covers, so both are INFO: the context-budget framing of the excerpt problem, and the title's use of "capture" where the body's operative concept is "the evidence this check used".
