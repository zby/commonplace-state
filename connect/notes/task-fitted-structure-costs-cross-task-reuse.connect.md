---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/task-fitted-structure-costs-cross-task-reuse.md"
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: Current-task fit alone does not warrant costly structural entrenchment

**Source:** [Current-task fit alone does not warrant costly structural entrenchment](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md)

## Discovery Trace

No semantic-search scores were available. This closing pass used only repo-local curated heads, fresh title and description surfaces, focused body searches, and one-hop link following. The source was read at SHA-256 `f9b3c60cf7231d412aad03ddf0e8f9083553dd66bb0e16dbe2b0f2dcb468adb4`.

**Source contract and destination authorization:**

- Read `kb/notes/COLLECTION.md`. It authorizes local prospecting in `kb/notes/`, `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`; it excludes `kb/work/`.
- The reserved `external` destination is authorized only for already-known targets. The user supplied none, so external prospecting was skipped.
- Note-to-instruction prospecting was treated as exceptional and inverse-aware: `operationalized-from` requires a procedure to add ordering, defaults, or stopping conditions that the methodology note leaves open; otherwise the usual useful direction is `instruction -> note` via `rests-on`.

**Curated heads and tag listings:**

- Read `kb/notes/README.md`, `kb/notes/document-system-README.md`, and `kb/notes/foundations-README.md`. Neither matching tag README declares `complete: true`, so neither by-tag description search was skipped.
- Ran `rg -l '^tags:.*\bdocument-system\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`. The closest results were the source's already-authored constraint, coordination, local-use, scope-warrant, universal-taxonomy, fixed-decomposition, locality, and scenario-decomposition links. `A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking` remained a useful target-side connection because it discusses coordination value and switching cost without yet linking the sharper entrenchment rule.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, `kb/instructions/README.md`, and `kb/types/README.md`. The reference head surfaced the profile catalogue and `Commonplace as an instrument`; the agent-memory head confirmed that the comparative lifecycle result is already authored into the source; the agentic head surfaced Compound Engineering; the sources surface exposed the two phased-transfer cases; the instruction head exposed `Retire an artifact`; and the types head supplied no contract whose actual claim tests current-task fit against entrenchment.

**Complete title surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`, and `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'` once each.
- The notes surface added `Machinery persists by warrant, not position`, `A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking`, `First-principles analysis maps a design space before selecting within it`, and `A repeatable operative path keeps a redesign class open to revision` to the residual evaluation set. The other surfaces added `Text contract profiles`, Compound Engineering, HarnessCompass, the phased agent-optimizer study, Memento-Skills, and `Retire an artifact`.

**Description listing scans:**

- Notes used the two by-tag description listings above. The source itself was excluded, and already-authored targets were not reintroduced as candidates.
- Ran `rg '^description:' kb/types/ --glob '*.md'`. `tag-readme.md` and `type-spec.md` describe binding structural contracts but provide no transfer, replacement-cost, or retirement evidence, so no type candidate passed the articulation test.
- Ran `rg '^description:' kb/reference/ --glob '*.md'`. `Text contract profiles` was rechecked against the narrowed claim; `Commonplace as an instrument` was rejected as a redundant route to the already-linked local-use and scope-warrant premises.
- Ran `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`. The comparative lifecycle review is already linked in the body. Individual fixed-schema and lifecycle reviews added examples but no distinct reader need beyond that aggregate result.
- Ran `rg '^description:' kb/agentic-systems/ --glob '*.md'`. Compound Engineering was evaluated as a residue-control case but rejected as secondary corroboration that does not test current-question fit or costly entrenchment.
- Ran `rg '^description:' kb/sources/ --glob '*.md'`. HarnessCompass and the phased agent-optimizer study survived only as reverse-edge candidates from their source analyses to the theory note; Memento-Skills was rejected because it tests reusable skill content under domain alignment, not entrenchment of a structural layer.
- Ran `rg '^description:' kb/instructions/ --glob '*.md'`. `Retire an artifact` was the closest result but operates after an artifact-level retirement decision and explicitly excludes vocabulary retirement; it does not supply the source's missing structural retirement trigger.

**Focused body searches:**

- Notes: ran `rg -n -i 'task-fitted|task-derived|cross-task reuse|question set|current-task fit|future transfer' kb/notes/ --glob '*.md' --glob '!task-fitted-structure-costs-cross-task-reuse.md'`; `rg -n -i 'hardening|harden|entrench|replaceable|replacement cost|migration cost|retirement trigger|deprecat|structural residue' kb/notes/ --glob '*.md' --glob '!task-fitted-structure-costs-cross-task-reuse.md'`; `rg -n -i 'fixed decomposition|structure.*transfer|taxonomy.*transfer|schema.*transfer|discriminating evidence|earned scope' kb/notes/ --glob '*.md' --glob '!task-fitted-structure-costs-cross-task-reuse.md'`; and `rg -n -i 'remain(s|ed)? revisable|open to revision|cheap to replace|replacement|retirement|retire|structural.*(drift|mismatch|residue)|coordination value|switching cost|dependency closure' kb/notes/ --glob '*.md' --glob '!task-fitted-structure-costs-cross-task-reuse.md'`. These searches kept the two note-side reverse edges below and rejected the broader design-space and operative-revision matches as redundant or mechanism-mismatched.
- Types: ran `rg -n -i 'replace|retire|deprecat|migration|evol|extension|scope|schema|coordination|stale' kb/types/ --glob '*.md'`. Results concern the current contracts and their local maintenance rules, not evidence that present fit licenses or fails to license costly permanence.
- Reference: ran `rg -n -i 'task-specific|cross-task|transfer evidence|fixed decomposition|taxonomy|profile.*default|worked case|promot|retire|replaceable|migration|structural' kb/reference/ --glob '*.md'`. The live profile catalogue states that its entries are a nonbinding palette and that each collection contract remains authoritative; local exercise admits an additive catalogue entry, not necessarily costly entrenchment.
- Agent memory and agentic systems: ran `rg -n -i 'fixed schema|schema.*(evol|adapt|mismatch)|taxonomy|page type|node type|migration path|retirement|retire|deprecat|stagnat|future task|held-out task|lifecycle' kb/agent-memory-systems/ --glob '*.md'` and `rg -n -i 'retirement|retire|stale|replace|refresh|cross-task|fixed.*(structure|workflow|decomposition)|transfer' kb/agentic-systems/ --glob '*.md'`. The first confirmed the already-linked 148-system lifecycle statistic as the most economical evidence target; the second surfaced Compound Engineering's operator-invoked refresh path but no direct test of the source's central distinction.
- Sources: ran `rg -n -i 'cross-task|held-out task|held-out.*(transfer|generaliz)|cross-model|future task|fixed decomposition|task-specific.*(schema|structure|harness|routing)|schema.*(reuse|evol|mismatch)|taxonomy.*(reuse|transfer)|retire|retirement|stagnation' kb/sources/ --glob '*.md'`. HarnessCompass separates evolution-set fit from held-out and cross-model transfer while withholding validation from its fixed partition; the phased optimizer study separates initial fit, transfer, and later re-optimization. Both source reports can therefore point to the final note under their own rare `is-evidence-for` authorization without expanding the source note's already dense evidence surface.
- Instructions: ran `rg -n -i 'retire|retirement|replace|migration|deprecat|supersed|scope|structur' kb/instructions/ --glob '*.md'`. The closest procedure fixes disposal mechanics only after semantic retirement has been decided.

**Candidate evaluations:**

- Kept `machinery-persists-by-warrant-not-position-in-a-reflective-loop.md` as a reverse edge: its rule that a gate or type persists because it keeps earning use needs the source's distinction between repeated present-task use, inherited constraint, discriminating transfer, and coordination value.
- Kept `a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` as a reverse edge: its coordination-value paragraph already identifies switching cost, while the source develops when that value may justify costly structural commitment and what decision threshold remains open.
- Kept the HarnessCompass ingest as a reverse edge: evolution-set improvement accompanied by a held-out drop in one ablation and recovery under the final configuration bears on the difference between present fit and discriminating transfer, while the report explicitly withholds warrant from the fixed component partition.
- Kept the phased agent-optimizer ingest as a reverse edge: all three optimizers improve on the first task set, then diverge on transfer and re-optimization, directly showing why current-objective success does not settle later reuse or revisability. The candidate is bounded to harness artifacts and Terminal-Bench rather than presented as direct evidence about KB migration cost.
- Rejected `first-principles-analysis-maps-design-space-before-selection.md`: it states the general keep-free-choices-replaceable rule, but the source already links the narrower fixed-decomposition, inherited-constraint, and earned-scope premises that serve the same reader need more directly.
- Rejected `a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md`: it tests causal continuity of an operative revision path, not whether current-task fit warrants paying the dependency and migration costs of structural entrenchment.
- Rejected Compound Engineering: refresh can update, consolidate, replace, stale-mark, or delete retained documents, but this is one operator-invoked lifecycle implementation and does not test the source's fit-to-entrenchment inference. The source already carries stronger aggregate lifecycle evidence.
- Rejected `Retire an artifact`: it supplies mechanics after a retirement decision, not the signal or threshold for retiring a structural element; its own scope excludes project-vocabulary retirement.
- Rejected `Text contract profiles` as a contradiction: the final source excludes cheap additive or binding choices that remain easy to replace, while the catalogue declares itself a nonbinding palette. Local exercise admitting a profile entry is not, by itself, the costly entrenchment the source governs.
- Rejected Memento-Skills: its domain-alignment result concerns transfer of learned executable skill content, not types, tags, indexes, schemas, link vocabularies, or routing rules becoming costly to replace.

**Link following:**

- Followed `Machinery persists by warrant, not position` to the earned-reach, fixed-decomposition, and reflective-loop cluster. This revealed a useful target-side sharpening: “keeps earning use” needs the final source's cross-question and costly-entrenchment boundary.
- Followed `A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking` through `Coordination value` and ADR 042. The neighborhood confirmed that the final source develops an already-named coordination/switching-cost problem rather than contradicting the profile model.
- Followed `Text contract profiles` to ADR 042 and the universal-taxonomy note. Its guidance-only posture and the final source's cheap-additive exclusion dissolve the earlier apparent policy tension.
- Followed HarnessCompass and the phased optimizer study to `Learning inside a fixed decomposition inherits its mistakes`, the scope-warrant note, and their neighboring harness analyses. This confirmed that their useful direction is source-analysis-to-theory: they bear on the distinction but do not establish KB entrenchment costs.
- Followed the comparative lifecycle review to `Trace-learning techniques in related systems`; the survey adds implementation detail but no distinct reader need beyond the aggregate result already authored into the source.
- Followed Compound Engineering's refresh and retirement discussion. It remains a concrete example, but not enough of a transfer or entrenchment test to justify another outbound evidence edge from the final note.

## Connections Found

None

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) -> source -- **extends**: the return path would sharpen “a type survives because its carve keeps earning use” by separating recurring present-task use from inherited constraint, discriminating cross-question transfer, and coordination value.
- [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](../../../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md) -> source -- **extends**: its coordination-value and switching-cost paragraph would gain the source's explicit rule for costly structural commitment and its unresolved threshold between interoperability and replaceability.
- [Ingest: HarnessCompass](../../../../sources/harnesscompass-guiding-automatic-harness-evolution.ingest.md) -> source -- **is-evidence-for**: its evolution-set/held-out divergence and later held-out recovery bear on the difference between present fit and discriminating transfer, while its fixed partition remains explicitly unvalidated.
- [Ingest: Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -> source -- **is-evidence-for**: first-phase success fails to predict transfer and re-optimization across the compared harness optimizers, a bounded empirical instance of current-objective fit not settling later reuse or revisability.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [First-principles analysis maps a design space before selecting within it](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md) -- its replaceability rule is genuine overlap, but the source already reaches the narrower fixed-decomposition, constraint, and earned-scope premises that explain the decision more directly.
- [A repeatable operative path keeps a redesign class open to revision](../../../../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) -- governs continuity of a causal revision path, not the economic and evidential warrant for making KB structure costly to replace.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- supplies a concrete refresh and retirement implementation, but does not test present-question fit against later transfer or migration cost; the already-linked comparative lifecycle review is the more economical support for the source's bounded retirement-asymmetry claim.
- [Retire an artifact](../../../../instructions/retire-artifact.md) -- begins after semantic retirement is decided and excludes vocabulary retirement, so it does not operationalize the missing trigger for retiring entrenched structure.
- [Text contract profiles](../../../../reference/collection-prototypes.md) -- no longer contradicts the final claim: catalogue admission is guidance-only and may remain a cheap additive choice, whereas the source governs costly entrenchment.
- [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) -- describes local composition evidence and missing transfer evidence, but the source already links the theoretical local-use and scope-warrant notes that supply the same premise without a Commonplace-specific detour.
- [Ingest: Memento-Skills: Let Agents Design Agents](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) -- tests transfer of learned executable skill content under different domain alignment, not entrenchment of a KB structural layer.

## Index Membership

- [Document system](../../../../tags/document-system-README.md) -- the source explains the lifecycle and transfer risk of the types, tags, indexes, schemas, link vocabularies, and routing rules grouped by this curated head; it carries the tag but is not yet listed.
- [Foundations](../../../../tags/foundations-README.md) -- the source supplies a general decision rule for when a structural choice may become costly to replace; it carries the tag but is not yet listed.

## Synthesis Opportunities

None

## Maintenance Observations

- The filename still encodes the superseded stronger formulation “task-fitted structure costs cross-task reuse,” while the H1 now states “Current-task fit alone does not warrant costly structural entrenchment.” A future relocation should use `commonplace-relocate-note` so inbound paths and the published redirect are updated together; baseline handling remains a separate concern under the retirement/relocation guidance.

## Flags

- **No new outbound candidate:** the final note already authors the strongest local theory links and the bounded comparative lifecycle evidence found by the initial pass. The residual useful graph work is target-side and index-side rather than another source footer expansion.
- **Potential split candidate:** the adoption-friction/weak-retirement section remains independently citable and the note connects across theory, empirical system coverage, and lifecycle concerns. Its current conditional form supports the entrenchment-cost argument, so split only if later inbound citation demand shows that the accumulation mechanism needs its own premise identity.
