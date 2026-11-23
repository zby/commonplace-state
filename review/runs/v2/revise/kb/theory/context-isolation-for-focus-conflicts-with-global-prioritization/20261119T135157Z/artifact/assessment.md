# Revision Assessment: `kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md`

**Proposed purpose:** Help agent-system architects and KB operators recognize when isolating an agent's context for task focus breaks relational global prioritization, so they can design the execution–triage boundary and its handoff interfaces without falling into priority flattening.

**Recommendation:** **Stop and rewrite before running text passes.** The highest-value change is a claim-level rewrite and restructuring of the argument—the note's universal claim is refuted inside its own stated conditions by compact dynamic global signals, its overflow precondition supports two materially different readings, and its split and causal-mechanism sections contain internal contradictions and unsupported attributions. Rescoping these claims also changes claims that nine KB dependents rely on. Because the rewrite will replace or restructure most of the text that passes would edit, the plan sets `stop` and recommends no passes (`passes: []`).

**Rewrite route:** `commonplace-review run rewrite kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md --commission FILE`, with the commission prepared with `cp-skill-write-multistage`.

---

## Hostile-reviewer target and what reads well

- **Sentence a hostile reviewer would attack first:** Line 14 — `"**Claim mode: universal** (under bounded effective context and a competing workload whose live state does not fit beside task-solving context). A system operating under those conditions whose isolated task workers reliably make decisions whose right answer depends on unseen competing work—or that loads full live portfolio state alongside deep task context without degrading execution competence—would refute the claim."` Its second disjunct directly contradicts the stated precondition, and its first disjunct is already refuted under the stated conditions whenever an external monitor injects a compact dynamic global threshold (shadow price, priority floor, or live interruption bar) into an isolated worker.
- **What reads well:** The note defines its central terms (`context isolation`, `global prioritization`, `narrow-deep`, `wide-shallow`) crisply on first use, separates missing context (indiscrimination) from direction-setting mechanisms, and grounds the two-view architecture in concrete examples without claiming empirical corroboration.
- **Repeated list/table openings check:** None of the lists hide distinctions behind repeated openings; no `readability-and-flow` pass is warranted on that ground.

---

## Ranked changes (highest value against the purpose first)

1. **Rescope the universal claim, fix the tautological refuter, resolve the overflow-threshold ambiguity, and reframe the execution–triage split as a two-sided compression trade-off** *(Claim-level rewrite — not a pass; stop and use `commonplace-review run rewrite ... --commission FILE` prepared with `cp-skill-write-multistage`)* — Cost: full-note argument rewrite plus dependent review.
   - Rescope the universal claim to non-decomposable or incommensurable workloads whose global opportunity cost cannot be compressed into a compact dynamic sufficient statistic (shadow price, Gittins/Whittle cutoff, live SLA interruption bar, or dynamic budget) and whose comparison-sufficient summary cannot fit or operate beside deep task context without degrading focus.
   - Replace the false dichotomy between static priority rules and full portfolio loading by comparing the two dual compression directions: compressing local facts out to wide-shallow triage versus compressing global opportunity cost into isolated execution.
   - Resolve the internal contradiction on `"This run should stop"` (line 37 vs. lines 10 and 55), separate durable retention (line 38) from the two-view split, narrow local technical assessment (lines 12, 32) to strictly task-internal facts rather than external timing/reversibility, tighten Section 1's causal attribution (distinguishing live project-specific comparison state from pretrained base-rate priors, absolute-stakes calibration failures, in-window primary-task displacement, and model-level biases), and remove/derive/demote the unargued tractability-bias branch (lines 54, 68).
2. **Consolidate duplicated boundary, falsification, disclaimer, and recap apparatus (`## Scope`, `## Open Questions`, inline parenthetical) and rebalance the Nostalgebraist/Anthropic quote overhang** *(Would use `readability-and-flow`, depth 4, once claims settle; deferred because the rewrite will restructure these sections)* — Cost: structural consolidation with editorial decisions on `## Scope` layout and verbatim-quote retention.
3. **Fix reversed `extends` relation labels in `Relevant Notes` and align the `unattended-work` bridge** *(Would use `fix-strategy-taxonomy` on `kb/theory/COLLECTION`, depth 2; deferred until after the rewrite)* — Cost: three footer-link edits plus checking whether the body or footer should carry the interactive-oversight/redirection bridge.
4. **Gloss borrowed KB terms (`oracle asymmetry`, `unsafe substitution`, `concern depth`) and identify Commonplace at first mention** *(Would use `fix-strategy-taxonomy` on `accessibility/undefined-terms` and `accessibility/unidentified-references`, depth 3; deferred until after the rewrite)* — Cost: four short inline glosses.
5. **Fix the parsing ambiguity on `eliminate *previously named* non-priorities and tolerances` and unpack six clause-packed sentences** *(Would use `fix-strategy-taxonomy` on `sentence/parsing-ambiguity` and `sentence/clause-packing`, depth 5; deferred because the rewrite will replace most of the affected sentences)* — Cost: local syntax rewrites across seven sentences.

---

## Depth 1 report and compression synthesis triage

### Defects stopping this run

1. **Universal claim refuted by compact dynamic global signals; one-way split ignores dual compression — Defect**
   - **Reports:** `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/critique-note.md`, `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/premise-decomposition-gate.md`
   - **Case inside stated conditions:** Under bounded effective context and a competing workload whose live state does not fit beside deep task context (lines 14, 59), a separable, commensurable workload can compress portfolio opportunity cost externally into a ~10–20 token live sufficient statistic (shadow price, Gittins/Whittle index cutoff, live SLA interruption bar, or dynamic budget) and inject it into the isolated worker. The worker then tracks changes in unseen competing work using uncompressed local detail—without loading a wide-shallow comparison set or degrading execution competence—refuting the universal impossibility claim (lines 10, 14) and showing that bounded context forces a choice between two compression directions (compress-local-to-global triage vs. compress-global-to-local threshold injection), not a forced move to post-hoc wide-shallow triage (line 30). Correcting this restructures the thesis, Section 1's static-rules rebuttal, Section 2, and `## Scope`.

2. **Ambiguous overflow precondition and tautological falsifier — Defect**
   - **Reports:** `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/composition-friction-gate.md`, `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/premise-decomposition-gate.md`, `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/semantic/underspecified-assertions.md`
   - **Two readings and contradiction:** The precondition `"whose live state does not fit beside task-solving context"` / `"once the combined state exceeds usable context"` (lines 14, 30, 59) supports **Reading 1** (full live portfolio state, matching `"loads full live portfolio state"` at line 14—under which a ~500-token compressed priority table can still fit beside deep task context on a 5–15 project workload, avoiding the split) and **Reading 2** (even a compressed, triage-sufficient comparison set cannot fit or share the window without degrading focus, matching `"compressed summaries of competing items"` at line 33 and `"compressed global state"` at line 67). In addition, line 14's second refuter (`"loads full live portfolio state alongside deep task context without degrading execution competence"`) contradicts the precondition that live state does not fit, insulating the claim tautologically.

3. **Contradictory stopping classification, overclaimed local technical assessment, Section 1 causal overreach, and unargued tractability-bias branch — Defects (bundled into the rewrite)**
   - **Reports:** `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/composition-friction-gate.md`, `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/critique-note.md`, `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/premise-decomposition-gate.md`, `kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/synthesis`, `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/compression-bundle/branch-bloat.md`
   - **Contradictions and false cases:**
     - *Stopping contradiction:* Line 10 defines `"when to stop or defer it"` as global prioritization (and line 55 bounds `"when to stop digging"` by compressed global priority proxies), while line 37 classifies `"This run should stop"` as a local execution judgment the isolated worker can make. Only hard-blocker or pre-injected local stop rules are locally determinable; diminishing-returns stopping is an opportunity-cost decision. Line 38 also bundles durable retention (`"This finding or answer should survive"`) into the two-view split even though persistence is an orthogonal workflow-memory policy.
     - *Local technical assessment overclaim:* Lines 12 and 32 assert that an isolated worker can judge `"what will break, how soon, and whether waiting is reversible"` and `"what decision would change"`. For a worker isolated to one module touching a shared interface or external release schedule, downstream blast radius, time-to-failure, and reversibility of waiting depend on excluded cross-project state.
     - *Section 1 causal overreach:* Line 18 (`"has no ambient comparison set outside what its window holds"`) ignores generic base-rate severity priors in model weights (only *live, project-specific* comparison state is missing). Lines 20–23 attribute failure direction solely to workflow/policy defaults and attribute low-value tangents and `"juice box vs. bleeding finger"` urgency flattening to absent competing work, even though the worker's own primary task is in-window, `"juice box vs. bleeding finger"` is primarily an absolute-stakes calibration failure, and model-level salience/thoroughness biases can skew failure direction even under symmetric workflows.
     - *Unargued tractability bias:* Line 54 (and the presupposing question at line 68) asserts that compressed-summary scans tilt allocation toward tractable low-value work without deriving directionality from bounded context or summary compression—contradicting the note's own rule that missing/compressed context causes indiscrimination while a separate mechanism sets direction.

### Choices (not ranked first; no claim defect shown)

- **Consolidate duplicated boundary, falsification, disclaimer, and recap apparatus (`## Scope`, `## Open Questions`, inline parenthetical) — Choice** (`kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/synthesis`, Opportunity 1). No claim defect is shown; whether to fold boundaries inline or keep a single trimmed `## Scope` and delete `## Open Questions` is an editorial layout choice best settled during the rewrite.
- **Rebalance Nostalgebraist/Anthropic quote overhang in Section 1 — Choice** (`kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/synthesis`, Opportunity 3). No claim defect is shown; trimming four verbatim quotes and duplicate citation links trades proportion against source anchoring (`has-external-sources`) and should be decided alongside the rewrite of Section 1.

### Extensions (not acted on)

- **Large-portfolio triage saturation — Extension** (`kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/premise-decomposition-gate.md`, finding 7). Noting that hundreds or thousands of items can also overflow a single wide-shallow triage call (requiring hierarchical pre-filtering or non-LLM indexing) extends the two-view model to a further scaling regime; the core trade-off does not depend on single-pass scaling, though a brief caveat fits easily into the rewrite if desired.

---

## Role in the KB and affected dependents

From the role report (`kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/role`), ten KB files link to this note (all via tag-head entries or footer glosses; no duplicated prose and no untaken recommendations). Rescoping the core universal conflict, reframing the narrow-deep versus wide-shallow split as a two-sided compression trade-off, and tightening Section 1's causal attribution of the Nostalgebraist/Anthropic examples touch claims that the following nine dependents rely on, so the operator must decide whether those dependents' glosses need matching updates when commissioning the rewrite:

- **Core conflict (rescoping to non-decomposable/incommensurable trade-offs where compact live thresholds do not suffice):**
  - `kb/tags/context-engineering-README.md`
  - `kb/tags/goal-prioritization-README.md`
  - `kb/theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md`
  - `kb/theory/weakly-discriminated-qualities-tend-to-be-underselected.md`
  - `kb/theory/unattended-work-needs-the-functions-that-interaction-supplied.md` (currently `PARTLY SUPPLIED`: relies on this note for isolation impairing stopping and redirection when interactive oversight is removed, a bridge present only in this note's footer gloss)
- **Narrow-deep execution vs. wide-shallow triage split (reframing from forced split to two-sided compression trade-off):**
  - `kb/reference/where-change-candidates-come-from-in-commonplace.md`
  - `kb/tags/architecture-README.md`
  - `kb/tags/context-engineering-README.md`
  - `kb/tags/goal-prioritization-README.md`
  - `kb/theory/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md`
  - `kb/theory/unattended-work-needs-the-functions-that-interaction-supplied.md`
- **Uncalibrated escalation, low-value tangents, and origin-not-corroboration source attribution:**
  - `kb/sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md`
  - `kb/tags/goal-prioritization-README.md`
  - `kb/theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md`

(`kb/theory/a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md` relies only on the local over-specification contrast, which survives unchanged if that bullet stays intact.)

---

## Candidate overclaims: divergence (`must-keep`) vs. support (may be narrowed)

### Divergence — must keep (included in `plan.md`'s `must-keep`)

1. Context isolation for per-window task focus carries a countervailing cost to relational global prioritization (contrasting with oracle-asymmetry accounts and isolation-as-benefit accounts).
2. Missing competing-work context produces priority indiscrimination rather than determining failure direction on its own; a separate mechanism sets whether failure skews toward over-escalation or silent continuation.
3. Explicit static priority rules can rule out previously named non-priorities and encode known tolerances, but cannot supply live relative scale for novel trade-offs across a changing workload.
4. Splitting narrow-deep execution from wide-shallow triage relocates the trade-off to the compression boundary between views rather than eliminating it.
5. Allocation triage supplies a comparison surface under given objectives and does not choose or revise objectives.

### Support — may be narrowed (or corrected in the rewrite)

- Universal claim mode and tautological refuter (lines 14, 30, 59) — narrow to non-decomposable/incommensurable workloads whose comparison-sufficient summary or live priority proxy cannot suffice inside the execution window.
- `"A stateless, isolated agent has no ambient comparison set outside what its window holds"` (line 18) — narrow to lacking a *live, project-specific* comparison set (acknowledging pretrained base-rate severity priors).
- `"The *direction* of the failure comes from the workflow's or policy's default action when relative priority is unknown"` and attributing Nostalgebraist/Anthropic symptoms solely to missing unseen work (lines 20–23) — narrow to include model-level salience/thoroughness biases, in-window primary-task displacement, and absolute-stakes calibration failures.
- Isolated workers judging `"what will break, how soon, and whether waiting is reversible"` and `"what decision would change"` (lines 12, 32) — narrow to strictly task-internal technical facts.
- `"This run should stop"` as a general local execution judgment and durable retention as part of the two-view split (lines 37–38) — narrow local stopping to hard blockers or pre-injected stop rules; treat durable retention as an orthogonal workflow-memory policy.
- `"Tractability bias in global scans"` as an asserted interface friction (lines 54, 68) — drop, derive from an explicit legibility/scoring premise, or demote to a neutral open question.
- Single wide-shallow triage pass scaling unconditionally across competing items (line 33) — note that very large portfolios can also overflow a single triage pass.

---

## Stale or mismatched qualifications

- **`## Scope` terminology mismatch (`relational` prioritization):** Scope bullet 2 restricts the claim to `*relational* prioritization` and exempts `explicit stop rules`, but the body never introduces the term `relational` and line 37 classifies `"This run should stop"` without that exemption.
- **Footer-to-body mismatch (`unattended-work-needs-the-functions-that-interaction-supplied.md`):** Line 85's footer gloss claims this note identifies context isolation as a structural reason `"stopping and redirection fail when interactive oversight is removed"`, but the body never discusses interactive-oversight removal or redirection (`report-5.md` flags it `PARTLY SUPPLIED`).
- **Reversed `extends` links in `Relevant Notes` (lines 75, 76, 85):** Three edges use `extends` pointing toward upstream notes (`bounded-context-orchestration-model.md`, `decomposition-heuristics-for-bounded-context-scheduling.md`, `unattended-work-needs-the-functions-that-interaction-supplied.md`), reversing `kb/theory/COLLECTION.md`'s asymmetric `extends` direction (`finding-6.md`).

---

## Claim questions for the operator

1. **Rewrite commission — core scope and dual compression:** Confirm rescoping the universal claim to non-decomposable/incommensurable trade-offs (where a compact dynamic shadow price, priority floor, or interruption bar cannot faithfully capture global opportunity cost) and reframing Section 2 as a two-sided compression trade-off (compress-local-to-global triage vs. compress-global-to-local threshold injection), plus whether to update the nine affected dependents' glosses (`kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/role`).
2. **Overflow threshold choice:** Commit to Reading 2 (the conflict binds when even a compressed, comparison-sufficient live representation overflows or degrades the deep task window) rather than Reading 1 (full live portfolio state overflow), and rewrite the falsifier accordingly (`kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/semantic/underspecified-assertions.md`, `composition-friction-gate.md`).
3. **Tractability bias disposition:** In the rewrite, should directional tractability bias (lines 54, 68) be cut/rehomed, derived via an explicit legibility/scoring premise linked to `weakly-discriminated-qualities-tend-to-be-underselected.md`, or retained only as a neutral open question (`kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/synthesis`, Opportunity 2; `branch-bloat.md`)?
4. **Layout and quotation choices (Choice — no defect shown):** In the rewrite, choose between (a) folding `## Scope` inline vs. keeping one trimmed `## Scope` that absorbs `Claim mode` and the non-corroboration disclaimer while deleting `## Open Questions` (Synthesis Opportunity 1), and (b) trimming Section 1's four Nostalgebraist/Anthropic verbatim quotes to two sharper anchors vs. keeping all four under `has-external-sources` (Synthesis Opportunity 3).
5. **`unattended-work` bridge and reversed `extends` links:** Decide whether the rewritten body should explicitly connect context isolation to stopping/redirection under removed interactive oversight (satisfying `unattended-work-needs-the-functions-that-interaction-supplied.md`) or narrow the footer gloss, and re-label or drop the three reversed `extends` edges (`kb/theory/COLLECTION.md`, `role`).

---

## Stored review findings not acted on in this run

All nine findings are deferred because the plan sets `stop` for a claim-level rewrite (`passes: []`):

- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/semantic/underspecified-assertions.md` (`semantic/underspecified-assertions`, depth 2): Surfaces the full-state vs. compressed-comparison-set ambiguity that requires a claim-level decision in the rewrite, not a text-only pass.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/theory/COLLECTION.md` (`kb/theory/COLLECTION`, depth 2): Valid reversed-`extends` finding, deferred until after the rewrite so footer edges match the revised claims and the `unattended-work` bridge decision.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/accessibility/undefined-terms.md` (`accessibility/undefined-terms`, depth 3): Valid glosses needed (`oracle asymmetry`, `unsafe substitution`, `concern depth`), deferred because the rewrite will edit or replace the surrounding passages.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/accessibility/unidentified-references.md` (`accessibility/unidentified-references`, depth 3): Valid first-mention identification needed for Commonplace, deferred because the run stops for a rewrite.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/compression-bundle/branch-bloat.md` (`kb/instructions/compression-bundle/branch-bloat`, depth 4): Unargued tractability-bias claim and ADR 138 answer-persistence branch require claim-level resolution in the rewrite.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/compression-bundle/detail-overhang.md` (`kb/instructions/compression-bundle/detail-overhang`, depth 4): Targets Section 1's Nostalgebraist/Anthropic quote blocks, which will be reworked during the rewrite of Section 1's causal framing.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/kb/instructions/compression-bundle/marginal-value-redundancy.md` (`kb/instructions/compression-bundle/marginal-value-redundancy`, depth 4): Targets the Commonplace parenthetical, `## Scope`, and `## Open Questions`, which will be restructured by the rewrite.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/sentence/clause-packing.md` (`sentence/clause-packing`, depth 5): Six packed sentences sit in passages that the rewrite will replace; fixing syntax beforehand would be discarded.
- `kb/reports/state/review/results/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md/sentence/parsing-ambiguity.md` (`sentence/parsing-ambiguity`, depth 5): Valid syntax fix on `eliminate *previously named* non-priorities and tolerances`, deferred because the rewrite will revise that static-rules paragraph to address dynamic global signals.
