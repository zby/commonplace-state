---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: abf619794808f4b076627694915b6a909d9d4fd6d4fe40188a87b3184f966140
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: 8e0e18fdd4d6e48deb265ce1948f4e927afd9bf8bfd884fd15d97228ac36fdbc
target-capture: kb/reports/state/review/runs/v2/20261117T074932Z/artifact/reviews/080c26a290150e9f0dc8b361/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/20261117T074932Z/artifact/reviews/080c26a290150e9f0dc8b361/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261117T074932Z
launch: 6d2876e1fb734812a1a013ca35729dc1
completed-at: '2026-11-17T07:50:04Z'
raw-output: kb/reports/state/review/runs/v2/20261117T074932Z/calls/launches/6d2876e1fb734812a1a013ca35729dc1/outputs/review.md
raw-output-sha256: 73812f468a45bd66e233ba42824761ba4adab54db4dc73d7427a0c0e3aaacbd1
format: 2
---

# Review

## Summary

No load-bearing assertion leaves a material choice unresolved. The note's central claim is that removing approval waits automates adoption. It does not necessarily automate monitoring or later revision. Each candidate ambiguity in that claim is resolved by nearby context.

## Assessment

- **What "required" means.** The opening paragraphs could have left "required human evaluation" open between two readings: required by stated rules, or required by actual execution. The second paragraph ties requirement to "the process being automated and its stated requirements." It also gives a two-part test: omitting the evaluation either "prevents that process from proceeding" or "leaves a required task undone." The Scope section then handles the gap between written requirements and actual waits. A habitual wait counts as blocking, and bypassing a written requirement does not show that its function was automated. Both readings are named and assigned, so neither is left open.
- **Which process is automated.** The section "Name the process being automated" tests the boundary with a weekly sample review and rollback. In that example, adoption is automated but the wider process is not. The scope of "fully automated" is therefore fixed by a concrete case, not left to the reader.
- **Dependency versus assessment.** The two hypothetical cases say what separates required approval from optional assessment: whether the operating process depends on the human activity. The comparison also covers the edge cases. A non-binding recommendation the agent must wait for is a dependency. Human-authored acceptance rules applied by a program are not.
- **Usefulness and adequacy.** A reader might take the claim to mean that required tasks are useful or that the checks are adequate. The note rules this out explicitly, in "Identifying these dependencies does not establish that each required task is useful" and in the final Scope bullet. So the claim's consequence is stated, not left open.

The note's assertions are broad, but they are exact about population, condition and consequence. Breadth alone is not underspecification under this criterion.
