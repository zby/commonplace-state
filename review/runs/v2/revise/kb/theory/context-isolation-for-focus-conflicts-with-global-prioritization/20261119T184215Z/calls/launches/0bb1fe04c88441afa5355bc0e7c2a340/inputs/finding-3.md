---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/complexity/connection-inflation.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: c7306313cb854c3182b2c775ae8b06a8
completed-at: '2026-11-19T15:48:07Z'
findings:
- scope: passage
  quotes:
  - '- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md)
    — grounds: supplies the per-window feasibility pressure that forces task isolation'
  reason: The opening paragraph already links this note inline and articulates the
    same grounding relationship ('pushes an agent system toward context isolation,
    because context efficiency binds first on per-window feasibility'); the footer
    restates the same framing without adding new navigational context.
  level: warn
- scope: passage
  quotes:
  - '- [Intent controls a local choice only when it distinguishes its live alternatives](./intent-controls-choices-by-distinguishing-live-alternatives.md)
    — grounds: explains why standing priority rules in static context cannot order
    unseen competing work'
  reason: The body already links this note inline in the discussion of standing priority
    instructions and articulates the exact same causal claim ('Because intent controls
    a local choice only when it distinguishes its live alternatives, a general priority
    rule cannot order a local branch against competing work the worker cannot see');
    the footer adds no new relationship semantics or framing.
  level: warn
- scope: passage
  quotes:
  - '- [An insufficient summary precedes the source rather than replacing it](./an-insufficient-summary-precedes-the-source-rather-than-replacing.md)
    — mechanism: explains why compressed blocker records that drop scale-bearing facts
    force deep-context fallback or unsafe severity misclassification'
  reason: The first bullet of 'Residual friction at the interface' already links this
    note inline and states the exact same mechanism (dropping severe local detail
    forces deep-context fallback or unsafe substitution); the footer repeats the inline
    framing without adding navigational value.
  level: warn
- scope: passage
  quotes:
  - '- [Unresolved frontier](../reference/definitions/unresolved-frontier.md) — defined-in:
    defines the distributed possible-work surface cited as one illustration of cross-surface
    queueing'
  reason: The third Commonplace example in the body already links directly to this
    definition, defines the surface inline, and labels it as an illustration of cross-surface
    queueing; the footer adds no relationship semantics or framing beyond the body's
    inline usage.
  level: warn
contract: verdict
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/c7306313cb854c3182b2c775ae8b06a8/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/deb7fc303a716db22d89a316/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/c7306313cb854c3182b2c775ae8b06a8/outputs/review-connection-inflation.md
raw-output-sha256: 0673649dffd42956a93d29516022a357c66a10c5cdc80a68235f561c01ddaa8b
---

# Review

## Assessment

Of the fifteen `Relevant Notes` entries, eleven add genuine navigational value beyond the body. Five target notes are not linked in the body at all (`Decomposition heuristics for bounded-context scheduling`, `An author should fix what the executor can't determine, not what it will`, `Agent statelessness makes routing architectural, not learned`, `Topology, isolation, and verification form a causal chain for reliable agent scaling`, and `Productive deferral requires a preserved option, discriminating evidence, and a convergence rule`). Six entries share a target with an inline link but add typed relationship semantics, contrast framing, or target-scope descriptions absent from the inline mention (`Bounded-context orchestration model`, `Weakly discriminated qualities tend to be underselected`, `A guard against a conjectured requirement removes the experiment that would test it`, `Unattended work needs the functions that interaction supplied`, `Open-ended knowledge work shares one epistemic layer across roles`, and the `Nostalgebraist` source ingest, whose inline links are bare quote attributions).

The remaining four entries flagged in frontmatter fail both test questions: the body already links each target inline and states the same causal or definitional role in nearly identical terms, so the footer adds no new framing or navigational guidance.
