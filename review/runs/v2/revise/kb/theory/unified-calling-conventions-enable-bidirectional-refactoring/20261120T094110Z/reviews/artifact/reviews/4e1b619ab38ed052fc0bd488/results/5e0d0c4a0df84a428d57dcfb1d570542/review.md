---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that
    owns control flow rather than a graph DSL. This is a deliberate contrast with
    declarative agent frameworks (LangGraph, CrewAI) where orchestration is defined
    as node-edge graphs.
  - '| State | Global context through graph | Local scope — each agent gets only its
    arguments |'
  - '| Control flow | DSL constructs | Native Python: `if`, `for`, `try/except` |'
  reason: 'The scheduler section is a branch about a second architectural choice:
    imperative orchestration versus graph DSLs. The main claim concerns the calling
    convention: same interface, name-based dispatch and unchanged call sites. Only
    the closing point, that cross-boundary refactoring reuses ordinary extract/inline/rename
    moves, bears on that claim. The State and Control flow rows and the LangGraph/CrewAI
    contrast add unsourced comparative claims about other frameworks. Those claims
    widen the attack surface without supporting the call-site argument. Reduce the
    section to one sentence on refactoring moves, and move the framework comparison
    to an llm-do system review or the abstracted persistence-boundary note. The open
    question on whether the scheduler is Python-specific should move with it.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/compression-bundle/branch-bloat.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/compression-bundle/branch-bloat.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/5e0d0c4a0df84a428d57dcfb1d570542/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/4e1b619ab38ed052fc0bd488/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 5e0d0c4a0df84a428d57dcfb1d570542
completed-at: '2026-11-20T09:43:41Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/5e0d0c4a0df84a428d57dcfb1d570542/outputs/review.md
raw-output-sha256: 69f5a6695f9118429d6309e1669646307ad4642a017290cad3691abe84bf9ce6
format: 2
---

# Review

**Main claim.** When neural and symbolic components share a calling convention, components can move across the boundary without changing call sites, so refactoring is local in both directions. llm-do's name-based dispatch over a hybrid VM serves as the demonstration.

**Material that supports the claim in its current place.**
- The mechanism section and the dispatch-chain diagram supply the premise.
- The four-step progression shows the codifying direction.
- The paragraph on switching `ticket_classifier` back to a prompt shows the relaxing direction, which the title's "bidirectional" commits the note to. It is long, but it supports the claim.
- The typed-callables section is compact. It ends by tying the calling convention to the claim ("makes the type-theoretic view practical"), so it supports the claim as context.
- The namespace-scale and debugging open questions are already in the right place for open questions.

**Branch that needs action.** "The scheduler layer" section compares orchestration styles (graph DSLs vs. an imperative scheduler) across four dimensions. Only one dimension, refactoring, connects to the main claim, and the section's last sentence already makes that point. The comparison of state handling and control flow, and the named contrast with LangGraph and CrewAI, are a separate claim about llm-do's design. That claim needs its own evidence, and here it draws attention away from the call-site mechanism. Keep a single sentence noting that cross-boundary refactoring uses ordinary code-refactoring moves. Rehome the comparison, together with the related Python-specificity open question.
