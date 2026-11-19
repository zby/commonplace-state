---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "equal bytes at an arbitrary path do not (ADR 073)"
      - "Forbidding concatenation of disjoint ranges prevents certifying a passage that never existed contiguously (ADR 094)"
    reason: "These claims are presented as grounded by ADR 073 and ADR 094, but the note gives no link to either ADR, so this gate cannot open them within its reading scope and cannot verify that the ADRs make these claims at this scope. Not judged as misgrounded; the missing link leaves the attribution unverifiable here."
    level: info
  - scope: passage
    quotes:
      - "which a permissive enough rule would ignore"
    reason: "The ADR 046 citation supports the mismatch profile (editorial omission, bracketed substitution, case changes). The added inference that a permissive enough normalization rule would ignore these is the note's own, not the ADR's; it is plausible for case changes and non-load-bearing, but for ellipsis omissions it needs more than normalization (the note's own Scope bullet treats segment-wise checking as open)."
    level: info
outcome: pass
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
