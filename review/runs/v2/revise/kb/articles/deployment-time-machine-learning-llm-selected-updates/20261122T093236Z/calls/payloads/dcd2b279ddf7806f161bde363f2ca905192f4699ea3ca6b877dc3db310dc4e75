---
type: types/review-result.md
format: 2
description: Retained report review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/premise-decomposition-gate.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
criterion: kb/instructions/premise-decomposition-gate.md
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: c55e5f9e91b744d08a201bcbe39fa55c
completed-at: '2026-11-22T09:39:00Z'
findings:
- scope: passage
  quotes:
  - A robust comparison can select changes without anyone choosing one scalar weighting
  reason: DOUBTFUL — Robust comparison (necessary preference over the preference model)
    does the selecting in the cases that matter, so selection happens without anyone
    choosing a weighting. Stated without a mode, so it reads as universal. — The note
    itself says the ordinary case goes the other way. With no stated preferences the
    rule 'leaves most real changes unordered'. 'Honest sets of compatible measures
    leave many trade-offs open.' Open cases are settled as 'a decision with its reasons'.
    The note's own worked case is one of these. Trial adoption may beat permanent
    adoption under every compatible measure. But the choice of trial over leaving
    the file alone is not shown to be robust. A compatible function that weighs diffuse
    context load heavily and the routing fix lightly prefers no change, because the
    line 'takes effect now under either form of adoption'. If open-case decisions
    are the bulk of selections, a decision that orders options a robust comparison
    leaves open picks a region of weightings without naming it. The distinctive mechanism,
    selection licensed by agreement across the set, then carries little of the load.
    'Without a single score' would reduce to 'an LLM decides with reasons'. Rescuing
    the commitment requires showing that reversibility-reshaped alternatives close
    most comparisons, and that is an empirical premise, not a boundary condition.
    — GLOBAL — prevalence
- scope: passage
  quotes:
  - Third, no single scalar metric had to be invented to compare saved misfilings
    against diffuse context load
  reason: DOUBTFUL — The routing-line walkthrough shows a selection made without a
    scalar metric. Stated as something the sequence 'establishes'. — The sequence
    is hypothetical ('Suppose'), so it shows that such a selection can be described,
    not that it occurred. Its selection step is trial versus unchanged, which is a
    comparison the note's own rule leaves open (see the previous finding). That step
    is where a weighting was in effect chosen. The example shows trial beating permanent
    adoption, not trial beating no change. Recast the third point as an illustration
    and say which comparison was robust and which was a bounded decision. — LOCAL
    — instance
- scope: passage
  quotes:
  - derive the preference model from the declared purpose of the work
  reason: 'DOUBTFUL — A fixed-weight LLM can derive the set of compatible value functions
    from a declared purpose. Stated as an empirical bet. — Read as a bet, it is not
    refuted by argument, but its test needs a premise the note never states: a specification
    of the compatible set that is independent of the judge. The robust-improvement
    test asks that behavior ''score higher under every compatible measure of the declared
    work''. If the judge''s own derived set defines ''compatible'', a judge that derives
    a too-narrow set passes its own test. A judge that derives a near-single weighting
    does too. The bet''s falsifiability depends on a separately fixed or audited compatible
    set. — LOCAL — instance'
- scope: passage
  quotes:
  - It is that the model can give reasons that do the same work
  reason: DOUBTFUL — Verbal reasons (which work changed, whose costs count, which
    weighting would reverse the choice) can stand in for computing agreement across
    all value functions in the set. Bet modality. — Necessary preference is a universal
    quantification over the set. A reason can show one reversing weighting exists,
    but naming no reversing weighting does not show none exists. LLM-as-judge studies
    repeatedly report position, verbosity and self-preference biases in pairwise judgments,
    so the stand-in has a documented common failure mode. It is not an isolated one.
    The note's consistency check (cycles) catches only some of these failures. A biased
    but consistent judge passes it. — LOCAL — prevalence
- scope: passage
  quotes:
  - recognize when an existing gate, validator, or review criterion is misleading
    and revise it
  reason: DOUBTFUL — The same LLM judgment can revise its own working criteria soundly
    while the declared objective stays fixed (the double-loop part of the bet). —
    The note's own EURISKO precedent is a concrete instance of the failure this requires
    avoiding. A heuristic 'could gain credit by influencing how credit was awarded'.
    The double-loop system could not catch this, and Lenat had to correct it from
    outside. Here an LLM judge revises the criteria by which its later judgments,
    including its judgments of criterion revisions, are scored. Nothing in the note
    says what stops the analogous capture. If this premise fails, the claim narrows
    to single-loop selection, and the commitment's core survives. — LOCAL — instance
- scope: passage
  quotes:
  - trace later failures to specific edits
  reason: 'DOUBTFUL — The model can assign blame for a later failure to the specific
    retained edit that caused it, which targeted correction needs. Bet modality. —
    The note concedes the ordinary case against it: ''when entries depend on each
    other, a later failure rarely identifies which entry should change''. It also
    flags unfaithful rationales as a hazard. As the store grows, dependence between
    entries becomes the ordinary case. Targeted correction then becomes the exception,
    and correction falls back to whole-change reverts or store-level comparison. Selection
    survives without targeted credit assignment, so this narrows the ''targeted correction''
    part rather than breaking the commitment. — LOCAL — prevalence'
- scope: passage
  quotes:
  - needs a comparison, not a single score
  reason: 'DOUBTFUL — Selection needs only a local comparison among the candidates
    at hand, including no change. A global measure is not needed. Universal. — The
    note concedes that the preference model can widen when ''an objection can introduce
    a criterion nobody had listed''. Under a drifting set, each change in a chain
    can be robustly better than its predecessor under the set in force at its own
    step. The endpoint need not then be better than the start under the later set,
    because pairwise local comparisons do not compose across a changing set. The accretion
    hazard is the same gap seen from another side. Needed boundary condition: periodic
    whole-store comparisons against earlier states under the current model, which
    the note mentions only as a counter to accretion. — LOCAL — instance'
- scope: passage
  quotes:
  - the system sits on the computation side of the Bitter Lesson
  reason: DOUBTFUL — Once an LLM supplies the comparison inside an automated loop,
    the system is on the computation side of the Bitter Lesson. Unqualified. — Sutton's
    dividing line is whether performance keeps improving as computation is added,
    not whether a step is automated. The note leaves exactly that open ('Whether that
    spending pays as the store grows is open'). The preference model is also derived
    from a human-declared purpose. The placement therefore holds only conditionally,
    as the bootstrap condition in the next paragraph already says. State the claim
    as conditional on scaling evidence. — LOCAL — instance
- scope: passage
  quotes:
  - Pre-training by gradient descent works the same way
  reason: 'DOUBTFUL — Gradient training is direct: the evidence determines the update,
    and nothing is proposed or rejected. Universal as stated for gradient training
    in general (the table column ''Direct gradient training''). — Trust-region methods
    such as TRPO compute a gradient-derived step, test it for surrogate improvement
    and a KL bound in a backtracking line search, and shrink or reject it. Large pre-training
    runs have rolled back to checkpoints and skipped data batches after loss spikes.
    Under the note''s own definition these are selection over gradient proposals.
    The contrast survives if it is restricted to plain SGD-style updates. — LOCAL
    — instance'
- scope: passage
  quotes:
  - is equivalent to no set of value functions
  reason: DOUBTFUL — Approving a change and then its reversal on the same evidence
    is consistent with no set of value functions. Universal. — It holds for strict
    necessary preference. But the note says the decision-analysis relation asks only
    for 'at least as good', and under indifference a single value function licenses
    both directions. Under the note's own concession that new criteria can widen the
    set, approving the reversal after a criterion is introduced is also consistent,
    unless 'same evidence' excludes newly raised objections. The cycle test needs
    to say it is checking strict preferences under a fixed set. — LOCAL — instance
- scope: passage
  quotes:
  - replaced it only if it won by a margin of 55%
  reason: HOLDS — The historical precedents are accurately characterized and do the
    contrastive work assigned to them. AlphaGo Zero's evaluator gated replacement
    of the best network at a 55% win rate, and AlphaZero dropped that gate. PRODIGY
    retained control rules under a fixed utility estimate of time saved. The Gödel
    machine admits only proved switches. — A hunt for misstatements found none that
    bear on the argument.
contract: report
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/c55e5f9e91b744d08a201bcbe39fa55c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/a61498a4a5249ac4625a541d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/c55e5f9e91b744d08a201bcbe39fa55c/outputs/review.md
raw-output-sha256: fdd75a24bf356fb16b216a4312c78acd8f465970b6a5f6a29bb6b5a0bea901b7
---

# Premise decomposition: Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score

**Register:** claim
**Central commitment (one sentence):** A deployed system can learn at deployment time by selecting edits to a readable store through a robust comparison across a preference model rather than a single score, and (the empirical bet) a fixed-weight LLM can build that preference model from a declared purpose and make the comparison, including diagnosing and revising its own criteria.

## Premises and counterexamples

The commitment has two layers, and the premises split along them.

The first layer is the paradigm claim. Selection needs only a local comparison, and robust comparison supplies it without a chosen weighting. Its premises are the sufficiency of local comparison, robust comparison doing the selecting, the worked example's demonstration, the contrast with direct gradient training, and the historical precedents. Here the hunt found the deepest problem. The note's own concessions make open comparisons the ordinary case, and its own worked selection (trial versus leaving the file unchanged) is one of them. So whether the "without a single score" mechanism carries the load depends on how often reversibility-reshaped alternatives close a comparison. That is an unargued empirical premise. Everything else in this layer fails locally: the contrasts and the consistency test need scope qualifiers.

The second layer is the bet. A fixed-weight LLM can derive the preference model, stand in for the universal quantification with reasons, assign credit to specific edits, and revise its own criteria. Bets are not refuted by argument, so the hunt targeted what would make the bet testable and what known evidence presses on it. One premise is never stated: the compatible set used to test robust improvement must be fixed independently of the judge, or the test is circular. Both the EURISKO precedent and LLM-judge bias evidence are pressures the note cites or should cite against its own bet.

The Bitter Lesson section is a side argument. Its placement claim is stated more strongly than its own "open" caveat allows, but it does not bear on the central commitment.

## For the human

Look first at whether robust comparison actually decides most selections. The worked example's trial-versus-unchanged choice is not shown to be robust, so the "without a single score" headline may rest on LLM decisions in open cases, not on agreement across the preference model.
