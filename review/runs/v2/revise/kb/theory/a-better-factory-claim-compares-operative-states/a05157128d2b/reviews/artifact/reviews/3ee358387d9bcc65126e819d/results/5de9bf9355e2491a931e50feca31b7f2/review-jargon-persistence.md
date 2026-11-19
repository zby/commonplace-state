---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the preserved-path consequence then no longer follows
  reason: '''Preserved-path consequence'' is a compressed back-reference to the factory-development
    non-regression requirement stated several sections earlier. It is used only once,
    so it is not persistent jargon, but in the Scope list it is opaque unless the
    reader recalls that paragraph; spelling it out (the requirement to keep the factory
    able to revise itself) would read more easily.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/3ee358387d9bcc65126e819d/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/3ee358387d9bcc65126e819d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 5de9bf9355e2491a931e50feca31b7f2
completed-at: '2026-11-18T00:18:19Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/5de9bf9355e2491a931e50feca31b7f2/outputs/review-jargon-persistence.md
raw-output-sha256: df3cdb16a43471cb8040ac5f552b98035031ce51b2e08b3eec5521b59d6cdf2f
format: 2
---

# Review

I tracked the note's KB-specific vocabulary through the body: operative / operative successor, predecessor, candidate, assessment relation, non-regression, prior scope, antecedent / antecedence, and declared comparison.

Each recurring term either has its meaning carried by a qualifier that plain language would lose (the "operative" in operative state or operative path marks the installed-and-depended-on condition) or stays readable from local context. "Predecessor", "candidate" and "declared comparison" are close to plain English after their grounded definitions. The Scope list's later uses of "antecedence" sit directly beside their consequences ("blocks post-hoc dimension selection"), so the reader does not need to scroll back. No term repeatedly reappears with its grounding lost. The one compressed back-reference is noted as info.
