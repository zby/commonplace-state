---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The three precedents raise the same question
  reason: 'The sentence and the heading (''Proof, formula, judgment'') announce three
    precedents. The section then gives four bolded entries: formal proof, fixed formula,
    changing heuristics and robust comparison. The fourth is a decision rule, not
    a historical system, and ''judgment'' in the heading seems to name the LLM bet
    rather than EURISKO. Readers may not be able to tell which three are meant.'
  level: info
- scope: passage
  quotes:
  - It keeps every value function compatible with the preferences a person has stated
  reason: Possible definition drift. The opening introduces 'preference model' as
    the set of weightings that the stated purpose permits. Here it is the set compatible
    with preferences a person has stated. The later 'In the decision-analysis method,
    a person states the preferences' paragraph reconciles the two as source sense
    versus the article's extension. The opening, however, presents the purpose-derived
    set under the source's name without that marker.
  level: info
- scope: passage
  quotes:
  - a third change revises the review check itself
  reason: The count is ambiguous. The narrative has the line's addition (first) and
    its narrowing (second), and it also mentions three other over-broad rules passing
    the brevity check. Calling the check revision 'a third change' fits only if those
    intervening rule additions are not counted as changes.
  level: info
outcome: pass
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/66ecfa59e4da03d19e2f2e11/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 59a27bb0c8874f0eb150c9b50d4e9333
completed-at: '2026-11-22T09:36:21Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/outputs/review-internal-consistency.md
raw-output-sha256: b3c882e347c3da668ce93f721bc8d7c044be60d9b9eaeb67a941f2e34f5e4ccf
format: 2
---

# Review

## Summary

I found no pairwise contradiction among the key claims. They agree with one another on these points:

- The process has no built-in guarantee of improvement, and success is judged separately.
- A trial differs from adoption as proposed, while both take effect now.
- Open comparisons are decisions, not improvements.
- Commonplace currently runs with people inside the loop, and there is no completed automated run.
- The bet is about comparison, not proposal quality.

The bet is stated at different breadths: bolded in the opening, expanded in the next sentence, and restated in the robust-comparison section with criterion revision and deciding open cases. These statements accumulate rather than conflict.

The remaining items are counting and naming ambiguities that a human should confirm.
