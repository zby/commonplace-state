---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/how-to-recursively-improve-your-agents-2084301728363462919.md"
source_has_frontmatter: true
date: "2026-08-03"
depth: standard
---

# Connection Report: How to Recursively Improve Your Agents

**Source:** [How to Recursively Improve Your Agents](../../../sources/how-to-recursively-improve-your-agents-2084301728363462919.md)

## Discovery Trace

**Description listing scan:**

- Generated fresh complete title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: notes (329), reference (125), agent-memory-systems (172), agentic-systems (10), and sources (424).
- `rg '^description:' kb/notes --glob '*.md' | rg -i 'self-improv|recursive|proposal|selection|evaluation|probe|diagnostic|outer-loop|objective|specification|fixed|reflect|retention|oracle|eval|agent.*improv|improv.*agent'` flagged the self-improvement definition and casebook, proposal-selection, diagnostic-richness, evaluation-phase, proximate-target, fixed-decomposition, warranted-autonomy, oracle-accumulation, and readable-artifact clusters.
- Equivalent description scans over reference, agent-memory-systems, agentic-systems, and sources rejected Commonplace implementation documentation as too local, but retained the code-grounded Agentic Harness Engineering review, Exo, Self-Harness, the Self-Healing Agent Harness, and Towards Automating Eval Engineering as discriminating comparisons.

**Topic indexes:**

- Read `kb/notes/tags-README.md`, `kb/notes/self-improving-systems-README.md`, and `kb/notes/deploy-time-learning-README.md`. They routed the source to frame-indexed membership, proposal selection, actor allocation, diagnostic richness, and fixed-boundary learning rather than to a single “recursive” ladder.
- Read `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/reference/README.md`, and `kb/sources/README.md`. The source is a practitioner report about a whole improvement workflow, not a code-grounded system review or Commonplace reference artifact.

**Body search:**

- `rg -n -i "ashpreet|recursive auto-improvement|improve-agent|AgentOS|Radar|mine.*(usage|session).*probe|probe.*(usage|session)|one lever|re-run.*failed|fixed point|toward.*spec|against its own spec" kb/... --glob '*.md'` found no duplicate account. It found Agno only in the unrelated Pal memory-system review and exposed the closest mechanism-level source comparisons.
- `rg -n -i "outer-loop|proposal.selection|diagnostic richness|probe|judge|oracle|fixed decomposition|specification|self-improv|recursive|convergent|fixed point" kb/notes --glob '*.md'` retained [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md), [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), and [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md).
- The source's own effective update space was extracted explicitly. Signals and histories are the target instructions/specification, stored sessions, user questions and answers, visible fumbles, live API responses, tool calls, errors, debug logs, and framework documentation. Permitted responses are one-at-a-time rule additions/tightening, tool swaps, parameter tuning, code edits, restart, and rerun. The coding agent's edit-generating policy defines the expressible mapping from those signals to reachable agent configurations. Fixed outside the reported loop are the target specification, probe derivation method, expected-behavior format, judge, coding agent, AgentOS architecture, logging/API surfaces, stopping rule, and choice to rerun only failed probes.

**Link following:**

- Followed the proposal-selection note into the self-improving-system definition and boundary-case note. The source is right that it does not demonstrate recursive self-improvement in its strong compounding sense, but “one AI improves another” does not settle self-improvement membership: the composite coding-agent + target-agent + platform boundary can still self-improve under the KB definition.
- Followed diagnostic richness into Meta-Harness and Agentic Harness Engineering. The source supplies the same high-level trace-to-edit pathway but no ablation, implementation inspection, or independent evaluation showing which diagnostic surface causes improvement.
- Followed the proximate-target note into objective, oracle, and exact-implementation distinctions. “Every probe passes” checks conformity to the derived probe set; it does not warrant the fixed specification as a proxy for production quality or establish generalization beyond the optimized probes.
- Followed Exo's RSI analysis and safety boundary. Exo preserves rollback, protected state, and failed-attempt history, whereas this source recommends `--dangerously-skip-permissions` and reports no sandbox, reversible promotion gate, independent canary, or protected substrate.

## Connections Found

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: the coding agent searches over bounded agent edits, probe judgments reject unsuccessful configurations, and passing changes become operative in the restarted target agent.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: the workflow deliberately combines instructions, usage sessions, live trajectories, tool calls, errors, and debug logs so the proposer can derive probes and causal edit hypotheses rather than optimize from a scalar score alone.
- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) -- **rests-on**: convergence to “its own spec” and full probe passage establish achievement of a fixed target, while the report supplies no independent evidence that the target warrants broader production quality.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: the reported loop can search reachable instruction/tool/parameter edits but cannot repair or test mistakes in its fixed specification, probe generator, judge, platform architecture, or stopping rule.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **rests-on**: an unattended 300–500-probe overnight run is autonomous, but the source does not calibrate the judge or bound which code and tool changes its oracle can safely authorize.
- [Self-Harness: Harnesses That Improve Themselves](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- **compares-with**: both mine failures and revise harness artifacts, but Self-Harness contributes quantitative multi-model evaluation and a two-split promotion gate while exposing a similarly fixed outer method.
- [Towards Automating Eval Engineering](../../../../sources/towards-automating-eval-engineering-2079976006644072796.ingest.md) -- **compares-with**: both turn traces into executable probes, but the eval-engineering workflow makes user-guided task design and verifier-trajectory inspection explicit before optimization.
- [The Self-Healing Agent Harness](../../../../sources/the-self-healing-agent-harness-2048912026018484317.ingest.md) -- **compares-with**: both wire live failures into agent edits and re-grading; the self-healing account adds production ticketing, rollout gates, and blast-radius control absent from this pre-deployment loop.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- **compares-with**: the code-grounded system turns Harbor rollouts into debugger reports, versioned harness edits, predicted impacts, and regression attribution, providing an inspectable analogue to this source's claimed workflow.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: both discuss recursive improvement through code-editing agents, but Exo explicitly separates a protected substrate, rewritable executor, retained failed-attempt record, rollback, and bounded host controls from the mutable layer.

## Bidirectional Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) <-> source -- **evidenced-by** from the note: this is a concise practitioner instance of search/evaluation/retention over agent instructions, tools, parameters, and code.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) <-> source -- **evidenced-by** from the note: the source independently assembles specification, usage, live API, and log evidence for trace-conditioned proposal generation, though it does not test their causal contribution.

## Reverse-edge Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → source -- **evidenced-by**: add as a practitioner instance only if the note needs another concrete loop; Self-Harness already provides stronger empirical coverage.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) → source -- **evidenced-by**: use as independent practitioner convergence on combining usage traces and live logs, not as evidence that the chosen diagnostic bundle is optimal.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- rejected as supporting evidence because the workflow generates probes and expected behavior automatically from the same specification and usage data without reported manual failure analysis, judge calibration, or independent labels; it is instead a limitation lens.
- [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) -- rejected because the source only says failures “can” become evals; it does not show probe retention, maintenance, or reuse across later development cycles.
- [The self-improving-system definition classifies its boundary cases](../../../../notes/the-self-improving-system-definition-classifies-its-boundary-cases.md) -- rejected as a durable outbound edge because the ingest can state the boundary-dependent terminology tension compactly without requiring a second casebook link.
- [Pal](../../../../agent-memory-systems/reviews/pal.md) -- rejected: shared use of Agno AgentOS is implementation adjacency, not an articulated connection between memory and improvement mechanisms.
- [Commonplace as a reflective system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) -- rejected as too implementation-specific; the transferable self-improvement and evaluation notes are the relevant destinations.

## Index Membership

None

## Synthesis Opportunities

None. The source's central loop is already covered by proposal-selection, diagnostic-richness, fixed-decomposition, objective/target, and warranted-autonomy notes; it contributes a new practitioner instance rather than an uncaptured higher-order claim.

## Maintenance Observations

- The X snapshot tool omitted the required `description` and `genre` fields for this X Article. Ingestion must repair those capture metadata fields before validation; this is a snapshot conformance issue, not a connection candidate.

## Flags

- Experiment boundary: “7/10” to “every probe passes” is reported without the probe list, scoring method, before/after table, held-out evaluation, cost breakdown, judge calibration, or independent reproduction.
- Regression boundary: the source says each edit reruns only what failed. Unless the unseen final report reruns the complete suite, a fix can regress previously passing probes while the loop still claims convergence.
- Security boundary: the setup explicitly uses Claude Code with `--dangerously-skip-permissions`; the source reports no sandbox, least-privilege split, approval gate, rollback requirement, or protected mutable boundary.
- Terminology tension: the source's “not RSI” distinction is sound for compounding improvement of improvement ability, but “one AI improves another” does not by itself exclude self-improvement of the composite system under a declared boundary.
