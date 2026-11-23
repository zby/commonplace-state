---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Evidence may be a later episode that exercises the path again or a specified transition mechanism that survives the transition."
    reason: "A later installation can consume a determination and authorization inherited from the predecessor even after the successor has lost the means to make either decision afresh. Require the episode to trace a new same-class challenge through the functions available from the successor state, including any handoff between actors or components."
  - scope: passage
    quotes:
      - "The first witnesses continuity for one successor; the second supports counterfactual applicability only within the declared model."
    reason: "Identify which installed state a witness establishes as open. A second completed change can demonstrate that the state left by the first change could be revised again. It supplies no continuity evidence for the state left by the second change unless the trace also establishes what remains available there."
outcome: report
attack-outcome: partially lands
---

# Critique: A repeatable operative path keeps a redesign class open to revision

**Note:** `kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md`  
**Central commitment:** A redesign class remains open after an operative change if the installed successor retains a complete causal path from evidence to another operative change in that class.  
**Critique mode:** claim  
**Attack outcome:** partially lands

## Strongest case against it

A release engineer would object that a successful second change can show that the predecessor left enough work queued to finish a rollout while concealing that the first transition disabled the route for new redesigns. Consider a change to verification machinery staged in two releases. Under the original verifier, failure evidence motivates both changes and reviewers approve both patches. The first release installs a verifier that checks submissions but stops retaining the failure information required to develop any fresh verifier patch. The second patch still passes through the familiar merge and deployment workflow, changes the verifier again, and affects later validation. The trace could include tickets, review records, two installed versions, and behavioral dependence on each. Even so, the second release used a decision the predecessor had already made. It never tested whether a new failure could carry a challenge to the first successor through determination and admission.

The same problem applies prospectively. A surviving issue tracker, editable verifier, and merge gate can each still serve a purpose while their composition is broken. If the gate requires the failure evidence that the installed verifier no longer produces, availability of the individual functions gives a false positive unless the reviewer checks that they can act on the same fresh challenge under the successor's rules. This matters for deciding where to intervene. In this example the missing repair is the evidence handoff. More edit permissions or another delivery of an approved patch leaves that break in place.

## How the note engages it

**Partially engaged.** The operational test calls for the causal functions to remain applicable to the successor. Its reject-all admission example shows that an addressable artifact cannot compensate for a dead gate. The discussion of rotating authority also requires the successor to retain or install an admissible route. Read strictly, those conditions exclude the staged rollout as a witness of continuity. The central conditional holds under that reading.

The remaining gap is in applying the test to a trace. The note says a later episode can exercise the path again and distinguishes this from evidence that an installed artifact was used or stayed editable. It does not say how to tell a new determination and admission under the successor's conditions from the completion of a decision already made under the predecessor. The HyperAgents discussion recognizes that replay and editing in selected lineages leave some continuity questions open. The linked inventory likewise distinguishes later modification of selected executable descendants from continuity of the revision path. The missing step is a rule for identifying which successor state and which causal functions the later episode actually tests.

## Constructive findings

- For a later-episode witness, name the installed state under test and trace a fresh same-class challenge through the remaining route. The evidence may predate that state. What matters is whether it can still inform a new determination and admission after the transition, with installation and downstream use following from those decisions.
- For prospective support, check the handoffs under the installed state's rules. Name the evidence the determination process can consume, the condition that can admit its result, and the route that can install and use an admitted change. State which successor the argument covers. A completed second transition witnesses reachability from its starting state.
