---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/composition-friction-gate.md
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
note-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
criterion: kb/instructions/composition-friction-gate.md
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: 2bd21c1d3db34db2a334293c0fc058c0
completed-at: '2026-11-18T16:03:52Z'
findings:
- scope: passage
  quotes:
  - A habitual wait for human input can block automation even without a written rule.
    It is an actual wait to remove, not evidence that the evaluation is needed to
    meet a stated requirement.
  reason: 'UNSUPPORTED — The note defines a requirement by what the process specification
    assigns, then classifies an unwritten habitual wait as purely a wait "to remove".
    It never argues why the habit could not be an unwritten specification: a tacit
    requirement that the team actually relies on. If it can be, removing the habit
    would retire a requirement, which is the change the note insists must be declared,
    not just removing a wait. The phrase "to remove" also adds a normative conclusion
    that nothing in the note''s definitions supplies. The definitions only say the
    habit is a blocking dependency.'
- scope: passage
  quotes:
  - A claim of full automation must say which tasks it preserves and which requirements
    it retires.
  reason: 'THIN — The obligation rests on the later example: calling the process automated
    "would conceal an omitted task". The note never says what scope "full automation"
    claims. The obligation follows only if "full automation" is read as a claim that
    every specified task is performed without a person. If the claim covers only adoption,
    the note itself says that such a claim "need not include monitoring or revision".
    So the "must" applies only to wider-process claims, and the opening sentence states
    it without that condition.'
- scope: passage
  quotes:
  - Calling the whole process automated would conceal an omitted task.
  reason: THIN — Concealment needs a reader who takes "automated" to mean the review
    is being done somehow. The note does not establish that this is the usual reading,
    as opposed to "proceeds without human waits". The example shows that a specified
    task goes undone. It does not show that the label "automated" asserts the task
    is done. A one-line statement of what "the whole process automated" commits to
    would make the inference go through.
- scope: passage
  quotes:
  - 'This is an optional study: neither adoption nor a required monitoring or revision
    task depends on it.'
  reason: 'HOLDS — The hypothetical sets these conditions itself: the agent adopts
    under its existing rules, and no specification is mentioned that requires the
    later examination. The classification follows from the definitions in the second
    paragraph. Its only weakness is that the absence of a requiring specification
    is assumed rather than shown, which is acceptable for a constructed case.'
- scope: passage
  quotes:
  - Repeated acceptance does not settle that choice
  reason: 'HOLDS — The note relies on the linked note for this. That note supplies
    the mechanism: routine approvals may never have met the exceptional case that
    needs judgment, or may have been granted without checking. The joint holds within
    the scope the note uses it for: deciding whether the check is moved, automated
    or retired.'
contract: report
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/7f10791dc4cdd3fd059fc438/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/7f10791dc4cdd3fd059fc438/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/2bd21c1d3db34db2a334293c0fc058c0/outputs/review.md
raw-output-sha256: 7575503ea90f11bd409dd09e8e7336cc8157f7f165e583c44ad7c1457b39eaaf
---

# Friction check: Removing approval waits can leave required human evaluation in place

**Central claim (one sentence):** Removing a blocking human approval wait is a different change from automating or retiring a human evaluation task that the process specification requires. So a claim about automating the wider process must state which human tasks remain and which requirements were retired.

## Filter
**Filter:** SURVIVES

The claim has three parts: a blocking dependency (a wait), an unfulfilled specified requirement (a task), and optional assessment (neither). These categories can coexist, and the note keeps them apart consistently. Removing an approval wait can turn the check into later human work, an automated check, or a retirement. Each of these is a single, coherent outcome. The note never asks one change to be both automation and retirement of the same review. It explicitly separates the two ("a change in requirements, not automation of that review"). The one place where the categories strain is the unwritten habitual wait, covered under the joints below. That strain is a gap in the definitions, not a contradiction that dissolves the claim.

## Thinnest joints

Most of the note's inferences are definitional. Once "wait" means execution blocks and "requirement" means the specification assigns the task, the case classifications and the "conversely" contrasts follow directly. Those joints are strong.

The weak points are where the note moves from its definitions to a normative statement or a claim about meaning:

- The habitual-wait bullet ranks thinnest. It applies the specification-based definition of requirement to a case the definition does not cover: an unwritten practice. It then adds "to remove" without argument.
- The two "full automation" joints rank next. They depend on an unstated reading of what "automated" asserts. The note's own scope rule says adoption-only claims are exempt, but the opening sentence does not carry that condition.
- The optional-study classification and the reliance on the linked routine-approvals note hold under the skeptical default. They are listed here because they are the remaining load-bearing inferences, not because they fail.

## For the human
Look first at the habitual-wait bullet. Decide whether an unwritten but relied-on human check counts as a specified requirement. If it does, the note's rule against silently retiring requirements also covers removing habits.
