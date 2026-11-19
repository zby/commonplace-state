---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/code-complements-weight-prompt-with-symbolic-operations.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connections: Code complements the weight–prompt pair with symbolic runtime operations

**Source:** [Code complements the weight–prompt pair with independently executed symbolic operations](../../../../notes/code-complements-weight-prompt-with-symbolic-operations.md)

## Discovery Trace

**Source and authorisation:**

- Read the source note, `kb/notes/COLLECTION.md`, and `kb/reports/types/connect-report.md` in full. The source distinguishes an interpreted, generally stochastic operation instantiated by weights plus prompt from a runtime-assigned symbolic operation instantiated by code plus runtime; it also claims that one code artifact can be consumed as prompt evidence and as executable symbolic state.
- The notes contract authorises prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; it excludes `work`. The reserved `external` destination was skipped because no external target was supplied or already loaded as a candidate.
- Read the main `README.md` for each authorised destination and the three source-tag heads: `kb/notes/computational-model-README.md`, `kb/notes/learning-theory-README.md`, and `kb/notes/constraining-README.md`. The learning-theory head routes through child tags but does not declare `complete: true`; none of the three heads justified skipping a by-tag sweep.
- Searched for existing source backlinks with `rg -n "code-complements-weight-prompt-with-symbolic-operations|Code complements the weight.?.prompt pair" kb/ --glob '*.md'`. The only durable library backlink is already authored from `natural-language-project-state-specializes-search-heuristics.md`; workshop hits were excluded rather than proposed.

**Fresh title and description surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each of the seven authorised local destinations. The notes surface highlighted the underspecification, LLM–code boundary, semantic-relocation, specification-level, progressive-constraining, cross-form-coverage, and readable-artifact clusters. Other destinations highlighted Claude Code dynamic workflows, Eigenius, o-o, ToolGate, and Memento-Skills for closer evaluation.
- Ran `rg -l '^tags:.*\bcomputational-model\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the corresponding `learning-theory` and `constraining` queries. These sweeps recovered the same operation-boundary cluster plus downstream continual-learning and reflective-architecture candidates.
- Ran `rg '^description:' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md' | rg -i 'model|prompt|code|symbolic|runtime|execution|interpreter|harness|mixed'`. The types surface exposed only structural contracts, reference hits described Commonplace implementation rather than the general operation distinction, and instruction hits did not operationalize this claim with additional ordering, defaults, or stopping conditions.

**Notes body search:**

- `rg -n -i "weight.?prompt|weights plus prompt|model-mediated operation" kb/notes/ --glob "*.md"` -- confirmed that the exact weight–prompt formulation is new; kept the underspecification foundation and recorded the existing natural-language-project-state edge rather than re-proposing it.
- `rg -n -i "symbolic operation|symbolic runtime|independent(ly)? executed" kb/notes/ --glob "*.md"` -- kept the boundary, progressive-constraining, readable-artifact, and cross-form-coverage notes; rejected downstream residue and theory-mediated-path uses that merely apply the already linked scheduler split.
- `rg -n -i "reinterpret|interpretation.*execution|execution.*interpretation" kb/notes/ --glob "*.md"` -- kept semantic relocation and specification-level separation because they respectively bound and contrast the source's independence claim.
- `rg -n -i "code.*prompt|prompt.*code|natural language.*code|code.*natural language" kb/notes/ --glob "*.md"` -- kept the readable-artifact loop and rejected the Bitter Lesson note because its operative distinction is production method rather than execution class.
- `rg -n -i "consumption path|operative part|same artifact|dual role" kb/notes/ --glob "*.md"` -- followed representational-form and action-model neighborhoods. The source already links the canonical representational-form definition; the action-model candidate was rejected because its use of “model-mediated” names mediation by a situation representation, not specifically an LLM weight–prompt call.

**Other-destination body search:**

- Ran `rg -n -i 'weight.?prompt|model-mediated|symbolic (operation|runtime)|code.{0,50}runtime|runtime.{0,50}code|prompt.{0,50}code|code.{0,50}prompt|reinterpret' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md'`.
- Read Claude Code dynamic workflows and Eigenius in full or through all claim-bearing sections. Both passed: the first has a model author JavaScript that a separate runtime executes, while the second interleaves kernel-owned symbolic evaluation with bounded model effects under explicit control.
- Read o-o in full. It passed specifically for the dual-consumption claim: one polyglot file is read by an updating model as project evidence and instructions, while its shell portion is also executed directly.
- Read ToolGate and Memento-Skills. ToolGate passed because probabilistic semantic selection is composed with typed preconditions, postconditions, and transactional symbolic state updates. Memento-Skills was rejected here because its evidence bears mainly on learning through mutable mixed-form skill bundles; it does not isolate the execution-class distinction as clearly as the retained system cases.
- No reference artifact, type, or instruction passed the articulation test, so no `evidenced-by`, `defined-in`, or `operationalized-from` candidate was forced into those destinations.

**Link following:**

- Read the complete candidate notes for underspecified instructions, semantic relocation, LLM–code checkpoints, specification-level separation, progressive constraining, cross-form boundary coverage, and the readable-artifact loop. Their claims divide into premise, mechanism, contrast, consequence, and learning-architecture roles rather than repeating one association.
- Followed the source's existing scheduler–LLM, bounded-orchestration, unified-calling, deployed-system, representational-form, and exact-implementation links. Candidates duplicating those routes were rejected; cross-form coverage survived because it governs responsibility transfer rather than merely making refactoring mechanically local.
- Checked the residue, theory-mediated-path, action-model, LLM-context, and Bitter Lesson neighborhoods as plausible adjacent clusters. They were rejected where the source's existing links or a more precise retained candidate already supply the reader need.
- Verified all 19 retained candidate, rejected-candidate, and index paths with `test -f` before writing this report.

## Connections Found

- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) -- **grounds**: supplies the one-to-many spec-to-program projection and the relative operational precision of code that underlie the source's distinction between prompt interpretation and runtime-assigned consequences.
- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) -- **grounds**: explains why model generation or selection of code moves semantic judgment upstream rather than making it disappear, while leaving the installed execution step mechanical.
- [LLM–code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md) -- **extends**: develops the operation split into a debugging and verification consequence: ambiguity and sampling collapse at the model-to-code transition and re-enter at the reverse transition.
- [Specification-level separation recovers scoping before it recovers error correction](../../../../notes/specification-level-separation-recovers-scoping-before-it-recovers.md) -- **contrasts**: shows a symbolic-looking DSL whose control structure is still model-interpreted, sharpening the source's rule that execution class follows the consumer rather than syntax or file form.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) -- **mechanism**: explains one path by which repeatedly interpreted behavior becomes an installed symbolic operation, while preserving the distinction between model-authored provenance and runtime execution.
- [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) -- **extends**: develops the governance consequence of transferring responsibility between the two operation classes; a reflective system must cover both forms and their mapping, not merely expose a common interface.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **extends**: places prompts and symbolic artifacts in one coupled learning surface around fixed or changing weights, turning the source's static operation complement into an optimization target with bounded validation paths.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- **evidenced-by**: a model authors a JavaScript orchestrator, then a separate sandboxed runtime executes its control flow and journal semantics, directly corroborating that model authorship does not make the installed operation model-mediated at each step.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) -- **evidenced-by**: its kernel owns typed program evaluation, state commits, and verification while registered handlers supply bounded model completions, providing a code-grounded composition of symbolic and model-mediated operations.
- [ToolGate](../../../../sources/toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md) -- **evidenced-by**: probabilistic semantic tool selection remains with the LLM while typed preconditions, postconditions, and no-commit-on-failure state transitions execute symbolically, a direct mixed-operation instance.
- [o-o](../../../../agent-memory-systems/reviews/o-o.md) -- **evidenced-by**: one polyglot document is read by an updating model as evidence and instruction while its embedded shell is executed as an orchestrator, concretely instantiating the source's same-artifact, different-consumption-path claim.

## Bidirectional Candidates

- [Specification-level separation recovers scoping before it recovers error correction](../../../../notes/specification-level-separation-recovers-scoping-before-it-recovers.md) <-> source -- **contrasts** from the specification-level note: the source gives the clean runtime-executed pole needed to understand why a structured DSL can recover scoping while remaining model-mediated.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) <-> source -- **grounds** from the progressive-constraining note: the source supplies the execution-class distinction that explains what changes after a stable interpretation is committed to code.
- [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) <-> source -- **grounds** from the cross-form-coverage note: the source defines the two operational endpoints between which responsibility moves.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) <-> source -- **is-evidence-for** from the system analysis: model-authored JavaScript plus separate runtime execution materially bears on the provenance-versus-execution claim.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) <-> source -- **is-evidence-for** from the system analysis: inspected kernel and completion-handler paths show symbolic control composed with bounded model effects rather than a model owning every transition.
- [ToolGate](../../../../sources/toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md) <-> source -- **is-evidence-for** from the ingest: the paper's explicit division between semantic ranking and symbolic state gates bears directly on the complementary-operation claim.
- [o-o](../../../../agent-memory-systems/reviews/o-o.md) <-> source -- **is-evidence-for** from the review: the inspected polyglot file is an unusually direct witness for one artifact carrying different operative parts under model and shell consumption.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) -- rejected as an edge because its “model-mediated” pathway means action selection through a representation of the situation, whereas the source uses the phrase for an LLM call instantiated by weights plus prompt; linking them without an explicit distinction would encourage a vocabulary conflation.
- [LLM contexts interpret instructions and content through the same token medium](../../../../notes/llm-context-interprets-instructions-and-content-through-one-medium.md) -- rejected because it supports the prompt-side role distinction, but the source's authored representational-form link and natural-language-project-state link already provide a more direct route for that need.
- [Residue classes need different mechanisms, so the architecture is mixed](../../../../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md) -- rejected because its symbolic-continuity application is downstream of the already authored scheduler–LLM mechanism and would not clarify the source's operation taxonomy.
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) -- rejected because it uses an artifact, model, evidence, and runtime as functional carriers but does not develop the weight–prompt versus code–runtime distinction beyond the more direct readable-artifact candidate.
- [The Bitter Lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- rejected because hand-authored versus learned production is orthogonal to model-mediated versus symbolic execution; a model-generated program can land on either side of the production axis while still executing symbolically.
- [Memento-Skills: Let Agents Design Agents](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) -- rejected because the paper supports mutable mixed-form memory and learning outcomes, but does not isolate the source's execution-class distinction as cleanly as Claude Code dynamic workflows, Eigenius, ToolGate, or o-o.

## Index Membership

- [Computational model](../../../../tags/computational-model-README.md) -- the selective head could place this note under “Foundations” as the explicit operation-level account connecting the underspecified-instruction framing to scheduler–LLM separation, unified calling, and specification-level boundary cases.
- [Constraining](../../../../tags/constraining-README.md) -- the selective head could place this note under “Definition and spectrum” after the underspecification foundation because it states what operationally changes when an interpretation crosses into executable symbolic form.

## Synthesis Opportunities

None. The higher-order claim that provenance, syntax, storage, and execution class are separate axes is already stated in the source through its installed-code and consumption-path sections rather than remaining implicit across the candidates.

## Maintenance Observations

- The phrase “model-mediated” names two different contrasts in the notes collection: this source means an LLM operation instantiated by weights plus prompt, while `an-action-model-matters-only-through-its-consumption-path.md` means action selection mediated by a representation of the situation. Both notes define their local use, but cross-note prose using the bare phrase could become ambiguous; a later vocabulary pass should decide whether the LLM-specific sense should be named `LLM-mediated` consistently.

## Flags

None
