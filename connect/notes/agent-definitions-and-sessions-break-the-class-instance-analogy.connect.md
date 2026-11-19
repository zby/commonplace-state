---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/agent-definitions-and-sessions-break-the-class-instance-analogy.md"
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: Instantiation alone cannot model agent learning across sessions

**Source:** [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md)

## Discovery Trace

**Description listing scan:**

- Generated the complete `# ` title surface with `rg -N --no-heading -m1 '^# '` for each authorised local destination: `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/sources/`, and `kb/instructions/`. Candidate filtering emphasized sessions, retention, learning, promotion, reflection, context, state, artifacts, and adaptation.
- Ran `rg '^description:' <destination> --glob '*.md'` for all five destinations, filtered with `session|write|retention|placement|promotion|reflect|adapt|learning|context|state`. This surfaced the deployment-time-learning cluster, Commonplace's reflective-system case, Meta-Harness, and several memory-system promotion cases.
- The source tags are `computational-model`, `deploy-time-learning`, and `learning-theory`. Read `computational-model-README.md`, `deploy-time-learning-README.md`, and `learning-theory-README.md`. The learning-theory head declares `covered_by`, not `complete`, so it justified child-tag routing but did not license skipping other searches. None of the three tag heads declares `complete: true`; no by-tag search was skipped on a completeness mark.

**Topic indexes:**

- Read `kb/notes/README.md` and the three matching tag heads. The deploy-time-learning head identified retained system-definition artifacts, governance, and context engineering as the closest conceptual cluster.
- Read `kb/reference/README.md`. Its Commonplace worked-case cluster surfaced `commonplace-as-a-reflective-system.md` as an observed definition-to-later-operation pathway.
- Read `kb/agent-memory-systems/README.md`. Its trace-learning and runtime-self-modification sections surfaced Meta-Harness and Nuggets as contrasting implementation cases.
- Read `kb/sources/README.md`; the already-authored Machine Studying ingest remained the strongest source connection. No additional source passed the incremental-value test.
- Read `kb/instructions/README.md` and the outbound-link posture in `kb/instructions/COLLECTION.md`. Instruction links to theory are exceptional and frontloaded. No procedure gained enough from a reverse `rests-on` edge to justify one.

**Body search:**

- `rg -n -i "class.instance|instantiat|cross-session|write-back|writeback|durable definition|session state|content placement|promotion|warm-up|warmup|changed agent|reflecti" kb/notes kb/reference kb/agent-memory-systems kb/sources kb/instructions --glob '*.md'` -- broad recall pass; retained the deployment-time-learning framework, governance note, explicit-retention comparison, Commonplace case, Meta-Harness, and Nuggets for full evaluation.
- `rg -l -i "cross-session|session-local|write-back|writeback|content placement|durable definition|changed agent|class.instance|instantiation" ...` -- narrowed the exact-language neighborhood. It confirmed that orchestration/run-state and ephemeral-computation notes were already linked from the source, and that most system-review hits concerned state continuity rather than selected definition revision.
- `rg -n "agent-definitions-and-sessions-break-the-class-instance-analogy" ...` -- found no existing inbound links, so every reverse-edge suggestion would need independent reader value rather than backlink repair.
- `rg -n -i "promotion|session|persistent|trace|harness|write" kb/agent-memory-systems/reviews/meta-harness.md kb/agent-memory-systems/reviews/nuggets.md kb/agent-memory-systems/reviews/OpenSage.md` -- distinguished evaluation-gated harness revision from frequency-gated memory promotion and runtime tool creation.

**Link following:**

- Followed the source's links to `a-proposal-selection-loop-requires-search-evaluation-and-retention.md`, `frontloading-spares-execution-context.md`, `ephemeral-computation-prevents-accumulation.md`, `promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md`, `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`, and `orchestration-strategies-and-run-state-have-opposite-persistence.md`. These explain why the four proposed note edges add distinct premises or comparisons rather than duplicating existing links.
- Followed the retained-artifacts note to the continual-learning governance and explicit-retention notes. The neighborhood separates persistence, selection, placement, and addressability, matching the source's four main distinctions.
- Followed the reflective-system candidate into its causal trace and proposal-selection reading. The case shows operation revising retained self-representation and the revision changing later behavior, directly instantiating the source's second relation.
- Followed the agent-memory index into Meta-Harness and Nuggets. Meta-Harness was kept as an evaluated transformation of harness definitions; Nuggets was rejected as a useful contrast whose frequency-only promotion would broaden the source beyond its present argument.

## Connections Found

- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **grounds**: supplies the broader framework in which an evaluated artifact change survives one run and changes later sessions, grounding the source's second definition-to-definition relation.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **grounds**: establishes that persistence alone is insufficient and that selection, validation, authority, and revisable form placement govern cross-session learning.
- [In-context learning presupposes context engineering](../../../../notes/in-context-learning-presupposes-context-engineering.md) -- **grounds**: explains why the boundary among always-loaded, retrieved, and locally assembled content is an adaptive system policy rather than a fixed property of session instantiation.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) -- **extends**: develops the source's durable-definition/session distinction into a comparison of retention forms and explains why explicit artifacts support selective cross-session revision.
- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) -- **evidenced-by**: traces a concrete case where operational strain changes retained system organization and the revised organization changes later agent and validator behavior.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) -- **evidenced-by**: provides a code-grounded case in which run evidence drives evaluation-gated revisions to persistent harness code, making later agent instances inherit a selected changed definition.

## Bidirectional Candidates

- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) <-> source -- **extends**: the reverse path would help framework readers reach the source's more precise two-relation model and its account of revisable content placement.
- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) <-> source -- **see-also**: case readers would gain a compact conceptual distinction between session startup and governed transformation of the durable organization; this is useful independently of the outbound evidence edge.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- rejected because its cross-session accumulation claim is downstream of the retained-artifacts framework and would duplicate that stronger, closer connection.
- [LLM recompute cost inverts the store-vs-recompute default](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) -- rejected because it explains one cost pressure behind storing derived values, not the governed cross-session transformation or general content-placement policy.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) -- rejected because the source already links the reflective-system definition and carefully limits reflection's role; adding the addressability thesis would introduce a neighboring comparison not needed to follow the present argument.
- [Nuggets](../../../../agent-memory-systems/reviews/nuggets.md) -- rejected because its hit-count promotion is a vivid weak-governance contrast, but the source does not analyze promotion-oracle quality deeply enough for the case to corroborate its main claim without a new argumentative passage.
- [OpenSage](../../../../agent-memory-systems/reviews/OpenSage.md) -- rejected because runtime subagent/tool creation demonstrates mutable topology, but its lack of quality gates makes it a self-modification example rather than a selected-learning instance.
- [Machine Studying](../../../../sources/machine-studying.ingest.md) -- rejected as a new candidate because the source already authors the `evidenced-by` edge and uses the changed-agent formulation directly.
- [Revise a note with AutoReason](../../../../instructions/cp-skill-revise-autoreason/SKILL.md) -- rejected because its candidate tournament is a procedure for revising one retained artifact, but the instruction is frontloaded and does not need this theory note to execute.

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) -- the source sharpens the tag's cross-session framework by separating instantiation from selected revision of the durable definition.
- [computational-model](../../../../tags/computational-model-README.md) -- the source contributes a disciplined limit on the class/instance analogy and an alternative two-relation computational model.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
