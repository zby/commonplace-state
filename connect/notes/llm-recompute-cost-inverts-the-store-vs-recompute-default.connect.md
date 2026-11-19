---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md"
source_has_frontmatter: true
date: "2026-08-23"
depth: standard
---

# Connection Report: LLM recompute cost shifts the store-vs-recompute balance

**Source:** [LLM recompute cost shifts the store-vs-recompute balance](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md)

## Discovery Trace

**Setup and authorised breadth:**

- Read the connect skill, `kb/cache/types/connect-report.md`, its schema, the source, and `kb/notes/COLLECTION.md` in full before judging candidates. The source has frontmatter and its SHA-256 was confirmed as `9837a9d9f73a0b8e8c1fb9f6377f0efad829d0af12d8454c4935897304cdc00c`.
- The notes contract authorises local prospecting in `kb/notes/`, `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`; `kb/work/` is excluded. The accepted labels below are drawn only from the notes contract for each destination.
- The reserved `external` destination is authorised, but the user supplied no external target and none was already loaded. External prospecting was therefore skipped; no web, MCP, or external semantic search was used. Repository searches returned no relevance scores.

**Curated heads and complete surfaces:**

- Read the matching tag heads [Computational model](../../../../tags/computational-model-README.md) and [Context engineering](../../../../tags/context-engineering-README.md), plus the destination heads `kb/notes/README.md`, `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. Neither matching tag head declares `complete: true`, so neither by-tag search was skipped.
- Generated the complete H1 surface once for each authorised destination by running `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, substituting `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions` in turn.
- Generated the complete description surface once for each of the same destinations with `rg '^description:' kb/<destination>/ --glob '*.md'`.
- For both source tags and every destination, ran the guarded queries `rg -l '^tags:.*\bcomputational-model\b' kb/<destination>/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and `rg -l '^tags:.*\bcontext-engineering\b' kb/<destination>/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`. The tag slices produced candidates mainly in notes and reference; types, agent-memory systems, and instructions had no tag matches, while agentic systems and sources returned only weak computational-model matches.

**Notes destination:**

- Body patterns were `recomput|materializ|cache|stored copy|derived copy`, `model-side|on-demand deriv|external.*deriv|replace.*work|substitut`, `maintenance cost|future value|expected cost|validity window`, and `access burden|transformation burden|frontload|partial evaluation`, each run with `rg -n` over `kb/notes/ --glob '*.md'`.
- Kept [Local materialization should outperform distant natural-language declarations](../../../../notes/local-materialization-should-outperform-distant-declarations.md): it turns the source's substitution condition into a refutable point-of-use intervention. Kept [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md): it separates the two kinds of model work that a materialized answer may remove.
- Rejected [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) as a broad scarcity premise that does not sharpen the three-path comparison, and [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) as a memory-promotion restatement without the source's serving-path or checking mechanism.
- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) was followed but rejected as a new outbound edge because it already authors the useful inbound `extends` link and the reciprocal direction adds no distinct reader need.

**Types destination:**

- Body patterns were `mark|recomput|derived|complete|covered_by`, `validat|invalidation|check`, and `frontload|cache|material`, each run over `kb/types/`.
- [Tag README](../../../../types/tag-readme.md) is the exact checked-mark instance, but the source already links it and the type already uses this source as its value theory. No new type edge survived.

**Reference destination:**

- Body patterns were `recomput|materializ|cache|stored copy|derived copy`, `checked inline|checked-inline|marked.*region|frontload|complete|covered_by`, `source of truth|ground truth|invalidat|validator.*re-deriv|re-deriv`, and `model reader|model-side|context cost|bounded context|replace.*work`, each run over `kb/reference/`.
- Kept [Checked inline blocks for shared instruction text](../../../../reference/proposals/checked-inline-blocks-for-shared-instruction-text.md): it directly develops the first open question into a machine-locatable, source-bound region with deterministic equality and an explicit lifecycle.
- Rejected [ADR 026](../../../../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) as a separate edge because the source already reaches the shipped instance through the tag-README type, and the ADR adds implementation history rather than a new decision boundary.

**Agent-memory-systems destination:**

- Body patterns were `recomput|materializ|precomput|cache|compiled view|generated view`, `validation|validator|checked|drift|fresh|invalidation`, `context pack|summary|summar|prompt-time|prompt injection|read-back`, and `amortiz|reasoning premium|replace.*work|cost`. Narrowing passes used `rebuildable cache|disposable.*cache|warm index|source files invalidat`, `displace raw|instead of.*raw|pre-digestion|cached wiki|dirty flags`, `incremental|fresh vector|derived projection|source change`, and `materialized.*answer|cached.*summary|summary.*source|regenerat`.
- Kept [sage-wiki](../../../../agent-memory-systems/reviews/sage-wiki.md) as a sparse companion to the source's second open question: it quarantines generated answers, promotes them through agreement or source-grounding checks, and demotes and de-indexes them when sources change, while the review preserves the limit that this is managed advisory trust rather than deterministic equality.
- Rejected [SkillNote](../../../../agent-memory-systems/reviews/skillnote.md): it materializes registry rows into native skill files and tracks sync lineage, but its review explicitly lacks behavioral faithfulness evidence and does not establish a checked answer replacing model derivation. Rejected [Beever Atlas](../../../../agent-memory-systems/reviews/beever-atlas.md): its cached wiki pages and dirty flags expose refresh machinery, but the review does not establish semantic fidelity or a break-even comparison.

**Agentic-systems destination:**

- Body patterns were `recomput|materializ|precomput|cache|compiled|derived`, `context cost|bounded context|prompt|summar|replace.*work`, and `validation|validator|checked|fresh|drift`, each run over `kb/agentic-systems/`.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) was the closest result. Its memoization key omits semantically relevant inputs and hides cache hits from traces, but this is a deterministic-component cache-identity warning rather than a checked model-facing materialization case. No agentic-system edge survived.

**Sources destination:**

- Body patterns were `recomput|materializ|memoiz|cache|build system`, `reasoning premium|amortiz|distill.*skill|skill.*distill|replace.*reason`, `context cost|context efficiency|token cost|prompt cost|context budget`, and `validator|checked|freshness|invalidat|drift`, each run over `kb/sources/`.
- Kept [Build Systems à la Carte](../../../../sources/build-systems-a-la-carte.ingest.md) as the deterministic software baseline and freshness/rebuilder boundary. Kept [Machine Studying](../../../../sources/machine-studying.ingest.md) for its preparation-versus-inference budget surface and low-budget corpus-map result. Kept [Reason Wide, Not Deep](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) for its held-out evidence that one retained natural-language skill can displace recurring reasoning while reducing output-token cost, together with its explicit missing-cost caveats.

**Instructions destination and inverse-direction pass:**

- Read `kb/instructions/COLLECTION.md` before evaluating reverse edges. Its note edge is the exceptional meta-reader label `rests-on`; procedures must remain executable without theory-link chasing.
- Body patterns were `recomput|materializ|cache|stored copy|derived copy`, `frontload|complete: true|covered_by|skip.*rg|by-tag`, `context cost|bounded context|model.*derive|replace.*work`, and `checkable|checked|validator|re-deriv|source-bound`, each run over `kb/instructions/`.
- [Connect — Discovery Only](../../../../instructions/cp-skill-connect/SKILL.md) uses a validated `complete: true` mark to skip a tag sweep, but it delegates the rule to the tag contract and does not require this source's economic argument to execute or to be maintained. An exceptional reverse `rests-on` edge would add no concrete meta-reader value.

**Backlinks and one-hop link following:**

- Ran `rg -n "llm-recompute-cost-inverts-the-store-vs-recompute-default|LLM recompute cost" kb/ --glob '*.md'`. Existing inbound links from the checked-copy, insufficient-summary, addressability, semantic-relocation, retained-instruction, documentation-recoverability, commitment, enforced-tag-README, type, and ADR neighborhoods were treated as graph state rather than automatically mirrored candidates.
- Followed local materialization to checked copies, frontloading, model-resolved indirection, and unscoped context; followed access/transformation burden to scheduler–LLM separation, bounded-context orchestration, and soft degradation. These traversals preserved the two note candidates as distinct behavioral and diagnostic continuations rather than redundant cache rules.
- Followed the checked-inline proposal to checked copies, local materialization, frontloading, model-resolved indirection, and build-time generation. Followed sage-wiki through its trust-managed Q&A, source-change demotion, tiering, and pull read-back sections. Followed Build Systems à la Carte, Machine Studying, and Reason Wide, Not Deep through their linked frontloading, learning, checking, and fixed-decomposition neighborhoods. No additional candidate passed the articulation test.

**Path verification:**

- Ran `test -e` over every path named in the accepted, bidirectional, rejected, index, and traced-head sets. Every listed path exists. No raw-text candidate or broken traversal path was found.

## Connections Found

- [Local materialization should outperform distant natural-language declarations](../../../../notes/local-materialization-should-outperform-distant-declarations.md) — **extends**: develops one benefit channel in the source's ledger into a refutable comparison of generated point-of-use materialization against declaration-only presentation, including the possibility that context bulk cancels the gain.
- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **extends**: separates finding inputs from deriving the requested answer, so a reader can identify which work each of the source's three serving paths removes before assigning costs.
- [Checked inline blocks for shared instruction text](../../../../reference/proposals/checked-inline-blocks-for-shared-instruction-text.md) — **see-also**: turns the source's open machine-locatable, source-bound natural-language-region question into a concrete Commonplace option space with deterministic equality, refresh behavior, and adoption criteria.
- [sage-wiki](../../../../agent-memory-systems/reviews/sage-wiki.md) — **see-also**: supplies a concrete managed-staleness design for non-deterministically checked generated answers—quarantine, agreement or grounding, promotion, and source-change demotion—while retaining the boundary that this yields advisory trust rather than mechanical correctness.
- [Build Systems à la Carte](../../../../sources/build-systems-a-la-carte.ingest.md) — **evidenced-by**: supplies the formal deterministic-software baseline—minimal rebuilding as generalized memoization and a rebuilder ladder—that the model-facing comparison modifies, while explicitly bounding transfer to mechanically recomputable values.
- [Machine Studying](../../../../sources/machine-studying.ingest.md) — **evidenced-by**: reports a precomputed corpus map helping mainly at low inference budgets while forced search closes much of the gap at high budgets, a bounded instance of materialization paying where it substitutes for expensive discovery rather than unconditionally.
- [Reason Wide, Not Deep](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) — **evidenced-by**: reports held-out cases where a one-time distilled natural-language skill displaces recurring reasoning and uses 2.9–4.5 times fewer output tokens, while its missing input-token, cache, latency, maintenance, and observed break-even costs qualify the source's total-cost requirement.

## Bidirectional Candidates

- [Local materialization should outperform distant natural-language declarations](../../../../notes/local-materialization-should-outperform-distant-declarations.md) → source — **grounds**: the return path would give the conjecture's bulk, checking, and gain-offset conditions the source's complete model-side, external-on-demand, and persisted-materialization cost comparison plus its explicit substitution requirement.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — the broad scarcity premise is compatible with the source but does not distinguish its three serving paths or checking boundary.
- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) — already authors the useful inbound `extends` edge; a reciprocal source edge would not serve a distinct traversal need.
- [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) — restates the future-value/maintenance threshold for memory promotion without the source's substitution test, serving-path comparison, or validity window.
- [Tag README](../../../../types/tag-readme.md) — already linked inline from the source, and its contract already identifies this source as the mark's value theory.
- [ADR 026](../../../../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — implementation history for the already-linked mark instance rather than a distinct reader need.
- [SkillNote](../../../../agent-memory-systems/reviews/skillnote.md) — materializes registry instructions, but the review does not establish behavioral substitution or a deterministic check of the model-consumed value.
- [Beever Atlas](../../../../agent-memory-systems/reviews/beever-atlas.md) — dirty flags and cached wiki pages expose refresh machinery, but not semantic fidelity or a total-cost result.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) — exposes an incomplete cache identity for deterministic components, not the checked model-facing store-versus-recompute decision the source explains.
- [Connect — Discovery Only](../../../../instructions/cp-skill-connect/SKILL.md) — uses the checked-mark instance but already delegates its skip rule to the type contract; an exceptional reverse theory dependency would not improve execution or maintenance.

## Index Membership

- [Context engineering](../../../../tags/context-engineering-README.md) — add among the core claims on checked copies, cache economics, addressability, and substitution: this source supplies the model-specific three-path decision and states when a materialized answer actually replaces work.
- [Computational model](../../../../tags/computational-model-README.md) — add under Instruction Properties beside frontloading and local materialization: this source explains when a model-facing precomputed value earns persistence and how its natural-language payload can remain deterministically checked through a symbolic envelope.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Split candidate: the source now composes separable assertions about serving economics, deterministic checking, and mixed representational form, while its surviving connections span behavioral uptake, burden diagnosis, validation mechanisms, managed staleness, and evaluation evidence. The safety claim currently qualifies the economic claim coherently, but further development of either open question should move to a dedicated note rather than add another independent cluster here.
