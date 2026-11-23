---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The imperative style means refactoring between neural and symbolic uses the same
    patterns as normal code refactoring — extract function, inline, rename. No graph
    topology to update.
  reason: 'The table''s Refactoring row already says this: ''Redraw edges, update
    graph'' versus ''Change code — extract functions, inline agents''. The closing
    sentence adds only the explicit link to the neural/symbolic boundary. Its last
    clause, ''No graph topology to update'', repeats the Graph DSL cell outright.
    Recommend cutting the trailing clause and folding the neural/symbolic link into
    the sentence that introduces the table, or into the Refactoring row.'
  level: warn
- scope: passage
  quotes:
  - Both are callables with defined interfaces.
  reason: 'The previous sentence already entails this: `.agent` files are a type signature
    plus an implementation, and tools are typed Python functions. Deleting it costs
    nothing, because the next sentence makes the point that matters, unified calling
    makes the typed-callable view practical. Cut it.'
  level: warn
- scope: passage
  quotes:
  - Local scope — each agent gets only its arguments
  - 'Native Python: `if`, `for`, `try/except`'
  reason: The State and Control flow rows contrast llm-do with graph DSLs on axes
    that do not bear on the note's claim about movable neural/symbolic boundaries.
    They may be useful context about the scheduler. It is unclear whether they do
    reader work here or belong in a note about llm-do's orchestration style.
  level: info
- scope: passage
  quotes:
  - Each link can be independently refactored without disturbing the rest.
  reason: This mostly restates the intro's 'refactoring across the boundary becomes
    a local operation' and the preceding paragraph's 'the prompt that invokes it doesn't
    change'. Its remaining job is to caption the diagram's multi-hop chain. Possibly
    fold it into the diagram's lead-in sentence.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/f326cb0c639a41ff91f45cd40f51996f/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/701eac605e9d7583ce69d29d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: f326cb0c639a41ff91f45cd40f51996f
completed-at: '2026-11-20T09:44:38Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/f326cb0c639a41ff91f45cd40f51996f/outputs/review.md
raw-output-sha256: 1459a55755da0a482e7d8e46d9cc6529f34533732a5f2f6a94c4794fceab1458
format: 2
---

# Review

Most of the note earns its space. The opening paragraph gives the gap and the answer once. The name-based dispatch paragraph states the requirement that makes the mechanism work. The four-step progression makes the codify/relax cycle concrete. The `ticket_classifier` paragraph adds a distinct use: switching back to a prompt for exploration while working code still exists. That case is not covered by step 4's relaxing for new requirements, so it is not redundant. The friction sentence in "Why this matters for constraining" ("pushes toward big-bang rewrites") turns the mechanism into a consequence and should stay.

The problems are local and come from recap. In the scheduler section, the paragraph after the table repeats the table's Refactoring row. The typed-callables section contains one sentence that its previous sentence already entails. Two lower-confidence items are flagged as INFO: the comparison-table rows that do not touch the note's claim, and the sentence after the diagram, which partly recaps earlier text.
