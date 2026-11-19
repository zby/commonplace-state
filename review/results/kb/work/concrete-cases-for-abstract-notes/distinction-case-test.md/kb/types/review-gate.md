---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/work/concrete-cases-for-abstract-notes/distinction-case-test.md
  against kb/types/review-gate.md
note: kb/work/concrete-cases-for-abstract-notes/distinction-case-test.md
note-sha256: bbf2fe65274dd4e85d0f886ed529000cb83d39991e2b7f2b5fd34208c7396d50
criterion: kb/types/review-gate.md
criterion-sha256: e1c9e54fabee72f5a5064ffaf36272337fd257fd044de0e4a85de2a9a5b6a6ae
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261118T184600Z
launch: 8cd540f156ba4383840d6b3b6ef4a027
completed-at: '2026-11-18T18:46:30Z'
findings:
- scope: passage
  quotes:
  - The note does not say which, and does not exclude the case.
  reason: 'The type spec''s optional `## Example (fail)` block is meant to make the
    test concrete. This gate never returns FAIL, so the example headed ''fail'' actually
    shows a WARN case, and it never names the decision it leads to. The example still
    conforms, but adding a closing sentence such as ''Result: WARN'' would tie it
    to the gate''s own decision rules.'
  level: info
contract: verdict
target-sha256: bbf2fe65274dd4e85d0f886ed529000cb83d39991e2b7f2b5fd34208c7396d50
target-capture: kb/reports/state/review/runs/v2/20261118T184600Z/artifact/reviews/bb53a538064292a8953fe2f1/inputs/target/kb/work/concrete-cases-for-abstract-notes/distinction-case-test.md
observation: kb/reports/state/review/runs/v2/20261118T184600Z/artifact/reviews/bb53a538064292a8953fe2f1/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261118T184600Z/calls/launches/8cd540f156ba4383840d6b3b6ef4a027/outputs/review.md
raw-output-sha256: 099f4ff3480d6e9cb5f895cf852824ecd8e2717bf58f396bfd19f1c8dec7c7dd
---

# Review

The draft gate does what the review-gate authoring instructions ask.

- **Failure mode.** `## Failure mode` names the pattern a reviewer should look for: a central distinction that fails on a particular case. It lists five concrete ways this happens: the case fits both sides, fits neither, depends on an unfixed word, gets an unsupported conclusion, or the distinction changes nothing.
- **Test.** `## Test` is a numbered procedure followed by explicit decision rules for WARN and PASS. INFO appears only as a finding label under PASS, never as a final decision, as the spec requires. The spec asks for a procedure for choosing PASS, WARN or FAIL. The gate deliberately rules out FAIL and explains why: the cases are the reviewer's own constructions. This matches the spec's "Force and warrant" section, which says to write a gate as a detector rather than an acceptance authority, so leaving out FAIL is consistent with the type.
- **Exceptions.** The spec asks the test to name exceptions explicitly. The "Do not flag here" paragraph hands four neighbouring failure modes to named gates and states this gate's own boundary.
- **Self-contained test.** The test does not depend on contract text kept elsewhere. Its criteria come from the target note itself and the cases the reviewer builds, so all of the judgment rests on hashed criterion text.
- **Examples.** The gate has both a fail example and a pass example. They share one scenario: the pass example adds the sentence that fixes the lapsed case, which makes the test concrete as the spec intends. The one INFO finding covers a minor gap: the fail example never states which decision it leads to.

The frontmatter and the HTML draft marker are left to the deterministic validator.
