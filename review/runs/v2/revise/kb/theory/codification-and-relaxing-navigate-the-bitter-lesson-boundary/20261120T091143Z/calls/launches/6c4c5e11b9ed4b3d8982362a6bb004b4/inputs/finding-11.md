---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/theory/COLLECTION.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
criterion: kb/theory/COLLECTION.md
criterion-sha256: 95ad0d6ce3828b25282f7610268c4e1aca006fa34526bc2b4e4056f3e271cccd
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: d81350cceafa46af97949c1215e0fac6
completed-at: '2026-11-20T09:14:33Z'
findings:
- scope: passage
  quotes:
  - 'foundation: the exact-spec/proxy-theory distinction this note operationalizes'
  reason: The footer label `foundation` is not in the collection's authorized label
    table. The described relation (this note builds on the target's premise) fits
    `grounds` or `extends`.
  level: warn
- scope: passage
  quotes:
  - the bottom-up extraction method that avoids the vision-feature failure mode
  - detects when codified components are encoding vision features
  reason: 'These footer entries carry no label. The contract''s footer form is `-
    [title](path) — label: context phrase`, with the label taken from the table. Both
    targets are theory notes, so `mechanism`, `extends` or `enables` could apply depending
    on the intended reader need.'
  level: warn
- scope: passage
  quotes:
  - grounds when codification targets real patterns
  reason: The external sources in the Sources footer use the label `grounds`, whose
    only permitted destination is theory. For external sources the table allows `evidenced-by`
    or `abstracted-from`. The Ebrahimi entry carries no label at all.
  level: warn
- scope: passage
  quotes:
  - provide evidence from the other direction
  reason: The Ebrahimi results are presented as evidence for the claim that arithmetic-regime
    codification bets persist under scaling. Under 'Origin is not corroboration',
    evidence that corroborates must state what the claim risked and whether the evidence
    was recorded after or independently of how the claim was built. Otherwise it must
    be framed as qualifying or bounding the claim, or linked as `abstracted-from`.
    The note does neither.
  level: warn
contract: verdict
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/d81350cceafa46af97949c1215e0fac6/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/575a47f0d3c86cfe8b5d7503/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/d81350cceafa46af97949c1215e0fac6/outputs/review.md
raw-output-sha256: 051226b0fa0aecbdbd1ccc4d7b1766c959a18a8f1b2aa17f5fda8a66fddb978b
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
