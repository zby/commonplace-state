---
type: types/answers.md
description: The operator's answers to kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/artifact/edits/3ac11b80aa0026b5194a41c1/results/001ad28428d046088be5075196e73bf1/result.md
question: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/artifact/edits/3ac11b80aa0026b5194a41c1/results/001ad28428d046088be5075196e73bf1/result.md
question-sha256: d7d3efac9c0edef64e4c43b538c6a5ef2554d15641c99895d27f0825d37b449e
items:
- id: '1'
  proposal:
    quote: The first is a blocking dependency
    change: 'Name the blocking thing ''wait'' throughout, the word the title and the opening already use. Drop the alternate labels ''blocking dependency'', ''dependency'' and ''human stop'' (4 occurrences, all in scope): ''The first is a blocking dependency; the second is an unfulfilled requirement'' -> ''The first blocks execution; the second is an unfulfilled requirement''; ''A non-binding recommendation still creates a dependency if the agent must wait for it'' -> ''A non-binding recommendation still blocks execution if the agent must wait for it''; ''that assessment is a dependency of the revision process, though not of the earlier adoption'' -> ''the revision process waits for that assessment, though the earlier adoption did not''; ''without creating a human stop'' -> ''without creating a wait for a person''. Leave the verb ''depends on'' in the Required approval case, which is ordinary English.'
    reason: 'No occurrence needs a distinction that ''wait'' lacks: the note itself defines ''blocking dependency'' as ''an actual wait'', and every later ''dependency'' and the ''human stop'' in Scope name that same thing (execution cannot proceed until a person acts). With four names for one thing, a reader may take ''dependency'' in the revision paragraph or ''human stop'' in Scope for something other than the wait the title is about. kb-role lists these terms as unused by other notes, so no inbound use blocks the change.'
  state: pending
- id: '2'
  proposal:
    quote: Optional assessment creates neither
    change: 'Keep ''optional assessment'' throughout and replace its synonym ''optional study'' with it (3 occurrences): ''This is an optional study'' -> ''This is an optional assessment''; ''Using an optional study''s available findings does not itself require future studies'' -> ''Using an optional assessment''s available findings does not itself require future assessments''.'
    reason: 'The term is needed: the Optional assessment case and the revision paragraph contrast it with assessment that the specification requires or that execution waits for. The deciding occurrence is ''Making a new human assessment a condition of each revision does'', where the bare word ''assessment'' names the required kind, so the optional kind needs its qualifier. ''Optional study'' names the same activity under a second name, so it reads as a second referent.'
  state: pending
---

# Answers

Set each item's `state` on the operator's word: `approved`, `rejected` with a `reason`, or `deferred` with a `reason` and a `revisit` condition. A decided item also carries `decided-by: operator` and `decided-at`. Change no `id` or `proposal`.
