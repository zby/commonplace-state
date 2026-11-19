---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the second is an unfulfilled requirement, not by itself evidence that the system would fail or degrade without the task"
    reason: "The note's only arbiter of whether a non-blocking human task is 'required' is the written process specification, but it never says what makes that specification authoritative over the running process. An operations-minded opponent holds that a task nothing waits on and whose output nothing consumes has already been retired de facto, so the 'required human evaluation' the title says remains in place may be a dead letter. Add one or two sentences that tie 'required' to something beyond the text: either the task's output is consumed by a later decision (the revision paragraph already points this way), or someone owns the specification and could be held to it. Then say that a specified task with neither is a stale requirement, to be retired explicitly."
  - scope: passage
    quotes:
      - "A claim about the wider process must distinguish tasks performed automatically from tasks no longer required."
    reason: "The disclosure duty is the note's answer to the 'dead specification' objection: if a requirement has lapsed in practice, the claimant must say it was retired. The note does not show that it intends this answer. One sentence would show it: an unenforced requirement does not make an automation claim false, but treating it as automated rather than retired does. That turns the partially landing attack into one the note visibly answers."
  - scope: passage
    quotes:
      - "assigns a maintainer a weekly sample review and rollback of harmful changes"
    reason: "The worked example puts a scheduled task (the weekly review) together with a conditional one (rollback when harm is found). An exception-triggered human task is the commonest form 'monitoring' takes in automated pipelines, and it does not fit cleanly into either the 'wait' category or the 'specified task left undone' category: it is undone only when its trigger fires. Separating the two would show whether the distinction survives the case operators most often call 'human in the loop on exception'."
  - scope: document
    quotes: []
    reason: "The file slug, 'evaluation-that-controls-adoption-helps-determine-the-change', states a different claim (credit or determination of the change) from the title, 'Removing approval waits can leave required human evaluation in place'. The body also explicitly sets aside causal credit ('rather than deciding who deserves causal credit for an improvement'). A reader or linker who goes by the filename will expect the wrong commitment. Relocate the file so its slug matches the title."
outcome: report
attack-outcome: partially lands
---

# Critique: Removing approval waits can leave required human evaluation in place

**Note:** kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
**Central commitment:** Removing a human approval wait (a blocking dependency) is a different change from removing a specified human evaluation task (a requirement that can stay unfulfilled while execution proceeds), so a full-automation claim must say which human tasks it keeps and which requirements it retires.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is an operations or "policy-as-code" practitioner. Their stance is that a process is what executes and what is enforced, not what a document says. On that view, the note's three categories reduce to two: blocking dependencies, and everything else. A specified human task that nothing waits on, and whose output no later step consumes, is not a part of the process that "remains in place". It is a stale document. Unenforced requirements decay: the weekly sample review in the note's own example is exactly the kind of obligation that lapses quietly once adoption no longer stops for it. So once every human wait is removed, "the process is automated" is a true description of the running system. Requiring the claimant to also list "requirements it retires" asks them to account for fictions. It also lets anyone block an automation claim by writing a requirement nobody acts on.

The best form of the argument goes further. The note's test for "required" (assigned by "the process specification") makes the distinction depend on how the system is documented, not on how it behaves. The behavioural property that matters is whether a human output is consumed by a later decision. That property is already captured either by a wait (adoption or revision stops for it) or by nothing at all. If so, the "specified task" category is idle: it adds no information about the system beyond the existence of a sentence in a document.

## How the note engages it

The note **partially engages** the objection, and the engagement is substantial.

- It concedes the behavioural point outright. An unfulfilled specified task is "not by itself evidence that the system would fail or degrade without the task". The example "establishes a gap against the specification, not that skipping review causes harm." The note claims nothing about necessity.
- It already has the answer to the "fictions" charge, though it does not state it as an answer. "Retiring an unnecessary review may be justified, but it is a change in requirements, not automation of that review." The opponent's own position, that the requirement has lapsed de facto, is exactly what the note asks the claimant to say out loud. That is cheap, and it is informative to whoever owns the specification. The disclosure duty does not stop automation; it relabels part of it.
- It partly addresses the consumption criterion in "Name the process being automated". If the next revision requires the maintainer's assessment, that assessment is a dependency of the revision process. That is the opponent's "consumed by a later decision" test, applied to a later process.
- It handles the reverse direction: a habitual wait with no written rule is still a wait to remove.

What the note leaves exposed is the authority of "the specification". It never says why a written assignment that nothing enforces or consumes still counts as "required", and the title asserts that such evaluation "remains in place". Against an opponent for whom specification and operation coincide, that phrase claims more than the note defends. The attack therefore lands against the title's wording and against the unexplained reliance on the specification. It does not land against the core distinction, which survives because the note asks for disclosure, not preservation.

## Constructive findings

- Ground "required" in more than the text. A specified human task counts as required when its output feeds a later decision, or when an owner of the specification would treat its omission as a defect. A specified task with neither is a stale requirement that should be retired explicitly. The note has the materials for this in the revision paragraph.
- State the answer to the dead-specification objection directly. An unenforced requirement does not make an automation claim false. Calling it automated instead of retired does.
- Split the example's scheduled review from its conditional rollback. Exception-triggered human tasks are the commonest real form of monitoring, and they test whether the wait/task distinction covers "human on exception".

## Secondary objections (optional)

- An informed requirements engineer would call the wait-versus-obligation distinction standard, not novel. That affects the note's contribution, not its truth. The note's value lies in applying the distinction to automation claims about agent processes, and it should make that application its emphasis.
- The filename slug describes a different commitment (who determines the change) from the title and body. The body explicitly sets aside causal credit. Linkers who go by the slug will cite the note for the wrong claim.
