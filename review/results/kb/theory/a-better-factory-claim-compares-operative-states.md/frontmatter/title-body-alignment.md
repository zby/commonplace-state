---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: a39e6b6d3349d2a2189bd1edad233c8d633242991b5402a3dda3208b99643843
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: aa251602f949425d987ea5473292cbcd
completed-at: '2026-11-18T00:18:07Z'
findings:
- scope: passage
  quotes:
  - Antecedence guards this claim's auditability; it is not constitutive of improvement.
    An independently supplied retrospective criterion can ground a legitimate improvement
    claim, just not this audit-proof one.
  reason: 'Scope drift: the H1 says that a better-factory claim in general compares
    states under an antecedent relation. The body limits the antecedent requirement
    to one kind of claim: a relation-relative, auditable claim (''Throughout, *better*
    means better under the declared relation''). It also grants that a retrospective
    criterion can ground a legitimate improvement claim. So the body establishes that
    an auditable better-factory claim compares operative states under an antecedent
    assessment relation. It does not establish this for every better-factory claim.
    The title should carry the qualifier, for example ''An auditable better-factory
    claim compares…''.'
  level: warn
- scope: document
  quotes: []
  reason: 'The body also establishes a further claim that the title does not cover:
    improvement, retention and learning are different claims, and learning needs evidence
    that the experience-derived change contributed causally. This section develops
    the comparison''s role rather than drifting away from it, so it is informational
    only.'
  level: info
contract: verdict
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/371d6bf3fd618f7087a7f7a4/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/371d6bf3fd618f7087a7f7a4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/aa251602f949425d987ea5473292cbcd/outputs/review-title-body-alignment.md
raw-output-sha256: e384f108507f69150c4cd20e5c49bf2f2de29ee9f4faa81a091ffd04045d465b
---

# Review

## Summary

Most of the body supports the H1. One section argues that the relata are operative states: the predecessor and the installed successor, with no candidate. Another argues that the assessment relation is declared before development and indexed to the predecessor's prior scope. Both parts of the title therefore have support.

The mismatch is in scope. The title is phrased as a general claim about what any better-factory claim does. The body explicitly gives up that generality. It treats *better* as relation-relative and auditable. In its Scope section it says that antecedence is not constitutive of improvement, and that a retrospective criterion can ground a legitimate improvement claim. Read literally, the title asserts something the body denies. A qualifier such as "auditable" would bring the H1 into line with what the body establishes.
