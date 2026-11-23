---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
outcome: fail
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 765fee9a50524c84b74692bd14c7d801
completed-at: '2026-11-20T09:44:01Z'
findings:
- scope: passage
  quotes:
  - says components should move between underspecified (LLM-interpreted) and precise
    (code) semantics as systems evolve — constrain patterns to code, relax rigid code
    back to LLM
  reason: 'The sentence credits the linked note (prompting-changes-failure-diagnosis-with-the-semantic-reference)
    with a prescription: components should move in both directions between LLM interpretation
    and code as systems evolve. The target never makes that claim. It compares two
    accounts of prompting: programming in a language defined by a model package, and
    executing English through a fallible interpreter. It explains how the choice of
    semantic reference changes the diagnosis of a failure. It does not use the term
    ''underspecified''. It mentions code extraction only as a trade-off to assess,
    with no bidirectional constrain/relax rule. The English-execution account (an
    instruction permits a set of behaviors) loosely supports the ''underspecified''
    half. The note''s main premise, that this framing calls for movable boundaries,
    is not in the target.'
  level: fail
- scope: passage
  quotes:
  - argues that prompts, skills, and tools share a callable structure with typed inputs
    and outputs
  reason: The target (instructions-are-typed-callables) argues something narrower.
    Skills, tasks and workflows are callable 'in this limited sense' and declare document-type
    signatures such as note → connection-report. The target does not discuss tools
    or prompts generally as sharing a callable structure. It also warns that declaring
    a signature does not turn a procedure into a conventional function. The note then
    calls llm-do the operationalisation that makes 'the type-theoretic view practical
    rather than just analogical'. That claim stretches the target's document-type
    interface checks into a general neural/symbolic function equivalence that the
    target explicitly declines to assert.
  level: warn
- scope: passage
  quotes:
  - describe the learning mechanisms — narrowing the interpretation space, changing
    medium
  reason: Constraining as 'narrowing the interpretation space' matches its definition,
    which also counts constraining as learning in Simon's sense. Glossing codification
    as 'changing medium' is looser. The definition says codification moves a rule
    into symbolic form, either by rewriting it or by adopting a consumer as the governing
    reference. In the adoption case the text does not change. The gloss is close enough
    for a passing reference.
  level: info
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/765fee9a50524c84b74692bd14c7d801/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/149db9ee906ea46ea4f7ee4b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/765fee9a50524c84b74692bd14c7d801/outputs/review-concept-attribution.md
raw-output-sha256: f5c3673bfaeba0c27e95b340d31953be3a5b5c1f7878dd63414909d41f9678be
---

# Review

## Summary

I checked every identity claim against its linked target. The spec-mining attribution holds: spec-mining is "discovering that an underspecified spec consistently resolves to one interpretation, then committing to it in code". The target's pattern (watch behavior, extract regularities into deterministic artifacts) supports it. The constraining attribution also holds.

The opening attribution fails. The note's motivating premise comes from a "framing" that the linked note does not state. That note is about the semantic reference and failure diagnosis, not about a boundary that should move in both directions. A reader who follows the link to find the constrain/relax prescription will not find it. The typed-callables attribution overstates its target's scope by adding tools and prompts. It also turns the target's limited, document-typed sense of "callable" into a general equivalence.

The external llm-do repository link makes no identity claim about another note's concept, so it was not checked.
