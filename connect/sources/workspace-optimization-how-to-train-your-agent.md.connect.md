---
description: "Discovery report for possible KB connections from the Workspace Optimization paper snapshot"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/workspace-optimization-how-to-train-your-agent.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Workspace Optimization: How to Train Your Agent

**Source:** [Workspace Optimization: How to Train Your Agent](../../../../sources/.snapshots/workspace-optimization-how-to-train-your-agent.md)

## Discovery Trace

**Collection and type checks:**

- Read `kb/reports/types/connect-report.md` and `kb/sources/COLLECTION.md`. The source collection authorizes local prospecting into `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`; it excludes `work` and `instructions`. The snapshot is immutable, so every retained outbound candidate below is for the future matching ingest's authored surface, not for an edit to the snapshot.
- Read the 2,481-line snapshot in full. Its frontmatter and full-source capture were readable. The independent source-side claims evaluated were the general workspace-optimization proposal, DreamTeam's typed multi-agent implementation, the executable world-model and commit-then-retrodict mechanism, regression replay, and the reported ARC-AGI-3 result.

**Curated heads and topic indexes:**

- Read `kb/notes/README.md`, `kb/notes/deploy-time-learning-README.md`, `kb/notes/self-improving-systems-README.md`, `kb/notes/agent-memory-README.md`, `kb/notes/context-engineering-README.md`, and `kb/notes/evaluation-README.md`. These routed the source toward readable-artifact learning, deployment-time writes, diagnostic evidence, credit assignment, and action-conditioned world models. The source has no `tags` field, so there was no source-tag by-tag sweep.
- Read `kb/reference/README.md`, then followed the agent-memory coverage and trace-learning references into `commonplace-agent-memory-gap-plan.md`, `agent-memory-coverage.md`, `tag-readme-trace-as-self-improving-loop.md`, and `where-change-candidates-come-from-in-commonplace.md`.
- Read `kb/agent-memory-systems/README.md` and `kb/agent-memory-systems/lightweight/README.md`, then followed the trace-learning neighborhood into Meta-Harness, AriGraph, Agentic Harness Engineering, Dynamic Cheatsheet, and Voyager.
- Read `kb/agentic-systems/README.md`, then evaluated Exo, Autogenesis, Compound Engineering, Fractal, and Claude Code dynamic workflows.
- Read `kb/sources/README.md`, then followed the closest source comparisons into Symbolic Learning, Continual Harness, Harness Continual Learning, Memento-Skills, Recuris, and Self-Harness.

**Full title and description scans:**

- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' --glob '!.snapshots/**' | wc -l` and `rg '^description:' kb/notes/ --glob '*.md' --glob '!.snapshots/**' | wc -l`: 398 titles and 396 descriptions.
- Ran the same two complete-surface queries over `kb/reference/`: 159 titles and 158 descriptions.
- Ran the same two complete-surface queries over `kb/agent-memory-systems/`: 175 titles and 173 descriptions.
- Ran the same two complete-surface queries over `kb/agentic-systems/`: 14 titles and 12 descriptions.
- Ran the same two complete-surface queries over `kb/sources/`, excluding `.snapshots`: 339 titles and 339 descriptions. These were lexical scans, so no relevance scores were available.

**Notes pass:**

- `rg -i '^description:.*(workspace|deployment-time|deploy-time|continual learning|self-improv|retained artifact|artifact loop|world model|counterexample|credit assignment|regression|trace|external state|frozen)' kb/notes/ --glob '*.md'` flagged the retained-artifact, readable-artifact, governance, diagnostic-richness, localized-retention, bitter-lesson, and world-model notes retained below.
- Body searches were `rg -n -i 'workspace|external state|frozen[- ]model|without weight'`, `rg -n -i 'credit assignment|failure attribution|typed slot|named owner|locali[sz]'`, `rg -n -i 'regression set|regression replay|counterexample|retrodict'`, `rg -n -i 'world model|action-conditioned|committed prediction'`, and `rg -n -i 'deploy-time|deployment-time|continual learning|retained artifact'`, each scoped to `kb/notes/ --glob '*.md'`.
- Followed the deploy-time-learning head through [retained artifacts](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [the readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), and [governed writes](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md). Followed [the bitter-lesson production-method note](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) into localized retention and its open cross-artifact credit-assignment problem. Followed the world-model note into action-model consumption and the symbolic-versus-parametric assessment distinction.

**Reference pass:**

- `rg -i '^description:.*(self-improv|agent memory|artifact|trace|workspace|adapt|learn|govern|harness|loop|external state|continual)' kb/reference/ --glob '*.md'` flagged the coverage, gap-plan, trace-loop, and candidate-formation documents.
- Body searches were `rg -n -i 'trace.*(search|evaluation|retention)|search.*evaluation.*retention'`, `rg -n -i 'session trace|candidate queue|replay|regression'`, and `rg -n -i 'agent memory|autonomous learning|behavior-changing'`, each scoped to `kb/reference/ --glob '*.md'`.
- Kept the Commonplace gap plan as a sparse companion because the paper supplies a bounded episode-local trace-to-repair instance while leaving the plan's cross-session trace retention, authority, and lifecycle questions open. Rejected the broader coverage and candidate-formation pages because the plan already carries the useful operator-facing comparison.

**Agent-memory pass:**

- `rg -i '^description:.*(trace|learn|adapt|self-improv|workspace|artifact|skill|world model|regression|failure|trajectory|external|frozen|harness)' kb/agent-memory-systems/ --glob '*.md'` identified trace-to-system-definition systems and in-run world-model memory.
- Body searches were `rg -n -i 'in-run|within.*episode|world model'`, `rg -n -i 'component-scoped|failure attribution|owner|localized'`, `rg -n -i 'regression|counterexample|replay'`, and `rg -n -i 'frozen.*(model|LLM)|trace-to-system-definition|executable.*memory'`, each scoped to `kb/agent-memory-systems/ --glob '*.md'`.
- Read the retained candidates in full or through all mechanism-bearing sections. Meta-Harness supplied the outer-loop, held-out harness-search contrast; AriGraph supplied an in-run advisory graph-world-model contrast; Agentic Harness Engineering supplied staged component diagnosis and regression-gated adoption; the trace-learning synthesis supplied the comparative taxonomy.

**Agentic-systems pass:**

- Read all 12 available descriptions with `rg '^description:' kb/agentic-systems/ --glob '*.md'`.
- Body searches were `rg -n -i 'workspace|world model|frozen (model|LLM)|without weight'`, `rg -n -i 'failure attribution|credit assignment|typed (artifact|slot|surface)|owner|component-scoped'`, `rg -n -i 'regression|counterexample|replay|rollback|rewind'`, and `rg -n -i 'trace|retrodict|committed prediction|artifact.*(edit|patch|rewrite)'`, each scoped to `kb/agentic-systems/ --glob '*.md'`.
- Kept Exo for its protected-substrate, broad-executor-rewrite, and evidence-preserving rewind contrast. Kept Autogenesis for its uniform versioned resource lifecycle and rollback contrast. Fractal's workspace is a mounted task directory, and Claude Code dynamic workflows retain orchestration only when explicitly saved; neither implements the paper's evidence-driven typed workspace learner.

**Sources pass:**

- `rg -i '^description:.*(workspace|frozen|weight|self-improv|harness|trace|world model|counterexample|regression|artifact|continual|test-time|symbolic|skill|external state|agent.*learn)' kb/sources/ --glob '*.md' --glob '!.snapshots/**'` identified the five retained comparisons.
- Body searches were `rg -n -i 'credit assignment|failure attribution|language gradients|textual gradients'`, `rg -n -i 'regression[- ]gated|regression set|counterexample|replay'`, `rg -n -i 'typed (artifact|slot|surface)|artifact ownership|named owner'`, `rg -n -i 'world model|retrodiction|action-conditioned'`, and `rg -n -i 'frozen (model|LLM)|without weight|beyond model parameters'`, each scoped to `kb/sources/ --glob '*.md' --glob '!.snapshots/**'`.
- Followed comparison links among Symbolic Learning, Memento-Skills, Continual Harness, Harness Continual Learning, Self-Harness, Recuris, the readable-artifact note, and the governed-writes note. The retained set spans direct owner routing versus model-mediated diagnosis, and live replay feedback versus unit-test, same-example rollback, or held-out admission gates.
- Ran `rg -n -i 'credit assignment|failure attribution|repair.*(gate|admi|accept)|typed owner|owner.*failure|admission.*repair' kb/notes/ kb/sources/ kb/agent-memory-systems/ --glob '*.md' --glob '!.snapshots/**'` to test whether the localization-versus-admission synthesis already existed. The hits discuss fragments of both mechanisms, but none names them as independent design axes.
- External prospecting was skipped as required. The paper's arXiv URL is source identity already present in snapshot metadata, not a discovered external connection; no other already-known external target was supplied.

**Candidate verification:**

- Verified every path linked below with `test -e`. All retained, rejected, and index-membership paths exist. No candidate target under `Connections Found` is raw text.

## Connections Found

- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: DreamTeam jointly revises natural-language role state and symbolic executable world-model code while a fixed model operates, and transition replay gives those readable edits an explicit validation neighborhood.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- **rests-on**: direct interface-level credit works only because each prediction is emitted by a named typed surface with an owner, while regression replay checks effects outside the initially blamed surface; the paper itself leaves the fixed decomposition as a limitation.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: typed diffs, an error ledger, peer audit, counterexamples, and transition replay give repair agents structured causal evidence beyond a final game score, although the paper does not ablate that evidence surface.
- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **is-evidence-for**: named interface ownership plus replay is a concrete bounded substitute for the cross-artifact credit-assignment machinery the note identifies as missing from learned localized systems.
- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) -- **compares-with**: both make action-conditioned predictions answerable to later observations, but the note's main route is distributed-parametric while DreamTeam uses executable symbolic state and commit-then-retrodict checks to support planning.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **compares-with**: DreamTeam gives code edits parse/load checks and replay feedback, but adopts live repairs without a rejectable pre-commit regression gate or automatic rollback, exposing the difference between diagnostic feedback and governed admission.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **compares-with**: the paper treats external artifacts as the trainable system boundary, but its DreamTeam evidence is in-run and level-local; it does not establish that selected workspace changes survive into later sessions, which the note requires for persistent deployment-time adaptation.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) -- **see-also**: DreamTeam is a concrete episode-local instance of trace capture, owner-routed diagnosis, artifact change, and replay, adjacent to the plan's unshipped cross-session trace, candidate, authority, retention, and behavioral-evaluation paths.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **is-evidence-for**: Workspace Optimization adds an online action-trace-to-typed-executable-workspace case in which ownership routes failures directly and historical transition replay supplies later feedback.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) -- **compares-with**: both keep model weights fixed and learn executable artifact state from traces, but Meta-Harness searches whole harness candidates across evaluation episodes behind held-out gates while DreamTeam patches a fixed typed workspace during one live episode.
- [AriGraph](../../../../agent-memory-systems/reviews/AriGraph.md) -- **compares-with**: both build action-relevant world state during a run, but AriGraph writes advisory triplets and embeddings for retrieval while DreamTeam writes executable dynamics, commits predictions before acting, and routes retrodiction failures to typed owners.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- **compares-with**: both convert structured execution evidence into component-scoped artifact repairs, while Agentic Harness Engineering stages diagnosis and regression-gates broad harness versions rather than immediately applying per-step workspace patches.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: Exo protects a substrate while allowing broad executor rewrites and preserves failed-attempt evidence across rewind; DreamTeam freezes the harness, edits narrower typed workspace surfaces, and preserves replay evidence without automatically rolling back a failed repair.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- **compares-with**: both expose addressable natural-language and symbolic update surfaces, but Autogenesis emphasizes uniform version history and rollback across resource classes while DreamTeam emphasizes direct per-transition ownership and retrodiction without a comparable versioned admission boundary.
- [Ingest: Symbolic Learning Enables Self-Evolving Agents](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) -- **compares-with**: Symbolic Learning propagates prompted language gradients backward across a graph and uses same-example rollback; Workspace Optimization routes failure directly to the interface that emitted the falsified prediction and uses historical transition replay as feedback rather than a hard gate.
- [Ingest: Continual Harness](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) -- **compares-with**: both adapt mixed artifact state without resetting a long embodied episode, but Continual Harness directly edits a broad prompt/sub-agent/skill/memory partition and may also train weights, whereas DreamTeam fixes weights and centers typed executable world-model predictions.
- [Ingest: Harness Continual Learning](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) -- **compares-with**: both update a fixed-model agent from post-execution evidence, but HCL isolates a jointly versioned candidate behind current-validation and historical-anchor commitment checks while DreamTeam patches live state and treats replay failures as further repair evidence.
- [Ingest: Memento-Skills](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) -- **compares-with**: both localize failure to an addressable mixed-form artifact, but Memento selects one skill and rolls back against a generated unit test while DreamTeam assigns every prediction to a typed surface and replays a regression set across transitions.
- [Ingest: Recuris](../../../../sources/recursive-experiential-working-memory-evolution.ingest.md) -- **compares-with**: both keep the base model fixed and turn structured traces into component-scoped repairs, but Recuris uses model-mediated localization and a deterministic held-out paired gate while DreamTeam relies on direct output ownership and live replay feedback.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None. The target is an immutable snapshot and the matching ingest does not yet exist, so no durable artifact may author a return link to this path. The strongest future return-link cases are already represented above as outbound candidates for the matching ingest and can be reconsidered after that durable target exists.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) -- the planner's use of simulated rollouts passes the articulation test, but the retained world-model candidate carries the same reader value plus the paper's distinctive commit-then-retrodict evaluation mechanism.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) -- rejected as a lexical collision: the paper's “workspace” includes behavior-shaping world-model and strategy artifacts, not only unfinished-work state.
- [Tag-README maintenance is a trace-driven self-improvement loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) -- search, evaluation, and retention are structurally adjacent, but the Commonplace-specific deterministic loop does not clarify the paper beyond the broader gap-plan comparison.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) -- the trace-learning and behavioral-evaluation gaps are relevant, but the gap plan owns their actionable sequence and makes this second reference edge redundant.
- [Dynamic Cheatsheet](../../../../agent-memory-systems/reviews/dynamic-cheatsheet.md) -- it offers a fixed-model online natural-language memory comparator, but lacks the typed executable world model, direct output ownership, and regression-replay combination that makes this source distinctive.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) -- executable skill memory is adjacent, but its cross-task skill accumulation does not supply the direct transition-level credit and replay mechanism; Memento-Skills is the sharper skill-level comparison.
- [Compound Engineering Plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- it retains lessons and regression tests around broader project work, but does not implement a standing live evidence-to-workspace optimizer; Exo and Autogenesis provide closer whole-system contrasts.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) -- “workspace” denotes a mounted task directory whose model-authored orchestration is normally ephemeral, not a typed trainable substrate revised from falsified predictions.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- it exposes runtime orchestration and an explicit save path, but not the paper's evidence-driven artifact-learning loop.
- [Ingest: Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- a genuine fixed-model harness-editing comparator, but its reject-capable held-out architecture is already represented more precisely by HCL and Meta-Harness; retaining it would add comparison volume without a new axis.

## Index Membership

- [Agent-memory lightweight coverage](../../../../agent-memory-systems/lightweight/README.md) -- if no inspectable DreamTeam implementation becomes available, a paper-grounded entry would add an online trace-to-executable-world-model system with an explicit in-run rather than cross-session boundary.
- [Agentic systems index](../../../../agentic-systems/README.md) -- if DreamTeam receives a whole-system analysis, it belongs here as a multi-agent harness whose scheduler, typed role ownership, shared workspace, tool use, and repair loop are all part of the result.

## Synthesis Opportunities

- This source plus [Symbolic Learning](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md), [Memento-Skills](../../../../sources/memento-skills-let-agents-design-agents.ingest.md), [Harness Continual Learning](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md), and [Recuris](../../../../sources/recursive-experiential-working-memory-evolution.ingest.md) imply a higher-order claim not yet captured: **readable-artifact learners separate failure localization from repair admission**. Localization ranges from direct typed ownership through single-skill attribution and backward textual propagation to model-mediated component diagnosis. Admission independently ranges from live patch plus replay feedback through same-example or generated-test rollback to held-out candidate gates.

## Maintenance Observations

None

## Flags

- **Split candidate:** the source connects to more than five notes across deployment-time learning, diagnostic evidence, credit assignment, artifact locality, and world-model assessment, and it makes independent framework, system-design, and empirical claims. A future ingest should keep those claims in distinct analytical subsections rather than treating “workspace optimization” as one result.
- **Empirical comparison caveat:** the reported DreamTeam mean combines one completed run with an operator-stopped partial second run, while the Symbolica comparator is a single run and provider/version conditions differ. A future ingest should not promote the table as a clean state-of-the-art comparison without preserving those limits.
- **Persistence boundary:** DreamTeam demonstrates adaptation within a game run and across its retained level history, not durable cross-session learning. The framework's broader “training” vocabulary should not erase that observed boundary.
