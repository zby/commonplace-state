---
type: types/edit-result.md
outcome: unchanged
description: Retained unchanged result of kb/instructions/simplification-passes/narrow-overclaims.md
  on kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
format: 1
operation: kb/instructions/simplification-passes/narrow-overclaims.md
operation-sha256: fff83f2074936afa498432ab20d6f522624d8af329308aa5cdb1bd7f5cd99feb
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
input-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/artifact/edits/459954aada21701f5cfe2c49/results/bf8daf636ccb47e3b8a07e75465e1d26/candidate.md
candidate-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/artifact/edits/459954aada21701f5cfe2c49/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z
launch: bf8daf636ccb47e3b8a07e75465e1d26
completed-at: '2026-11-18T16:07:21Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/calls/launches/bf8daf636ccb47e3b8a07e75465e1d26/outputs/result.md
raw-output-sha256: 71848092b0485f2dfa971721e5ec11fb68009d8f8a4b0ad515217c257756e63c
---

# Report

No sentence changed. The scope is the single opening-paragraph sentence "A claim of full automation must say which tasks it preserves and which requirements it retires."

The sentence is a normative condition on an automation report, not a claim about what another system holds, what builders expect, or what the note's method can decide precisely. None of the operation's moves applies:

- **From held to judged:** it attributes no belief or content to a system.
- **No attributed expectations:** it attributes no expectation to builders or authors.
- **Name the instrument actually used:** it does not claim the note's method decides anything precisely.

The note's own argument supports the sentence as written. "Name the process being automated" shows that calling a whole process automated, when the specification still assigns a maintainer a review that goes undone, "would conceal an omitted task". It also lists the ways a check can change: moved, partly or wholly automated, replaced by a different control, or no longer required. Saying which tasks remain and which requirements are retired is therefore the minimum a full-automation claim needs to avoid that concealment. The sentence is also bounded already: it covers only claims of *full* automation, and the note says separately that "A claim about automated adoption alone need not include monitoring or revision." The sentence does not claim that any requirement must be retired, and it does not say that keeping or retiring a task is justified; the next sentence leaves usefulness and necessity as a separate question.

Noticed but not applied, because it is outside this operation: "which tasks it preserves" does not say that these are the *human* tasks. Writing "which human tasks it keeps" would match the purpose statement more closely. That is a clarity edit, not a narrowing.
