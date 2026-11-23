---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A fixed review rule can use lessons from new incidents only if it can identify
    when they apply
  reason: The title makes the rule the agent that must identify when a lesson applies,
    while the body says the rule only tells the reviewer where to look and that the
    reviewer's recognition does the identifying without the rule changing; a reader
    must reconcile the two before the central claim is clear. A revision could align
    the title's subject with the body's mechanism, so that the title, the opening
    and the closing sentence state one claim.
outcome: report
description: Retained report review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
contract: report
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
criterion-sha256: 0639a8d235bbdf791feaa2f1eae21d28a4131c0fe56e0a15fefe51fa524835cf
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/synthesis/calls/launches/ea53d375226f4142baab7b4e506e8d94/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/synthesis/artifact/reviews/0b2728a80112bfc0bd2c245f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/synthesis
launch: ea53d375226f4142baab7b4e506e8d94
completed-at: '2026-11-23T11:44:44Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/synthesis/calls/launches/ea53d375226f4142baab7b4e506e8d94/outputs/review.md
raw-output-sha256: 06cb84a5e9ae2ad8cf283b9ceb58730380ad9898ed8e3bf38c743451929bd8d6
format: 2
---

# Simplification synthesis: fixed review rules and incident lessons

All four compression checks passed with no findings. The note has three short paragraphs: the claim, one worked example and the test the example implies. No branch, detail or redundancy needs removal. The one opportunity worth an author's judgment comes from reading the title against the body. It is not a compression cut.

## Opportunities

### 1. Align who identifies applicability in the title and the body

- Location: the title, "A fixed review rule can use lessons from new incidents only if it can identify when they apply", read against the first paragraph ("It does not tell the reviewer which earlier failure bears on the page at hand") and the last sentence ("The incident shows what the review must distinguish, not that the review rule must change").
- Combines: cross-cutting. The core-claim-obscured check noted, as a non-finding, that the closing contrast is the sharpest form of the claim and could be lifted into the opening. This opportunity extends that observation: the mismatch sits in the title, not only in the opening.
- Reader problem: grammatically, "it" in the title is the rule, so the title reads as a requirement on the rule. The body places identification in the reviewer and argues that the rule does not need to change. A reader cannot tell whether the note requires the rule to encode applicability conditions or says that reviewer recognition suffices under an unchanged rule.
- Direction: make the title's subject match the body's mechanism. One possible resolution, offered for illustration only: "A fixed review rule carries new incident lessons only when the reviewer can recognize which feature of a past failure applies". The opening paragraph could then state the closing contrast ("a distinction to recognize, not a rule to change") so that the first and last statements match.
- Preserve or decide: the author must choose between two materially different claims. (a) The rule stays fixed and the reviewer's recognition carries the lesson, which is what the body argues. (b) The rule must itself supply a way to identify when lessons apply. The description ("leaves the reviewer to determine") supports (a). The title and the filename (`...-must-identify-when-incident-lessons-apply`) lean toward (b). Do not resolve this as a wording edit. If (a) is chosen, retitling also means relocating the file, and that is a separate step.
