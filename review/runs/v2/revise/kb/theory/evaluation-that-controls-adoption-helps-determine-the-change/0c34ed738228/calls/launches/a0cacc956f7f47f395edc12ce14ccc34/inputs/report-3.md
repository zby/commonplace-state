---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/premise-decomposition-gate.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
criterion: kb/instructions/premise-decomposition-gate.md
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 16494152dcda4f12bcced89b2e58358e
completed-at: '2026-11-17T07:23:29Z'
findings:
- scope: passage
  quotes:
  - A human approval required for adoption is part of the process that selected the
    revision.
  reason: 'DOUBTFUL — Premise (universal, no stated mode): a judgment that formally
    controls adoption thereby helps determine which revision results. — Counterexample:
    a rubber-stamp gate whose approver approves every proposal (the routine ''LGTM''
    review). The approval is required and controls entry, but the resulting system
    does not depend counterfactually on it; the same revision would have entered use
    anyway. Control in the gating sense does not by itself supply a selection contribution.
    The case is checkable but the note does not establish how common it is, so it
    dents rather than defeats. Repair by qualifying the gate condition: the verdict
    could have gone otherwise, or the proposer selected in anticipation of it. — LOCAL
    — instance'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — Unstated premise (universal): selection contributions are located
    in per-change adoption judgments, so the approval-before versus assessment-after
    partition covers the evaluator roles that matter for explaining an improvement.
    — Counterexample from the note''s own second case: the agent adopts the instruction
    ''under its existing rules''. Whoever authored those standing rules, such as test
    thresholds or acceptance criteria, helped select the instruction without making
    any judgment about this change. An account that inspects only per-change judgments,
    as the note recommends, would miss that contribution. The Scope bullet about ''other
    influence'' concedes that a later evaluator can have other influence, but it does
    not name rule authorship as a selection role. The commitment survives if the note
    adds standing adoption criteria as a third form of control. — LOCAL — instance'
- scope: passage
  quotes:
  - Whether approval was required for that adoption is a fact about the process.
  reason: 'DOUBTFUL — Premise (universal): whether approval was required is a determinate
    process fact that redescription cannot change. — Counterexample: a de jure rule
    requires approval, but agents routinely adopt first and seek sign-off afterward.
    Alternatively, a soft norm says agents usually wait, but nothing prevents them
    from proceeding. Whether approval was ''required'' then depends on whether the
    account reads the formal rule or the counterfactual practice. That choice is the
    kind of descriptive decision the note says cannot change the role. The premise
    holds once ''required'' is fixed to mean the counterfactual gating condition,
    not the stated rule. — LOCAL — instance'
- scope: passage
  quotes:
  - The later assessment could still cause a future revision or a rollback. That would
    give it a causal role in a different transition.
  reason: 'HOLDS — Premise (universal): adoption is relative to a named transition,
    so a post-adoption assessment that triggers a rollback or wider rollout acts as
    a gate for a different transition, not for the one already made. — Hunted with
    staged and canary rollouts, where a metric check after partial deployment decides
    full deployment. The linked operative-change definition counts a partial or later-rolled-back
    change as operative while it holds. The canary check is therefore assessment-after
    for the partial transition and approval-before for the full one. The note''s requirement
    to name the change and the decision sorts the case correctly.'
- scope: passage
  quotes:
  - An evaluator who only assesses an already-adopted change does not, through that
    assessment alone, determine its adoption.
  reason: 'HOLDS — Premise (universal): an assessment made after adoption does not
    determine that adoption. — Hunted with anticipated evaluation, where a proposer
    shapes a change to pass a known later assessment. That influence runs through
    the known criterion before adoption, not through the assessment act, and ''through
    that assessment alone'' already excludes it. Temporal order makes the premise
    close to definitional, and no counterexample survives.'
- scope: passage
  quotes:
  - The difference is what the judgment controls, not whether a person or a program
    makes it.
  reason: 'HOLDS — Premise (universal): the role of a judgment does not depend on
    whether a human or a program makes it. — Hunted with accountability and authority
    differences between human and automated gates. Those differences affect who answers
    for the outcome, not whether the judgment gates entry. An automated CI test gate
    and a maintainer''s approval occupy the same causal position.'
- scope: passage
  quotes:
  - A favorable assessment of a proposal that is never adopted does not establish
    an improvement of the deployed system.
  reason: 'HOLDS — Premise (universal): a proposal that never becomes operative cannot
    improve the deployed system. — This follows from the linked operative-change definition:
    an approved patch that is never merged affects nothing. No counterexample was
    found.'
contract: report
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/c598b957887ad1e56dd8771b/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/c598b957887ad1e56dd8771b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/16494152dcda4f12bcced89b2e58358e/outputs/review.md
raw-output-sha256: 57f8130c954d65f7a361773d0e2a7307dea1fcb9b28435ea073f08ccffbce193
---

# Premise decomposition: Evaluation that controls adoption helps determine the change

**Register:** claim
**Central commitment (one sentence):** A judgment that controls whether a proposed change enters use is part of the process that selects the resulting system, whereas a judgment that only assesses an already-adopted change is not part of that change's selection; which role a judgment plays is a process fact fixed by what it controls, not by who makes it or how the episode is described.

## Premises and counterexamples

The commitment has two halves and one invariance clause, and each consumes different premises.

The positive half ("controls adoption → helps determine the change") rests on treating gating control as a selection contribution. This is the most consequential node. A gate can be required and still make no counterfactual difference, as in a rubber stamp. The note needs a counterfactual or anticipatory qualification to make "control" carry the weight it puts on it.

The negative half ("assessment after adoption does not determine that adoption") is nearly definitional. It rests on individuating transitions, which the note does explicitly. Staged rollouts, rollbacks and anticipated evaluation all sort correctly under the note's own requirement to name the change and the decision. Those premises hold.

The invariance clause ("a different description cannot turn required approval into assessment") rests on "required" being a determinate fact. It becomes one only if the term is read counterfactually, not as the stated rule.

One premise is unstated. The note's motivating use is explaining "whose contributions explain a system's improvement". That use assumes selection lives in per-change judgments. The note's own second case adopts the change under "existing rules", whose authors are selectors the two-role partition does not name.

The approval-does-not-establish-quality and outside-the-learner points are scope concessions, not premises the commitment consumes, so they are not decomposed.

## For the human

Look first at the gate premise: decide whether "controls adoption" means a formal requirement or a verdict that could have gone otherwise, because a rubber-stamp approval satisfies the first and contributes nothing under the second.
