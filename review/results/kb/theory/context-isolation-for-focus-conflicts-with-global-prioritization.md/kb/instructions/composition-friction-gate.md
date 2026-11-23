---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/composition-friction-gate.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
criterion: kb/instructions/composition-friction-gate.md
criterion-sha256: 6e789a3c72156944d9b8f1322f23bbba3dec8f966da5a398c36cbea0c37230fc
outcome: report
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T184215Z/reviews
launch: a4f90806920547dd926a25f49219b701
completed-at: '2026-11-19T18:46:05Z'
findings:
- scope: passage
  quotes:
  - Inside a local frame, fixing a minor inconsistency or chasing a side question
    looks concrete and justified when competing higher-value work is absent from the
    window (and even the in-window primary task has no live opportunity-cost counterweight).
  reason: UNSUPPORTED — Excluding external competing work does not explain why a worker
    chases a low-value tangent instead of completing the primary task already loaded
    in its window. The parenthetical concedes that the in-window primary task fails
    to act as a counterweight, but supplies no context-isolation mechanism for why
    it fails, pointing instead to within-task salience or effort-valuation failure.
- scope: passage
  quotes:
  - 'In open-ended work without such a scale, a compressed cost signal is not comparable
    in local scope: the isolated worker cannot calibrate its local issue against an
    abstract bar, whereas a global view lets the agent compare concrete tasks side
    by side.'
  reason: UNSUPPORTED — Treating every compact live cost signal as an abstract scalar
    bar creates a false dichotomy and never rules out compact concrete reference anchors
    (such as brief descriptions of the current top competing tasks or marginal cutoff
    item) injected into the worker. The contrast also assumes the global view compares
    concrete tasks directly, whereas wide-shallow triage compares compressed summaries
    that the note later concedes can drop severity-bearing local detail.
- scope: passage
  quotes:
  - 'Because deep problem solving requires a **narrow-deep** context and relational
    global prioritization requires a **wide-shallow** comparison set, the two functions
    cannot share one bounded call once even a comparison-sufficient summary of competing
    work cannot sit beside deep task context without degrading focus—and no calibrated
    local threshold can replace side-by-side comparison. Separating them turns the
    conflict into an architectural interface between separate bounded calls, consistent
    with [bounded-context orchestration](./bounded-context-orchestration-model.md):'
  reason: UNSUPPORTED — The causal clause largely restates its conclusion by stipulating
    that even a comparison-sufficient summary of competing work degrades focus beside
    deep context, without establishing a regime where that summary is too heavy for
    the worker yet the full set of severity-preserving summaries fits in one wide-shallow
    triage call. Moving to separate calls also assumes an isolated worker can select
    scale-bearing local facts without seeing the external state that the note says
    governs cross-boundary blast radius, external deadlines, and external reversibility.
- scope: passage
  quotes:
  - A workflow that bundles local stopping with immediate operator action manufactures
    urgency even when the worker's local stop is sound. Unbundling them lets an unattended
    worker stop cleanly and preserve its finding without demanding immediate redirection
    or operator intervention—addressing one structural reason stopping and redirection
    degrade when interactive oversight is removed ([unattended work needs the functions
    that interaction supplied](./unattended-work-needs-the-functions-that-interaction-supplied.md)).
  reason: UNSUPPORTED — Separating a local stop from an immediate operator ping reduces
    escalation noise after a hard blocker already halts a run, which is an asynchronous
    notification choice rather than an effect of execution-triage separation. It does
    not explain or repair mid-run stopping on diminishing returns or redirection off
    low-value tangents, because the note leaves opportunity-cost stopping to triage
    and within-episode branch choices inside the local worker, where a tangent triggers
    no hard stop.
- scope: passage
  quotes:
  - That example also reflects weak absolute-stakes calibration, and the account does
    not isolate whether worker behavior or a workflow that turns every stop into an
    immediate ping made interruption the default; either way, removing competing work
    leaves the isolated worker without live relative urgency.
  reason: THIN — After conceding both weak absolute-stakes calibration and a possible
    ping-on-stop workflow default, the 'either way' bridge drops the causal claim
    that missing competing-work context accounts for the babysitting example's flattened
    urgency. It also sits in tension with the earlier claim that stateless isolated
    agents retain generic base-rate severity priors from pretraining, which should
    already separate a juice box from a bleeding finger without live competing tasks.
contract: report
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T184215Z/reviews/calls/launches/a4f90806920547dd926a25f49219b701/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T184215Z/reviews/artifact/reviews/bfb720b12e01c9f3fab2b2da/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T184215Z/reviews/calls/launches/a4f90806920547dd926a25f49219b701/outputs/review.md
raw-output-sha256: c3d5afd2d10ceaf09e8764aa0ae29a8666c8b5a6b9f2fd059dae49977d5269f2
---

# Friction check: Context isolation for focus conflicts with global prioritization

**Central claim (one sentence):** Under bounded effective context, when a comparison-sufficient live summary of competing work cannot sit beside deep task context without degrading focus and no locally calibrated common scale lets an injected threshold stand in for competing tasks, isolating an agent's context for task focus removes the live comparison set required for relational global prioritization.

## Filter

**Filter:** SURVIVES

The central claim commits to a single structural trade-off rather than demanding that deep task focus and full cross-task visibility coexist inside one call. Its execution/triage split likewise treats the conflict as relocated to the summary boundary rather than eliminated. What stays under-concretized is not an internal contradiction in the thesis, but whether the conditions that force the split and the cited failure modes are earned by the argument rather than stipulated into it.

## Thinnest joints

The five surfaced findings rank from most self-undermining to most hedged. The first finding is weakest because it appeals to missing external work while conceding that the already-loaded primary task fails to restrain tangents. The second and third findings carry the main architectural load: ruling out compact injected signals by reducing them to abstract scalar bars, then pivoting through a largely stipulative `Because` clause to a narrow-deep versus wide-shallow split whose summary-size regime and blind fact-selection remain unestablished. The fourth finding overclaims the downstream payoff for unattended stopping and redirection from what is mainly asynchronous escalation decoupling. The fifth finding ranks strongest of the surfaced set because the author explicitly hedges the confounding causes in the motivating example, leaving a narrowed restatement rather than an unflagged leap. Other explicit joints in the note—per-window feasibility pushing toward isolation, general slogans failing to rank unseen alternatives, and insufficient summaries forcing fallback or unsafe substitution—held up better under adversarial testing and sit above this cut.

## For the human

Look first at the second joint (compact injected signals) alongside the third (the narrow-deep versus wide-shallow pivot): concretize why a few concrete one-line anchors of competing tasks cannot sit beside deep task context, yet a full set of severity-preserving local summaries can sit together inside one triage pass—and separate in-window tangent-chasing (first joint) from missing external work.
