---
description: "Discovery for Agent Plasticity: effects-based evaluation, causal controls, artifact inheritance, and return-link candidates."
type: types/connect-report.md
source: kb/sources/agent-plasticity.ingest.md
source_has_frontmatter: true
date: "2026-10-18"
depth: standard
---

# Connection Report: Agent Plasticity: Measuring Self-Improvement Through Experience

**Source:** [Agent Plasticity ingest](../../../../sources/agent-plasticity.ingest.md)

Discovery only. No candidate below has been authored by this operation. The effects requirement already has an outbound link in the ingest; its entry below recommends strengthening that existing connection, not duplicating it.

Produced with `gpt-6.1-sol` under `cp-skill-connect/SKILL.md`, using the live source, collection contracts, and connect-report type on 2026-10-18. No workers, external searches, snapshot inspection, or source-code execution were used. Source-side empirical statements below are assessments of the ingest, not independent verification of the paper.

## Discovery Trace

### Scope and authorization

Read [sources contract](../../../../sources/COLLECTION.md), [reports contract](../../../COLLECTION.md), and [connect-report type](../../../../types/connect-report.md) before report authoring. The source contract permits prospecting notes, reference, agent-memory-systems, agentic-systems, tags, and other sources. Notes permit evidence, comparison, theory-dependency, and definition edges; reference permits only `see-also`; system accounts permit comparison or adjacency (and `is-evidence-for` for agent-memory-systems). Sources permit comparison or adjacency. Tags are named as a scan surface but have no authorized source-to-tag label. Instructions and work are excluded.

Read the source fully. Its central mechanism is fixed-weight adaptation through inherited artifacts across fresh acting contexts. Its distinctive contributions are checkpoint outcome curves, learning-cost accounting, and coverage/use/failure diagnostics. Limits include missing budget-matched development without feedback, unequal NetHack game difficulty, and observation rather than intervention for most reuse attributions.

### Shared search procedure

For each `d` in `notes reference agent-memory-systems agentic-systems tags sources`, generated the complete fresh title surface once with:

```bash
rg -N --no-heading -m1 '^# ' "kb/$d/" --glob '*.md'
```

Read all six collection README landings. Scanned scoped description results using:

```bash
rg '^description:' "kb/$d/" --glob '*.md' \
  | rg -i 'learn|evaluat|reuse|artifact|reflect|cost|plastic|failure'
```

Ran these two body searches separately in each of those six destinations:

```bash
rg -l -i 'artifact.{0,25}reuse|reuse.{0,25}(benefit|performance)|acquisition.{0,15}(cost|efficien)|plasticity' "kb/$d/" --glob '*.md'
rg -l -i 'fresh.context|budget.matched|failure.composition|causal uptake|held.out' "kb/$d/" --glob '*.md'
```

These were Boolean repository searches; no semantic scores were available. The source has `domains`, not `tags`, so no source-tag membership search was applicable. The theory-builder head read below declares `complete: true`; no by-tag `rg` was run for it. No generated site listings were used. Large search outputs were examined in bounded reads or narrowed by a subsequent scoped query.

### Notes

- Read [notes landing](../../../../notes/README.md) and the [evaluation](../../../../tags/evaluation-README.md), [agent-memory](../../../../tags/agent-memory-README.md), and [theory-builder](../../../../tags/theory-builder-README.md) curated heads. The heads routed to effects evaluation, causal contrasts, retained-theory intervention, and process-versus-capacity evidence.
- Titles and descriptions nominated effects evaluation, diagnostic richness, persistent adaptation, fixed decomposition, complete theory paths, compounding, and sample efficiency. Body query A particularly exposed effects evaluation and sample efficiency; query B exposed causal contrasts and complete theory paths.
- Read the candidate documents fully. Retained effects evaluation, causal contrasts, complete theory paths, and the compounding measurement note for distinct reader needs. Diagnostic richness was not retained as an evidence edge: the diagnostic taxonomy does not experimentally isolate a feedback-quality effect.
- Followed the effects note's Memento-Skills neighborhood through its causal-contrast companion; read the source-to-source comparison candidates instead of adding another generic skill-learning link. Followed complete-theory-path links to theory-builder and addressable-theory definitions, and the compounding protocol to its accumulation companion. Read the retained-theory intervention and activation notes as reverse-edge sources.
- The ingest already links theory builder, addressable theory, and fixed decomposition. Those links are adequate for discovery; no duplicate definition or dependency entries are proposed.
- Sample efficiency was rejected as direct corroboration: learning dollars and stronger-opponent transfer do not measure target observations saved under controlled structured shifts.
- Read [notes contract](../../../../notes/COLLECTION.md) for all proposed returns and reverse edges. `evidenced-by` phrases below explicitly qualify or bound claims; none asserts that a paper was an independent attempted refutation of an existing note.

### Reference

- Read [reference landing](../../../../reference/README.md). Title/description scan nominated the ablation-baselines proposal, trajectory-aware judging proposal, and memory gap plan. Body query B found the ablation proposal; query A mostly found unrelated artifact-run machinery.
- Fully read [ablation baselines](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md), reached both from the evaluation head and the compounding note. Retained as a concrete Commonplace protocol consumer of checkpoint inheritance and cost accounting, not as a premise or adopted design.
- Did not keep trajectory-aware judging: its output-only versus trajectory-aware judge contrast is not the paper's checkpoint learning-curve contrast. Did not keep the broad gap plan merely because both discuss evaluation.
- Read [reference contract](../../../../reference/COLLECTION.md). No return edge is proposed: the proposal is already motivated by other sources, and this paper has not informed an authored revision of it.

### Agent-memory-systems

- Read [historical landing](../../../../agent-memory-systems/README.md); respected its frozen survey boundary. The complete title surface and filtered descriptions surfaced Voyager, Reflexion, Meta-Harness, and general trace-learning accounts.
- Narrowed descriptions with `rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg -i 'voyager|meta-harness|reflexion|trace.learning'`. Body query B also found Meta-Harness and autocontext. Voyager was selected from its executable-library description and fully read.
- Retained [Voyager](../../../../agent-memory-systems/reviews/voyager.md) only as a mechanism comparison: success-gated executable skill admission versus structurally valid inventory admission, and prompt exposure versus runtime execution. Its read-back section explicitly leaves causal faithfulness untested.
- Followed Voyager's activation link to the activation note, already retained for reverse evaluation. Did not treat a game-agent keyword match as evidence about Voyager's measured performance.
- No return mutation is recommended into the frozen historical review; this report's comparison leaves its pinned observation intact.

### Agentic-systems

- Read [agentic-systems landing](../../../../agentic-systems/README.md). Title and description surfaces included current authored reviews and historical analysis archives. Narrowed current descriptions with `rg '^description:' kb/agentic-systems/reviews/ --glob '*.md'`.
- Body query B nominated Compound Engineering, Ecdysis, and historical optimization accounts. Fully read the archived Ecdysis overview. Its strict numeric candidate selection and external adapter boundary are informative, but too indirect compared with the source-to-source evaluation contrasts; rejected as a connection target.
- Evaluated Compound Engineering at passage resolution with `rg -n -i 'learning|evaluation|skill|failure|memory' kb/agentic-systems/reviews/compound-engineering-plugin.md`. Its unmeasured later-episode productivity is already covered more precisely by the compounding theory note. No separate system-level edge was retained.
- Existing links from the source-comparison neighborhood led to diagnostic-richness and fixed-decomposition notes; these were read, but did not justify adding an agentic-system account merely to fill this destination.

### Tags, other sources, and external

- **Tags:** read the tags landing and the three heads named above. Both body searches returned no matches in tags. Heads supplied routing, not connection targets: sources do not participate in the declared tag membership space, and no outbound source-to-tag label is authorized. No request to expand authorization is warranted.
- **Sources:** read the sources landing; complete titles and filtered descriptions identified Harness Updating, Faithful Self-Evolvers, Continual Harness, Memento-Skills, and many less specific optimizers. Fully read the first three and retained them on distinct axes: update/use/benefit, causal content perturbation, and reset-free versus fresh-context adaptation. Followed Harness Updating's links to causal contrasts and compounding, and Continual Harness's links to diagnostic richness and fixed decomposition. Memento-Skills remains the effects note's existing example; a direct new link would add less than the selected comparisons.
- **Existing-edge check:** `rg -n 'agent-plasticity|2610\.08902' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` found only the target ingest's source URL. No incoming links were found on these searched surfaces.
- **External:** the primary arXiv URL is already supplied by source metadata and qualifies for `derived-from`. It needs no duplicate connection suggestion. No open-web prospecting was performed.

## Connections Found

- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — **is-evidence-for**: Agent Plasticity supplies a bounded evaluation example separating checkpoint task scores, acquisition expense, decision-level reuse, and failure-conditioned coverage. Strengthen the existing connection; invocation is not causal uptake, and these games do not test Commonplace's memory architecture.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **rests-on**: the ingest's limits on attributing gains to experience depend on the absent budget-matched no-feedback comparison; its guard-removal replay identifies a local move change, not an individual artifact's aggregate winning contribution.
- [A complete theory path does not establish improved capacity](../../../../notes/a-complete-theory-path-does-not-establish-improved-capacity.md) — **is-evidence-for**: reported content-directed repairs, later use, and flat or negative learning curves give a bounded case for assessing process evidence separately from improved capacity. Do not claim that every lineage supplies a complete causal path.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — **see-also**: a score-gain-per-learning-dollar measure can be mistaken for improved productivity of subsequent improvement; this note supplies the additional later-episode counterfactual and trace that the paper does not establish.
- [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) — **compares-with**: compare Agent Plasticity's coupled same-model acting/reflection lineages with crossed updater/consumer pairings; both separate artifact use from benefit, but their attribution units and denominators differ.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) — **compares-with**: compare observational reuse diagnostics and one local guard replay with explicit content perturbations that test behavioral dependence. These are different evidence designs, not conflicting results about a common treatment.
- [Continual Harness](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) — **compares-with**: compare fresh-context inheritance and isolated held-out checkpoints with reset-free mid-episode revision; preserve the latter's optional weight-learning loop, sparse reuse, and different admission conditions rather than treating the systems as equivalent.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) — **compares-with**: compare what admits generated executable memory and how later acting consumes it: critic-success admission with retrieved prompt code and full runtime library versus structurally/executably valid inventory inheritance. This helps choose what admission and consumption tests a KB experiment needs, without importing the review's historical performance claims.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) — **see-also**: the unadopted Commonplace proposal is a concrete recipient for fresh-context frozen-artifact arms, full checkpoint curves, and separate acquisition-cost accounting. Its human-judgment denominator cannot be replaced by the paper's learning dollars.

## Bidirectional Candidates

These are return links from outbound targets, not automatically symmetric labels.

- [Effects requirement](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) → source — **evidenced-by** under the notes contract: add a bounded methods example distinguishing reuse, failure coverage, task outcome, and acquisition cost. This adds trajectories and diagnostic denominators to its existing routing/outcome example; it does not establish causal benefit for each reused artifact.
- [Experimental contrast note](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) → source — **evidenced-by** under the notes contract: use the missing no-feedback budget control and local guard replay as a worked qualification of attribution grain. The paper illustrates the bound; it does not independently corroborate the general methodological rule.
- [Harness Updating ingest](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) → source — **compares-with** under the sources contract: readers of its role-crossing evaluation gain a complementary protocol measuring longitudinal acquisition efficiency while coupling updater and consumer identity.
- [Faithful Self-Evolvers ingest](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) → source — **compares-with** under the sources contract: readers gain the complementary distinction between causal behavioral dependence and task benefit despite high measured reuse; retain task and representation differences.

## Reverse-edge Candidates

These inbound-only recommendations serve claims in other collections. They are not duplicate outbound proposals.

- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) → source — **evidenced-by** under the notes contract: fresh acting contexts inheriting fixed-weight inventory revisions supply a bounded persistence example, with held-out improvement in some lineages. Qualify the note's selection account: structural acceptance is not a behavioral-effectiveness gate, and the paper does not prove experience's incremental value over equally budgeted artifact construction.
- [A retained-theory intervention isolates one surface](../../../../notes/retained-theory-intervention-isolates-one-explicit-surface.md) → source — **evidenced-by** under the notes contract: the exact-position guard-removal replay is a concrete local intervention on one explicit surface. It bounds the example to a changed move, not broad generalization, total program-theory possession, or aggregate win contribution.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source — **evidenced-by** under the notes contract: the source offers failure diagnostics distinguishing absent coverage, available-but-unused artifacts, and failure despite use. Add as diagnostic instrumentation, not a causal estimate of activation-failure prevalence; semantic annotations do not establish content-directed influence.

## Off-authorisation Candidates

None. Tag heads were useful routing surfaces, but no standalone articulated source-to-head connection justified requesting a new label.

## Raw Text Candidates

None. Retained connection candidates all have frontmatter. Untyped collection landings were used for navigation only.

## Rejected Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — the paper's diagnostic detail is useful, but post-hoc failure annotations are not all available to the learner, and no contrast isolates the effect of richer proposer evidence. Do not present diagnostic reporting as evidence of improved outer-loop learning.
- [Retained theories may improve sample efficiency under structured shifts](../../../../notes/retained-theories-may-improve-sample-efficiency.md) — no controlled target-observation comparison, persistence-grade contrast, or reach-selector comparison tests this conjecture. Learning dollars and stronger opponents are not substitutes.
- [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md) — valid conceptual context, but the retained compounding protocol provides the more useful operational distinction without another overlapping outbound edge.
- [Ecdysis archived overview](../../../../agentic-systems/reviews-archive/ecdysis.md) — its external scorer/editor contracts and strict score selection make an indirect admission comparison; the selected source comparisons are closer to the evaluation question, and this archived account must retain its inspected boundary.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) — retained project knowledge and absent later-productivity attribution overlap with the topic, but the general compounding protocol already gives the needed test without importing another system's machinery.

## Index Membership

None. Sources are outside the [tag collection's participating list](../../../../tags/COLLECTION.md). Do not propose membership in evaluation, theory-builder, or trace-learning heads merely because their topics fit. The sources landing is a format/workflow landing, not a curated paper roster. The legacy memory-system roster is frozen, and this ingest is not an accepted current agentic-system analysis set.

## Synthesis Opportunities

None. Effects evaluation, experimental contrast, local theory intervention, and later-improvement compounding already own the apparent higher-order claims. A new synthesis would mostly repeat their distinctions; the immediate opportunity is bounded examples in those owners.

## Maintenance Observations

- The [source ingest](../../../../sources/agent-plasticity.ingest.md) retains no verbatim quotes. Before promoting paper-dependent reverse links into library claims, a separate authorized grounding operation should retain the minimum supporting quotes, or the future citation should explicitly require the pinned snapshot. This connect run neither reads nor changes snapshot bytes.
- While following the [Faithful Self-Evolvers ingest](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md), its connection narrative says Agent Workflow Memory was one of the benchmarked frameworks, but its Summary lists ExpeL, Dynamic Cheatsheet, ReasoningBank, and G-Memory. Reconcile that internal discrepancy against its pinned source before using that particular cross-system claim; it is not needed for the comparison retained here.

## Flags

- **Evidence granularity:** acquisition efficiency, reuse attribution, local behavioral dependence, task improvement, and later-improvement productivity are separate claims. The board-game and NetHack results also have different evaluation controls. Preserve these boundaries in every accepted edge.
- **Analytical split review:** the discovery spans at least five notes across memory evaluation, theory-guided repair, persistent adaptation, and compounding. If derived writing attempts to carry those independent contributions as one note, split by claim. Keep the source ingest unified as the provenance owner; this flag does not authorize splitting or rewriting it.
- **Priority:** implement the effects requirement's bounded example first, matching the ingest's recommended next action. Other entries are optional navigation or narrowly scoped examples, not a request for a broad citation sweep.
