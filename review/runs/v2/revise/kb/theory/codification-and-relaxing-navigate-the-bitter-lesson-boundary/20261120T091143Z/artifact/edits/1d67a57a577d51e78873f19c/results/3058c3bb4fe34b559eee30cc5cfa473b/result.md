---
type: types/edit-result.md
outcome: changed
changes:
- 'Opening paragraph: kept the hybrid-not-partition sentence and moved its model-package
  caveat to the codification-definition paragraph.'
- 'Codification-definition paragraph: stated the model-package-adoption caveat once
  (''an adopted model package can itself be a codified reference'', without readable
  rules or lower inference cost), after the code-extraction case it is contrasted
  with.'
- 'Codification-definition paragraph: merged the prose-convention caveat with heuristic
  1''s constrains-without-codifying contrast, linked to definitions/constraining.md.'
- 'Relaxing definition: split so the cost/reliability-for-generality trade-off is
  its own sentence.'
- 'Heuristic 1: removed the last sentence (''Merely writing the convention…''), whose
  content now sits in the definition paragraph.'
removed-links: []
description: Retained changed result of kb/instructions/simplification-passes/readability-and-flow.md
  on kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
format: 1
operation: kb/instructions/simplification-passes/readability-and-flow.md
operation-sha256: 01707fd7181b99fd0fa1f7bc60fcc6d289b0dcdd5abbacf34daa5d33777123db
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
input-sha256: 877995d86d7e1940da9135a763a155eb1e3ae15d2cf24fb84d23720b54853459
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/calls/launches/3058c3bb4fe34b559eee30cc5cfa473b/outputs/candidate.md
candidate-sha256: 2737d2d4261e1be6b733c26e2c12c11520501749cb8704d14013f761da2c0344
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/artifact/edits/1d67a57a577d51e78873f19c/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z
launch: 3058c3bb4fe34b559eee30cc5cfa473b
completed-at: '2026-11-20T09:26:44Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/calls/launches/3058c3bb4fe34b559eee30cc5cfa473b/outputs/result.md
raw-output-sha256: ff53c41775e349fc0fcc73dcb4189c4e6f7f13d21efa3a0f208a61afed1ede72
---

# Report

Structural moves:

- Deduplicated caveats: the model-package caveat (opening and definition paragraph) and the prose-convention caveat (definition paragraph and heuristic 1) now each appear once, in the definition paragraph.
- Moved the constrains-without-codifying contrast from heuristic 1 into the definition paragraph, with a new link to `./definitions/constraining.md`.
- Split the relaxing-definition sentence at its argument boundary: the definition comes first, then the trade-off in its own sentence.

Sentence-level edits: 3. These are the opening's last sentence ('These hybrids are not a partition…'), the reordered model-package sentence and the reworded prose-convention sentence.

Preserved: the hybrid-not-partition point, "an adopted model package can itself be a codified reference", the term relaxing and its definition, and the sentence "The replacement can itself be codified by adoption; what relaxing reverses is the extraction, not symbolic membership". That sentence lies outside the assigned scope, so I left it unchanged. No link was removed. No text outside the scope changed.
