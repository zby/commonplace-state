---
type: types/edit-result.md
outcome: changed
changes:
- 'new-pattern (defensive redundancy: a disclaimer restated a third time with no new
  job) — ''Name the process being automated'', first paragraph: cut ''This example
  establishes a gap against the specification, not that skipping review causes harm.'';
  the paragraph now ends at ''Calling the whole process automated would conceal an
  omitted task.'''
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
input-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/artifact/edits/9f9a49e10ddd97f17adbf5ff/results/f0516976de26400f8a72ed9c4d124de1/candidate.md
candidate-sha256: 5111320ea026b34d7697f869a35f72cbd6b3245b5c481328ae21f02df13ae524
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/artifact/edits/9f9a49e10ddd97f17adbf5ff/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z
launch: f0516976de26400f8a72ed9c4d124de1
completed-at: '2026-11-18T19:06:17Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/calls/launches/f0516976de26400f8a72ed9c4d124de1/outputs/result.md
raw-output-sha256: 8bb16a1227ba9b075728a9780399ec0b42fd06c1ed9f288d29f3db0e66c6f3cd
---

# Report

One sentence cut.

- `new-pattern` — defensive redundancy, where a caveat the note already states is repeated with nothing new added. Passage: "This example establishes a gap against the specification, not that skipping review causes harm." Change: removed the sentence. The lead's "Whether a specified task is useful or necessary is a separate question" still makes the same point, as does the mechanism paragraph's "not by itself evidence that the system would fail or degrade without the task". The must-keep claims are unchanged. As the scope requires, "Calling the whole process automated would conceal an omitted task." is left unchanged.

Findings not touched:

- Finding 2 (info, "This distinguishes human work within the process from optional assessment of its results, rather than deciding who deserves causal credit for an improvement."): outside the supplied scope, which names only the sentence from finding 1. The reviewer also wasn't sure the clause should go, because it marks the boundary with the linked note.

No links or quoted spans were removed. The text has no `user-verified` field.
