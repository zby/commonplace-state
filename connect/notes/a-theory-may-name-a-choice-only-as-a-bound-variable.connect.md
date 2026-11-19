---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/a-theory-may-name-a-choice-only-as-a-bound-variable.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: A theoretical artifact must preserve the scope of each named system choice

**Source:** [A theoretical artifact must preserve the scope of each named system choice](../../../notes/a-theory-may-name-a-choice-only-as-a-bound-variable.md)

## Discovery Trace

**Pinned source and governing contract:**

- Verified `sha256sum kb/notes/a-theory-may-name-a-choice-only-as-a-bound-variable.md` as `557fe2e99e75eb727c126a37ec58f701019387cb441a864de2ac040d51c8655c` before discovery. Read the complete 206-line source, the complete `kb/notes/COLLECTION.md`, and the complete connect-report type contract.
- The source claim is about communicative scope, not mandatory quantifier syntax: intended consumers must be able to recover both the assignment of every named system choice and its proposition-level role from context guaranteed within the interpretation and consumption boundaries. The placement consequence is secondary: once scope is recoverable, theory versus system record turns on what contribution survives. The historical audit is explicitly unreconstructable and does not independently warrant the general claim.
- `kb/notes/COLLECTION.md` authorizes local prospecting in `notes` (including `notes/definitions`), `types`, `reference` (including `reference/definitions`), `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; it excludes `work`. The reserved `external` destination is authorized only for already-known evidence/source targets. No external target was supplied or present in loaded context, so open-web prospecting was skipped.
- Applied only the source contract's per-destination labels. In particular, instruction links were treated as exceptional: source-to-instruction is eligible only as `operationalized-from`, while instruction-to-source reverse edges use the instruction contract's `rests-on` label. For reverse-edge evaluation, the complete `kb/instructions/COLLECTION.md`, `kb/types/COLLECTION.md`, and `kb/reference/COLLECTION.md` contracts were read.

**Curated heads and tag scans:**

- Read the complete destination heads `kb/notes/README.md`, `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`.
- Read all three matching note tag heads: `kb/notes/document-system-README.md`, `kb/notes/artifact-analysis-README.md`, and `kb/notes/foundations-README.md`. The `artifact-analysis` head declares `complete: true`, already links the source, and therefore licensed skipping `rg -l '^tags:.*\bartifact-analysis\b' ...`; its stale link text is recorded under Maintenance Observations.
- Ran `rg -l '^tags:.*\bdocument-system\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` over 26 tagged artifacts and `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` over 64 tagged artifacts. These scans surfaced the source's existing choice-classification neighbors, the warrant/scope cluster, and two selective heads where the source could improve navigation.

**Complete title and description surfaces:**

- Generated each authorized local destination's complete title surface once with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: notes 359 titles, types 10, reference 140, agent-memory-systems 173, agentic-systems 12, sources 289, and instructions 47.
- Enumerated each destination at description resolution with `rg '^description:' kb/<destination>/ --glob '*.md'`: notes 356 description lines, types 13, reference 139, agent-memory-systems 171, agentic-systems 10, sources 289, and instructions 99. Repeated description lines inside type/templates account for totals exceeding artifact counts.

**Notes prospecting:**

- Ran body searches with the exact patterns `named choice|system choice|design choice|selected value|residual choice`; `bound variable|quantif|binder|referent|assignment|ranged use|fixed use|substantive witness`; `consumption boundary|interpretation boundary|guaranteed context|self-contained|portable|isolated extraction`; and `system-specific|local label|transferable claim|theoretical artifact|theory.*scope|scope.*theory` over `kb/notes/ --glob '*.md'`.
- Tightened the recall pass with file-list searches for `consumption path|consumption boundary|interpretation boundary|guaranteed.*context|context.*guarante`, `self-contained|isolated extraction|quotation|independent retrieval|portable|packag`, `referent|assignment|binding|binder|bound variable|quantif`, and `system-specific|local label|selected value|substantive witness|fixed subject`.
- Kept [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md): it turns the source's general boundary condition into a retention rule for what a linked artifact or enforced path may safely supply.
- Kept [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md): it supplies the adjacent epistemic-scope layer that the source explicitly says recoverable semantic scope does not settle.
- Kept [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md): it distinguishes missing required origin context from the different failure of excess ambient context with no enforced local isolation.
- Kept [Model-resolved indirection adds interpretation work to LLM execution](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) as a reverse-edge candidate: its placeholder/binding case is a concrete instance of assignment that must travel inside the model's consumption boundary.
- Evaluated [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md), [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md), [Ad hoc prompts extend the system without schema changes](../../../../notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md), and [Descriptive link labels may supply the self-sufficiency a reconstruction gate would check](../../../../notes/descriptive-link-labels-may-supply-claim-self-sufficiency.md). The first two are broader premises already reached through the more precise durable-payload and model-resolved candidates; the ad-hoc-prompt example already routes to the context-scoping note; the descriptive-label conjecture's own ablation rejects its original label-based mechanism.
- The source already links [A framework rule with a boundary-preserving rival is not an inherited constraint](../../../../notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md), [Artifact classification separates content kind, lineage, and authority](../../../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md), [Areas exist because useful operations require reading notes together](../../../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md), [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md), and [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md). They were traversed but not re-proposed.

**Types prospecting:**

- Ran `rg -n -i "choice|scope|context|referent|theor" kb/types/ --glob "*.md"` and `rg -n -i "frontmatter|consumer|artifact" kb/types/ --glob "*.md"` after the complete title/description scans.
- Kept [Review gate](../../../../types/review-gate.md). Its self-containment rule pins the operative interpretation boundary to criterion text plus note text because those are the only hashed inputs; an outside contract dependency would not invalidate an accepted verdict. This is a concrete Commonplace case of the source's consumption-boundary rule.
- Rejected `kb/types/note.md`, `kb/types/instruction.md`, and `kb/types/type-spec.md`: their mentions of transferable theory, consumer context, and fixed choices are general authoring/type requirements, not a distinct application of named-choice assignment and role.

**Reference prospecting:**

- Ran the exact patterns `a-theory-may-name|choice-binding|bind choices|bind the choices|selected value|intended contribution`; `context guaranteed|guaranteed.*consumer|consumer.*guarante|self-contained|origin context|scope.*artifact`; and `notes.*choices|choices.*notes|reference.*selected|selected.*reference` over `kb/reference/ --glob "*.md"`.
- Kept [ADR 070: Notes bind choices; reference records Commonplace selections and state](../../../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md). It is the accepted Commonplace decision that applies the source's theory in both collection contracts and already carries the inverse `rests-on` edge to this source. A source-to-ADR `evidenced-by` return path would serve a different reader need: seeing the theory's concrete adoption and bounded consequences.
- Rejected `kb/reference/collections-never-own-frontmatter-semantics.md`: its self-containment argument concerns where Commonplace assigns frontmatter semantics, not whether an artifact preserves the assignment and role of a named system choice. The already-linked [Collection and text contract](../../../../reference/definitions/collection.md) supplies the vocabulary the source actually uses.
- `kb/reference/proposals/per-artifact-write-briefs.md` and `kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md` were evaluated and rejected because they are unadopted context-assembly designs and do not ground this settled semantic requirement.

**Agent-memory-system prospecting:**

- Ran file-list body searches for `bound variable|quantif|referent|binding|selected value|system choice`, `self-contained|context.*guarante|guarante.*context|consumption path|scope.*consumer`, and `transferable claim|theoretical artifact|system-specific|generaliz.*choice` over `kb/agent-memory-systems/ --glob "*.md"`.
- Evaluated `reviews/llm-context-base.md`, `reviews/o-o.md`, `reviews/gnosis.md`, the comparative review, and the review framework. Their hits concerned system configuration bindings, self-contained packaging, or review scope. None articulates the source's two-part obligation for assignment and proposition-level role, so no connection survived.

**Agentic-system prospecting:**

- Ran the same three scoped patterns over `kb/agentic-systems/ --glob "*.md"` and inspected the matching passages in `eigenius.md`, `fractal.md`, and `exo.md`.
- Rejected Eigenius's cache-key omission: it concerns semantic cache identity, not a consumer's recovery of a named choice. Fractal's bounded-context workbench and Exo's protected-boundary selection are system cases, but neither tests or explains assignment-plus-role scope in retained theory.

**Sources prospecting:**

- Ran file-list searches for `bound variable|quantif|referent|binding|selected value|system choice`, `self-contained|context.*guarante|guarante.*context|consumption path|scope.*consumer`, and `transferable claim|theoretical artifact|system-specific|generaliz.*choice` over `kb/sources/ --glob "*.md"`.
- Evaluated `the-nature-of-theory-in-information-systems-gregor-2006.ingest.md`, `the-anatomy-of-a-design-theory-gregor-jones-2007.ingest.md`, `smith-reflection-and-semantics-in-lisp-1984.ingest.md`, and `optimal-choice-of-hypothesis-is-the-weakest-not-the-shortest.ingest.md`. Gregor uses *scope* for a theory's generality and boundary statements, not for recovering a named selection's assignment and role. The Lisp source concerns reflection and causal self-reference, while the hypothesis source concerns model selection. None supports the source's specific claim closely enough for `evidenced-by`, `derived-from`, or `abstracted-from`.

**Instructions prospecting and inverse-edge pass:**

- Ran `rg -n -i "named choice|system choice|selected value|bind|bound variable|system-specific|transferable" kb/instructions/ --glob "*.md"` and `rg -n -i "scope|referent|assignment|consumer context|collection placement" kb/instructions/ --glob "*.md"`.
- Kept [Underspecified assertions](../../../../instructions/review-gates/semantic/underspecified-assertions.md). It turns an unresolved argument-relevant scope or choice into an executable semantic-review procedure: construct two reasonable readings, name the unresolved choice, test materiality, inspect nearby context, and stop at PASS/WARN/ERROR. That procedure operationalizes the source's defect class while leaving the source's open question about cheaper detection unresolved.
- The inverse direction independently passes the instruction contract: a meta-reader maintaining the gate benefits from a `rests-on` link to the source's narrower account of named-choice assignment and role.
- Rejected `accessibility/unidentified-references.md`: identifying what a proper noun names covers only a narrow referent problem and never checks the name's proposition-level role. Rejected `semantic/unearned-generality.md` and `prose/source-residue.md`: both police abstraction altitude or leaked source framing, not missing scope after a system-specific name is retained. `cp-skill-write/SKILL.md` applies collection placement but already loads the authoritative collection contract and adds no distinct named-choice test.

**Link following:**

- Followed one hop from all five existing note neighbors, the linked collection definition, and the seven strongest new candidates. The existing classification cluster led to `derivation-and-inheritance-give-starting-warrant-earns-scope.md`, which confirmed that epistemic scope is a later layer rather than a substitute for semantic scope. The context cluster led to `semantic-work-can-be-relocated-but-not-eliminated.md`, `ad-hoc-prompts-extend-the-system-without-schema-changes.md`, and `links-encode-conditional-possibilities-not-obligations.md`; these supported the durable-payload and context-isolation candidates but did not add a more precise edge. ADR 070's neighborhood confirmed that the reverse `rests-on` edge already exists. The gate and type-spec neighborhoods exposed the two independent meta-reader return paths listed below.

## Connections Found

- [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) — **extends**: develops the source's general guarantee boundary into a retention rule—inline the recognition, assignment, rationale, or fidelity that the intended path cannot reliably supply, while allowing a guaranteed path to carry the rest.
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — **contrasts**: separates the source's semantic question, “what proposition can the consumer recover?”, from the epistemic question, “what claim-and-domain unit does the evidence license?”
- [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md) — **contrasts**: the source diagnoses failure from missing required origin context, while this target diagnoses failure from excess ambient context with no enforced local isolation; both use scope language but require different repairs.
- [ADR 070: Notes bind choices; reference records Commonplace selections and state](../../../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md) — **evidenced-by**: the accepted decision applies this theory through the notes/reference collection boundary and records concrete consequences; its existing `rests-on` edge already supplies the inverse rationale path.
- [Review gate](../../../../types/review-gate.md) — **evidenced-by**: the type contract makes one consumption boundary operational—only note and criterion text participate in freshness—so any interpretation dependency outside that boundary must be copied into the criterion or it becomes invisible to invalidation.
- [Underspecified assertions](../../../../instructions/review-gates/semantic/underspecified-assertions.md) — **operationalized-from**: the gate adds a review sequence, a two-reading materiality test, nearby-context recovery, and verdict stopping conditions for the unresolved-scope defect the source explains.

## Bidirectional Candidates

- [Review gate](../../../../types/review-gate.md) <-> source — **rests-on** (return edge from the type spec): the self-containment requirement is a system-specific contract whose rationale is the source's general rule that interpretation dependencies must remain inside the consumer's guaranteed boundary.
- [Underspecified assertions](../../../../instructions/review-gates/semantic/underspecified-assertions.md) <-> source — **rests-on** (return edge from the gate): a gate maintainer needs the narrower theory explaining why a named system choice can be semantically unresolved even when the sentence is grammatical and the name is identified.

## Reverse-edge Candidates

- [Model-resolved indirection adds interpretation work to LLM execution](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) -> source — **exemplifies**: a model-facing placeholder is a concrete named choice whose authoritative assignment must be delivered inside the model's consumption boundary, while its fixed/runtime role determines whether upstream resolution is correct.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md) — relevant to consumer-relative content value, but too broad for this source's narrower assignment-and-role test; the durable-payload candidate already carries the useful path-specific consequence.
- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) — explains that binding work must be paid somewhere, but does not decide whether the resulting artifact preserves a proposition's assignment and role; the model-resolved reverse edge is the more discriminating instance.
- [Ad hoc prompts extend the system without schema changes](../../../../notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md) — its clean sub-agent prompt is an illustrative consumption boundary, but it already points to the stronger context-scoping account and adds no distinct named-choice criterion.
- [Descriptive link labels may supply the self-sufficiency a reconstruction gate would check](../../../../notes/descriptive-link-labels-may-supply-claim-self-sufficiency.md) — its own ablation rejects the original claim that link labels supply self-sufficiency; it tests premise availability in mature note bodies, not assignment and role for named choices.
- [Collections never own frontmatter semantics](../../../../reference/collections-never-own-frontmatter-semantics.md) — Commonplace-specific self-containment case about contract ownership; it does not articulate the source's proposition-level scope condition.
- [Ingest: The Nature of Theory in Information Systems](../../../../sources/the-nature-of-theory-in-information-systems-gregor-2006.ingest.md) — Gregor's “scope” means degree of generality plus boundary statements; treating that as evidence for assignment-and-role recoverability would conflate two scope concepts.
- [Unidentified References](../../../../instructions/review-gates/accessibility/unidentified-references.md) — catches a proper noun without an inline class gloss, but a gloss can identify a referent without specifying how the named choice functions in the proposition.
- `kb/agent-memory-systems/reviews/llm-context-base.md`, `kb/agentic-systems/eigenius.md`, `kb/agentic-systems/fractal.md`, and `kb/agentic-systems/exo.md` — scoped system-description hits only; none passes the articulation test for the source's assignment-plus-role claim.
- The source's five existing note neighbors and linked collection definition — already authored in the source, so they are traversal context rather than candidate edges.

## Index Membership

- [Document system](../../../../tags/document-system-README.md) — add the source under Writing Conventions or Foundations: it gives the document-level test for when a system-specific name preserves theoretical scope and when collection placement must change.
- [Foundations](../../../../tags/foundations-README.md) — add the source near artifact classification and the boundary-preserving-rival test: it completes that cluster by stating how a recognized design choice may appear inside a transferable theoretical proposition.

## Synthesis Opportunities

- [A theoretical artifact must preserve the scope of each named system choice](../../../notes/a-theory-may-name-a-choice-only-as-a-bound-variable.md), [Model-resolved indirection adds interpretation work to LLM execution](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md), and [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md) jointly imply a two-sided context-assembly obligation not yet named as one claim: an assembly boundary must include every binding required to interpret the unit, and it must exclude or isolate ambient material that can capture those bindings. Completeness and hygiene are independent—a package can preserve the needed assignment yet still admit capture, or isolate cleanly while omitting the assignment.

## Maintenance Observations

- The target was retitled and substantively reframed, but its filename still carries the former “bound variable” thesis. Two live inbound surfaces also preserve that superseded wording: [artifact-analysis](../../../../tags/artifact-analysis-README.md) says a general claim “must quantify” over each choice, and [ADR 070](../../../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md) links the old title. The current source explicitly says literal quantifier syntax is neither necessary nor sufficient, so both link texts and the artifact-analysis context phrase are semantically stale even though all paths resolve.

## Flags

- **Possible split candidate:** the main assignment/role/consumption-boundary theory and the unreconstructable 27-file historical audit are independent contributions. The source already disclaims the audit as evidence for the general claim; extracting or retiring that section would improve composability, although the lost manifest limits what a separate evidence artifact could responsibly assert.
