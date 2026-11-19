---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The first is a blocking dependency; the second is an unfulfilled requirement, not by itself evidence that the system would fail or degrade without the task."
      - "Calling the whole process automated would conceal an omitted task."
    reason: "The note concedes that an unfulfilled requirement carries no consequence for execution or outcomes, so the only thing separating a 'required' non-blocking task from 'optional assessment' is what a specification says. The note never states what makes a specification authoritative: who may change it, whether the automated process itself may revise it, or how stale text differs from a live requirement. Without that condition, an operational opponent can read the required/optional split as wording in a document. Add the condition under which a specified task counts as a requirement. For example, an owner is accountable for it, or a change to the specification is itself a reviewed act. Then show that the 'conceal an omitted task' charge holds only under that condition."
  - scope: passage
    quotes:
      - "A habitual wait for human input can block automation even without a written rule."
      - "Optional assessment creates neither when the process can proceed without it and its specification does not require it."
    reason: "The note counts unwritten waits as dependencies but recognises requirements only when a specification assigns them. In agent-operated systems where much of the process is unwritten, this asymmetry decides most cases. A maintainer's habitual weekly check that nothing blocks on and nothing writes down is classed as optional assessment, even if everyone relies on it. Either state that unwritten but relied-on tasks are deliberately out of scope, or say how they are classified."
  - scope: passage
    quotes:
      - "Removing approval waits can leave required human evaluation in place"
    reason: "The title uses 'required' in the specification sense only; the body explicitly denies that this implies necessity. A reader who sees only the title, as in an index, will likely read 'required' as 'needed for the system to work', which is the claim the note disclaims. Qualify the title or the description so the specification sense is visible without reading the body."
outcome: report
attack-outcome: partially lands
---

# Critique: Removing approval waits can leave required human evaluation in place

**Note:** kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
**Central commitment:** Removing a human approval wait differs from removing a specified human evaluation task, so a claim of full automation must say which specified tasks it preserves and which requirements it retires, separately from whether those tasks are useful.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is an operational functionalist, as in SRE or workflow-automation practice, where "the purpose of a system is what it does." The opponent argues that the note's three-way split (blocking dependency, unfulfilled requirement, optional assessment) is really a two-way split that the system actually exhibits: what execution waits on, and what it does not. Everything else is documentation.

The argument uses the note's own concessions. The note says an unfulfilled requirement is "not by itself evidence that the system would fail or degrade without the task", and that its example "establishes a gap against the specification, not that skipping review causes harm." So the difference between a "required" weekly review and an "optional study" lies in nothing the process does or produces. It lies only in whether some text assigns the task. In an agent-operated KB, specifications are often informal, stale, or editable by the same automated process whose automation is being described. In that setting, "required" costs nothing: an author can create or dissolve the category by editing a sentence. On this view, the demand that automation claims list "which requirements it retires" is a bookkeeping norm dressed up as a distinction in kind. The honest automation claim is just "nothing blocks on a human", plus, separately, an empirical claim about outcomes.

The opponent adds a sharper point. The note treats unwritten habitual waits as real dependencies but treats unwritten relied-on checks as nothing. This shows that the classification follows what is written down, not how the process actually operates.

## How the note engages it

Partially engaged.

The note anticipates the necessity confusion and fences it off well. It separates the requirement from usefulness ("Whether a specified task is useful or necessary is a separate question"). It separates the gap from harm ("not that skipping review causes harm"). It also allows retirement of requirements to be legitimate ("Retiring an unnecessary review may be justified, but it is a change in requirements, not automation of that review"). That answers the weaker objection that the note smuggles in a claim that humans are needed.

The note's reply to the core of the attack is implicit: the distinction serves an honest account of the process ("Calling the whole process automated would conceal an omitted task"). This reply is real. A description that silently drops assigned work misreports the process, even if dropping the work causes no harm. But the reply depends on the specification having some authority beyond its text, and the note never says what that authority is. It does not say who owns the specification, whether the automated process may revise it, or what separates a live requirement from dead letter. The Scope bullet on habitual waits concedes that unwritten practice counts on the dependency side. It does not grant the same to the requirement side, so the asymmetry the opponent points to stands unaddressed.

## Constructive findings

- State the condition under which a specified task counts as a requirement rather than stale text. Candidates include: an accountable owner exists; a change to the specification is itself a deliberate, reviewable act; or the task is part of what the process is claimed to deliver. Then tie "conceal an omitted task" to that condition. This turns the bookkeeping norm into a claim about accurately describing a process someone is accountable for.
- Address specifications that the automated process can itself edit. If an agent can retire a requirement by revising the instruction, say whether that counts as "a change in requirements" (and so must be reported) or as automation. This is the case most relevant to agent-operated KBs.
- Resolve the written/unwritten asymmetry. Either declare unwritten but relied-on checks out of scope, or classify them, for example as implicit requirements that an automation claim must surface.
- Make the title's "required" visibly mean "assigned by the specification", so index readers do not take it as a claim of necessity.

## Secondary objections (optional)

- The demand that automation claims enumerate preserved and retired tasks may already be standard practice in deployment automation, where "fully automated deploys" conventionally coexist with human on-call monitoring. The note partly answers this by allowing claims scoped to adoption alone ("A claim about automated adoption alone need not include monitoring or revision"). The remaining contribution is therefore to make the scope explicit, not to discover the distinction; the note could acknowledge that.
- The file name ("evaluation that controls adoption helps determine the change") and the title ("Removing approval waits can leave required human evaluation in place") assert different claims. The note argues the second. The mismatch will hurt retrieval and linking.
