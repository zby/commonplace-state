---
type: types/edit-result.md
outcome: proposed
proposals:
- quote: the natural operation is to write the useful artifact
  change: write the useful artifact
  reason: '''the natural operation is'' is a roundabout frame; the imperative states
    the same recommendation'
- quote: are still live
  change: are still in the agent's context
  reason: '''live'' is a figure for ''still held in context''; the literal phrase
    says where the information is'
- quote: while understanding was live
  change: while the agent still held that understanding
  reason: same figure as in the opening paragraph; use one literal wording for both
- quote: A check can fossilize a temporary workaround.
  change: A check can make a temporary workaround permanent.
  reason: '''fossilize'' is a figure; the literal verb keeps the meaning (the workaround
    persists after it is needed)'
description: Retained proposed result of kb/instructions/simplification-passes/plain-wording.md
  on kb/theory/agent-memory-requirements/create-memory-directly.md
format: 1
operation: kb/instructions/simplification-passes/plain-wording.md
operation-sha256: ae9094451a0d8c479ebfd0dd4d4f7625246322a7fda1b9bc676e34d26ea25542
note: kb/theory/agent-memory-requirements/create-memory-directly.md
input-sha256: 0bdfa3ce9899554531cdf9949d928fd9ac673d1f3941e7ebec2b623341d4f608
candidate: null
candidate-sha256: null
observation: kb/reports/state/review/runs/v2/revise/kb/theory/agent-memory-requirements/create-memory-directly/cc1a38038007/artifact/edits/4913a1286c36f61ec43226ed/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: sonnet
  effort: medium
model: claude-sonnet-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/agent-memory-requirements/create-memory-directly/cc1a38038007
launch: 8d5b82d6bd03429ba3da0f446115d625
completed-at: '2026-11-16T11:36:19Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/agent-memory-requirements/create-memory-directly/cc1a38038007/calls/launches/8d5b82d6bd03429ba3da0f446115d625/outputs/result.md
raw-output-sha256: 5043e2da6bab0d206765039122d6d076123f5604eae5127d76e22cc09a678c34
---

# Report

Four proposals; none applied.

Kept (not proposed):

- "Direct memory creation is the context-efficient path when understanding is already available during work": protected by `defend`; already literal.
- "Forcing the lesson through later trace extraction spends future context on rediscovery and risks losing structure the agent already had": protected by `defend`. "Forcing" is a mild figure, but it carries the contrast with direct writing, and rewording would risk narrowing the claim.
- "spends future context", "rediscovery", "context-efficient": field vocabulary with a literal mapping.
- "representational form", "authority path", "promotion": registered or defined KB terms.
- Evaluation Questions 2-4: already plain and positive.

Noticed outside scope (not proposed):

- Second paragraph: "Direct creation is not blank-page writing" is a negation-first construction, and "not just accept content after the fact" is a contrast. Both are outside the stated scope.
- Failure Modes opening: "fails when it becomes generic capture rather than a role-specific artifact" is a contrast, outside scope.

No questions of step 6: no figure lacks a referent.
