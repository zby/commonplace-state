---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Inside one module or diff, guarding a hypothetical edge case looks prudent when
    system-wide complexity budgets and accepted product tolerances are absent
  reason: UNSUPPORTED — Offered as one of three ways the missing live comparison set
    surfaces, this premise cites absent system-wide complexity budgets and accepted
    product tolerances—standing design rules rather than changing competing work.
    The note itself states two lines later that explicit static rules can encode known
    tolerances and injects explicit tolerances into the isolated worker, so this fails
    to establish that local over-specification stems from removing the live competing-work
    comparison set.
- scope: passage
  quotes:
  - Inside a local frame, fixing a minor inconsistency or chasing a side question
    looks concrete and justified when competing higher-value work is absent from the
    window (and even the in-window primary task has no live opportunity-cost counterweight).
  reason: UNSUPPORTED — Absence of out-of-window competing work does not establish
    why an isolated worker diverts effort from an in-window primary task to a minor
    inconsistency or silly low-value tangent. Comparing a side question against the
    primary task already loaded in the window is a task-internal choice; the parenthetical
    assertion that the in-window primary task itself lacks an opportunity-cost counterweight
    without outside work is asserted without support.
- scope: passage
  quotes:
  - 'Injected cutoffs work when the local task and the global signal share a locally
    calibrated scale—for instance, a numeric latency budget, token cap, or metered
    dollar cost that the worker can evaluate directly. In open-ended work without
    such a scale, a compressed cost signal is not comparable in local scope: the isolated
    worker cannot calibrate its local issue against an abstract bar, whereas a global
    view lets the agent compare concrete tasks side by side.'
  reason: UNSUPPORTED — Ruling out numeric cutoffs in open-ended work does not establish
    that no compact live signal can calibrate local choices. The inference equates
    any compressed non-numeric signal with an unanchored abstract bar, ignoring compact
    concrete reference anchors—such as a brief description of the current marginal
    competing task or active P0 bottleneck—that fit beside deep task context without
    degrading focus and allow concrete side-by-side comparison.
- scope: passage
  quotes:
  - 'When it encounters an out-of-scope defect, tangent, or decision boundary, it
    records **scale-bearing local facts** on a shared surface or in a structured stop
    record. Those are the task-internal judgments its deep context uniquely supports:
    what breaks inside its loaded scope, how soon that local failure manifests, whether
    waiting is reversible locally, whether the main path is blocked, and which local
    branch or assumption would change.

    2. **Wide-shallow triage (global comparison without execution detail).** A separate
    pass—an operator, coordinator, or dedicated triage call (preceded by filtering
    or indexing when a portfolio is too large for one pass)—reads compressed summaries
    of competing items side-by-side against current bottlenecks without loading deep
    task context for any single item. It decides which items earn execution effort,
    which wait on a named wake-up event, and which warrant operator attention now.'
  reason: 'THIN — Listing five task-internal facts does not establish that wide-shallow
    triage can reliably decide allocation and escalation without loading deep context.
    The note''s own second paragraph concedes that cross-boundary blast radius, external
    deadlines, and external reversibility depend on excluded state: when severity
    is a joint property of deep local detail and external dependencies, neither the
    isolated worker nor wide-shallow triage holds both halves, and the worker cannot
    know which local details are scale-bearing for unseen bottlenecks. In addition,
    how soon a failure manifests and whether waiting is reversible often depend on
    external callers or release schedules, and pre-triage filtering on large portfolios
    reintroduces the same compression trade-off unexamined.'
- scope: passage
  quotes:
  - A workflow that bundles local stopping with immediate operator action manufactures
    urgency even when the worker's local stop is sound. Unbundling them lets an unattended
    worker stop cleanly and preserve its finding without demanding immediate redirection
    or operator intervention—addressing one structural reason stopping and redirection
    degrade when interactive oversight is removed
  reason: THIN — Unbundling local stopping from immediate operator action establishes
    how to avoid false-alarm escalation after a sound local stop triggered by a hard
    blocker or pre-injected stop rule, but does not establish how it addresses redirection
    or stopping on diminishing returns and tangents when no hard blocker fires. The
    note assigns diminishing-returns stopping to triage rather than the worker, yet
    provides no mechanism by which unbundling prompts triage to interrupt or redirect
    a running worker that never self-stops.
outcome: report
description: Retained report review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/composition-friction-gate.md
contract: report
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/composition-friction-gate.md
note-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/72fc9b78ccee472eac825eebccbeacdf/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/8e44d3857b4cfcc93d94f94f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: 72fc9b78ccee472eac825eebccbeacdf
completed-at: '2026-11-19T15:59:39Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/72fc9b78ccee472eac825eebccbeacdf/outputs/review.md
raw-output-sha256: 36660a1d99c7628eaa43ceace2acfcc82c8d6fadb5edd59ed3f46f5bedde9536
format: 2
---

# Friction check: Context isolation for focus conflicts with global prioritization

**Central claim (one sentence):** Under bounded effective context, open-ended trade-offs lacking a locally calibrated common scale, and a competing workload whose comparison-sufficient live summary degrades focus if co-loaded with deep task material, isolating an agent's context for task focus removes the live comparison set required for relational global prioritization, pushing workflows to split narrow-deep execution from wide-shallow triage while relocating friction to summary compression and local micro-prioritization.

## Filter
**Filter:** SURVIVES

The claim asks for a consistent set of properties to hold together: deep task solving requires excluding competing work under bounded usable attention, relational prioritization requires comparing against live competing work when no locally calibrated scale stands in for it, and splitting execution from triage relocates rather than eliminates the trade-off. Because the note explicitly narrows its scope to relational prioritization under those three conditions and treats interface compression and local micro-prioritization as residual costs rather than solved problems, concretizing the claim yields one coherent structural tension rather than incompatible commitments.

## Thinnest joints

The note's core deductive spine holds under skeptical review: per-window feasibility pressure motivating exclusion of unrelated work, the analytic consequence that excluding competing work removes the live comparison set, the distinction between missing context causing indiscrimination and defaults setting failure direction, the failure of purely comparative standing priority rules on unseen alternatives, and the application of insufficient-summary fallback to lossy blocker records all earn their connectives.

The five surfaced findings rank from outright inferential disconnects (`UNSUPPORTED`) to partially supported architectural leaps (`THIN`). The first two findings sit in the empirical-symptom section and are thinnest on direct logical support: the first conflates omitted static tolerances (which the note itself later permits inside isolated workers) with missing live competing work, and the second blames absent external work for a worker abandoning an in-window primary task for a tangent. The third finding is also `UNSUPPORTED` and is structurally the most load-bearing for the main thesis: it rules out compact live external signals in open-ended work only by narrowing them to abstract scalar bars, leaving compact concrete benchmark anchors unexamined. The fourth and fifth findings rate `THIN` rather than `UNSUPPORTED` because the note partially qualifies them elsewhere (noting compression failure, open questions on minimal local facts, and the triage boundary for diminishing-returns stops), yet the architectural split still leaves cross-boundary severity detection and redirection of non-stopping workers under-established.

## For the human

Look first at Finding 3 (line 26): concretize why an external monitor in open-ended work cannot inject a compact concrete reference anchor (such as a two-line description of the current marginal competing task or active bottleneck) alongside deep task context, since that premise carries the necessity of separating triage from execution.
