---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md"
source_has_frontmatter: true
date: "2026-11-03"
depth: standard
---

# Connection Report: The Architecture of Complexity (Simon, 1962)

**Source:** [The Architecture of Complexity](../../../../sources/.snapshots/herbert-simon-architecture-of-complexity.md)

The source is an immutable snapshot. Every outbound candidate below is a recommendation for the matching ingest, `kb/sources/herbert-simon-architecture-of-complexity.ingest.md`, which did not exist at report time. Durable links must target that ingest, never `.snapshots/`.

Source claims used for judging candidates:
1. Complex systems that arise by evolution tend to be hierarchies. The watchmaker parable (Hora vs Tempus) shows that stable intermediate subassemblies make assembly feasible under interruption. Without them, the chance of finishing a long uninterrupted sequence falls exponentially with its length.
2. Problem solving is selective trial and error. Subgoals and cues of progress act as stable subassemblies.
3. Hierarchies are nearly decomposable. Interactions within a subsystem are strong and fast, and interactions between subsystems are weak. In the short run, subsystems behave almost independently. In the long run, each depends on the others only in aggregate. Subsystems can be defined operationally by clusters of frequent interaction. The span of each level is limited.
4. Hierarchy and redundancy allow compact descriptions (the "empty world hypothesis"). Non-hierarchic systems may escape our observation and understanding.
5. State descriptions (blueprints) differ from process descriptions (recipes). Problem solving maps a goal state to a process that produces it.

## Discovery Trace

**Outbound section read:** `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags and other sources. `kb/work/` and `kb/instructions/` are excluded. The snapshot never authors links; the ingest does. Labels used, by destination: theory (`is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`); sources (`compares-with`, `see-also`); external (`derived-from`, `see-also`).

**Snapshot scan:** `grep -n -iE "decomposab|watchmaker|Tempus|Hora|state description|process description|redundan|subassembl|trial and error|selectivity|span|interaction"`, plus a second pass for "DESCRIPTION|empty|blueprint|recipe|...". This located the watchmaker section (~L347-410), problem solving and selectivity (~L570-690), near-decomposability (~L728-830), comprehension (~L1055-1100), simple descriptions and the empty world hypothesis (~L1105-1220), and state vs process descriptions (~L1227-1320).

**Description/title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'`, filtered with `grep -iE "decompos|modul|hierarch|compos|scope|boundar|interface|local|isolation|span|layer|compress|descri|regular|structure|split|area|tree|coupl|independ|context|aggregat|reuse|stable|evol|search"`. Flagged: localized-retention, learning-inside-a-fixed-decomposition, use-tests-a-decomposition-locally, decomposition-heuristics-for-bounded-context-scheduling, scenario-decomposition-drives-architecture, areas-exist-because..., short-composable-notes, topology-isolation-and-verification, feasibility-is-the-heaviest-forks-net-load, human-analogies-suggest-functions, addressability-grain, backtracking / failure-explanation / program-theory (search-control cluster).
- Ran `rg '^description:'` on those 17 candidates and read their tags.
- `rg -N -m1 '^# ' kb/theory | grep -iE "checkpoint|intermediate|subgoal|sub-goal|progress"` found llm-code-boundaries-are-natural-checkpoints and semantic-sub-goals-that-exceed-one-context-window.
- `rg -N -m1 '^# ' kb/theory | grep -iE "compress|redundan|regular|recipe|blueprint|generat"` found weight-resident-methodologies-compress-behavior, addressability-grain and reverse-compression. None addresses redundancy-enabled description in Simon's sense.
- `ls kb/sources | grep -iE "parnas|simon|complex|hierarch|compositional"` found the Parnas 1972 ingest, Tu's hierarchical-MAS ingest, 08-simplicity-hidden-in-complexity, gibson-1998 and language-model-harnesses-are-compositional-generalizers.

**Topic indexes:**
- `kb/tags/computational-model-README.md` (head and first sections). It routes decomposition-heuristics and bounded-context-orchestration under "Scheduling & Orchestration". This confirms the hierarchy/decomposition cluster lives there. No tag on the snapshot; tag assignment belongs to the ingest.
- `kb/tags/learning-theory-README.md`. Simon appears only via the 1983 learning definition (a different work).

**Body search** (over kb/theory, kb/reference, kb/agentic-systems, kb/agent-memory-systems, kb/sources, kb/tags):
- `rg -l -i "Simon"`: every theory hit cites Simon's *learning* definition or bounded rationality/attention economics, not this essay. No KB artifact cites *The Architecture of Complexity*.
- `rg -n -i "near.decompos|nearly decompos|near-decompos" kb`: zero hits outside the snapshot. The concept is absent from the KB.
- `rg -l -i "decomposab"`: archive proposal exceeding-a-review-budget-splits-the-task, plus five source ingests, all using "decomposable" loosely for task splitting. Rejected as keyword-only.
- `rg -l -i "modular"` / `"hierarch"`: led to localized-retention, use-tests-a-decomposition-locally, short-composable-notes, topology-isolation-and-verification and the Parnas ingest. The agent-memory-systems hits (atomic, cognee, VLM-wiki, agentic-local-brain) are hierarchical memory layouts and were rejected as keyword-only.
- `rg -l -i "watchmaker"`, `"subassembl"`, `"stable intermediate"`: zero hits.
- `rg -l -i "state description|process description"`: hits only in unrelated source ingests (agent-workflow-memory, world-models-life-mind-continuity, a Ukrainian prompt article) and the Sutskever-list chapters. Rejected.
- `rg -l -i "exponential(ly)? (decay|accumul)|decays exponentially"` found topology-isolation-and-verification (strong) and novel-memory-forgetting-techniques (rejected: forgetting curves).
- `rg -n -i "interaction (density|frequency)|dense interaction|loosely coupled|loose coupling|aggregate" kb/theory`: only compiling-coordination-preserves-primitive-not-aggregate-authority ("aggregate authority" is a different sense). Rejected.
- `rg -n -i "span|branching|managerial" decomposition-heuristics...`: no span/branching constraint named. The Tu ingest (L62) explicitly flags that gap.
- `rg -n "Parnas" kb/theory -l` found localized-retention, use-tests-a-decomposition-locally, first-principles-analysis, soft-bound-traditions and short-composable-notes. This confirms the Parnas cluster that Simon would join.

**Link following:**
- localized-retention → Parnas KWIC, reflection-buys-addressability, readable-artifact-loop bounded validation radius, use-tests-a-decomposition-locally. This is the KB's locality-of-change cluster. Simon's near-decomposability is the interaction-structure counterpart that is missing from it.
- topology-isolation-and-verification → Tu ingest, decomposition-heuristics, bounded-context-orchestration-model, MAKER. The hierarchy-vs-exponential-sequential-failure argument is there, but without its 1962 precedent.
- Tu ingest L62: "Managerial capacity as a branching constraint", described as a constraint "the KB's decomposition heuristics don't explicitly name". This is Simon's span of control.

**External:** the source URL is already in hand from snapshot frontmatter, so it was evaluated under `derived-from`. No web prospecting.

**Reference / agentic-systems / agent-memory-systems:** no plausible trigger. Hits were architectural decomposition descriptions of specific systems (autogenesis, agno-agentos, ai-agent-book) with no claim about why hierarchy works. Skipped after the body search.

## Connections Found

- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) -- **is-evidence-for**: the watchmaker parable is an independent 1962 form of the note's topology step. When a long sequence has a per-step failure probability, the chance of completing it decays exponentially. Stable intermediate subassemblies cap the loss per failure, so hierarchy bypasses the ceiling. Simon's failure mode is interruption that destroys partial work, not wrong outputs, so the essay bears on topology only. It says nothing about isolation or verification. That boundary is itself useful to the note's "simpler account" test.
- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) -- **is-evidence-for**: Simon treats subgoals and cues of progress as the problem-solving analogue of stable subassemblies. This bears on the heuristic "save reusable intermediates in scheduler state". His limited span per hierarchy level supplies the branching constraint that the Tu ingest says the note does not name.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../theory/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- **compares-with** (axis: what makes a decomposition keep effects local): the note uses Parnas's change-anticipation criterion and adds a bounded-impact condition. Simon's near-decomposability states that condition in structural terms: strong within-subsystem interaction and weak between-subsystem interaction. It adds a time-scale split, with independence in the short run and only aggregate dependence in the long run. That split could sharpen the note's "small, explicit impact closure".
- [Areas exist because useful operations require reading notes together](../../../../theory/areas-exist-because-useful-operations-require-reading-notes-together.md) -- **compares-with** (axis: how groupings are identified): Simon defines subsystems operationally, as clusters in a matrix of interaction frequency. The note derives areas from operations that need co-reading, and it treats membership rules as implementation choices. Both make interaction, not declared membership, the basis of grouping.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) -- **compares-with** (axis: describable structure depends on the describer): Simon argues that compact description depends on finding redundancy through "recoding". He adds that non-hierarchic systems may escape our understanding entirely. The note already cites Simon's bounded rationality, so the ingest would give that citation a second, more specific anchor.
- [Parnas 1972 ingest](../../../../sources/parnas-1972-criteria-decomposing-systems-modules.ingest.md) -- **compares-with** (axis: criterion for drawing module boundaries): Parnas draws boundaries around decisions likely to change. Simon locates boundaries where interaction is weak. Both are locality criteria, of different kinds: anticipated change vs interaction intensity. The KB already leans on Parnas, so the pair is a useful comparison.
- [Tu: structured test-time scaling / hierarchical MAS theory](../../../../sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md) -- **compares-with** (axis: why hierarchy defeats exponential sequential failure): Tu writes e^(-εW) and reduces sequential span to log depth. Simon's watchmaker makes the same probabilistic argument and adds bounded span. Tu's "managerial capacity" maps to Simon's span of control.
- External `https://www2.econ.iastate.edu/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf` -- **derived-from**: the ingest analysis is worked out from this captured PDF (JSTOR reprint of Proc. APS 106(6), 1962).

## Bidirectional Candidates

- [Tu: hierarchical MAS theory](../../../../sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md) <-> Simon ingest -- **compares-with**: a reader of Tu's formal result gains the classic precedent and the span-of-control framing for its branching constraint. Sources-to-sources `compares-with` is authorised in both directions.
- [Parnas 1972 ingest](../../../../sources/parnas-1972-criteria-decomposing-systems-modules.ingest.md) <-> Simon ingest -- **compares-with**: Parnas's ingest says downstream validation costs are "unproven". Simon's near-decomposability names the structural condition under which they would stay local.

## Reverse-edge Candidates

These would be authored from the theory side under `kb/theory/COLLECTION.md`, targeting the future ingest.

- [Topology, isolation, and verification form a causal chain...](../../../../theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) → Simon ingest -- **evidenced-by**: the watchmaker case qualifies the topology step. Hierarchy helps even without verification when failures destroy partial work, which bounds how far the chain is "strict".
- [Localized retention pays when sparse changes have bounded impact...](../../../../theory/localized-retention-pays-where-change-is-sparse-in-a-matching.md) → Simon ingest -- **evidenced-by**: near-decomposability qualifies the bounded-impact condition. Locality holds in the short run, and long-run coupling persists through aggregates.
- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) → Simon ingest -- **evidenced-by**: span of control as an unnamed branching constraint, and subgoals as stable intermediates.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- tempting via Simon's remark that non-hierarchic systems escape observation, but the axes differ: observer comprehension vs optimizer update space. The link would mislead.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../theory/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- part of the Parnas cluster but about rationale for transfer. Simon offers nothing on retained design rationale.
- [Short composable notes maximize combinatorial discovery](../../../../theory/short-composable-notes-maximize-combinatorial-discovery.md) -- cites Parnas modularity in passing. Simon's hierarchy argument does not bear on note length or combinatorial discovery; the match is keyword-level only.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) and [Learning is not only about generality](../../../../theory/learning-is-not-only-about-generality.md) -- cite different Simon works (attention economics; the learning definition). Linking would conflate the works.
- [Statecharts and programs differ in what they show, not in what they can compute](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) -- superficially parallels blueprint vs recipe, but Simon's state/process distinction concerns goal recognition vs production, not which control structure stays visible.
- [08-simplicity-hidden-in-complexity ingest](../../../../sources/08-simplicity-hidden-in-complexity.ingest.md) -- redundancy-enables-compact-description resembles compression-as-objective, but the ingest is about compression as a theory of generalization. Possible `see-also` at most. Held back as too weak to help traversal.
- [LLM↔code boundaries are natural checkpoints](../../../../theory/llm-code-boundaries-are-natural-checkpoints.md) -- "stable intermediate" resembles a checkpoint, but the note's claim is inspection/replay at a medium boundary, not loss-capping under interruption.
- Agent-memory-systems hierarchical-memory reviews (atomic, cognee, VLM-wiki, agentic-local-brain) -- keyword-only "hierarchy" of storage layout.

## Index Membership

None. Sources are outside tag participation. The ingest may carry `tags: [computational-model]` if its analysis substantively treats hierarchy as a scheduling/orchestration limit. Read the head's inclusion condition first.

## Synthesis Opportunities

The Parnas ingest, the Simon ingest, localized-retention and topology-isolation-and-verification together imply a higher-order claim that the KB has not stated. Decomposition pays through two separable locality conditions: change locality (Parnas: what will be edited together) and interaction locality (Simon: what affects what, and on what time scale). Hierarchy's reliability benefit (Simon's watchmaker, Tu) depends on interaction locality, not change locality. Do not create this note during connect.

## Maintenance Observations

- Near-decomposability has zero occurrences in the KB outside this snapshot, although the decomposition/locality cluster leans on Parnas alone. This is a vocabulary gap, and a later write could consider registering the term.
- The Tu ingest's quick-win (L62, naming managerial capacity as a branching constraint in decomposition-heuristics) is still open. Simon's span of control is a citable anchor for it.

## Flags

- Split candidate for the ingest: the essay makes several independent assertions (hierarchy via stable intermediates; near-decomposability; describability; state vs process descriptions) that land in computational-model, document-system and learning-theory areas. The ingest should foreground the first two, which carry all the kept connections.
- The ingest file did not exist at report time. Outbound and reverse-edge candidates target `kb/sources/herbert-simon-architecture-of-complexity.ingest.md` once written.
