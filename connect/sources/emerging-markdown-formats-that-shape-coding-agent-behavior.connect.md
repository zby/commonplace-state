---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/emerging-markdown-formats-that-shape-coding-agent-behavior.md"
source_has_frontmatter: true
date: "2026-08-03"
depth: standard
---

# Connection Report: Emerging Markdown Formats That Shape Coding Agent Behavior

**Source:** [Emerging Markdown Formats That Shape Coding Agent Behavior](../../../sources/emerging-markdown-formats-that-shape-coding-agent-behavior.md)

## Discovery Trace

**Description listing scan:**

- Generated fresh complete title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: notes (329 titles), reference (125), agent-memory-systems (172), agentic-systems (10), and sources (422).
- Scoped `rg '^description:' kb/notes --glob '*.md' | rg -i 'instruction|context|memory|artifact|skill|procedure|workshop|authority|promotion|compiled|projection'` flagged [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), [AGENTS.md should be organized as a control plane](../../../../notes/agents-md-should-be-organized-as-a-control-plane.md), [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md), [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md), [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md), [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md), [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), and [A functioning knowledge base needs a workshop layer, not just a library](../../../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md).
- Equivalent scoped description scans over `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` used the same role terms. Reference hits restated Commonplace's own implementation rather than adding a comparison target. Related-system hits were system-specific and did not match this ecosystem essay's unit of analysis. Source hits identified [Context Engineering for AI Agents in Open-Source Software](../../../../sources/context-engineering-ai-agents-oss.ingest.md), [Harness Engineering](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md), and [The What & When of Self-Evolving Agents](../../../../sources/the-what-and-when-of-self-evolving-agents.ingest.md) as the strongest comparisons.

**Topic indexes:**

- Read `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The notes head routed toward context engineering, artifact analysis, and agent memory; the external-system heads confirmed that this essay is not a code-grounded system review. No matching complete tag head was available from the source, which carries no tags.

**Body search:**

- `rg -n -i "AGENTS\\.md|SKILL\\.md|always-loaded|always loaded|standing (rule|guidance)|vendor-specific|compatibility bridge|compiled view|source of truth|canonical (file|source)|local memory|machine-local|promotion.*(rule|skill)|contextual activation|intent compiler|metacode|work-in-flight|workshop" kb/notes --glob '*.md'` found the role-separation, compiled-view, activation, promotion, and workshop candidates above. The article supplies an ecosystem inventory and a simple human-reviewed promotion example; the notes supply the mechanisms and missing safeguards.
- The analogous body searches over `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` found no additional candidate that passed the articulation test. `kb/agent-memory-systems/reviews/synapptic.md` is a concrete canonical-profile-to-vendor-files implementation, but the article does not examine it and [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) already routes readers there.
- `rg -n -i "metacode|AGENTS\\.md|SKILL\\.md|standing rules|local memory|machine-local memory|intent compiler|vendor-specific" kb/sources --glob '*.md'` found the three source comparisons retained below. The OSS study is empirical breadth on context files, Harness Engineering is a production-depth example of the short-map pattern, and The What & When essay provides a broader substrate-and-persistence taxonomy.

**Link following:**

- Followed the neighborhood from [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) to the control-plane, skill, loading-frequency, and Synapptic compiled-view artifacts. This showed that the article corroborates the surface inventory but does not replace the KB's loading-cadence and source-of-truth analysis.
- Followed [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) to contextual activation and trace-signal requirements, and followed [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) to the constraining gradient. The article's tentative-observation-to-shared-rule path is a useful practitioner instance, but recurrence and human review alone do not supply verification, bounded abstraction, maintenance cost, lineage, or activation.
- Followed the planning-file candidates into [A functioning knowledge base needs a workshop layer, not just a library](../../../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md). Kept it as a rejected boundary candidate: the source groups plans with durable repository knowledge, whereas the note distinguishes consumed work-in-flight from retained library artifacts.

## Connections Found

- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- **is-evidence-for**: the essay independently inventories standing context files, on-demand skills, domain documents, and machine-local memory, corroborating the note's surface distinctions while adding versioned plan/spec files as a neighboring role.
- [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) -- **is-evidence-for**: its observation → recurrence/impact review → rule, skill, ADR, or domain-document path is a concrete practitioner example of promoting candidate memory into stronger and more costly durable surfaces.
- [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) -- **is-evidence-for**: the recommendation to keep one canonical file and use thin vendor-specific bridges is a practical instance of source-of-truth discipline across assistant-facing views, though it does not specify regeneration or freshness checks.
- [Context Engineering for AI Agents in Open-Source Software](../../../../sources/context-engineering-ai-agents-oss.ingest.md) -- **compares-with**: this essay supplies a 2026 practitioner taxonomy of multiple Markdown roles, while the study supplies empirical adoption and evolution data for context files but no behavior measurement.
- [Harness Engineering: Leveraging Codex in an Agent-First World](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) -- **compares-with**: both recommend a short agent-facing map pointing to deeper versioned sources, but Harness Engineering reports one production implementation and stronger enforcement machinery rather than a cross-ecosystem inventory.
- [The What & When of Self-Evolving Agents](../../../../sources/the-what-and-when-of-self-evolving-agents.ingest.md) -- **compares-with**: both place persistent files between one-session prompting and model-weight change; the 3×3 substrate-by-horizon frame separates dimensions that this essay compresses into the single term “metacode.”

## Bidirectional Candidates

- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) <-> source -- **evidenced-by** from the note: the snapshot is a dated practitioner inventory that adds planning artifacts and explicit machine-local/shared authorship distinctions to the harness-surface comparison.
- [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) <-> source -- **evidenced-by** from the note: the snapshot gives a concise observed-memory-to-rule/skill/ADR promotion workflow that the note can qualify with its stronger cost and authority gates.

## Reverse-edge Candidates

- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) → source -- **evidenced-by**: add the snapshot as point-in-time practitioner corroboration, explicitly not as behavioral-effect evidence.
- [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) → source -- **evidenced-by**: use the article's human-reviewed local-memory promotion example as an instance and retain the note's maintenance-cost and authority caveats.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- rejected as an outbound connection because the source provides no evidence about activation; it is instead the principal limitation on the article's assumption that discoverable files shape behavior.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) -- rejected as direct evidence because the source's review step is too underspecified to establish verification or bounded abstraction; it remains useful interpretive context for the ingest.
- [System-definition artifact](../../../../notes/definitions/system-definition-artifact.md) -- rejected as `defined-in`: “metacode” is the source author's loose umbrella, not a local term whose definition the source reader needs. The definition instead exposes why file extension and repository placement do not establish behavior-shaping force.
- [A functioning knowledge base needs a workshop layer, not just a library](../../../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) -- rejected as a connection because it primarily marks a disagreement in classification: reviewed planning files can still be work-in-flight with a consumed-value lifecycle rather than durable knowledge.
- [Commonplace control-plane goals](../../../../reference/control-plane-goals.md) -- rejected as too implementation-specific; the note-level control-plane and always-loaded-context artifacts give the source reader the general mechanism.
- [Synapptic](../../../../agent-memory-systems/reviews/synapptic.md) -- rejected because the article does not study this system; the compiled-view note already provides the useful route to the concrete implementation.

## Index Membership

None

## Synthesis Opportunities

None. The apparent synthesis—filename families do not determine behavioral authority, lifecycle, or activation—is already covered by the artifact-analysis definitions, workshop distinction, and activation note.

## Maintenance Observations

None

## Flags

- Evidence boundary: the source catalogs formats and recommends placement, but it does not measure discovery, compliance, maintenance quality, or behavior change. Any reverse edge should identify it as practitioner corroboration, not outcome evidence.
- Vocabulary boundary: “metacode” is convenient retrieval vocabulary but collapses natural-language knowledge artifacts, system-definition artifacts, work-in-flight plans, local memory, and versioned specifications into one repository-level category.
