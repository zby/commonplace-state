---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/ephemeral-computation-prevents-accumulation.md
  against kb/instructions/review-gates/prose/mannered-prose.md
note: kb/theory/ephemeral-computation-prevents-accumulation.md
note-sha256: d3a6a9e3e3da3e9b0cfdf1f37204cd3f0a4037ff53011b0c118feabbef1ffbc3
criterion: kb/instructions/review-gates/prose/mannered-prose.md
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews
launch: 005320693e03462fa070a4b9fdb23e69
completed-at: '2026-11-20T14:56:52Z'
findings:
- scope: passage
  quotes:
  - The house may keep the failure it exposed
  reason: Replace 'The house' with 'The deployed system' or 'The system'. The figurative
    label 'house' is undefined here, forces the reader to infer that it refers back
    to the deployed system introduced earlier, and brings unrelated institutional
    or physical connotations without compressing or clarifying the claim.
  level: warn
- scope: passage
  quotes:
  - A house can combine both choices
  reason: Replace 'A house' with 'A deployed system' or 'A system'. As with the earlier
    occurrence, 'house' adds decoding effort and unsupported institutional or physical
    connotations while offering no precision or brevity advantage over the literal
    term already used elsewhere in the note.
  level: warn
contract: verdict
target-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/005320693e03462fa070a4b9fdb23e69/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/artifact/reviews/5751b52337ffc2cc1dc9df55/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/005320693e03462fa070a4b9fdb23e69/outputs/review-mannered-prose.md
raw-output-sha256: 0e3529dd88a242bbe5075aca465cf72c21ab1735ee085c19f24b6839dfeeb007
---

# Review

Most of the note uses direct, literal technical phrasing, and conventional terms such as `machinery`, `carrier`, `horizon`, and `defeat that assumption` function as standard technical shorthand. The two unexplained uses of `house` for the operating or deployed system are localized mannered phrasing that obscures the subject without contributing precision or structure.
