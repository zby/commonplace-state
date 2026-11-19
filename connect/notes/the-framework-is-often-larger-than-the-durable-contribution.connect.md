---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/the-framework-is-often-larger-than-the-durable-contribution.md"
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: Recognition anchors over reconstructable framework recaps

**Source:** [Linked notes should retain recognition anchors, not reconstructable framework recaps](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md)

## Discovery Trace

**Curated heads and complete title surfaces:**

- Read `kb/notes/README.md` and [Context engineering](../../../../tags/context-engineering-README.md). The tag README does not declare `complete: true`, so the by-tag scan was run. Read the destination landings `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, `kb/instructions/README.md`, and `kb/types/README.md`.
- Generated each complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination> --glob '*.md'`: 354 notes, 135 reference artifacts, 172 agent-memory artifacts, 12 agentic-system artifacts, 502 source artifacts, 44 instructions, and 10 global type artifacts.
- No matching `context-engineering-README.md` exists outside `kb/notes/`. External is authorized for already-known evidence but was not prospected because no external target was supplied or already loaded.

**Notes and definitions:**

- Ran `rg -l '^tags:.*\bcontext-engineering\b' kb/notes --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`. Besides the source and its existing context-engineering links, this surfaced [Warranted reader update is the objective of substantive writing](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md), [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md), and [LLM recompute cost inverts the store-vs-recompute default](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md).
- Ran `rg '^description:' kb/notes --glob '*.md' | rg -i 'reconstruct|recognition|recap|framework|scaffold|inline|point.of.use|derefer|reader need|conditional|mapping|cue|local reason|rationale|recover|omission|semantic work|author should fix|composable|minimal|recompute|ablation'` and body search `rg -n -i 'recognition anchor|recognition condition|reconstructable|reconstruct.*(framework|explanation|rationale)|framework (recap|exposition|address|tutorial)|local (reason|rationale|fact)|condition,? mapping|name plus|name-only|point of use|dereference|omitted material|omission.*recover|recover.*omission|behavioral(ly)? test|downstream effects|semantic work.*relocat|executor can.t determine|framework.*scaffold|scaffold.*model|shared framework|inline.*link|link.*inline' kb/notes --glob '*.md'`.
- Kept [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md): generic framework recap that exposes no new structure to the intended reader is a specific reverse-compression failure, while the source adds the recognition-anchor remedy.
- Kept [Warranted reader update is the objective of substantive writing](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md): it supplies the general contribution-selection premise behind retaining the reader update rather than the volume of framework material present during writing. It already links to the source, so that existing inbound edge was not repeated as a reverse-edge candidate.
- Kept [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md): the source places generic framework work in the shared artifact and preserves the case-specific semantic judgment in the recognition anchor rather than pretending compression removed the judgment.
- Kept [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md): it sharpens the source's exception for authoritative interpretation, provenance, currentness, and contestability even when content is reconstructable.
- Evaluated [Natural-language content lacks reliable dereference](../../../../notes/local-materialization-should-outperform-distant-declarations.md), [An author should fix what the executor cannot determine](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), [Minimum viable vocabulary](../../../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md), [Use tests a decomposition locally](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md), and [LLM recompute cost inverts the store-vs-recompute default](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md). They were rejected respectively as already reached through the source's stronger links-and-activation treatment, an author/executor timing rule rather than a linked-note retention rule, a vocabulary-set optimization rather than a single recognition-address rule, a narrower decomposition-transfer case, and a materialized-value argument that does not apply when the fuller framework already exists as a named linked artifact.

**Reference:**

- Ran `rg '^description:' kb/reference --glob '*.md' | rg -i 'reconstruct|recognition|framework|scaffold|inline|reader|link|rationale|ablation|behavior|shared|contribution|context|omission|recover'` and `rg -n -i 'recognition anchor|recognition condition|reconstructable|reconstruct.*(framework|rationale)|framework (recap|exposition|address)|local (reason|rationale|fact)|point of use|dereference|omitted material|downstream effects|shared framework|inline.*link|link.*inline|ablation.*artifact|artifact.*ablation' kb/reference --glob '*.md'`.
- Evaluated `proposals/checked-inline-blocks-for-shared-instruction-text.md`, `proposals/per-artifact-write-briefs.md`, `proposals/ablation-baselines-for-the-declared-objective.md`, and `design-rationale-management.md`. The first concerns literal reuse of binding instruction text where runtime dereference is unsafe; the others concern commissions, whole-system ablation, or the shipped rationale record. None gives a more direct reader need than the retained note candidates.

**Agent-memory systems:**

- Ran `rg '^description:' kb/agent-memory-systems --glob '*.md' | rg -i 'progressive|context|compact|summary|skill|instruction|framework|disclosure|distill|compress|cue|activation|link|scaffold|recognition|self-contained|metadata'` and `rg -n -i 'recognition anchor|recognition condition|reconstructable|reconstruct.*framework|framework (recap|address|exposition)|point of use|progressive disclosure|minimal.*(cue|link)|cue.*activation|description.*full|full.*description|scaffold.*model|model.*scaffold|local rationale|semantic work' kb/agent-memory-systems --glob '*.md'`.
- Followed [Fintool](../../../../agent-memory-systems/lightweight/fintool.md), [napkin](../../../../agent-memory-systems/reviews/napkin.md), and the progressive-skill surfaces in Exo and Hermes Agent. Their metadata-first/full-body-on-demand mechanisms corroborate progressive disclosure generically. Fintool's scaffolding deletion is the closest case, but the source ingest already linked from the target is the less mediated evidence surface, so no agent-memory candidate was kept.

**Agentic systems:**

- Ran `rg '^description:' kb/agentic-systems --glob '*.md'` and `rg -n -i 'recognition anchor|recognition condition|reconstructable|framework (recap|address|exposition)|point of use|progressive disclosure|scaffold|cue|local rationale|semantic work|minimum scaffolding|context' kb/agentic-systems --glob '*.md'`.
- Evaluated Exo's minimum-scaffolding goal and Fractal's distilled return boundary. Both concern harness control or bounded work delegation, not what a linked case note must retain, so no agentic-system candidate passed the articulation test.

**Sources:**

- Ran `rg '^description:' kb/sources --glob '*.md' | rg -i 'framework|scaffold|writing|compression|context|skill|parametric|reconstruct|recognition|knowledge|distill|tutorial|prose|insight|model absorb|familiar|rationale|reason|cue|progressive disclosure'` and `rg -n -i 'recognition anchor|recognition condition|reconstructable|reconstruct.*framework|framework (recap|exposition|address)|model will eat|eat your scaffolding|absorb.*(skills|scaffold)|delete.*scaffold|framework.*(reconstruct|repeat|recap)|active knowledge|durable contribution|contribution.*edge|local rationale|writing.*thinking|putting ideas into words|point of use|name plus.*cue' kb/sources --glob '*.md'`.
- The target already carries [Ingest: Lessons from Building AI Agents for Financial Services](../../../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) as evidence. Its source-side analysis does not yet link back to this sharper retention rule, so the return path was kept as a reverse-edge candidate under the sources collection's `is-evidence-for` authorization.
- Evaluated [Ingest: Claude Fable 5 Made Most of My Agent Scaffolding Obsolete](../../../../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md), the writing-as-thinking ingests, and the AI;DR discussion. The Fable case is about system scaffolding and duplicates the already-linked deletion/survival boundary; the writing sources concern idea formation; and AI;DR supplies generic inflation reports rather than the recognition-anchor mechanism.

**Instructions:**

- Ran `rg '^description:' kb/instructions --glob '*.md' | rg -i 'framework|scaffold|background|tutorial|reconstruct|recognition|minimal|compression|contribution|retain|derivation|behavioral|ablation|redund|point of use|reader'` and `rg -n -i 'recognition anchor|recognition condition|reconstructable|framework (recap|exposition|address)|scaffold|background|tutorial|point of use|local rationale|marginal value|delete|fold|behavioral test|ablation|downstream effect|core claim|contribution' kb/instructions --glob '*.md'`.
- Followed the compression bundle and kept [Marginal-value redundancy](../../../../instructions/compression-bundle/marginal-value-redundancy.md): it operationalizes the source's retention default with chunk-level deletion/folding questions, decision outcomes, and exceptions. `detail-overhang`, `redundant-restatement`, and `framework-decoration` were rejected as narrower surface checks that do not test the source's reconstructability-plus-activation boundary.
- Per the instructions collection's inverse-link posture, evaluated a `rests-on` return link from the marginal-value gate. Rejected it because this source explains one important application of the gate but is not the gate's general theoretical dependency.

**Global types:**

- Ran `rg '^description:' kb/types --glob '*.md'` and `rg -n -i 'reconstruct|recognition|framework|scaffold|background|reader|link|contribution|context|self-contained|local' kb/types --glob '*.md'`.
- `note.md` requires enough body context for use and `definition.md` gives cheap canonical glosses, but neither type contract is an observation or case that corroborates this note. No type candidate passed the articulation test.

**Link following and existing graph:**

- Followed the source's current links through information value, recognition, activation, history, composability, system-definition artifacts, and effects-based memory evaluation. Followed the retained candidates one hop through reverse compression's linking/observer-relative cluster, semantic work's frontloading/recompute cluster, and parametric reproduction's explicit-retention/authority cluster.
- Ran `rg -n 'the-framework-is-often-larger-than-the-durable-contribution' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions kb/types --glob '*.md'`. [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md) and [Warranted reader update is the objective of substantive writing](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) already link to the source; these existing edges were not presented as new reverse-edge candidates.

## Connections Found

- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) — **exemplifies**: reproducing a familiar framework around a small case-specific recognition is the framework-recap instance of expansion that adds no extractable structure for an intended reader.
- [Warranted reader update is the objective of substantive writing](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) — **grounds**: the retention rule depends on selecting the warranted change for the intended reader rather than preserving the volume of framework material present during composition.
- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) — **grounds**: placing generic framework treatment in one shared artifact works because the case-specific semantic judgment is still paid and retained as the recognition condition, mapping, and operation.
- [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) — **grounds**: reliable reconstruction does not preserve authoritative identity, provenance, contestability, currentness, or revision handles, sharpening the source's exception for unrecoverable local reasons and authority.
- [Marginal-value redundancy](../../../../instructions/compression-bundle/marginal-value-redundancy.md) — **operationalized-from**: the review gate adds a chunk-by-chunk deletion/folding procedure, explicit outcomes, and exceptions for deciding whether framework background earns its current context cost.

## Bidirectional Candidates

- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) ↔ source — **extends** from Reverse compression to source: the source develops one recurrent subtype of reverse compression and supplies a recognition-anchor remedy plus a behavioral boundary test.

## Reverse-edge Candidates

- [Ingest: Lessons from Building AI Agents for Financial Services](../../../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) → source — **is-evidence-for**: its deletion of model-absorbed procedural scaffolding while retaining exact fiscal-calendar normalization materially bears on the source's reconstructability boundary and should expose the later generalization from the source-side analysis.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Natural-language content lacks reliable dereference, so facts need reinforcement at point of use](../../../../notes/local-materialization-should-outperform-distant-declarations.md) — rejected as a direct candidate because the source already states the local-restatement boundary and links to the more directly applicable conditional-link rule, whose neighborhood reaches this mechanism.
- [An author should fix what the executor cannot determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — rejected because it governs author-time commitments versus live executor knowledge, not a linked note's division between shared framework and case-specific recognition.
- [Minimum viable vocabulary](../../../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) — rejected because optimizing a set of domain names for a bounded newcomer is adjacent to, but does not develop, the adequacy test for one framework address plus a case recognition anchor.
- [LLM recompute cost inverts the store-vs-recompute default](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — rejected because the source preserves the fuller framework as a named artifact to read; it does not ask each consumer to re-derive an unmaterialized value.
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — rejected because it predicts system-definition scaffolding across capability frontiers, whereas the source governs what one linked knowledge note retains for an intended consumer population.
- [Fintool](../../../../agent-memory-systems/lightweight/fintool.md) — rejected as a mediated duplicate of the already-linked practitioner ingest.
- [Ingest: Claude Fable 5 Made Most of My Agent Scaffolding Obsolete](../../../../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md) — rejected because its authority/scaffolding boundary is already represented by the linked financial-agent case and concerns operating instructions rather than case-note recap.
- [Checked inline blocks for shared instruction text](../../../../reference/proposals/checked-inline-blocks-for-shared-instruction-text.md) — rejected because it addresses literal, binding instruction reuse where runtime dereference is unsafe, not conditional loading of non-binding knowledge exposition.

## Index Membership

- [Context engineering](../../../../tags/context-engineering-README.md) — candidate for the selective Core Claims list: the note gives a concrete retention, linking, and behavioral-testing rule for keeping familiar framework recap out of bounded artifacts without losing activation or auditability.

## Synthesis Opportunities

None

## Maintenance Observations

- The H1 and description now assert “Linked notes should retain recognition anchors, not reconstructable framework recaps,” while the path still carries the earlier `the-framework-is-often-larger-than-the-durable-contribution` slug. A closing author should decide whether to preserve the stable address or run the repository's relocation workflow and reconcile visible inbound link text.

## Flags

None
