---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 42d3e1baabad4cc48a4f34214ae538b7
completed-at: '2026-11-20T09:15:36Z'
findings:
- scope: passage
  quotes:
  - High-epiplexity regularities are genuinely structural — codifying them is safer
    because they reflect real patterns, not artefacts of the observer's computational
    budget
  reason: 'Conflates the source account (Finzi et al.''s epiplexity framework, introduced
    in the preceding sentence) with the current note''s application of it to codification.
    Reading A: the paper establishes that high-epiplexity regularities are structural
    and that codifying them is safer; the note reports this. Reading B: the paper
    defines epiplexity as learnable structure under computational bounds, and the
    note itself extends that to a claim about codification safety. The paragraph opens
    with "Two formal results help bound when codification bets are safe", which attributes
    the bounding role to the results, and the Sources footer says the paper "grounds
    when codification targets real patterns". The choice changes attribution and what
    the note contributes. The author must decide whether the codification-safety claim
    is the source''s or the note''s application.'
  level: warn
- scope: passage
  quotes:
  - separates exact specs (the spec is the problem) from proxy theories (the spec
    is a theory about a larger capability). Since you can't reliably tell which regime
    you're in
  reason: 'The object to which the regime classification applies shifts between the
    situation ("which regime you''re in"), decompositions ("Arithmetic-regime decompositions"),
    and an artifact relative to a contract (heuristic 1). Two assignments: the regime
    is a property of the problem the practitioner faces, or of one artifact-requirement
    path. Heuristic 1''s "relative to that numerical contract" largely settles it
    toward the path reading, so the blur is plausible but mostly resolved by context.'
  level: info
contract: verdict
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/42d3e1baabad4cc48a4f34214ae538b7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/f3d8b9465f519ef2b865c100/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/42d3e1baabad4cc48a4f34214ae538b7/outputs/review-conceptual-role-conflation.md
raw-output-sha256: c29bd06c3c88a7f1f57ff831f890cfe80ab97d9307420ea7856e7df9f95455e6
---

# Review

The note is generally careful about roles. The Codification paragraph explicitly separates the linked definition (moving a rule into symbolic form by rewriting or adoption) from the narrower code-extraction case this note concerns, and says what is excluded (prose conventions) and what remains codification without this case's benefits (adopted model packages). The relaxing paragraph likewise states what relaxing reverses (the extraction) and what it does not (symbolic membership). These pass.

The material role blur is in the epiplexity paragraph. A cited formal framework is described, and the next sentence moves without a marker from the framework's distinction to a claim about which codifications are safer. A reader cannot tell whether the codification-safety claim is inherited from the paper or is the note's own extension. The adjacent Ebrahimi paragraph avoids this by marking its inference with "This means", so the contrast is visible within the same section.

The regime-object shift is noted as INFO because heuristic 1 resolves it.
