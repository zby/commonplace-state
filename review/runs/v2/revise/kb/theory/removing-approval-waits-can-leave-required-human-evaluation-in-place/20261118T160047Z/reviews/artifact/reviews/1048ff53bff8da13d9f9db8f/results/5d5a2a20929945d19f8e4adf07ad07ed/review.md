---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Adoption may proceed without a person while the process specification still assigns
    monitoring or later revision decisions to one.
  reason: 'The note never says what gives a process specification authority to make
    a task required. It also never says how to tell an in-force requirement from stale
    text once the only enforcing mechanism, the wait, is gone. Without that condition,
    an opponent can call every unenforced specified task an already-retired requirement,
    and the distinction becomes a choice of description. One or two sentences should
    state the condition: for example, the requirement is still endorsed by whoever
    owns the process, or a person is still accountable for doing it.'
- scope: passage
  quotes:
  - A habitual wait for human input can block automation even without a written rule.
    It is an actual wait to remove, not evidence that the evaluation is needed to
    meet a stated requirement.
  reason: The two categories rest on different evidence. Waits are identified from
    practice, so an unwritten habit counts. Requirements are identified only from
    text, so an unwritten expectation does not count and an unenforced written one
    does. The note gives no reason for this split. The opponent uses that silence
    to argue that, judged by practice, an unenforced specified review is not a requirement
    at all. The note should either justify the split or apply the same evidence standard
    to both.
- scope: passage
  quotes:
  - Calling the whole process automated would conceal an omitted task.
  reason: This sentence carries the note's practical claim, but it assumes the weekly
    review is still in force. The worked example needs one sentence on what would
    make the review still in force rather than already abandoned. With that sentence,
    'conceal' would follow from the example instead of being asserted.
- scope: document
  quotes: []
  reason: 'Secondary. The distinction resembles the standard human-in-the-loop versus
    human-on-the-loop (supervisory control) contrast in automation research. The note
    neither cites that contrast nor says what it adds. Its added element appears to
    be the third case: optional assessment that is neither blocking nor required.
    Saying so would make the note''s contribution easier to see.'
outcome: report
attack-outcome: partially lands
description: Retained report review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/critique-note.md
contract: report
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
criterion: kb/instructions/critique-note.md
note-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/1048ff53bff8da13d9f9db8f/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/1048ff53bff8da13d9f9db8f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: 5d5a2a20929945d19f8e4adf07ad07ed
completed-at: '2026-11-18T16:03:53Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/5d5a2a20929945d19f8e4adf07ad07ed/outputs/review.md
raw-output-sha256: 3b6f135817a64a9cdff9267990381ad9bebf3cba3b7bda091de259a5455145f5
format: 2
---

# Critique: Removing approval waits can leave required human evaluation in place

**Note:** kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
**Central commitment:** Removing a blocking human approval wait is a different change from automating or retiring a specified human evaluation task, so a claim of full automation must say which specified tasks remain and which requirements were retired. Both differ from optional assessment, which neither blocks execution nor is required.
**Critique mode:** claim (a distinction claim with a normative consequence for how automation claims are reported)
**Attack outcome:** partially lands

## Strongest case against it

The opponent holds an operational view of controls, which I call "enforced-or-absent." Compliance-as-code practitioners and SRE and policy-as-code engineers hold it: a control exists only if something enforces it. Commonplace's own linked note leans the same way. It treats a state as operative only when later work actually depends on it, as opposed to merely stored text ([a better-factory claim compares operative states](./a-better-factory-claim-compares-operative-states.md)).

The note sorts human evaluation into three cases:

1. **Blocking wait:** execution cannot proceed until a person acts.
2. **Required but non-blocking task:** the specification assigns the task, but execution continues if nobody does it.
3. **Optional assessment:** neither of the above.

On the opponent's view, case 2 is not stable. The approval wait was what enforced the evaluation. After the wait is removed, nothing makes the weekly sample review happen: no gate, no alarm, no escalation. The review continues to exist only as text in a specification. A requirement that nothing enforces and that no execution depends on is a dead letter, not a live requirement. So removing the wait did not "leave required human evaluation in place." It retired the requirement in fact, and the specification is simply out of date. Calling the process "automated" is then accurate about the operative process, and the only error is a stale document.

The note's own Scope section supports this reading. It counts a habitual, unwritten wait as real because practice determines what blocks. Applied to requirements, the same evidence standard makes an unpracticed, unenforced written review not a requirement.

Under this view the note's distinction does not separate two changes. It separates one change (removing the only enforcement) from the paperwork that should record it. The headline turns a documentation lag into a claim about the process.

## How the note engages it

**Partially engaged.**

- The note anticipates part of the objection. It says that "whether a specified task is useful or necessary is a separate question." It says the omitted-review example "establishes a gap against the specification, not that skipping review causes harm." It also says that "retiring an unnecessary review may be justified, but it is a change in requirements, not automation of that review." So the note concedes that retirement is a legitimate outcome and asks only that it be reported as retirement. Its reporting obligation ("must say which tasks it preserves and which requirements it retires") survives the attack. Even the opponent should agree that the change must be reported as retirement or as automation, and the note asks only for that.
- The note does not answer the central move. It never says what makes a specified task *required* once nothing enforces it. Every judgment of "required" depends on "the process specification," whose authority the note assumes.
- The Scope bullet on habitual waits creates the asymmetry the opponent uses. Waits are recognized from practice; requirements are recognized from text. The note gives no reason for the different evidence standards.

So the attack does not defeat the distinction. A wait and an unfulfilled requirement are different kinds of dependency, and the reporting obligation holds. The attack does weaken the title's claim that required human evaluation is *left in place*, and the claim that calling the process automated would *conceal* an omitted task. Both hold only if the specification remains authoritative after its enforcement is removed. The note assumes that condition and never states it.

## Constructive findings

- State the condition under which an unenforced specified task is still required. Candidates: the process owner still endorses the task, a named person remains accountable for it, or missing it would count as a fault under the process's governance. Place the condition next to the "process specification" sentence in the opening paragraph.
- Address the evidence asymmetry in Scope. Either explain why waits are identified from practice and requirements from text, for example because a requirement is a normative commitment rather than a behavior, or apply the same standard to both.
- In the weekly-review example, add one sentence on what keeps the review in force rather than abandoned, so that "conceal an omitted task" follows from the example. Alternatively, weaken it to "would leave unstated whether the review was retired."
- Optionally, say that the reporting obligation holds on either reading. If the requirement is still live, the task is undone. If it was abandoned in fact, the claim must report a retirement. This turns the opponent's view into a sub-case the note already covers.

## Secondary objections (optional)

- **Unacknowledged precedent.** The blocking versus non-blocking contrast closely matches human-in-the-loop versus human-on-the-loop (supervisory control) in automation research. The note's distinct contribution appears to be the third case, optional assessment that is neither a dependency nor a requirement. The note should name that contribution against the familiar contrast.
- **Mixed cases.** A required task enforced only by a deadline or an escalation, such as a missed weekly review that raises an alert, falls between a blocking wait and an unfulfilled requirement. The note's two-way split does not place it. Mentioning such cases would show the split is a spectrum of enforcement strength, not a binary.
