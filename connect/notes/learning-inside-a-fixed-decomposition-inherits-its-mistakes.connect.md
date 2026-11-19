---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md"
source_has_frontmatter: true
date: "2026-07-30"
depth: standard
---

# Connection Report: Learning inside a fixed decomposition inherits its mistakes

**Source:** [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md)

## Discovery Trace

**Source reading and authorisation:**

- Read the source in full. Its causal claim is that optimization cannot repair a consequential correction outside the effective update space determined by accessible information and histories, composable actions, and the hypothesis class. The three failure modes are information omission, action-closure omission, and hypothesis-class omission; the scope preserves fixed decompositions that are warranted or whose nominal interface still admits the correction.
- Read `kb/notes/COLLECTION.md` as the sole outbound authority. Authorised local destinations checked were `notes` (including `notes/definitions`), `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; `kb/work/` was excluded. The reserved `external` destination was not prospected because no external target was supplied and this run was repo-local.
- Re-read the existing source links before judging missing edges. The source already authors links to the proposal-selection loop, exact-implementation, local-use/rationale, scope-warrant, Bitter Lesson reach, ACM, Meta-Harness, diagnostic-richness, oracle-dependent memory policy, reflective machinery, and Co-Harness surfaces. Those authored edges were not re-proposed as outbound candidates.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/learning-theory-README.md`, and `kb/notes/deploy-time-learning-README.md`. `learning-theory-README.md` declares `covered_by` but not `complete: true`; `deploy-time-learning-README.md` also lacks `complete: true`, so neither matching by-tag description scan was skipped.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. No `kb/types/README.md` exists, so the types destination was assessed from its full title surface and scoped description/body searches.

**Full title surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`. Flagged reflective coverage, relaxing signals, the production-method reading of the Bitter Lesson, contextual action capacity, task-fitted structure, localized retention, and in-context learning for closer evaluation.
- Ran `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`, and `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'`. Flagged the fixed-source-bundle proposal, Meta-Harness, AgeMem, the trace-learning survey, Exo, concept bottlenecks, induction bias, Symbolic Learning, No Free Lunch, and Schmidhuber's learning-strategy report.

**Description listings:**

- Ran `rg -l '^tags:.*\blearning-theory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and `rg -l '^tags:.*\bdeploy-time-learning\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`. These confirmed reflective machinery, relaxing signals, the production-method note, diagnostic richness, oracle-dependent memory policy, and the source's already-authored decomposition-warrant cluster.
- Ran `rg -n -i '^description:.*(decompos|represent|learn|search|optim|operation|feedback|ontology|bottleneck|bias|outer.loop|reflect|hypothesis|action)' kb/reference/ --glob '*.md'`, then the same query separately over `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, `kb/instructions/`, and `kb/types/`. Reference yielded the fixed-source-bundle proposal and reflective-system descriptions; agent-memory yielded Meta-Harness and trace-learning systems; agentic-systems yielded Exo; sources yielded the concept-bottleneck, induction-bias, ACM, Symbolic Learning, No Free Lunch, and self-modifying-learning-strategy surfaces. Instruction and type hits did not articulate an operational or evidential reader need.

**Body searches:**

- Ran `rg -n -i "fixed (decomposition|representation|ontology)|decomposition.*(fixed|omission|learn|optim)|outside (the )?(update|search|learning)|effective update space" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions kb/types --glob '*.md'`. This confirmed the reflective-coverage and reflective-machinery neighborhood; scheduling hits used decomposition as task splitting rather than as a learner's expressivity boundary.
- Ran `rg -n -i "action set|action capacity|operation vocabulary|action basis|information omission|hypothesis.class omission|representational omission|update boundary|search space.*(omit|exclude|bound)|candidate.*(exclude|unreachable)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions kb/types --glob '*.md'`. This retained the relaxing-signals and self-modifying-learning-strategy candidates, and confirmed that the source already links the memory-policy note that mediates AgeMem's fixed operation set.
- Ran `rg -n -i "inductive bias|concept bottleneck|task[- ]fitted structure|feature representation|learn.*(representation|ontology)|representation.*learn|non.linearly separable" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions kb/types --glob '*.md'`. Concept bottlenecks, induction bias, No Free Lunch, task-fitted structure, and localized retention were evaluated as boundary or adjacent cases rather than direct support for inherited mistakes.
- Ran `rg -n -i "meta-decomposition|outer[- ]loop|jointly searched|co-evol|revision boundary|reflective loop" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions kb/types --glob '*.md'`. This retained reflective coverage, the production-method note, Exo, and the Schmidhuber source; it also confirmed that Co-Harness and reflective machinery are already authored links.
- Ran `rg -n -i "fixed decomposition|effective update|update space|action capacity|operation set|hypothesis class|learning boundary|relax" kb/instructions/ --glob '*.md'` and the same query over `kb/types/`. The only instruction hits concerned prose relaxation or unrelated gate examples; no procedure operationalizes the source's audit of effective update space, and no type spec observes or enforces it.
- Ran `rg -n -i "fixed decomposition|effective update|update space|action capacity|operation set|hypothesis class|learning boundary|mutable boundary|revision boundary" kb/agent-memory-systems/ --glob '*.md'`, then separately over `kb/agentic-systems/` and `kb/reference/`. AgeMem's fixed operation set is already mediated by the linked theory note; the trace-learning survey's “action capacity” is about promoted executable tools rather than missing corrections; Exo's configurable mutable boundary passed the articulation test; reference produced no equally precise system-level case.
- Ran `rg -n -i "fixed decomposition|effective update|update space|action capacity|operation set|hypothesis class|learning boundary|mutable boundary|revision boundary|concept bottleneck|inductive bias" kb/sources/ --glob '*.ingest.md'`. Kept Schmidhuber's self-modifying action language as a bounded answer to the open meta-decomposition question; rejected the remaining direct-source hits as already linked, mediated, redundant, or unable to demonstrate an omitted correction.
- Ran `rg -l 'learning-inside-a-fixed-decomposition-inherits-its-mistakes' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions kb/types --glob '*.md' | sort`. It returned no existing inbound link to the source.

**Link following:**

- Followed every existing source link one hop. The proposal-selection and scope-warrant notes have useful missing return paths: the source develops their epistemic search/scope limits into a causal expressivity boundary. The diagnostic-richness and memory-policy notes also benefit from return paths because the source prevents rich evidence or strong scores from being mistaken for an adequate state, action, or hypothesis space.
- Followed `reflective-coverage-is-graded-across-representational-forms.md` through representational form, behavior-determining organization, Commonplace's reflective-system case, and unified calling. Kept it because form coverage plus per-component operation profiles provide an audit vocabulary for deciding what actually lies inside a self-modifying system's update boundary.
- Followed `operational-signals-that-a-component-is-a-relaxing-candidate.md` through exact implementation, the codify/relax cycle, spec mining, and unified calling. Kept it as the operational response to a fixed proxy decomposition: detect brittleness or composition failure, preserve alternatives, and keep replacement cheap.
- Followed `the-bitter-lesson-selects-production-methods-not-representational.md` through representational-form coevolution, localized retention, reflective machinery, Meta-Harness, Symbolic Learning, and Co-Harness. Kept it because it applies the source's update-boundary condition to the learned-localized quadrant and identifies fixed artifact classes as a remaining limitation.
- Followed Exo into its memory-system companion and reflective-system definitions. Kept it as a descriptive boundary case: a protected substrate and rewritable executor make the mutable boundary explicit and configurable while leaving a deliberate fixed layer.
- Followed Schmidhuber's ingest into oracle-dependent memory policy, the proposal-selection neighborhood, and the self-improvement lineage. Kept it because its action language moves future learning strategy inside the update space while its programmer-chosen primitives and top-level payoff gate remain fixed.

**Per-destination evaluations:**

- `notes`: kept reflective coverage, relaxing signals, and the production-method note. Existing source links were not duplicated; contextual action capacity, task-fitted structure, localized retention, and in-context learning were rejected as adjacent but less precise.
- `reference`: evaluated the fixed-source-bundle proposal and the Commonplace reflective-system case. The proposal uses “fixed” to protect evidence provenance while allowing output split/drift/kill; the reference case is already mediated more generally by reflective coverage, so neither was retained.
- `agent-memory-systems`: evaluated Meta-Harness, AgeMem, and the trace-learning survey. Existing theory/source links mediate Meta-Harness and AgeMem more precisely, while promoted tool capacity is not the same as an omitted effective correction; none was retained.
- `agentic-systems`: kept Exo as the explicit configurable-revision-boundary case.
- `sources`: kept Schmidhuber's self-modifying learning-strategy report. ACM and Co-Harness are already linked; Concept Bottleneck Models, induction bias, Symbolic Learning, and No Free Lunch were evaluated and rejected as untested, boundary-only, redundant, or better mediated.
- `instructions`: honored the inverse-first posture. No procedure was found whose ordering, defaults, or stopping conditions operationalize this note, so no `operationalized-from` candidate or instruction reverse edge was retained.
- `types`: no type spec observes or implements the causal limitation, so no candidate passed the articulation test.
- Verified every path included below with `stat --format='%n' <paths>` after candidate selection.

## Connections Found

- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) — **mechanism**: form coverage and per-component operation profiles provide the audit vocabulary for determining which signals, mappings, and modification operations actually lie inside a reflective learner's effective update space
- [Operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — **extends**: turns the inherited-risk claim into a practical response by detecting brittleness and composition failure, preserving alternative decompositions, and keeping suspect fixed components replaceable
- [The Bitter Lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) — **extends**: applies the source's boundary condition to learned prompts, tools, code, and harnesses—search over localized artifacts escapes hand-crafting only to the extent that consequential artifact classes and their decomposition are themselves inside the search
- [Exo](../../../../agentic-systems/reviews/exo.md) — **evidenced-by**: its protected Rust substrate and rewritable executor make the revision boundary explicit and configurable, furnishing a concrete case where harness policy enters revision while canonical state remains deliberately fixed
- [Ingest: On Learning How to Learn Learning Strategies](../../../../sources/on-learning-how-to-learn-learning-strategies.ingest.md) — **evidenced-by**: self-modification programs place future action distributions and inductive bias inside the action language, while programmer-chosen primitives and the top-level payoff-per-time gate remain fixed, directly exhibiting both boundary expansion and relocation

## Bidirectional Candidates

- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) ↔ source — **extends**: the return path would supply the causal learning consequence of leaving a behavior-bearing form, mapping, or operation outside reflective coverage
- [Operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) ↔ source — **grounds**: the return path would explain why its fixed proxy components must remain replaceable—some corrections are unreachable until the decomposition itself is relaxed
- [The Bitter Lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) ↔ source — **grounds**: the return path would justify that note's warning that a search can optimize localized artifacts while still inheriting the fixed artifact classes and decompositions that define its candidate space
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) ↔ source — **extends**: the return path would develop “evaluation cannot select what search never reaches” into the stronger result that a fixed decomposition determines which distinctions, actions, and mappings can count as candidates
- [Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it](../../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) ↔ source — **extends**: the return path would show the causal cost of leaving a free-choice decomposition fixed while optimizing only variables inside it
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) ↔ source — **contrasts**: the return path would prevent readers from treating richer diagnostic evidence as a substitute for a state, action, or hypothesis space capable of expressing the correction
- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) ↔ source — **grounds**: the return path would supply the general causal mechanism behind that note's statement that reliable outcome ranking cannot teach a memory operation outside the supplied vocabulary

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Claw learning loops must improve action capacity, not just retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — its action-capacity claim broadens the system objective beyond retrieval, but it does not ask whether the learner's state, actions, or hypothesis class can express a needed correction
- [Task-fitted structure costs cross-task reuse](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — warns that a decomposition fitted to one question imposes reuse cost under question drift, but does not establish an unreachable learning update
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) — usefully describes the benefit of a matching decomposition, but the source's scope already preserves warranted fixed structure and the note does not develop the omission mechanism
- [In-context learning presupposes context engineering](../../../../notes/in-context-learning-presupposes-context-engineering.md) — relocates learning into the context-selection layer but does not test whether that layer's effective state, actions, or mappings omit the required correction
- [Automated note refinement as a search over a fixed source bundle](../../../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) — “fixed” protects the evidence anchor while set-valued output already admits split, drift, and kill, so it names a different role for stability
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) — the source already links both a theory note devoted to its ablation and the underlying ingest context, which mediate the relevant evidence more precisely than another descriptive-system edge
- [AgeMem](../../../../agent-memory-systems/lightweight/agemem.md) — its fixed operation set is the worked case behind the already-linked oracle-dependent memory-policy note; a direct edge would duplicate the mediated distinction
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — its action-capacity language concerns promotion of executable tools and workflows, not a comparison showing that a fixed update space omitted a required correction
- [Ingest: Concept Bottleneck Models](../../../../sources/concept-bottleneck-models.ingest.md) — the fixed concept vocabulary looks like a possible information or hypothesis-class omission, but the study assumes the vocabulary and does not test an incomplete, wrong, or contested set
- [Ingest: On the “Induction Bias” in Sequence Models](../../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) — demonstrates that a matching architectural bias can improve data efficiency, a boundary already represented in the source's scope; it does not demonstrate an omitted correction in the fixed architecture
- [Ingest: Symbolic Learning Enables Self-Evolving Agents](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) — broadens the editable harness surface, but the source already links the broader Co-Harness case and the retained production-method note mediates Symbolic Learning without redundant direct evidence
- [Ingest: The No Free Lunch Theorem](../../../../sources/no-free-lunch-theorem-no-universal-learning-algorithm.ingest.md) — explains why every learner carries inductive bias and why matching fixed structure can help, but it is an explainer rather than direct evidence of the source's three omission modes

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) — add under “Learning fundamentals” as the causal boundary on what deploy-time learners can revise when task representation, action basis, or hypothesis class remains fixed outside their effective update space

## Synthesis Opportunities

- **Learning loops have three non-substitutable adequacy boundaries.** This source supplies update-space adequacy (can the correction be represented and executed), [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) supplies proposal-evidence adequacy (can the learner infer what to try), and [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) supplies selection-signal adequacy (can outcomes rank attempts). Improving one cannot repair a failure in either of the others.

## Maintenance Observations

None

## Flags

None
