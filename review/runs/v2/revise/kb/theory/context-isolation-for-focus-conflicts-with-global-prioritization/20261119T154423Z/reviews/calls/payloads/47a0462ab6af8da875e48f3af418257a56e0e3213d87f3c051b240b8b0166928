---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "In open-ended work without such a scale, a compressed cost signal is not comparable in local scope: the isolated worker cannot calibrate its local issue against an abstract bar, whereas a global view lets the agent compare concrete tasks side by side."
    reason: "Address the omitted middle case of live, concrete marginal anchors (a compact O(1) handoff of active bottlenecks and the 2-5 competing tasks at the current cutoff), which allow side-by-side concrete comparison without a numeric scale; show specifically when and why concrete marginal anchors fail rather than jumping from abstract scalar bars to a full wide-shallow view."
  - scope: passage
    quotes:
      - "a competing workload whose comparison-sufficient live summary cannot sit beside deep task context without degrading focus, and open-ended trade-offs lacking a locally calibrated common scale"
    reason: "Replace the question-begging second condition with non-circular structural conditions that actually block compact marginal anchoring—such as content-addressed cross-portfolio coupling, concurrent sibling-worker staleness, or empirically established attention interference—so the universal claim does not become true by stipulation while deferring its load-bearing premise to Open Question 2."
  - scope: passage
    quotes:
      - "On a small workload whose comparison-sufficient live state fits inside one usable window—or a separable workload whose opportunity cost reduces to a locally calibrated metric such as a dollar cap or latency budget—the conflict disappears or can be handled by injected thresholds."
    reason: "Revise the Scope boundary so it does not equate compact comparison-sufficient live state with a small workload; marginal opportunity-cost comparison scales with the cutoff frontier (O(1)), not total portfolio size (O(N)), so large open-ended workloads can still fall outside the conflict unless cross-portfolio coupling or concurrency defeats compact anchoring."
  - scope: passage
    quotes:
      - "When it encounters an out-of-scope defect, tangent, or decision boundary, it records **scale-bearing local facts** on a shared surface or in a structured stop record."
    reason: "Address the selection circularity at the execution-triage interface: because cross-boundary blast radius and external deadlines depend on excluded state, an isolated worker cannot reliably identify which local facts are globally scale-bearing without receiving compact global relevance cues."
  - scope: passage
    quotes:
      - "Inside a local frame, fixing a minor inconsistency or chasing a side question looks concrete and justified when competing higher-value work is absent from the window (and even the in-window primary task has no live opportunity-cost counterweight)."
    reason: "Separate context-isolation crowding from distinct mechanisms in the motivating examples: chasing tangents against an already in-window primary task reflects local effort-budgeting failure rather than excluded external work, and parallel workers' simultaneous uncalibrated escalations reflect concurrent-snapshot staleness and weak absolute-stakes calibration."
outcome: report
attack-outcome: lands
---

# Critique: Context isolation for focus conflicts with global prioritization

**Note:** kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
**Central commitment:** Under bounded effective context and open-ended trade-offs lacking a locally calibrated common scale, isolating an agent's context for deep task focus structurally removes the live comparison set required for relational global prioritization, forcing architectures to separate narrow-deep execution from wide-shallow triage.
**Critique mode:** claim
**Attack outcome:** lands

## Strongest case against it

**Stance:** A decision-theoretic agent-systems designer who treats decentralized prioritization as comparison against the *marginal alternative*, not visibility of the full portfolio.

The note builds its structural conflict on a false dichotomy between full-portfolio visibility and uncalibratable proxies, then immunizes the resulting universal claim with a question-begging condition.

1. **The missing middle case: live concrete marginal anchors scale as O(1), not O(N).**
   To decide whether a local branch merits further effort or whether a blocker merits interrupting the operator, an isolated worker does not need to see all $N$ competing tasks in the portfolio. By basic opportunity-cost reasoning, a binary invest/defer or escalate/log choice only requires comparing the local issue against the **marginal competing benchmark**—the 2–5 concrete tasks currently occupying the operator's attention or sitting just above the current priority cutoff (for example: active production outage, Friday release blocker, current top backlog item, plus concrete recent examples of log-and-defer issues).
   - Unlike standing generic rules ("do not escalate trivia"), a live marginal anchor card updates as competing work changes.
   - Unlike an abstract scalar bar ("only escalate above priority 8/10"), concrete competing tasks require **no numeric common scale**: the worker compares its concrete local blocker side-by-side against concrete competing tasks right inside its prompt.
   - Unlike a full portfolio summary, 3–5 concrete marginal anchors take a few hundred tokens—O(1) in portfolio size—so they fit easily beside deep task context even on a very large workload.

   In the body, the note rejects static rules and abstract scalar thresholds, then leaps directly to the conclusion that only a separate wide-shallow pass can "compare concrete tasks side by side." Its Scope section reinforces the same error by asserting that comparison-sufficient live state fits beside task context only "on a small workload." Both claims fail against O(1) concrete marginal anchors.

2. **The tautology-versus-reach dilemma in the universal claim.**
   The author might reply that whenever a 300-token marginal anchor card suffices without degrading focus, Condition 2 of the universal claim ("a competing workload whose comparison-sufficient live summary cannot sit beside deep task context without degrading focus") simply does not hold. That defense traps the note in a destructive fork:
   - **Horn A (retreat to Condition 2 → near-tautology):** If Condition 2 stipulates that no comparison-sufficient live summary can sit beside deep task context without degrading focus, and Condition 3 stipulates that no compact threshold substitutes for it, then "isolating for focus conflicts with global prioritization" follows almost by definition. The real empirical and architectural question—*what makes a compact comparison-sufficient summary impossible or focus-degrading?*—is assumed away in the premise and punted to Open Question 2.
   - **Horn B (keep explanatory reach → unsubstantiated):** If the note claims that real coding-agent and KB workloads actually satisfy Condition 2 (explaining Nostalgebraist's tangents, Anthropic's babysitting, and Commonplace's workflows), it supplies no argument that a few hundred tokens of concrete active priorities would either fail to be comparison-sufficient or degrade focus. In the cited practitioner workflows, workers received *zero* live priority anchors; the evidence never tests context-window crowding against compact marginal anchoring.

A genuine conflict between isolation and global prioritization still exists in narrower regimes—specifically **content-addressed cross-portfolio coupling** (where which of $N$ other tasks is relevant depends on what the worker discovers mid-run, defeating a fixed O(1) anchor set), **concurrent multi-worker arbitration** (where sibling workers discover competing blockers simultaneously after handoff, which is snapshot staleness rather than context-window crowding), and any regime where even tiny off-task priority headers demonstrably cause **attention interference**. But the note neither identifies nor restricts its universal claim to those regimes.

## How the note engages it

**partially engaged.** The note explicitly acknowledges the boundary of compact injected summaries in Condition 2 (line 14), Scope (line 58), and Open Question 2 (line 66, asking how much compressed global state—including "active bottlenecks"—can be injected before context load degrades task solving). However, its core argument never engages **live concrete marginal anchors**: line 26 argues only against static standing rules and abstract scalar cutoffs, assuming concrete side-by-side comparison requires a separate wide-shallow view, and line 58 equates fitting comparison-sufficient live state with having a "small workload." Because the note leaves the feasibility and calibratability of injected active bottlenecks unanswered in Open Question 2 while treating their failure as settled in lines 14, 26, and 58, the objection lands against the central commitment as formulated.

## Constructive findings

- **Close the dichotomy in line 26 against live concrete marginal anchors.** Explicitly compare wide-shallow triage against injecting an O(1) live card of concrete active bottlenecks and cutoff tasks, and state the concrete conditions under which concrete marginal anchors fail (rather than only ruling out static rules and abstract numeric thresholds).
- **Replace Condition 2 (line 14) with non-circular structural triggers.** State what actually prevents a compact live summary from being comparison-sufficient or focus-preserving—for example, content-addressed cross-portfolio coupling (where relevant competing work cannot be chosen before local discovery), concurrent sibling-worker staleness, or empirical attention distraction—instead of stipulating that no comparison-sufficient summary fits without degrading focus.
- **Correct the "small workload" boundary in Scope (line 58).** Distinguish workload cardinality ($N$) from marginal-frontier complexity: a large workload with a simple active priority frontier admits O(1) concrete anchors, whereas a moderately sized workload with dense cross-task coupling or simultaneous parallel workers may not.
- **Resolve the interface circularity around "scale-bearing local facts" (lines 12, 32, 53).** Explain how an isolated worker that cannot see cross-boundary blast radius or external deadlines can reliably decide which local facts to preserve in a compressed stop record without already receiving compact global relevance cues.
- **Tighten the causal attribution in the motivating examples (lines 20–24).** Separate failures caused by excluding external competing work from (a) local effort-budgeting failures against an already in-window primary task (earnest tangents) and (b) concurrent-snapshot staleness plus weak absolute-stakes calibration across parallel workers (babysitting escalation).

## Secondary objections

- **Selection circularity at the narrow-deep / wide-shallow interface (lines 12, 32, 53).** The note frames dropped emergencies in triage as a lossy-compression problem ("compression hides emergencies") while prescribing that isolated workers record "scale-bearing local facts." Yet line 12 concedes that cross-boundary blast radius, external deadlines, and external reversibility depend on excluded state. In coupled work, which local fact is scale-bearing is observer-relative to the excluded portfolio—a minor schema quirk is trivia unless another active branch depends on it. An isolated worker therefore lacks the context not only to rank an issue, but to select which local facts to emit in its summary or which side-finding warrants logging at all.
- **Motivating practitioner failures do not isolate context-crowding (lines 20–24, 54).** Two of the three failure patterns cited in Section 2 point to mechanisms other than context-window limits. For earnest low-value tangents, the note concedes in a parenthetical that "even the in-window primary task has no live opportunity-cost counterweight"—meaning the agent fails to prioritize against work that *is* already loaded, and splitting execution from triage leaves within-episode micro-prioritization unsolved (line 54). For parallel babysitting escalations, simultaneous blockers across concurrent workers cannot be reconciled inside any single worker even with infinite context, because sibling discoveries do not exist at handoff time; that is a concurrency-barrier problem compounded by weak absolute-stakes calibration ("juice box vs. sliced finger"), not a focus-versus-context-capacity conflict.
