---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/articles/moving-revision-decisions-into-the-automatic-system.md"
source_has_frontmatter: true
date: "2026-08-27"
depth: standard
---

# Connection Report: Moving revision decisions into the automatic system

**Source:** [Moving revision decisions into the automatic system](../../../../articles/moving-revision-decisions-into-the-automatic-system.md)

## Discovery Trace

The source has frontmatter but no `tags:` field, so there were no source-tag-matched by-tag scans. Search scores were not available from the repo-local tools.

### `kb/notes/`

- Read `kb/notes/README.md` and the complete `kb/notes/tags-README.md` hub. The title and description scans then warranted reading the curated heads for self-improving systems, learning theory, computational models, and evaluation; none declared completeness over this untagged source's candidate surface.
- Generated the complete title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and `rg '^description:' kb/notes/ --glob '*.md'`.
- Ran `rg -n -i 'admission|authoriz(e|ation)|warrant|successor|revision (decision|machinery)|self-revis' kb/notes/ --glob '*.md'`, `rg -n -i 'computational closure|human judgment|human[^.]{0,40}decision|moving[^.]{0,30}decision|automatic system|machinery' kb/notes/ --glob '*.md'`, `rg -n -i 'addressab|reflective|operative installation|continuity|repeatable' kb/notes/ --glob '*.md'`, and `rg -l -i 'model realization|requested model|execution provenance|actual execution' kb/notes/ --glob '*.md'`.
- Opened the candidates on explicit retention, methodology self-extension, authorization-to-force binding, warranted autonomy, terminal-objective revision, machinery persistence, proposal selection, automation boundaries, and reflective coverage. Followed their links one hop into the Commonplace reflective-system evidence, the six-path audit, the Gödel-machine case, proposal-selection anatomy, and the requested-versus-realized binding neighborhood.
- Kept explicit retention because it states the transport mechanism behind the article's central representation claim. Kept the methodology self-extension note because it distinguishes naming a decider from representing decision content. Kept the authorization-to-force note because it explains why live installation does not preserve admission legitimacy and what a channel must bind to the consumed version. Kept warranted autonomy because it supplies the oracle-domain limit on moving admission. Kept the objective-revision note because it materially bounds what represented purpose and the Gödel comparison can establish.
- The Commonplace reflective-system note was already encoded in `source_notes`, and its narrower six-path audit and tag-README trace are already reader-facing links. The machinery-persistence, proposal-selection, automation-boundary, and reflective-coverage candidates were rejected as less discriminating than the kept candidates, the Bitter Lesson reverse edge, or the direct operational evidence below.

### `kb/reference/`

- Read `kb/reference/README.md`, then scanned all titles and descriptions with `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` and `rg '^description:' kb/reference/ --glob '*.md'`.
- Ran `rg -n -i 'model realization|requested model|realized model|execution provenance|mis-?attribut|model identity' kb/reference/ --glob '*.md'`, `rg -n -i 'maintainer admission|admission|authoriz(e|ation)|who (may|can)|approval.*operative|adoption decision' kb/reference/ --glob '*.md'`, and `rg -n -i 'revision (path|decision|machinery|governance)|self-improv|successor|operative.*revis|change candidates' kb/reference/ --glob '*.md'`.
- Opened the model-selection regression, the change-candidate survey, the full tag-README improvement-loop mapping, and the model-partition registry proposal. Followed the regression's links one hop to ADR 034, the review-batch procedure, and freshness architecture.
- Kept the regression because it is the direct operative trace behind the article's model-realization claim. Kept the change-candidate survey because it substantiates the article's claim that noticing, drafting, and checking have moved while admission has not. Rejected the partition registry because requested partition identity is not execution evidence, and rejected the tag-README mapping as redundant with the article's existing audit and observed-trace links.

### `kb/sources/`

- Read `kb/sources/README.md`, then scanned the full title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` and `rg '^description:' kb/sources/ --glob '*.md'`.
- Ran `rg -l -i 'fixed (objective|evaluator|outer loop)|human[^.]{0,50}(adopt|approv|decision)|admission|authorization|warrant' kb/sources/ --glob '*.md'`, `rg -l -i 'self-revis|self-improv|harness[^.]{0,50}(edit|evol|updat)|revision decision|successor' kb/sources/ --glob '*.md'`, and `rg -l -i 'externaliz|addressab|explicit artifact|represent(ed|ation)[^.]{0,80}(decision|rule|authority|criterion)' kb/sources/ --glob '*.md'`.
- Opened the Gödel-machine ingest and the source analyses for harness engineering, Symbolic Learning, and Self-Harness. Followed the Gödel ingest into its retained comparison note and the harness reports into their fixed-evaluator and promotion-gate neighborhoods.
- No source candidate survived. The article already links the grounded Gödel-machine note, which is the better outward-facing theoretical target. The harness sources would add new empirical systems rather than support a claim the article currently makes; the whole-system Exo analysis below offers the more precise comparison on the article's six named axes.

### `kb/agent-memory-systems/`

- Read `kb/agent-memory-systems/README.md`, then scanned all titles and descriptions with `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` and `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`.
- Ran `rg -l -i 'self-modif|self-improv|harness[^.]{0,40}(edit|patch|evol)|promotion gate|acceptance rule' kb/agent-memory-systems/ --glob '*.md'` and `rg -l -i 'authorization|warrant|human review|fixed (objective|evaluator|outer)|model[^.]{0,40}(realiz|provenance)' kb/agent-memory-systems/ --glob '*.md'`.
- Opened the Exo memory review and the reviews of Agentic Harness Engineering, HyperAgents, and Auto-Harness. The source makes a whole-system revision-governance claim rather than a memory-subsystem claim, so none passed the destination trigger. The Exo whole-system analysis is the precise authored surface for the comparison retained below.

### `kb/agentic-systems/`

- Read `kb/agentic-systems/README.md`, then scanned all titles and descriptions with `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` and `rg '^description:' kb/agentic-systems/ --glob '*.md'`.
- Ran `rg -n -i 'self-modif|self-improv|revision|accept|gate|govern|fixed|objective|warrant|human' kb/agentic-systems/ --glob '*.md'`.
- Opened Exo, Autogenesis, GBrain, and Compound Engineering. Followed Exo's links one hop to its memory review, the proposal-selection model, warranted autonomy, and the reflective-system cluster.
- Kept Exo because it is a running comparison case on the article's named axes: an explicit mutable boundary, addressable machinery, a rebuild-and-restart installation path, rollback and continuity, computational adoption, and a warrant surface limited to build, tests, and immediate behavior. Autogenesis and GBrain were rejected as additional breadth after Exo supplied the most discriminating practical comparison.

### `kb/articles/`

- Read `kb/articles/README.md`, then scanned all titles and descriptions with `rg -N --no-heading -m1 '^# ' kb/articles/ --glob '*.md'` and `rg '^description:' kb/articles/ --glob '*.md'`.
- Ran `rg -n -i 'revision|admission|human|automat|self-improv|warrant|compounding|Gödel|maintainer' kb/articles/ --glob '*.md'` and the inbound search `rg -n 'moving-revision-decisions-into-the-automatic-system' kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems kb/articles kb/instructions kb/tasks --glob '*.md'`.
- Opened the continual-learning and Bitter Lesson articles, and inspected the already-authored inbound passages in the theory-building and self-theories articles. The source already links the latter two. Continual learning already links to this source but the source lacks the distinct outward continuation, so its missing source-to-target edge is retained under `Connections Found`, not as a new target-side return edge. The Bitter Lesson article does not yet link here and is retained as a reverse-edge candidate because its safe-decomposition-revision problem needs this article's six requirements.
- The source is already listed in the curated article README; no index candidate remains.

### `kb/instructions/` and `kb/tasks/`

- Read `kb/instructions/README.md`; `kb/tasks/` has no curated `README.md`. Scanned both destinations' complete title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`, `rg '^description:' kb/instructions/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/tasks/ --glob '*.md'`, and `rg '^description:' kb/tasks/ --glob '*.md'`.
- Ran `rg -n -i 'revision (decision|machinery|path)|maintainer admission|authorization|warrant|model realization|execution provenance|self-revis|self-improv' kb/instructions/ --glob '*.md'` and the same query over `kb/tasks/`.
- Opened the review-batch procedure while following the model-provenance evidence. It mitigates false finalization when concrete harness metadata exists but neither proves model realization nor gives the article's external reader a concrete next step. The recurring explanatory-reach task is already linked by the source. No new `procedure` candidate passed the articulation test.

### Excluded and external destinations

- Per `kb/articles/COLLECTION.md`, `kb/work/` and `kb/reports/` were excluded as durable link destinations.
- The `external` destination is authorized for article research, but no external target was supplied or already loaded as a research target. Open-web prospecting was therefore skipped.

## Connections Found

- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) -- **extends**: the article says moving a revision decision costs representation; this note supplies the mechanism, showing that explicit externalization is the only current transport that lets a criterion become durable, computationally writable, and selectively addressable without escaping governance.
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../../../../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) -- **extends**: the article's generic-maintainer gap is not closed by naming the maintainer; this note distinguishes routing a decision from representing its decision content and derives the form, verification, and authority meta-decisions that a self-revision method must settle.
- [A consumption channel delivers force without the history that earned it](../../../../notes/a-consumption-channel-delivers-force-without-the-history-that.md) -- **extends**: the article distinguishes substantive warrant from admission and requires authorization to be bound to the installed version; this note supplies the missing failure mechanism and control boundary, showing that a live channel confers force unless it checks an authorization covering the exact content, version, role, and use.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **extends**: the article contrasts Gödel-machine proof with Commonplace's human semantic gate; this note explains why handing that gate to a model would move the decision operationally without warranting it, and why only the oracle's domain determines which admission decisions can safely move.
- [Revising an improvement objective is licensed from outside it or is not improvement](../../../../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md) -- **extends**: the article requires purpose to be represented, but this note supplies the material boundary that representation alone does not cross: terminal-purpose revision needs an outside license, while a Gödel-machine utility rewrite is licensed only relative to its incumbent utility or a higher retained criterion.
- [Harness sub-agent model selection regression](../../../../reference/harness-sub-agent-model-selection-regression.md) -- **evidenced-by**: this is the direct operative trace for the article's model-realization gap, including 268 results persisted under false Luna provenance and the current distinction between a requested model binding and evidence of which model executed.
- [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) -- **evidenced-by**: the article says noticing, drafting, and checking have moved around a still-human adoption decision; this survey identifies the skills, mechanical checks, freshness signals, and agent initiative that perform that work and preserves the remaining explicit triage step.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: Exo is a running practical contrast on the article's six axes: its mutable boundary, self-map, edit/build/restart path, durable event record, and rollback preserve addressability, installation, and continuity, while its computational admission is warranted only by build, tests, and immediate-behavior checks.
- [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md) -- **extends**: this companion develops the article's represented-revision mechanism into an account of a governed artifact layer as a continual-learning substrate, and names evaluator calls and human admission as both the unresolved bottleneck and a cost in the proposed experiment.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [The Bitter Lesson does not require everything to live in weights](../../../../articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) → source -- **extends**: that article says artifact learning still needs a safe way to revise its update-space decomposition and counts human decisions in the scaling cost; this source supplies the six representational requirements and a worked Commonplace case for moving those revision decisions into machinery.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- relevant general anatomy, but the source already distinguishes proposal-selection from direct updates and links the six-path audit; the kept methodological-closure and warranted-autonomy notes add the missing decision-content and oracle boundaries.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- its verification ceiling is relevant to one of the six requirements, but presenting it as the onward path would understate the article's additional authority, installation, addressability, and continuity requirements; the warranted-autonomy candidate applies the verification claim at the needed gate.
- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) -- relevant to requested-versus-realized model binding, but the already-linked six-path audit applies that distinction to Commonplace and the harness regression supplies the direct evidence.
- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) -- directly relevant to revisable revision machinery, but its main development is a separate Bitter Lesson argument about replacing a frozen meta-method with governance; the warranted-autonomy candidate and the retained reverse edge from the Bitter Lesson article give this source's reader the more discriminating onward paths.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) -- a strong allocation trace, but the article already links both the observed tag-README trace and the broader six-path audit; the change-candidate survey supplies the otherwise unsupported broader claim about noticing and drafting.
- [Model-partition registry](../../../../reference/proposals/model-partition-registry.md) -- records requested review partitions and aliases, but explicitly does not establish execution provenance and therefore cannot support the article's model-realization claim.
- [Gödel Machines](../../../../sources/goedel-machines-schmidhuber.ingest.md) -- the source is already reached through the article's grounded Gödel-machine note, which gives an external reader the comparison, proof assumptions, and limits without duplicating source-level detail.
- [Self-Harness: Harnesses That Improve Themselves](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- a relevant bounded empirical loop, but adding it would create a new multi-system comparison; Exo's whole-system analysis covers the article's six named axes more completely.
- [Exo agent memory system review](../../../../agent-memory-systems/reviews/exo.md) -- contains useful promotion-gate detail, but the article's claim concerns whole-system revision governance; the agentic-system Exo analysis is the correct unit and already links this subsystem where needed.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- its versioned resource lifecycle and smoke gate are relevant, but it adds a second weak-semantic-gate comparison after Exo without changing the reader's conclusion.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) -- its machine-oracle loops and bundled-skill human checkpoint illustrate mixed admission, but the system does not exercise the article's full continuity and successor-governance comparison as directly as Exo.
- [Run review batches](../../../../instructions/run-review-batches.md) -- gives operators a bounded rule for recording concrete model provenance, but it neither establishes realized model identity nor supplies a concrete next step for the article's external reader.

## Index Membership

None. The source is already listed in `kb/articles/README.md` under the curated article sequence.

## Synthesis Opportunities

None. The source article is already the synthesis surface for the representation, authority, warrant, installation, and continuity claims surfaced here.

## Maintenance Observations

None.

## Flags

- **Split review:** the five retained note candidates span retention, methodology extension, authorization, evaluation, and objective governance, while the source makes independent claims about six path requirements, two audited gaps, and the Gödel-machine comparison. This meets the report type's breadth trigger. The claims currently serve one movement-of-decision thesis, so treat splitting as a review question rather than an automatic recommendation; model realization is the cleanest detachable case.
- **Gödel-machine purpose scope:** the statement that “every revision decision has moved” can be read as including the choice of terminal purpose. The retained objective-revision note says an objective change is an improvement only relative to the incumbent objective or another outside level; the Gödel machine may rewrite its utility only when the old utility licenses the rewrite. A future edit should scope the sentence to rewrite decisions under the incumbent formalization or state explicitly that terminal-purpose selection remains declared rather than internally warranted.
