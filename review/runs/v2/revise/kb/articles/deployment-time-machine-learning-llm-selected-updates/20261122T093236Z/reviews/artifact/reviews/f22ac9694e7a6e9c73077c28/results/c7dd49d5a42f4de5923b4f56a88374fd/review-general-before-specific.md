---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Before stating the paradigm abstractly, follow a single edit through a deployed
    agent system
  reason: '''One change followed through'' is a worked example of the paradigm, and
    it comes before ''Selection-based learning versus direct gradient training'',
    which states the general definition. Taken alone, this is the exemplify-before-general
    pattern. However, the opening paragraphs already state the general idea: selection
    by comparison and the robust comparison over a preference model. The section also
    announces the example-first order as deliberate. So the reader learns the rule
    before the case, and reordering would gain little.'
  level: info
outcome: pass
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/structural/general-before-specific.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/structural/general-before-specific.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/c7dd49d5a42f4de5923b4f56a88374fd/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/f22ac9694e7a6e9c73077c28/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: c7dd49d5a42f4de5923b4f56a88374fd
completed-at: '2026-11-22T09:34:52Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/c7dd49d5a42f4de5923b4f56a88374fd/outputs/review-general-before-specific.md
raw-output-sha256: 85c852af6ef95d47f085b8071bb14bbc58d91a5a4fee3862d6a3be9b02a5c971
format: 2
---

# Review

## Summary

Adjacent section pairs checked:

1. "One change followed through" → "Selection-based learning versus direct
   gradient training": specific case before the formal definition. The
   lede states the general pattern first, so this pair is recorded as info.
2. "Selection-based learning versus direct gradient training" → "Proof,
   formula, judgment: where the bet enters": general definition, then the
   ways evaluation can work, with historical precedents. Order is correct.
3. "Proof, formula, judgment" → "Compatible with the Bitter Lesson": the
   later section answers an objection. Neither section is a specific case of
   the other.
4. "Compatible with the Bitter Lesson" → "Whether a change improved the
   system, current evidence, and limits": these address separate questions.
   No pattern/instance relation.
5. "Whether a change improved the system..." → "Where to go next":
   navigation. Not applicable.

Inside "Proof, formula, judgment", the bold-headed precedents (Gödel machine,
PRODIGY, EURISKO) come before "Robust comparison". That paragraph is the next
option in the sequence, not the general rule the precedents exemplify, so the
order is correct.
