---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: bcdab9a9707244b8a3b307957cd61085
completed-at: '2026-11-20T11:12:21Z'
findings:
- scope: passage
  quotes:
  - is a runtime in which prompt-backed agents and Python functions share one callable
    namespace and invoke each other by name
  reason: 'The Mechanism section rests on specific claims about llm-do: a shared callable
    namespace, callables receiving only declared arguments rather than conversation
    history, per-call binding resolution, and `.agent` files as frontmatter plus system
    prompt. The only support is a link to an external GitHub repository. There is
    no tracked kb/sources ingest and no paired quotation. The note carries the has-external-sources
    trait, and these descriptive claims are load-bearing as the concrete instance
    of the mechanism. Within this gate''s reading scope they cannot be checked against
    retained source material. They are plausible, but the support route is not verifiable.'
  level: warn
- scope: passage
  quotes:
  - describe the learning mechanisms — narrowing the interpretation space, changing
    medium
  reason: The linked codification definition moves a rule into symbolic form either
    by rewriting it or by adopting a consumer as its reference. It states that under
    adoption the text does not change. 'Changing medium' fits only the rewriting route.
    The note concerns code extraction, so the gloss is harmless here, but it is narrower
    than the definition the note cites.
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/1e51644b9c368161d2e3a8cb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/outputs/review-grounding-alignment.md
raw-output-sha256: 3769779a9c09528b5349f8bd4f6667311e55451415f021248b5abd62e55e0467
---

# Review

## Summary

I checked each evidential link for representation:

- **English account** (`prompting-changes-failure-diagnosis-with-the-semantic-reference.md`): The target states that under an applicable interpretation an instruction permits a set of behaviors and the executor produces one. It also states that extracting a repeated operation into code is a different intervention whose trade-off should be assessed. The note's attribution matches both claims and their scope.
- **Typed callables** (`instructions-are-typed-callables.md`): The target's opening limits callability to "this limited sense" and says that a signature does not turn a procedure into a conventional function. The note reproduces that qualification and presents the extension to tools as its own.
- **Constraining and codification definitions:** "Narrowing the interpretation space" matches the constraining definition. "Changing medium" is a narrower gloss of codification than the definition gives (INFO).
- **Spec mining:** The ticket example's step, checking decisions against outcomes and keeping a rule, matches the target's pattern of watching behavior, identifying regularities and extracting them.
- **Relaxing and relaxing signals:** The target defines relaxing as replacing an extracted component with a more general one. It explicitly separates that from switching to a prompt to test a changed requirement. The signals note lists distribution shift and brittleness. The note's use matches both.
- **llm-do** (external GitHub link): This link carries the concrete mechanism, but it has no tracked ingest or quotation. Its specific architectural claims therefore cannot be verified (WARN).

The remaining footer links, to the scheduler, programming-practices and abstracted-into notes, are adjacency or extension relations and make no support claim that needs checking.
