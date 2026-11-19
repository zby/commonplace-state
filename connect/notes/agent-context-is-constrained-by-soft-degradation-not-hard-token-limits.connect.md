---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md"
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: Soft degradation often constrains agent work before hard token limits bind

**Source:** [Soft degradation often constrains agent work before hard token limits bind](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md)

## Discovery Trace

**Collection rules loaded:**
- Read [../../../notes/COLLECTION.md](../../../../notes/COLLECTION.md). The outbound rules authorize prospecting local note-adjacent destinations plus `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; `external` is authorized but not a prospecting surface. `kb/work/` is explicitly excluded.
- The collection posture says most useful edges from `kb/notes/` land in `kb/notes/`; note → `instructions` is rare and normally inverse, with direct edges justified only by `operationalized-from`.
- The labels table authorizes `types` only in narrow evidence cases; that destination was scanned, but no type contract looked like evidence-bearing support for this theory note.

**Curated heads:**
- Read [../../../notes/README.md](../../../../notes/README.md), [../../../notes/learning-theory-README.md](../../../../tags/learning-theory-README.md), [../../../notes/foundations-README.md](../../../../tags/foundations-README.md), and [../../../notes/deploy-time-learning-README.md](../../../../tags/deploy-time-learning-README.md). None of the tag READMEs declared `complete: true`, so no by-tag search was skipped.
- Read [../../../sources/README.md](../../../../sources/README.md), [../../../reference/README.md](../../../../reference/README.md), [../../../instructions/README.md](../../../../instructions/README.md), [../../../agent-memory-systems/README.md](../../../../agent-memory-systems/README.md), [../../../agentic-systems/README.md](../../../../agentic-systems/README.md), and [../../../types/README.md](../../../../types/README.md) before destination-specific scans.

**Notes destination:**
- Generated the full title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`. The strongest nearby titles were already encoded in the source itself: `Context efficiency is the central design concern in agent systems`, `Under sub-agent decomposition, feasibility is the heaviest fork's net load`, `LLM context is composed without scoping`, `Bounded-context orchestration model`, `Context contamination operates below an agent's compliance reasoning`, `Indirection is costly in LLM instructions`, `Knowledge storage does not imply contextual activation`, and `Session history should not be the default next context`.
- Scanned descriptions with `rg '^description:' kb/notes/ --glob '*.md'`, plus tag-scoped listings:
  - `rg -l '^tags:.*\blearning-theory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`
  - `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`
  - `rg -l '^tags:.*\bdeploy-time-learning\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`
- Ran focused body search with `rg -n 'soft bound|soft degradation|hard token|context rot|lost in the middle|workspace|interference|session history|bounded context|context contamination|active work state' kb/notes/ --glob '*.md'`.
- Followed candidate neighborhoods by opening [../../../notes/llm-context-is-composed-without-scoping.md](../../../../notes/llm-context-is-composed-without-scoping.md), [../../../notes/bounded-context-orchestration-model.md](../../../../notes/bounded-context-orchestration-model.md), [../../../notes/frontloading-spares-execution-context.md](../../../../notes/frontloading-spares-execution-context.md), [../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md), [../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md), [../../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md](../../../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md), and [../../../notes/context-engineering-README.md](../../../../tags/context-engineering-README.md).
- Kept no new outbound note-edge. The highest-value mechanism, extension, and grounding notes are already encoded in the source body or `Relevant Notes`. Additional hits such as `active-work-state` and `flat-memory` were judged one step downstream of the source's core claim and would dilute traversal rather than sharpen it.
- Retained one index signal: [../../../notes/context-engineering-README.md](../../../../tags/context-engineering-README.md) is an appropriate additional landing because the source's consequence section is explicitly about selective loading, scoped state, decomposition, and session-history control under bounded context.

**Sources destination:**
- Generated the full title surface with `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`.
- Scanned descriptions with `rg '^description:' kb/sources/ --glob '*.md'`.
- Ran focused body searches with:
  - `rg -n 'Paulsen|GSM-DC|Chung et al.|ConvexBench|verbalizable-representations-global-workspace-llms|lost in the middle|context rot' kb/sources kb/agentic-systems kb/agent-memory-systems kb/reference --glob '*.md'`
  - `rg -n 'soft degradation|hard token|context rot|bounded context|interference|workspace|MECW|session history|irrelevant context' kb/sources kb/reference kb/instructions kb/agent-memory-systems kb/agentic-systems kb/types --glob '*.md'`
- Opened [../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md), [../../../sources/llm-webagents-long-context-reasoning-benchmark.ingest.md](../../../../sources/llm-webagents-long-context-reasoning-benchmark.ingest.md), [../../../sources/convexbench-can-llms-recognize-convex-functions.ingest.md](../../../../sources/convexbench-can-llms-recognize-convex-functions.ingest.md), [../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md), [../../../sources/semantic-leakage-lms-gonen.ingest.md](../../../../sources/semantic-leakage-lms-gonen.ingest.md), and [../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md](../../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md).
- Existing local-source links were not repeated as candidates: the source already encodes [../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md), [../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md), [../../../sources/llm-webagents-long-context-reasoning-benchmark.ingest.md](../../../../sources/llm-webagents-long-context-reasoning-benchmark.ingest.md), [../../../sources/convexbench-can-llms-recognize-convex-functions.ingest.md](../../../../sources/convexbench-can-llms-recognize-convex-functions.ingest.md), and [../../../sources/verbalizable-representations-global-workspace-llms.ingest.md](../../../../sources/verbalizable-representations-global-workspace-llms.ingest.md).
- Kept [../../../sources/semantic-leakage-lms-gonen.ingest.md](../../../../sources/semantic-leakage-lms-gonen.ingest.md): it is the strongest missing local source for the relevance/interference dimension because it names and measures semantically linked irrelevant-context steering rather than only synthetic distractor count or agent-level objective loss.
- Rejected [../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md](../../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md): it is a looser architectural analogue about state-tracking data efficiency and only touches `context rot` speculatively, so it offers weaker traversal value than the already-linked benchmark ingests and J-space mechanism note.

**Reference destination:**
- Scanned descriptions with `rg '^description:' kb/reference/ --glob '*.md'`.
- Reused the shared body query `rg -n 'soft degradation|hard token|context rot|bounded context|interference|workspace|MECW|session history|irrelevant context' kb/sources kb/reference kb/instructions kb/agent-memory-systems kb/agentic-systems kb/types --glob '*.md'`.
- Evaluated hits such as `control-plane-goals`, `agent-memory-coverage`, and `navigation`. They describe Commonplace's shipped system or operator surface, not evidence, a tighter mechanism, or a useful contrast for this theory note. No candidate kept.

**Instructions destination:**
- Scanned descriptions with `rg '^description:' kb/instructions/ --glob '*.md'`.
- Reused the shared bounded-context body query above.
- No `operationalized-from` candidate surfaced. The note's consequences recommend design postures and mitigation families, but no instruction in this collection was the specific ordering/defaults/stopping-conditions realization of this note's claim.

**Agent-memory-systems and agentic-systems destinations:**
- Scanned descriptions with `rg '^description:' kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`.
- Reused the shared bounded-context body query above.
- Evaluated obvious instance surfaces such as [../../../agent-memory-systems/reviews/claude-workstream-kit.md](../../../../agent-memory-systems/reviews/claude-workstream-kit.md), [../../../agent-memory-systems/reviews/LLM-WIKI-MCP.md](../../../../agent-memory-systems/reviews/LLM-WIKI-MCP.md), and [../../../agentic-systems/fractal.md](../../../../agentic-systems/reviews/fractal.md). They instantiate active-work/session-history discipline or bounded-call scaffolding, but as system cases they are weaker traversal targets from this note than the already-linked theory notes and empirical ingests. No candidate kept.

**Types destination:**
- Scanned descriptions with `rg '^description:' kb/types/ --glob '*.md'`.
- No candidate kept. The global type contracts are structural and non-evidentiary here.

**External destination:**
- `external` is authorized, but the skill forbids open-web prospecting here. No user-supplied external target beyond the already-loaded citations was available, so external discovery was skipped.

## Connections Found

- [Ingest: Does Liking Yellow Imply Driving a School Bus? Semantic Leakage in Language Models](../../../../sources/semantic-leakage-lms-gonen.ingest.md) -- **evidenced-by**: names and measures the semantically linked irrelevant-context steering that the source currently treats more generically as interference, tightening the relevance/interference dimension and the exclusion-over-instruction consequence.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) -- useful downstream application of the source's session-history consequence, but weaker first traversal value than the source's already-encoded links on scoping, activation, and decomposition.
- [Flat memory predicts specific cross-contamination failures that are empirically testable](../../../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) -- same broad family of interference concerns, but it specializes to memory-architecture failure modes rather than directly developing the source's volume/interference/complexity framework.
- [Ingest: On the "Induction Bias" in Sequence Models](../../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) -- architectural analogue with a speculative `context rot` extension, but weaker direct evidence for this note than the already-linked benchmark ingests and workspace-mechanism evidence.

## Index Membership

- [Context engineering](../../../../tags/context-engineering-README.md) -- the source's consequence section is directly about routing, loading, scoping, decomposition, and session-boundary control under bounded context, so the note belongs on this tag landing even though its current explicit tags route it through `foundations` and `learning-theory`.

## Synthesis Opportunities

- A synthesis note connecting [GSM-DC](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md), [semantic leakage](../../../../sources/semantic-leakage-lms-gonen.ingest.md), [the web-agent benchmark](../../../../sources/llm-webagents-long-context-reasoning-benchmark.ingest.md), and [context contamination below compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) could compress the current evidence into one claim: the same interference mechanism appears as synthetic distractor degradation, semantically linked prompt steering, agent-history objective drift, and sub-threshold stance drift.

## Maintenance Observations

- The source's volume-side evidence still mixes an external-only `lost in the middle` citation with mostly local KB ingests for the rest of the note's empirical surface. If a local snapshot/ingest for that paper is ever added, this note is an obvious place to align the evidence posture.

## Flags

None
