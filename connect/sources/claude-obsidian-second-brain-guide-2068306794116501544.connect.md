---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/claude-obsidian-second-brain-guide-2068306794116501544.md"
source_has_frontmatter: true
date: "2026-06-30"
depth: standard
---

# Connection Report: How to Build an AI Second Brain With Claude and Obsidian That Gets Smarter Every Day

**Source:** [How to Build an AI Second Brain With Claude and Obsidian That Gets Smarter Every Day](../../../sources/claude-obsidian-second-brain-guide-2068306794116501544.md)

## Discovery Trace

**Collection rules read:**
- Read `kb/sources/COLLECTION.md`. Snapshots are immutable; active authored links belong in the matching ingest report. The source collection authorizes scanning notes, reference, agent-memory-systems, agentic-systems, and sources; it excludes work and instructions. Labels available to an ingest report/source review include `evidence`, `derived-from`, `rationale`, `compares-with`, `defined-in`, and sparing `see-also`.

**Description listing scan:**
- Read destination heads: `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
- Ran `rg -n "^description:.*(Obsidian|second brain|LLM [Ww]iki|wiki|Claude|MCP|agent memory|memory|plain text|plain-text|filesystem|skill|permission|read-only|context activation|activation)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`. Kept the Karpathy ingests, `claude-obsidian`, `MehmetGoekce--llm-wiki`, `kenhuangus--llm-wiki`, `napkin`, the activation/storage notes, and the skill/authority notes. Rejected broad memory reviews where the only overlap was "memory" or "wiki".
- Ran `rg -n "^description:.*(permission|safety|credential|read-only|access control|authority|RBAC|secrets)" kb/notes kb/reference kb/sources kb/agent-memory-systems --glob '*.md'`. Kept `make-authority-explicit` and `what-is-an-agent-harness-2046980769747533830.ingest.md`; rejected shared-system RBAC reviews because this source only gives single-user permission advice.

**Topic indexes:**
- Read `kb/notes/agent-memory-README.md` and `kb/notes/learning-theory-README.md`. The source fits the agent-memory/context-engineering cluster, but the curated heads route to existing notes rather than requiring a new topic path.
- Ran `rg -n "^tags:.*(agent-memory|context-engineering|filesystem|skills|obsidian|activation|permission)" kb/notes kb/reference kb/instructions kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`. Kept `raw-accumulation-does-not-create-usable-memory`, `activate-behavior-changing-memory`, and `make-authority-explicit`; rejected tag-only hits without a specific articulation.

**Body search:**
- Ran `rg -n "Karpathy|LLM Wiki|Obsidian|second brain|mcp-obsidian|Local REST API|Claude Code tab|Schedule tab|keys, not prompts|read-only|plain text files|plain-text files|gets smarter" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`. Kept `llm-knowledge-bases-something-i-m-finding-very-useful.ingest.md`, `karpathy-llm-wiki.ingest.md`, `the-second-brain-trap-2041486539067154753.ingest.md`, `claude-obsidian.md`, and `MehmetGoekce--llm-wiki.md`.
- Ran `rg -n "obsidian-second-brain|eugeniughelbur|second-brain-starter|coleam00|claude-obsidian|AgriciDaniel" kb/agent-memory-systems kb/sources kb/notes kb/reference --glob '*.md'`. Found existing coverage only for `claude-obsidian`; the other two named repos have no durable artifact in the KB.
- Ran `find kb/agent-memory-systems -maxdepth 3 -type f -iname '*obsidian*' -o -iname '*second*brain*' -o -iname '*claude*obsidian*' -o -iname '*arscontexta*'`. Kept `claude-obsidian.md`; rejected `arscontexta.md` for this source because its generated-vault architecture is adjacent but not specifically named or newly illuminated.

**Link following:**
- Followed the existing Karpathy ingest links to `files-not-database`, `agents-navigate-by-deciding-what-to-read-next`, and `knowledge-storage-does-not-imply-contextual-activation`. These remain the central mechanism notes.
- Followed `claude-obsidian.md` relevant notes to `Knowledge storage does not imply contextual activation`, `Axes of artifact analysis`, `System-definition artifact`, and `Use trace-derived extraction`; kept only the activation and authority-related targets for this source because the guide is not an artifact-analysis review.
- Followed the security phrasing "keys, not prompts" to the permission/safety source and `make-authority-explicit`; kept the memory-authority note as the better local fit and kept the harness source as a weaker adjacent source.

## Connections Found

- [Karpathy LLM Wiki ingest](../../../../sources/karpathy-llm-wiki.ingest.md) -- **compares-with**: this guide repackages Karpathy's raw/wiki/schema architecture into a beginner operational setup for Claude Desktop, Obsidian, MCP, projects, skills, and schedules.
- [LLM Knowledge Bases ingest](../../../../sources/llm-knowledge-bases-something-i-m-finding-very-useful.ingest.md) -- **compares-with**: this guide cites the same Karpathy workflow line but adds setup-level adoption steps rather than new retrieval architecture.
- [The Second Brain Trap ingest](../../../../sources/the-second-brain-trap-2041486539067154753.ingest.md) -- **compares-with**: both sources frame second-brain value as activation during real work, though this guide is more promotional and less explicit about failure modes.
- [claude-obsidian](../../../../agent-memory-systems/reviews/claude-obsidian.md) -- **compares-with**: the guide explicitly recommends `claude-obsidian` as a ready-made implementation; the review gives the code-grounded version of the same adoption story.
- [LLM Wiki (MehmetGoekce)](../../../../agent-memory-systems/reviews/MehmetGoekce--llm-wiki.md) -- **compares-with**: both use Claude Code plus Logseq/Obsidian-style files with L1/L2 or project-scoped context as the activation mechanism.
- [napkin](../../../../agent-memory-systems/reviews/napkin.md) -- **compares-with**: both treat an Obsidian-compatible Markdown vault as an agent-readable substrate, but Napkin emphasizes pull tools and progressive disclosure rather than Claude Desktop setup.
- [Files beat a database for agent-operated knowledge bases](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) -- **evidence**: the guide argues that plain text, local ownership, Obsidian browsing, and model portability are the reason the setup stays useful across agents.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **evidence**: the guide's promised benefit is not storage alone but future sessions loading profile, project, live-data, and scheduled maintenance context.
- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -- **evidence**: the setup turns scattered notes into memory only after adding handles such as `CLAUDE.md`, project folders, links, skills, feedback, and maintenance routines.
- [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) -- **evidence**: project-scoped vaults, calendar/email reads, and scheduled organization are examples of trying to surface memory before the next action rather than only on retrospective search.
- [Make Authority Explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md) -- **evidence**: the "keys, not prompts" rule is a practitioner version of governing read/write/delete authority at the permission layer rather than relying on instruction text.
- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- **evidence**: the source presents user-authored project skills as reusable invoked workflows, supporting the claim that skills are a practical activation and workflow packaging surface.

## Bidirectional Candidates

- [claude-obsidian](../../../../agent-memory-systems/reviews/claude-obsidian.md) <-> source -- **compares-with**: if the review ever gets an adoption-evidence update, this source is a user-facing guide that recommends the reviewed system and names the setup affordances users notice first.

## Reverse-edge Candidates

- [Files beat a database for agent-operated knowledge bases](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) -> source -- **evidence**: the guide supplies mainstream-practitioner support for local plain-text files as the easiest agent memory substrate.
- [Make Authority Explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md) -> source -- **evidence**: "keys, not prompts" is a concise external phrasing for separating behavioral instructions from enforced permission boundaries.
- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -> source -- **evidence**: the source shows skills as end-user workflow memory, not only methodology packaging for KB operators.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [MCP bundles stateless tools with a stateful runtime](../../../../notes/mcp-bundles-stateless-tools-with-stateful-runtime.md) -- rejected: the guide uses MCP as the Obsidian bridge, but it does not make or evidence the note's state-tax argument.
- [Agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- rejected: the guide mentions scheduling, files, tools, and permissions, but not in a way that materially sharpens the runtime decomposition.
- [Commonplace agent memory coverage](../../../../reference/agent-memory-coverage.md) -- rejected: the source is useful comparison material for Commonplace's memory posture, but it does not describe the shipped Commonplace system.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) -- rejected: the guide points at similar memory gaps but does not change the local implementation plan.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- rejected: both involve Claude, but this source is about vault memory and setup, not model-authored workflow orchestration.
- [LLM Wiki (kenhuangus)](../../../../agent-memory-systems/reviews/kenhuangus--llm-wiki.md) -- weak fit: it shares the Karpathy wiki family, but this source does not discuss autonomous monitors, LLM extraction/integration, BM25 search, or daemon loops.
- `obsidian-second-brain` by `eugeniughelbur` -- rejected as a connection because no durable KB artifact exists yet.
- `second-brain-starter` by `coleam00` -- rejected as a connection because no durable KB artifact exists yet.

## Index Membership

- [Agent Memory Systems README](../../../../agent-memory-systems/README.md) -- the source itself should not be indexed as a reviewed system, but it can serve as source evidence for future lightweight coverage of the two named unreviewed repos.

## Synthesis Opportunities

The guide suggests an adoption-facing synthesis already implicit in the KB: successful "second brain" onboarding packages several layers together--plain files, always-loaded profile/project context, pull search, reusable skills, live-data reads, scheduled maintenance, and permission boundaries. Existing notes cover the mechanisms; the possible new synthesis would be about packaging order for beginners, not about agent-memory architecture itself.

## Maintenance Observations

- The source names `obsidian-second-brain` by `eugeniughelbur` and `second-brain-starter` by `coleam00`, but no matching source snapshot, lightweight coverage, or code-grounded review was found. Future agent-memory coverage could snapshot or inspect them if this family remains important.

## Flags

- No split required. The guide is broad, but the value is concentrated in adoption packaging around an already-covered Karpathy/Obsidian memory pattern.
