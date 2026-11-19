---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/prose/orphan-references.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/review-gates/prose/orphan-references.md
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 304ff2b910374d728798b623f2a4a074
completed-at: '2026-11-18T16:02:23Z'
findings:
- scope: passage
  quotes:
  - In one casebook corpus the real mismatches were mostly editorial omissions, bracketed
    substitutions and case changes (ADR 046)
  reason: The empirical claim cites ADR 046, which is linked earlier in the same paragraph,
    so a source is supplied. But the note never says what the casebook corpus is or
    how many mismatches it had. The linked ADR describes a prototype run over a sibling
    casebook corpus with 18 mismatches among 87 candidates. A short gloss, such as
    'a prototype run over a sibling KB's casebook (18 mismatches in 87 candidates)',
    would let the reader judge how much weight 'mostly' can bear without leaving the
    note.
  level: info
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/35e1e41ed2159b35ffed9c9a/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/35e1e41ed2159b35ffed9c9a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/304ff2b910374d728798b623f2a4a074/outputs/review-orphan-references.md
raw-output-sha256: f085618a97ee614fb164f2f6c9b17112f9ece418a909142fdc7e5f5820bb5bd2
---

# Review

## Summary

The note contains one concrete empirical claim: the casebook-corpus mismatch profile. It has a source, ADR 046, which is linked in the same paragraph and supports the claim. That ADR reports a prototype run in which the mismatches were "dominated by editorial omission (`...`), bracketed substitution, case changes, and punctuation moved inside the quotation boundary". Local context is thin, because the reader learns neither what the corpus is nor its size. Since the claim is qualitative and the source is one link away, this is an info finding, not a warning.

The other specific references are design decisions, not empirical claims: ADR 094 on concatenating disjoint ranges and ADR 073 on identity binding and silent fallback. Each is named where it is used. Two statements explicitly mark themselves as unmeasured: the reliability of support judgment and the rate of quotations the extractor never recognized. Neither uses unsupported specificity.
