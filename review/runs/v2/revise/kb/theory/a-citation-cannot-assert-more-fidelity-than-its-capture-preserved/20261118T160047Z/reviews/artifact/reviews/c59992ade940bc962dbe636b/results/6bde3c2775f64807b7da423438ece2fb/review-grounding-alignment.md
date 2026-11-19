---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - equal bytes at an arbitrary path do not (ADR 073)
  - Forbidding concatenation of disjoint ranges prevents certifying a passage that
    never existed contiguously (ADR 094)
  reason: These claims are presented as grounded by ADR 073 and ADR 094, but the note
    gives no link to either ADR, so this gate cannot open them within its reading
    scope and cannot verify that the ADRs make these claims at this scope. Not judged
    as misgrounded; the missing link leaves the attribution unverifiable here.
  level: info
- scope: passage
  quotes:
  - which a permissive enough rule would ignore
  reason: The ADR 046 citation supports the mismatch profile (editorial omission,
    bracketed substitution, case changes). The added inference that a permissive enough
    normalization rule would ignore these is the note's own, not the ADR's; it is
    plausible for case changes and non-load-bearing, but for ellipsis omissions it
    needs more than normalization (the note's own Scope bullet treats segment-wise
    checking as open).
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/c59992ade940bc962dbe636b/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/c59992ade940bc962dbe636b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 6bde3c2775f64807b7da423438ece2fb
completed-at: '2026-11-18T16:04:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/6bde3c2775f64807b7da423438ece2fb/outputs/review-grounding-alignment.md
raw-output-sha256: e2b5ebfda9d31634970aec728366bb89e14059a08ec0ca180aa26181a9695837
format: 2
---

# Review

The note links two library artifacts.

**Checking retained results trades cost against reliance risk.** The note invokes it to frame the fail-not-warn choice as "a choice within the trade-off", not a universal rule, and says later readers can reuse a check's result while accepting the risk of changes since it ran. The target's title claim is exactly that trade-off; its completeness-mark section says an inexpensive, defined check on a stop-authorizing claim makes enforcement attractive and that subsequent reads reuse the checked result, with assurance dating from the last check. The invocation matches the target's claim and scope.

**ADR 046.** Three uses:

- "ADR 046 judges such false mismatches worse than no check" matches the ADR's Consequences: an under-normalized checker "would produce false mismatches on correct quotes, which is worse than no check".
- The casebook profile ("mostly editorial omissions, bracketed substitutions and case changes") matches the ADR's "dominated by editorial omission (`...`), bracketed substitution, case changes, and punctuation moved inside the quotation boundary"; "mostly" fairly compresses the list.
- The appended inference about a permissive rule is the note's own (INFO).

The paraphrase-marker remark in the opening paragraph is consistent with ADR 046's statement that `paraphrase layer` and `second-hand` remain unchecked because they never claimed exact text, though the note does not link the ADR there.

ADR 073 and ADR 094 are cited by number without links; they are outside this gate's reading scope (INFO). No quoted sources or `kb/sources/` ingests are linked.
