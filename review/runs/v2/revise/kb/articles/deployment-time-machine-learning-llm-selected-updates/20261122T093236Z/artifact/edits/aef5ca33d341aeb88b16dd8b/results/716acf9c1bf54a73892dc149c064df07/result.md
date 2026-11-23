---
type: types/edit-result.md
outcome: proposed
proposals:
- quote: represents the hard-oracle extreme
  change: is the strictest case, where a change is admitted only by formal proof
  reason: figure 'hard-oracle extreme' made literal; the next sentences state the
    proof requirement
- quote: Honest sets of compatible measures leave many trade-offs open.
  change: Realistic sets of compatible measures leave many trade-offs open.
  reason: '''Honest'' is a moral adverb for a set of measures; ''realistic'' says
    what is meant'
- quote: the paradigm claim stays honest only if success is judged
  change: the paradigm claim has content only if success is judged
  reason: '''stays honest'' made literal: without a success condition the claim would
    exclude nothing'
- quote: The system can still act on it as a bounded decision
  change: The system can still act on it, as a decision whose possible loss is limited,
  reason: '''bounded decision'' made literal; the clause that follows names reversibility
    as the limit'
description: Retained proposed result of kb/instructions/simplification-passes/plain-wording.md
  on kb/articles/deployment-time-machine-learning-llm-selected-updates.md
format: 1
operation: kb/instructions/simplification-passes/plain-wording.md
operation-sha256: ae9094451a0d8c479ebfd0dd4d4f7625246322a7fda1b9bc676e34d26ea25542
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
input-sha256: de7364c2bdff81e4854c7b93d299ad587921f91ada3618bba09a65c7bc503253
candidate: null
candidate-sha256: null
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/artifact/edits/aef5ca33d341aeb88b16dd8b/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: sonnet
  effort: medium
model: claude-sonnet-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z
launch: 716acf9c1bf54a73892dc149c064df07
completed-at: '2026-11-22T09:51:56Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/calls/launches/716acf9c1bf54a73892dc149c064df07/outputs/result.md
raw-output-sha256: 1772733bc9e549c9f4c0fb784e49bcb3414a89c93a0c12679022841548008462
---

# Report

Scope was the five quoted phrases; four become proposals, none applied.

Kept, with reason:

- "a third change revises the review check itself" (the scope list's fifth phrase). It is literal: the change edits the check by which edits are accepted. "Third change" counts the edits in the sequence. No figure and no exclusion to remove.
- "bounded decision" is a defensible term here, since it recurs in the note's theory sources. It is proposed for replacement only at the one occurrence in scope; the other uses ("a bounded decision under reversibility", line 100) are outside scope and unchanged. The operator may reject the proposal if one term should be kept at every occurrence.

Questions (step 6): none.

Must-keep and kb-role claims are untouched: the title, the "comparison, not a single score" claim, the fixed-weight-LLM bet, the "no completed end-to-end automated run" status and the "letting a change stand while its verdict is open" sentence do not occur in any proposal.
