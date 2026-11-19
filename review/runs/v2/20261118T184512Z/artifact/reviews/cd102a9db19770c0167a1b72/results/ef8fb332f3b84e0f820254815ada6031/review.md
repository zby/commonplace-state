---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - INFO when cases exist but the difference they make is not stated, or when the
    only case sits far from the statement of the contribution.
  - PASS otherwise.
  reason: The type spec says INFO may label a finding but is not a final decision,
    and that the Test may route INFO findings without changing a clean final decision.
    The gate lists INFO beside WARN and PASS as a decision branch and then says 'PASS
    otherwise', so read literally an INFO case is excluded from PASS and has no final
    decision. A reviewer must guess whether to return PASS with an info finding. State
    that these conditions produce an INFO finding under a PASS decision.
  level: warn
- scope: document
  quotes: []
  reason: The Test never routes to FAIL; its strongest outcome is WARN. The type spec
    asks for a procedure for choosing PASS, WARN or FAIL, but it does not require
    every gate to use FAIL. A gate that only detects a problem can reasonably top
    out at WARN. Saying so explicitly would remove any doubt that FAIL was left out
    by accident.
  level: info
outcome: warn
description: Retained verdict review of kb/work/concrete-cases-for-abstract-notes/abstract-claim-without-case.md
  against kb/types/review-gate.md
contract: verdict
note: kb/work/concrete-cases-for-abstract-notes/abstract-claim-without-case.md
criterion: kb/types/review-gate.md
note-sha256: 86f16e3981ba12719743a111fb41c5c1f78acdbea5a3ecc94398a36430f0391e
criterion-sha256: e1c9e54fabee72f5a5064ffaf36272337fd257fd044de0e4a85de2a9a5b6a6ae
target-sha256: 86f16e3981ba12719743a111fb41c5c1f78acdbea5a3ecc94398a36430f0391e
target-capture: kb/reports/state/review/runs/v2/20261118T184512Z/artifact/reviews/cd102a9db19770c0167a1b72/inputs/target/kb/work/concrete-cases-for-abstract-notes/abstract-claim-without-case.md
observation: kb/reports/state/review/runs/v2/20261118T184512Z/artifact/reviews/cd102a9db19770c0167a1b72/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261118T184512Z
launch: ef8fb332f3b84e0f820254815ada6031
completed-at: '2026-11-18T18:45:48Z'
raw-output: kb/reports/state/review/runs/v2/20261118T184512Z/calls/launches/ef8fb332f3b84e0f820254815ada6031/outputs/review.md
raw-output-sha256: 1e00b52521b0ce9d89ee77a8733886ffad0d587a1946b11df2a7129c5d19c755
format: 2
---

# Review

The draft gate mostly does what the review-gate type spec asks. It is a closed-ended verdict assay. Its `## Failure mode` names a concrete pattern: a central distinction or mechanism stated without a case. Its `## Test` gives a numbered procedure with explicit PASS and WARN conditions. It names the neighbouring gates it should not double-flag (`accessibility/undefined-terms`, `semantic/unearned-generality`, `compression-bundle/detail-overhang`) and the artifact kinds it does not apply to. It has fail and pass examples, plus a second pass example for wording that is already particular. The test is self-contained: it defines "case", "distinction" and "mechanism" in its own text and does not depend on contract language held elsewhere. It works as a detector, not as an acceptance authority, which matches the Force and warrant section.

One instruction is not met: INFO's place in the verdict. The type spec treats INFO only as a finding label that leaves a clean final decision unchanged. The gate gives INFO a branch of its own next to WARN and PASS, and "PASS otherwise" then leaves the INFO case without a final decision. A one-line fix closes the gap: these conditions produce an INFO finding under a PASS decision.

The missing FAIL route is noted for information only. It is a defensible design choice, not a conformance failure.
