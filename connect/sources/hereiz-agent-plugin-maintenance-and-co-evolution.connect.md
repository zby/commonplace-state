---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/hereiz-agent-plugin-maintenance-and-co-evolution.md"
source_has_frontmatter: true
date: "2026-09-03"
depth: standard
---

# Connection Report: On the Maintenance and Co-evolution of Agent Plugins

**Source:** [On the Maintenance and Co-evolution of Agent Plugins](../../../../sources/.snapshots/hereiz-agent-plugin-maintenance-and-co-evolution.md)

## Discovery Trace

**Collection contract and authored surface:**

- Read `kb/sources/COLLECTION.md` and `kb/reports/types/connect-report.md`. The snapshot is immutable; its matching ingest is the authored outbound surface. Authorised local destinations are notes, reference, agent-memory systems, agentic systems, and sources. Work and instructions are excluded.
- Read the complete 41-page snapshot and the curated heads `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The snapshot has no tags, so no tag README or by-tag search applied.
- Read `kb/notes/COLLECTION.md` while checking possible return edges. No reverse edge is proposed before the tracked ingest exists because durable artifacts must not link to an immutable `.snapshots/` path.
- No semantic-search scores were available. Discovery used repo-local lexical scans followed by full-artifact evaluation.

**Full title listings:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` separately over all authorised local destinations. The fresh listings covered 424 note titles, 159 reference titles, 175 agent-memory-system titles, 14 agentic-system titles, and 370 source titles.
- The note titles surfaced the readable-artifact, system-definition, instruction-testing, semantic-review, and compiled-view clusters. The source and system titles surfaced the closest empirical comparators and concrete instruction/runtime drift cases. The reference listing supplied no target whose Commonplace-specific state would help interpret this external study.

**Description and body searches:**

- `rg -n -i 'co-evol|co-change|coupl|synchron|drift|stale' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' --glob '!.snapshots/**'` -- kept the readable-artifact note, the context-file study, and the Fractal and beads-rust drift cases; rejected generic freshness and database-staleness matches.
- `rg -n -i 'natural-language.{0,40}(instruction|software|artifact)|instruction.{0,40}(runtime|behavior|artifact)|AI-facing Markdown|Markdown.{0,40}(behavior|instruction)' ...` over the same destinations -- kept the system-definition vocabulary and Harness-IF comparison; evaluated but rejected the general skill-packaging note because this paper does not test routing or declarative execution policy.
- `rg -n -i 'semantic.{0,24}(diff|change)|commit.{0,24}(meaning|classification)|docs commit|instruction.{0,24}(test|validat)' ...` -- found the instruction-testing and semantic-review cluster, but the paper proposes rather than evaluates those methods, so they were rejected as outbound targets.
- `rg '^description:.*(skill|instruction|system-definition|natural-language|artifact|maintain|semantic|coupl|drift)' ...` -- evaluated descriptions across every authorised destination. The paper's empirical claims are strongest for mixed-form maintenance and commit interpretation, not for memory read-back or Commonplace implementation details.

**Link following:**

- Followed the readable-artifact note to representational-form co-evolution and Co-Harness. Co-Harness uses *co-evolution* for alternating optimization of harness artifacts and model weights, not repository co-change, so it is a lexical false friend here.
- Followed the instruction-testing note to automated text tests, semantic review, and underspecification. These provide possible future methods but do not receive direct evidence from the paper's repository-mining design.
- Followed the compiled-view note to concrete source-of-truth rules and then inspected Fractal and beads-rust. The note itself is scoped to generated derivatives, but the two system analyses contain direct examples of agent-facing instructions disagreeing with runtime behavior.
- Inspected Agent Skills for Context Engineering as a concrete plugin marketplace. The paper's aggregate dataset does not identify findings for that repository, so a direct comparison would imply unsupported sample membership or representativeness.

## Connections Found

- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: the paper supplies repository-scale evidence that natural-language instructions and symbolic scripts form a real maintenance dependency inside skills, while not establishing the note's broader optimization or continual-learning claims.
- [System-definition artifact](../../../../notes/definitions/system-definition-artifact.md) -- **defined-in**: the definition precisely names why a Markdown instruction file read at runtime is behavior-shaping software rather than ordinary documentation.
- [Context Engineering for AI Agents in Open-Source Software](../../../../sources/context-engineering-ai-agents-oss.ingest.md) -- **compares-with**: both are empirical studies of agent-facing repository text; the earlier study measures context-file adoption and evolution and leaves code–instruction co-evolution open, while this paper measures that dependency inside plugins.
- [Harness-IF](../../../../sources/harness-if-instruction-following-across-instruction-surfaces.ingest.md) -- **compares-with**: Harness-IF measures whether rules on several instruction surfaces affect agent behavior, while this paper measures how those behavior-shaping surfaces are classified and maintained in repositories.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) -- **compares-with**: the code-grounded Fractal analysis contains a concrete stale-skill/runtime-location mismatch of the kind this paper treats as an instruction-maintenance defect.
- [beads-rust](../../../../agentic-systems/reviews/beads-rust.md) -- **compares-with**: the beads-rust analysis shows shipped agent instructions lagging stronger current CLI claim and sync behavior, providing another concrete instance of runtime-significant instruction drift.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None. Durable return links should target the tracked ingest after it exists, not this immutable local snapshot.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- topical overlap is strong, but the paper inventories components and repository changes rather than testing skill discovery, invocation, or frontmatter execution policy.
- [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) -- the paper demonstrates script–instruction maintenance coupling, but its paired Markdown files are not shown to be generated derivatives of scripts, so the note's source-of-truth and regeneration claim is not directly tested.
- [Unit testing LLM instructions requires mocking the tool boundary](../../../../notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) -- the paper calls for instruction-aware consistency checks but neither implements nor evaluates tool-boundary mocking.
- [Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) -- both use *co-evolution*, but Co-Harness studies an optimization loop across model weights and a mutable harness; this paper studies observed repository co-change among plugin components.
- [Agent Skills for Context Engineering](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) -- it is a concrete plugin marketplace, but the aggregate paper does not expose repository-level results that would support a specific comparison.

## Index Membership

None

## Synthesis Opportunities

- The paper, the context-file evolution study, and the Fractal and beads-rust cases jointly suggest a bounded claim: classify and maintain agent-facing text by its runtime behavioral role, not by file extension or documentation-flavored commit labels. This would combine population evidence, commit-diff semantics, and concrete drift failures; it should preserve the Claude Code plugin scope until replicated elsewhere.

## Maintenance Observations

None

## Flags

- Split candidate for later theory extraction: the paper independently supports marketplace-growth, commit-semantics, and Script–Markdown-dependency findings. A single new note would not remain composable across all three.
