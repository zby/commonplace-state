---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 7bbc0106e7eedbac5bfd71e7cebc917ff6a74056d6eef1719383daf0ce96dc6e
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: 5e36d291e02142ad8df5bc8e2f3a242b
completed-at: '2026-11-19T13:26:03Z'
findings:
- scope: passage
  quotes:
  - The conflict requires bounded effective context and a competing workload whose
    combined live state does not fit beside deep task context.
  reason: The body establishes the conflict only under bounded effective context and
    a competing workload that does not fit beside task context. It also limits the
    claim to relational prioritization, not intrinsic local checks. The H1 is unqualified,
    but the opening paragraph, the claim-mode statement and the Scope section carry
    these conditions next to the claim. That is acceptable compression for a title,
    not scope drift. Recorded for visibility only.
  level: info
contract: verdict
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/5e36d291e02142ad8df5bc8e2f3a242b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/d51fc413ddb377488d1c2e99/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/5e36d291e02142ad8df5bc8e2f3a242b/outputs/review-title-body-alignment.md
raw-output-sha256: 9ec4f8aad021b7563d2330fdb183599fff9c4350cff20a1eeb6a710f45d93e0e
---

# Review

## Summary

The H1 says context isolation for focus conflicts with global prioritization. The body supports this directly. The opening argues that a worker isolated to its own task lacks the live comparison set that global prioritization needs. The body then defines both sides of the conflict and states falsification conditions.

The later sections do not drift from the claim. The section on missing context and defaults explains how the conflict shows up. The sections on splitting execution from triage and on residual friction answer the conflict without replacing it. They argue that the split moves the trade-off to an interface rather than removing it, which keeps the title's claim central. The body is wider than the title because it also covers the architectural response. Development beyond the headline claim is normal and does not count as claim drift.
