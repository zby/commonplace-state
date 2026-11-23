---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The house may keep the failure it exposed, a corrected dependency account, or
    a test for later scripts.
  - 'A house can combine both choices: keep a theory and examples, generate a short-lived
    implementation, test it, then retain the result that matters.'
  reason: '''The house'' / ''A house'' is used as an undefined actor or concept with
    no prior introduction, gloss, or link after earlier paragraphs refer to ''the
    deployed system'' and ''the system''. A first-time reader cannot tell whether
    it means the hosting runtime or harness, an engineering organization, or a KB-internal
    term; replace it with plain language or define it inline.'
  level: fail
- scope: passage
  quotes:
  - '[Codification](./definitions/codification.md) assigns an operation to a symbolic
    consumer.'
  reason: Codification is an active KB vocabulary term whose inline gloss depends
    on another undefined KB-specific phrase, 'symbolic consumer'. Although the next
    two sentences contrast a generated program with a natural-language procedure,
    a first-time reader without the KB's representational-form background cannot tell
    what makes a consumer 'symbolic' (a runtime, validator, or other consumer bound
    by formal rules rather than a model reinterpreting prose) without following the
    link.
  level: warn
- scope: passage
  quotes:
  - The [codification–relaxing account](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)
    addresses when to move operations between interpretation and assigned execution;
    it should not be read as a binary choice between learning and forgetting.
  reason: Introduces the KB-specific technical term 'relaxing' (in 'codification–relaxing
    account') through a link without defining it inline, and pairs it with the unglossed
    phrase 'assigned execution'. A reader unfamiliar with the linked note has to infer
    or click through to learn what 'relaxing' means and what 'assigned execution'
    refers to.
  level: warn
outcome: fail
description: Retained verdict review of kb/theory/ephemeral-computation-prevents-accumulation.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/ephemeral-computation-prevents-accumulation.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: d3a6a9e3e3da3e9b0cfdf1f37204cd3f0a4037ff53011b0c118feabbef1ffbc3
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/0a532cc50df3481eb93c77ca4fd6095a/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/artifact/reviews/17d62613e4ae0a05d825af70/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews
launch: 0a532cc50df3481eb93c77ca4fd6095a
completed-at: '2026-11-20T14:56:29Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/0a532cc50df3481eb93c77ca4fd6095a/outputs/review-undefined-terms.md
raw-output-sha256: 9993c13cfd1ed1887ebccdc32a100bc86ec6fcdb90a8d7d912a0ecf14a62d9ac
format: 2
---

# Review

## Summary

Most of the note is written in clear, self-contained prose, and `ephemeral computation` is defined inline in the opening sentence. However, three places rely on undefined or KB-internal terminology that leaves a first-time reader without adequate inline grounding: an unexplained actor term (`The house` / `A house`) with no antecedent or definition, an active-vocabulary gloss for `Codification` that leans on the undefined KB phrase `symbolic consumer`, and a linked reference to the `codification–relaxing account` that leaves `relaxing` and `assigned execution` unglossed.
