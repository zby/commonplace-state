---
description: "Discovery inputs for ingesting Flywheel hooks: event admission, durable automation, recovery, and observable effect boundaries."
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/flywheel-hooks-and-automations.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: Flywheel — Hooks And Automations

**Source:** [Flywheel — Hooks And Automations](../../../../sources/.snapshots/flywheel-hooks-and-automations.md)

Discovery-only output produced with `cp-skill-connect` by GPT-6 Codex. Recommendations belong in the eventual matching ingest, never in the immutable snapshot. This is product documentation captured with `capture_scope: partial-source`, not implementation or outcome evidence.

## Discovery Trace

**Scope and authorization:** Read the source fully, `kb/sources/COLLECTION.md`, `kb/reports/COLLECTION.md`, and the connect-report type. Prospected notes, reference, agent-memory-systems, agentic-systems, and sources. Instructions and work are excluded. The source has no tags, so there was no source-tag sweep. External discovery was skipped; the source URL already in hand is eligible for `derived-from`.

**Curated heads:** Read each destination's `README.md`, plus `kb/notes/tags-README.md`, `kb/notes/observability-README.md`, and `kb/notes/tool-loop-README.md`. The observability head supplied the outcome/path distinction. The agentic head supplied GBrain; full-title and body discovery additionally found Swamp. The memory head supplied Semiont's event/projection distinction. No complete-tag mark was used to suppress discovery.

**Full titles and descriptions:** Ran `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. Recovered its initially truncated output into an in-memory listing and read all 1,200 title lines in chunks. Ran `rg '^description:' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md' | rg -i 'hook|event|durable|retry|execution|lifecycle|permission|workflow|authority'`. Broad description output was truncated; candidate-specific reads below supplied the decision evidence. No scores apply to lexical discovery.

**Body search and per-destination decisions:**

- Shared recall query: `rg -l -i 'hook|deduplic|submission|lifecycle|retry' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. The large match set was a locator pass, not evidence that every match was relevant.
- Notes: fully read methodology enforcement, structured recovery, and final-task-success notes. Retained enforcement for separating runtime activation from response, recovery for terminal versus retryable failures, and outcome/path health as a comparison rather than a claim that Flywheel implements semantic fallback. Read cross-task-transition policy and rejected a scheduler inference from multi-step hooks alone.
- Reference: read review architecture; searched `rg -n -m2 'accept|complete|retry|terminal|finaliz' kb/reference/review-architecture.md kb/reference/freshness-architecture.md kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md kb/notes/methodology-enforcement-is-constraining.md`. Retained review architecture for its contrasting finalization boundary: Commonplace withholds completion when evidence persistence fails, whereas a later Flywheel hook failure does not roll back the original artifact.
- Agentic systems: searched `rg -n 'hook|idempot|retry|lifecycle|forwarded|Flywheel' kb/agentic-systems/reviews/ kb/agent-memory-systems/reviews/gbrain.md kb/agent-memory-systems/reviews/semiont.md kb/reference/review-architecture.md kb/sources/verified-tool-calls-improve-llm-agent-reliability.ingest.md --glob '*.md'`. Read Swamp's workflow, policy, audit, and secret sections and the full GBrain whole-system review. Kept Swamp as the closest declarative automation comparison and GBrain for durable execution journals and constrained replay.
- Agent-memory systems: inspected Semiont's event authority and derived projections, and GBrain's memory-side queued extraction. Neither adds enough beyond the whole-system runtime comparisons for this particular source; no outbound memory-review candidate retained.
- Sources: read the Verified Tool Calls ingest. Kept it because it distinguishes enqueue deduplication from verification/idempotency of external effects under retries. Other broad harness and memory sources were not retained merely for mentioning hooks.

**Link following:** Followed the observability head to final-task-success, then its recovery link; followed recovery to methodology enforcement; followed Verified Tool Calls to GBrain; followed review architecture to ADR 043. Read `kb/notes/COLLECTION.md` before proposing the reverse evidence edge. These paths supplied narrower candidates than generic automation or memory similarity.

## Connections Found

- [Original hook documentation](https://docs.flywheel.paradigma.inc/concepts/hooks) — **derived-from**: the future ingest analyzes the captured documentation from this URL; the current page was not fetched during discovery.
- [Methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md) — **is-evidence-for**: Flywheel separately declares event/scope matching, deterministic filters, and executable response steps, giving a documented case in which hook packaging does not itself specify one response or enforcement strength.
- [Enforcement without structured recovery is incomplete](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md) — **compares-with**: Flywheel classifies missing secrets and ambiguous selectors as terminal while network and selected HTTP failures may retry; this makes a concrete recovery boundary available for comparison with the note's corrective/fallback/escalation vocabulary. The snapshot does not document the complete retry policy.
- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) — **compares-with**: source-artifact persistence and automation success are separate observable facts in Flywheel. Durable attempts and step errors help inspect the latter, but the source does not establish the note's particular semantic-fallback mechanism.
- [Swamp](../../../../agentic-systems/reviews/swamp.md) — **compares-with**: both use declarative automation with runtime-owned execution, durable run inspection, and scoped secret handling. Swamp's code-grounded DAG/approval/remote-worker account is broader than Flywheel's documented event-hook surface; the comparison should preserve that evidence asymmetry.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) — **compares-with**: GBrain journals tool executions and replays pending idempotent tools, while Flywheel specifies at-most-one run per hook/event and changed-input reruns. These are different replay and duplication boundaries, useful to an operator designing reliable KB automation.
- [Verified Tool Calls](../../../../sources/verified-tool-calls-improve-llm-agent-reliability.ingest.md) — **compares-with**: its post-dispatch verification and idempotency address duplicate external effects, which Flywheel's hook/event cardinality and input-change policy alone do not establish. This prevents interpreting run deduplication as exactly-once HTTP effects.
- [Review system architecture](../../../../reference/review-architecture.md) — **see-also**: inspect Commonplace's explicit evidence-write/completion transaction when comparing it with Flywheel's independent artifact-commit and asynchronous automation boundaries.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md) → future tracked ingest — **evidenced-by**: a bounded product-documentation example can illustrate independently configured activation and response. Read the notes contract: this label is authorized to sources. The writer must wait for the tracked ingest, retain the needed quote or mark snapshot-required grounding, and not cite this ignored snapshot as durable authority.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Cross-task transition policy remains scheduling behind tools](../../../../notes/cross-task-transition-policy-remains-scheduling-behind-tools.md) — hooks contain several steps, but the capture does not establish independently steerable goals or a supervising controller's interceptable transitions. A scheduler classification would exceed the evidence.
- [Semiont](../../../../agent-memory-systems/reviews/semiont.md) — canonical event replay into graph/vector projections is not the same mechanism as an artifact-triggered external workflow; the event vocabulary alone does not justify another edge here.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Partial capture: several passages announce YAML examples but contain no corresponding code block. Do not reconstruct configuration syntax from surrounding prose.
- Run cardinality, rerun suppression, execution retries, and external side-effect idempotency are separate guarantees. The snapshot specifies the first two and sketches the third; it does not establish the fourth.
- Organizer-owned hooks can process participant submissions without changing attempt ownership. That documents an authority boundary; it is not evidence of resistance to hostile payloads or privilege escalation.
- The companion campaigns capture clarifies submission validity and lifecycle state. Cross-link matching tracked ingests only once they exist; neither immutable capture should be edited.
