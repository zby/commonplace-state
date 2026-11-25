---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: Coverage of the 'keep' decision is strained. The Stakes section frames the
    question as how to 'rank, keep, or reject candidate notes', and the description
    says 'worth keeping or selecting'. Of the five lenses, answerability, validity/value
    and reader update are admission-time tests, and structural proxies serve ranking.
    Only counterfactual use, plus the retirement trigger inside answerability, speaks
    to whether an already retained note should be kept or retired. A note that once
    passed admission and later becomes stale or redundant fits the framework only
    through those two lenses. The framework is labelled 'partial', so this is a strain,
    not a gap in claimed coverage.
  level: info
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/581afe52ce56a6098f165397/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: a38acad87c914bb7ae48d968378006fb
completed-at: '2026-11-25T05:23:10Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/outputs/review-completeness-boundary-cases.md
raw-output-sha256: f7e2730b056d3052e65ecf4932f7cce77353c88a61dffd06df6459efeb453950
format: 2
---

# Review

## Summary

The enumeration under test is the "five partial lenses" in Current answer. The note explicitly calls them partial and says they are spread "rather than one rule". It also moves the known gaps (root questions, cold-start admission, combining signals) into Unsettled. So it does not claim exhaustive coverage of note valuation.

Boundary cases tried:

- **Simplest instance.** A grounded, non-redundant note that answers a clear question maps to answerability, validity/value and reader update without difficulty.
- **Extreme instance.** A valid top-level note that answers a live question but has no inbound links or observed use. The structural-proxy lens would undervalue it. The note names this case in the root-question Unsettled item, so the boundary is acknowledged.
- **Between items.** Maintenance cost is not a separate lens. It appears inside the validity/value lens and the comparative-work-gain lens, and again as a dimension in the last Unsettled item. It maps, though across two lenses.
- **Adjacent concept.** Retirement of a previously admitted note sits near the "keep" boundary named in Stakes. Coverage is possible but strained; see the INFO finding.
- **Collection goals** (explanatory-reach, fidelity, economy). Stakes places them outside the lenses as a baseline that "does not exhaust" valuation. That is a stated scope boundary, not an omission.

No case clearly falls outside the claimed coverage. Five bullets is proportionate to the note's role as a standing query's current answer, so expansion is not indicated.
