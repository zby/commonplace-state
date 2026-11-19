---
note: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
note-sha256: 69550b9aa320f6c0200baf5efdd2222b48aa5f8276f6ce43065c56f3cff23ea0
criterion: kb/instructions/review-gates/sentence/clause-packing.md
criterion-sha256: 574b8a9b1a59c9337d2236c50a10cf9443a41de9a7b5629dd4af39737cdbdad9
outcome: warn
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: 061c70de9982450b95b1c9f6d3ed3fe9
completed-at: '2026-11-12T08:26:22Z'
---
### Summary

The note is generally easy to follow. Two sentences nest qualifications and conclusions deeply enough to merit revision. The longer hybrid-document example remains readable because its two parallel descriptions directly explain the same distinction.

### Findings

- WARN: In “Current state of the gap,” the sentence beginning “But this note exists to mark the gap” nests the note’s purpose, a future condition (“when we want”), a relative clause (“that supports”), a parenthetical contrast, and the conclusion about future design work. The reader must retain the purpose and condition before reaching the substantive claim. Moving the condition first helps, but separating the statement of purpose gives the claim a natural structure.
- WARN: In the first “Open questions” item, the sentence beginning “But their internal structure is diverse enough” combines structural diversity, the inference about local conventions, the condition that more temporal types appear, and a trailing comparison to an existing argument about tasks. The final “what … already argues” phrase arrives after the reader has resolved the main inference and requires attaching another relation. Put the condition first and separate the comparison.

### Suggested Revision

For “Current state of the gap”:

> When we want to build a knowledge base that supports real workflows (not just knowledge management), the workshop layer is where most of the new design work will be needed. This note exists to mark that gap.

For the first “Open questions” item:

> As more temporal types appear, local conventions per subsystem are likely the right default because their internal structure is diverse. This extends what [why directories despite their costs](./why-directories-despite-their-costs.md) already argues for tasks.

## Result: WARN
