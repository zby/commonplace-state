---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: null
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews
launch: e40178eb1b0744768d92f2d8f1f6cce6
completed-at: '2026-11-19T13:44:23Z'
findings:
- scope: passage
  quotes:
  - '- **Tractability bias in global scans.** When a wide-shallow pass selects from
    compressed summaries, items with crisp scope and easy checks can look cleaner
    than messy, high-stakes bottlenecks, tilting allocation toward tractable low-value
    work.'
  - '- How can a global scan over compressed frontier items prevent tractable, well-specified
    tasks from crowding out harder, higher-stakes bottlenecks without re-introducing
    unbounded assessment cost?'
  reason: Asserts a separate directional selection-bias hypothesis—that summary-based
    scans tilt allocation toward tractable low-value work—without deriving it from
    bounded context or summary compression; unlike the other two interface frictions,
    this adds unargued attack surface akin to oracle/legibility asymmetry. Remove
    the asserted bullet from Residual friction and either rehome the hypothesis as
    a separate note/workshop lead or reframe the paired Open Question to ask whether
    and under what conditions compressed-summary scans induce tractability bias.
  level: warn
- scope: passage
  quotes:
  - '- **"This finding or answer should survive"** — durable retention so later runs
    do not re-ask the same question.'
  - an operator's answer to a stop can be recorded so the next run does not re-ask
  reason: Folds cross-run operator-answer persistence (an ADR 138 workflow-memory
    concern) into the execution-vs-triage split, whereas the note's own synthesis
    only requires preserving the worker's finding so stopping does not demand immediate
    operator action. Either narrow this point to durable finding retention for deferred
    triage or explicitly connect answer carry-over to preventing repeat re-escalation
    across stateless runs.
  level: info
contract: verdict
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/e40178eb1b0744768d92f2d8f1f6cce6/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/artifact/reviews/6624f421c78ddb21cb4165f0/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/e40178eb1b0744768d92f2d8f1f6cce6/outputs/review.md
raw-output-sha256: 2325d2d64421502b308d7b684528fe4eec9692c3ed2e447df2252c803efc8d9f
---

# Review

The note's core commitment is well-bounded: isolating an agent's context for task focus removes the live competing-work comparison set that global prioritization requires, workflow defaults turn that indiscrimination into priority flattening, and splitting narrow-deep execution from wide-shallow triage relocates the trade-off to the interface between views. Most sections—including the human-specialist contrast, the defense against static priority rules, the three Commonplace illustrations, and the Scope boundaries—directly serve that commitment.

The main branch bloat is the asserted tractability-bias friction in `## Residual friction at the interface`. The other two bullets in that section follow directly from the two-view split (compression hides local severity detail; within-episode branch choices still lack full global state). By contrast, claiming that global scans tilt allocation toward crisp, easily checked work introduces an unargued directional selection-bias mechanism—breaking the note's own earlier discipline that missing or compressed context causes indiscrimination while a separate mechanism sets direction. Because the note already carries a matching entry in `## Open Questions`, demoting the asserted bullet out of `Residual friction` (and reframing that open question so it does not presuppose the bias) or splitting tractability bias into its own note protects the main argument without losing the lead.

A smaller side concern enters where the three-decision unbundling and the ADR 138 illustration include retaining an operator's answer so later runs do not re-ask the same question. Persisting a worker's finding is part of decoupling a local stop from immediate operator interruption, whereas operator-answer carry-over is a cross-run workflow-memory detail unless explicitly tied back to preventing repeat escalation by stateless workers.
