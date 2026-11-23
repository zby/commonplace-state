---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Solving a hard problem in a bounded LLM context pushes an agent system toward
    **context isolation**: load deep task-relevant material and exclude unrelated
    work so the task stays within the model''s usable attention budget, because [context
    efficiency binds first on per-window feasibility](./context-efficiency-is-the-central-design-concern-in-agent-systems.md).'
  reason: 45 words chaining four clauses (push toward isolation, colon-introduced
    definition, purpose clause, and a trailing causal clause reaching back across
    the definition to ground the main push); moving the because-clause next to context
    isolation or splitting the definition into a second sentence reduces working-memory
    load without losing meaning.
  level: warn
- scope: passage
  quotes:
  - '**Global prioritization**—deciding how much effort a local branch deserves relative
    to other work, when to stop or defer it, and whether a blocker warrants interrupting
    scarce operator attention—moves in the opposite direction.'
  reason: 'A 26-word three-item em-dash list separates the subject from its verb (''moves
    in the opposite direction''); reordering to put the predicate immediately after
    the subject (''Global prioritization moves in the opposite direction: deciding...'')
    preserves every word and relation while closing the subject-verb gap.'
  level: warn
- scope: passage
  quotes:
  - A system operating under those conditions whose isolated task workers reliably
    make decisions whose right answer depends on unseen competing work—or that loads
    full live portfolio state alongside deep task context without degrading execution
    competence—would refute the claim.
  reason: A 33-word chain of participial, nested 'whose', and coordinated em-dash
    relative clauses separates the subject ('A system') from its verb ('would refute
    the claim'); reordering so the main predicate comes first ('The claim would be
    refuted by a system operating under those conditions...') keeps every word and
    relation without the long gap.
  level: warn
- scope: passage
  quotes:
  - When it encounters an out-of-scope defect, tangent, or decision boundary, it supplies
    the local judgments its deep context uniquely supports—**scale-bearing local facts**
    such as what will break, how soon, whether waiting is reversible, whether the
    main path is blocked, and what decision would change—recorded on a discoverable
    surface or in a typed stop record.
  reason: 56 words packing four ideas (trigger condition, local judgments, a five-item
    definition of scale-bearing local facts, and recording surface) with a 23-word
    interrupting em-dash list between the object and its trailing modifier ('recorded
    on...'); moving the shorter recording phrase before the em-dash list (or splitting
    the enumeration into a second sentence) resolves both length and distance.
  level: warn
- scope: passage
  quotes:
  - '*Single-artifact workflow stops:* [ADR 138](../reference/adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md)
    unbundles the three decisions for unattended note revision—a run ends at its first
    stop with a typed continuation record, an operator''s answer to a stop can be
    recorded so the next run does not re-ask, and commissioning follow-up work such
    as a rewrite remains a separate decision.'
  reason: 54 words chaining four clauses (five finite verbs) after an em-dash; splitting
    at 'revision.' into a lead sentence followed by the three-part mapping reduces
    working-memory load without losing meaning.
  level: warn
- scope: passage
  quotes:
  - Because [an insufficient summary precedes the source rather than replacing it](./an-insufficient-summary-precedes-the-source-rather-than-replacing.md),
    an isolated worker that emits an uninformative blocker ("blocked on operator input")
    or drops the local detail that makes an issue severe forces triage either to fall
    back to deep context or to misclassify severity under unsafe substitution.
  reason: '51 words with five finite verbs and two long unresolved dependencies open
    simultaneously: an 11-word leading because-clause followed by a 19-word coordinated
    relative clause separating ''an isolated worker'' from ''forces''; moving the
    because-clause after the main clause (or into a separate sentence) and recasting
    the long subject as a when-clause relieves both peak load and distance.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/sentence/clause-packing.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/sentence/clause-packing.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/c043185d3d9f4a17b0d509c28ec48409/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/artifact/reviews/b78f86471eed9d88dae28f87/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: null
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews
launch: c043185d3d9f4a17b0d509c28ec48409
completed-at: '2026-11-19T13:45:04Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/c043185d3d9f4a17b0d509c28ec48409/outputs/review-clause-packing.md
raw-output-sha256: 0618725d69fd1de9be80fbdf1fdc276887cfa56c68bbebddcf4e40decfda1d35
format: 2
---

# Review

Most sentences in the note are concise and well-paced, but six sentences exceed working-memory limits through either long subject-verb/head-modifier interruptions or multi-clause chaining past 40 words. The most severe instances are the refutation sentence (a 33-word subject-verb interruption across nested relative clauses), the scale-bearing local facts sentence (56 words with a 23-word list separating object from modifier), and the insufficient-summary sentence (two long open dependencies at once). In most cases, reordering the interrupting clause or moving the shorter phrase first removes the load without dropping content; splitting works cleanly where four distinct clauses are chained.
