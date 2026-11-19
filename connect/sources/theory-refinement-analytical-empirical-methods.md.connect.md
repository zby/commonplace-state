---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/theory-refinement-analytical-empirical-methods.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Theory Refinement Combining Analytical and Empirical Methods

**Source:** [Theory Refinement Combining Analytical and Empirical Methods](../../../../sources/.snapshots/theory-refinement-analytical-empirical-methods.md)

## Discovery Trace

**Source reading and authorization:**

- Read the complete snapshot, `kb/sources/COLLECTION.md`, and `kb/reports/types/connect-report.md`. The paper's central mechanism is to start with an imperfect propositional Horn-clause theory, use complete or partial proofs to localize suspect rules or antecedents, use induction to construct bounded repairs, and retain a minimally changed explanatory theory. Its independent results and limits include lower observed sample demand than ID3 in two domains, preservation or creation of intermediate concepts, exact consistency with the training set, exponential worst-case search, and a fixed acyclic propositional-Horn update space.
- The source contract makes the matching ingest the authored surface. No matching `kb/sources/theory-refinement-analytical-empirical-methods.ingest.md` exists. The authorized local destinations are `notes`, `reference`, `sources`, `agent-memory-systems` (named `agent-memory` in the label table), and `agentic-systems`; `work` and `instructions` are excluded. Authorized useful labels here are `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, and sparse `see-also`, filtered by destination. External prospecting was skipped because no user-supplied or already-loaded external target required evaluation.

**Curated heads and title surfaces:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source has no `tags:` field, so no matching-tag README or by-tag `rg` pass was required. To resolve the paper's evident learning-theory cluster, also read `learning-theory-README.md`, `deploy-time-learning-README.md`, `self-improving-systems-README.md`, `observability-README.md`, and `evaluation-README.md`.
- Generated each complete fresh title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: 403 headings in notes, 159 in reference, 175 in agent-memory-systems, 14 in agentic-systems, and 344 in sources.

**Description listing scan:**

- Counted the complete description surfaces with `rg '^description:' kb/<destination>/ --glob '*.md'`: 401 notes, 158 reference artifacts, 173 agent-memory artifacts, 12 agentic-system artifacts, and 344 source artifacts.
- Scoped the listings with `rg -i '^description:.*(theor|refin|revis|repair|failure|diagnos|empir|induct|abduct|symbolic|sample|learning|locali|explan|intermediate|rule|evidence)' kb/<destination>/ --glob '*.md'`. Notes yielded the five kept theory/refinement candidates below plus weaker bootstrap, delayed-feedback, and localization matches. Sources yielded the five kept comparison cases below. Reference yielded note-refinement and gate-learning proposals whose artifact and oracle problems differ from domain-theory repair. Agent-memory yielded the trace-learning synthesis and many system-specific rule miners; the synthesis is the useful comparison surface. Agentic-systems yielded no artifact whose central mechanism is explicit theory diagnosis and revision.

**Body search:**

- `rg -n 'EITHER|Theory refinement combining analytical' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` found the exact historical placement in the theory-mediated-system-learning note and no existing tracked ingest.
- In notes, `rg -n -i 'sample efficien|fewer (target |training )?(examples|observations)|structured shift'`, `rg -n -i 'failed? (proof|branch)|partial proof|diagnostic rich|locali[sz].*(failure|defect|repair|revision)|failure.*locali[sz]'`, and `rg -n -i 'explanatory structure|intermediate concepts?|selective revision|faithful rationale|fixed decomposition|update space'` separated the sample-efficiency, diagnostic, rationale, and fixed-boundary claims retained below.
- In sources, `rg -n -i 'approximate domain theor|imperfect (explicit |domain )?theor|theory refinement|theory-guided'`, `rg -n -i 'failure mining|prediction failures?|failed (proof|branch)|local edits?|diagnos.*(repair|revision|patch)|trace.*diagnos'`, and `rg -n -i 'intermediate concepts?|explanatory structure|symbolic librar|addressable theor|sample efficien'` surfaced Workspace Optimization, Self-Harness, MDA, TRACE, DreamCoder, and Concept Bottleneck Models. The first five survived the articulation test; Concept Bottleneck Models was rejected as a redundant direct edge after the more precise note-level landings were retained.
- In reference, `rg -n -i 'theory refinement|failure.*repair|refinement.*search|learn(ing)?.*gate|repair.*evidence' kb/reference/ --glob '*.md'` confirmed that the obvious hits concern note-identity search, semantic-gate learning, or review repair rather than revising an explicit domain theory.
- In agent-memory-systems, `rg -n -i 'failed task|failure feedback|failed trajectories|failure.*(rule|edit)|diagnostic|explicit.*(ADD|EDIT|REMOVE)' kb/agent-memory-systems/ --glob '*.md'` showed many individual implementations, but the collection synthesis already compares their ingestion, promotion form, authority, and evaluation gap and is therefore the least redundant target.

**Link following and candidate evaluation:**

- Followed the theory-mediated-system-learning note to its sample-efficiency, faithful-rationale, fixed-decomposition, delayed-feedback, Workspace Optimization, and draft-article neighbors. Kept the first four note mechanisms and Workspace Optimization; rejected the delayed-feedback note because EITHER is batch, externally targeted, and not longitudinal. The draft article passes the articulation test but falls outside the source contract's authorized destinations.
- Followed Workspace Optimization to diagnostic richness and fixed decomposition, then compared its typed ownership and replay path with Self-Harness's failure signatures and reject-capable gate, TRACE's diagnosis-only endpoint, and EITHER's proof-localized, applied, training-consistent repair. All four provide a named comparison axis; the cross-case synthesis is recorded below.
- Followed the sample-efficiency note to MDA, DreamCoder, and Concept Bottleneck Models. MDA supplies the closest active-theory/sample-efficiency contrast; DreamCoder supplies the closest symbolic concept-creation contrast. Concept Bottleneck Models shares inspectable intermediates but only performs per-inference parametric correction, and the retained note candidates already carry that distinction more precisely.
- Read the trace-learning synthesis's recurring-stage model, representational-form comparison, diagnostic-richness section, borrowable mechanisms, and open limits. EITHER provides a useful historical formal comparator: its proof trace is semantically tied to the theory being repaired, and its promotion gate is exact training consistency, unlike the open-ended trace-to-rule systems surveyed there.

## Connections Found

- [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) -- **is-evidence-for**: EITHER is the note's explicit historical epistemic lineage—an imperfect addressable theory guides inference, empirical failures localize defects, and the theory itself is revised—while the paper's external classification target cleanly preserves the note's stated gap to reflective self-targeting.
- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) -- **is-evidence-for**: the promoter and soybean learning curves report that an approximate explicit theory plus labeled examples outperforms ID3 and can reach a given accuracy with fewer examples; this supports the conjecture's intermediate sample-efficiency premise but not its decisive controlled-shift, cross-shift reuse, or total-cost claim.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: EITHER consumes complete and partial proof structure to identify suspect rules and restrict the example set passed to induction, giving a formal historical instance of diagnostics shaping proposal search rather than merely selecting a winner; the paper contains no ablation isolating diagnostic richness.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) -- **is-evidence-for**: in an acyclic Horn theory, actual deductive and abductive proof paths are semantically tied to the downstream conclusion, so editing the implicated antecedent or rule supplies a constructive case where a faithful rationale enables premise-level repair; it does not test reconstructed natural-language rationales.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **is-evidence-for**: EITHER can move repair up the theory and create intermediate concepts, yet cannot express repairs outside its acyclic propositional Horn language and named operators—its stated negation-as-failure, relational, probabilistic, and category limits make the effective update-space boundary unusually explicit.
- [Workspace Optimization](../../../../sources/workspace-optimization-how-to-train-your-agent.ingest.md) -- **compares-with**: both systems turn prediction failure into localized edits of inspectable mixed reasoning state; EITHER attributes through formal proof structure and requires training consistency, while DreamTeam attributes through typed ownership and treats replay deltas as feedback after live adoption.
- [Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- **compares-with**: both mine structured failures into minimal local edits and preserve an incumbent structure, but Self-Harness uses model-inferred failure signatures plus a two-split regression gate over harness artifacts, whereas EITHER uses deduction/abduction plus inductive rule repair and guarantees consistency on the supplied examples.
- [Model Discovery Agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) -- **compares-with**: both combine explicit theories with empirical observations to reduce experiment or example demand; EITHER revises a supplied approximate theory from batch labels, while MDA expands candidate mechanisms and actively selects discriminating interventions with Bayesian machinery.
- [TRACE](../../../../sources/trace-trajectory-attribution-for-automated-context-engineering.ingest.md) -- **compares-with**: both walk failure evidence backward to a responsible symbolic component and constrain the repair target, but TRACE stops at a human-reviewed CRUD recommendation whereas EITHER applies the rule revision and checks the full training set.
- [DreamCoder](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) -- **compares-with**: EITHER's inverse-resolution concept creation and DreamCoder's library learning both compress corrected solutions into reusable symbolic intermediates; EITHER performs post-repair Horn-theory compression, while DreamCoder selects program abstractions through a description-length objective in a supplied DSL.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **compares-with**: EITHER is a useful pre-LLM formal comparator for the survey's trace-to-readable-artifact branch—proof traces and labeled failures drive explicit rule edits, while exact training consistency supplies a local promotion gate that the survey identifies as missing in open-ended domains.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

- [A research program for theory-mediated system learning](../../../../articles/a-research-program-for-theory-mediated-system-learning.md) -- the paper supplies the article's named theory-refinement lineage and an explicit-theory baseline for its proposed experiment, but `articles` is not an authorized destination in `kb/sources/COLLECTION.md`; either extend the source collection's destination/label authorization for articles or continue routing this support through the tracked theory-mediated-system-learning note.

## Raw Text Candidates

None

## Rejected Candidates

- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- EITHER prefers small syntactic changes and preserves intermediate structure, but it does not measure the dependency or validation impact closure required by this note; the shared word "local" is insufficient.
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- EITHER can revise supplied rules and create intermediate concepts, but its Horn language, objective, operators, and evaluator remain fixed, so it does not demonstrate the bootstrap's required ability to outgrow the outer method; the fixed-decomposition edge states the supported lesson more precisely.
- [Holding a program theory means sustaining coherent search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) -- EITHER shows theory-guided search and repair, but batch classification against immediate labels lacks the note's program-self-target, delayed consequence, recovery continuity, and later modified episode.
- [Automated note refinement as a search over a fixed source bundle](../../../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) -- the title-level refinement match is misleading: that proposal concerns identity drift, splitting, and non-convergence of prose artifacts, not fault localization and consistency repair in an explicit theory.
- [Concept Bottleneck Models](../../../../sources/concept-bottleneck-models.ingest.md) -- named intermediates and intervention create a real contrast, but the correction is per-inference and parametric rather than a retained theory revision; the sample-efficiency and faithful-rationale note edges already preserve the useful distinction without adding a redundant source-to-source edge.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- versioned mutation and rollback make it a broad self-evolving neighbor, but its whole-harness execution and extension architecture does not share EITHER's proof-guided explicit-theory repair mechanism.

## Index Membership

None

## Synthesis Opportunities

- [Workspace Optimization](../../../../sources/workspace-optimization-how-to-train-your-agent.ingest.md), [Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md), [TRACE](../../../../sources/trace-trajectory-attribution-for-automated-context-engineering.ingest.md), and this paper jointly imply that **failure localization and repair admission are orthogonal stages**. Direct ownership, model-mediated trace attribution, and formal proof paths can each nominate an edit site; live replay, human review, split regression, and exact example consistency then confer different authority on the proposed repair. The mechanism is already named as an extractable gap in Workspace Optimization's ingest but has no note-level owner.

## Maintenance Observations

- The immutable snapshot has no matching tracked ingest. Until `kb/sources/theory-refinement-analytical-empirical-methods.ingest.md` exists, there is no authorized surface on which to author these links and no durable local artifact that notes or comparisons may cite; consumers must not link to `.snapshots/`.

## Flags

- Scope guard for future consumption: the paper establishes batch repair of an external classification theory and bounded sample/accuracy results. It does not establish controlled-shift reuse, reflective self-modification, delayed longitudinal learning, natural-language-rationale faithfulness, or open-ended revision beyond its fixed formal language.
