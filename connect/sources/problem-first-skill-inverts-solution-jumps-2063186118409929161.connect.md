---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/problem-first-skill-inverts-solution-jumps-2063186118409929161.md"
source_has_frontmatter: true
date: "2026-06-17"
depth: standard
---

# Connection Report: /problem-first: a simple skill to invert bad ideas

**Source:** [/problem-first: a simple skill to invert bad ideas](../../../sources/problem-first-skill-inverts-solution-jumps-2063186118409929161.md)

## Discovery Trace

**Description listing scan:**
- Read `kb/sources/COLLECTION.md`; source snapshots are immutable, while ingest reports carry the active outbound surface. Authorised source-report labels to notes include `evidence`, `derived-from`, `rationale`, `defined-in`, and sparse `see-also`.
- Read `kb/notes/COLLECTION.md`; reverse edges from notes to sources may use `evidence` or `derived-from` when a source corroborates or grounds a claim.
- Read destination heads `kb/notes/README.md`, `kb/reference/README.md`, and `kb/agent-memory-systems/README.md`.
- Ran `rg -n "^description:.*(skill|instruction|workflow|triage|problem|solution|validation|context|agent|reasoning|procedure)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob "*.md"`. Flagged [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md), [Skills derive from methodology through distillation](../../../../notes/skills-derive-from-methodology.md), [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md), [Instructions are typed callables with document type signatures](../../../../notes/instructions-are-typed-callables.md), [Methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md), [Unit testing LLM instructions requires mocking the tool boundary](../../../../notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md), and [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md).

**Topic indexes:**
- No `x-article` tag README exists. The source content routes mainly to the skills/instruction/process-structure cluster rather than a source tag.
- Read `kb/agent-memory-systems/README.md`; rejected agent-memory review destinations because the source is a product-skill anecdote, not an inspectable memory system or context-engineering system review.

**Body search:**
- Ran `rg -n "problem-first|solution jump|solution-jumping|triage capacity|assumption challenges|alternative framings|evidence status|draft message|process structure|output structure" kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems --glob "*.md"`. No prior KB artifact discusses `problem-first` or the PM solution-to-problem inversion pattern. Existing hits around process structure reinforce that the novelty is an applied example rather than a new theory cluster.
- Evaluated process-structure hits in existing ingests: the source differs from code-reasoning papers because its example is a lightweight practitioner skill for product judgment, not benchmarked reasoning accuracy.

**Link following:**
- Followed [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) to [Skills derive from methodology through distillation](../../../../notes/skills-derive-from-methodology.md), [Methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md), and [Instructions are typed callables with document type signatures](../../../../notes/instructions-are-typed-callables.md). The source corroborates the skills-as-procedural-packaging cluster but does not change its harness-policy distinction.
- Followed [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) to [Methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md). The source gives a non-code example where required process sections prevent predictable skipped reasoning steps.

## Connections Found

- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- **evidence**: the `problem-first` skill's value is explicitly attributed to mandatory sections that a PM under pressure skips: assumption challenges, alternative framings, and a draft message.
- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- **evidence**: the source presents `problem-first` as a directly invoked skill running in Claude Code, Cowork, or Cursor on company context files, reinforcing skills as packaged, user-invoked procedures rather than only prose advice.
- [Skills derive from methodology through distillation](../../../../notes/skills-derive-from-methodology.md) -- **evidence**: the post describes a reusable PM reasoning method distilled into a one-call skill, preserving the procedure while stripping broader PM discovery theory from the runtime path.
- [Methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md) -- **evidence**: the source frames the skill as a way to ensure the same eight-step reasoning protocol runs every time, demonstrating skill-level process enforcement below scripts or deterministic validation.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -> source -- **evidence**: this note could cite the source as a practitioner example outside code/math reasoning where process constraints supply value by forcing skipped reasoning work.
- [Skills derive from methodology through distillation](../../../../notes/skills-derive-from-methodology.md) -> source -- **evidence**: this note's caveat about skills distilled directly from domain artifacts could use `problem-first` as an example of domain-practice-to-skill distillation.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Instructions are typed callables with document type signatures](../../../../notes/instructions-are-typed-callables.md) -- rejected as too indirect: the source implies an input/output shape for `problem-first`, but does not discuss type signatures, document affordances, or validation at the callable boundary.
- [Unit testing LLM instructions requires mocking the tool boundary](../../../../notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) -- rejected: the source mentions validation tests inside product discovery, not testing the skill's own tool-call behavior.
- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md) -- rejected: the source says the skill runs in one AI call and is wired into PM OS, but the mechanism is not precomputing known inputs before a later call.
- [Agent memory systems README](../../../../agent-memory-systems/README.md) -- rejected: PM OS may include company context files, but the source does not expose enough system design to review it as an agent-memory system.

## Index Membership

- [type-system README](../../../../tags/type-system-README.md) -- possible future membership only if a promoted note expands the process-structure example set; the snapshot itself should not be indexed directly from connect.

## Synthesis Opportunities

The source and existing process-structure ingests suggest a synthesis around "skill value often comes from forcing skipped reasoning moves under pressure, not from automating the domain answer." This is adjacent to [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) but may become a narrower note if more practitioner skill examples accumulate.

## Maintenance Observations

None

## Flags

- The source is promotional and anecdotal. Treat it as a practitioner example, not evidence that `problem-first` works at the reported success rates.
