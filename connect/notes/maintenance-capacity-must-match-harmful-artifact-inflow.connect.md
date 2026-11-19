---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/maintenance-capacity-must-match-harmful-artifact-inflow.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Maintenance capacity must match harmful-artifact inflow

**Source:** [Maintenance capacity must match harmful-artifact inflow](../../../../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md)

## Discovery Trace

**Topic indexes:**
- Read [kb/notes/kb-maintenance-README.md](../../../../tags/kb-maintenance-README.md) as the source tag head. It does not declare `complete: true`, so I did not treat it as exhaustive beyond its authored grouping.
- Read [kb/notes/README.md](../../../../notes/README.md) titles/descriptions surface indirectly through the required listing queries.
- Read adjacent curated heads surfaced by the title/description scan: [kb/notes/observability-README.md](../../../../tags/observability-README.md) and [kb/reference/README.md](../../../../reference/README.md). No instruction, agent-memory-system, or agentic-system README produced a stronger maintenance-capacity candidate than the note and source surfaces below.

**Description listing scan:**
- `rg '^description:' kb/notes/ --glob '*.md'` flagged [notes-need-quality-scores-to-scale-curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md), [quality-signals-for-kb-evaluation](../../../../notes/quality-signals-for-kb-evaluation.md), [stale-self-description-conceals-its-own-staleness](../../../../notes/stale-self-description-conceals-its-own-staleness.md), [link-graph-plus-timestamps-enables-make-like-staleness-detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md), [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in](../../../../notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md), and [raw-accumulation-does-not-create-usable-memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md).
- `rg '^description:' kb/reference/ kb/instructions/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'` flagged [where-change-candidates-come-from-in-commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md), [commonplace-agent-memory-gap-plan](../../../../reference/commonplace-agent-memory-gap-plan.md), [harness-engineering-leveraging-codex-agent-first-world.ingest](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md), and [what-spec-driven-development-gets-wrong.ingest](../../../../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md).

**Title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` confirmed nearby claim titles with stronger maintenance dynamics than generic “staleness” notes: [Spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md), [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md), and [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md).

**Body search:**
- `rg -n "harmful|backlog|queue|cleanup|maintenance capacity|inflow|slop|stale|staleness|quality drift|repair queue|detection latency|quarant|exposure" kb/notes/ --glob '*.md'`
  - Kept [stale-self-description-conceals-its-own-staleness](../../../../notes/stale-self-description-conceals-its-own-staleness.md): names reflexive drift as harmful inflow even without high new-artifact volume.
  - Kept [spec-mining-as-codification](../../../../notes/spec-mining-as-codification.md): turns observed cleanup burden into codified prevention/detection capacity.
  - Rejected [many-to-many-edge-state-is-where-files-yield-to-a-database](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md): shares “queue/staleness” vocabulary, but its claim is about storage-substrate boundaries rather than maintenance-capacity allocation.
  - Rejected [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in](../../../../notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md): about trigger placement, not the scaling invariant itself.
- `rg -n "entropy-management-must-scale-with-generation-throughput|Maintenance capacity must match harmful-artifact inflow|harmful-artifact inflow|maintenance capacity|risk-weighted inflow" kb/notes/ kb/reference/ kb/instructions/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`
  - Found existing inbound uses in [false-positive-generation-is-filtered-before-retention](../../../../notes/false-positive-generation-is-filtered-before-retention.md), [weakly-discriminated-qualities-tend-to-be-underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md), and both source ingests above.
- `rg -n "cleanup throughput must match generation throughput|cleanup throughput|maintenance throughput|background cleanup agents|AI slop cleanup|Friday cleanup|repair queue|harmful retained" kb/notes/ kb/reference/ kb/instructions/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`
  - Kept [harness-engineering-leveraging-codex-agent-first-world.ingest](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md): authored local surface for the main evidence already cited only by URL in the note body.
  - Kept [what-spec-driven-development-gets-wrong.ingest](../../../../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md): second architecture for throughput matching, with maintenance folded into generation rather than run as a parallel cleanup stream.

**Link following:**
- Followed the source note’s existing outbound links to [notes-need-quality-scores-to-scale-curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md), [stale-self-description-conceals-its-own-staleness](../../../../notes/stale-self-description-conceals-its-own-staleness.md), and [where-change-candidates-come-from-in-commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md). The first two are load-bearing and kept. The reference note already appears in the source and did not open a denser reference cluster than the note already captures.
- Followed [what-spec-driven-development-gets-wrong.ingest](../../../../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md), which explicitly recommends updating the source note with the bidirectional-spec pattern; kept as a strong source candidate.
- Followed existing inbound links from [false-positive-generation-is-filtered-before-retention](../../../../notes/false-positive-generation-is-filtered-before-retention.md) and [weakly-discriminated-qualities-tend-to-be-underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md). Both already link to the source, so they are not reverse-edge candidates.

## Connections Found

- [notes-need-quality-scores-to-scale-curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md) -- **extends**: bounded maintenance capacity needs a way to spend attention on the highest-risk inflow first, and this note supplies one concrete allocation mechanism through risk-sensitive candidate ranking.
- [stale-self-description-conceals-its-own-staleness](../../../../notes/stale-self-description-conceals-its-own-staleness.md) -- **extends**: it identifies one high-cost harmful-inflow mechanism the source only gestures at, namely reflexive drift that keeps generating maintenance load even when gross artifact generation is low.
- [spec-mining-as-codification](../../../../notes/spec-mining-as-codification.md) -- **mechanism**: this note explains how recurring cleanup burden can be converted into prevention and detection capacity by mining repeated failures into tests, rules, and automated monitors.
- [harness-engineering-leveraging-codex-agent-first-world.ingest](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) -- **evidenced-by**: this is the local authored ingest for the main practitioner case already cited in the note body, preserving the Friday-cleanup-to-background-agents evidence on a KB-native surface.
- [what-spec-driven-development-gets-wrong-2025993446633492725.ingest](../../../../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) -- **evidenced-by**: it contributes a second, structurally different throughput-matching witness where maintenance scales by making spec upkeep a side effect of generation instead of a separate cleanup process.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [quality-signals-for-kb-evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) → source -- **extends**: its prioritization signals answer where scarce maintenance effort should go, and the source supplies the queue-stability reason that such prioritization matters at all.
- [commonplace-agent-memory-gap-plan](../../../../reference/commonplace-agent-memory-gap-plan.md) → source -- **rests-on**: the plan’s ranking, lifecycle, and candidate-queue steps assume that maintenance capacity is bounded and must be allocated against harmful inflow rather than raw accumulation.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [many-to-many-edge-state-is-where-files-yield-to-a-database](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) -- rejected because it explains when churning edge-state earns a database, not how maintenance capacity must scale with harmful retained artifacts.
- [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in](../../../../notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) -- rejected because it governs when maintenance runs, not the throughput or risk-weighting invariant that determines whether maintenance is sufficient.
- [raw-accumulation-does-not-create-usable-memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -- rejected because it is about ingress requirements for usable memory in general; it shares lifecycle vocabulary but does not sharpen this note’s queue-stability claim.
- [link-graph-plus-timestamps-enables-make-like-staleness-detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) -- rejected as a direct connection because the source already cites it in the KB-implications section and its role there is already appropriately captured.

## Index Membership

None

## Synthesis Opportunities

- [spec-mining-as-codification](../../../../notes/spec-mining-as-codification.md) + [what-spec-driven-development-gets-wrong-2025993446633492725.ingest](../../../../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) + source imply a higher-order design-space note: throughput matching has at least two distinct architectures, parallel cleanup capacity and maintenance-as-a-side-effect of generation, with different failure modes and review burdens.

## Maintenance Observations

- The source note cites the OpenAI article by external URL in prose, while the repo now has a local authored ingest at [harness-engineering-leveraging-codex-agent-first-world.ingest](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md). Future maintenance may prefer the local source surface for lineage and snapshot stability.

## Flags

- The source already belongs in [kb-maintenance-README](../../../../tags/kb-maintenance-README.md), so there is no missing-index action from this run.
