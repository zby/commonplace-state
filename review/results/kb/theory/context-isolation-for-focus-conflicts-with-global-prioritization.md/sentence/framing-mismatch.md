---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: 1afb04a7210a42f6880d821b817ed06e
completed-at: '2026-11-19T15:52:14Z'
findings:
- scope: passage
  quotes:
  - Parallel isolated workers each hit local blockers without seeing one another's
    work or the operator's queue.
  reason: Frames uncalibrated escalation as a parallel multi-worker phenomenon, excluding
    single-worker isolation; the actual mechanism (hitting a local blocker without
    seeing competing work or the operator's queue) applies identically to a single
    isolated worker running alongside an operator's other tasks, as the bullet's closing
    clause acknowledges.
  level: warn
- scope: passage
  quotes:
  - '**Compression hides emergencies.** Wide-shallow triage compares many candidates
    only by compressing each one. When an isolated worker emits an uninformative blocker
    ("blocked on operator input") or drops the local detail that makes an issue severe,
    triage must either fall back to deep context or misclassify severity by **unsafe
    substitution**—acting on a lossy summary as if it were the source.'
  reason: The lead-in frames the interface failure one-directionally as hiding emergencies
    (false negatives), whereas the cited mechanism—insufficient summaries forcing
    deep-context fallback or unsafe substitution—covers both unnecessary fallback
    cost on routine blockers and bidirectional severity misclassification (over-escalating
    vague trivia as well as missing emergencies).
  level: warn
- scope: passage
  quotes:
  - Inside one module or diff, guarding a hypothetical edge case looks prudent when
    system-wide complexity budgets and accepted product tolerances are absent
  reason: Emphasizes software-engineering artifacts ('module or diff') for a local
    over-specification mechanism that applies to any isolated task; does not explicitly
    exclude other domains.
  level: info
contract: verdict
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1afb04a7210a42f6880d821b817ed06e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/6310f450f862d3f883ba5d3a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1afb04a7210a42f6880d821b817ed06e/outputs/review-framing-mismatch.md
raw-output-sha256: 2ac7d4c73ea4ca6221e8e2f56d804283b0cd0f5912d0a27936f074c668898823
---

# Review

The note's core causal framing—bounded context forcing narrow-deep focus while relational prioritization needs a wide-shallow comparison set, with failure direction set by defaults rather than missing context alone—matches its mechanisms accurately. Two passages narrow a general mechanism in a way that excludes covered cases: the uncalibrated-escalation bullet opens by tying the mechanism to parallel workers rather than any isolated worker, and the residual-friction bullet titles a symmetric summary-insufficiency problem as one-directional emergency hiding.
