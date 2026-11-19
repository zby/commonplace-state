---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This is the navigational value of [encoding link strength in position and prose](./link-strength-is-encoded-in-position-and-prose.md).
  reason: The link text paraphrases the target title accurately. In this sentence,
    though, a reader expects the target to explain how link prose preserves bearings
    during a scope transition. The target's navigational content is traversal priority
    by link weight. Only its relationship-words table, which says the introducing
    word reveals the linked note's role, bears on preserving relationships. A reader
    who follows the link finds a related but narrower point. The link text itself
    does not mislead, so this is INFO.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/255997a5222e998339244fe0/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/255997a5222e998339244fe0/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: 02a0da1552d64a10a5644fda428e405a
completed-at: '2026-11-16T22:30:39Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/02a0da1552d64a10a5644fda428e405a/outputs/review-misleading-link-text.md
raw-output-sha256: 096ccfac6ebd64fe5d0b67e5137e3dcda4bb2790e67aed5491df1ab1cb04b443
format: 2
---

# Review

Each distinct link target was checked against its title and opening paragraph; all targets resolve.

- "title-as-claim supports traversal as reasoning" matches the target's claim that claim titles turn link traversal into reasoning.
- "different metadata requirements" matches the target's comparison of link-following and search.
- "encoding link strength in position and prose" matches the target title. The surrounding sentence sets a somewhat different expectation, which is the INFO finding.
- "pointer types trade off specificity, cost, availability, and accuracy" matches the target's four axes. The target calls the first axis "context-specificity".
- "Recognizing shared structure" matches the target's definition of recognition.
- The footer links use the target titles or close paraphrases. "Addressability grain sets a matched selective-read floor" drops the title's "not compression ratio" contrast but does not misstate the claim. Each gloss agrees with its target's head.
