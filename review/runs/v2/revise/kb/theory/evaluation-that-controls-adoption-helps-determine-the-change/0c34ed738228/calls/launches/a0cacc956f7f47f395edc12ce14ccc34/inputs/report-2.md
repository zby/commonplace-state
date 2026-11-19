---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/critique-note.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 58cd0444b639440281ed8cd3ee0a6d63
completed-at: '2026-11-17T07:22:53Z'
findings:
- scope: passage
  quotes:
  - Whether approval was required for that adoption is a fact about the process.
  reason: 'The note treats formal position in the process (approval required before
    adoption) as sufficient for a causal contribution to selection. On a difference-making
    account, a required approval that would have passed any candidate the agent proposed
    selects nothing: the agent and its test results did the selecting. The note should
    either add the condition that the judgment was sensitive to differences between
    candidates (it could have rejected this one, or the proposer filtered against
    it), or restate the claim as one about adoption authority rather than about helping
    determine which system results.'
- scope: passage
  quotes:
  - The later assessment could still cause a future revision or a rollback. That would
    give it a causal role in a different transition.
  reason: The linked better-factory note allows the successor to be the operative
    state at a named measurement boundary, after a period of development. Under that
    declaration, a post-adoption assessment with keep-or-rollback authority decides
    which state exists at the boundary, so it is selection for the transition being
    examined, not a different one. The note should say that which transition is examined
    (entry into use versus the state at a measurement boundary) is part of the declared
    comparison, fixed before the judgments it attributes, and that post-adoption assessment
    with rollback authority counts as selection under a boundary-defined successor.
- scope: passage
  quotes:
  - An evaluator who only assesses an already-adopted change does not, through that
    assessment alone, determine its adoption.
  reason: 'The phrase ''through that assessment alone'' is what protects the claim
    against anticipation effects: a proposer that writes or chooses changes to survive
    a known later assessment is shaped by that assessor before adoption. The Scope
    bullet about ''other influence'' gestures at this, but it does not name the mechanism.
    Naming anticipation as a separate path, and saying it is excluded from the judgment''s
    role rather than from its causal effect, would stop a reader from using the distinction
    to deny an evaluator''s selective pressure.'
contract: report
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/83434d330579b4e90c502b52/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/83434d330579b4e90c502b52/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/58cd0444b639440281ed8cd3ee0a6d63/outputs/review.md
raw-output-sha256: eff0c1e81eb4443083e653cefeb772548a993e0fd33f8f39b08736217bdea051
attack-outcome: partially lands
---

# Critique: Evaluation that controls adoption helps determine the change

**Note:** kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
**Central commitment:** An evaluator's judgment contributes to selecting a system revision exactly when the judgment controls whether the change enters use; assessment after adoption does not make that contribution, and this role is fixed by the process, not by how the episode is described.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent holds an interventionist, difference-making view of causation, as in Woodward's account or the counterfactual tradition. On that view, a judgment helps determine which system results when changing the judgment would have changed the resulting system. The note's criterion is different. It uses process position: whether the judgment's approval was required and whether it came before or after entry into use. The opponent argues that process position and difference-making come apart in both directions.

1. **Required but idle.** Suppose a maintainer must approve every proposed instruction but in practice approves whatever passes the agent's own tests. The approval is required, so the note says the maintainer "helps select the instruction that enters use". Counterfactually, nothing would change if the maintainer were replaced by an automatic pass. The note also says "Whether approval was required for that adoption is a fact about the process". The opponent answers that it is the wrong fact. A formal gate is a place where selection could happen. It does not show that selection happened.

2. **After adoption but selective.** Suppose the agent adopts instructions under its own rules, and a maintainer reviews them a week later and rolls back the ones judged unhelpful. If the improvement claim compares the predecessor with the operative state at a measurement boundary, the maintainer's judgments decide which instructions are in that state. The linked better-factory note explicitly allows this form: "the successor can instead be the operative state at a named measurement boundary". So does the operative-change definition: "a change later rolled back was operative while it held". The note calls rollback "a causal role in a different transition". The opponent says this classification depends on choosing to examine entry into use rather than the state at the boundary. That choice is descriptive, which is the kind of choice the note says cannot change the attribution.

3. **Anticipation.** A proposer that knows a later assessment will happen can write changes to survive it. The later assessor then shapes which changes are proposed and adopted without making any judgment before adoption.

Together, these cases say that the before/after distinction tracks formal authority and not causal contribution to selection. Those are the two things the note says it separates.

## How the note engages it

**Partially engaged.**

- On anticipation, the note hedges in its opening: "through that assessment alone". Its Scope section also says the distinction "does not establish that a later evaluator had no other influence on the system." This answers objection 3 well enough, because the claim is about the role of one judgment, not about the evaluator's total effect. The mechanism, however, is not named.
- On rollback, the note concedes that later assessment can cause a rollback and assigns it to "a different transition". It also requires that "The account must name the change and the decision being examined." This is the right lever. However, the note does not say that the choice of transition is part of the declared comparison, or that under a boundary-defined successor (which its parent note allows) keep-or-rollback judgment is selection for the very transition being examined. As written, the worked "Assessment after adoption" case suggests that later assessment never selects for the improvement claim. That holds only when the examined transition is entry into use.
- On required-but-idle approval, the note does not engage. The Scope bullet "Approval does not establish quality" is about whether the selected revision is good, not whether the approval did any selecting. The claim "the difference is what the judgment controls" equates control with the authority to block, without asking whether that authority was exercised in any way sensitive to the candidate.

The note's core point survives: a judgment that comes after a change is in use cannot have been what let that change in, and relabelling an episode cannot erase a judgment that was required. The objection succeeds against the stronger reading. The note's verbs ("helps determine which system results", "helps select") claim causal contribution, and it supports them only with formal process position.

## Constructive findings

- Make the causal claim conditional on sensitivity. A required approval helps select a revision when the judgment could have rejected that candidate, or when the proposer filtered candidates against it. Otherwise, call it adoption authority and stop there. An unexercised gate is still worth recording, because it shows where selection could be audited, but it is not evidence of a selective contribution.
- Tie the "different transition" move to the declared comparison. State that which transition is examined, whether entry into use or the operative state at a measurement boundary, is fixed when the comparison is declared, as the parent note requires for its other parameters. Under a boundary-defined successor, a post-adoption assessment with rollback authority counts as selection. This keeps the note's anti-redescription principle: what is fixed in advance is the transition, and redescription afterwards cannot move the judgment.
- Name anticipation as a separate path. Say that a later assessor's influence on what is proposed is real causal influence, and that it is outside this distinction because the distinction classifies a judgment's role, not an evaluator's total effect.

## Secondary objections (optional)

- The worked "Assessment after adoption" case puts the selective work into "its existing rules". Those rules were themselves adopted, possibly with the same maintainer's approval. The note could say that an earlier adoption judgment over the adoption rule is a selection contribution one level up. Otherwise, a reader may conclude that the maintainer had no role in selection at all.
- The open question about external adoption judgments outside the learner boundary overlaps with the Scope bullet that already requires such a judgment to "be acknowledged as a contribution". The open part is narrower than stated: how to report the judgment, not whether to report it.
