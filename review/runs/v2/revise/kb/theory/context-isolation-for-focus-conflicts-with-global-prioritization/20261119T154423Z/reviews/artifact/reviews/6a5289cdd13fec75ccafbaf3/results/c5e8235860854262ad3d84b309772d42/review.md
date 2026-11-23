---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Solving a hard problem in a bounded LLM context pushes an agent system toward
    **context isolation**, because [context efficiency binds first on per-window feasibility](./context-efficiency-is-the-central-design-concern-in-agent-systems.md).
    Context isolation loads deep task-relevant material and excludes unrelated work
    so the task stays within the model''s usable attention budget. **Global prioritization**
    moves in the opposite direction: deciding how much effort a local branch deserves
    relative to other work, when to stop or defer on opportunity cost, and whether
    a blocker warrants interrupting scarce operator attention. Whenever the right
    decision changes as the operator''s other work changes—and no locally calibrated
    scale translates that competing work into a compact threshold—a worker that sees
    only its own task cannot reliably make that decision. Isolating an agent for task
    focus therefore removes the live comparison set that relational global prioritization
    requires.'
  reason: The opening paragraph delays the core claim until its final sentence behind
    feasibility setup, two definitions, and an inline caveat; leading with the claim
    plainly and defining the two terms in service of it makes the thesis immediately
    visible.
  level: warn
- scope: passage
  quotes:
  - 'This claim is narrower than saying isolated agents lack judgment. Isolation does
    not prevent **task-internal** technical assessment: the worker can still judge
    what breaks inside its loaded scope, how soon that local failure manifests, and
    whether deferring the local change is reversible within that scope—precisely the
    judgments a later reader without deep task detail cannot cheaply reconstruct.
    Cross-boundary blast radius, external deadlines, and external reversibility still
    depend on excluded state.'
  - '**Claim mode: universal** under three conditions: bounded effective context,
    a competing workload whose comparison-sufficient live summary cannot sit beside
    deep task context without degrading focus, and open-ended trade-offs lacking a
    locally calibrated common scale (such as a numeric latency budget or dollar cost)
    that would let a compact injected threshold stand in for competing tasks.'
  reason: Two full paragraphs of defensive narrowing and scope conditions sit immediately
    after the opening claim before the reader sees either the failure mechanism or
    the architectural split, duplicating material already carried in the execution-triage
    section and Scope.
  level: warn
- scope: document
  quotes: []
  reason: The same boundary conditions (summary load degrading focus; absence of a
    locally calibrated metric such as a latency budget or dollar cost) are restated
    five times across the body and Scope, and the non-corroboration caveat interrupts
    both the Nostalgebraist and Commonplace illustrations; folding repeated qualifications
    into a single Scope home keeps later sections subordinate to the main claim.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/c5e8235860854262ad3d84b309772d42/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/6a5289cdd13fec75ccafbaf3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: c5e8235860854262ad3d84b309772d42
completed-at: '2026-11-19T15:54:44Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/c5e8235860854262ad3d84b309772d42/outputs/review.md
raw-output-sha256: 1f542ec7820ec31a7104bdb4b9097b7e2e9a6d2b7a3001c277c45319c0cdd6ca
format: 2
---

# Review

## Core claim

Using only commitments the note already makes, its strongest claim is:

> Isolating an agent's context for deep task focus removes the live comparison set of competing work that relational global prioritization requires, forcing bounded-context systems either to accept uncalibrated local priority behavior or to split narrow-deep execution from wide-shallow triage across a lossy summary boundary.

The note already commits to this claim (it does not need a reconstructed stronger thesis), and its section arc—mechanism, architectural split, residual interface friction, scope, open questions—is sound. The problem is uptake: defensive qualification apparatus surrounds and interrupts the claim from the opening paragraph through the architectural payoff.

## Assessment and simplest restoration

Right now, the lead spends roughly 250 words on setup, definitions, narrowing, and a three-condition universal-claim formula before the reader encounters what breaks or what architecture follows, with the core sentence tucked at the end of paragraph 1. Worse, almost every caveat placed in the lead is re-litigated inside the mechanism and split sections—most visibly when the opening sentence of `## Splitting narrow-deep execution from wide-shallow triage` replays both boundary conditions before naming the narrow-deep/wide-shallow trade-off, and when inline evidential disclaimers break the momentum of the practitioner quote and Commonplace examples despite `## Scope` stating the same disclaimer once for both.

The simplest way to restore prominence is structural consolidation rather than new prose:

1. **Lead with the claim.** Open paragraph 1 with the conflict and its architectural consequence in one or two plain sentences, then define context isolation and global prioritization directly in support of that statement.
2. **State each boundary once where it earns its keep.** Remove the two post-claim qualification paragraphs from the lead: keep the task-internal judgment list inside narrow-deep execution (where it specifies what a stop record must capture), keep the locally-calibrated-scale distinction where it answers the injected-threshold objection, and hold the complete boundary conditions and non-corroboration caveat in `## Scope` (keeping a brief `Claim mode` note there or as a single concise line if required).
3. **Strip repeated hedges from section openings and examples.** Let `## Splitting narrow-deep execution from wide-shallow triage` open directly with the narrow-deep versus wide-shallow contrast, and drop the inline disclaimers from the Nostalgebraist and Commonplace passages so the illustrations serve the main thread cleanly.
