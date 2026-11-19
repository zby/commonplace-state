---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/building-self-correcting-memory-in-openwiki-2092280107033616451.md"
source_has_frontmatter: true
date: "2026-08-25"
depth: standard
---

# Connection Report: Building Self-Correcting Memory in OpenWiki

**Source:** [Building Self-Correcting Memory in OpenWiki](../../../../sources/.snapshots/building-self-correcting-memory-in-openwiki-2092280107033616451.md)

## Discovery Trace

**Description listing scan:**

- Read the complete title surfaces produced by `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for every authorised local destination: `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` across all five destinations. The notes scan retained the lineage, staleness-detection, localized-retention, and compiled-view candidates. The reference scan retained `freshness-architecture.md`. The agent-memory scan found the same-system OpenWiki review. The sources scan retained the earlier Karpathy LLM Wiki ingest and weaker forgetting/temporal-memory comparisons. The agentic-systems scan found no whole-system analysis matching this memory-subsystem mechanism.
- The snapshot carries `tags: [x-article]`, but no destination has an `x-article-README.md`. The by-tag query `rg -l '^tags:.*\bx-article\b' kb/<destination> --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` returned no candidates in any authorised destination.

**Topic indexes:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The note and agent-memory heads located the source in lifecycle, lineage, and external-system-review work; the reference head exposed Commonplace's freshness analogue.
- Read `kb/sources/COLLECTION.md` before discovery. The candidate edges below use only its authorised `is-evidence-for`, `compares-with`, and sparing `see-also` labels for the applicable destinations. Read `kb/notes/COLLECTION.md` before proposing note-side `evidenced-by` return links.

**Body search:**

- `rg -n -i "stale|staleness|freshness|invalidate|source changes|evidence version|self-correct|forget" kb/notes/ --glob '*.md'` — surfaced the source-change lineage note, make-like staleness detection, compiled-view lifecycle requirements, and several keyword-only forgetting matches.
- `rg -n -i "claim[- ]level|individual claims|claim.*evidence|evidence.*claim|dependency|lineage|selective revision|re-?verif|recheck|reconcile" kb/notes/ --glob '*.md'` — retained localized retention and distinguished claim-granular review from document-level timestamp checks.
- `rg -n -i "stale|staleness|freshness|baseline|source.*change|evidence.*version|claim" kb/reference/ --glob '*.md'` — retained `freshness-architecture.md`; review-system and ADR hits were implementation detail or historical decisions rather than better traversal targets.
- `rg -n -i "openwiki|stale|staleness|freshness|forget|claim.*evidence|evidence.*claim|versioned evidence|self-correct" kb/agent-memory-systems/ --glob '*.md'` — found the existing OpenWiki review and several systems with different invalidation mechanisms. The same-system review was the only candidate with a direct maintenance payoff.
- `rg -n -i "openwiki|claim|stale|freshness|forget|self-correct|wiki|documentation" kb/agentic-systems/ --glob '*.md'` — produced only generic documentation and staleness mentions; no candidate passed the articulation test.
- `rg -n -i "claim.*evidence|evidence.*claim|stale|staleness|forget|self-correct|versioned|source.*change|temporal" kb/sources/ --glob '*.md'` — retained the Karpathy LLM Wiki source as the closest architectural precursor and evaluated Graphiti and budgeted forgetting as weaker comparisons.

**Link following:**

- Followed [Source changes should surface downstream review targets](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) to [Link graph plus timestamps enables make-like staleness detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) and [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). OpenWiki supplies a more granular dependency record than a file link, but its deterministic version comparison only detects review need; it does not mechanically verify natural-language claim truth.
- Followed [Localized retention pays when sparse changes have bounded impact](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) to [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md). OpenWiki's pre-existing claim units and claim-to-code evidence links match the localization mechanism, while its reported evaluation is only vendor evidence for the claimed cost/result effects.
- Read the existing [OpenWiki review](../../../../agent-memory-systems/reviews/openwiki.md) in full. Its pinned July 2026 account explicitly reports no claim-level provenance or deterministic invalidation, making this August 2026 source a refresh signal rather than authority for silently rewriting the code-grounded review.
- Followed the source-side comparison to [Karpathy's LLM Wiki ingest](../../../../sources/karpathy-llm-wiki.ingest.md). Karpathy supplies the raw/wiki/schema architecture and an ingest/query/lint lifecycle; this source adds a concrete claim/evidence freshness mechanism to the maintenance problem that architecture leaves open.
- External prospecting was skipped. The supplied X article is already the external source in hand, and `external` authorisation does not make the open web a prospecting surface.

## Connections Found

- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — **is-evidence-for**: OpenWiki records each material wiki claim's supporting code evidence and evidence version, then turns a changed version into an explicit downstream re-verification target. This is a concrete system witness for the note's interruption-first lineage mechanism, not proof that the mechanism is sufficient.
- [Link graph plus timestamps enables make-like staleness detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — **compares-with**: both designs treat dependency-version mismatch as a review trigger rather than a truth verdict, but OpenWiki uses claim-to-code evidence versions instead of document links and Git timestamps. The comparison exposes the precision gained by claim-granular dependencies and the evidence-extraction cost they require.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) — **is-evidence-for**: the source reports that pre-existing claim units plus evidence links let updates recheck affected page claims rather than rebuild the whole wiki, and that cost scales with changed code rather than total claims. The reported 80-to-9 stale-claim and 15-to-0 hallucination changes are vendor-reported evidence, not an independently inspected experiment.
- [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) — **is-evidence-for**: OpenWiki treats generated wiki claims as source-dependent views, records code evidence versions, persists distrust after evidence changes, and clears it only after reconciliation. This directly instantiates the note's source-version and stale-detection requirements for compiled memory.
- [Freshness architecture](../../../../reference/freshness-architecture.md) — **see-also**: both systems define freshness as whether current inputs match an accepted version, explicitly separate staleness from wrongness, and preserve stale state until rechecking. Commonplace registers review-pair inputs and evidence baselines; OpenWiki reports claim-to-code evidence versions and page-level reconciliation, so the direct analogue helps compare target granularity and evidence semantics.
- [OpenWiki](../../../../agent-memory-systems/reviews/openwiki.md) — **compares-with**: the pinned review describes an earlier OpenWiki with Git-scoped wiki updates but no claim-level provenance or deterministic invalidation. This source reports a later claims runtime, OKF v0.2 trust metadata, and evaluation results, giving a reader the exact version-sensitive axis on which the code-grounded review now needs refresh rather than silent amendment.
- [Ingest: LLM Wiki](../../../../sources/karpathy-llm-wiki.ingest.md) — **compares-with**: Karpathy's raw/wiki/schema architecture names ingest, query, and lint but leaves the semantic maintenance oracle open; OpenWiki's source-evidence versions, persistent staleness, and claim reconciliation supply one concrete answer for code-derived wikis while adding operational state and claim-extraction cost.

## Bidirectional Candidates

- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) <-> source — **evidenced-by**: once the matching ingest exists, a return link would provide a concrete claim-to-code lineage implementation while preserving the source's vendor-report evidence boundary.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) <-> source — **evidenced-by**: the source reports both the matching claim decomposition and the predicted changed-footprint scaling, with the caveat that the evaluation is not independently reproduced here.
- [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) <-> source — **evidenced-by**: OpenWiki is a direct system instance in which a compiled wiki view carries source versions and stays stale until reconciliation.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — OpenWiki deterministically detects that supporting evidence changed, but the agent must still judge whether each natural-language claim remains true. Treating the runtime as the note's checked branch would confuse stale-candidate detection with mechanical verification; the source-change lineage candidate captures the actual regime.
- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) — the title-level “forgetting” match is misleading. This source keeps claims and withdraws trust until re-verification; it does not report redaction, decay, retirement, policy relaxation, or point-in-time supersession semantics.
- [Stale self-description conceals its own staleness](../../../../notes/stale-self-description-conceals-its-own-staleness.md) — OpenWiki maintains documentation about a repository, but the source does not establish the stronger reflexive case in which the describing artifact is consumed by the same self-modifying process whose organization it describes.
- [Ingest: Graphiti: Temporal Knowledge Graph for AI Agents](../../../../sources/graphiti-temporal-knowledge-graph.ingest.md) — Graphiti's fact-validity intervals and point-in-time queries distinguish historical truth from current truth; OpenWiki's evidence-version mismatch instead records uncertainty pending recheck. The shared word “invalidation” does not create enough traversal value to justify another comparison edge.
- [Ingest: Novel Memory Forgetting Techniques for Autonomous AI Agents](../../../../sources/novel-memory-forgetting-techniques-autonomous-ai-agents.ingest.md) — that paper prunes low-scoring memories under a capacity budget; OpenWiki retains claims and marks their warrant stale after source change. The mechanisms solve different lifecycle problems despite sharing “forgetting” language.
- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) — its possible stale-source invalidation is an open watch item in a general ingest workbench, not an implemented claim-to-evidence freshness loop or a whole-system OpenWiki analogue.

## Index Membership

None.

## Synthesis Opportunities

- The source, [Freshness architecture](../../../../reference/freshness-architecture.md), and [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) jointly suggest a sharper lifecycle distinction: **epistemic forgetting withdraws trust after evidence changes without deleting, temporally superseding, or capacity-pruning the retained claim**. The source states the OpenWiki instance; a future synthesis would need to establish how broadly the distinction transfers across memory systems.

## Maintenance Observations

- [OpenWiki](../../../../agent-memory-systems/reviews/openwiki.md) is pinned to commit `23428de0cc0b1b6d3e5d09be413e92a5d6ee451f` and last checked 2026-07-06. Its claims that the system has “no claim-level provenance” and no deterministic invalidation are directly challenged by this 2026-08-25 vendor article about OpenWiki 0.4.0. Refresh the checkout and code-grounded review before changing those claims; the article alone establishes a maintenance trigger, not current implementation correspondence.

## Flags

- The matching authored surface `kb/sources/building-self-correcting-memory-in-openwiki-2092280107033616451.ingest.md` did not exist during this run. All outbound and return-link candidates are for that future ingest; the immutable snapshot must not be edited or linked as durable authority.
- Evidence boundary: this is an affiliated practitioner article with self-reported evaluation numbers and no retained methods, checkpoint corpus, code commit, or independent reproduction. Treat the mechanism and results as reported claims until code and evaluation artifacts are inspected.
