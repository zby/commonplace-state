---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "**Claim mode: universal** (under bounded effective context and a competing workload whose live state does not fit beside task-solving context). A system operating under those conditions whose isolated task workers reliably make decisions whose right answer depends on unseen competing work—or that loads full live portfolio state alongside deep task context without degrading execution competence—would refute the claim."
    reason: "UNSUPPORTED — Neither disjunct of the stated falsifier can actually obtain under the stated conditions. Reliably making decisions whose right answer varies with unseen competing work is information-theoretically impossible by definition, and loading full live portfolio state without degrading execution competence violates the precondition that the live state does not fit beside task-solving context. Framing the test around full portfolio state insulates the claim tautologically while leaving unestablished why a compact live priority proxy (such as active bottlenecks, budgets, or marginal escalation thresholds—which the note itself invokes later) cannot fit inside the execution window."
  - scope: passage
    quotes:
      - |-
        Crucially, this split unbundles three decisions that naive agent workflows collapse into one:

        - **"This run should stop"** — a local execution judgment the isolated worker can make.
        - **"This finding or answer should survive"** — durable retention so later runs do not re-ask the same question.
        - **"The operator should act now"** — a global allocation judgment that depends on competing work.
    reason: "UNSUPPORTED — Treating 'This run should stop' as a local execution judgment the isolated worker can make contradicts the opening definition of global prioritization as including 'when to stop or defer it' (and the later concession that 'when to stop digging' remains bounded by global priority proxies). Only hard or pre-injected local stops are locally determinable; stopping a diminishing-returns branch or tangent is an opportunity-cost decision the isolated worker lacks. In addition, splitting narrow-deep execution from wide-shallow triage does not itself unbundle durable retention ('This finding or answer should survive'), which is an orthogonal persistence policy rather than a consequence of separating the two views."
  - scope: passage
    quotes:
      - "When it encounters an out-of-scope defect, tangent, or decision boundary, it supplies the local judgments its deep context uniquely supports—**scale-bearing local facts** such as what will break, how soon, whether waiting is reversible, whether the main path is blocked, and what decision would change—recorded on a discoverable surface or in a typed stop record."
    reason: "UNSUPPORTED — Deep local task context does not by itself establish 'how soon' something will break, 'whether waiting is reversible', or 'what decision would change'. Time-to-failure and reversibility of waiting routinely depend on external release schedules, downstream consumers, concurrent branches, or deadlines excluded by isolation, and knowing which local facts are scale-bearing depends on the unseen competing bottlenecks. The note later acknowledges that compression drops severity-critical details and leaves the minimal fact set as an open question, so asserting that isolated workers reliably supply these judgments does not support the handoff interface."
  - scope: passage
    quotes:
      - "Inside a local frame, fixing a minor inconsistency or chasing a side question looks concrete and justified because the displaced higher-value work is absent from the window."
    reason: "UNSUPPORTED — The absence of unseen competing work from the window does not establish why fixing a minor inconsistency or chasing a side question looks justified. Inside a task-scoped session, the worker's own assigned primary task is already in the window, so a low-value tangent displaces in-window work rather than only unseen projects; nor does the absence of other work justify scope creep or rule out model-level causes such as completion bias or weak discernment."
  - scope: passage
    quotes:
      - "Missing context alone explains why the worker cannot know its issue's relative priority; it does not by itself explain why the worker acts as if that priority is high. An equally isolated worker under a silent-continuation default can suppress a real emergency and keep going. The *direction* of the failure comes from the workflow's or policy's default action when relative priority is unknown."
    reason: "THIN — The silent-continuation counterfactual shows that a workflow or policy default can flip the failure direction, but it does not establish that failure direction generally comes from a default action under unknown relative priority. It leaves out model-level salience or helpfulness biases and uncalibrated intrinsic severity—for example, voicing a trivial local issue with the same alarm as a local emergency even though the note claims isolated workers retain local technical assessment."
outcome: report
---

# Friction check: Context isolation for focus conflicts with global prioritization

**Central claim (one sentence):** Under bounded effective context and a competing workload whose live state does not fit alongside deep task context, isolating an agent's context to preserve task focus removes the live comparison set required for relational global prioritization.

## Filter

**Filter:** SURVIVES

The central claim commits to one consistent structural trade-off rather than trying to hold incompatible properties simultaneously: it argues that narrow-deep task focus and a wide-shallow global comparison set pull context assembly in opposite directions once combined state exceeds usable context, and it explicitly treats the proposed execution–triage split as relocating rather than eliminating that tension. The friction lies in the inferential joints around its falsification boundary, the division of labor at the split interface, and its causal attribution of observed failure modes.

## Thinnest joints

The five surfaced joints are ordered from foundational claim-level gaps down to partially supported causal bridges:

1. **First (unfalsifiable universal-claim boundary)** ranks thinnest because it governs the warrant and testability of the note's headline universal claim; its two refutation branches are blocked by definition and by the note's own precondition, bypassing the substantive question of compact live priority signals.
2. **Second and third (the stopping/retention unbundling and scale-bearing local facts)** rank immediately behind it because they carry the architectural split's core division of labor: one introduces an unresolved contradiction over whether stopping is local or global and conflates retention with triage separation, while the other assigns cross-context judgments (timing, reversibility, decision impact) to the isolated worker without warrant.
3. **Fourth (attributing low-value tangents to absent competing work)** ranks below the structural architecture joints because it concerns one illustrative symptom rather than the split's viability, though its explicit causal connective still fails to account for the in-window primary task and rival model-level biases.
4. **Fifth (attributing failure direction to workflow or policy defaults)** is the strongest of the five and rates `THIN` rather than `UNSUPPORTED` because the silent-continuation counterfactual genuinely demonstrates that defaults can steer failure direction; it overreaches only by presenting defaults under unknown relative priority as the general source of directionality.

Other explicit joints in the note—such as per-window feasibility pushing toward isolation, insufficient summaries forcing fallback or risking unsafe substitution at the triage boundary, and allocation remaining distinct from objective revision—are better grounded in their cited premises and therefore fall below this cutoff.

## For the human

Look first at the universal claim's refutation condition: concretize what non-tautological test rules out injecting a compact live priority proxy into a focused worker, and then align the execution–triage split by distinguishing hard local stop rules from opportunity-cost stopping without assuming isolated workers can judge external timing or reversibility.
