---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Human evaluation remains a dependency when omitting it either prevents that process
    from proceeding in practice or leaves an evaluation task specified by those requirements
    undone.
  reason: THIN — The second disjunct makes a task a dependency because the requirements
    say so. The weekly-review conclusion ('The process including that task is not
    fully automated') and the central claim's 'can still require' then follow by stipulation,
    not from anything about how the process runs. The note does not say why a stated
    task that the process can skip and still continue makes the process less automated,
    as opposed to merely not meeting its requirements. It also does not say what stops
    'required' from meaning just 'written down as required'. The later admission that
    identifying a dependency does not show that the task is useful only partly covers
    this. It does not show why the requirements-relative test is the right test of
    automation.
- scope: passage
  quotes:
  - Using an optional study's available findings does not itself require future studies.
    Making a new human assessment a condition of each revision does.
  reason: THIN — The line between using findings and depending on assessment is asserted,
    not argued. Suppose revisions in practice happen only when a human study supplies
    findings. Then omitting the studies stops revision from proceeding. That meets
    the note's own first disjunct ('prevents that process from proceeding in practice'),
    even with no written condition. The note does not explain why this case stays
    optional rather than becoming a practical dependency of the revision process.
- scope: passage
  quotes:
  - It is an actual wait to remove, not evidence that the evaluation is needed to
    meet a stated requirement.
  reason: THIN — The sentence correctly says a habitual wait is not evidence that
    a requirement exists. But 'to remove' presumes that the wait does no evaluation
    work the process relies on. That conflicts with the note's own warning that routine
    approvals do not show human judgment is dispensable. The note does not establish
    that a habitual wait, unlike a written stop, can be removed without first making
    the 'automated or unnecessary' decision the Required approval case demands.
- scope: passage
  quotes:
  - The process depends on human intervention even if the maintainer always approves.
  reason: HOLDS — The case stipulates that adoption happens only after approval, so
    the process waits on the human whatever the approval rate. The dependency follows
    from the first disjunct of the note's definition. The follow-on normative claim,
    that removal requires deciding whether the check can be automated or is unnecessary,
    rests on the linked note and is not argued here.
- scope: passage
  quotes:
  - Execution continuing without a person establishes only the absence of a blocking
    step.
  reason: HOLDS — Under the two-part definition, continuing without a person rules
    out only the first disjunct (a blocking step). It leaves the second (an undone
    specified task) open. The inference is narrow and matches the definition just
    given.
outcome: report
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/composition-friction-gate.md
contract: report
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/composition-friction-gate.md
note-sha256: c3b814e077eaa68b1c25e9a772e98ac41b6b9bb452044d02fd88b442ed7f747f
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
target-sha256: c3b814e077eaa68b1c25e9a772e98ac41b6b9bb452044d02fd88b442ed7f747f
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/ae66d115124f7648f48344e3/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/ae66d115124f7648f48344e3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews
launch: 9d2c6924c7f846119d88de8b5f175f2d
completed-at: '2026-11-17T07:56:13Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/calls/launches/9d2c6924c7f846119d88de8b5f175f2d/outputs/review.md
raw-output-sha256: 6d1da5b73428b96e6688cfda08e4ecfdeb69436b20a8ded89e6b3488c7d433f1
format: 2
---

# Friction check: Removing approval waits can leave required human evaluation in place

**Central claim (one sentence):** A system can remove approval waits so that adoption runs unattended while human evaluation is still required for monitoring or subsequent revision, so automating adoption does not by itself automate the wider process.

## Filter
**Filter:** SURVIVES

The claim needs two things at once: adoption without a human stop, and a human evaluation that the wider process requires. These can coexist because the note makes "dependency" relative to a named process and its stated requirements. Adoption can be free of human input while a monitoring or revision task, also part of the process, is not. Concretizing the claim does not split it. The cost is that the claim's force depends on how the process and its requirements are drawn (see the first joint).

## Thinnest joints

The definitional sentence ranks first because the main worked example and the central claim's second disjunct both depend on it. It is a stipulation, so the conclusion it supports is only as strong as the choice of a requirements-relative test, and the note does not defend that choice. The findings-versus-assessment line ranks second because the note's own first disjunct (practical blocking) seems to cover the case the note calls optional. The habitual-wait bullet ranks third because "to remove" pulls against the linked claim that routine approvals do not show judgment is dispensable. The last two joints are the note's most direct inferences from its definition and case setups. They hold under skeptical reading.

## For the human

Look first at the definition's second disjunct: decide whether "required" human evaluation should mean "the process specifies it" or "the process cannot work properly without it", because the weekly-review example and the optional-study boundary come out differently depending on which you choose.
