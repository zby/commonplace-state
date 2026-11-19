---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/prose/redundant-restatement.md
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion: kb/instructions/review-gates/prose/redundant-restatement.md
criterion-sha256: 8ac83c3a221e55a6ece3b99917f2f96f145c07d525fd6743b90df87afc272d67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: 0b808d1de3e64c04abdb9554dbd77b33
completed-at: '2026-11-16T22:29:35Z'
findings: []
contract: verdict
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/f815b94e72a3af8b3e2e7b3f/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/f815b94e72a3af8b3e2e7b3f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/0b808d1de3e64c04abdb9554dbd77b33/outputs/review-redundant-restatement.md
raw-output-sha256: c55c64c6b020da52436ac0c257d169a701a98489cc7d0d6fa7b76ec10840e390
---

# Review

**Section openings.**

- "Commonplace mechanisms" opens directly with its first mechanism, the
  title/description/body tiers.
- "The evaluative criterion" opens by naming "resolution-switching fluidity".
  That paragraph overlaps the introduction's call for inexpensive
  bidirectional switches. However, the mechanisms section sits between them,
  so this is not a restatement of the previous section. The paragraph also
  adds the term and the contrast with retrieval accuracy, and the section
  would lose that content without it.
- "Connection to discovery" opens with the dependency on recognition, which is
  new material.
- "Boundaries" opens with the grain distinction, also new material.
- "Open questions" is a list.

**Closing paragraphs before headings.**

- The introduction ends with "This is a qualitative design criterion, not yet
  a metric…". That sentence scopes the claim. It does not preview the
  mechanisms enumeration.
- The mechanisms section ends on pointer trade-offs and does not preview the
  criterion section.
- The criterion section ends with a two-sentence limit, "These questions
  identify possible friction…". The discovery section does not repeat it.
- The discovery section's last sentence bounds that section's own claim.
- The Boundaries section's closing "Fluidity is relative to the task…" belongs
  to that section and does not preview the open questions.

Some themes recur across non-adjacent sections, such as "not yet a metric" and
task-relativity. These are not section-boundary duplications, so they are
outside this gate.
