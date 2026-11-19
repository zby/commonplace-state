---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/role-in-the-kb-gate.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
criterion: kb/instructions/role-in-the-kb-gate.md
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/role
launch: 4b4b343dd8184d7dbb2a117027fe1f6e
completed-at: '2026-11-16T22:06:23Z'
findings:
- scope: passage
  quotes:
  - The claim holds between two operative states of the factory, under an assessment
    relation fixed before the development it judges
  reason: SUPPLIED — kb/tags/software-factory-README.md — the tag head cites the note
    for what an improvement claim compares and for the relation being fixed in advance;
    the note states both directly in its opening paragraph and develops them in its
    first two sections.
- scope: passage
  quotes:
  - Whether it got *better* is therefore its own claim with different relata and its
    own declarations. The claim holds between two operative states of the factory,
    under an assessment relation fixed before the development it judges
  reason: SUPPLIED — kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md
    — the definition note hands off 'establishing the claim' of improvement as a separate
    measurement problem disciplined by an antecedent better-factory comparison, and
    its footer says the note supplies the relata and antecedent relation for the improvement
    half of the learning claim. The note supplies the separation, the relata (predecessor
    and operative successor) and the antecedent relation. Its Scope line that antecedence
    'guards this claim's auditability; it is not constitutive of improvement' agrees
    with the dependent's position that improvement can be a fact of the trajectory
    before anyone verifies it.
- scope: passage
  quotes:
  - 'Retention has no quality requirement: a retained change can degrade the factory
    as easily as improve it.'
  reason: 'DUPLICATED — kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md
    — the dependent''s passage already states that a retained change can degrade later
    production, so retention is established without learning. The note recaps this
    as its motivating premise. The dependent states it better for the dependents''
    use: it is the definition''s home, names the consequence (the factory degenerates
    rather than learns) and ties it to the declared objective; the note''s sentence
    is a one-line restatement that links back to it.'
contract: report
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/role/artifact/reviews/f93abf47955ed2692186da59/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/role/artifact/reviews/f93abf47955ed2692186da59/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/role/calls/launches/4b4b343dd8184d7dbb2a117027fe1f6e/outputs/review.md
raw-output-sha256: 2ef2d61cdae403070ebcde4e81d62e97cb30f4b2ce9f0b7ee1e92b73b752c4dd
---

# Role in the KB: A better-factory claim compares operative states

## Role
The note is the measurement-side companion to the factory-learning definition: that definition delegates to it the question of how an improvement claim is established, and the software-factory tag head lists it for what an improvement claim compares and for the relation being fixed in advance. No dependent argues from its finer structure; both use it for its headline claim.
Relied on: the better-factory claim as a separate claim from retention; operative states (predecessor and operative successor) as the relata; the antecedent assessment relation. Unused: the candidate/operative-successor distinction and the two successor routes (measurement over snapshots, candidate admission); scope-indexed non-regression and the specified target; the preserved factory-development path; evaluator location as a declaration separate from the learner boundary; the oracle problem; the claim that neither improvement nor retention entails the other; the whole-production-environment scope of the compared states.

## Dependents
- `kb/tags/software-factory-README.md` — a citation with a gloss: what an improvement claim compares, and that the relation is fixed in advance.
- `kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md` — a premise for its hand-off: establishing improvement is a separate measurement problem, disciplined by an antecedent comparison over stated relata.

## Duplication
The note's opening sentence on retention having no quality requirement restates the factory-learning note's passage that a retained change can degrade later production. The dependent's version is the fuller and better-placed one for the dependents' use; see the DUPLICATED finding.

## Untaken recommendations
None. Neither linking file is a source ingest or carries a revise or add-citation passage aimed at the note.

## Reach
- The separation of the better-factory claim from retention, the operative-state relata and the antecedence of the relation reach `kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md`, which hands improvement-measurement off to the note in exactly these terms, and `kb/tags/software-factory-README.md`, whose gloss names "what an improvement claim compares" and "the relation is fixed in advance".
- The phrase "antecedent better-factory comparison" is the dependent definition note's link text; renaming the concept away from comparison or antecedence would leave that link text stale.
- Changes to the successor routes, scope indexing, preserved factory-development path, evaluator location, oracle problem or the neither-entails section reach no dependent.
