---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/sentence/clause-packing.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion: kb/instructions/review-gates/sentence/clause-packing.md
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
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
  - '**Claim mode: universal** under three conditions: bounded effective context,
    a competing workload whose comparison-sufficient live summary cannot sit beside
    deep task context without degrading focus, and open-ended trade-offs lacking a
    locally calibrated common scale (such as a numeric latency budget or dollar cost)
    that would let a compact injected threshold stand in for competing tasks.'
  reason: 56 words packing the claim mode with three multi-clause conditions; in the
    third condition, a 9-word parenthetical interrupts the noun phrase 'a locally
    calibrated common scale' before its relative clause 'that would let...'. Move
    the parenthetical to the end of the condition or split the conditions into separate
    sentences or bullets.
  level: warn
- scope: passage
  quotes:
  - That example also reflects weak absolute-stakes calibration, and the account does
    not isolate whether worker behavior or a workflow that turns every stop into an
    immediate ping made interruption the default; either way, removing competing work
    leaves the isolated worker without live relative urgency.
  reason: 45 words chaining four clauses across three distinct points (a second confound,
    an attribution caveat, and the takeaway), with a 9-word relative clause ('that
    turns every stop into an immediate ping') separating the compound subject from
    its verb ('made'). Reorder the 'whether' clause so the verb comes before the long
    modifier and split the 'Either way' conclusion into its own sentence.
  level: warn
- scope: passage
  quotes:
  - Inside one module or diff, guarding a hypothetical edge case looks prudent when
    system-wide complexity budgets and accepted product tolerances are absent, compounding
    the oracle asymmetry—tests reward a present guard but rarely penalize an unneeded
    one—analyzed in [a guard against a conjectured requirement removes the experiment
    that would test it](./a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md).
  reason: 54 words chaining the local framing, missing global budgets, compounding
    of oracle asymmetry, a 10-word parenthetical definition, and the citation; the
    em-dash gloss separates 'the oracle asymmetry' from 'analyzed in [...]'. Move
    the gloss after the citation ('analyzed in [...], where tests reward...') or split
    the compounding clause into a second sentence.
  level: warn
- scope: passage
  quotes:
  - Because deep problem solving requires a **narrow-deep** context and relational
    global prioritization requires a **wide-shallow** comparison set, the two functions
    cannot share one bounded call once even a comparison-sufficient summary of competing
    work cannot sit beside deep task context without degrading focus—and no calibrated
    local threshold can replace side-by-side comparison.
  reason: '52 words chaining five clauses: two causal premises, the main conclusion,
    and two trailing scope conditions (the last tacked on after an em-dash). Splitting
    the scope conditions into a second sentence preserves every relation while cutting
    working-memory load.'
  level: warn
- scope: passage
  quotes:
  - A separate pass—an operator, coordinator, or dedicated triage call (preceded by
    filtering or indexing when a portfolio is too large for one pass)—reads compressed
    summaries of competing items side-by-side against current bottlenecks without
    loading deep task context for any single item.
  reason: 43 words with a 20-word em-dash appositive containing a nested 11-word parenthetical
    separating the subject ('A separate pass') from its verb ('reads'). Move the actor
    list and portfolio-filtering qualification after the main clause or into a second
    sentence.
  level: warn
- scope: passage
  quotes:
  - 'Isolation does not prevent **task-internal** technical assessment: the worker
    can still judge what breaks inside its loaded scope, how soon that local failure
    manifests, and whether deferring the local change is reversible within that scope—precisely
    the judgments a later reader without deep task detail cannot cheaply reconstruct.'
  reason: 47 words joining the scope narrowing, a three-item enumeration, and a downstream-cost
    corollary via both a colon and a trailing em-dash. Splitting at the em-dash ('Those
    are precisely the judgments...') trims peak load without losing meaning.
  level: info
contract: verdict
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1afb04a7210a42f6880d821b817ed06e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/1c9f7e0a2109e14c8f995d0c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1afb04a7210a42f6880d821b817ed06e/outputs/review-clause-packing.md
raw-output-sha256: 66e5640af48288682f885fc4e48b25361e92e86ca47f28ea39deebd16e7638b4
---

# Review

Most of the note uses crisp, well-paced sentences, but five sentences exceed 40 words while packing multiple revision-style qualifiers or opening long syntactic interruptions (including a 20-word appositive-plus-parenthetical between subject and verb in the wide-shallow triage paragraph, and 9–10 word interruptions inside noun-modifier and subject-verb dependencies elsewhere). Reordering the interrupting material or splitting the trailing scope qualifiers resolves each case without dropping any condition or relation.
