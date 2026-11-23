---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The unified calling convention is what makes the type-theoretic view practical
    rather than just analogical.
  reason: The sentence lets 'the type-theoretic view' be read two ways. It may be
    the linked note's account (document-type signatures for skills and tasks), which
    llm-do applies. Or it may be the note's own extension of that account to Python
    tools and agent frontmatter. It is also unclear whether 'the unified calling convention'
    means the general concept or llm-do's implementation. Nearby context mostly settles
    this as an application ('llm-do operationalises this'), so the blur is plausible
    but below the materiality threshold for this gate.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/f44cbdf310d9276f2388dd94/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 96c4eea5828c4089a10b19a54bdfd799
completed-at: '2026-11-20T09:44:58Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/outputs/review-conceptual-role-conflation.md
raw-output-sha256: 84dad752dff49bc47276bd5c05b0df6d8a3bd870048585cca7617569373cac48
format: 2
---

# Review

I inspected the passages that import, apply or extend a concept:

- The opening attribution to the "underspecified instructions framing".
- The mechanism section, where llm-do instantiates the general convention.
- "Why this matters for constraining", which imports constraining and codification and then applies them in the progression.
- The typed-callables section.

In most passages the roles are clear. The general concept, a unified calling convention, is stated as the answer. llm-do is presented as one implementation ("llm-do implements this"). Constraining and codification are imported as the existing mechanisms that the convention makes cheaper. Whether the opening attribution matches its linked target is a grounding question, not a role conflation, because the sentence is clear about what it attributes to whom.

The only remaining blur is in the typed-callables closing sentence. Context ("llm-do operationalises this") points to the application reading, so the result is PASS with INFO.
