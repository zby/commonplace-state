---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 59a27bb0c8874f0eb150c9b50d4e9333
completed-at: '2026-11-22T09:36:21Z'
findings:
- scope: passage
  quotes:
  - false-positive acceptance, unfaithful rationales, and accretion below the gains
    it finds
  reason: 'The falsification condition leaves its comparison basis unresolved. Reading
    A: the losses from these hazards are netted against the gains on some aggregate
    scale. The article argues against exactly that kind of single score. Reading B:
    the whole-system state after the loop''s changes is not robustly better than the
    state before them under every compatible measure. Under reading B, an outcome
    that is open (gains on some measures and losses on others) does not show failure.
    Under reading A, it may. The choice changes which experimental result refutes
    the bet and what evidence the test must collect.'
  level: warn
- scope: passage
  quotes:
  - those domains stay with weights-only continual learning
  reason: '''Those domains'' has no stated antecedent. It could mean the domains tested
    in the controlled runs, or all work ''where no fixed criterion is adequate''.
    The scope of the consequence after a failed test differs between these readings.
    The difference is less load-bearing than the falsification basis itself.'
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/d19e6c08be3edf06ef28ad6a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/outputs/review-underspecified-assertions.md
raw-output-sha256: 014080259e7bf99ab2cfec395c3606a840514543e2817fda5a70b569e6c4c6d1
---

# Review

## Summary

Most load-bearing assertions are resolved locally. Several examples:

- The Bitter Lesson claim is qualified at once by the bootstrap condition.
- 'Deployment time' is pinned to lifecycle, not speed.
- The robust comparison names its fixing choices: alternative, whose costs count, and horizon.
- The two-part test names its conditions.

The material gap is in the stated refutation condition. Read against the article's own thesis, 'below the gains it finds' could mean net loss on a scale or failure of robust improvement. These readings set different bars for what an experiment must show before the bet fails.
