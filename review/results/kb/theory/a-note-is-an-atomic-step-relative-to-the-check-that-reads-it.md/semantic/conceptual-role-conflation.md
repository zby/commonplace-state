---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 15276ece3fca4dcf9ad58dc741abbb87
completed-at: '2026-11-16T22:40:09Z'
findings:
- scope: passage
  quotes:
  - Sizing a step to its checker rather than to the material is old.
  reason: 'The sentence can be read as attributing the checker-relative concept to
    Descartes (a prior account), or as the note''s own explication for which Descartes
    is offered as an earlier, looser precedent. Nearby context mostly settles it:
    the note says Descartes''s parts ''are sized to the solution'', that ''Lamport
    makes the checker explicit'', and that the transfer is ''an analogy''. The remaining
    blur is immaterial to what the note contributes.'
  level: info
contract: verdict
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/f2f5681eb25e0c87a381bd39/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/f2f5681eb25e0c87a381bd39/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/15276ece3fca4dcf9ad58dc741abbb87/outputs/review-conceptual-role-conflation.md
raw-output-sha256: 3eaa0703b20346aff9809bb095353ed43ed714a38e522ee2b1b79da64c87939f
---

# Review

The passages that import or apply concepts mostly keep their roles distinct. The note defines its own term ("atomic step"), presents the checker relativity as an instance of the linked oracle-domain rule, and calls the derived-copy rule "applied to citation". These relations are explicit. It also separates its explication from the linked prior accounts: it says what is general (the relativity) and what is derived for one check (the unit).

The one place where roles blur is the opening of the precedent paragraph. Its topic sentence presents checker-relative sizing as old, with Descartes as the first exhibit. However, the following sentences assign Descartes a sizing relative to the solution, make Lamport the one who names the checker, and label the transfer an analogy. The prior account and the current explication can therefore be recovered from nearby context. No finding meets the materiality threshold.
