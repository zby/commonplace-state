---
description: "SKILL.state tests explicit current-state prompts and exposes the sufficiency, schema and evidence-retention boundaries of discarding conversational history."
type: kb/reports/types/connect-report.md
source: kb/sources/skill-state-scalable-long-horizon-agent-skills.ingest.md
source_has_frontmatter: true
date: "2026-09-25"
depth: standard
---

# Connection Report: SKILL.state

**Source:** [Accepted SKILL.state ingest](../../../../sources/skill-state-scalable-long-horizon-agent-skills.ingest.md)

## Discovery Trace

Post-ingest pass: read the accepted ingest fully and reassessed all three connections and the inbound candidate. Reused pre-ingest discovery below; no new lexical search is claimed. The selected example remains bounded by supplied schemas and keeps prompt selection distinct from permanent evidence disposal.

Read the complete 1,740-line v3 paper, including prompt templates, generator pseudocode, noise construction, model failures and all appendix tables. Reused the batch contracts, curated heads and complete title surfaces across all five destinations. Notes-description query for state, sufficiency, bounds, history and schema identified session-history selection, active work state and evidence retention. Read session-history, preserve-evidence and the linked chat-history tradeoff fully; active work state was already fully read in this batch. Followed the history note's explicit retention/loading distinction through those linked notes. Focused SKILL.state, SkillExecBench, sufficient-statistic and null-deletion search across reference, agent-memory-systems, agentic-systems and sources returned no candidate. No external prospecting; instructions and work excluded.

## Connections Found

- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) — **compares-with**: each step receives fixed procedure, current structured state and latest observation. Domain-state patches replace repeated transcript reconstruction. The benchmark comparisons support this design in the reported tasks, not an unconditional claim that history is dispensable.
- [Preserve evidence without loading history](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) — **compares-with**: permanent reasoning disposal is stronger than excluding history from the acting prompt. The paper's own limitations recognize tasks whose objective includes the historical trajectory and observations whose later relevance was missed. External audit retention is a separate design choice; the paper does not test retaining an unloaded evidence archive.
- [Active work state](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) — **compares-with**: domain-authored mutable schemas and null deletion keep current facts effective, but the paper's action-state examples do not establish the note's full evidence-gated closure lifecycle. A schema-valid predicted state can still disagree with the environment.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) → accepted tracked ingest — **evidenced-by**: reported state-only versus transcript and capped-compression comparisons, preserving fixed-domain schema, model, units and sufficiency limits.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- A fixed number of JSON fields proves constant state size: field contents and latest observations must also remain bounded independently of horizon.
- Schema validation establishes correct world-state updates: well-formed but wrong omissions or overwrites remain possible.
- Noise tests establish adversarial injection resistance: Appendix C explicitly tests random, irrelevant, non-state-changing telemetry.
- LangGraph itself necessarily has the benchmark's full-history behavior: the comparison uses an authored LangGraph-style prompt, not all configurations of the framework.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

Version 3 is dated September 2, 2026. The runtime uses a domain-authored schema, model-proposed dictionary mutations/null deletions, deterministic validation and rollback/retry on invalid patches. It applies the patch before executing the action in Algorithm 1; the paper does not fully specify reconciliation of valid patches after an action fails. Correctly maintained sufficient state is an assumption, not established by the syntax validator.

The O(1) prompt and O(T) cumulative-input argument holds only if procedure, serialized state and latest observation sizes are bounded independently of horizon. A fixed field count does not bound growing tested-hypothesis or discovered-item lists. The source explicitly limits lossless disposal when schemas must evolve, earlier observations acquire unforeseen relevance, or history is itself the output. Multi-agent concurrency/conflict resolution remains future work.

Warehouse Gemini T=100 reports .94 versus .84/.87/.91 accuracy for Prompt/Memory/Stateful and 65,408 versus 1,062,387 Stateful tokens; T=200 remains .94. These are five-generator-seed results, not all possible horizons or domains. Software T=25 is .88 versus Stateful .94, and Gemma T=100 ties Stateful .42; do not repeat universal improvement. Budget-controlled Warehouse T=100 scores .94 versus .18 window/.52 summary/.22 LLMLingua. The text alternates characters and tokens for the approximately 1,800 budget and prompt sizes; avoid claiming precise tokenizer-matched equivalence. Report cumulative counts as source-reported, not independently verified.

Public Gemini results are CTF 54.2%, Retail 58.3%, Airline 32.4%, but the paper does not clearly explain repetition producing fractional CTF percentages over 100 tasks. Retail's prompt is larger for SKILL.state despite lower cumulative tokens. Recovery is immediate only after a corrective alert in successful scenarios; canceled order and closed PR fail for all runtimes. Noise is strictly irrelevant observational telemetry, despite broader language about rule overrides in the main text.

Reported small-model errors are overwrite/deletion 68%, schema/type 20%, syntax 12%. This classification does not isolate reasoning ability or show that grammar constraints repair semantic loss. Domain schemas and immutable procedures are supplied; maintaining task state is not by itself cross-task learning or harness self-revision. No code inspected or executed for this paper pass.
