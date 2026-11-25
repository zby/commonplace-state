---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["over a modular store of hundreds or thousands of artifacts it gives a plausible path to fully automated credit assignment"]
    reason: "UNSUPPORTED — the conclusion rests on remedies that the note's own three obstacles partly defeat: load traces are admitted not to show which sentence steered a decision, explicit links do not capture the implicit coupling it names, and replay is weakened by the noisy, diffuse failures it describes. 'Modular' is assumed rather than earned. The second Open Question asks whether an autonomous loop can keep the store modular and replayable without human refactoring, which is the precondition for 'fully automated'. The paragraph does not show that the remedies cover the obstacles; it only lists them next to each other."
  - scope: passage
    quotes: ["and explicit dependency links bound how many artifacts can interact"]
    reason: "UNSUPPORTED — the 'Implicit coupling' bullet says prose conventions interact semantically 'without any explicit link in the store'. Explicit links therefore bound only declared interactions, not the undeclared ones the note identifies as the distinctive difficulty. The note needs a mechanism that turns implicit coupling into declared coupling, or that prevents it, before links can bound anything."
  - scope: passage
    quotes: ["Replaying the failing case with a shortlisted entry withheld or modified verifies causal responsibility directly"]
    reason: "THIN — 'directly' ignores two conditions the note itself raises. Failures may be noisy and diffuse, so one replay may not reproduce them. A failure may come from a 'combination of edits', and withholding one entry does not reveal interaction effects. Verification needs repeated or statistical replay and some way to test combinations, which brings back the ablation cost the note has just called prohibitive."
  - scope: passage
    quotes: ["Yet that does not block full automation: large software codebases have no chain rule either"]
    reason: "THIN — the analogy shows that chain-rule-free fault localization is practicable, mostly with humans in the loop. It does not show that it can be fully automated. 'Engineers and coding agents routinely localize faults' does not establish that agents do this unaided at the scale in question. The next paragraph also argues that prose stores lack the very properties that make codebase debugging work, which weakens the analogy that this sentence relies on."
  - scope: passage
    quotes: ["Because of those three differences, naive workarounds still break down at scale."]
    reason: "THIN — the 'because' does not connect to its examples. Appending local exceptions fails through bloat and added coupling, which is independent of soft traces or noise. Exhaustive ablation fails through combinatorial cost, which would also apply to deterministic code. Only the faulty-rationale example depends on one of the three differences (softer traces). Most of the breakdown follows from scale, not from the prose-specific properties the connective names."
outcome: report
---

# Friction check: Credit assignment without a chain rule is a debugging problem over an interdependent store

**Central claim (one sentence):** In a selection-based store without a chain rule, credit assignment is a debugging problem: it is less scalable than backpropagation and harder than ordinary software debugging because prose weakens traces, coupling and reproduction, but making the store debuggable can still bring it to full automation.

## Filter
**Filter:** SURVIVES

The note wants three things at once: credit assignment that is far less scalable than gradient learning, harder than code debugging, and still fully automatable. These can coexist. Being less scalable than backpropagation and harder than code does not rule out automation at a bounded store size. The claim makes one consistent commitment. The tension lies in whether the remedies support the automation clause, not in the claim's form.

## Thinnest joints

The ranking follows how much of the note's own diagnosis each joint must overcome. The final "fully automated" conclusion is thinnest. It sums the remedies, and each remedy is partly undercut by an obstacle stated earlier, while the open questions leave its precondition unresolved. The explicit-links joint comes next because it directly contradicts the implicit-coupling bullet rather than only straining against it. The replay joint is thin because noise and combination effects, both named in the note, prevent a single withheld-entry replay from verifying causality "directly". The codebase analogy supports practicability but not automation, and the next paragraph weakens it. The "because of those three differences" connective is the least damaging. Its conclusion is plausible, but its stated cause is mostly scale, not the three differences. Stronger joints did not make the list. These include the claim that lacking a chain rule makes credit assignment less scalable, the backward-inverse framing of validation radius, and the conditional claim that addressable theory names premises.

## For the human
Start with how the three obstacles map to the remedies. Implicit coupling has no remedy that works without explicit links, and the "fully automated" conclusion depends on Open Question 2 being answered yes.
