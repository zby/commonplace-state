---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - What matters is whether the operating process depends on the human activity, not
    whether the activity is called evaluation.
  reason: 'DOUBTFUL — (universal, no stated mode) the boundary criterion ''the operating
    process depends on the human activity'' sorts every human activity cleanly into
    operating dependency or result assessment — sampled audits are a counterexample:
    a maintainer reviews a random 10% of adopted instructions after adoption. No individual
    adoption waits for or relies on its own review, so per episode each review sorts
    as non-blocking assessment. Yet the process as designed relies on the audit regime
    to catch harmful changes, so in aggregate it is an operating dependency. The criterion''s
    unit (per change vs per regime) is unspecified, and the boundary mis-sorts or
    under-determines this case. The monitoring paragraph covers ''must inspect each
    adopted instruction'' but not reliance through sampling — LOCAL (state in Scope
    that reliance is judged at the level of the regime, not the single episode) —
    instance'
- scope: passage
  quotes:
  - the second can observe a process that runs without one
  reason: 'DOUBTFUL — (universal) assessment that only measures an already-adopted
    change leaves a process that still runs without it, so the distinction picks out
    the human stops automation must address — counterexample: in an improvement loop,
    the week-later verdict on whether the instruction helped is the input the next
    proposal or retirement decision consumes. Without it, adoption keeps running but
    the loop''s selection function lapses; the process ''runs'' only in the narrow
    sense of adoption. Whether the non-blocking assessment is a dependency then depends
    on whether the named process is adoption or improvement. The ''Name the process
    being automated'' section gestures at this but only for monitoring and rollback,
    not for assessments that steer future changes — LOCAL (qualify that the sort is
    relative to the named process, and that an assessment non-blocking for adoption
    can be a dependency of the improvement loop) — instance'
- scope: passage
  quotes:
  - A non-binding recommendation still creates a dependency if the agent must wait
    for it.
  reason: 'DOUBTFUL — (universal, unstated in general form) whether a process depends
    on a human activity is fixed by what the process requires, so prescribed structure
    rather than observed behaviour determines the sort — the Scope bullet on written
    requirements vs execution handles only one direction, a required check that is
    bypassed. The converse case is a de facto stop: no rule requires waiting, but
    agents or operators conventionally hold adoption until a maintainer comments,
    so in practice the process does not proceed without the person. ''Must wait''
    does not say whether the obligation is formal or effective, so this case is under-determined.
    Automation that removes only formal stops would leave the effective one in place
    — LOCAL (state which reading of ''must'' the distinction uses, and that effective
    stops count) — instance'
- scope: passage
  quotes:
  - The process depends on human intervention even if the maintainer always approves.
  reason: HOLDS — (universal) a required approval is an operating dependency regardless
    of its approval rate — the hunt considered auto-approve-on-timeout and rubber-stamp
    approval. The first is a different process design with no required stop. In the
    second, a person must still act before adoption proceeds. Neither defeats the
    premise.
- scope: passage
  quotes:
  - a program can apply human-authored acceptance rules without requiring a new human
    judgment for each change
  reason: HOLDS — (possibility claim) human-authored acceptance rules can be applied
    mechanically without per-change human judgment — automated test suites and lint
    rules written by people are standing counterexamples to the opposite view. Rules
    that escalate uncovered cases reintroduce a stop only for those cases, which the
    note's criterion then sorts correctly.
- scope: passage
  quotes:
  - Anticipated assessment can shape proposals without creating a human stop.
  reason: HOLDS — (possibility claim) anticipating a later review can influence a
    proposer without the process waiting for that review — a proposer that optimizes
    for a known post-hoc audit adopts without waiting. No case was found where anticipation
    alone forces a wait.
- scope: passage
  quotes:
  - Moving the check after adoption has not eliminated that dependency.
  reason: HOLDS — (conditional on required post-adoption monitoring and rollback)
    relocating a required human check from before adoption to after it does not remove
    the dependency — the hunt considered a fully automated rollback trigger. That
    removes the human from monitoring, falls outside the stated condition ('a maintainer
    must inspect'), and so does not defeat the premise.
outcome: report
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: 541a682500facea176646d7bdfe6093663673fe51d93f06bb184d3c3d493580e
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
target-sha256: 541a682500facea176646d7bdfe6093663673fe51d93f06bb184d3c3d493580e
target-capture: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/0fc0aba79378758264a07037/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/0fc0aba79378758264a07037/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261117T074216Z
launch: 0c9354f8f28a43869af737b6b0c571fd
completed-at: '2026-11-17T07:44:31Z'
raw-output: kb/reports/state/review/runs/v2/20261117T074216Z/calls/launches/0c9354f8f28a43869af737b6b0c571fd/outputs/review.md
raw-output-sha256: 2d5a9d5a6ba1a80072caa9219021f773ee2425c4857dcf2e7249fa99234b0590
format: 2
---

# Premise decomposition: Evaluation required for adoption is part of the operating process

**Register:** definition
**Central commitment (one sentence):** A human activity belongs to a system's operating process exactly when the process must wait for or rely on it in order to proceed — whatever the activity is called — and assessment that only measures already-adopted changes falls outside it. This cut identifies the human stops that automation must address.

## Premises and counterexamples

The note is a definition: it draws a boundary between operating dependency and result assessment, and it claims the boundary is the right cut for automation decisions. The decomposition therefore tests three kinds of commitment:

- **The criterion sorts cases determinately.** This is the "depends on" test of the first finding.
- **The distinction is not idle for automation.** Non-blocking assessment really leaves a process that runs without it; this is the second finding.
- **Dependency is fixed by the process requirement.** The note never states this premise in general form, but its Scope bullet and its "must wait" wording consume it; this is the third finding.

The remaining findings are the supporting premises the illustrative cases and Scope bullets rest on: the always-approving maintainer, human-authored rules applied by programs, anticipation without a stop, and post-adoption monitoring.

The three doubtful premises share one root. The note's test, whether the process depends on the activity, needs a fixed unit of analysis, and the note leaves three choices of unit open:

- per episode or per regime (the sampled-audit case);
- adoption or the improvement loop (the steering-assessment case);
- formal or effective requirement (the de facto stop).

The "Name the process being automated" section already shows that the author sees the process boundary as a choice. The repair is to make all three choices explicit in Scope. None of the three counterexamples defeats the distinction itself; each shows a case the boundary leaves under-determined until the unit is named. So all three route LOCAL. No premise failure reaches the central commitment.

## For the human

Look first at the "depends on" criterion's unit of analysis. Sampled audits and assessments that steer the next proposal are non-blocking per episode but relied on in aggregate. One Scope bullet saying at what level reliance is judged would close all three doubtful premises.
