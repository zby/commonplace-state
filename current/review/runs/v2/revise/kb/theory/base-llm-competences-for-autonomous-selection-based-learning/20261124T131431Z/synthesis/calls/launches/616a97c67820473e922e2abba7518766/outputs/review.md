---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["Because an LLM that writes code can also build new harness tools for those jobs, the frozen model does not need to keep track of budgets, traces, or regression suites in its head."]
    reason: "The offload half of the claim is said up to three times: in the three harness bullets, in this bridge sentence, and again in 'Detecting bloat, stale entries, or rising regressions belongs to harness code'. The recap delays the turn to the three residual competences, which are the claim's distinctive half. A revision could move the one new point (a code-writing LLM can build more harness tools) into the lead-in to the bullets. It could cut the recap so the relocation-not-elimination pivot comes straight after the list. It could also trim each bullet to the examples the later store-maintenance paragraph relies on."
  - scope: document
    quotes: []
    reason: "What makes the working hypothesis testable is spread across four places: the revision rule in the first Scope bullet, the independence and bootstrap sentences, the bounded ceiling evidence, and the first Open Question. Meanwhile the 'working hypothesis' label appears three times. The reader sees repeated hedges, but no single statement of what would move a sub-task out of the LLM column or how to find which competence binds. A revision could state the hypothesis status once. The revision rule and the independent-failure point could then appear together as the note's test conditions, with the ceiling paragraph as the evidence for a floor, so the hedging becomes a stated falsification route."
outcome: report
---

# Simplification synthesis: Harness code may offload much of a selection loop, leaving three base LLM competences

The note is short and its core claim is easy to find. All four checks passed or found local issues, and none found a buried thesis. Two opportunities combine those local findings into changes a reader would notice: shortening the offload half so the residual competences arrive sooner, and turning scattered hedges into one statement of how the hypothesis would be tested or revised. Neither requires choosing between different theses.

## Opportunities

### 1. Say the offload half once and turn sooner to the residual competences

- Location: opening section, from the three harness bullets through "Because an LLM that writes code can also build new harness tools for those jobs, the frozen model does not need to keep track of budgets, traces, or regression suites in its head."; the store-maintenance paragraph's "Detecting bloat, stale entries, or rising regressions belongs to harness code" restates the same items.
- Combines: core-claim-obscured (bridge sentence delays the pivot), marginal-value-redundancy finding 2 (consequence clause restates the bullets), detail-overhang (bullets carry more examples than needed, and two later sentences recap them).
- Preserve or decide: Keep the tool-building point. It is the only new content in the bridge, and it supports "much of the loop's machinery". Detail-overhang notes that the bullets' concreteness grounds the "much" quantifier. Decide how many examples per bullet are needed for that, and which examples the store-maintenance paragraph depends on, so a trim does not orphan its back-reference. One possible lead-in, offered only as an illustration: "Harness code, including tools the LLM itself writes, can take over much of the loop's machinery:".

### 2. Replace repeated hedges with one statement of how the hypothesis is tested

- Location: cross-cutting. It covers the bold "Working hypothesis" lead-in, "our working hypothesis is", the first Scope bullet ("not an established impossibility result" plus its revision rule), the independence paragraph's last sentence ("Separating them lets a human-assisted bootstrap identify which competence currently binds..."), the ceiling paragraph and the first Open Question.
- Combines: marginal-value-redundancy finding 1 (the hypothesis label appears three times, with a defensive contrast clause), branch-bloat (the bootstrap sentence is an undeveloped application), and a cross-cutting observation that the revision rule, independent-failure point and binding-competence question form one testability thread split across three sections.
- Preserve or decide: Keep the revision rule, which is the note's falsification route: offloadable sub-tasks leave the LLM column, and newly found bottlenecks can join it. Also keep the necessary-not-sufficient boundary and the bound on the ceiling evidence ("Even within one benchmark and loop"). The author must decide whether the human-assisted bootstrap is a method this note proposes or an aside. If it is a method, it needs a stated role beside the test conditions. If it is an aside, it can be cut to the independence point or moved to an open question. Branch-bloat left the destination unresolved, and this synthesis does not choose it.
