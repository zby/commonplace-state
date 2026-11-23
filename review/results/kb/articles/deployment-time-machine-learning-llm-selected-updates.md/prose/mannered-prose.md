---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/prose/mannered-prose.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/prose/mannered-prose.md
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: b4e70f5925ff4ae894d0f33589d060fa
completed-at: '2026-11-22T09:34:29Z'
findings:
- scope: passage
  quotes:
  - Honest sets of compatible measures leave many trade-offs open.
  - the paradigm claim stays honest only if success is judged separately
  reason: '''Honest'' is applied to a set of measures and to a claim. The literal
    meanings are roughly ''Sets that include every measure the declared purpose permits
    leave many trade-offs open'' and ''the paradigm claim stays testable only if success
    is judged separately''. The moral word adds a connotation of deceit or good faith
    that the note does not discuss. It also leaves the reader to work out which property
    (''complete'', ''not narrowed to favor a change'') is meant. The literal versions
    state the condition directly.'
  level: warn
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b4e70f5925ff4ae894d0f33589d060fa/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/aad2472c9647d35499fceaf9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b4e70f5925ff4ae894d0f33589d060fa/outputs/review-mannered-prose.md
raw-output-sha256: 1568651b2855e4a820eb7cf89ce62ebfeadd62573306f48a3f3142a0154bec9f
---

# Review

## Summary

The prose is mostly literal. Most of its figurative phrases are conventional
or do real work:

- "credit assignment without a chain rule" names a precise contrast with
  backpropagation.
- "hard-oracle extreme" places the Gödel machine on a spectrum that the
  section then develops.
- "sits on the computation side of the Bitter Lesson" maps directly onto the
  essay's own dichotomy between human knowledge and computation.
- "belong on the ledger" and "maintenance drag" are familiar idioms whose
  connotations match the claim.

One local pattern meets the test. "Honest" describes a measure set and a
claim. A literal adjective would say which property is meant and would drop a
connotation the note never establishes. "Re-anchored" in the closing list is
a mild case: it means "revised to start from". Its connotation is harmless,
so it is not flagged.
