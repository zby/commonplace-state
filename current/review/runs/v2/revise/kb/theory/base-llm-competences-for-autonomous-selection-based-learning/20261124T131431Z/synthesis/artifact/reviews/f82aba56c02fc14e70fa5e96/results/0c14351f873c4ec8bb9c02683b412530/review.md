---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Because an LLM that writes code can also build new harness tools for those jobs,
    the frozen model does not need to keep track of budgets, traces, or regression
    suites in its head.
  reason: The bridge between the offload list and the three competences first repeats
    the list ('budgets, traces, or regression suites') and then adds a tool-building
    point the note never uses again. This delays the pivot to the semantic remainder,
    which is the half of the claim the title names. A revision could move the tool-building
    point into the lead-in to the bullets as one clause, drop the recap, and let the
    relocation-not-elimination sentence follow the list directly. Trimming each bullet
    to two representative sub-jobs is an optional part of the same fold.
- scope: passage
  quotes:
  - our working hypothesis is that three irreducible semantic competences remain on
    the frozen base LLM
  reason: 'The note''s epistemic status is stated in three places: the bold ''Working
    hypothesis'' lead-in, this sentence, and the first Scope bullet''s ''not an established
    impossibility result''. Inside the hedged sentence, ''irreducible'' asserts the
    strength that the Scope bullet later withdraws. A reader therefore gets repeated
    hedges and one overclaim instead of one clear status. A revision could state the
    status once, next to the three competences, together with the bullet''s revision
    rule: offloadable sub-tasks leave the LLM column, and newly found bottlenecks
    join it. The remaining labels could then be cut.'
- scope: passage
  quotes:
  - 'Separating them lets a human-assisted bootstrap identify which competence currently
    binds: people temporarily supply the missing semantic step while transfer tests
    check each kind of decision on its own.'
  reason: The independence paragraph justifies the three-way split, but its last sentence
    adds a method — a human-assisted bootstrap with transfer tests — that the note
    neither grounds nor develops. The method is really an answer to the first open
    question ('Which of the three competences binds first'). A reader cannot tell
    whether the method is part of the claim or a proposed use of it. A revision could
    end the paragraph at the independence point and attach the bootstrap to the first
    open question as a candidate way to answer it, or develop the method elsewhere.
outcome: report
description: Retained report review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
contract: report
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
criterion-sha256: c7ee82f0ff41ddcb59d841986fcc47111cf98d676924cffe53a7a9a98dfa6d1c
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/synthesis/calls/launches/0c14351f873c4ec8bb9c02683b412530/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/synthesis/artifact/reviews/f82aba56c02fc14e70fa5e96/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/synthesis
launch: 0c14351f873c4ec8bb9c02683b412530
completed-at: '2026-11-24T13:22:30Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/synthesis/calls/launches/0c14351f873c4ec8bb9c02683b412530/outputs/review.md
raw-output-sha256: 8a958f371bbc1487e280651e65c03ebb56206204e4ebc6e931235a4ce08e7431
format: 2
---

# Simplification synthesis: harness offloading and base LLM competences

The note's central claim is easy to find: harness code takes over much of the loop, and three semantic competences remain on the frozen model. None of the four checks found an obscured thesis. The opportunities below concern how the argument moves. One bridge holds back the pivot to the competences. The note's epistemic status is spread over three hedges and one overclaim. One sentence leaves unclear whether a method is part of the claim.

## Opportunities

### 1. Fold the bridge so the pivot follows the offload list

- Location: the opening section, from the three harness bullets to "Because an LLM that writes code can also build new harness tools for those jobs, the frozen model does not need to keep track of budgets, traces, or regression suites in its head."
- Combines: core-claim-obscured (an aside delays the turn), marginal-value-redundancy finding 2 (the consequence clause restates the bullets), detail-overhang (the list is restated twice later).
- Preserve or decide: whether the tool-building point does argumentative work. It implies that the offloadable set can grow as the LLM extends its own harness. That would support "much of the loop" and the Scope bullet's rule that sub-tasks leave the LLM column. If it does this work, keep it as one clause, possibly in the bullets' lead-in, rather than drop it. Keep the store-bookkeeping restatement in the criterion-revision paragraph, because there it marks the boundary that rules out a fourth competence. One possible resolution: "Harness code, including tools the LLM itself writes, can take over much of the loop's machinery:" followed by the bullets, then directly "Harness code can relocate mechanical and structural work, yet semantic work can be relocated without being eliminated."

### 2. State the hypothesis status once and resolve "irreducible"

- Location: the bold "**Working hypothesis.**" lead-in; "our working hypothesis is that three irreducible semantic competences remain"; the first Scope bullet.
- Combines: marginal-value-redundancy finding 1 (third repetition of the label, defensive contrast clause), plus a cross-cutting tension between "irreducible" and "not an established impossibility result".
- Preserve or decide: what "irreducible" means. The author must choose between "not offloadable to harness code in principle" and "not yet shown offloadable". The Scope bullet's revision rule supports the second meaning. If the author means the first, the Scope bullet understates the claim. Keep the revision rule and the separate necessary-not-sufficient bullet in either case. Do not settle this choice as a compression edit.

### 3. Separate the bootstrap method from the independence argument

- Location: the independence paragraph, last sentence ("Separating them lets a human-assisted bootstrap identify which competence currently binds…"), and the first Open Question.
- Combines: branch-bloat (an ungrounded applied method adds attack surface); detail-overhang treated the contrast example as earning its place, and this opportunity keeps that example.
- Preserve or decide: whether the note's contribution includes a procedure for finding the binding competence, or only the split itself. If it includes the procedure, the method needs grounding. If it does not, the sentence belongs with the first open question or in a separate note on bootstrapping. Keep the contrast example ("follow clear prose procedures while still misdiagnosing noisy traces"), because it is what shows that the competences fail independently.
