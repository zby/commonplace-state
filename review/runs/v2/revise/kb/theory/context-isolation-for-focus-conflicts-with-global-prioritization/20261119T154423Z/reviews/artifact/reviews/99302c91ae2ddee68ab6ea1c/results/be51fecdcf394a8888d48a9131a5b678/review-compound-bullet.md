---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - On a small workload whose comparison-sufficient live state fits inside one usable
    window—or a separable workload whose opportunity cost reduces to a locally calibrated
    metric such as a dollar cap or latency budget—the conflict disappears or can be
    handled by injected thresholds.
  reason: Packs two independent scope exclusions—a small workload fitting in one window
    (where the conflict disappears) and a separable workload with a locally calibrated
    metric (where injected thresholds handle it)—into one 43-word bullet via em-dashes,
    burying the second exclusion during scanning.
  level: warn
- scope: passage
  quotes:
  - How much compressed global state (active bottlenecks, tolerances, budgets) can
    be injected into a focused worker's handoff—and what makes such signals locally
    calibratable—before context load degrades task solving?
  reason: Combines two independent open questions—the context-budget ceiling for injecting
    compressed global state and the design property that makes such signals locally
    calibratable—by interrupting the first question with an em-dash clause.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/structural/compound-bullet.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/structural/compound-bullet.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion-sha256: 21f452393fa553aa0a6e6cd65cb858499bb281d2dffc82d4c90e000c0cb6344f
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/be51fecdcf394a8888d48a9131a5b678/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/99302c91ae2ddee68ab6ea1c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: be51fecdcf394a8888d48a9131a5b678
completed-at: '2026-11-19T15:50:15Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/be51fecdcf394a8888d48a9131a5b678/outputs/review-compound-bullet.md
raw-output-sha256: a2ce5d077ea5f892e9fe621ecad0ff365e96f7ddaaa33f5461d12c9eebaadd52
format: 2
---

# Review

Most longer bullets in the note develop a single failure mode, architectural role, mechanism, or friction point with supporting elaboration and examples. Two bullets in the closing sections instead merge two separable points with em-dashes—one bundling two distinct scope exclusions with separate consequents, and one wedging a second open question inside the syntax of another. Splitting each into standalone bullets would keep both points visible during scanning.
