---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 919cb9448e7e0a0da74d2b827a7c345dc485401067e357fa4ecff065222eed52
criterion: kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
criterion-sha256: 72878e536fd897c07be2c1dec0230689269ff118d9e862eef66f6fc8b814c3b2
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/rewrite/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261123T103826Z/reviews/874ccee35866
launch: ee4249bec2d54a4c8999ec1b399ff2fb
completed-at: '2026-11-23T10:42:56Z'
findings:
- scope: passage
  quotes:
  - The supplied theory does not settle it.
  reason: 'Basis: note.md, section ''When does open-ended work need more than level
    1?''. ''The supplied theory'' is language from the rewrite commission (''if the
    supplied theory does not settle it''). A reader of the published note has no supplied
    theory and cannot tell which notes are meant. Required change: name what does
    not settle the question in terms the reader has, for example ''The notes cited
    here do not settle it'' or ''Neither this argument nor the fixed-model note settles
    it''.'
  level: warn
- scope: document
  quotes: []
  reason: 'Basis: supplied-candidate-report.md, ''Still supported (no action)'', checked
    against supplied-inbound.md. Three classifications are inaccurate. (1) The continual-learning-in-token-space
    ingest uses the note for the substrate framing the candidate dropped: ''the same
    anti-weight-monopoly move... covers one branch of the non-weight side'', and its
    proposed note treats this note as part of ''the KB''s broader repo-artifact model''.
    That is a lost use like the trace-learning and from-human-memory entries. (2)
    The faithful-self-evolvers passage is cut at 1200 characters before its reason
    for citing this note (''(acc [cut''), so the report cannot list it as still supported.
    It needs the same ''check directly'' treatment as externalization and prime-agent.
    (3) The long-horizon-agents passage says the campaign ''does not establish systematic
    regression checking for such changes'', which reads the note as asking for regression
    checks. That part of the use is weakened, even though its retained-rule example
    still fits. Required change: move token-space to the affected list, mark faithful-self-evolvers
    as truncated and needing a check, and note the weakened regression framing in
    long-horizon-agents. The candidate text itself needs no change.'
  level: warn
- scope: passage
  quotes:
  - Some retained state must differ between the histories that call for different
    decisions.
  reason: 'The two-part requirement follows almost analytically from its condition:
    if decisions at the same input differ across histories, some retained difference
    must reach the decision. The note acknowledges this in effect by keeping the requirement
    weak and putting its predictive content in the contrasting-histories test, the
    changed-versus-improved separation and the three levels. That is what the commission
    asked for (''Prefer an honest limited result''), so no change is needed. A later
    critique may push here.'
  level: info
- scope: document
  quotes: []
  reason: The title is unchanged, as the commission requires. The candidate flags
    the mismatch both in Scope ('The title's word can be read more strongly than the
    argument supports') and in the report, which offers a retitle option for the operator.
    This satisfies the reserved-decision instruction. The Scope flag covers 'governing'
    but not the unconditional 'Continual learning requires...', which the body narrows
    to capabilities stated as history-dependent decisions. The operator may want to
    weigh that as well when deciding on a retitle.
  level: info
contract: verdict
target-sha256: 919cb9448e7e0a0da74d2b827a7c345dc485401067e357fa4ecff065222eed52
target-capture: kb/reports/state/review/runs/v2/rewrite/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261123T103826Z/reviews/874ccee35866/calls/launches/ee4249bec2d54a4c8999ec1b399ff2fb/inputs/note.md
observation: kb/reports/state/review/runs/v2/rewrite/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261123T103826Z/reviews/874ccee35866/artifact/reviews/d5fd43114a7b94d2004284cd/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/rewrite/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261123T103826Z/reviews/874ccee35866/calls/launches/ee4249bec2d54a4c8999ec1b399ff2fb/outputs/review.md
raw-output-sha256: cb783a3ad62be40f723d19b2e48f8b9d6b8bcd147fd9d29054661805278fc179
---

# Review

## Summary

The candidate makes the commissioned contribution and can be published. Two nonblocking changes are needed. One phrase in the body leaks rewrite-workflow language. The writer's affected-citations report misclassifies three inbound uses.

## Commission fit

- **Strongest nontrivial conditional requirement.** The note states a conditional necessity: history-dependent decisions at matched inputs require retained state that differs across histories plus a consumption rule giving it behavioral authority. It also states what the requirement does not demand: rewriting code, weights or rules, a reject-capable gate, or autonomous selection. It goes beyond "storage is not use" in three ways:
  - It separates fixed program text from behaviour at matched inputs (`d = P(x, s)`).
  - It turns the requirement into a test with contrasting histories.
  - It sorts what must change into three levels.
- **Fixed-program objection.** The note keeps the objection in its strongest form, a fixed interpreter computing over arbitrary retained data, and answers it rather than dismissing it.
- **Required elements.** The note includes:
  - the contrasting-histories test, with a labelled hypothetical winning case and losing case;
  - the separation of changed decisions from improved ones, with a hypothetical regression continuation;
  - the history / procedure / machinery distinction;
  - a falsifiable matched comparison for the open-ended conjecture.
- **Exclusions.** The note respects every commissioned exclusion:
  - Scope disclaims a universal definition of continual learning.
  - The note says outright that open-endedness alone does not defeat a fixed interpreter.
  - It makes no empirical claims about regression prevalence.
- **Switching among existing behaviours.** The opening and level 1 together let a designer predict when switching suffices. Switching on the current input needs no learning. Switching chosen by a retained selector is level-1 learning.

## Source fidelity

Each sourced claim matches its authorized source:

- **Behavioral authority (source 3):** consumer, channel and force; authority belongs to the use, not the bytes.
- **Knowledge storage (source 2):** the four evaluation results, and raw trajectories versus condensed experience. The candidate scopes the second to "the experiments reported" and does not generalize it.
- **Fixed-model house (source 1):** the cost-versus-expressiveness distinction, the effective-update-space limit and the matched frozen-versus-revising comparison.
- **Proposal-selection loop (source 4):** direct updates versus gated selection, with both counting.
- **Defining improvement (source 5):** consequences on the expected work stream compared against a named alternative fixed before the trial.

The link to the fixed-decomposition note is not an authorized source. It is used only as source 1 uses it, so it adds no unsupported content.

## Contracts

The candidate has a claim title with the `title-as-claim` trait. Its main claim and mechanism appear at the top, and its limits sit under `## Scope`. Its footer labels are permitted in the theory collection. Every body passage serves the designer's task, and none surveys unneeded detail.

## Affected citations

The report identifies most lost uses accurately: regression validation, the substrate split, approval-based governance, and the "reserves the term" wording. Its "still supported" list misclassifies three entries; the warn finding lists them. Fixing those dependents is separate work and does not affect this candidate's publication.
