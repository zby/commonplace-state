---
type: types/edit-result.md
outcome: changed
changes:
- 'new-pattern (link text claims more than the target, or a different main claim):
  replaced the link text ''inspectability as a property of form'' with ''inspection
  needs an affordable route, not just readable form''; same target.'
- 'new-pattern (link text claims more than the target, or a different main claim):
  unlinked the must-keep sentence ''a plausible written rule need not be what actually
  drove the model''s behavior'', added the target''s own consequence ''so a rationale
  read from it can send repair to the wrong rule'', and attached the link as a parenthetical
  with the target''s title as text; same target.'
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
input-sha256: 3501d8329bf6f3ec2c30d2a91b2ec8f9cc08f952372e3de48cbf04555fb0397a
candidate: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/calls/launches/4e6c9179cb4f4a8eae1bc8e075d1486e/outputs/candidate.md
candidate-sha256: 1012bb6ee7962b45d9c9720ac6443a0b15de294d3e58065af99dbe134f81592c
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/artifact/edits/6d60503c7d8b9921770cf6c4/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z
launch: 4e6c9179cb4f4a8eae1bc8e075d1486e
completed-at: '2026-11-21T19:46:52Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/calls/launches/4e6c9179cb4f4a8eae1bc8e075d1486e/outputs/result.md
raw-output-sha256: 0b0cf1958e825a9c4e223d4991d2503cb1192abe7f9152972a4bc60db28f46cd
---

# Report

Strategy: `new-pattern`. The link text promised a claim the target does not
make or qualifies. The fix rewrites the link text to match the target's main
claim and keeps the target. No listed strategy covers link text.

1. Passage `([inspectability as a property of form](../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md))`.
   The link text now reads "inspection needs an affordable route, not just
   readable form". This matches the target's claim that readable rules supply
   an inspection route only at affordable cost and that symbolic form alone
   does not. It also agrees with the sentence it closes.
2. Passage `[a plausible written rule need not be what actually drove the model's behavior](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md)`.
   The must-keep claim (legibility does not guarantee faithfulness; a written
   rule need not be what drove behavior) stays verbatim as plain prose. A short
   clause now states what the target argues: a rationale read from such a rule
   can send repair to the wrong rule. The link follows as a parenthetical
   titled with the target's own title. The clause comes from the target's
   description. It narrows nothing and adds no claim beyond the linked note.

Untouched: finding 3 (`Readable, [addressable](...) store`, level info). It is
outside the supplied scope, which names only the two WARN link texts. Both link
targets are kept. Nothing else in the text changed.
