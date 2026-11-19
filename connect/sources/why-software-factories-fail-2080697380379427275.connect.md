---
description: "Discovery report for possible KB connections from Why Software Factories Fail"
type: kb/cache/types/connect-report.md
source: "kb/sources/why-software-factories-fail-2080697380379427275.md"
source_has_frontmatter: true
date: "2026-07-26"
depth: standard
---

# Connection Report: Why Software Factories Fail

**Source:** [Why Software Factories Fail](../../../sources/why-software-factories-fail-2080697380379427275.md)

## Discovery Trace

**Description listing scan:**
- Read the curated heads for notes, reference, agent-memory systems, and agentic systems, then generated the full `# ` title surface with `rg -N --no-heading -m1 '^# ' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`.
- Scoped description searches used `rg '^description:.*(oracle|verification|quality|throughput|oversight|review|frontload|benchmark|maintain)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md' -i`. The strongest candidates were the verification boundary, generation-throughput entropy, outcome-versus-process verification, autonomy-frontier, and inspectability notes. Reference results described Commonplace's own review machinery rather than the post's general claim and were rejected. No agent-memory-system or agentic-system review passed the articulation test.

**Topic indexes:**
- Read `kb/notes/evaluation-README.md`, `kb/notes/observability-README.md`, `kb/notes/context-engineering-README.md`, and `kb/notes/tool-loop-README.md`. Evaluation and observability supplied the oracle and hidden-quality-drift cluster. Context engineering and tool-loop candidates were rejected because the post uses "front-loading" for team alignment and "loops" for production automation, not the KB's bounded-context mechanisms.

**Body search:**
- `rg -n -i 'maintainab|software factor|code quality|code review|technical debt|harness engineering|benchmark|verifier|oracle|human review|oversight|entropy|generation throughput|front-load' ...` surfaced the core note cluster and the existing Harness Engineering source.
- `rg -n -i 'lights.off|software factory|codebase quality|maintainability|shotgun surgery|slop|frontier code|SWE.Marathon|DeepSWE' kb --glob '*.md'` confirmed that no existing artifact covers this post and that the most direct comparison is the Codex Harness Engineering snapshot.

**Link following:**
- Followed the verification-boundary note to warranted autonomy and the augmentation/automation discrimination note. These sharpen the lights-off-factory failure into the absence of an adequate per-change maintainability oracle.
- Followed the entropy-throughput note to spec mining and Harness Engineering. The post corroborates degradation under high generation volume but disputes that automated cleanup and harness work necessarily reach maintainability failures.
- Followed the process-verification note to diagnostic richness. The post's critique is specifically that pass/fail task outcomes omit the long-horizon process property that matters.
- Followed the autonomy-frontier note to Bainbridge and warranted autonomy. The review bottleneck is a concrete relocation of human work to the verification frontier.
- Followed the inspectability note to its Harness Engineering evidence. The post agrees that code remains inspectable but contests the note's stronger inference that agent inspection can replace human steering when the evaluator shares the model's quality ceiling.

## Connections Found

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **evidence**: maintainability costs arrive months after a patch, so no fast reliable oracle currently supports lights-off automation of long-lived codebases.
- [Maintenance capacity must match harmful-artifact inflow](../../../../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) -- **evidence**: the author's lights-off case reports risk-weighted maintainability failures outrunning prevention, detection, and repair capacity; it also limits the note's automated-cleanup remedy by arguing that current checks miss delayed design harm.
- [An outcome check licenses replay; a rule needs the process verified](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -- **evidence**: SWE-bench-style pass/fail scoring verifies that one patch works but not that its design process preserves maintainability across later changes.
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) -- **evidence**: faster agent generation moves the bottleneck to review and design judgment rather than eliminating human work.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) -- **evidence**: the post agrees that generated code must remain readable and inspectable, but supplies a counterexample to the claim that agent-only review suffices when model judges lack a reliable maintainability oracle.
- [Harness Engineering: Leveraging Codex in an Agent-First World](../../../sources/harness-engineering-leveraging-codex-agent-first-world.md) -- **compares-with**: both discuss high-throughput agentic software factories, but Harness Engineering reports automated cleanup and repository constraints as a successful response while this post argues those measures raise the floor without solving the maintainability ceiling.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source -- **evidence**: this post supplies a software-maintainability case where delayed costs make verification too expensive for warranted automation.
- [Maintenance capacity must match harmful-artifact inflow](../../../../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) → source -- **evidence**: the failed lights-off experiment corroborates degradation when harmful retained changes outrun adequate maintenance, while qualifying automated cleanup as incomplete.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) → source -- **evidence**: the post is a useful adverse case for whether inspectability plus model review can replace human supervision in long-lived codebases.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md) -- rejected as a vocabulary collision: the post means aligning a human team before implementation, not partial evaluation into an LLM context.
- [Tool loop](../../../../tags/tool-loop-README.md) -- rejected because generic overlap around agent loops does not give a reader a specific mechanism or consequence beyond the post itself.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- rejected as duplicative of the more direct automation/verification connection.
- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- rejected as a useful supporting explanation already reachable from the verification-boundary note, not an additional durable edge.
- [Human Bottlenecks](../../../sources/fernando-borretti-human-bottlenecks.md) -- rejected because its human-capital thesis is too broad to clarify the specific maintainability-oracle bottleneck.

## Index Membership

None

## Synthesis Opportunities

The source, the verification-boundary note, and the inspectability note expose a distinction worth testing: artifact inspectability makes review possible, but unattended automation additionally requires an evaluator with discrimination over the delayed quality property at stake. The present source is an adverse practitioner case, not enough by itself to settle that higher-order claim.

## Maintenance Observations

None

## Flags

- Tension: the source challenges the inspectability note's claim that artifact form, rather than reviewer identity, is sufficient to defeat the blackbox problem; both may hold only after separating inspectability from adequate evaluator discrimination.
