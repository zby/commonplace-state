---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - implements this through a hybrid VM where agents
  reason: '"Hybrid VM" is not defined as a term. The sentence says agents and tools
    share one namespace inside it, which is enough to keep reading. But it never says
    what "VM" means here (a runtime that executes both kinds of component). A short
    gloss such as "a hybrid runtime (VM) that executes both LLM agents and Python
    tools" would remove the guess.'
  level: info
- scope: passage
  quotes:
  - narrowing the interpretation space, changing medium
  reason: 'The two active vocabulary terms are linked and glossed, so this sentence
    meets the gate. The gloss for codification, "changing medium", is terse: it does
    not say which medium changes into which. The surrounding text implies the change
    is from LLM prompt to code. Stating that directly, for example "moving a behavior
    from prompt to code", would make the gloss self-sufficient.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/3eb26f9df34f411faf101251b0454a5c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/fcaf347fe5175e1e577b40c9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 3eb26f9df34f411faf101251b0454a5c
completed-at: '2026-11-20T09:42:07Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/3eb26f9df34f411faf101251b0454a5c/outputs/review-undefined-terms.md
raw-output-sha256: 7e68326d29c01b93a133efdd8cb6076344d43ef41d9af0910e125c881f51345d
format: 2
---

# Review

## Summary

Most technical terms are introduced with enough local context. The remaining gaps are minor.

The opening glosses its key distinction inline: "underspecified (LLM-interpreted) and precise (code)". It also explains spec-mining where it first appears. Name-based dispatch, late binding and the imperative scheduler each get a definition or paraphrase in the same sentence or the next one. The active vocabulary terms constraining and codification are linked at their first technical use and receive a paired gloss. Earlier uses of "constrain" and "relax" in the opening are ordinary verbs, and their objects explain them ("constrain patterns to code, relax rigid code back to LLM"). "Relaxing" in step 4 is defined by the action that follows it.

The two info findings concern glosses that could be sharper: "hybrid VM" is never expanded, and the gloss for codification does not name what changes into what. Neither prevents a reader from understanding the sentence.
