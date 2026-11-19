# Friction check: Final task success does not establish intended-path health

**Note:** kb/notes/final-task-success-does-not-establish-intended-path-health.md
**Central claim (one sentence):** When intended-path success and fallback success share one observable terminal state and no independent execution signal distinguishes them, final task success cannot establish intended-path health, so path deviation and guarantee degradation must be recorded separately.

## Filter
**Verdict:** SURVIVES

The claim consistently combines uninterrupted recovery with diagnosable execution: the terminal task result can remain successful while separate execution evidence identifies the path taken and any weakened guarantee.

## Signal — thinnest joints
1. **“A run-level degraded status is one projection over durable tool-attempt events, not a substitute for them. The events support asynchronous detection of primary-path failures; comparing the guarantees of the intended and actual paths supports degraded-execution classification.”** — UNSUPPORTED — Durability alone does not make attempt events sufficient for either inference. Detection also requires the events to identify the prescribed path, relate attempts to one run, and distinguish failure from intentional bypass; guarantee classification additionally requires a defined mapping from each path to assurances.
2. **“Two signals are needed because two different facts can change.”** — THIN — Showing that path deviation and guarantee degradation vary independently establishes two data dimensions, but not two distinct signals; one structured event or status could encode both. The operational meaning of “separately” needs concretization.
3. **“This enlarges the fallback space and makes the path taken harder to infer from terminal status.”** — THIN — Synthesis can increase the number of possible paths, but path identifiability depends on what terminal status exposes. Once multiple paths already collapse to the same status, a still larger fallback set does not create the non-identifiability and may not make an already non-identifying status meaningfully worse.
4. **“Together, these properties make fallback success possible.”** — THIN — Keeping the error in context, preserving the goal, and allowing another tool choice permit another attempt, but they do not by themselves supply a viable alternative capability or enough information to use it successfully.
5. **“When primary-path and fallback success have the same observable terminal state and no independent execution signal is available, that state cannot identify intended-path health.”** — HOLDS — The two underlying path-health states are observationally equivalent under the stated conditions, so the terminal state cannot distinguish them.

## For the human
Look first at what information a “durable tool-attempt event” must carry before it can actually support path-deviation detection and guarantee comparison.
