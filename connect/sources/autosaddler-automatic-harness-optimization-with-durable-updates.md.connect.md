---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/autosaddler-automatic-harness-optimization-with-durable-updates.md"
source_has_frontmatter: true
date: "2026-08-25"
depth: standard
---

# Connection Report: AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces

**Source:** [AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces](../../../../sources/.snapshots/autosaddler-automatic-harness-optimization-with-durable-updates.md)

## Discovery Trace

**Source framing:**

- Read the complete snapshot and the sources collection contract. The source presents an offline proposal-selection loop over prompt, tool, and middleware edits: trajectory diagnosis and structured patch generation produce candidates; same-mini-batch verification and development-set evaluation select them; reflection plus EvoDAG retains lessons and patch history for later search. Its experiments report results on GAIA2, SWE-Bench Pro, and Terminal-Bench 2.0, with ablations for diagnosis depth, intervention structure, phase scheduling, development-set filtering, and reflection/EvoDAG. The source fixes the model and outer optimizer, assumes supervised task success, excludes memory and skill curation, and recommends human/security review before production use.
- The snapshot has no `tags:` field, so no tag-README pass applied. The active authored surface would be the matching `.ingest.md`, which did not exist at discovery time; no candidate below recommends editing or durably linking to the immutable snapshot.

**Curated heads and complete listings:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md` before body search. The most relevant curated neighborhoods were learning/evaluation notes, trace-learning harness reviews, and whole-system self-improvement analyses.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over every authorised local destination. Counts were notes 363, reference 150, sources 305, agent-memory-systems 173, and agentic-systems 12. The title pass surfaced the diagnostic-richness, proposal-selection, experimental-contrast, fixed-decomposition, harness-optimization, and self-improvement neighborhoods evaluated below.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over every authorised local destination. Counts were notes 360, reference 149, sources 305, agent-memory-systems 171, and agentic-systems 10. No candidate was accepted from title or description overlap alone.

**Notes body search:**

- `rg -n -i 'failure[- ]trace|execution trace|trace-grounded|diagnostic richness|deep debugging' kb/notes/ --glob '*.md'` — kept diagnostic richness because AutoSaddler directly ablates the diagnosis surface; followed its Meta-Harness, Agentic Harness Engineering, HALO, and trace-learning-survey neighborhood.
- `rg -n -i 'validation set|held-out|generalization|regression|overfit|current-task fit' kb/notes/ --glob '*.md'` — kept the false-positive-acceptance note because the no-generalization-selection trajectory admits a broad hook and suffers a held-out regression spike; rejected current-task fit because it concerns the cost and reversibility of KB structural entrenchment rather than harness-patch selection.
- `rg -n -i 'harness optimization|prompt.*tool|tool.*prompt|retained instruction|system-definition artifact' kb/notes/ --glob '*.md'` — kept fixed decomposition because the paper's editable prompt/tool/middleware surface and explicit exclusions bound the result; rejected retained instruction because the more specific proposal-selection candidate already captures the paper's mixed code-and-text retention mechanism.
- `rg -n -i 'proposal-selection|search, evaluation.*retention|accepted edit|selection gate' kb/notes/ --glob '*.md'` — kept the proposal-selection loop as the exact functional decomposition and followed its false-positive-acceptance neighbor.
- Read the full experimental-contrast note after the ablation hits. Kept it because the headline ablations jointly remove multiple mechanisms while the appendix's finer-grained variants isolate only some of them.

**Reference body search:**

- `rg -n -i 'trajectory-aware|accepted edits|ablation|harness optimization|held-out|generalization' kb/reference/ --glob '*.md'` and `rg -n -i 'failure trace|execution trace|regression|patch selection|validation set' kb/reference/ --glob '*.md'` — evaluated the trajectory-aware evaluation, ablation-baseline, and gate-learning proposals. None passed the articulation test: each specifies a Commonplace review-system change or evaluates transformed outputs, whereas AutoSaddler uses trajectories to optimize an external agent harness. Source-to-reference also offers only sparse `see-also`, which would not carry the stronger methodological relation these hits would need.

**Sources body search:**

- `rg -n -i 'harness optimization|harness evolution|harness search' kb/sources/ --glob '*.md'` — kept Meta-Harness as the closest direct baseline and HarnessCompass as the closest independent structured/generalization-aware evolution method.
- `rg -n -i 'failure[- ]trace|trace.*diagnos|diagnos.*trace|root cause' kb/sources/ --glob '*.md'` — confirmed the above pair and surfaced Co-Harness's trace-attribution loop; kept Co-Harness for the fixed-model-versus-weight-coevolution contrast.
- `rg -n -i 'held-out|generalization-aware|dev-set|validation set|regression' kb/sources/ --glob '*.md'` — kept the phased agent-optimizer study because it tests later task arrival and re-optimization, a materially stronger durability question than AutoSaddler's one-run development/test transfer. Self-Harness passed topical recall but was rejected as a redundant peer for this report: its two-split gating axis is already represented by HarnessCompass and Auto Harness, while its same-model proposer allocation is not a foregrounded AutoSaddler claim.
- `rg -n -i 'structured patch|patch taxonomy|prompt.*tool.*middleware|capability patch|steering patch' kb/sources/ --glob '*.md'` — confirmed HarnessCompass and Co-Harness as the useful taxonomy/update-space comparisons.

**Agent-memory body search:**

- `rg -n -i 'harness optimizer|harness optimization|trace-driven outer loop|evolv|promotes evals|patch' kb/agent-memory-systems/ --glob '*.md'` and `rg -n -i 'held-out|generalization|regression|validation set|failure trace|execution trace' kb/agent-memory-systems/ --glob '*.md'` — kept the code-grounded Agentic Harness Engineering and Auto Harness reviews. Agentic Harness Engineering supplies the closest debugger-to-multi-component-edit implementation comparison; Auto Harness supplies an independently implemented train-trace, test-withholding, regression-suite, and score-gate comparison. The Meta-Harness review was not separately kept because its source ingest already supplies the direct paper-to-paper comparison and avoids duplicating one system in two forms.

**Agentic-systems body search:**

- `rg -n -i 'self-improv|evolv|rewrit|reflection|validation|regression|patch|trace' kb/agentic-systems/ --glob '*.md'` and `rg -n -i 'protected|rollback|held-out|generalization|failure diagnos' kb/agentic-systems/ --glob '*.md'` — kept Agno AgentOS because its analysis names the production promotion path that AutoSaddler partially realizes offline and the governance pieces AutoSaddler leaves outside the experiment. Followed Agno's comparison to Exo; rejected Exo because its self-rebuild/rollback loop lacks automatic behavioral candidate selection and is a broader architectural contrast than an execution-useful source link.

**Link following:**

- From diagnostic richness, followed Meta-Harness, Agentic Harness Engineering, HALO, and the trace-learning survey; these established that AutoSaddler is a new empirical case rather than a duplicate definition of the axis.
- From the proposal-selection loop, followed false-positive acceptance and fixed-decomposition links; these separated the selection-gate claim from the search-space boundary.
- From HarnessCompass, followed Meta-Harness, Self-Harness, Agentic Harness Engineering, and the phased optimizer study; this resolved the closest peer set and the distinct axes each retained candidate contributes.
- From Agno AgentOS, followed Exo; the traversal favored Agno's explicit held-out/canary/promotion gap over Exo's more general protected-substrate comparison.
- Read `kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md` as the relevant comparative catalog. It currently places Meta-Harness and Agentic Harness Engineering but not AutoSaddler, making it the only credible index-membership candidate.

**External destination:**

- The sources contract authorises already-known external targets, but external is not a prospecting surface. No user-supplied external candidate was in scope, so open-web prospecting was skipped.

## Connections Found

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **is-evidence-for**: AutoSaddler's no-in-depth-diagnosis ablation lowers GAIA2 development performance from 62.0% to 57.8%, while the full method gives the diagnosis agent the harness code and successful as well as failed trajectories. This is a new bounded case in which richer inspectable evidence improves proposal formation, distinct from the oracle that later selects patches.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **is-evidence-for**: the headline “structured intervention” arm removes both the patch taxonomy and phased scheduling, and the headline “generalization-aware selection” arm removes development filtering plus reflection/EvoDAG. The appendix's finer-grained variants narrow some attribution, so the paper is a worked example of bundle-level versus component-level experimental contrast.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **rests-on**: AutoSaddler's diagnosis/patch and evolution sessions search over candidate harnesses, same-batch and development evaluation can reject them, and the selected harness plus EvoDAG state become operative inputs to subsequent iterations.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) — **is-evidence-for**: without generalization-aware selection, a broad high-frequency tool hook is retained after fixing local cases and development regressions spike from 8% to 22%; the full method's reflection/selection path blocks the same regression-inducing patch. The case shows the behavioral cost of an acceptance error rather than merely the cost of generating a bad candidate.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **rests-on**: the reported gains range over a fixed model, prompt/tool/middleware intervention taxonomy, supervised success metric, optimizer roles, and stateless task assumption; the paper explicitly excludes memory and skill curation. The note supplies the scope boundary needed to avoid treating improvement inside that space as validation of the outer decomposition.
- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — **compares-with**: both optimize executable model harnesses from task trajectories, and AutoSaddler directly benchmarks against Meta-Harness; compare raw-trace proposer access and frontier search with AutoSaddler's explicit debugger, intervention taxonomy, development-set selection, and EvoDAG.
- [Ingest: HarnessCompass](../../../../sources/harnesscompass-guiding-automatic-harness-evolution.ingest.md) — **compares-with**: both separate structural/capability changes from textual guidance and add controls intended to prevent trajectory-specific repair. HarnessCompass uses grounded first-person feedback, two-track evolution, and disjoint/cross-model transfer; AutoSaddler uses diagnosis roles, phased scheduling, development selection, reflection, and untouched tests.
- [Ingest: Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) — **compares-with**: AutoSaddler tests retained patches within one offline optimization run and on a fixed untouched test set, while the phased study introduces new tasks and re-optimizes from the retained harness. The comparison prevents one-shot generalization from being read as evidence of later-update compounding.
- [Ingest: Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) — **compares-with**: both diagnose failed trajectories and validate local prompt/tool/middleware repairs, but Co-Harness alternates those repairs with model-weight updates and includes skills and memory in its declared harness. It exposes the fixed-model and fixed-edit-surface boundary of AutoSaddler's results.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) — **compares-with**: the code-grounded system also preserves raw execution traces, inserts a debugger report before evolution, and edits prompts, tools, middleware, skills, sub-agents, and memory. AutoSaddler provides a scientific-paper counterpart with structured ablations, development selection, and EvoDAG history, while Agentic Harness Engineering supplies implementation-grounded mutation and trace surfaces.
- [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) — **compares-with**: Auto Harness exposes train traces to a coding agent, structurally withholds test traces, gates edits on a regression suite and score frontier, and promotes fixed failures into future obligations. AutoSaddler instead uses explicit diagnostic/reflection roles and a three-way mini-batch/development/test protocol, making the pair useful for comparing how evidence separation becomes update control.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) — **compares-with**: Agno's analysis calls for a controlled path from production traces through isolated candidates, held-out/adversarial evaluation, capability-appropriate approval, version publication, canarying, and rollback. AutoSaddler experimentally realizes diagnosis, isolated code patches, held-out selection, and retained failed-attempt history offline, but leaves production authority, security review, canarying, and rollback outside its automated loop.

## Bidirectional Candidates

- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) ↔ the future AutoSaddler ingest — **compares-with**: Meta-Harness is AutoSaddler's closest named predecessor and direct experimental baseline; readers entering either analysis need the diagnosis/taxonomy/selection additions and the raw-trace/frontier-search baseline in the opposite direction.
- [Ingest: HarnessCompass](../../../../sources/harnesscompass-guiding-automatic-harness-evolution.ingest.md) ↔ the future AutoSaddler ingest — **compares-with**: the two recent systems independently partition intervention types and add generalization controls, but their evidence design and selection protocols differ enough that neither analysis subsumes the other.
- [Ingest: Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) ↔ the future AutoSaddler ingest — **compares-with**: the phased study should identify AutoSaddler as a strong static/generalization-aware optimizer whose “durable” claim still leaves later task arrival and re-optimization untested.

## Reverse-edge Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) → the future matching ingest — **evidenced-by**: add AutoSaddler's diagnosis ablation as a second bounded empirical case beside Meta-Harness, while preserving that only GAIA2 directly isolates the shallow-diagnosis variant.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) → the future matching ingest — **evidenced-by**: add AutoSaddler as a compact worked case where headline bundle ablations and appendix component removals license different attribution grains.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) → the future matching ingest — **evidenced-by**: add the admitted high-frequency hook and 8%→22% regression spike as an empirical illustration of a bad acceptance becoming operative, paired with the full method blocking that candidate.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) — rejected as too generic for an additional edge: AutoSaddler retains mixed executable and textual harness changes, and the selected-procedure point is already carried more precisely by the proposal-selection-loop connection.
- [Ingest: Self-Harness: Harnesses That Improve Themselves](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) — rejected to avoid a peer-method link spray: its two-split regression gate overlaps the generalization axis already supplied by HarnessCompass and Auto Harness, while its distinctive same-model proposer allocation is not a central AutoSaddler claim.
- [Exo](../../../../agentic-systems/reviews/exo.md) — rejected because protected substrate, rebuild, rewind, and failure-record preservation are an architectural self-modification comparison without AutoSaddler's automatic behavioral selection; Agno gives the more decision-relevant production-promotion contrast.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — rejected because it proposes how Commonplace should judge transformed workflow outputs, whereas AutoSaddler uses task trajectories to diagnose and edit an external harness.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) — rejected because its baselines are scoped to Commonplace's declared review objective; AutoSaddler is a useful analogy for experimental contrast but not evidence for the shipped-system proposal.
- [Gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md) — rejected because it concerns deriving semantic review criteria from accepted KB edits, not retaining benchmark-selected harness patches or optimizer lessons.

## Index Membership

- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — add AutoSaddler, after a matching ingest exists, to the source-grounded trajectory-run catalog and readable/symbolic harness-promotion branch. It adds a dedicated diagnosis layer, capability/steering patch schedule, three-level mini-batch/development/test evidence split, and EvoDAG optimizer memory beyond the catalog's current Meta-Harness and Agentic Harness Engineering cases; its evidence tier should remain paper-grounded rather than code-inspected.

## Synthesis Opportunities

None. The higher-order distinctions surfaced by this source already have homes in diagnostic richness, experimental contrast, proposal-selection loops, false-positive acceptance, fixed decomposition, and later-improvement compounding.

## Maintenance Observations

- Section 5.2 contains arithmetic/assignment inconsistencies. It describes 37.3%→46.9% as `+8.4 pp`, although the difference is 9.6 points and the abstract/conclusion report 9.6. It also describes 42.5%→46.9% as `+6.2 pp` and 43.3%→50.0% as `+4.4 pp`; those differences are 4.4 and 6.7 points, respectively, matching the abstract/conclusion but in the opposite assignment from the section prose. A future ingest should quote endpoints or tables and flag the prose inconsistency rather than silently selecting the erroneous deltas.

## Flags

- The snapshot is immutable and no matching `kb/sources/autosaddler-automatic-harness-optimization-with-durable-updates.ingest.md` existed at discovery time. All outbound, bidirectional, reverse-edge, and index recommendations must be applied to or link to that authored ingest only after it exists; none should be authored against `.snapshots/`.
- Split-candidate signal: the paper connects to five notes across diagnostic evidence, experimental attribution, proposal-selection safety, and update-space scope, and it advances multiple independent claims. Because source identity requires one snapshot/ingest pair, the future ingest should separate these as explicit analytical claim clusters rather than physically splitting the source analysis into unrelated ingest files.
- Terminology tension: AutoSaddler's “durable updates” are development-selected patches that transfer to an untouched fixed test set within one offline optimization study. That does not establish durability under later task arrival, a second optimization episode, production drift, or cumulative deployment; the phased optimizer comparison should remain attached wherever the durability claim is summarized.
