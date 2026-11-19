---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/documentation-generates-the-system-rather-than-describing-it.md"
source_has_frontmatter: true
date: "2026-08-23"
depth: standard
---

# Connection Report: Attempted recovery identifies informational gaps, not provenance or authority

**Source:** [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md)

## Discovery Trace

**Authorization and setup:**

- Read the promoted `cp-skill-connect` contract, `kb/cache/types/connect-report.md`, the source in full, and `kb/notes/COLLECTION.md`. The final source separates three per-content-unit relations: recoverability from a declared source set, historical provenance, and current authority through a live change loop. Recovery is an availability assay; it does not establish either of the other relations.
- The notes contract authorizes local prospecting in `kb/notes/`, `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`. It excludes `kb/work/`. Read every authorized destination's `README.md` and `COLLECTION.md` before evaluating outbound and reverse-edge labels.
- `external` is authorized only for already-known targets. No external target was supplied in the task or loaded context, so open-web prospecting was skipped. No numeric similarity or retrieval scores were available; candidates were judged from full text and collection contracts.

**Curated heads and tag routing:**

- Read `kb/notes/README.md`, [Artifact analysis](../../../../tags/artifact-analysis-README.md), [KB maintenance](../../../../tags/kb-maintenance-README.md), and the linked [Document system](../../../../tags/document-system-README.md). `artifact-analysis-README.md` has `complete: true` and already lists the source, so the notes-level by-tag sweep for `artifact-analysis` was skipped. `kb-maintenance-README.md` is incomplete, so ran `rg -l '^tags:.*\bkb-maintenance\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`.
- Read `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. No matching curated tag head existed in those destinations, so both tag strings were searched directly there.

**Full title, description, and tag surfaces:**

- Notes: ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (then the split globs `--glob '[a-lA-L0-9]*.md'` and `--glob '[m-zM-Z]*.md'` after output truncation), `rg '^description:' kb/notes/ --glob '*.md'`, and the required `kb-maintenance` listing above.
- Types: ran `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'`, `rg '^description:' kb/types/ --glob '*.md'`, `rg -l '^tags:.*\bartifact-analysis\b' kb/types/ --glob '*.md'`, and `rg -l '^tags:.*\bkb-maintenance\b' kb/types/ --glob '*.md'`.
- Reference: ran `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`, `rg '^description:' kb/reference/ --glob '*.md'`, `rg -l '^tags:.*\bartifact-analysis\b' kb/reference/ --glob '*.md'`, and `rg -l '^tags:.*\bkb-maintenance\b' kb/reference/ --glob '*.md'`.
- Agent-memory systems: ran `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`, `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`, `rg -l '^tags:.*\bartifact-analysis\b' kb/agent-memory-systems/ --glob '*.md'`, and `rg -l '^tags:.*\bkb-maintenance\b' kb/agent-memory-systems/ --glob '*.md'`.
- Agentic systems: ran `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`, `rg '^description:' kb/agentic-systems/ --glob '*.md'`, `rg -l '^tags:.*\bartifact-analysis\b' kb/agentic-systems/ --glob '*.md'`, and `rg -l '^tags:.*\bkb-maintenance\b' kb/agentic-systems/ --glob '*.md'`.
- Sources: ran `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`, `rg '^description:' kb/sources/ --glob '*.md'`, `rg -l '^tags:.*\bartifact-analysis\b' kb/sources/ --glob '*.md'`, and `rg -l '^tags:.*\bkb-maintenance\b' kb/sources/ --glob '*.md'`.
- Instructions: ran `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`, `rg '^description:' kb/instructions/ --glob '*.md'`, `rg -l '^tags:.*\bartifact-analysis\b' kb/instructions/ --glob '*.md'`, and `rg -l '^tags:.*\bkb-maintenance\b' kb/instructions/ --glob '*.md'`.

**Body search — notes:**

- Ran `rg -n -i 'recoverab|recovery|reconstruct|regenerat' kb/notes/ --glob '*.md'`, `rg -n -i 'provenance|production history|historical relation|lineage evidence|worked out from' kb/notes/ --glob '*.md'`, and `rg -n -i 'source of truth|ground truth|authoritative record|current authority|change loop|causal path' kb/notes/ --glob '*.md'`. These retained the general artifact-dimension model, the lineage and behavioral-authority definitions, the consumption-channel mechanism, and the outcome/process distinction.
- Ran `rg -n -i 'rejected alternatives|design rationale|warrant for choices|decision-relevant|unique content|information gap|informational gap' kb/notes/ --glob '*.md'` and `rg -n -i 'bidirectional|both directions|system-to-document|document-to-system|common source|common cause' kb/notes/ --glob '*.md'`. These retained the checked-copy consequence and the sufficiency contrast while exposing narrower decision-trace and documentation-economics cases that were rejected below.
- Also ran file-list variants of the first four searches to compare candidate density before opening files. The source's seven existing footer links were treated as encoded state and were not re-proposed.

**Body search — types:**

- Ran `rg -n -i 'recoverab|recovery|reconstruct|regenerat|provenance|lineage|source of truth|ground truth|authority|consumer|channel|force' kb/types/ --glob '*.md'`. [Instruction](../../../../types/instruction.md) passed as a concrete Commonplace contract for current authority through a consumer, channel, and force. `tag-readme.md` was a checked-cache example but did not add a distinct relation.

**Body search — reference:**

- Ran `rg -n -i 'recoverab|recovery|reconstruct|regenerat' kb/reference/ --glob '*.md'`, `rg -n -i 'provenance|production history|lineage evidence|worked out from|design rationale|rejected alternatives' kb/reference/ --glob '*.md'`, `rg -n -i 'source of truth|ground truth|authoritative record|current authority|change loop|consumer.*channel.*force|causal path' kb/reference/ --glob '*.md'`, and `rg -n -i 'system.*documentation|documentation.*system|specification.*implementation|implementation.*specification' kb/reference/ --glob '*.md'`.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) passed as a bounded failure-to-guarantee-recovery case. [Instruction generation](../../../../reference/instruction-generation.md) passed as a positive case where canonical inputs and a concrete generation path independently establish production provenance. [Link vocabulary and linking approach](../../../../reference/link-vocabulary.md) exposed a terminology/authorization tension routed below rather than being forced into an authorized weak label.

**Body search — agent-memory systems:**

- Ran `rg -n -i 'recoverab|recovery|reconstruct|regenerat' kb/agent-memory-systems/ --glob '*.md'`, `rg -n -i 'provenance|production history|lineage|design rationale|rejected alternatives|decision record|why-memory' kb/agent-memory-systems/ --glob '*.md'`, `rg -n -i 'source of truth|ground truth|authoritative|authority|read-back|pull-only|pushed' kb/agent-memory-systems/ --glob '*.md'`, and `rg -n -i 'living document|update contract|generated (skill|instruction|wiki)|compiled (wiki|context)|docs? (generate|drive|govern)' kb/agent-memory-systems/ --glob '*.md'`.
- [WUPHF](../../../../agent-memory-systems/reviews/wuphf.md) passed because its review states the discriminating result directly: its Markdown/Git source-of-truth story is reconstructable and attributable, while the code cannot establish whether an agent searched, used, or changed behavior because of that memory. Gnosis, o-o, and LLM Project Wiki supplied real cases but were rejected as instance spray after WUPHF covered the three-relation separation most exactly.

**Body search — agentic systems:**

- Ran `rg -n -i 'recoverab|recovery|reconstruct|regenerat|provenance|lineage|design rationale|source of truth|authority|documentation|specification|protocol|instruction' kb/agentic-systems/ --glob '*.md'`. [Eigenius](../../../../agentic-systems/reviews/eigenius.md) passed because its manually loaded protocol, checked justification records, and `ProgramTrace` records separate current force, warrant, and execution history in one code-grounded system. GBrain and Compound Engineering Plugin were overlapping authority-path cases.

**Body search — sources:**

- Ran `rg -n -i 'recover.*(rationale|intent|decision)|regenerat.*(rationale|intent|decision)|reconstruct.*(rationale|intent|decision)' kb/sources/ --glob '*.md'`, `rg -n -i 'spec is the new code|spec-driven|documentation.*(generate|driv|govern)|docs?.*(generate|driv|govern)|policy.*(review|audit|code generation)' kb/sources/ --glob '*.md'`, `rg -n -i 'provenance.*(execution|history|lineage)|production history|design rationale|rejected alternatives|source of truth|authoritative record' kb/sources/ --glob '*.md'`, and `rg -n -i 'change loop|consulted.*(document|spec|policy)|read.*(specification|design document|policy)|operative.*(document|spec|policy)' kb/sources/ --glob '*.md'`.
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) passed as causal-intervention evidence that retained and visible content can remain behaviorally inert. The Figma policy thread was a weaker self-reported positive case; PROV was broader provenance vocabulary; the code-simplification ingest was a practitioner rationale case already covered more precisely by retained notes and reference documentation.

**Body search — instructions:**

- Ran `rg -n -i 'recoverab|recovery|reconstruct|regenerat|provenance|production history|lineage evidence|design rationale|rejected alternatives' kb/instructions/ --glob '*.md'` and `rg -n -i 'source of truth|ground truth|authoritative record|current authority|change loop|consumer.*channel.*force|causal path' kb/instructions/ --glob '*.md'`.
- [Write an Instruction](../../../../instructions/write-instruction.md) passed only in the reverse direction: its rule that procedure steps should be recoverable from methodology plus task depends on the source's boundary between a useful reconstructibility relation and a historical provenance claim. The raw `kb/instructions/COLLECTION.md` contract's instruction-duality rule also passed but is routed to Raw Text Candidates.

**Inbound search, link following, and evaluation:**

- Ran `rg -n 'documentation-generates-the-system-rather-than-describing-it|Attempted recovery identifies informational gaps, not provenance or authority' kb/ --glob '*.md'`. Existing library inbound paths came from `artifact-analysis-README.md`, `opposed-recompute-factors-do-not-decide-documentation-segmentation.md`, `addressability-grain-sets-a-matched-selective-read-floor.md`, and `an-insufficient-summary-precedes-the-source-rather-than-replacing.md`. Hits under excluded `kb/work/` and generated/operational reports were not candidates.
- Followed candidate neighborhoods one hop and read the full artifacts used below: `artifact-classification-separates-content-kind-lineage-and-authority.md`; `definitions/lineage.md`; `definitions/behavioral-authority.md`; `definitions/operative-change.md`; `a-consumption-channel-delivers-force-without-the-history-that.md`; `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`; `checked-outcome-licenses-episode-retention-not-abstraction.md`; `knowledge-storage-does-not-imply-contextual-activation.md`; `structure-inference-needs-capture-at-the-decision-surface.md`; `parametric-reproduction-cannot-replace-an-authoritative-record.md`; the three inbound documentation-economics notes; `types/instruction.md`; `reference/design-rationale-management.md`; `reference/instruction-generation.md`; `reference/link-vocabulary.md`; the Gnosis, o-o, LLM Project Wiki, and WUPHF reviews; the Eigenius, GBrain, and Compound Engineering Plugin analyses; the Faithful Self-Evolvers, Figma, PROV, and code-simplification ingests; `instructions/write-instruction.md`; and `instructions/COLLECTION.md`.
- Retained candidates each add a distinct test, mechanism, contract, or bounded case. Obvious duplicates and narrower applications are recorded under Rejected Candidates. Existing reverse traversal from the sufficiency note was not mistaken for the still-useful new source-to-sufficiency direction.
- Verified every candidate path below with `test -f` against the current worktree.

## Connections Found

- [Artifact classification separates content kind, lineage, and authority](../../../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md) — **exemplifies**: the source is a document/system application of the general rule that content kind, production relation, and behavioral authority attach independently and may differ by artifact unit.
- [Lineage](../../../../notes/definitions/lineage.md) — **defined-in**: the source asks for lineage evidence while distinguishing full historical provenance; this definition narrows lineage to the dependency records needed for review, invalidation, and regeneration rather than treating it as every fact about origin.
- [Behavioral authority](../../../../notes/definitions/behavioral-authority.md) — **defined-in**: the source's “current authority” relation is exactly the consumer, channel, force, and horizon through which content reaches later behavior.
- [A consumption channel delivers force without the history that earned it](../../../../notes/a-consumption-channel-delivers-force-without-the-history-that.md) — **mechanism**: a loaded channel can confer present behavioral force without carrying the production history or warrant that originally earned the content, explaining why provenance and current authority vary independently.
- [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — **extends**: it develops a successful recoverability finding into the checked-copy maintenance rule while preserving the source's warning that recoverability alone does not settle value or authority.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) — **grounds**: matching or successful outcomes underdetermine the process that produced them, supporting the source's claim that extensional recovery cannot establish historical provenance without process evidence.
- [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — **contrasts**: recoverability asks whether the content exists in the declared sources, while sufficiency asks whether reading it closes the consumer's task; the two tests cross independently.
- [Instruction](../../../../types/instruction.md) — **evidenced-by**: Commonplace's type contract implements the current-authority condition by requiring a consumer, channel, and force and treating an instruction nothing loads as persistent but inert.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) — **evidenced-by**: the shipped system distributes constraints, alternatives, and evidence across several surfaces and explicitly cannot guarantee later recovery without authors carrying or linking that rationale.
- [Instruction generation](../../../../reference/instruction-generation.md) — **evidenced-by**: the documented canonical inputs, manifest, placeholder substitution, copy path, and drift reporting provide a positive case where a production path independently establishes provenance for covered generated artifacts.
- [WUPHF](../../../../agent-memory-systems/reviews/wuphf.md) — **evidenced-by**: its Markdown and Git state is reconstructable and attributable, yet the implementation cannot prove that an agent searched, used, or changed behavior because of the retained memory, separating availability and lineage from current force.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) — **evidenced-by**: its manually loaded method has current force only when a host follows it, justification certificates record warrant, and `ProgramTrace` records execution history, making the source's three relations observable through distinct mechanisms.
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) — **evidenced-by**: controlled perturbations show condensed experience can be retained, visible, and semantically plausible while downstream behavior remains causally insensitive to it, directly bounding claims of current authority from availability alone.

## Bidirectional Candidates

- [Artifact classification separates content kind, lineage, and authority](../../../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md) → source — **extends**: readers of the general classification gain a concrete two-direction recovery assay for one artifact pair, plus explicit failure conditions for inferring lineage or authority from that assay.

The sufficiency note already authors its independently useful return edge, so it is not re-proposed here.

## Reverse-edge Candidates

- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) → source — **rests-on**: the shipped description's warning that rationale recovery depends on explicit carry-forward or links depends on the source's distinction between an information gap and evidence of production history.
- [WUPHF](../../../../agent-memory-systems/reviews/wuphf.md) → source — **is-evidence-for**: its stronger source-of-truth story and weaker activation story materially bear on the claim that recoverability, provenance, and current authority must be assessed separately.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) → source — **is-evidence-for**: its distinct host-loading, justification, and execution-trace mechanisms are a code-grounded instance of the source's three-relation separation.
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) → source — **is-evidence-for**: the causal interventions materially bear on the current-authority claim by distinguishing stored or context-present content from content that actually changes behavior.
- [Write an Instruction](../../../../instructions/write-instruction.md) → source — **rests-on**: its recoverability prescription needs the source's boundary—reconstructible procedure content supports maintenance and recheck, but does not by itself prove that the procedure was historically produced from the methodology.

## Off-authorisation Candidates

- [Link vocabulary and linking approach](../../../../reference/link-vocabulary.md) — candidate **contrasts**: the reference groups `derived-from` among lineage relations while specifying reconstructibility from a source plus consumer goal as its truth condition; the source says that recoverability alone does not establish historical production. `contrasts` is not authorized for notes → reference. A future collection-contract/vocabulary pass should either authorize that relationship after clarifying the two meanings of lineage or reject the edge as off-scope rather than downgrade it to `see-also`.

## Raw Text Candidates

- [Writing conventions for kb/instructions/](../../../../instructions/COLLECTION.md) → source — potential **rests-on**: the raw contract's instruction-duality rule says an edit is a deployment only when a named consumer and channel make it live, and that unloaded instructions are inert; this is a prescriptive application of the source's current-authority relation, but the contract has no frontmatter and therefore is not proposed as a regular connection.

## Rejected Candidates

- [Operative change](../../../../notes/definitions/operative-change.md) — genuine adjacent vocabulary, but it adds persistence and horizon conditions for system changes; `Behavioral authority` is the exact definition for the source's artifact-to-change-loop relation.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — strongly related, but the retained behavioral-authority definition, consumption-channel mechanism, WUPHF case, and causal source already cover the availability-to-effect boundary without adding another broad activation link.
- [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) — a useful model-weight-specific application of reproduction without authority, but narrower than the retained general mechanism and external cases.
- [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) — a real missing-history instance, but specialized to ontology induction and redundant with the broader outcome/process and rationale-management candidates.
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md) and [Opposed recompute factors do not decide documentation segmentation](../../../../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) — both are valid downstream cache-economics cases, but the source already separates deletion value from recoverability and links the general recompute-cost note; adding both would overpopulate the footer with narrower cost consequences.
- [Gnosis](../../../../agent-memory-systems/reviews/gnosis.md), [o-o](../../../../agent-memory-systems/reviews/o-o.md), and [LLM Project Wiki](../../../../agent-memory-systems/reviews/llm-project-wiki.md) — each supplies a genuine rationale or authority-path case, but WUPHF states the recoverability/attribution versus activation separation most directly; retaining all four would be instance spray.
- [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) and [Storage architecture](../../../../reference/storage-architecture.md) — both expose partial provenance or authority surfaces, but `design-rationale-management.md` is the bounded shipped-system account targeted to later rationale recovery.
- [GBrain](../../../../agentic-systems/reviews/gbrain.md) and [Compound Engineering Plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) — their host-loaded or rewritten instructions fit current authority, but Eigenius adds independently recorded warrant and execution history rather than another authority-only example.
- [Ingest: PROV-Overview](../../../../sources/prov-overview.ingest.md) — supplies a broad provenance model, but the source's argument needs the narrower local distinction and concrete production evidence, not another general provenance vocabulary.
- [Ingest: Thread by @frgx](../../../../sources/figma-agent-security-review-thread-2081739292859421118.ingest.md) and [Ingest: Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) — plausible policy-authority and missing-rationale cases, but self-reported practitioner evidence adds less than the causal-intervention source and the bounded Commonplace rationale account.
- [Tag README](../../../../types/tag-readme.md) — an enforced checked-cache example, but it duplicates the more general derived-copy consequence and does not exercise the provenance or current-authority distinctions.

## Index Membership

- [KB maintenance](../../../../tags/kb-maintenance-README.md) — the source contributes two maintenance tests absent from the curated head: all-source recovery before deleting a documentary copy, and a causal-path check before treating retained content as current authority.

The source is already present in [Artifact analysis](../../../../tags/artifact-analysis-README.md), so no candidate membership is proposed there.

## Synthesis Opportunities

None. The source already performs the higher-order synthesis among recoverability, historical provenance, and current authority; the retained candidates supply definitions, mechanisms, cases, and consequences rather than a missing fourth relation.

## Maintenance Observations

- The final title and thesis no longer match the filename, and several inbound surfaces still preserve the superseded title or stronger “generator content” interpretation: [Artifact analysis](../../../../tags/artifact-analysis-README.md), [Opposed recompute factors do not decide documentation segmentation](../../../../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md), [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md), and [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md). Their paths resolve, but a future maintenance pass should refresh titles and context phrases so they do not imply that recovery failure itself proves generative provenance.
- [Link vocabulary and linking approach](../../../../reference/link-vocabulary.md) uses “lineage” for a `derived-from` maintenance relation whose stated truth condition is recoverability, while the final source reserves historical provenance for independently evidenced production history. This may be a deliberate narrower dependency sense (as in the local lineage definition), but the boundary should be made explicit before readers treat the formal label as a historical claim.

## Flags

- **Split candidate:** the source yields more than five note connections across artifact classification, provenance, behavioral authority, cache maintenance, and evaluation, and it makes three independent assertions. A future writer should test whether the recovery assay, provenance-evidence boundary, and current-authority condition remain clearer as one contrastive synthesis or should become separately composable notes; this flag does not itself require a split.
