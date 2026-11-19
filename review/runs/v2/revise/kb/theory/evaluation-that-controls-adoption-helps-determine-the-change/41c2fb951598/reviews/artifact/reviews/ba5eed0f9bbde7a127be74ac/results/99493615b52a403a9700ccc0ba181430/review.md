---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'DOUBTFUL — Unstated, universal: whether a human evaluation task is ''required''
    or ''optional assessment'' is fixed by a determinate process specification that
    a reader can consult. — In agent-operated KBs and small teams, the ordinary case
    is an informal or partly written process: a maintainer''s weekly look at results
    is expected by convention but written nowhere, or is written in a stale document
    nobody follows. The note tests both cases against ''its specification'' and ''the
    process specification'', and the Scope section treats unwritten habit only for
    waits (''A habitual wait ... even without a written rule''), not for tasks. Under
    an implicit specification, the same weekly review sorts as either a required task
    or an optional study depending on whom you ask, so the note''s central sorting
    cannot be applied. Repair: state in Scope that the task side of the distinction
    presupposes an explicit specification, or say how habitual tasks are classified,
    as the note already does for habitual waits. — LOCAL — prevalence'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — Unstated, universal: required human work splits cleanly into
    an actual wait (execution cannot proceed) and a specified task (execution continues
    while it goes undone). — Conditional escalation fits neither cleanly. An automated
    adoption pipeline that proceeds unattended in the ordinary case but halts on a
    failed check or conflict until a person resolves it waits only on exceptions.
    Whether this pipeline has ''removed the approval wait'' depends on the exception
    rate, which the binary does not ask about. The note''s own example (''rollback
    of harmful changes'') is such a conditional task, but the note files it under
    the specified-task side without discussion. Repair: name conditional waits in
    Scope as waits that occur only on the exception path. — LOCAL — instance'
- scope: passage
  quotes:
  - Calling the whole process automated would conceal an omitted task.
  reason: 'DOUBTFUL — Universal: a whole-process automation claim made while a specified
    human task is undone conceals that task from its reader. — Ordinary usage of ''automated
    deployment'' or ''automated publication'' scopes the word to the execution path.
    Readers do not assume that on-call monitoring or periodic audits were removed,
    so in common practice nothing is concealed. The note concedes this for adoption-only
    claims (''A claim about automated adoption alone need not include monitoring or
    revision''). It does not cite a case where a broader claim actually misled anyone,
    so the concealment risk rests on an assumed reader who extends ''automated'' to
    the whole process. The premise holds if ''whole process'' is read strictly, and
    is idle otherwise. — LOCAL — prevalence'
- scope: passage
  quotes:
  - A specified task can remain undone while execution continues.
  reason: 'HOLDS — Universal possibility claim: a specification can require a task
    that execution does not wait on. — The hunt found no defeater. Required periodic
    access reviews or post-deployment audits are routinely specified, routinely skipped,
    and execution continues regardless. This premise carries most of the note''s weight,
    and it survives.'
- scope: passage
  quotes:
  - The first is a blocking dependency; the second is an unfulfilled requirement
  reason: 'HOLDS — Universal: an undone specified task is a gap against the specification,
    not by itself evidence of failure or degradation. — No counterexample. The note
    explicitly separates spec conformance from usefulness (''Whether a specified task
    is useful or necessary is a separate question''), so a dead-letter requirement
    does not dent it.'
- scope: passage
  quotes:
  - The process depends on human intervention even if the maintainer always approves.
  reason: 'HOLDS — Universal: a blocking approval is a dependency regardless of how
    often it approves. — Follows from the note''s definition of an actual wait, since
    execution cannot proceed until the person acts. A 100% approval rate changes the
    expected outcome, not the dependency. No defeater found.'
- scope: passage
  quotes:
  - A non-binding recommendation still creates a dependency if the agent must wait
    for it.
  reason: 'HOLDS — Universal: dependency is set by whether execution waits, not by
    whether the human output binds. — Consistent with the note''s definition. A hunt
    for a waited-on but non-dependency case (for example a timeout that proceeds without
    input) turns into a bounded wait, which is still a wait until the timeout. No
    defeater found.'
- scope: passage
  quotes:
  - a program can apply human-authored acceptance rules without requiring a new human
    judgment for each change
  reason: 'HOLDS — Possibility claim: human-authored rules applied mechanically do
    not create a per-change human dependency. — CI test suites and lint gates are
    ordinary instances. No defeater found.'
- scope: passage
  quotes:
  - Using an optional study's available findings does not itself require future studies.
  reason: 'HOLDS — Universal: consuming existing assessment findings does not make
    further assessments a condition of revision. — A hunt for a revision procedure
    that consumes study findings and would stall without fresh ones lands on the note''s
    own counter-case (''Making a new human assessment a condition of each revision
    does''). That case is a different specification, not an exception to this premise.'
- scope: passage
  quotes:
  - Retiring an unnecessary review may be justified, but it is a change in requirements,
    not automation of that review.
  reason: 'HOLDS — Universal: retiring a check and automating a check are different
    changes. — Replacing a human review with a narrower automated check is both at
    once, partly automation and partly retirement. The note explicitly allows this
    (''These changes can be combined''), so the mixed case is accounted for and does
    not defeat the distinction.'
outcome: report
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/ba5eed0f9bbde7a127be74ac/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/ba5eed0f9bbde7a127be74ac/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews
launch: 99493615b52a403a9700ccc0ba181430
completed-at: '2026-11-17T13:17:50Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/calls/launches/99493615b52a403a9700ccc0ba181430/outputs/review.md
raw-output-sha256: 8a68b012a3baa89e8954414017d6df2481e0b9af048a1a9024dc79043b4fada1
format: 2
---

# Premise decomposition: Removing approval waits can leave required human evaluation in place

**Register:** claim
**Central commitment (one sentence):** Removing a human approval wait is a different change from automating or retiring a specified human evaluation task. Adoption can therefore run without a person while the process specification still assigns evaluation work to one, and a claim of full automation must say which tasks it preserves and which requirements it retires.

## Premises and counterexamples

The claim is largely conceptual: it draws a distinction and says what an automation claim must report. Its premises fall into three groups.

- **Separability.** A specification can require a task that execution does not wait on, and an undone task is a specification gap rather than evidence of harm. Both premises hold.
- **Classification.** These premises cover how activities sort into wait, specified task or optional assessment: approval as dependency, non-binding waits, mechanical rule application, use of optional findings, and retirement versus automation. Each holds. The note's own qualifications already fence the obvious counter-cases.
- **Applicability.** For the distinction to apply and matter, two unstated conditions must hold. There must be a determinate specification to consult, and the wait/task binary must be exhaustive. It also matters only if automation claims actually conceal undone tasks.

All three applicability premises are dented, and none is defeated. Each dent is local: a Scope qualification rescues the commitment without changing it. No premise failure propagates to the central claim, because the distinction remains valid wherever a specification is explicit and waits are unconditional. The doubts mark where it stops being usable, not where it becomes false.

## For the human

Start with the unstated premise that "required" is fixed by an explicit, consultable specification. The note handles unwritten habitual waits but not unwritten habitual evaluation tasks, and informal processes are the ordinary case in agent-operated KBs.
