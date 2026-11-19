---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - just not this audit-proof one
  reason: The intended meaning is the auditable, antecedently declared claim that
    the opening calls 'relation-relative and auditable'. The '-proof' idiom suggests
    resistance or immunity. 'Audit-proof' can therefore be read as 'immune to audit',
    which reverses the point, or as 'certain to survive audit', a certainty the note
    disclaims. The literal replacement 'just not this antecedently declared, auditable
    one' removes both readings and matches the earlier wording.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/prose/mannered-prose.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/prose/mannered-prose.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/61cda0d6d2732376e0ead464/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/61cda0d6d2732376e0ead464/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 96dd9be42f1b478db1298ed248f72326
completed-at: '2026-11-18T00:19:52Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/96dd9be42f1b478db1298ed248f72326/outputs/review-mannered-prose.md
raw-output-sha256: fd73e73c826aa15b2959c8df5ffba5f0e4d77af1a3e1ee7ca195087082591218
format: 2
---

# Review

## Summary

The note is mostly literal. Most of its figurative wording is conventional and precise: "keep the comparison's endpoints straight", "read off a construction event", "out of reach", "blocks" and "guards". These phrases add no unsupported connotations. "Factory" is a defined, linked term, not ornament.

One phrase needs a literal replacement. "Audit-proof" in the Scope section is an idiom. It is ambiguous between "immune to audit" and "guaranteed to pass audit", and neither reading matches the auditability the note establishes. "Auditable" or "antecedently declared" says the intended thing directly. This is a single local instance, so the outcome is WARN.
