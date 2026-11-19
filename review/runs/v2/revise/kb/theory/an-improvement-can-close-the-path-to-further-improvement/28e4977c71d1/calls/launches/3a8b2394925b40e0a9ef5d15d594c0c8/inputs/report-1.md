---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
  against kb/instructions/composition-friction-gate.md
note: kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
note-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
criterion: kb/instructions/composition-friction-gate.md
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews
launch: 1126659b4d0c4d6bae391b2c1dff2c92
completed-at: '2026-11-17T07:24:41Z'
findings:
- scope: passage
  quotes:
  - A gain can consume the mechanism that produced it
  reason: 'THIN — The heading claims a causal coupling: the gain consumes the mechanism.
    The example under it shows only that the two co-occur. A faster configuration
    installs and the revision workflow disappears, but the note never says that removing
    the workflow produces the speed gain. It also never explains why a selection process
    scoring speed would favour a configuration that removes the selector. The co-occurrence
    supports the opening''s compatibility claim. It does not establish ''consume'',
    which would require the removal to be part of what makes the successor score better.'
- scope: passage
  quotes:
  - the ability to revise the system's improvement machinery
  reason: 'THIN — The example''s lost capability is first-order: testing and installing
    another instruction change. This sentence puts a second-order capability in the
    checked scope: revising the improvement machinery itself. Including the second
    does not obviously cover losing the first, and the reverse also fails. The joint
    linking the example to the non-regression remedy depends on these being the same
    capability, and the note does not reconcile them.'
- scope: passage
  quotes:
  - fails the requirement even if its production performance improves
  reason: THIN — The note infers that a successor fails non-regression whenever the
    revision capability is in the checked scope. That follows only if the check actually
    exercises the capability. For example, the check could carry a probe revision
    through proposal, adoption, installation and use in the successor. Putting a capability
    in scope does not establish that the check can detect its absence. The description's
    word 'prevents' depends on that detection, which the note leaves to the linked
    note on repeatable operative paths without stating it as a condition.
- scope: passage
  quotes:
  - Merely declaring non-regression on ordinary production tasks does not include
    it.
  reason: HOLDS — The example separates the production task set from the revision
    workflow, so a production-only check cannot observe the workflow's loss. The joint
    would weaken only if the revision workflow were itself one of the declared tasks,
    and the note's framing excludes that case.
- scope: passage
  quotes:
  - 'There is no contradiction: the comparison checked task performance, while the
    change removed a different capability.'
  reason: HOLDS — Under the stated example, the speed comparison and the removed workflow
    concern disjoint capabilities. A gain on one is therefore consistent with a loss
    on the other. The joint holds without further support.
contract: report
target-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/28ae9a9ffc5a434383a9cc6e/inputs/target/kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/28ae9a9ffc5a434383a9cc6e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/calls/launches/1126659b4d0c4d6bae391b2c1dff2c92/outputs/review.md
raw-output-sha256: 69d11bc95bd7c4df0e8e3c2ec4b94610650a008c28e74043b6d8984fe0f6cf36
---

# Friction check: An improvement can close the path to further improvement

**Central claim (one sentence):** A successor can improve declared production performance while disabling the system's route for selecting and installing later revisions, and non-regression prevents this only when that revision capability is in the checked scope.

## Filter
**Filter:** SURVIVES

The claim commits to two properties that coexist: a real production gain and a real loss of revision capability. Nothing in the gain requires keeping the capability, and nothing in the loss requires giving up the gain. The conditional remedy, scoping non-regression to the capability, does not contradict either property. The Scope section consistently bounds the claim to declared system boundaries and to the absence of another applicable path.

## Thinnest joints

The two thinnest joints come at the main transitions. The first is the move from the example to the section heading's causal language. The second is the move from the example to the non-regression remedy, where the capability placed in scope differs from the capability the example lost. The third joint is the remedy's implied sufficiency: scoping the capability is treated as if it ensured detection, but the check's means of exercising a dispositional capability is never stated. The two `HOLDS` joints are the note's local inferences about disjoint capabilities. They hold under the example as stated and rank last.

## For the human
Look first at whether the checked-scope sentence should name the first-order capability the example loses, and whether "prevents" should be conditioned on a check that exercises the revision path.
