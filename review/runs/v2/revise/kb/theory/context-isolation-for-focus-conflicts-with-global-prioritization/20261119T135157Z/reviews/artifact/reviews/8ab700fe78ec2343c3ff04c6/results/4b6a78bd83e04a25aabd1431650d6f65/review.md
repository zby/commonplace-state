---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Because deep problem solving requires a **narrow-deep** context and global prioritization
    requires a **wide-shallow** comparison set, the two functions cannot live in the
    same bounded call once the combined state exceeds usable context.
  reason: DEFEATED — Universal premise that relational global prioritization requires
    loading a wide-shallow comparison set of competing items rather than a compact
    live sufficient statistic — In separable, commensurable workloads (price-directed
    / Lagrangian shadow pricing, Gittins-index scheduling, or a live SLA interrupt
    bar), a deterministic queue tracker can compress the live opportunity cost of
    hundreds of competing tasks into a ~10-20 token live scalar threshold injected
    into the isolated worker (no larger than the local tolerances the note already
    allows), letting the worker reliably shift escalation and effort decisions as
    unseen competing work changes without loading the comparison set or degrading
    focus; the conflict requires incommensurable or semantically coupled trade-offs
    whose opportunity cost does not compress to a compact live statistic — GLOBAL
    — instance
- scope: document
  quotes: []
  reason: 'DOUBTFUL — Unstated universal premise bridging the Scope condition (the
    competing workload''s full live state does not fit beside task-solving context)
    to the impossibility of co-locating execution and triage: that whenever full live
    portfolio state overflows usable context, the compressed wide-shallow summary
    sufficient for triage also cannot fit beside deep task context without degrading
    execution competence — On a 5-15 project workload, full live state (codebases,
    diffs, logs, threads) overflows a deep task window while a ~500-token live table
    of active priorities and bottlenecks (the exact compressed view Section 2 relies
    on for triage) adds minimal token share; unless small unrelated summaries cause
    harmful semantic distraction independent of token fit (unargued here), the stated
    condition is too weak to force the conflict — GLOBAL — instance'
- scope: passage
  quotes:
  - '**"This run should stop"** — a local execution judgment the isolated worker can
    make.'
  reason: DEFEATED — Universal premise that deciding whether the current run should
    stop is a purely local execution judgment available to an isolated worker — On
    non-blocked work with diminishing returns (e.g., whether to test a fourth debugging
    hypothesis or refine a working draft further when no hard invariant or explicit
    budget limit has fired), optimal stopping depends directly on the opportunity
    cost of unseen competing work, contradicting the note's own definition of global
    prioritization as deciding when to stop or defer a branch; only hard-blocker or
    externally bounded stops are purely local — LOCAL — instance
- scope: passage
  quotes:
  - 'Isolation does not prevent local technical assessment: the worker can still judge
    what will break, how soon, and whether waiting is reversible—precisely the judgments
    a later reader without deep task detail cannot cheaply reconstruct.'
  reason: DEFEATED — Universal premise that an isolated worker can reliably assess
    what will break, how soon, and whether waiting is reversible from deep task context
    alone — When a worker isolated to one module modifies a shared interface or detects
    a behavioral/performance regression, knowing which downstream callers will break,
    how soon (given external deployment schedules or traffic shifts), and whether
    waiting is reversible (whether concurrent branches will lock in incompatible dependencies)
    depends on cross-project state outside its window; isolation preserves only strictly
    task-internal checks, not cross-boundary blast radius or external reversibility
    — LOCAL — instance
- scope: passage
  quotes:
  - A stateless, isolated agent has no ambient comparison set outside what its window
    holds.
  reason: DEFEATED — Universal premise that a stateless isolated agent lacks any ambient
    comparison set outside its current context window — Pretrained and post-trained
    weights encode substantial generic base-rate severity priors (e.g., ranking a
    production credential leak or data loss far above a docstring typo, or a bleeding
    finger above an unopened juice box) even with zero competing tasks in context;
    what a stateless worker lacks is a live, project-specific comparison set (current
    bottlenecks, deadlines, and operator queue), not any ambient comparison scale
    — LOCAL — instance
- scope: passage
  quotes:
  - The *direction* of the failure comes from the workflow's or policy's default action
    when relative priority is unknown.
  reason: DOUBTFUL — Universal premise that the directional skew of prioritization
    failure (over-escalation and tangents vs. silent suppression) is determined by
    the workflow's or policy's default action under unknown priority — Even under
    symmetric action channels (explicitly offering silent deferral alongside immediate
    escalation) and a conservative escalation policy, an LLM immersed in deep local
    context can still skew systematically toward earnest tangents or over-escalation
    via local-context salience bias, RLHF thoroughness/caution bias, or verification-oracle
    asymmetry (unless 'policy' is stretched to encompass the model's own learned behavioral
    weights rather than workflow rules) — LOCAL — instance
- scope: passage
  quotes:
  - A separate pass—an operator, coordinator, or dedicated triage call—reads compressed
    summaries of competing items side-by-side against current bottlenecks without
    loading deep task context for any single item. It decides which items earn execution
    effort, which wait on a named wake-up event, and which warrant operator attention
    now.
  reason: DOUBTFUL — Architectural premise (partially qualified by the Residual friction
    section) that competing items compress cleanly enough to be compared side-by-side
    in one wide-shallow triage pass without routinely collapsing back into deep context
    — At large portfolio scales (hundreds or thousands of active issues, PRs, or frontier
    entries), even minimal summaries exceed a single bounded call's usable attention
    budget, reproducing the same per-window feasibility limit inside triage and forcing
    hierarchical pre-filtering or non-LLM indexing; in addition, when severity depends
    on subtle cross-detail interactions, triage must repeatedly fall back to deep
    context — LOCAL — instance
- scope: passage
  quotes:
  - 'Solving a hard problem in a bounded LLM context pushes an agent system toward
    **context isolation**: load deep task-relevant material and exclude unrelated
    work so the task stays within the model''s usable attention budget, because [context
    efficiency binds first on per-window feasibility](./context-efficiency-is-the-central-design-concern-in-agent-systems.md).'
  reason: 'HOLDS — Conditioned premise (under bounded effective context and a competing
    workload whose live state exceeds remaining capacity beside deep task context)
    that per-window feasibility forces excluding the full competing workload from
    the solving call — Active counterexample hunt found no defeater once the combined-state
    overflow condition holds: pulling full competing state into the solving window
    via tools still overflows effective attention for subsequent reasoning unless
    spun off into a separate bounded frame, which preserves isolation'
- scope: passage
  quotes:
  - Explicit static rules can eliminate *previously named* non-priorities and tolerances;
    they cannot supply live relative scale for novel trade-offs across a changing
    workload.
  reason: 'HOLDS — Universal premise (scoped to static standing rules and novel trade-offs
    under an unseen changing workload) that fixed priority prose cannot supply live
    relative scale — Active counterexample hunt found no defeater: a rule written
    prior to workload changes carries zero information about subsequent unseen changes
    for unenumerated trade-offs, and adding a live query tool ceases to be a static
    rule'
outcome: report
description: Retained report review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/reviews/calls/launches/4b6a78bd83e04a25aabd1431650d6f65/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/reviews/artifact/reviews/8ab700fe78ec2343c3ff04c6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/reviews
launch: 4b6a78bd83e04a25aabd1431650d6f65
completed-at: '2026-11-19T13:59:39Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/reviews/calls/launches/4b6a78bd83e04a25aabd1431650d6f65/outputs/review.md
raw-output-sha256: 8dd7abc11be80f1cd098b77418a44109176b49b7e94cb5429a49c0764645da28
format: 2
---

# Premise decomposition: Context isolation for focus conflicts with global prioritization

**Register:** claim
**Central commitment (one sentence):** Under bounded effective context and a competing workload whose live state does not fit beside deep task-solving context, isolating an agent's context for task focus removes the live comparison set required for relational global prioritization, preventing both functions from operating reliably within the same bounded call.

## Premises and counterexamples

The argument decomposes into three layers of load-bearing premises:

1. **The conflict core (what forces isolation and what global prioritization requires).** The note combines a capacity premise (excluding full competing state to preserve per-window feasibility) with two strong information-structure premises: explicitly, that relational global prioritization requires a wide-shallow comparison set of competing items; and implicitly, that whenever the *full* live portfolio state fails to fit beside deep task context, the *compressed* portfolio summary sufficient for triage also fails to fit (or degrades focus). The capacity premise holds within its stated overflow condition, as does the corollary that *static* priority rules cannot track changing unseen workloads. Both information-structure premises fail globally as stated: price-directed / sufficient-statistic allocation (Lagrangian shadow prices, Gittins cutoffs, live SLA bars) eliminates the need for a wide-shallow comparison set on separable, commensurable workloads, and small-to-medium portfolios can overflow in *full* live state while fitting easily in *compressed* summary form. Together, these show that the conflict requires stricter conditions than the note states: unpriced/incommensurable (or semantically coupled) trade-offs whose *comparison-sufficient summary* still overflows or distracts the deep task window.
2. **The failure-mode diagnosis (why isolated workers flatten priority and skew toward urgency/tangents).** The note supports its conflict with two diagnostic premises: that stateless isolated workers have no ambient comparison set at all outside their window, and that workflow/policy defaults set the direction of failure. Both overreach locally: pretrained weights retain generic base-rate severity priors (only *live, project-specific* comparison state is absent), and model-level salience or thoroughness biases can skew failure direction even under symmetric workflows and conservative escalation policies.
3. **The architectural boundary and two-view split (what isolated workers can still judge and what wide-shallow triage can decide).** To keep the claim narrow and constructive, the note relies on three boundary premises: that isolated workers can still assess what will break, how soon, and whether waiting is reversible; that "this run should stop" is a purely local execution judgment; and that a single wide-shallow pass can compare compressed summaries side-by-side. The first two are defeated locally—cross-boundary blast radius/reversibility and non-blocked optimal stopping both depend on unseen external state—while the third is dented at large portfolio scale where even compressed summaries overflow a single triage window. None of these three overturns the core conflict (the first two actually widen the scope of what isolation impairs), so they route locally to the boundary and split sections.

## For the human

Look first at the global defeat of the wide-shallow comparison-set premise (line 30): under separable, commensurable workloads, a ~10-20 token live shadow price, Gittins cutoff, or dynamic SLA threshold lets an isolated worker track unseen competing work without loading the comparison set—so the central commitment needs rescoping to incommensurable or semantically coupled trade-offs whose comparison-sufficient summary cannot fit beside deep task context.
