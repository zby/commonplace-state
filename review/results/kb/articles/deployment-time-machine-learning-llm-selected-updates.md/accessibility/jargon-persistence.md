---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 11dc69181fe0448e92a191477673a3f7
completed-at: '2026-11-22T09:34:02Z'
findings:
- scope: passage
  quotes:
  - 'demonstrating sustained

    autonomous double-loop learning yet'
  reason: '"Double-loop" is glossed at its first use ("when it can also revise what
    it selects by") and illustrated in the EURISKO paragraph, but its last uses in
    the evidence section come long after either grounding. The qualifier carries meaning
    that plain language cannot replace, so this is not a strip-the-term case; a short
    refresh such as "double-loop learning (revising its own selection criteria)" would
    keep the late uses self-standing.'
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/11dc69181fe0448e92a191477673a3f7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/53062da464d508e44960ebb7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/11dc69181fe0448e92a191477673a3f7/outputs/review-jargon-persistence.md
raw-output-sha256: 2194d752fc5d218528cb75b05744ea4aa9e5cacc0a38029b2fd921964aa9c5b3
---

# Review

The note's recurring framework vocabulary is mostly kept grounded. "Selection-based learning", "preference model" and "robust comparison" are defined in the opening and their later uses usually carry a restatement nearby: the decision-analysis section re-explains the preference model and necessary preference, and the success section restates "robustly better" as "better under every compatible measure of the declared work over the declared horizon". "Targeted correction" is defined in the PRODIGY paragraph and reused once in the next section, which is within easy reach. "Workshop" and "operative change" are glossed where they appear.

These terms are also ones whose qualifier carries meaning ("robust" comparison, "double-loop", "selection-based"), so the gate's stripping remedy does not apply. Only the late uses of "double-loop" drift far from their grounding, and a brief refresh would cure that; it does not impair reading enough to warn.
