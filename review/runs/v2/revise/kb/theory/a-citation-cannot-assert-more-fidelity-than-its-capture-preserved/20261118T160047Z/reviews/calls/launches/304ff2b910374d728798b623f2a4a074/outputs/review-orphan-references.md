---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "In one casebook corpus the real mismatches were mostly editorial omissions, bracketed substitutions and case changes (ADR 046)"
    reason: "The empirical claim cites ADR 046, which is linked earlier in the same paragraph, so a source is supplied. But the note never says what the casebook corpus is or how many mismatches it had. The linked ADR describes a prototype run over a sibling casebook corpus with 18 mismatches among 87 candidates. A short gloss, such as 'a prototype run over a sibling KB's casebook (18 mismatches in 87 candidates)', would let the reader judge how much weight 'mostly' can bear without leaving the note."
    level: info
outcome: pass
---

# Review

## Summary

The note contains one concrete empirical claim: the casebook-corpus mismatch profile. It has a source, ADR 046, which is linked in the same paragraph and supports the claim. That ADR reports a prototype run in which the mismatches were "dominated by editorial omission (`...`), bracketed substitution, case changes, and punctuation moved inside the quotation boundary". Local context is thin, because the reader learns neither what the corpus is nor its size. Since the claim is qualitative and the source is one link away, this is an info finding, not a warning.

The other specific references are design decisions, not empirical claims: ADR 094 on concatenating disjoint ranges and ADR 073 on identity binding and silent fallback. Each is named where it is used. Two statements explicitly mark themselves as unmeasured: the reliability of support judgment and the rate of quotations the extractor never recognized. Neither uses unsupported specificity.
