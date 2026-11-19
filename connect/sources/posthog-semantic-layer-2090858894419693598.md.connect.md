---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/posthog-semantic-layer-2090858894419693598.md"
source_has_frontmatter: true
date: "2026-08-22"
depth: standard
---

# Connection Report: Building a semantic layer at PostHog

**Source:** [Building a semantic layer: What it is and how we did it at PostHog](../../../sources/posthog-semantic-layer-2090858894419693598.md)

## Discovery Trace

No semantic-search service or scored retrieval was used; discovery was repo-local, so no candidate scores were available.

**Curated heads and tag routing:**

- Read `kb/notes/tags-README.md` and the selective heads `agent-memory-README.md`, `context-engineering-README.md`, `observability-README.md`, and `kb-maintenance-README.md`. These surfaced the strongest theoretical clusters: explicit authority, activation, effects-based evaluation, lineage, and drift detection.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The strongest non-note surfaces were Commonplace's freshness architecture, the Palantir ontology/decision-trace ingest, and Cognee's differently scoped use of “semantic layer.”
- The source carries `tags: [x-article]`, but no authorised destination has an `x-article-README.md`. The exact by-tag description command `rg -l '^tags:.*\bx-article\b' kb/<destination>/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` returned no files in notes, reference, agent-memory-systems, or agentic-systems. In sources it returned two unrelated X captures, which were rejected.

**Complete title and description scans:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'` over every authorised local destination: `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`.
- The notes scans flagged authoritative records, authority assignment, compiled-view drift, activation, effects-based evaluation, coordination value, explicit retention, and source-of-truth rules. The reference scan flagged freshness baselines. The agent-memory-system scan flagged Cognee and ontology-oriented systems. The agentic-system scan flagged only Semantic Engine, a lexical rather than architectural match. The sources scan flagged the Palantir ontology/decision-trace ingest and an organisational-KB critique of “single source of truth.”

**Body search:**

- `rg -n -i '(semantic layer|semantic catalog|governed catalog|context warehouse|business metric|metric definition|single source of truth|canonical definition)' ...` found the PostHog source, the Palantir ingest's discussion of thinner metric semantics, Cognee's graph-backed semantic layer, and several generic single-source mentions.
- `rg -n -i '(approved|approval|canonical|governed|governance|human review|human[- ]owned|authority)' kb/notes --glob '*.md'` surfaced authority and commitment candidates. The authoritative-record and explicit-authority notes survived the articulation test; coordination value was explanatory but redundant.
- `rg -n -i '(drifted|drift|stale|staleness|snapshot|lineage|provenance)' kb/notes --glob '*.md'` surfaced compiled-view alignment, checked-derived-copy, and general staleness notes. Compiled-view alignment was the precise match because PostHog snapshots an insight query, retains origin lineage, and computes drift on read.
- `rg -n -i '(catalog|ontology|metric|definition|authoritative|canonical|governance|approval|drift)' kb/agent-memory-systems kb/agentic-systems --glob '*.md'` surfaced Cognee, Graphiti, operational-ontology coverage, and Semantic Engine. None matched PostHog's combination of human-governed business definitions and native SQL execution closely enough to retain.

**Link following:**

- Followed [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) to explicit retention, commitment-created ground truth, and compiled-view alignment. This separated the canonicality claim from the narrower drift mechanism.
- Followed the agent-memory curated head through [Make Authority Explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md), [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md), [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md), and [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md). PostHog's proposed/approved states, drift bit, catalogue-use measure, and golden-question accuracy map onto four distinct stages rather than one generic governance claim.
- Followed the Palantir ingest to its distinction between a prescribed ontology and a trace-inferred world model. PostHog supplies a narrower prescribed layer—metrics, trusted tables, and joins—whose definitions remain executable through existing data primitives.
- Followed Commonplace's freshness architecture to exact accepted-input baselines and current-state comparison. It is a useful implementation comparison to PostHog's source-query snapshot and live drift flag, without implying that either system copied the other.
- Followed Cognee and Graphiti through their storage, authority, and read-back sections. Their automatically extracted graph memory differs enough from PostHog's curated business-semantic catalogue that a direct edge would make the shared term “semantic layer” more confusing, not less.
- Read [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) because the source includes an anecdotal three-agent comparison and proposes a golden-question evaluation. The available agent contexts, tools, tables, metric representations, approval workflow, and question set remain fixed outside those comparisons.
- Verified every retained and rejected candidate path before writing this report.

**Destination decisions:**

- `notes`: retained four source-side relationships and two reciprocal evidence candidates around authority, drift, activation, and effect-based evaluation; rejected broader source-of-truth and routing matches.
- `reference`: retained one comparison with the shipped freshness architecture.
- `agent-memory-systems`: no candidate survived; the closest systems solve automated graph-memory or general ontology problems rather than governed executable business metrics.
- `agentic-systems`: no plausible whole-harness match survived; Semantic Engine is ingest infrastructure, not a semantic-governance layer.
- `sources`: retained the Palantir ontology/decision-trace ingest as a comparison on ontology breadth and construction strategy.
- `external`: authorised for already-known targets, but no additional external target was supplied in context; open-web prospecting was skipped as required.
- `kb/work/` and `kb/instructions/` were excluded by the source collection contract and were not prospected.

## Connections Found

- [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) -- **is-evidence-for**: PostHog's motivating case is that several capable agents can reconstruct plausible metric content while none thereby acquires the authority to decide which definition is operative; the proposed remedy is a separately governed, explicit record.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) -- **rests-on**: PostHog does not propose counting catalogue entries as success. Its stated measures separately ask whether answers become correct, whether agents use approved metrics, and whether the catalogue continues to grow, although the source reports no results yet.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **rests-on**: an approved metric helps only if the agent checks the catalogue and executes the governed definition instead of silently deriving its own SQL; PostHog names that uptake as an explicit measurement target.
- [Palantir Ontology vs Decision Traces](../../../../sources/palantir-ontology-vs-decision-traces.ingest.md) -- **compares-with**: both concern structured LLM-facing semantics, but PostHog prescribes a deliberately thin catalogue of metrics, trusted tables, and joins over an existing warehouse, whereas the Palantir framing ranges over a broader world model and contrasts up-front ontology with trace-inferred structure.
- [Freshness architecture](../../../../reference/freshness-architecture.md) -- **compares-with**: both retain an accepted snapshot and compare it with a current input to expose drift. PostHog does this live for insight-backed metric definitions; Commonplace registers exact input snapshots and freshness baselines for review-pair targets.

## Bidirectional Candidates

- [Make Authority Explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md) ↔ source -- source-side **is-evidence-for**; target-side **evidenced-by**: agent drafts remain proposed, a human promotes definitions to approved status, edits revoke approval, and consumers receive one explicit canonicality predicate. The report does not show whether human review remains accurate or scales.
- [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) ↔ source -- source-side **is-evidence-for**; target-side **evidenced-by**: an insight-backed metric retains a server-side query snapshot plus its origin, compares them on read, and marks divergence instead of silently treating the compiled metric as current. The described check covers that lineage path, not every metric, join, or upstream table dependency.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Coordination value](../../../../notes/definitions/coordination-value.md) -- rejected as redundant: adopting one shared metric definition plausibly creates coordination value, but the source's distinctive contribution is its authority, execution, and drift machinery rather than a new account of why shared conventions are valuable.
- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -- rejected because PostHog is not describing a raw-ingress failure. It starts from already structured warehouse data and adds governed semantic commitments; the authority and activation notes carry the reader need more precisely.
- [Agent statelessness makes routing architectural, not learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) -- rejected because the source shows repeated reinvention across tools but does not establish session statelessness as the cause. Missing shared authority and inconsistent data access are sufficient explanations.
- [Local materialization should outperform distant declarations](../../../../notes/local-materialization-should-outperform-distant-declarations.md) -- rejected because PostHog exposes one live SQL-readable catalogue rather than duplicating declarations near each use; the note's proximity intervention is not tested here.
- [Cognee](../../../../agent-memory-systems/reviews/cognee.md) -- rejected as a terminology collision: Cognee's “semantic layer” is an automatically extracted graph/vector memory over arbitrary documents and traces, while PostHog's is a human-governed catalogue of executable business semantics. The difference is too broad for a useful system comparison edge.
- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) -- rejected because “semantic” is only lexical overlap; Semantic Engine stages source chunks and embeddings before KB promotion, not canonical data definitions for runtime queries.
- [How we built our knowledge base](../../../sources/how-we-built-our-knowledge-base-2077822555159945507.md) -- rejected because its critique of organisational “single source of truth” concerns consolidating heterogeneous documents into one platform. PostHog leaves data in place and centralizes only selected semantic commitments, so the apparent tension dissolves once the objects are distinguished.

## Index Membership

None

## Synthesis Opportunities

None. The source is a compact implementation witness joining authority, lineage, activation, and outcome evaluation, but those relationships are already stated together by the agent-memory requirements cluster. It adds a concrete executable-catalogue design rather than a missing higher-order claim.

## Maintenance Observations

None

## Flags

- **Fixed-decomposition boundary:** the opening three-agent comparison does not hold agent context, tool access, table visibility, prompts, or query procedures constant, so it demonstrates disagreement but does not identify which missing signal caused it. The proposed golden-question evaluation can measure improvement within PostHog's fixed catalogue, metric forms, agent interfaces, approval workflow, and question set; without rival decompositions it cannot validate those choices as a whole.
- **Outcome-evidence boundary:** the source describes a beta design and future success measures, not benchmark results, adoption data, error rates, or a controlled comparison with and without the semantic layer.
