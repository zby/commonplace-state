---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Because an LLM that writes code can also build new harness tools for those jobs,
    the frozen model does not need to keep track of budgets, traces, or regression
    suites in its head.
  reason: The turn from what harness code offloads to what stays on the model is delayed
    by a sentence that recaps the three offload bullets, and the store-bookkeeping
    items are restated again in the criterion-revision paragraph, so the reader meets
    the offload half of the claim three times before and after the pivot; a revision
    could move the one new point (a code-writing LLM can build further harness tools)
    into the lead-in to the bullets, drop the recap, and place the relocation-not-elimination
    pivot directly after the list so the three competences arrive sooner.
- scope: passage
  quotes:
  - our working hypothesis is that three irreducible semantic competences remain on
    the frozen base LLM
  - This split is a **working hypothesis**, not an established impossibility result.
  reason: The note's epistemic status is stated three times (bold lead-in, competence
    introduction, first Scope bullet) while the competence introduction also calls
    the competences 'irreducible', and the Scope bullet's revision rule says offloadable
    sub-tasks leave the LLM column; the reader gets repeated labels but must reconcile
    'irreducible' with 'revisable' alone. A revision could state the status once,
    beside the competence introduction, together with the revision rule, and cut the
    duplicate labels and the defensive contrast clause.
outcome: report
description: Retained report review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
contract: report
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
criterion-sha256: c7ee82f0ff41ddcb59d841986fcc47111cf98d676924cffe53a7a9a98dfa6d1c
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/synthesis/calls/launches/1785cae14bf644c9be1ee4a5f7f9d3a0/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/synthesis/artifact/reviews/f82aba56c02fc14e70fa5e96/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/synthesis
launch: 1785cae14bf644c9be1ee4a5f7f9d3a0
completed-at: '2026-11-24T13:22:20Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/synthesis/calls/launches/1785cae14bf644c9be1ee4a5f7f9d3a0/outputs/review.md
raw-output-sha256: 5728468d5d27924089b1beb1c25204d2c4a86c00bb4bc276bd7ef43bbcb7d8fa
format: 2
---

# Simplification synthesis: harness offloading leaves three base LLM competences

The note's two-part claim is already prominent, and the four checks found no branch that competes with it. Two opportunities remain that each combine several local findings into one structural change. The bootstrap sentence flagged by branch bloat is compact and its destination is unclear, so it does not clear the threshold here as a separate opportunity.

## Opportunities

### 1. Make the pivot follow the offload list directly

- Location: opening section, from "Because an LLM that writes code can also build new harness tools for those jobs" to "semantic work can be relocated without being eliminated", plus the criterion-revision paragraph's "Detecting bloat, stale entries, or rising regressions belongs to harness code".
- Combines: core-claim-obscured (INFO on the tool-building aside), marginal-value-redundancy (WARN on the restated consequence clause), detail-overhang (INFO on the offload bullets being recapped twice later).
- Preserve or decide: Keep the point that a code-writing LLM can extend the harness itself, unless the author judges it inessential; it implies the offload boundary moves as the model builds tools, which bears on the Scope revision rule. The criterion-revision paragraph needs some reference to harness-side detection to make its reduction to competences 2 and 3 legible. Shortening that reference is safe, but removing it entirely is not. Whether each offload bullet keeps three or four examples or drops to two is a minor choice. The examples ground the "much of the loop" quantifier, so trimming should keep each category distinguishable.

### 2. State the hypothesis status once, with its revision rule

- Location: the bold "**Working hypothesis.**" lead-in; "our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM"; first Scope bullet.
- Combines: marginal-value-redundancy (WARN on the third "working hypothesis" label and the "not an established impossibility result" clause); cross-cutting tension between "irreducible" and the revision rule.
- Preserve or decide: The author must decide what "irreducible" asserts. It could mean irreducible under current harness techniques, which fits the revision rule, or in principle, which conflicts with it and with the working-hypothesis framing. This is a meaning choice, not a compression edit. Once it is settled, one possible resolution is to keep a single status statement beside the competence introduction, for example "as a working hypothesis, revisable when a sub-task proves reliably offloadable or a new bottleneck appears", and reduce the Scope bullet to the remaining necessary-not-sufficient boundary. Preserve the second Scope bullet, because it states a boundary that appears nowhere else.
