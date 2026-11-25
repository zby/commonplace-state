---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["and explicit dependency links bound how many artifacts can interact"]
    reason: "UNSUPPORTED — The note's own implicit-coupling bullet says prose conventions \"can interact semantically across unrelated tasks without any explicit link in the store.\" Explicit links can bound only declared interactions. They cannot bound the semantic interactions the note names as the obstacle. The note never says how undeclared coupling becomes declared, or how the store detects that a link is missing."
  - scope: passage
    quotes: ["Replaying the failing case with a shortlisted entry withheld or modified verifies causal responsibility directly"]
    reason: "UNSUPPORTED — The noisier-failures bullet says reproduction and bisect-style isolation are noisier than a failing unit test. Replay is a form of reproduction, so the same noise applies. The note also allows a failure to come from a \"combination of edits\"; withholding one entry at a time can miss a cause that needs several entries together. The note never addresses how many repeats, which statistical threshold, or what interaction search would make replay settle causality \"directly.\" The earlier claim that one-by-one ablation \"verifies causality cleanly on small stores\" has the same gap."
  - scope: passage
    quotes: ["over a modular store of hundreds or thousands of artifacts it gives a plausible path to fully automated credit assignment"]
    reason: "THIN — The conclusion rests on the preceding remedies. Two of them (dependency links and replay) do not answer the obstacles the note itself lists. The premise \"modular store\" assumes the store's modularity, which the second open question admits may need human refactoring. \"Plausible path\" hedges, but \"fully automated\" is still stronger than the support: the paragraph shows tools that narrow suspects, not that automation without humans closes the loop."
  - scope: passage
    quotes: ["Because of those three differences, naive workarounds still break down at scale."]
    reason: "THIN — The connective attributes the breakdown to softer traces, implicit coupling and noisy failures. The examples that follow break down for other reasons. Appending exceptions fails through bloat. Exhaustive ablation fails through cost as artifact count grows, and both would also fail in ordinary code. Only the rationale-trusting example rests on one of the three differences, softer traces."
  - scope: passage
    quotes: ["Yet that does not block full automation: large software codebases have no chain rule either, and engineers and coding agents routinely localize faults across hundreds of interdependent modules"]
    reason: "THIN — The analogy carries the turn from \"far less scalable\" to \"does not block full automation,\" but the note then lists three ways a prose store is harder to debug than code. That weakens the analogy. The evidence is also that engineers and coding agents localize faults \"routinely\". That shows assisted or agent-driven debugging happens, not that fully automated credit assignment works without humans across hundreds of modules."
outcome: report
---

# Friction check: credit assignment without a chain rule is a debugging problem

**Central claim (one sentence):** In selection-based learning, credit assignment over a growing, interdependent store has no chain rule. It is therefore a debugging problem. That problem can be automated when the store is made debuggable, though prose artifacts weaken traces, hide coupling and make reproduction noisy.

## Filter

**Filter:** SURVIVES

The note wants four things at once. Credit assignment is far less scalable than backpropagation. It is still fully automatable. A prose store is harder to debug than code in three specific ways. Ordinary debugging remedies still give a plausible path. These properties can coexist because the note scopes the claim to "hundreds or thousands" of artifacts, not billions. It also hedges the conclusion as a "plausible path," not a guarantee. The trade-off is inside the remedy list, where some remedies presuppose the properties the obstacles deny. Explicit links presuppose declared coupling, and replay presupposes clean reproduction. This makes the bridge thin, but the claim does not split into incompatible parts.

## Thinnest joints

The two weakest joints are remedies that the note's own obstacle list undercuts. The note says prose coupling bypasses explicit links, then says explicit links bound interaction. It says reproduction is noisy and failures can come from combinations of edits, then says single-entry replay "verifies" causality "directly." These are rated UNSUPPORTED because the text gives evidence against them. The final "fully automated" conclusion comes next: it inherits both weaknesses and depends on a modular store that, as the open questions admit, may not stay modular without humans. The "Because of those three differences" connective follows. It is a misattributed cause, not a missing argument, so it matters less. The codebase analogy is strongest of the five surfaced joints. It is reasonable as an existence argument for debugging without gradients, but it over-reaches by moving from routine assisted debugging to full automation.

## For the human

Look first at the last paragraph. For each remedy, say which of the three obstacles it answers and how. The dependency-link and replay remedies are where the note needs that concrete account.
