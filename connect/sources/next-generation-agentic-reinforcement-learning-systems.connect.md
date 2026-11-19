---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/next-generation-agentic-reinforcement-learning-systems.md"
source_has_frontmatter: true
date: "2026-08-06"
depth: standard
---

# Connect: Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents

**Source:** [Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents](../../../sources/next-generation-agentic-reinforcement-learning-systems.md)

## Discovery Trace

**Collection rules and source reading:**

- Read `kb/sources/COLLECTION.md`; authorised local destinations are notes, reference, agent-memory-systems, agentic-systems, and sources. Snapshots are immutable, so accepted outbound candidates belong on the adjacent ingest report and useful inbound edges belong here as reverse candidates.
- Read the full 13-page snapshot. The source is a position/design preprint with a scoped AReaL2.0 implementation of only the policy-weight branch. It reports no benchmark comparison, intervention study, or empirical outcome for the proposed multi-surface control plane.

**Curated heads and complete title/description surfaces:**

- Read `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source has no `tags:` field, so no tag-README routing or complete-tag skip applied.
- Generated fresh full-title listings with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: 335 note titles, 127 reference titles, 172 agent-memory titles, 11 agentic-system titles, and 439 source titles.
- Generated fresh description listings with `rg '^description:' kb/<destination>/ --glob '*.md'`: 332 note descriptions, 125 reference descriptions, 170 agent-memory descriptions, 9 agentic-system descriptions, and 379 source descriptions.

**Body search:**

- `rg -n -i 'trajectory (data|protocol)|credit.assign|replay|rollback|intervention surface|update space|self-evolv|self-improv|control plane|memory insertion|skill patch|harness edit|model weights' kb/notes/ --glob '*.md'` surfaced the decision-surface capture, fixed-decomposition, artifact-analysis, deploy-time-learning, representational-form coevolution, trace-authority, and proposal-selection clusters. Kept the capture, decomposition, and coevolution candidates because they constrain the paper's architecture directly; rejected broad self-improvement vocabulary matches that did not sharpen a design choice.
- `rg -l -i 'decision surface|credit.assign|trajectory|replay' kb/notes/ --glob '*.md'` and `rg -l -i 'representational.form coevolution|cross.form credit|intervention surface|multi.surface' kb/notes/ --glob '*.md'` confirmed [decision-surface capture](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) and [representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) as the strongest theoretical targets.
- `rg -l -i 'trajectory.*(provenance|govern)|replay.*rollback|control plane' kb/reference/ --glob '*.md'` returned Commonplace-specific review, freshness, and agent-memory plans. Rejected them because the paper does not describe the shipped Commonplace system, and `see-also` would add only topical adjacency.
- `rg -l -i 'self-evolv|trajectory.*(memory|skill|weight)|model weights.*harness|control plane' kb/agent-memory-systems/ --glob '*.md'` surfaced the trace-learning survey plus many individual reviews. Kept the survey because it provides the code-grounded comparison surface for the paper's proposed service substrate; rejected individual memory systems as redundant at this source's architectural level.
- `rg -l -i 'self-evolv|trajectory|replay|rollback|control plane' kb/agentic-systems/ --glob '*.md'` surfaced Exo, Autogenesis, Agno AgentOS, Swamp, and others. Kept [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) because it is the closest code-grounded multi-resource evolution-and-rollback counterpart. Rejected AgentOS and Swamp because their control planes operate execution and automation rather than selecting learning interventions.
- `rg -l -i 'self-evolv|trajectory.*(memory|skill|weight)|model weights.*harness|control plane|data proxy' kb/sources/ --glob '*.ingest.md'` surfaced the adaptation survey, Co-Harness, The What & When of Self-Evolving Agents, Why AI Systems Don't Learn, harness-engineering surveys, and trace-learning papers. Kept Co-Harness and the two closest architectural taxonomies; rejected broader survey duplicates.

**Link following:**

- Followed [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) to [Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md), [deploy-time learning](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), and [axes of artifact analysis](../../../../notes/axes-of-artifact-analysis.md). Co-Harness is the strongest concrete complement because it actually alternates harness and weight updates, while the requested paper only sketches selection among surfaces and implements weight updating.
- Followed [Bottom-up structure inference needs capture at the decision surface](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) to [preserve evidence without making history the next context](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) and [trace-extracted memory earns authority per operation](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md). The paper's ATDP supplies a candidate event schema for the first requirement but does not solve the second.
- Followed [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) to its fixed-decomposition and proposal-selection analyses. Its versioned resource substrate and rollback are implemented; its semantic evaluation remains weak, which is the closest concrete test of the paper's proposed governed control plane.
- Read the relevant trace-learning survey sections for recurring stages, promotion targets, Autocontext, Meta-Harness, Agentic Harness Engineering, OpenClaw-RL, SkillRL, and the cross-system comparison. The survey already distinguishes readable-artifact and weight promotion; the requested paper adds a proposed enterprise data/control substrate rather than a new inspected system.

## Connections Found

- [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) -- **rests-on**: the proposed ATDP can support credit assignment and intervention selection only because it captures observation, relevant state, action, outcome, reward, and execution metadata at the decision surface instead of preserving endpoint state alone.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **compares-with**: the note names cross-form credit assignment as the open problem; this source proposes a trajectory-driven controller that chooses among memory, skills, harnesses, tools, and policy weights, but implements only the weight-update branch.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: the paper fixes the ATDP event tuple, intervention menu, failure-to-surface mapping, replay categories, and governance envelope outside the proposed learner, so successful optimization within one branch would not validate that decomposition.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **compares-with**: the code-grounded survey shows many concrete trace-ingestion and promotion paths; the source proposes the shared enterprise protocol, data proxy, and controller those heterogeneous systems currently lack.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- **compares-with**: Autogenesis provides a concrete, versioned multi-resource mutation and rollback substrate, while the source proposes a broader intervention selector and replay-first governance that its AReaL2.0 prototype does not implement.
- [Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) -- **compares-with**: Co-Harness is an empirical alternating harness-and-weight loop; the source instead proposes the service substrate and decision layer that would choose such an update path from deployed trajectories.
- [The What & When of Self-Evolving Agents](../../../../sources/the-what-and-when-of-self-evolving-agents.ingest.md) -- **compares-with**: its substrate-by-horizon matrix classifies where updates land and persist, while this source adds the capture, governance, and automatic-trigger architecture needed to select among those cells.
- [Why AI systems don't learn and what to do about it](../../../../sources/why-ai-systems-dont-learn-and-what-to-do-about-it.ingest.md) -- **compares-with**: both are position papers that make meta-control the missing systems layer; this source replaces the A/B/M cognitive architecture with an enterprise trajectory protocol, data proxy, multi-surface action set, and scoped weight-update prototype.

## Bidirectional Candidates

- [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) <-> source -- **evidenced-by** from the note side: ATDP independently proposes decision-shaped, versioned event capture for credit assignment, but should be cited as a design proposal rather than validation.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) <-> source -- **evidenced-by** from the note side: the proposed controller makes cross-form intervention selection explicit and AReaL2.0 implements one scoped policy-weight path, while leaving the full coevolution loop unbuilt.

## Reverse-edge Candidates

- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -> source -- **evidenced-by**: add the paper as lower-authority architecture-level evidence for a vendor-neutral event protocol and enterprise data/control substrate, clearly separated from the survey's code-inspected systems.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Commonplace agent-memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) -- rejected: shared words such as trajectory, lifecycle, and control plane do not make an external enterprise-RL design a useful target for shipped-system documentation; only weak `see-also` adjacency was available.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) -- rejected: it is an execution and component-management control plane, not a controller that chooses learning substrates from trajectory evidence.
- [Externalization in LLM Agents](../../../../sources/externalization-in-llm-agents-unified-review.ingest.md) -- rejected: its broad memory/skills/protocols/harness map overlaps, but The What & When and Co-Harness give sharper classification and implementation comparisons.
- [Harness Engineering for Self-Improvement](../../../../sources/harness-engineering-for-self-improvement.ingest.md) -- rejected: it is an orientation synthesis whose fixed-decomposition analysis is already represented by the direct theoretical connection and the more specific Co-Harness comparison.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) -- rejected as a direct edge: the source proposes provenance, replay, redaction, and deployment gates, but it does not establish the verification and abstraction oracles needed for captured traces to gain epistemic authority.

## Index Membership

None

## Synthesis Opportunities

- [Bottom-up structure inference needs capture at the decision surface](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md), [representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md), and the source jointly imply a missing claim: **multi-surface learning needs a typed, replayable evidence substrate before an intervention controller can assign a failure to memory, skill, harness, tool, or weights**. The source supplies a concrete ATDP/data-proxy witness; the KB supplies the capture and fixed-decomposition limits.

## Maintenance Observations

None

## Flags

- The source is published as a scientific preprint but is primarily a position/design paper. Its only implementation, AReaL2.0, covers policy-weight updates; it does not implement ATDP completely, multi-surface intervention selection, governed replay, or the claimed full self-evolving substrate.
- Fixed-decomposition lens: available signals are ATDP observations, internal/harness state, actions, outcomes, delayed rewards/critiques, metadata, and trajectory statistics; available responses are the fixed action menu of memory, skill, harness, tool-schema, policy update, rollback, or no-op; the controller's hypothesis class maps trajectory windows to that menu. The event representation, artifact partitions, action taxonomy, replay categories, governance rules, and controller objective remain fixed outside the effective update space.
