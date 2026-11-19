---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/work/concrete-cases-for-abstract-notes/abstract-claim-without-case.md
  against kb/types/review-gate.md
note: kb/work/concrete-cases-for-abstract-notes/abstract-claim-without-case.md
note-sha256: 3fed3cf7d04f630e298f6f6a24e80edbcc98644bf1013304ba2d429ce152a587
criterion: kb/types/review-gate.md
criterion-sha256: e1c9e54fabee72f5a5064ffaf36272337fd257fd044de0e4a85de2a9a5b6a6ae
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261118T184641Z
launch: 3a1835d8c1c4499188a76b936fa695b9
completed-at: '2026-11-18T18:47:15Z'
findings:
- scope: passage
  quotes:
  - '## Example (fail)'
  reason: The type spec suggests `## Example (pass)` and `## Example (fail)` blocks
    to make the test concrete. This gate states that it never returns FAIL, so the
    example under the fail heading actually shows a WARN case. The heading follows
    the template's shape but misnames the decision the example produces. A heading
    such as `## Example (warn)`, or a sentence saying the example yields WARN, would
    keep the examples consistent with the Test.
  level: info
contract: verdict
target-sha256: 3fed3cf7d04f630e298f6f6a24e80edbcc98644bf1013304ba2d429ce152a587
target-capture: kb/reports/state/review/runs/v2/20261118T184641Z/artifact/reviews/c23e499e025ce3d16cacc983/inputs/target/kb/work/concrete-cases-for-abstract-notes/abstract-claim-without-case.md
observation: kb/reports/state/review/runs/v2/20261118T184641Z/artifact/reviews/c23e499e025ce3d16cacc983/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261118T184641Z/calls/launches/3a1835d8c1c4499188a76b936fa695b9/outputs/review.md
raw-output-sha256: e1570078d9c89ae878cd9c21e17c072e470e452ce500c4cbf3f8d74fc48726dd
---

# Review

The note is a draft review gate. Judged against the authoring instructions of the `review-gate` type spec, it does what they ask.

**Closed-ended verdict assay.** The gate names one failure to look for: a central distinction or mechanism that is never shown at work on a particular case. Its Test walks the reviewer to a final decision. INFO appears only as a finding label under PASS ("add an INFO finding when cases exist but the difference they make is not stated"), as the spec requires. The gate deliberately rules out FAIL and gives a reason ("A missing case is a detectable gap, not a ground for escalation"). That fits the spec's Force and warrant section, which describes a gate as a detector rather than an acceptance authority. The spec asks for a procedure for choosing among PASS, WARN and FAIL. It does not require every gate to be able to return each of them.

**Failure mode.** The section states a concrete pattern: the reader "can repeat the wording and still cannot say which side a given situation falls on". It also limits the gate to the central contribution.

**Test.** The procedure is stepwise. It classifies the contribution, applies a wording test that exempts contributions already stated in particular terms, defines what counts as a case and what does not, and sets the requirement separately for a distinction and for a mechanism. Exceptions are named explicitly, with the adjacent gates that own them (`accessibility/undefined-terms`, `semantic/unearned-generality`, `compression-bundle/detail-overhang`). The spec asks for exactly this so that adjacent gates do not double-flag. The note also excludes instructions, ADRs, reference documents, indexes and logs.

**Self-containment.** The test depends on no contract text kept elsewhere. Every judgment it requires can be made from the note text and the criterion text, which is what the freshness hash covers.

**Examples.** The gate gives one failing example and two passing examples. The second passing example covers the wording-test exemption. The examples are minimal and match the Test. The only gap is the INFO finding above: the fail heading labels what is really a WARN case.

The draft marker comment and the file's location outside `kb/instructions/review-gates/` concern catalog discovery and the `gate_id`-to-path match. Those are left to the deterministic validator and to promotion.
