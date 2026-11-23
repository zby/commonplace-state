---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "foundation: the exact-spec/proxy-theory distinction this note operationalizes"
    reason: "The footer label `foundation` is not in the collection's authorized label table. The described relation (this note builds on the target's premise) fits `grounds` or `extends`."
    level: warn
  - scope: passage
    quotes:
      - "the bottom-up extraction method that avoids the vision-feature failure mode"
      - "detects when codified components are encoding vision features"
    reason: "These footer entries carry no label. The contract's footer form is `- [title](path) — label: context phrase`, with the label taken from the table. Both targets are theory notes, so `mechanism`, `extends` or `enables` could apply depending on the intended reader need."
    level: warn
  - scope: passage
    quotes:
      - "grounds when codification targets real patterns"
    reason: "The external sources in the Sources footer use the label `grounds`, whose only permitted destination is theory. For external sources the table allows `evidenced-by` or `abstracted-from`. The Ebrahimi entry carries no label at all."
    level: warn
  - scope: passage
    quotes:
      - "provide evidence from the other direction"
    reason: "The Ebrahimi results are presented as evidence for the claim that arithmetic-regime codification bets persist under scaling. Under 'Origin is not corroboration', evidence that corroborates must state what the claim risked and whether the evidence was recorded after or independently of how the claim was built. Otherwise it must be framed as qualifying or bounding the claim, or linked as `abstracted-from`. The note does neither."
    level: warn
outcome: warn
---

# Review

The note belongs in `kb/theory/`. After its examples are scoped, a transferable claim about the design space remains: code-extraction codification and relaxing are complementary moves under uncertainty about whether a spec is exact or a proxy. It names no Commonplace selection that would route it to `kb/reference/`. It handles conjectural force well in places. For example, it says that scale selecting on the property "is conjectural, not established", and its trajectory-not-law framing keeps boundaries visible. Both serve the explanatory-reach goal.

The unmet conventions are in outbound linking and evidence framing:

- The footer uses an unauthorized label (`foundation`).
- Two Relevant Notes entries have no label.
- The external sources use `grounds`, which the table reserves for theory destinations, or no label.
- The epiplexity and induction-bias studies are offered as support without the corroboration framing the contract requires.

None of these affects placement or the main claim. They are local fixes, so the outcome is WARN rather than FAIL.

The source-grounding bound is not at issue. Both sources are external URLs, not tracked `kb/sources/` ingests, and both are cited in the body as well as the footer.
