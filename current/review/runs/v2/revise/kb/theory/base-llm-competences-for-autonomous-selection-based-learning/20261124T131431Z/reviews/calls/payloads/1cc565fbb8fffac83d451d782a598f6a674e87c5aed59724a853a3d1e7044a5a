---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM"]
    reason: "THIN — The linked relocation note supports a semantic residue at use time for novel cases. Because an autonomous loop has no other semantic processor, that residue falls on the LLM. Nothing argues for this particular three-way partition, though, or shows that the three exhaust the residue. The note does not explain why interpretation, diagnosis-plus-synthesis and trade-off judgment are the natural cuts, and not, for example, abstraction or refactoring, recognizing relevance, or splitting synthesis from diagnosis. 'Irreducible' also states more than the cited relocation note supports. That note says semantic work can be pre-paid upstream wherever the regularity already exists, so the residue's size depends on how novel the cases are, not on a fixed list."
  - scope: passage
    quotes: ["store-level maintenance and [criterion revision](./definitions/single-loop-and-double-loop-learning.md) do not require a separate model competence"]
    reason: "THIN — The reduction is asserted, not shown. Competence 2 is defined around turning an unanticipated failure and its trace into a diagnosis. 'Spotting semantic conflicts between prose rules' and 'refactoring them into a cleaner abstraction' can happen with no failure present, and they look closer to competence 1, interpreting unformalized text, or to a separate abstraction competence. Proposing a revised check (double-loop) means questioning the criterion itself. The note does not show that competence 3's 'recognize when an existing check is misleading' covers generating the replacement. The claim depends on this joint because it keeps the count at three."
  - scope: passage
    quotes: ["These three competences can fail independently and sit at different capability thresholds. A model may follow clear prose procedures while still misdiagnosing noisy traces or overclaiming certainty on incomplete records."]
    reason: "THIN — The example only dissociates competence 1 from competences 2 and 3 jointly. It shows no case where 2 and 3 come apart. The previous paragraph also routes criterion revision through '2 and 3 applied' together, which suggests they are exercised jointly. Independence is what justifies the bootstrap step that follows ('identify which competence currently binds'), so this support is thinner than that step needs."
  - scope: passage
    quotes: ["Because an LLM that writes code can also build new harness tools for those jobs, the frozen model does not need to keep track of budgets, traces, or regression suites in its head."]
    reason: "THIN — Building correct harness tools for new jobs is itself competence 2's synthesis of 'executable harness code', and maybe competence 1's reading of what the tool should enforce. So the offloading depends on the residual competences. The 'because' establishes that tracking can be moved out of the model's working context. It does not establish that this costs the frozen model nothing, or that tools the model builds will track the right things."
  - scope: passage
    quotes: ["Even within one benchmark and loop, an inadequate base model can block outer-loop learning before the store itself saturates."]
    reason: "THIN — The cited result supports the existence of a base-model floor under one harness-evolution loop. It does not tie that floor to any of the three named competences. It also does not show that the harness had already offloaded everything offloadable, so the weak models might have failed on work the note assigns to harness code. 'Before the store itself saturates' assumes the store had not saturated, and the cited summary does not show this. The note labels the evidence an illustration, but it is the only empirical support offered."
outcome: report
---

# Friction: Harness code may offload much of a selection loop, leaving three base LLM competences

**Central claim (one sentence):** In an autonomous selection-based learning loop over open-ended work, harness code can take over enforcement, evidence capture and store bookkeeping, but three semantic competences remain on the frozen base LLM: interpreting unformalized text into action, diagnosing novel failures and synthesizing candidates, and judging unformalized trade-offs and missing evidence.

## Filter
**Filter:** SURVIVES

The claim commits to one consistent split, with mechanical and structural work in harness code and the semantic residue on the model. One tension is worth noting, though it does not dissolve the claim. The note calls the three competences "irreducible" yet scopes the split as revisable: offloadable sub-tasks move out and new bottlenecks "can add to it". Read as "irreducible relative to current harness capability, count open", the claim holds together. Read literally as a fixed set of three irreducible items, it conflicts with its own Scope section. The necessity claim in Scope ("necessary for operating the loop autonomously") inherits whichever reading is chosen.

## Thinnest joints

The ranking follows how much of the claim each joint carries. The count of three is the claim's distinctive content, so the joint asserting the three-way partition ranks first. The criterion-revision reduction ranks second because it is the only defense against a fourth competence. The independence claim ranks next because the note's practical payoff, the human-assisted bootstrap, depends on it. The tool-building "because" and the empirical illustration rank lower. Each is circular or bounded, but neither carries the partition. The opening move, that harness code can absorb enforcement, replay and bookkeeping, is backed by the linked scheduler–LLM separation note and was not surfaced.

## For the human
Look first at why there are exactly three competences. Without an argument that diagnosis, synthesis, abstraction and trade-off judgment cut where the note says they do, "three" rests on assertion.
