---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 3201016eb0fe485d8456e269c8f1d639
completed-at: '2026-11-18T00:21:21Z'
findings:
- scope: passage
  quotes:
  - This framework uses the predecessor's prior capabilities as that scope.
  - If the checked prior scope includes an operative path
  reason: The non-regression scope drifts across the note. The body first says the
    scope is the predecessor's prior capabilities. Later the factory-development consequence
    is conditional on the 'checked prior scope' including that path, and Scope says
    preservation follows 'only when that capability is included in the checked scope'.
    The description says 'declared prior capabilities'. If the scope is all prior
    capabilities, an existing factory-development path is always included and the
    condition is idle. If it is a declared or checked subset, the earlier sentence
    overstates it. This needs human confirmation of which is meant.
  level: info
- scope: passage
  quotes:
  - just not this audit-proof one
  reason: The opening calls the claim 'auditable'; the Scope section calls it 'audit-proof'.
    'Audit-proof' can read as immune to audit, the opposite of open to inspection.
    This is likely terminology drift rather than a contradiction.
  level: info
contract: verdict
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/b894b8be536e50d929c685e7/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/b894b8be536e50d929c685e7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/3201016eb0fe485d8456e269c8f1d639/outputs/review-internal-consistency.md
raw-output-sha256: d3e1d9b69f0471cf0587c170f140c79490500c2b636f29aa91eb44a63f0cb882
---

# Review

Claims checked across sections:

- **Opening and Scope.** The opening stipulates relation-relative "better" and disclaims any verdict on quality over the open family. Scope repeats this ("does not supply an oracle"). They are consistent.
- **Candidate exclusion and staging.** "A candidate … is not a term in the comparison" sits alongside "A staging comparison can supply evidence for adopting a candidate". These are consistent: staging evidence bears on adoption, not on the improvement claim.
- **Two-component relation and the alternative relation.** The body declares non-regression plus improvement as this framework's choice. Scope allows a retirement-permitting relation and drops the preserved-path consequence. These are consistent.
- **Antecedence.** The body says prior declaration blocks post-hoc selection and does not show that the requirements track quality. Scope says antecedence guards auditability and is not constitutive of improvement. These are consistent with each other.
- **Improvement, retention and learning.** The three cases match the opening's separation of retention from improvement.
- **Description and body.** The description's "separates an adopted improvement from a discarded proposal" matches the relata section.

There are no pairwise contradictions. The two drifts recorded as INFO concern which prior capabilities non-regression covers, and "auditable" versus "audit-proof".
