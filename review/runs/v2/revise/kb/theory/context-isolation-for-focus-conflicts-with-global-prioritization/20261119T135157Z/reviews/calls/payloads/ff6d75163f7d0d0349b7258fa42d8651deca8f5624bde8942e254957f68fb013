---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - '**Claim mode: universal** (under bounded effective context and a competing workload whose live state does not fit beside task-solving context). A system operating under those conditions whose isolated task workers reliably make decisions whose right answer depends on unseen competing work—or that loads full live portfolio state alongside deep task context without degrading execution competence—would refute the claim.'
    reason: 'Add the missing load-bearing condition—non-decomposability or incompressibility of global opportunity cost—and revise the refuter. Under the two stated conditions alone, isolated workers given a compact, dynamically updated sufficient statistic (a shadow price, live priority floor, or attention-cost threshold) reliably track changes in unseen competing work without loading the comparison set.'
  - scope: passage
    quotes:
      - 'Explicit static rules can eliminate *previously named* non-priorities and tolerances; they cannot supply live relative scale for novel trade-offs across a changing workload.'
    reason: 'Replace the false dichotomy between static generic rules and full live portfolio state by addressing compact dynamic global signals (live interruption bars, rolling bottleneck briefs, adjustable budgets) and reconciling them with the note’s own concessions on injected boundaries and within-episode compressed proxies.'
  - scope: passage
    quotes:
      - 'Because deep problem solving requires a **narrow-deep** context and global prioritization requires a **wide-shallow** comparison set, the two functions cannot live in the same bounded call once the combined state exceeds usable context.'
    reason: 'Treat execution–triage separation as a choice between two dual compression directions rather than a forced move to post-hoc wide-shallow triage: compressing local facts out to global triage (which risks hiding local emergencies) versus compressing global opportunity cost into isolated execution (which lets the worker judge uncompressed local facts against a live threshold), and state when each wins.'
  - scope: passage
    quotes:
      - '- **"This run should stop"** — a local execution judgment the isolated worker can make.'
    reason: 'Resolve the contradiction with the opening definition of global prioritization ("when to stop or defer it"): distinguish stopping on hard local invariants or explicit stop rules from discretionary stopping on tangents or diminishing returns, and separate absolute-stakes calibration failures ("juice box vs. bleeding finger", silly tangents) from relational competing-work conflicts.'
outcome: report
attack-outcome: lands
---

# Critique: Context isolation for focus conflicts with global prioritization

**Note:** kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
**Central commitment:** Under bounded effective context and a competing workload that cannot fit beside task-solving context, isolating an agent for task focus universally prevents it from reliably making global prioritization decisions, forcing a split between narrow-deep execution and wide-shallow triage.
**Critique mode:** claim
**Attack outcome:** lands

## Strongest case against it

**Stance:** Distributed optimization, operations research, and mechanism-design theorists (Hayekian price coordination, Lagrangian dual decomposition, and Gittins/Whittle index scheduling), together with distributed-systems architects who coordinate concurrent workers via live priority floors and dynamic budgets rather than centralized per-item triage.

**Reasoning:** Global prioritization across a large competing workload does not require the deciding worker to hold the live comparison set ("wide-shallow comparison set" or "full live portfolio state"). A foundational result across price theory, dual decomposition, and stochastic scheduling is that decentralized actors with strictly local state can make globally calibrated stopping, effort-allocation, and escalation decisions whenever the competing workload's marginal opportunity cost compresses into a low-dimensional live sufficient statistic—a **shadow price**, **dynamic priority floor**, or **live threshold** $\lambda(t)$.

An isolated worker needs only two inputs to decide whether a local branch warrants more effort or an operator interruption:

1. **Uncompressed local scale**—what will break, how soon, whether waiting is reversible, and what marginal effort buys—which the note itself concedes an isolated worker can assess (paragraph 2).
2. **A compact, dynamically updated global threshold**—for example, a live interruption bar ("operator is in P0 incident response: page only for irreversible data loss or blocked release; defer P1–P3"), a shifting compute/time budget, or a short rolling digest of the top active bottlenecks.

That threshold updates as the unseen competing workload changes, yet takes $O(1)$ tokens and fits inside a narrow-deep context window without degrading execution competence. This directly meets the note's own universal refutation condition: under bounded effective context and a competing workload too large to fit beside task context, isolated task workers *can* reliably make decisions whose right answer changes as unseen competing work changes.

Crucially, an opponent does not even have to claim that no external layer tracks the portfolio; computing or setting $\lambda(t)$ still happens outside the worker (whether via operator mode-setting, symbolic queue/SLA metrics, or a periodic coordinator pass). What collapses is both the universal impossibility claim and the architectural inference that global prioritization must move out to a post-hoc wide-shallow comparison pass over compressed local summaries. Instead, bounded context forces a **symmetric choice between two dual compression directions**:

- **Compress local state out to global triage** (the note's architecture): the worker emits brief scale-bearing facts and a wide-shallow pass compares items side-by-side—incurring the note's own "compression hides emergencies" failure whenever local severity cannot be captured cleanly in a summary.
- **Compress global state in to local execution** (the price/threshold dual): an external monitor compresses portfolio pressure into a compact live bar and injects it into the isolated worker, which evaluates **uncompressed** local detail against that bar.

Whenever local technical emergencies are harder to compress faithfully than the current global opportunity-cost bar—common in deep debugging, security review, and production engineering—pushing compressed global state into isolated execution outperforms pushing compressed local summaries out to global triage. The note's universal conflict therefore holds only under an unstated extra premise: that the competing workload is **non-decomposable or incommensurable**, such that no compact live threshold or priority rubric can summarize its opportunity cost for novel cross-task trade-offs.

## How the note engages it

**Partially engaged**—the note anticipates neighboring ideas but misses the refutation and its own internal tension:

- **Static-rule strawman (`Missing context causes indiscrimination`, final paragraph):** The note argues that *standing generic rules* ("focus on high-leverage work") and *explicit static rules* cannot track a changing workload. It never tests **dynamic, low-dimensional global signals** (live thresholds, shadow prices, rolling bottleneck summaries) that change with the workload without importing the comparison set.
- **Unreconciled concessions (`Splitting narrow-deep execution`, item 1; `Residual friction`, item 3; `Open Questions`, item 2):** The note concedes that isolated workers can assess local technical scale (paragraph 2), receive "explicit tolerances, and local stop conditions from outside," and rely on "whatever compressed proxy of global priority—intent, tolerances, concern depth, or budget—fits cheaply inside the local window." Yet it treats compressed global proxies only as an imperfect fallback for within-episode micro-prioritization, never recognizing that the same mechanism applies to escalation, stopping, and deferral and directly challenges the universal claim and the one-way push to post-hoc wide-shallow triage.
- **Missing scope condition (`Claim mode` and `Scope`):** Neither section restricts the claim to non-decomposable or non-priceable workloads where global opportunity cost cannot be compressed into a compact live statistic.

## Constructive findings

- Restrict the universal claim and its refutation condition to workloads whose global opportunity cost is **non-decomposable or incommensurable** (where novel cross-task trade-offs cannot be faithfully represented by a compact live threshold, priority floor, or shadow price).
- Close the gap between static generic rules and full portfolio loading by explicitly analyzing **compact dynamic global signals** and integrating the note's concessions on injected tolerances and compressed proxies into the main model rather than leaving them as residual footnotes.
- Reframe the execution–triage architecture as a **two-sided compression trade-off**—comparing compress-local-to-global triage against compress-global-to-local threshold injection—and state the conditions (rich local emergencies vs. incommensurable cross-task coupling) that favor each direction.
- Reconcile the stopping classification across the note (defining "when to stop or defer" as global prioritization in the opening, then treating `"This run should stop"` as a local execution judgment in the unbundling list) and cleanly separate absolute-stakes miscalibration from relational competing-work conflicts.

## Secondary objections

- **Causal misattribution of the motivating symptoms (absolute-stakes calibration vs. context isolation):** The note's flagship examples—Anthropic's "juice box vs. sliced finger" escalation flattening and Nostalgebraist's "silly low-value tangents"—are primarily failures of an internalized **absolute-stakes prior**, not missing visibility into competing work. An isolated human engineer with zero knowledge of concurrent projects still distinguishes a lint tangent or juice box from a bleeding finger, and Nostalgebraist observes the same trivia-chasing inside single-thread sessions where no multi-agent isolation exists. Although `Scope` restricts the claim to relational prioritization and marks the account as origin rather than corroboration, Section 1 still explains these absolute-stakes failures through missing portfolio visibility and attributes human restraint to an "ambient cross-project model." If model-side value calibration and weak discrimination drive these behaviors, a wide-shallow LLM triage pass inherits the same flattening.
- **Slippage on whether stopping is local or global:** Paragraph 1 places "when to stop or defer it" inside global prioritization, yet the unbundling section classifies `"This run should stop"` as a local execution judgment the isolated worker can make. Unbundling stop, durable retention, and immediate operator paging fixes notification plumbing—preventing every stop from acting as an emergency ping—but does not resolve how an isolated worker decides *whether* to stop digging on an open-ended branch versus continue without either burning effort on tangents or prematurely dumping work onto triage.
