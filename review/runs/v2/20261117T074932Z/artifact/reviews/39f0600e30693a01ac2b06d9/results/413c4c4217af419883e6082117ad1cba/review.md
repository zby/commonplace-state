---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Conversely, bypassing a written requirement does not by itself establish that
    its function has been automated or is unnecessary.
  reason: This sentence restates the closing paragraph of 'Name the process being
    automated', which already says removing an unnecessary requirement changes the
    process and that simply skipping the task does not fulfill the existing requirement.
    The Scope bullet adds no new boundary case. The first half of the bullet (a habitual
    wait can block automation without a written rule) is new and should stay; cut
    this trailing sentence, or fold any distinct nuance into the earlier paragraph.
  level: warn
- scope: passage
  quotes:
  - The distinction identifies required work and actual waits; it does not establish
    that the chosen requirements or checks are adequate, or that the resulting changes
    improve the system.
  reason: This is defensive redundancy. The opening framing already separates operating
    dependency from whether the system improved ('a judgment that the system improved
    does not by itself show whether human evaluation was required'). The body also
    already states 'Identifying these dependencies does not establish that each required
    task is useful.' This bullet repeats both disclaimers and adds only 'checks are
    adequate', which is close to the body's statement that a required task may not
    be useful. Delete the bullet, or fold 'or adequate' into the earlier sentence.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
note-sha256: abf619794808f4b076627694915b6a909d9d4fd6d4fe40188a87b3184f966140
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
target-sha256: 8e0e18fdd4d6e48deb265ce1948f4e927afd9bf8bfd884fd15d97228ac36fdbc
target-capture: kb/reports/state/review/runs/v2/20261117T074932Z/artifact/reviews/39f0600e30693a01ac2b06d9/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/20261117T074932Z/artifact/reviews/39f0600e30693a01ac2b06d9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261117T074932Z
launch: 413c4c4217af419883e6082117ad1cba
completed-at: '2026-11-17T07:50:05Z'
raw-output: kb/reports/state/review/runs/v2/20261117T074932Z/calls/launches/413c4c4217af419883e6082117ad1cba/outputs/review.md
raw-output-sha256: 846466de0c915167db3c1b9599c35583a2a2cee1c1a154907365d72a0e005604
format: 2
---

# Review

## Summary

Most of the note earns its space. The opening paragraphs state the claim and define "required" relative to a named process. The two hypothetical cases make the distinction concrete. The paragraph after them adds two boundary cases that are easy to miss: a non-binding recommendation that still blocks, and human-authored rules applied without a new judgment. The weekly-review example shows how a task can be required without blocking adoption. The first Scope bullet, on anticipated assessment, adds a new boundary.

Two parts of the Scope section mostly repeat the body as disclaimers. One is the second half of the written-versus-actual bullet. The other is the final bullet on adequacy and improvement. Both qualifications are already stated in the body: one in "Name the process being automated", the other in the opening comparison with the operative-states note. They should be cut or folded into those passages.

The sentence "Execution continuing without a person establishes only the absence of a blocking step" partly repeats the first paragraph. It still passes because it turns the definition into a usable inference limit. The sentence "What matters is whether the operating process depends on the human activity" also passes: it is the pivot from the examples, and new boundary cases follow it.
