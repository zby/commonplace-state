---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Testing and review can happen before disposal. A temporary program can be checked
    against a retained test suite, inspected before execution, and leave a record
    of its result. What disposal removes is the ability to inspect or rerun those
    exact bytes later, unless another record preserves them. Independent regeneration
    need not reproduce the same program.
  - Ephemerality also does not imply safety or purity. Temporary code can consume
    resources, expose data, or change persistent state. Even a pure computation's
    output may guide a consequential decision. Approval, isolation, and result checking
    depend on those effects, not on whether the generated file survives.
  reason: These two paragraphs in the note's largest section pivot from cross-run
    accumulation to general caveats about temporary code (pre-disposal review, byte-level
    reproducibility, runtime safety, purity, approval, and isolation). Because they
    make up nearly a fifth of the body without serving the accumulation claim, cutting
    them or folding their only relevant thread (persistent side effects) into Scope
    would keep the middle of the note subordinate to the core claim.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/ephemeral-computation-prevents-accumulation.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/ephemeral-computation-prevents-accumulation.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: d3a6a9e3e3da3e9b0cfdf1f37204cd3f0a4037ff53011b0c118feabbef1ffbc3
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/30ebb965e8cd4b978f7a78983e38393b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/artifact/reviews/012aabe34507ff18b990a50f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews
launch: 30ebb965e8cd4b978f7a78983e38393b
completed-at: '2026-11-20T15:02:46Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/30ebb965e8cd4b978f7a78983e38393b/outputs/review.md
raw-output-sha256: 9a7d7b8ad5c5dac8b6b7e29962ecd74938885ba39db762bba8a8ebfd39ba04df
format: 2
---

# Review

## Core claim

Discarding an ephemeral generated artifact removes one reuse path rather than learning itself; cross-run accumulation fails only when no experience-dependent state survives anywhere in the deployed system to affect later work.

## Assessment

The claim is easy to find and state after one read. The four-sentence opening puts it directly in front of the reader without preamble, `## What must survive` grounds the mechanism and crystallizes it in a three-line contrast block, `## Retention and codification are different choices` guards against conflating artifact lifetime with execution form, and `## Scope` closes cleanly on what survives the claimed learning horizon.

What keeps the note slightly less sharp than it could be is the middle of `## What discarding saves and costs`, which is the longest section of the body. Its first paragraph (maintenance overhead versus regeneration or alternate carriers) and final paragraph (Kirsch's point that durable production knowledge need not live solely in the code) directly serve the core claim. Between them, however, two paragraphs branch into pre-disposal review, exact-byte reproducibility, and runtime safety, purity, approval, and isolation. Those caveats are sensible observations about ephemeral software in general, but they do not advance the cross-run accumulation argument and briefly pull the reader onto a different topic.

The simplest restoration is to remove those two middle paragraphs—leaving persistent environment state to `## Scope`, which already covers it—so `## What discarding saves and costs` moves directly from the maintenance-versus-regeneration trade-off to Kirsch's durable-carrier point. As a minor optional tightening of the headline itself, the current H1 (`Discarding all experience-dependent state prevents cross-run accumulation`) states only the necessary-condition half of the claim, leaving the sharper contrast with discarding a single ephemeral artifact to the description and opening paragraph; aligning the title with that contrast would make the takeaway even easier to retain at a glance.
