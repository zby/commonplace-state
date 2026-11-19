---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: 8c985cf61ad84b2695a8814434cb8927
completed-at: '2026-11-19T13:26:17Z'
findings:
- scope: passage
  quotes:
  - Three mechanisms in Commonplace illustrate this split at different scales
  reason: The scale labels (Mid-task noticing, Single-artifact workflow stops, Cross-surface
    queueing) arrange the examples by scale, but no later inference uses scale as
    a distinction. The list functions as illustration, and the labels are harmless
    navigation rather than load-bearing categories.
  level: info
contract: verdict
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/8c985cf61ad84b2695a8814434cb8927/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/a6ad5f7a4f4b9cdffdc8c92e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/8c985cf61ad84b2695a8814434cb8927/outputs/review-framework-decoration.md
raw-output-sha256: ace62e3007585a71fbaf2d6e2652494d72dc254b07e6ef6706f5c4fccdb5f7dd
---

# Review

## Summary

I checked each structured element to see whether one sentence could replace it without losing an inference the note uses.

- **Three failure manifestations** (uncalibrated escalation, earnest low-value tangents, local over-specification). Each has its own evidence anchor or mechanism link, and later parts use them. Escalation feeds the "operator should act now" decision and triage's "which warrant operator attention now". Tangents and out-of-scope defects appear in the narrow-deep worker's role. Over-specification connects to injected tolerances. Load-bearing.
- **Narrow-deep / wide-shallow split.** This vocabulary carries the architectural argument. The residual-friction section and the open questions use it repeatedly, for example "wide-shallow triage compares many candidates only by compressing each one". Load-bearing.
- **Three unbundled decisions** (stop, survive, operator acts now). This distinction enables a specific inference: bundling them manufactures urgency even when local judgment is sound. The ADR 138 example also uses it. Load-bearing.
- **Three residual frictions.** These are distinct failure conditions, and the open questions return to them (minimal scale-bearing facts, injected compressed state, tractability crowding). Load-bearing.
- **"Claim mode: universal" label.** It brings a refutation condition and the conditions under which universality holds, and the Scope section later reuses them. This is not decorative formalism.
- **Scale labels on the Commonplace mechanisms.** These are minor and are recorded as an info finding: the scale ordering enables no later inference.

The note contains no equations or notation that claims quantitative power.
