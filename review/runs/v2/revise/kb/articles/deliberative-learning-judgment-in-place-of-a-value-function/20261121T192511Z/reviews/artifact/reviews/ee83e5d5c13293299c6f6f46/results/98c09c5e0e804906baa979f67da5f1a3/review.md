---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Three payoffs follow directly from storing what the system retains in readable,
    addressable artifacts.
  - And when a mistake occurs, an addressable store lets later rounds point at the
    faulty line and fix it without wiping out unrelated work.
  reason: 'The three-payoffs paragraph restates three rows of the table directly above
    it (When updates happen: deployment time; Inspectability: direct reading; Credit
    assignment and correction: edit or revert specific entries while keeping the rest).
    The routing-line example and its ''three things'' recap have already made the
    deployment-time and targeted-fix points. What the paragraph adds is two links
    and the phrase ''by other agents at volumes people could not read''. Fold the
    links into the table cells or into one short sentence that introduces the cost
    ledger, and cut the rest.'
  level: warn
- scope: passage
  quotes:
  - Treating the paradigm as already validated would invert the order of proof.
  reason: This is defensive redundancy. The sentence before it already reports no
    completed end-to-end automated run, and the section opens by saying success must
    be judged separately. Readers who know that no run is complete already know not
    to treat the paradigm as validated. Cut the sentence.
  level: warn
- scope: passage
  quotes:
  - The initial human scaffolding must serve as a launchpad that computation comes
    to supply and revise, not a permanent ceiling of hand-crafted rules.
  reason: This closing restatement adds no admission beyond its opening. 'Fits the
    Bitter Lesson only if automated learning outgrows that starting point' already
    says the scaffolding must not remain a permanent ceiling. The launchpad/ceiling
    metaphor repeats that condition without adding a test or a consequence. Cut it,
    or replace it with an observable criterion for having outgrown the bootstrap.
  level: warn
- scope: passage
  quotes:
  - Legible prose can diverge from what actually steers the model's outputs, masking
    the real cause of gains or losses.
  reason: 'The comparison section already makes this point, with a link: ''legibility
    does not guarantee faithfulness''. In the hazards list, the bullet gives the closing
    falsification condition something to name (''unfaithful rationales''), so it may
    be doing structural work. The bullet could shrink to a back-reference, or the
    earlier sentence could move here. Low confidence that either form is wasteful
    enough to change.'
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
contract: verdict
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/98c09c5e0e804906baa979f67da5f1a3/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/ee83e5d5c13293299c6f6f46/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: 98c09c5e0e804906baa979f67da5f1a3
completed-at: '2026-11-21T19:29:39Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/98c09c5e0e804906baa979f67da5f1a3/outputs/review.md
raw-output-sha256: 3eb450acfa4888c55c50f699c738795c402d63d49db9813a3aa0333789dc66e3
format: 2
---

# Review

Most of the article earns its space. The opening sets up a two-level thesis, and the later sections pay it off. The routing-line example grounds the abstract claims, and its "three things" recap turns the example into the claims the rest of the article uses. The precedent sequence (proof, formula, changing heuristics, on-balance judgment) builds toward the bet. The bet paragraph returns to the intro's three capabilities, but it adds the single-loop/double-loop framing and the condition that the declared objective stays fixed. That is a deliberate restatement with a job, so it is not flagged. The paragraph after the two-condition list partly repeats "the special case." It is kept because it explains why a non-weighing validator still counts, and it supplies the boundary cases that fail each condition.

The WARNs concern local redundancy. The payoffs paragraph largely recaps the table above it. Two sentences, one in the evidence section and one in the Bitter Lesson section, restate their preceding sentence in a defensive or metaphorical form. Each is a cut or a fold, not a structural change. The hazard bullet on unfaithful rationales overlaps an earlier sentence. It is recorded as INFO because the closing falsification condition refers to it by name.
