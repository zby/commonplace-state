---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '**Uncalibrated escalation.** Parallel isolated workers each hit local blockers
    without seeing one another''s work or the operator''s queue.'
  reason: Emphasizes parallel multi-worker setups even though the stated mechanism—hitting
    local blockers without seeing the operator's queue—applies equally to a single
    isolated worker; kept at info because the preceding sentence introduces this as
    one familiar manifestation rather than excluding single-worker cases.
  level: info
- scope: passage
  quotes:
  - '**Local over-specification.** Inside one module or diff, guarding a hypothetical
    edge case looks prudent when system-wide complexity budgets and accepted product
    tolerances are absent, compounding the oracle asymmetry analyzed in [a guard against
    a conjectured requirement removes the experiment that would test it](./a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md).'
  reason: Emphasizes software-engineering context ('one module or diff', 'product
    tolerances') when the local-isolation mechanism applies to any isolated subtask
    lacking global complexity budgets and tolerances; kept at info because it illustrates
    a familiar domain without excluding other domains.
  level: info
- scope: passage
  quotes:
  - '**Compression hides emergencies.** Wide-shallow triage compares many candidates
    only by compressing each one.'
  reason: The lead-in emphasizes false negatives (hidden emergencies), while the following
    sentence identifies the broader mechanism—deep-context fallback or severity misclassification
    under unsafe substitution—which covers severity errors in either direction; kept
    at info because the body does not exclude the broader cases.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/c043185d3d9f4a17b0d509c28ec48409/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/artifact/reviews/6ed3b700136cbac9debfe816/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: null
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews
launch: c043185d3d9f4a17b0d509c28ec48409
completed-at: '2026-11-19T13:45:04Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/c043185d3d9f4a17b0d509c28ec48409/outputs/review-framing-mismatch.md
raw-output-sha256: 127776aff0d45c7c2d52cc7f9438baca7d527480bedd84037075bfedbdd7698c
format: 2
---

# Review

The note frames its core claims and mechanisms at the right level of generality: bounded effective context, competing workloads exceeding usable context, missing live comparison sets versus default-action direction, and the narrow-deep versus wide-shallow architectural interface are all accurately identified. Three bullet lead-ins emphasize a narrower setting or failure direction (parallel workers, code diffs, and hidden emergencies), but none excludes the broader cases covered by the underlying mechanisms.
