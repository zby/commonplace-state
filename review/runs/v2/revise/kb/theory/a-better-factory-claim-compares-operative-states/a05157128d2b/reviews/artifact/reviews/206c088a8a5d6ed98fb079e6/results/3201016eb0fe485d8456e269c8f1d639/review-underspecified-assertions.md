---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Both are declared while only the predecessor exists.
  reason: 'Reading 1: the requirements are declared before any candidate is constructed.
    Reading 2: they are declared before any successor is installed, which allows declaration
    after staged candidates have been evaluated. Under reading 2, requirements could
    be chosen after seeing a candidate''s staging results, which reopens the post-hoc
    selection the note aims to block. The opening''s ''fixed before the development
    it judges'' largely settles the matter in favour of reading 1. That leaves a possible
    but not clearly material ambiguity.'
  level: info
- scope: passage
  quotes:
  - just not this audit-proof one
  reason: '''Audit-proof'' could mean open to audit for post-hoc selection, or proof
    against audit challenge. The sentence marks the boundary between legitimate retrospective
    improvement claims and this framework''s claim. Nearby context (''auditable'',
    ''available for inspection'') favours the first reading.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/206c088a8a5d6ed98fb079e6/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/206c088a8a5d6ed98fb079e6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 3201016eb0fe485d8456e269c8f1d639
completed-at: '2026-11-18T00:21:21Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/3201016eb0fe485d8456e269c8f1d639/outputs/review-underspecified-assertions.md
raw-output-sha256: 5ba2e12de6d2645bbe2d6c13a890b786661788a7ae95a287388a7d1b170cb504
format: 2
---

# Review

Load-bearing assertions checked:

- **The relata.** The definitions of predecessor, candidate and operative successor specify their conditions. A successor is installed and depended on, and is fixed at a named measurement boundary in continuously revised systems.
- **The two-component relation.** "non-regression thresholds on the predecessor's prior scope" and "improve … by a declared amount on at least one named production dimension" leave thresholds and dimensions open. That is deliberate: they are parameters the comparison must declare, not choices the note leaves unresolved. Open Questions records what the declaration must specify about baselines and measurement.
- **The post-hoc selection mechanism.** It is stated precisely, with its limit ("does not show that the requirements track factory quality").
- **The factory-development preservation consequence.** It is conditional on scope and specifies the property to preserve: a revision path that remains applicable, not merely editable files.
- **The learning case.** It names the evidence needed: a contrast of otherwise equivalent runs with and without the retained instruction.

The two remaining ambiguities are mostly settled by nearby context and are recorded as INFO.
