---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: DOUBTFUL — (unstated, universal) Every process has a determinate specification
    that fixes which human tasks are required, so each human evaluation can be sorted
    as either a specified requirement or optional assessment — Many agent and KB processes
    have no written specification of after-adoption work. Requirements live in team
    norms, onboarding habits or one maintainer's belief. Take a maintainer who 'usually'
    samples changes on Fridays, with no written rule. Is that an unfulfilled requirement
    when skipped, or an optional study? The note's test ('its specification does not
    require it') cannot sort it. The Scope section admits practice for waits ('A habitual
    wait ... even without a written rule') but gives no matching rule for habitual
    requirements. Implicit requirements are the ordinary case, not a marked exception,
    so the sorting test is unavailable across a common class of processes. The distinction
    survives if the note states how unwritten requirements are identified, or limits
    itself to processes with an explicit specification — LOCAL — prevalence
- scope: passage
  quotes:
  - Adoption continues if the maintainer does nothing, but the specified review goes
    undone. Calling the whole process automated would conceal an omitted task.
  reason: 'DOUBTFUL — (universal) A specified task that goes undone after automation
    is an omitted task, and calling the process automated without naming it conceals
    that omission — Counterexample: a process document still assigns a weekly review
    that has not been done for a year, and that no participant treats as binding.
    Automating adoption then conceals nothing. The specification is stale, and the
    ''omitted task'' exists only on paper. The note treats the written specification
    as authoritative for requirements, even though it uses practice as authoritative
    for waits. A stale specification makes the specification-gap test report a concealment
    that no reader would be misled by. The fix is a qualification that the specification
    is the currently operative one, or that a lapsed requirement is retired in fact
    even if not on paper — LOCAL — instance'
- scope: passage
  quotes:
  - A claim of full automation must say which tasks it preserves and which requirements
    it retires.
  reason: DOUBTFUL — (normative, universal) A claim of full automation leaves its
    reader uninformed about retained human tasks unless it lists them — In domains
    such as deployment pipelines, 'fully automated' is a conventional, marked scope.
    It covers the execution path and conventionally excludes on-call monitoring and
    rollback, which readers in that domain already expect to stay human. There the
    omission is priced into the term, and listing retained tasks adds no information.
    The note partly concedes this ('A claim about automated adoption alone need not
    include monitoring or revision'). The opening 'must' should therefore apply where
    the scope of 'full' is not already fixed by convention, or to claims about the
    wider process only — LOCAL — priced-exception
- scope: passage
  quotes:
  - A specified task can remain undone while execution continues.
  reason: 'HOLDS — (existential) A specified task and a blocking wait can come apart:
    execution can proceed while a required task is not done — The hunt looked for
    specified tasks that are necessarily blocking. Mechanically enforced reviews,
    such as branch protection, are blocking, but the note classifies them as waits,
    not as counterexamples. The existential claim needs only one case of a non-blocking
    specified task, and the note''s weekly-review example supplies a re-derivable
    one'
- scope: passage
  quotes:
  - Calling an activity evaluation does not tell us whether execution waits for it
    or the specification requires it.
  reason: HOLDS — (universal) The activity of examining results and forming a verdict
    does not fix its process role; role is set by blocking and requirement status
    — No defeater found. The same review can be gating, scheduled-required or optional,
    as the paired cases show. The non-binding-but-awaited recommendation case confirms
    that role follows blocking, not label or authority
- scope: passage
  quotes:
  - Retiring an unnecessary review may be justified, but it is a change in requirements,
    not automation of that review.
  reason: HOLDS — (universal) Retiring a requirement and automating the task that
    meets it are distinct changes — The hunt considered partial replacement, where
    an automated check covers part of what a human review covered. The note already
    says 'These changes can be combined', so a mixed case decomposes into automation
    of one part and retirement of the remainder. It does not mis-sort
- scope: passage
  quotes:
  - Repeated acceptance does not settle that choice
  reason: HOLDS — (universal, negative) A record of repeated human approvals does
    not by itself decide whether the check should remain human, be automated or be
    retired — A record that included seeded defects the approver caught or missed
    would bear on the choice. That evidence goes beyond acceptance, so the premise
    holds as stated. Its support is delegated to the linked note
- scope: passage
  quotes:
  - a program can apply human-authored acceptance rules without requiring a new human
    judgment for each change.
  reason: HOLDS — (existential) Human authorship of acceptance criteria does not make
    each application a human dependency — The hunt found no defeater. Rule authorship
    is a one-time human contribution, and each per-change application by a program
    needs no person. The case where rules must be re-authored for each change would
    make authorship a dependency, and the note's framing already sorts it as one
- scope: passage
  quotes:
  - Anticipated assessment can shape proposals without creating a human stop.
  reason: HOLDS — (existential) Human influence through anticipated review is not
    a blocking dependency — The hunt found no defeater. An agent that tunes proposals
    to anticipated scrutiny still proceeds without anyone acting, so no wait exists
outcome: report
description: Retained report review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/29ae6d13c1bafe2db3873144/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/29ae6d13c1bafe2db3873144/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: 84dec3e1b3b045abaa8f37f7fbd2a162
completed-at: '2026-11-18T16:04:22Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/84dec3e1b3b045abaa8f37f7fbd2a162/outputs/review.md
raw-output-sha256: 8ba4546e5b8ad94d1e6e6bb4334c862829154d074943986bdff3eae12d9b9911
format: 2
---

# Premise decomposition: Removing approval waits can leave required human evaluation in place

**Register:** claim
**Central commitment (one sentence):** Removing a human approval wait is a different change from automating or retiring a specified human evaluation task, so an account of automation must state which required human tasks it keeps and which it retires, and optional assessment belongs to neither change.

## Premises and counterexamples

The commitment is a separation claim, and its core is existential. It holds if the two changes can come apart. That core rests on two structural premises: that a blocking wait and a specified task are separable, and that an activity's role comes from blocking and requirement status rather than from its being "evaluation". Both survived the hunt.

The weaker premises are the ones the note uses to make the distinction operational. The note sorts each human evaluation as a wait, a requirement or optional, and that sorting needs some authority that says what is required. The note silently treats the process specification as that authority. The specification is a determinate object when it is written and current. It is not determinate when requirements are unwritten, which is common, or written but lapsed. The Scope section already treats waits by practice ("habitual wait ... even without a written rule") but treats requirements by specification only. That asymmetry is where both specification-related doubts arise. Neither reaches the central commitment. The separation still holds wherever requirements are determinate. The repair is a scope qualification, or a rule for identifying unwritten or lapsed requirements.

The normative "must" in the opening paragraph depends on a third premise: that omitting retained tasks leaves readers uninformed. Domains where "fully automated" has a conventional, bounded scope dent that premise. The note's later concession, that adoption-only claims need not include monitoring, partly answers it. The opening sentence does not carry that concession.

The remaining premises cover distinctness of retirement and automation, the insufficiency of approval records, rule authorship and anticipatory influence. They held under a hunt and are recorded so that the boundary of what was tested is visible.

## For the human

Look first at the unstated premise that a determinate process specification fixes which human tasks are required. The Scope section should say how unwritten or lapsed requirements are identified, as it already does for habitual waits.
