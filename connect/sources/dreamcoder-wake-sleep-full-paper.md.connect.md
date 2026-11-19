---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/dreamcoder-wake-sleep-full-paper.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: DreamCoder full paper

**Source:** [DreamCoder full-paper snapshot](../../../../sources/.snapshots/dreamcoder-wake-sleep-full-paper.md)

## Discovery Trace

The snapshot is an immutable local input. Every outbound candidate below is therefore for a future matching full-paper ingest, not for the snapshot itself. The older DreamCoder ingest was excluded from source scans with `--glob '!dreamcoder*.ingest.md'` and was not opened or used as discovery evidence.

**Curated heads and linking contracts:**

- Read `kb/sources/COLLECTION.md`, which authorises prospecting in `notes`, `reference`, `sources`, `agent-memory`, and `agentic-systems`, excludes `work` and `instructions`, and assigns the labels used below. External prospecting was skipped because no external target was supplied.
- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/learning-theory-README.md`, `kb/notes/deploy-time-learning-README.md`, `kb/notes/artifact-analysis-README.md`, `kb/notes/self-improving-systems-README.md`, and `kb/notes/computational-model-README.md`. These routed the search toward representational-form coevolution, proposal selection, theory-mediated transfer, and learned symbolic artifacts. No by-tag scan was required because the snapshot carries no `tags` field.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. Read the outbound-linking sections of the four other collections before evaluating return-link candidates.

**Full title surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (413 titles), `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` (159), `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` (175), and `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` (14).
- Ran `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md' --glob '!dreamcoder*.ingest.md'` (356 titles). This surfaced the program-synthesis survey, the later sleep-consolidation paper, SkillRL, Soar chunking, Symbolic Learning, and the self-revising-discovery paper for closer evaluation.

**Description listing scans:**

- Notes: `rg -n '^description:' kb/notes/ --glob '*.md' | rg -i '(symbolic|neural|representational|bootstrap|wake|sleep|program induction|domain-specific|library|procedural|declarative|continual learning|learning loop|search policy|search heuristic|compression|abstraction|expertise|few-shot|sample efficiency|bitter lesson|human learning)'`. Kept the five general claims and one evidence casebook listed below; rejected generic continual-learning governance because DreamCoder does not address authority or deployment governance.
- Reference: `rg -n '^description:' kb/reference/ --glob '*.md' | rg -i '(learning|self-improv|adapt|search|selection|proposal|artifact|symbolic|parametric|library|source|evidence|ablation|trajectory)'`. The automated-note-refinement and ablation proposals were evaluated but rejected as Commonplace-specific designs with no direct DreamCoder mechanism to compare under the source collection's sparse `see-also` label.
- Agent memory: `rg -n '^description:' kb/agent-memory-systems/ --glob '*.md' | rg -i '(learning|self-improv|skill|procedural|symbolic|parametric|trace|replay|dream|library|abstraction|compression|search|evolution)'`. The trace-learning comparison was followed, but DreamCoder learns from a fixed training-task corpus rather than the live operational traces that delimit that survey.
- Agentic systems: `rg -n '^description:' kb/agentic-systems/ --glob '*.md' | rg -i '(learning|self-improv|evol|symbolic|parametric|search|library|abstraction|compression|dream|replay)'`. Autogenesis, Exo, and GBrain were evaluated; their whole-system mutation and harness-control questions do not supply a narrow reader-useful comparison to DreamCoder's program-library mechanism.
- Sources: `rg -n '^description:' kb/sources/ --glob '*.md' --glob '!dreamcoder*.ingest.md' | rg -i '(program synthesis|program search|symbolic|skill|procedural|meta-learn|learning how to learn|self-improv|wake|sleep|library|abstraction|compression|explanation-based|neural.*symbolic|symbolic.*neural|Bitter Lesson|concept bottleneck)'`. Kept three source comparisons and rejected Soar chunking, Symbolic Learning, and self-revising discovery as weaker or less direct comparisons.

**Body searches:**

- Notes: ran `rg -n -i 'declarative knowledge|procedural (knowledge|skill)'`, `rg -n -i 'symbolic.*(neural|parametric)|(neural|parametric).*symbolic'`, `rg -n -i 'bootstrap|bootstrapping'`, `rg -n -i 'domain-specific language|learned librar|library learning'`, `rg -n -i 'program induction|program synthesis'`, `rg -n -i 'wake[-/ ]sleep|sleep phase'`, `rg -n -i 'recognition model|search (policy|heuristic|strategy)'`, and `rg -n -i 'sample efficien|few-shot'` over `kb/notes/ --glob '*.md'`.
- Other collections: ran `rg -n -i 'DreamCoder|program induction|library learning|description[- ]length|neural.*symbolic|symbolic.*neural' kb/reference/ --glob '*.md'`; analogous searches including `wake[-/ ]sleep`, `replay`, and `dream` over `kb/agent-memory-systems/` and `kb/agentic-systems/`; and `rg -n -i 'program synthesis|program induction|library learning|wake[-/ ]sleep|description[- ]length|neural.*symbolic|symbolic.*neural|learned (library|abstraction)|skill bank' kb/sources/ --glob '*.md' --glob '!dreamcoder*.ingest.md'`.

**Link following and candidate evaluation:**

- Followed the theory-mediated-learning note to proposal selection, representational form, and formal reach-assessment. Kept it because the full paper supplies the exact description-length/Bayesian library objective that the note says its prior evidence boundary lacked.
- Followed the coevolution note to the Bitter Lesson production-method distinction and the readable-artifact loop. Kept coevolution and production method because DreamCoder jointly improves a symbolic library and a distributed-parametric recognition model, with ablations showing both contribute and the recognition model helps produce deeper libraries.
- Followed the bootstrap note to domain extensibility and proposal selection. Kept it because DreamCoder both demonstrates learned displacement of supplied domain knowledge and states the limiting costs and remaining supplied primitives.
- Followed the self-improving-systems casebook to reflective coverage. Kept the casebook because its DreamCoder row explicitly leaves the acceptance criterion unread, while this snapshot exposes the Bayesian/MDL gate; rejected reflective coverage as a direct edge because the paper does not itself establish the KB's causal self-representation criterion.
- Followed the sleep-consolidation, program-synthesis-survey, and SkillRL ingests. Kept them on, respectively, retained representational form under an offline schedule; learned versus supplied language/search bias; and symbolic/readable library plus learned policy coevolution.

## Connections Found

- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) -- **is-evidence-for**: DreamCoder retains reusable symbolic abstractions, reuses them across tasks, and mechanically selects library growth by a Bayesian description-length objective; the full paper therefore supplies the formal retention criterion and transfer mechanism needed by this conjecture, while not testing the note's proposed controlled distribution shifts.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **is-evidence-for**: DreamCoder's symbolic library reduces search depth while its distributed-parametric recognition model reduces breadth, and each bootstraps the other; ablations show both components contribute to held-out performance and learned recognition produces deeper libraries.
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- **is-evidence-for**: DreamCoder grows functional-programming, vector-algebra, and physics vocabularies from sparse starting primitives, but its high compute cost, per-domain bases, and recommendation to begin from richer general resources sharply bound what it demonstrates about outgrowing supplied specialization.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: the abstraction phase searches refactorings and candidate routines, rejects candidates that do not improve the Bayesian/MDL score, and installs accepted routines into the library that governs later program search; the recognition-model update is separately a direct gradient update.
- [The Bitter Lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **is-evidence-for**: DreamCoder is a bounded learned-localized case in which computation searches and selects symbolic library content while a neural model learns to use it, rather than symbolic form implying hand production.
- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) -- **is-evidence-for**: the full paper resolves that casebook's stated DreamCoder evidence gap by exposing the library's description-length/Bayesian acceptance criterion and also shows that the symbolic library uses proposal selection while the recognition network uses direct gradient updates.
- [Language Models Need Sleep](../../../../sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md) -- **compares-with**: both systems move learning into wake/sleep cycles and use replay plus generated experience, but DreamCoder retains reusable abstractions in an inspectable symbolic library while the later system consolidates into distributed-parametric weights.
- [Program Synthesis (Gulwani, Polozov, and Singh, 2017)](../../../../sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md) -- **compares-with**: the survey maps synthesis inside supplied specifications, program spaces, and domain biases, while DreamCoder makes the program library and search guidance themselves learned objects; the comparison isolates which framing and primitives remain supplied.
- [SkillRL](../../../../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md) -- **compares-with**: both couple a hierarchical reusable library with a learned policy that improves use of that library, but DreamCoder's library is executable lambda-calculus code selected by compression and SkillRL's is natural-language skills distilled from trajectories and coupled to reinforcement learning.

## Bidirectional Candidates

- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) <-> future full-paper ingest -- **evidenced-by** from the note side: replace the note's full-capture-unavailable limitation with the paper's explicit description-length objective, refactoring search, and held-out ablations, while preserving the note's stronger structured-shift claim as untested.
- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) <-> future full-paper ingest -- **evidenced-by** from the casebook side: update the DreamCoder row's unread evidential limit and distinguish its proposal-selected library update from its direct-gradient recognition update.
- [Language Models Need Sleep](../../../../sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md) <-> future full-paper ingest -- **compares-with** from the target side: retain the existing shared wake/sleep axis while grounding the DreamCoder half in the full paper's symbolic-library mechanism and ablations.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- DreamCoder demonstrates durable behavior-changing updates and a mechanical objective, but it does not address deployment authority, write governance, or regression control at the breadth this note claims.
- [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md) -- the paper's sleep-stage analogy is explicitly speculative and disclaimed as a biological model; it motivates phase functions but does not test the note's component-boundary claim.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- DreamCoder replays solved training tasks and abstracts their programs, but the comparison's declared population learns from operational sessions, event streams, agent turns, and run trajectories; adding DreamCoder would change that boundary rather than merely connect an instance.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- both systems alter retained behavior-determining structure, but Autogenesis is a whole-harness protocol-mutation analysis and no narrower shared mechanism would make a `compares-with` edge useful.
- [Automated note refinement as a search over a fixed source bundle](../../../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) -- both use search and selection over structured artifacts, but the proposal is a Commonplace-specific unsettled design and the source collection authorises only sparse `see-also` links into reference; topical analogy is insufficient.
- [Chunking in Soar](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md) -- both compile experience into reusable symbolic routines, but Soar variabilizes dependency-traced subgoal results into productions while DreamCoder searches semantic refactorings under a compression objective; the shared abstraction is already better expressed by the retained learning-theory candidates.
- [Self-Revising Discovery Systems for Science](../../../../sources/self-revising-discovery-systems-agentic-ai.ingest.md) -- both use description-length criteria, but one selects program-library abstractions inside a fixed meta-language and the other claims schema-level regime change; MDL alone does not supply a reader-useful comparison.

## Index Membership

None.

## Synthesis Opportunities

- The DreamCoder full paper, [Language Models Need Sleep](../../../../sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md), and [SkillRL](../../../../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md) jointly support a higher-order comparison: offline consolidation is a scheduling posture, while the retained result may be symbolic code, natural-language skills, distributed-parametric weights, or a coupled pair. No existing note title found in the scan owns that exact claim.
- DreamCoder's explicit depth/breadth decomposition suggests a narrower mechanism for [representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md): reusable symbolic abstractions shorten solution trajectories while learned guidance lowers branching entropy. This should first be incorporated as bounded evidence or tested against another system, not promoted as a universal law from one paper.

## Maintenance Observations

- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) says the available DreamCoder capture is abstract-only and does not expose a description-length retention gate. This full-paper snapshot now exposes that gate, so the statement is stale once a matching full-paper ingest exists.
- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) says DreamCoder's acceptance criterion is unread. The full paper gives the abstraction phase's Bayesian/MDL criterion, but also reveals a mixed update architecture that should not be flattened into one gate kind.

## Flags

- The source is an immutable snapshot; all authored links belong in a future matching full-paper ingest or in the target artifacts named under bidirectional candidates.
- Do not describe DreamCoder as wholly proposal-selected: symbolic library additions are candidate-selected under the Bayesian/MDL objective, while recognition-model learning is a direct gradient update.
