---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md"
source_has_frontmatter: true
date: "2026-08-27"
depth: standard
---

# Connection Report: The Bitter Lesson does not require everything to live in weights

**Source:** [The Bitter Lesson does not require everything to live in weights](../../../../articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)

## Discovery Trace

**Source and rules read:**
- Read `kb/cache/types/connect-report.md` for the report contract, the target article in full, and `kb/articles/COLLECTION.md` for outbound rules. The article argues that Sutton's 2019 Bitter Lesson constrains how behavior-shaping content is produced and selected, not the representational form where selected content must live. It then names credit assignment, evaluation quality, retrieval/maintenance cost, and revisable decomposition as the open problems for learned localized artifacts.
- The article collection authorizes outbound links to `kb/notes/`, `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/articles/`, `kb/instructions/`, `kb/tasks/`, and `external`, while excluding `kb/work/` and `kb/reports/`. External prospecting was skipped because the connect skill forbids open-web search and no new external target was supplied.

**Description listing scan:**
- `rg '^description:' kb/notes/ --glob '*.md' | rg 'Bitter|bitter|representational|localized|retention|scaling|continual|decomposition|parametric|oracle|artifact|weights|learning|credit|evaluation|self-improv|system-definition|retained'` flagged the source-note neighborhood and additional notes about deployed-system learning, explicit retention, diagnostic richness, proposal selection, typed verification, and evaluation automation. Kept candidates only when a reader following the article would get a distinct next step rather than a duplicate source-note path.
- `rg '^description:' kb/reference/ --glob '*.md' | rg 'review|freshness|artifact|Commonplace|learning|article|validation|system|architecture'` surfaced Commonplace-system docs and proposals, including `commonplace-as-an-instrument.md` and `ablation-baselines-for-the-declared-objective.md`. These were rejected as outbound article links because the source's argument is about learned artifacts generally rather than a Commonplace operative trace.
- `rg '^description:' kb/sources/ --glob '*.md' | rg 'symbolic|Memento|Co-Harness|Sutton|FunSearch|AlphaDev|learning|agent|harness|self|knowledge|weights|continual'` found Sutton 2019, Sutton-Javed 2026, Symbolic Learning, Memento-Skills, Co-Harness, Meta-Harness, SkillRL, and newer harness/self-improvement ingests. Kept Sutton 2019 and the three named system ingests as current article evidence; kept Sutton-Javed only as off-authorisation/bridge context because the direct contrast label is unavailable for article-to-source links.
- `rg '^description:' kb/instructions/ --glob '*.md' | rg 'article|publish|connect|ground|source|review|validate|learning|write'` found `publish-an-article.md`, connect, validation, grounding, and review procedures. Only `publish-an-article.md` articulates an operational next step, but it applies only after explicit promotion approval, so it was rejected.

**Topic indexes:**
- Read `kb/notes/README.md` and `kb/notes/tags-README.md`. The source article has no `tags:` frontmatter, so there were no source-matching tag READMEs to load.
- Read relevant curated heads identified from the title/description surface: `kb/notes/learning-theory-README.md`, `kb/notes/deploy-time-learning-README.md`, `kb/notes/artifact-analysis-README.md`, `kb/notes/self-improving-systems-README.md`, and `kb/notes/evaluation-README.md`.
- `learning-theory-README.md` pointed to deploy-time learning, representational form, verification, and recognition as the governing area; its `covered_by` mark routed discovery into child heads rather than a generic by-tag expansion.
- `deploy-time-learning-README.md` evaluated `retained-artifacts-enable-persistent-deployment-time-adaptation.md`, `readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md`, `treat-continual-learning-as-representational-form-coevolution.md`, `diagnostic-richness-constrains-outer-loop-learning-quality.md`, and `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`; the latter four were kept because they are the more specific onward routes for this article.
- `artifact-analysis-README.md` has `complete: true`; I skipped a by-tag `rg` for `artifact-analysis` and used the curated entries. It kept `definitions/representational-form.md` and rejected the broader four-field review vocabulary as unnecessary for this article's reader-facing path.
- `self-improving-systems-README.md` kept `a-proposal-selection-loop-requires-search-evaluation-and-retention.md` as loop-shape background but rejected broader reflection/autonomy material as belonging to later companion articles.
- `evaluation-README.md` kept `diagnostic-richness-constrains-outer-loop-learning-quality.md`; `evaluation-automation-is-phase-gated-by-comprehension.md` was rejected because the article names reliable evaluation without needing the staged verifier-construction procedure.
- Read destination `README.md` files for `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/articles/`, and `kb/instructions/`. Agent-memory and agentic-system heads pointed to system comparisons, but the article uses source ingests for its three system cases, so individual system reviews were not promoted.

**Full title surfaces:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` surfaced the full notes title surface. Kept titles included `The bitter lesson selects production methods, not representational forms`, `Localized retention pays when sparse changes have bounded impact in a matching decomposition`, `Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier`, `The readable-artifact loop is the tractable unit for continual learning`, `Treat continual learning as representational-form coevolution`, and `Learning inside a fixed decomposition inherits its mistakes`.
- `rg -N --no-heading -m1 '^# ' kb/articles/ --glob '*.md'` surfaced companion articles. `continual-learning-outside-the-weights.md` was kept because it directly extends the same disagreement into Sutton and Javed's later claim. `when-systems-learn-theories-about-themselves.md` was kept as a bidirectional candidate because it uses this article as text-versus-weights context. `moving-revision-decisions-into-the-automatic-system.md` and `theory-building-inside-the-system.md` were rejected as later downstream arguments.
- `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` surfaced article lifecycle ADRs and Commonplace architecture docs; none passed the articulation test for this article's reader-facing argument.
- `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md' | rg 'symbolic|memento|harness|sutton|FunSearch|AlphaDev|learning|agent|Gödel|knowledge|self'` surfaced the evidence set plus newer adjacent sources. Kept the named source ingests and Sutton 2019; rejected newer harness/self-improvement sources because they would broaden the article's evidence roster rather than connect the current draft.
- `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md' | rg 'Skills|Memento|Agent|Co-Harness|trace|learning|symbolic|weights|harness|Memory|system'` surfaced `trace-learning-techniques-in-related-systems.md`, `reviews/SkillRL.md`, `reviews/meta-harness.md`, and `reviews/agentic-harness-engineering.md`; rejected them as direct article targets because the source's current empirical section is source-ingest-grounded.
- `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md' | rg 'Autogenesis|Compound|Exo|harness|learning|bitter|self|agent'` found `autogenesis.md`, `compound-engineering-plugin.md`, and `exo.md`. Kept only the Compound Engineering plugin as an off-authorisation reverse-edge signal because its body explicitly applies the same bitter-lesson distinction to Markdown artifacts.

**Body search:**
- `rg -n "Bitter|bitter|representational form|localized retention|continual learning|decomposition|parametric|weights|credit assignment|oracle|artifact learning|search and learning|Sutton|FunSearch|AlphaDev|Memento|Co-Harness|Agent Symbolic Learning" kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems kb/articles kb/instructions --glob '*.md'` returned a large hit set; evaluated hits were filtered to artifacts whose claim or evidence would change a technical reader's next step from this article.
- `rg -n "the-bitter-lesson-does-not-require-everything-to-live-in-weights|Bitter Lesson does not require everything|bitter-lesson article|article on the bitter lesson" kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems kb/articles kb/instructions --glob '*.md'` found direct inbound links from `continual-learning-outside-the-weights.md`, `when-systems-learn-theories-about-themselves.md`, and `kb/articles/README.md`.
- `rg -n "Bitter Lesson|Sutton|representational form|source_notes|article|working paper|draft|publish" kb/instructions kb/tasks --glob '*.md'` found `publish-an-article.md`; rejected because the source article remains a draft and there is no explicit publication request.

**Link following:**
- Followed the source article's body and `source_notes` neighborhood into the production-method note, the bitter-lesson defense note, the unearned-reach note, localized retention, scaling absorption, readable-artifact loop, representational-form coevolution, fixed decomposition, parametric reproduction, commitment, oracle accumulation, and the three named system ingests.
- Followed the source ingests for Sutton 2019, Symbolic Learning, Memento-Skills, Co-Harness, and Sutton-Javed 2026. Kept the first four as direct evidence for the article's current claims; treated Sutton-Javed as a comparison/next-article bridge.
- Followed companion articles: `continual-learning-outside-the-weights.md`, `moving-revision-decisions-into-the-automatic-system.md`, `when-systems-learn-theories-about-themselves.md`, and `theory-building-inside-the-system.md`. Kept `continual-learning-outside-the-weights.md` as a forward companion and `when-systems-learn-theories-about-themselves.md` as bidirectional context; rejected the others as downstream of different questions.

## Connections Found

- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **extends**: the note carries the full two-axis argument and empirical burden that the article distills for external readers.
- [Representational form](../../../../notes/definitions/representational-form.md) -- **defined-in**: the article's central distinction depends on the natural-language, symbolic, distributed-parametric, and mixed-form vocabulary.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- **extends**: the note gives the mechanism behind the article's claim that localized artifacts can be efficient when change touches a few matched units with bounded dependency closure.
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- **extends**: the note develops the article's boundary between temporary scaffold absorption and durable structure recurring at a moving deployment frontier.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **extends**: the note develops the natural-language-plus-symbolic loop that the article names as the tractable artifact-learning target.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **extends**: the note turns the article's mixed-system framing into the broader claim that improvement loops across forms coevolve.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **extends**: the note provides the deeper argument for the article's warning that artifact learners can optimize within designer-chosen decompositions while leaving consequential fixed choices untested.
- [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) -- **contrasts**: the note separates content absorption into weights from authority-bearing record substitution, bounding what the article's weights-vs-artifacts argument does and does not need.
- [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) -- **extends**: the note develops one proposed way explicit artifacts can improve future learning by retaining checks, not only lessons.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **extends**: the note sharpens the article's credit-assignment discussion by separating selection oracles from the evidence a proposer needs to diagnose what to change.
- [Ingest: The Bitter Lesson](../../../../sources/sutton-the-bitter-lesson-original-essay.ingest.md) -- **evidenced-by**: the ingest is the tracked local source analysis for Sutton's 2019 production-method claim, which the article currently links only through the external primary page.
- [Ingest: Symbolic Learning Enables Self-Evolving Agents](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) -- **evidenced-by**: this source analysis grounds the article's Agent Symbolic Learning case and its limits around language-mediated whole-harness optimization.
- [Ingest: Memento-Skills: Let Agents Design Agents](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) -- **evidenced-by**: this source analysis grounds the article's persistent skill-folder learning case and its single-skill attribution and test-gate limitations.
- [Ingest: Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) -- **evidenced-by**: this source analysis grounds the article's mixed harness/weight coevolution case and its missing matched-ablation caveat.
- [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md) -- **extends**: the companion article takes up Sutton and Javed's stronger 2026 weight-plasticity claim after this article separates it from Sutton's 2019 essay.

## Bidirectional Candidates

- [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md) <-> source -- **extends**: readers benefit in both directions because this article supplies the 2019 Bitter Lesson boundary, while the companion article handles the later stronger Sutton/Javed continual-weight-learning position.
- [When systems learn theories about themselves](../../../../articles/when-systems-learn-theories-about-themselves.md) <-> source -- **see-also**: the self-theory article uses this article as the text-versus-weights context for objective-level ablations; a return path helps readers move between the artifact-learning question and the reflective self-improvement question.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- The whole-system analysis has a "The bitter lesson does not select against Markdown" section that would usefully point to this article, but `kb/agentic-systems/COLLECTION.md` authorizes outbound links to sources, external, notes, agent-memory-systems, reference, and instructions, not articles. Either extend the collection contract for article companions or reject the link as outside the current topology.
- [Ingest: Sutton and Javed on why AI models stop learning](../../../../sources/sutton-javed-why-ai-models-stop-learning.ingest.md) -- The source is a strong contrast for the article's thesis, but the article collection's `kb/sources/` labels are `evidenced-by` and `see-also`; `contrasts` is not authorized for article-to-source links. Use `see-also` only if the article wants a bridge to the later weight-plasticity position, or keep the source for the companion article where it is already central.

## Raw Text Candidates

None

## Rejected Candidates

- [The bitter-lesson defense portfolio has one load-bearing member for the form-only rebuttal](../../../../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) -- rejected as a direct article link because it is authoring/debugging context for the article's evidential burden rather than an onward path an external reader needs after the article.
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- rejected as already subsumed by the production-method note for this article's main path; it is useful if the article adds a paragraph on selection over structure, but the current prose does not need a second nearby bitter-lesson theory link.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- rejected because it is the broader deploy-time-learning frame; `readable-artifact-loop` and `representational-form coevolution` are more specific onward paths for this article.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- rejected because the article implies whole-system learning but does not need the full evaluation-boundary argument until the later continual-learning article.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) -- rejected for this article because its addressability argument is central to the Sutton/Javed sequel, while this article's narrower task is separating Sutton 2019 from a weights-only inference.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- rejected as definitional machinery behind several candidate notes; link it only if the article explicitly names proposal-selection as a term readers must follow.
- [Verification needs a typed target before it needs an oracle](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md) -- rejected because it generalizes the evaluator-domain problem but would over-expand the article's current evaluation paragraph.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- rejected because the article's "reliable evaluation" challenge is broader than this staged verifier-construction prescription.
- [Moving revision decisions into the automatic system](../../../../articles/moving-revision-decisions-into-the-automatic-system.md) -- rejected as downstream of Commonplace-specific revision allocation, not this article's Sutton-specific representational-form argument.
- [Theory building inside the system](../../../../articles/theory-building-inside-the-system.md) -- rejected as part of the later Naur/theory sequence; it depends on premises this article does not establish.
- [Publish an article](../../../../instructions/publish-an-article.md) -- rejected because it is a procedure for an explicitly approved promotion, not a concrete next step implied by this draft article.
- Agent-memory reviews surfaced by title search (`agent-skills-for-context-engineering.md`, `SkillRL.md`, `meta-harness.md`, `trace-learning-techniques-in-related-systems.md`) -- rejected because the article's current empirical section cites source ingests for named systems rather than code-grounded memory-system reviews.
- Agentic-system analyses surfaced by title/body search (`autogenesis.md`, `exo.md`, `compound-engineering-plugin.md`) -- rejected as direct outbound links because their system-specific arguments would broaden the article beyond its current Sutton-centered scope.

## Index Membership

- [Articles](../../../../articles/README.md) -- The source already belongs under "In draft"; the current entry accurately describes it as separating Sutton's 2019 search-and-learning claim from a weights-only extrapolation and naming credit assignment, evaluation, and decomposition revision as open problems.
- [Learning theory](../../../../tags/learning-theory-README.md) -- If article indexes ever list article companions from tag heads, this source belongs near the deploy-time learning and representational-form entries as a reader-facing synthesis of the production-method/form distinction.

## Synthesis Opportunities

- The source article plus [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md), [When systems learn theories about themselves](../../../../articles/when-systems-learn-theories-about-themselves.md), [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md), and [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) imply a higher-order synthesis on credit assignment across representational forms: how failures should be attributed among weights, natural-language artifacts, symbolic artifacts, evaluators, and decompositions. The current KB has pieces of this but no single note that names the cross-form credit-assignment problem as its own design target.

## Maintenance Observations

- `kb/articles/COLLECTION.md` authorizes outbound links to `kb/tasks/`, but this checkout has no `kb/tasks/COLLECTION.md`. Discovery treated `kb/tasks/` as a low-priority search surface and found no candidate. If tasks are meant to remain a durable article destination, the collection may need its own contract.
- `kb/agentic-systems/COLLECTION.md` does not authorize links to `kb/articles/`, even though `compound-engineering-plugin.md` has a section whose reader-facing argument would naturally point to this article. This is a collection-contract gap rather than a connection the report can authorize.

## Flags

- The source is not a split candidate: it makes one main reader-facing argument, with evidence and limits organized under that thesis.
