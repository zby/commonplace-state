---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Removing that stop requires deciding whether its check can be automated or is
    unnecessary
  reason: THIN — the two options offered are not exhaustive. The check can also be
    moved out of the blocking path and kept as a non-blocking specified task, such
    as post-adoption sample review with rollback. The note's own weekly-review example
    shows this third option. Removing the stop therefore does not force a choice between
    automating the check and declaring it unnecessary, and the note does not say why
    relocation is excluded or how it would be classified.
- scope: passage
  quotes:
  - Calling the whole process automated would conceal an omitted task.
  reason: THIN — concealment follows only if 'automated' means that every specified
    task is performed without a person. The note never states that meaning. Under
    the common reading, a process that runs without waiting for a person, the label
    is accurate and nothing is concealed. The normative opening line, 'A claim of
    full automation must say which tasks it preserves and which requirements it retires',
    relies on this same unstated definition.
- scope: passage
  quotes:
  - Using an optional study's available findings does not itself require future studies.
    Making a new human assessment a condition of each revision does.
  reason: THIN — the line drawn here depends on whether the assessment is a formal
    condition. It leaves unclassified a revision that happens only because an optional
    study found something. That revision would not have occurred without human work,
    yet the note counts it neither as a dependency nor as an unfulfilled requirement.
    The Scope bullet about 'human influence' gestures at this case but does not show
    that counterfactual necessity falls outside 'required human intervention'.
- scope: passage
  quotes:
  - Conversely, a program can apply human-authored acceptance rules without requiring
    a new human judgment for each change.
  reason: 'HOLDS — the sentence is true and relevant, but ''Conversely'' presents
    it as the inverse of the preceding sentence about non-binding recommendations,
    and it is not. It is an independent point: the activity''s label does not settle
    whether a per-change human stop exists. The claim stands on its own; only the
    connective overstates the logical relation.'
- scope: passage
  quotes:
  - The first is a blocking dependency; the second is an unfulfilled requirement,
    not by itself evidence that the system would fail or degrade without the task.
  reason: HOLDS — this follows from the two definitions in the preceding sentences.
    A specification gap shows only a mismatch with the specification, not harm, and
    the note keeps that limit consistently, for example 'This example establishes
    a gap against the specification, not that skipping review causes harm.'
outcome: report
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/composition-friction-gate.md
contract: report
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/composition-friction-gate.md
note-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
target-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/c0c80bced65c66b3055bdb50/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/c0c80bced65c66b3055bdb50/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews
launch: 7f1d0011a71144719462deb32e2ee462
completed-at: '2026-11-17T13:08:56Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/calls/launches/7f1d0011a71144719462deb32e2ee462/outputs/review.md
raw-output-sha256: 4dd8d98d5a7e087efa588db780971701be4659ad31982ca2d353bb59e62f1b6a
format: 2
---

# Friction check: Removing approval waits can leave required human evaluation in place

**Central claim (one sentence):** Removing a human approval wait, which blocks execution, is a different change from automating or retiring a specified human evaluation task, which can go undone without blocking; so a claim of automation must say which specified tasks remain and which requirements were dropped.

## Filter
**Filter:** SURVIVES

The note holds three categories at once: blocking waits, specified but non-blocking tasks, and optional assessment that is neither. Committing to one does not force giving up another. They are separated by two independent axes: whether execution waits and whether the specification requires the task. Habitual unwritten waits fall on the first axis, and the note classifies them consistently. One risk does not dissolve the claim: the axes are relative to a specification the note treats as given. If a reader ties "automated" to the waiting axis only, the normative "must say" weakens. The claim itself stays consistent.

## Thinnest joints

The three THIN joints rank above the HOLDS joints because each leans on something the note does not supply. The first is the thinnest because the note's own later example contradicts the dichotomy it asserts. The required-approval case says removing the stop needs one of two decisions. The weekly-review case then shows a third route: demote the check to a non-blocking specified task. The second joint carries the note's normative weight, the "must say" obligation. It depends on an unstated definition of "automated", which is a gap in terminology, not in logic. The third concerns an edge case at the boundary between "required" and "influential" human work. It matters less to the central claim but is where a reader would most likely misclassify a real process. The two HOLDS joints were the strongest remaining candidates. Under the skeptical default they still hold: one is definitional, and in the other only the connective is wrong.

## For the human
Look first at the required-approval paragraph: decide whether "move the check to post-adoption review" counts as automating it, retiring it, or a third kind of change, and define "automated" to match.
