---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: supplies the per-window feasibility pressure that forces task isolation"
    reason: "The opening paragraph already links this note inline and articulates the same grounding relationship ('pushes an agent system toward context isolation, because context efficiency binds first on per-window feasibility'); the footer restates the same framing without adding new navigational context."
    level: warn
  - scope: passage
    quotes:
      - "- [Intent controls a local choice only when it distinguishes its live alternatives](./intent-controls-choices-by-distinguishing-live-alternatives.md) — grounds: explains why standing priority rules in static context cannot order unseen competing work"
    reason: "The body already links this note inline in the discussion of standing priority instructions and articulates the exact same causal claim ('Because intent controls a local choice only when it distinguishes its live alternatives, a general priority rule cannot order a local branch against competing work the worker cannot see'); the footer adds no new relationship semantics or framing."
    level: warn
  - scope: passage
    quotes:
      - "- [An insufficient summary precedes the source rather than replacing it](./an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — mechanism: explains why compressed blocker records that drop scale-bearing facts force deep-context fallback or unsafe severity misclassification"
    reason: "The first bullet of 'Residual friction at the interface' already links this note inline and states the exact same mechanism (dropping severe local detail forces deep-context fallback or unsafe substitution); the footer repeats the inline framing without adding navigational value."
    level: warn
  - scope: passage
    quotes:
      - "- [Unresolved frontier](../reference/definitions/unresolved-frontier.md) — defined-in: defines the distributed possible-work surface cited as one illustration of cross-surface queueing"
    reason: "The third Commonplace example in the body already links directly to this definition, defines the surface inline, and labels it as an illustration of cross-surface queueing; the footer adds no relationship semantics or framing beyond the body's inline usage."
    level: warn
outcome: warn
---

# Review

## Assessment

Of the fifteen `Relevant Notes` entries, eleven add genuine navigational value beyond the body. Five target notes are not linked in the body at all (`Decomposition heuristics for bounded-context scheduling`, `An author should fix what the executor can't determine, not what it will`, `Agent statelessness makes routing architectural, not learned`, `Topology, isolation, and verification form a causal chain for reliable agent scaling`, and `Productive deferral requires a preserved option, discriminating evidence, and a convergence rule`). Six entries share a target with an inline link but add typed relationship semantics, contrast framing, or target-scope descriptions absent from the inline mention (`Bounded-context orchestration model`, `Weakly discriminated qualities tend to be underselected`, `A guard against a conjectured requirement removes the experiment that would test it`, `Unattended work needs the functions that interaction supplied`, `Open-ended knowledge work shares one epistemic layer across roles`, and the `Nostalgebraist` source ingest, whose inline links are bare quote attributions).

The remaining four entries flagged in frontmatter fail both test questions: the body already links each target inline and states the same causal or definitional role in nearly identical terms, so the footer adds no new framing or navigational guidance.
