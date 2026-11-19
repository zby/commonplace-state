---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/chunking-in-soar-general-learning-mechanism.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Chunking in Soar: The Anatomy of a General Learning Mechanism

**Source:** [Chunking in Soar: The Anatomy of a General Learning Mechanism](../../../../sources/.snapshots/chunking-in-soar-general-learning-mechanism.md)

## Discovery Trace

**Collection contract and authored surface:**

- Read `kb/sources/COLLECTION.md`. It authorizes prospecting in notes, reference, sources, agent-memory systems, and agentic systems; it excludes work and instructions. The authorized labels used below are `is-evidence-for` and `compares-with`.
- The target is an immutable snapshot. `kb/sources/chunking-in-soar-general-learning-mechanism.ingest.md` does not exist, so every outbound candidate below is for that future matching ingest, not for an edit or durable link to the snapshot.

**Description and title listing scans:**

- Read the curated heads `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source has no `tags:` field, so no tag-README pass applied.
- Generated each complete destination title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`.
- Generated each complete description surface with `rg '^description:' kb/<destination>/ --glob '*.md'` for the same five destinations. No semantic scores were available. The scans foregrounded the whole-system learning, retained-artifact, behavior-changing-write, two-layer execution, decision-surface capture, trace-learning survey, and explanation-based generalization candidates evaluated below.

**Body search:**

- Notes: `rg -n -i 'chunking|macro-operator|macro operator|production rules?|knowledge compilation' kb/notes/ --glob '*.md'`; `rg -n -i 'goal-based experience|goal experience|trace-extracted|trajectory-derived|distill(ed|ation)?.*(rule|skill)|rules?.*trajector' kb/notes/ --glob '*.md'`; `rg -n -i 'representation.*generali[sz]ation|generali[sz].*representation|implicit generali[sz]ation|continual learning|deployment-time learning' kb/notes/ --glob '*.md'`; `rg -n -i 'problem solver.*memory|performance system.*learning|learning mechanism.*architecture|system.*unit of learning|unit of learning' kb/notes/ --glob '*.md'`; `rg -n -i 'referenced.*features|irrelevant.*features|representation.*bias|scope.*general' kb/notes/ --glob '*.md'`; and `rg -n -i 'search-control|operator implementation|behavior-changing|future behavior|future behaviour' kb/notes/ --glob '*.md'`. These searches retained five specific notes and rejected keyword-level or medium-specific analogies.
- Reference: searched `Soar|chunking|macro-operator|macro operator|production rule|knowledge compilation`, `trace-learning|trajectory|deployment-time learning|continual learning|behavior-changing`, and `generalization|representation.*learning|learning.*representation|source adoption` over `kb/reference/`. No shipped-system artifact gained a concrete traversal benefit from this historical learning mechanism.
- Agent-memory systems: searched `Soar|subgoal|macro-operator|macro operator|production rule|chunking`, `distill(ed|ation)?.*(rule|skill|workflow)|trajector(y|ies).*(rule|skill|workflow)|trace.*(rule|skill|workflow)`, `successful trajector|failed trajector|search control|operator implementation`, and `implicit generali[sz]ation|representation.*transfer|transfer.*representation|cross-task transfer` over `kb/agent-memory-systems/`. The comparative trace-learning survey passed; individual modern system reviews were useful one-hop comparisons but redundant as direct edges here.
- Agentic systems: `rg -n -i 'Soar|chunking|macro-operator|macro operator|production rule|knowledge compilation|trace learning|trajectory|deployment-time learning|continual learning|search-control|operator implementation' kb/agentic-systems/ --glob '*.md'` found only broad trajectory/governance overlap and the unrelated document-segmentation sense of chunking.
- Sources: `rg -n -i 'Soar|chunking|macro-operator|macro operator|production rule|knowledge compilation|explanation-based generalization|trajectory.*(rule|skill)|trace.*(rule|skill)|implicit generali[sz]ation|representation.*transfer' kb/sources/ --glob '*.md' --glob '!.snapshots/**'` retained the explanation-based-generalization comparison. Modern trajectory-to-skill sources were evaluated but added only a broad family resemblance already covered by the trace-learning survey.
- External prospecting was skipped as required. The already-known original source URL is present in the snapshot frontmatter, but `derived-from` belongs on the future ingest as ordinary source metadata rather than as a newly discovered connection.

**Link following:**

- Followed the neighborhoods of [the deployed-system unit](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), and [behavior-changing-write governance](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md). They separate the system boundary, persistent symbolic update path, and authority-control risk that the Soar paper demonstrates in different passages.
- Followed [theory and methodology as a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) to its existing Soar manual reference. The paper supplies the historical mechanism and macro-operator demonstration, while the note correctly treats cognitive architectures as comparison rather than evidence for its full maintenance policy.
- Followed [decision-surface capture](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) through its trace-extraction and authority neighbors. Soar's referenced lists and proposed production-trace dependency analysis give a concrete capture/extraction comparison, but do not establish the note's broader claim about human rationale-bearing structure.
- Followed [the trace-learning survey](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) into Agent Workflow Memory, ExpeL, and OS-Copilot. Those reviews sharpen the comparison, but the survey is the useful landing point: Soar supplies an earlier trace-to-symbolic-rule case with a fully specified trigger, source format, extraction rule, promotion store, and reinjection path.
- Followed [Explanation-Based Generalization](../../../../sources/explanation-based-generalization-unifying-view.ingest.md) into theory-mediated learning and actionable methodology. The direct source-to-source comparison passed; the broader theory-mediated-system claim did not, because Soar does not revise an explicit theory of itself.

## Connections Found

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: Soar's paper explicitly attributes the scope and generality of learning to the coupling among the learning mechanism, problem solver, production memory, and later elaboration, and its Eight Puzzle demonstration shows behavior changing through that whole organization rather than through an isolated learner.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **is-evidence-for**: at subgoal termination, Soar converts consulted prior-context elements and subgoal results into persistent production rules, installs them in production memory, and applies them during later decisions without changing model weights.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **is-evidence-for**: direct operator-implementation chunks could make Soar behave as though physical puzzle actions had occurred when they had not, so the experiment disables chunking in that problem space and permits only search-control chunks; this is a concrete operation-specific authority boundary on an automatic learning write.
- [Theory and methodology form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) -- **compares-with**: Soar chunks replace costly subgoal problem solving with direct production application, giving the note's slow-path/fast-path analogy a historically detailed comparison while leaving the note's derivation, coverage, and maintenance policies distinct.
- [Structure inference needs capture at the decision surface](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) -- **compares-with**: Soar records which pre-subgoal working-memory elements fired productions and uses those actual references as learned-rule conditions; its proposed dependency analysis further removes irrelevant references from false search paths, providing a concrete process-trace comparison without claiming to capture human rationale.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **is-evidence-for**: the paper contributes a primary historical trace-to-rule case whose stages map cleanly to the survey: subgoal termination triggers learning, production firings and working-memory references supply the trace, results and variabilized conditions form productions, production memory retains them, and elaboration reinjects them into later decisions.
- [Explanation-Based Generalization: A Unifying View](../../../../sources/explanation-based-generalization-unifying-view.ingest.md) -- **compares-with**: both mechanisms turn one problem-solving episode into a more operational rule, but EBG regresses through a proof licensed by a supplied domain theory and operationality criterion, whereas Soar selects conditions from actually referenced state under its production representation and architecture.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Frontloading is partial evaluation, not divide-and-conquer](../../../../notes/frontloading-is-partial-evaluation-not-divide-and-conquer.md) -- rejected because replacing repeated subgoal work resembles precomputation only at a high level; the note's claim depends on known LLM prompt inputs and execution-context economics that the Soar mechanism does not address.
- [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) -- rejected because the paper's task/knowledge/aspect generality taxonomy and speed gains are relevant background, but they do not materially test the note's broader Simon-derived capacity framework and would duplicate the more specific retained-artifact connection.
- [Commonplace agent-memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) -- rejected because it is a current implementation plan; the source offers historical mechanism evidence but no concrete dependency or shipped-state comparison for that plan.
- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) -- rejected because its “chunking” means document segmentation for ingest, not Soar's learned production compilation.
- [AI Agent Book](../../../../agentic-systems/reviews/ai-agent-book.md) -- rejected because its governed trajectory-to-knowledge workflow is only a broad contrast; the behavior-changing-write note and trace-learning survey provide narrower, more useful landing points.
- [Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) -- rejected as a direct edge because both compile experience into reusable behavior, but the extraction forms, evaluation regimes, and eras differ enough that the trace-learning survey already carries the useful shared axis without another pairwise link.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- The immutable snapshot has no matching ingest. Do not author any durable link to the snapshot; evaluate these candidates only while drafting or later editing `kb/sources/chunking-in-soar-general-learning-mechanism.ingest.md`.
- The source supports more than one independent assertion and connects to at least five notes across whole-system learning, persistent adaptation and governance, fast-path execution, and trace capture. Treat the future ingest as a split candidate at the claim-block level: keep architecture coupling, trace-conditioned generalization, and action-authority limits distinct even if they remain in one source analysis.
- Bidirectional and reverse-edge candidates are intentionally empty until an authored ingest exists, because other library artifacts must not link to `.snapshots/`.
