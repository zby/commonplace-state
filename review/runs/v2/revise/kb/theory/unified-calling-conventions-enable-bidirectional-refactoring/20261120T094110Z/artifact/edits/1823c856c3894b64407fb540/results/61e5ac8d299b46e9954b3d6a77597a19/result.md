---
type: types/edit-result.md
outcome: changed
changes:
- 'Surfaced the core claim: the opening paragraph now leads with the unified calling
  convention and its same-interface condition, and names both directions beside it
  (codify and extend in production; switch working code back to a prompt to test proposed
  requirements).'
- Moved the English-account context into a second opening paragraph that frames the
  claim as the answer to the premise's practical question; the link and both of the
  account's claims are kept.
- Removed the recap after the scheduler table ('The imperative style means refactoring
  ... uses the same patterns as normal code refactoring — extract function, inline,
  rename. No graph topology to update.'), which repeated the table's Refactoring row,
  as the scope directs.
- Removed 'Both are callables with defined interfaces.' from the typed-callables section,
  as the scope directs.
- 'Sentence-level edits: split the codification-breaks-callers sentence so its condition
  parses on first reading; replaced the semicolon splice in the big-bang-rewrites
  sentence with two sentences, keeping the expectation-not-observation qualifier;
  tightened the scheduler-introduction sentences.'
removed-links: []
description: Retained changed result of kb/instructions/simplification-passes/readability-and-flow.md
  on kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
format: 1
operation: kb/instructions/simplification-passes/readability-and-flow.md
operation-sha256: 01707fd7181b99fd0fa1f7bc60fcc6d289b0dcdd5abbacf34daa5d33777123db
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
input-sha256: c313ede182020d64c7bde03019de23a6edf6bbcca9f1859f8eced54ebde46139
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/calls/launches/61e5ac8d299b46e9954b3d6a77597a19/outputs/candidate.md
candidate-sha256: 619f99101fbaf6912c769229e997d8cc9c48c12d8b8022e85a450de82405a976
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/artifact/edits/1823c856c3894b64407fb540/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z
launch: 61e5ac8d299b46e9954b3d6a77597a19
completed-at: '2026-11-20T10:00:53Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/calls/launches/61e5ac8d299b46e9954b3d6a77597a19/outputs/result.md
raw-output-sha256: 1105bb538d4a68f2b18415b75711b71e65be08ef779ee813e3947a9ddd4adaa7
---

# Report

Structural moves:

- Surfaced the divergence: the core claim (shared interface → callers unaware → local refactoring with unchanged call sites) now opens the note, with both directions named next to it, using only what the body states.
- Split the former single opening paragraph at its argument boundary: claim first, then the English-account premise it answers.
- Deduplicated the scheduler recap sentence and its fragment "No graph topology to update." against the table's Refactoring row (scope-directed removal).
- Cut "Both are callables with defined interfaces." (scope-directed removal).

Sentence-level edits: 6 (codification-breaks-callers split, semicolon splice in the friction sentence, a missing "and" in the breaking-change list, two scheduler-introduction tightenings, the English-account sentence split).

Relied-on terms and claims from kb-role are kept: same name resolving to either implementation, local refactoring with unchanged call sites, reversibility back to a prompt, the hybrid VM example, the imperative-scheduler versus graph-DSL contrast and per-agent local scope (table rows untouched). All must-keep items are preserved. Steps 3 and 4 and the table rows are untouched, per scope.

Noticed but not applied: the must-keep statement that switching to a prompt "need not reflect brittleness or scaling" is not stated in the text; adding it would add a claim, which this pass does not do.
