---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
note-sha256: 0519683dd2a2ad488108c956b1c1a59791f57be492893178645772a263c8257f
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: bc277cf6d61d4be6914a3ce31a323912
completed-at: '2026-11-16T22:32:02Z'
findings:
- scope: document
  quotes: []
  reason: The title scopes the claim to 'a knowledge base'. The definition and the
    four questions (views of differing scope and detail, cheap transitions, preserved
    relationship) would apply to any navigable information system, such as documentation
    sets or codebases. The mechanisms section, however, is explicitly Commonplace-specific,
    and the KB's declared scope is KB methodology, so this reads as intentional domain
    scoping and not as narrowing the argument needs to undo.
  level: info
contract: verdict
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/be8ba3eb0b5f7dfe969aec05/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/be8ba3eb0b5f7dfe969aec05/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/bc277cf6d61d4be6914a3ce31a323912/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: a542702a01f36b61240959cccf6b0a355abad4c289faffb09f41fe704e88eb0e
---

# Review

## Summary

Qualifiers extracted from the title, description and opening:

- **"knowledge base"**: intentional domain scoping (INFO above).
- **"fluid"**: defined by the criterion section as moving without avoidable transition cost or loss of relationship. It is the property under evaluation, so it is load-bearing.
- **"task-relevant"**: used throughout and in Boundaries ("Fluidity is relative to the task"). Removing it would make the claim false for tasks that need no return to a broad view. It is load-bearing.
- **"in both directions"**: used by both the downward questions (choose a narrower target, reach the detail) and the upward one (recover a broader view). Boundaries develops it. It is load-bearing.
- **"qualitative"** (description and opening): this marks the criterion's status, not its scope. It does not narrow the claim.

No qualifier narrows the central claim without doing work in the reasoning.
