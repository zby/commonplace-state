# Assessment: `kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md`

**Proposed purpose:** Help an agent-systems architect recognise when context isolation removes the comparison set required for relational global prioritization, distinguish missing-context indiscrimination from default-driven failure direction, and see the architectural trade-offs of splitting narrow-deep execution from wide-shallow triage.

**Decision: Stop for a claim-level rewrite (`passes: []`).** Run `commonplace-revise rewrite kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md --commission FILE` with the commission prepared with `cp-skill-write-multistage`.

## Why this stop is raised after the rejected earlier stop

The operator rejected an earlier stop (`2026-11-19T15:16:25Z`, `kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/artifact/stop-answers.md`) because an injected compressed global cost signal (shadow price, Gittins/Whittle cutoff, or scalar bar) is not locally calibratable without a common scale, whereas a global view compares concrete tasks directly. Raising a new stop is warranted on both grounds allowed by the revision procedure:

1. **The text changed to incorporate the operator's earlier reason.** The revised artifact embeds the local-calibration boundary directly in the thesis, Condition 3, Section 1's injected-signal rebuttal, and Scope (lines 10, 14, 26, 58), and applies local fixes to lines 12, 18, 20–23, 32, 37, and 39.
2. **The new depth-1 reports present a new case the operator's reason does not address**, plus new tensions introduced by those edits:
   - **O(1) concrete marginal-anchor injection** directly answers the operator's concrete-comparison rationale: injecting 1–5 concrete competing tasks at the current priority cutoff (~50–300 tokens) requires *no numeric common scale* and enables *side-by-side comparison of concrete tasks inside local scope*, scaling with the cutoff frontier O(1) rather than portfolio size O(N).
   - The post-rejection edits also introduced two conflicting readings of the focus-degradation threshold (`without degrading focus` vs. `usable window`), an observer-relative salience tension between line 12 and line 32's task-internal `scale-bearing local facts`, a self-undermining parenthetical in line 23 for in-window tangents, and a gap between line 37's hard-blocker stops and line 41's claim to repair unattended stopping and redirection.

Correcting these defects reshapes the opening thesis, Conditions 2–3, Section 1, the Section 2 split and unbundling, Section 3's interface friction, Scope, and Open Question 2. Text passes cannot change claims and would polish passages the rewrite will replace, so no passes are planned.

## Sentence a hostile reviewer would attack first

> "In open-ended work without such a scale, a compressed cost signal is not comparable in local scope: the isolated worker cannot calibrate its local issue against an abstract bar, whereas a global view lets the agent compare concrete tasks side by side." (line 26)

A hostile reviewer immediately counters with a ~50–300 token live card naming the 1–5 concrete tasks at the current priority cutoff, which needs no numeric scale and lets the isolated worker compare concrete tasks side by side inside its local prompt without loading the full portfolio.

## What reads well

The causal separation between missing competing-work context (producing priority indiscrimination) and workflow/policy defaults (setting the direction of failure toward over-escalation or silent continuation), paired with concrete Commonplace illustrations at three operational scales, reads cleanly and gives the note genuine explanatory traction.

## Ranked list of changes

1. **Rescope the universal claim, local-calibration dichotomy, and Scope boundary against O(1) concrete marginal anchors (Defects 1–2; lines 10, 14, 26, 30, 58, 66).**
   - *Cost:* Full claim-level rewrite of thesis conditions, injected-signal rebuttal, Section 2 pivot, Scope, and Open Question 2, plus dependent checks.
   - *Route:* Stop and rewrite via `commonplace-revise rewrite kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md --commission FILE` (`cp-skill-write-multistage`). No text pass can change claims.
2. **Resolve observer-relative salience in "scale-bearing local facts" and the unattended stopping/redirection gap (Defects 3–4; lines 12, 22–23, 32, 37, 41, 53–54).**
   - *Cost:* Substantive claim revisions across Section 1 failure modes, Section 2 interface/unbundling, and Section 3 residual friction, plus dependent review for `unattended-work-needs-the-functions-that-interaction-supplied.md`.
   - *Route:* Include in the same rewrite commission (no pass can make claim changes).
3. **Surface the core claim upfront and consolidate boundary conditions and evidential caveats into one home (`report-4.md` Opportunity 1; `core-claim-obscured`, `marginal-value-redundancy`, `claim-to-section-ratio`).**
   - *Cost:* Structural consolidation of lead, Section 2 transition, and Scope once claims are settled.
   - *Route:* Defer to the rewrite (or post-rewrite `readability-and-flow` and `opening-and-title`); passages are directly replaced by changes 1–2.
4. **Rebalance the Nostalgebraist/Anthropic quotes and settle the orthogonal workflow-memory branch (`report-4.md` Opportunities 2–3; `detail-overhang`, `branch-bloat`).**
   - *Cost:* Editorial trimming of lines 22–23 and a scope decision on lines 35, 39, 46.
   - *Route:* Decide in the rewrite commission (see `Claim questions for the operator`), or run `readability-and-flow` after the rewrite.
5. **Narrow uncorroborated empirical attributions, fix source residue, and clean sentence/footer friction (`epistemic-status-blur`, `source-residue`, `undefined-terms`, `connection-inflation`, `anthropomorphic-framing`, `clause-packing`, `framing-mismatch`, `parsing-ambiguity`, `stock-phrases`, `compound-bullet`).**
   - *Cost:* Localized wording, framing, and footer edits across passages largely rewritten by changes 1–2.
   - *Route:* Defer until after the rewrite (`narrow-overclaims`, `fix-strategy-taxonomy`, `abstractions`, `readability-and-flow`, `plain-wording`).

*List/table scanning check:* Existing lists use distinct bolded or italicized lead-ins rather than repeated openings that hide scanning distinctions; two bullets in `## Scope` and `## Open Questions` pack two points into one bullet (`compound-bullet`), deferred with the rewrite of lines 58 and 66.

## Classification of depth-1 reports and compression synthesis

### Stopping Defects (require rewrite)

1. **Defect 1 — Universal claim and abstract-bar vs. global-view dichotomy defeated by concrete marginal-anchor injection (lines 10, 14, 26, 30, 58, 66).**
   - *Kind:* **Defect.**
   - *Reports:* `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/critique-note.md` (Findings 1–3; attack outcome `lands`); `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/premise-decomposition-gate.md` (Finding 1, `DEFEATED — GLOBAL — instance`); `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/composition-friction-gate.md` (Finding 2, `UNSUPPORTED`); `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/semantic/explanatory-reach.md` (`warn`).
   - *Case:* On a large open-ended workload with no numeric common scale (satisfying Condition 3 as written), injecting a ~50–300 token live marginal anchor card naming the 1–5 concrete tasks currently occupying operator attention or sitting at the priority cutoff lets an isolated worker compare concrete tasks side by side in local scope without a numeric scale and without loading all N tasks. This refutes line 26's claim that concrete side-by-side comparison requires a global view and line 58's equation of compact comparison-sufficient live state with a "small workload". Relying on Condition 2 ("whose comparison-sufficient live summary cannot sit beside deep task context without degrading focus") to exclude concrete anchors turns Condition 2 into an outcome-defined stipulation while punting its structural cause to Open Question 2 (line 66). Rescoping requires naming the non-circular structural conditions that defeat compact marginal anchoring too (e.g., content-addressed cross-portfolio coupling, concurrent sibling-worker staleness, or empirical attention distraction).

2. **Defect 2 — Two conflicting readings of the focus-degradation threshold and binary impossibility of a shared call (lines 10, 14, 30, 54, 58).**
   - *Kind:* **Defect.**
   - *Reports:* `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/semantic/underspecified-assertions.md` (`warn`); `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/premise-decomposition-gate.md` (Finding 2, `DEFEATED — LOCAL — instance`); `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/composition-friction-gate.md` (Finding 3, `UNSUPPORTED`).
   - *Two readings and counterexample:* The wording supports Reading 1 — strict zero measurable focus degradation ("without degrading focus", lines 14, 30; "without eroding focus", line 54) — and Reading 2 — exceeding the task's usable-window feasibility ceiling ("usable attention budget", line 10; "fits inside one usable window", line 58). Under soft attention decay, Reading 1 triggers a mandatory split for almost any summary, which fails when co-loading a brief summary causes mild focus loss inside the feasibility margin while avoiding larger split-interface compression errors or deep-context fallback costs; Reading 2 allows compact O(1) summaries on large workloads. Line 30's `Because` clause also stipulates a summary-size regime without showing when a competing-work summary is too heavy for the worker yet severity-preserving summaries of all candidates fit in one triage call.

3. **Defect 3 — Selection circularity around task-internal "scale-bearing local facts" (lines 12, 32, 53).**
   - *Kind:* **Defect.**
   - *Reports:* `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/premise-decomposition-gate.md` (Finding 3, `DEFEATED — LOCAL — instance`); `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/critique-note.md` (Finding 4 & Secondary objection 1); `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/composition-friction-gate.md` (Finding 3, `UNSUPPORTED`).
   - *Two statements and case:* Line 12 concedes that cross-boundary blast radius, external deadlines, and external reversibility depend on excluded state, yet line 32 prescribes that an isolated worker emit "scale-bearing local facts" as purely task-internal judgments, and line 53 frames missed emergencies as workers emitting uninformative blockers or dropping severe local detail. Case: an isolated worker refactoring a serialization helper verifies locally that changing JSON key order breaks nothing inside its module and omits it, unaware that an external billing signature check hashes raw serialized JSON; logging every locally benign detail instead breaks triage compression.

4. **Defect 4 — Unattended stopping/redirection overclaim and motivating-example causal tensions (lines 18, 22–23, 37, 41, 54).**
   - *Kind:* **Defect.**
   - *Reports:* `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/composition-friction-gate.md` (Findings 1, 4 `UNSUPPORTED`; Finding 5 `THIN`); `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/premise-decomposition-gate.md` (Finding 6, `DOUBTFUL — LOCAL — instance`); `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/critique-note.md` (Finding 5 & Secondary objection 2).
   - *Two statements and cases:*
     - Line 37 assigns diminishing-returns and global opportunity-cost stopping to triage while workers stop only on hard blockers or pre-injected stop rules, and line 54 leaves within-episode branch choices inside the worker, yet line 41 claims unbundling local stopping from immediate operator action repairs degraded stopping and redirection in unattended work. Case: a mid-run tangent or debugging loop triggers no hard blocker, so decoupling post-stop notification cannot stop or redirect it before episode-budget exhaustion.
     - Line 23 attributes earnest low-value tangents to absent external competing work while conceding in a parenthetical that "even the in-window primary task has no live opportunity-cost counterweight"—pointing to within-window effort-valuation failure rather than missing external context. Likewise, line 22's "either way" bridge over the juice-box vs. bleeding-finger example sits in tension with line 18's claim that isolated agents retain pretrained base-rate severity priors (and parallel simultaneous blockers reflect concurrent-snapshot staleness, not context crowding alone).

### Choices (from compression synthesis; non-stopping)

All three opportunities in `kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T184215Z/synthesis` are **Choices** (no defect shown in the claim itself):
- Opportunity 1: lead structure and single canonical home for boundaries (`## Scope` kept vs. removed and folded earlier).
- Opportunity 2: quote-stacking balance for Nostalgebraist/Anthropic and placement of the priority-flattening quote.
- Opportunity 3: removing vs. deriving the orthogonal workflow-memory bullet (lines 35, 39, 46).

### Extensions (non-stopping; listed below under Findings not acted on)

- `premise-decomposition-gate` Finding 4 (`DOUBTFUL — LOCAL — prevalence`): empirical prevalence of attention-budget crowding vs. harness siloing and concurrency staleness in typical parallel coding-agent workloads.
- `premise-decomposition-gate` Finding 5 (`DOUBTFUL — LOCAL — instance`): non-decomposable cross-item interactions (e.g., incompatible lock ordering across two benign refactors) and deep-context tractability estimation as additional limits on wide-shallow triage.

## Role in the KB and affected dependents

Role report run directory: `kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T184215Z/role`.

Rescoping the core conflict (when O(1) concrete marginal anchors work vs. when the narrow-deep / wide-shallow split is forced) and tightening the tangent-chasing and unattended stopping/redirection claims directly affects claims relied on by nine dependents, which the operator must decide alongside the rewrite:

- `kb/tags/context-engineering-README.md` (core thesis and forced narrow-deep vs. wide-shallow split)
- `kb/tags/goal-prioritization-README.md` (core thesis, urgency flattening / tangents, and split condition)
- `kb/tags/architecture-README.md` (narrow-deep vs. wide-shallow split and interface friction)
- `kb/reference/where-change-candidates-come-from-in-commonplace.md` (why local noticing needs a separate wide-shallow triage pass)
- `kb/theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md` (countervailing cost of isolation to global prioritization and escalation calibration)
- `kb/theory/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md` (general narrow-deep vs. wide-shallow split)
- `kb/theory/unattended-work-needs-the-functions-that-interaction-supplied.md` (unbundling local stopping from immediate operator action as a structural reason stopping and redirection degrade without interaction)
- `kb/theory/weakly-discriminated-qualities-tend-to-be-underselected.md` (missing live competing-work context as rival mechanism)
- `kb/sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md` (origin-not-corroboration framing of tangent and Anthropic babysitting quotes)

One dependent, `kb/theory/a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md`, relies only on the local over-specification bullet (line 24) and is unaffected unless that bullet's claim changes.

## Candidate overclaims and stale qualifications

### Divergence (must keep — recorded in `plan.md` `must-keep`)

These commitments define the note's contribution and held up under premise decomposition; they should survive rescoping unless the operator changes the thesis:

1. When the right allocation or escalation decision changes with live competing work and no locally comparable live signal enters the worker, isolating context for task focus removes the live comparison set relational global prioritization requires (core information-theoretic conflict, line 10).
2. Missing competing-work context alone causes priority indiscrimination; it does not by itself set the direction of failure (over-escalation versus silent continuation), which requires a separate mechanism (line 20).
3. Standing priority rules in static context cannot order a local branch against unseen live competing work across a changing workload (line 26).
4. Splitting narrow-deep execution from wide-shallow triage relocates the trade-off to the summary boundary between views rather than eliminating it (lines 51–53).

### Support (may be narrowed — do not treat as divergence)

- Line 20: `"most visibly the workflow's or policy's default action, reinforced by model-level thoroughness and salience biases"` — uncorroborated empirical attribution stated declaratively (`semantic/epistemic-status-blur`); narrow to illustrative or candidate mechanisms.
- Line 24: `"compounding the oracle asymmetry..."` — conjectural compounding stated declaratively (`semantic/epistemic-status-blur`, info); mark as conjectural.
- Line 26: `"Explicit static rules can eliminate previously named non-priorities"` — slightly over-narrowed (`premise-decomposition-gate`, HOLDS note); static rules can also exclude workload-invariant categorical non-priorities.
- Line 22 (`"Parallel isolated workers..."`) and line 53 (`"**Compression hides emergencies.**"`) — narrow framings of broader mechanisms (`sentence/framing-mismatch`).

### Stale qualifications against the body

- **Line 66 (Open Question 2):** Asks how much compressed global state ("active bottlenecks, tolerances, budgets") can be injected and what makes it locally calibratable before focus degrades, while lines 14, 26, and 58 already treat the failure of compact injected signals without a numeric scale as settled.
- **Line 46 (ADR 138 illustration):** Retains the cross-run answer-persistence clause ("an operator's answer to a stop can be recorded so the next run does not re-ask") to match line 39, which the body now explicitly labels an orthogonal workflow-memory policy independent of triage routing.
- **Line 58 (`## Scope` bullet 1):** Qualifies the conflict as disappearing only "on a small workload", narrower than the body's own "comparison-sufficient live summary" framing (lines 14, 30) once O(1) marginal anchors are considered.
- **Line 22 (`Uncalibrated escalation`) and line 53 (`Compression hides emergencies`):** Both openers qualify mechanisms more narrowly than their own sentences (parallel-only vs. single isolated worker; false negatives only vs. bidirectional misclassification and unnecessary fallback).

## Claim questions for the operator

To settle alongside the rewrite commission (each is a **Choice** with no defect shown; the operator may decline any of them):

1. **Boundary-condition layout (`report-4.md` Opportunity 1; Choice, no defect shown):** Keep `## Scope` as the single consolidated home for boundary conditions and evidential caveats (removing lead paragraphs 2–3), OR drop `## Scope` as a standalone recap and fold its three unique additions (intrinsic-check examples, allocation-vs-objective-choice boundary, unmeasured comparison metrics) into earlier prose? Also decide whether `Claim mode: universal` stays near the top or moves to `## Scope`.
2. **Nostalgebraist/Anthropic quote balance (`report-4.md` Opportunity 2; Choice, no defect shown):** Retain both babysitting quotes verbatim (to keep the second quote's direct link to multi-agent Claude use) or compress the second quote to paraphrase, and decide whether to promote `"Everything is flattened out..."` to frame all three failure modes instead of keeping it inside the tangents bullet.
3. **Orthogonal workflow-memory branch (`report-4.md` Opportunity 3 / `branch-bloat`; Choice, no defect shown):** Prune the third unbundling bullet (line 39) and the matching ADR 138 answer-carryover clause (line 46) to keep the section focused on the two-way execution/triage split (affects no dependent per the role report), OR argue cross-run answer persistence directly from agent statelessness rather than presenting it as orthogonal.

## Findings not acted on

No automated passes are planned because the run stops for a claim-level rewrite. Every stored `warn`/`fail` finding and non-stopping depth-1 extension is accounted for once below:

- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/semantic/explanatory-reach.md` (depth 2, `warn`): Subsumed into the `stop` (Defect 1: outcome-insulated Conditions 2–3 and missing falsifier); cannot be fixed by a text pass.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/semantic/underspecified-assertions.md` (depth 2, `warn`): Subsumed into the `stop` (Defect 2: two conflicting readings of "without degrading focus" vs. usable-window feasibility); cannot be fixed by a text pass.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/semantic/epistemic-status-blur.md` (depth 2, `warn`): Deferred to the rewrite (or post-rewrite `narrow-overclaims`) because `stop` lists no passes and line 20 sits in Section 1 alongside Defect 4.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/prose/source-residue.md` (depth 2, `warn`): Genuine local fixes (`module or diff` in line 24; `frontier` in line 67; `fix-strategy-taxonomy` responds to this criterion), deferred because `stop` lists no passes and the rewrite can generalize both in place.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/accessibility/undefined-terms.md` (depth 3, `warn`): Flags `Claim mode: universal` on line 14, which is directly rewritten under Defects 1–2; gloss or restate after/during the rewrite.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/complexity/claim-to-section-ratio.md` (depth 4, `warn`): Flags redundant `## Scope` section; deferred to the operator's layout choice in `Claim questions for the operator` (`report-4.md` Opportunity 1) after claims are rescoped.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/complexity/connection-inflation.md` (depth 4, `warn`): Flags four redundant `Relevant Notes` entries (`context-efficiency`, `intent-controls-choices`, `an-insufficient-summary`, `unresolved-frontier`); deferred because `stop` lists no passes and the rewrite may change inline links.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/compression-bundle/branch-bloat.md` (depth 4, `warn`): Flags orthogonal workflow-memory bullet (lines 35, 39, 46); classified as a Choice under `Claim questions for the operator` (`report-4.md` Opportunity 3).
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/compression-bundle/core-claim-obscured.md` (depth 4, `warn`): Flags delayed core claim and repeated boundary conditions across lead, line 30, and Scope; passages are directly rewritten under Defects 1–2 and governed by `report-4.md` Opportunity 1.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/compression-bundle/detail-overhang.md` (depth 4, `warn`): Flags stacked Nostalgebraist/Anthropic quotes (lines 22–23) and repeated conditions (line 30); lines 22–23 and 30 are rewritten under Defects 1, 2, and 4, and quote balance is a Choice under `Claim questions for the operator`.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/compression-bundle/marginal-value-redundancy.md` (depth 4, `warn`): Flags repeated conditions in line 30, Commonplace parenthetical (line 43), and `## Scope`; deferred to the rewrite (`report-4.md` Opportunity 1) since lines 30 and 58 change under Defects 1–2.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/prose/anthropomorphic-framing.md` (depth 5, `warn`): Flags `know` (line 20) and `Earnest low-value tangents` (line 23); deferred to post-rewrite prose passes because lines 20 and 23 are affected by `epistemic-status-blur` and Defect 4.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/sentence/clause-packing.md` (depth 5, `warn`): Flags long/interrupted sentences on lines 14, 22, 24, 30, 33 (plus info on line 12); deferred until post-rewrite passes because most of these sentences will be replaced.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/sentence/framing-mismatch.md` (depth 5, `warn`): Flags `Parallel isolated workers` (line 22) and `Compression hides emergencies` (line 53); deferred because both passages are touched by Defects 3–4.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/sentence/parsing-ambiguity.md` (depth 5, `warn`): Flags modifier attachment on line 22 and coordination scope on line 30; deferred because both sentences will be rewritten under Defects 1, 2, and 4.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/sentence/stock-phrases.md` (depth 5, `warn`): Flags line 12 opener and line 35 `Crucially,` (info); deferred because both sit in rewrite-affected sections.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/structural/compound-bullet.md` (depth 5, `warn`): Flags compound bullets in Scope (line 58) and Open Question 2 (line 66); deferred because both bullets will be rewritten under Defects 1–2.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/premise-decomposition-gate.md` (Finding 4, `DOUBTFUL — LOCAL — prevalence`): **Extension** — asks for empirical prevalence evidence that attention-budget crowding rather than harness siloing dominates ordinary parallel coding workloads; the note already frames its thesis conditionally and disclaims empirical corroboration.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/premise-decomposition-gate.md` (Finding 5, `DOUBTFUL — LOCAL — instance`): **Extension** — asks to cover non-decomposable cross-item interactions and deep-context tractability estimation as additional limits on wide-shallow triage; optional addition to Residual friction during the rewrite, not a defeater of the core isolation-vs-prioritization conflict.
