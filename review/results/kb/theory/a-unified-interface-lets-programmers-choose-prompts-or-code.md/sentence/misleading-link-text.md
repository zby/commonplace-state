---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: a13de1717c1c4bc3b58012768ccdd1bf
completed-at: '2026-11-20T11:11:48Z'
findings:
- scope: passage
  quotes:
  - '[llm-do](https://github.com/zby/llm-do)'
  reason: External repository link not resolved in this review (reading scope is local
    files). The link text names the repository, so the reader's expectation is low-risk.
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/c10c1814846d1063594439ce/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/outputs/review-misleading-link-text.md
raw-output-sha256: 586ea232c463e1f37662b024f386e30bb8a932c45cb541b92482da28b3f51266
---

# Review

I checked each local link against the target's title and opening, and read further where the head did not settle the question.

- `English account of prompting` → *Prompting changes failure diagnosis with the semantic reference*. The target presents an English-execution account alongside a model-defined one, and its English account matches the sentence's description. The extraction point also appears in the target.
- `Constraining`, `codification` → their definition notes. They match.
- `spec mining` → *Spec mining is codification's operational mechanism*. This matches the observe-and-extract use.
- `relaxing` → *Codification and relaxing navigate the bitter lesson boundary*. The target defines relaxing as replacing an extracted component with a more general one. This matches.
- `relaxing signals` → *Operational signals that a component is a relaxing candidate*. This matches.
- `Instructions are typed callables` → the typed-callables note. This matches.
- Footer links (RLM/Tendril/llm-do, host-language scheduler, programming practices, and repeats of the links above) use the target titles as link text. Their glosses agree with the target openings.

The external llm-do link was not resolved. No local link text misleads.
