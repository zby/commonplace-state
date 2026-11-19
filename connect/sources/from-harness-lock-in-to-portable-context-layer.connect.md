---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/from-harness-lock-in-to-portable-context-layer.md"
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: From Harness Lock-In to Portable Context Layer

**Source:** [From Harness Lock-In to Portable Context Layer](../../../sources/from-harness-lock-in-to-portable-context-layer.md)

## Discovery Trace

**Collection rules and destination breadth:**

- Read `kb/sources/COLLECTION.md`. Its outbound surface authorizes `kb/notes/`, `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`; it excludes `kb/work/` and `kb/instructions/`. External prospecting was skipped because connect is repo-local and no additional external target was supplied.
- Read the target snapshot in full. Its independent claim clusters are harness portability, filesystem-wiki versus graph-memory substrate, MCP/skills serving, retrieval and compression, automatic conversation ingestion, and the MongoDB single-store argument.

**Curated heads and full title surfaces:**

- Read `kb/notes/tags-README.md`, `agent-memory-README.md`, `context-engineering-README.md`, and `architecture-README.md`. The relevant curated clusters were memory as a crosscutting system, consumer-specific access surfaces, filesystem-first storage with earned database exceptions, and activation/governance beyond storage. These tag heads do not declare `complete: true`, so title and body searches were still required.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The external-memory casebook already contains file-wiki, graph-memory, MCP, hybrid-retrieval, and trace-learning systems. The agentic-systems collection had no candidate whose whole-system focus improved traversal beyond the memory-system and theory matches.
- Generated complete title listings with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `reference`, `sources`, `agent-memory-systems`, and `agentic-systems`.

**Description listing scan:**

- Ran `rg '^description:.*(memory|harness|MCP|filesystem|portable|portability|progressive disclosure|context)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`.
- Kept the memory-design requirements, the cross-system comparison, LLM Wiki, and OKF Harness because each supplies a distinct axis missing from the article's own framing. Rejected most named memory engines because the article merely inventories them and following each would not sharpen its role.

**Body search:**

- Ran `rg -n -i "portable|portability|lock-in|disposable harness|swap.*harness|multiple consumers|serving layer|business logic|MCP|filesystem|unified memory|hybrid search|progressive disclosure|append-only|materialized view|continual learning" kb/notes --glob '*.md'`.
- Ran `rg -n -i "portable|portability|lock-in|disposable harness|multiple consumers|MCP|filesystem|unified memory|hybrid retrieval|progressive disclosure|append-only|materialized view" kb/reference --glob '*.md'`.
- Ran `rg -n -i "portable|portability|harness|MCP|filesystem|LLM wiki|hybrid retrieval|knowledge graph|append-only|materialized view|multi-consumer" kb/agent-memory-systems --glob '*.md'`.
- Ran `rg -n -i "portable|portability|lock-in|disposable|harness|MCP|context layer|memory" kb/agentic-systems --glob '*.md'`.
- Ran `rg -n -i "portable.*harness|context layer|MCP.*skills|LLM wiki|filesystem.*database|unified memory|continual learning|agent memory" kb/sources --glob '*.ingest.md' --glob '*.md'`.

**Link following and candidate evaluation:**

- Followed the memory-design synthesis into `serve-multiple-consumers`, `keep-compiled-views-aligned`, `evaluate-memory-by-effects`, `raw-accumulation`, and `continual-learning-requires-governing-behaviour-changing-writes`. The article's MCP-plus-skills design fits the first two, while its automatic-ingestion claim is bounded by the last three.
- Followed `files-not-database` to `many-to-many-edge-state-is-where-files-yield-to-a-database` and the Graphiti boundary. Kept both because the article supplies practitioner testimony for a light file wiki but uses scale and product sponsorship rather than relation structure to justify a database.
- Followed the skills-portability note through its cross-harness comparison. Kept it because the article independently reports that data portability does not make skill execution policy portable.
- Followed the casebook index into `llm-wiki`, `okf-harness`, Graphiti, Mem0, and Cognee. Kept LLM Wiki and OKF Harness as inspected realizations of the article's portable file-wiki branch; kept the cross-system matrix because it directly challenges substrate as the primary discriminator. Rejected separate edges to Graphiti, Mem0, and Cognee because the article's build-versus-buy inventory adds no technical evidence beyond the existing reviews.
- Followed the source neighborhood through the Karpathy LLM Wiki ingest, Koylan Personal Brain OS, Context Providers, Managed Agents, and Cerebras Knowledge. Kept Karpathy as the direct conceptual predecessor and Managed Agents as the strongest interface-portability comparison. Rejected Koylan and Cerebras as duplicate practitioner evidence for file-first and multi-surface memory already better represented by notes and code-grounded reviews.

## Connections Found

- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **compares-with**: the article calls periodic conversation ingestion continual learning, while the note requires selection, validation, authority, activation, and regression control before a durable write counts as governed behavioral learning.
- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- **is-evidence-for**: the author's reported difficulty moving Claude-specific workflows and embedded agents corroborates the note's distinction between portable instruction bodies and harness-specific execution policy.
- [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) -- **is-evidence-for**: the recommendation to host skills from the MCP server so business logic is not fragmented is practitioner evidence for one authoritative source plus synchronized consumer views.
- [Files beat a database for agent-operated knowledge bases](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) -- **is-evidence-for**: the author prefers a per-project Markdown/YAML wiki for everyday research and reserves graph memory for higher-precision workloads, giving context-bound practitioner support for an earned-complexity boundary.
- [Churning state on a many-to-many edge is where files yield to a database](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) -- **compares-with**: the article chooses database infrastructure by retrieval features and scale, whereas the note proposes relation structure plus edge-state churn as the sharper substrate trigger.
- [MCP bundles stateless tools with a stateful runtime](../../../../notes/mcp-bundles-stateless-tools-with-stateful-runtime.md) -- **compares-with**: the article treats MCP as a portability boundary for stateful memory and business logic; the note distinguishes that legitimate stateful case from the unjustified tax on stateless operations.
- [What the matrix shows across 148 agent memory systems](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) -- **compares-with**: the article organizes choices mainly by build effort and storage architecture, while the casebook finds activation and verification more discriminating than substrate alone.
- [LLM Wiki (nvk)](../../../../agent-memory-systems/reviews/llm-wiki.md) -- **compares-with**: this inspected implementation realizes the article's portable filesystem branch with mirrored Claude, Codex, and OpenCode packaging, while exposing the semantic-governance work the article leaves implicit.
- [OKF Harness](../../../../agent-memory-systems/reviews/okf-harness.md) -- **compares-with**: the article cites OKF as a vendor-neutral file format; the inspected harness shows that actual portability also needs generated agent guidance, bounded reads, provenance, checks, and adapter maintenance.
- [Ingest: LLM Wiki](../../../../sources/karpathy-llm-wiki.ingest.md) -- **compares-with**: Karpathy supplies the direct raw/wiki/control-plane predecessor; this article adds harness lock-in, MCP serving, graph-memory alternatives, and the still-unresolved portability of skills.
- [Ingest: Scaling Managed Agents: Decoupling the brain from the hands](../../../../sources/scaling-managed-agents-decoupling-brain-from-hands.ingest.md) -- **compares-with**: both argue for replaceable harness implementations over stable retained state and interfaces, but Managed Agents grounds the boundary in a production session/computation/capability decomposition rather than a personal-memory architecture.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) → source -- **evidenced-by**: the practitioner report independently identifies embedded workflows and agents as the remaining skill-portability failure after data portability.
- [Files beat a database for agent-operated knowledge bases](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) → source -- **evidenced-by**: the author's reported use of a light file wiki for ordinary work and a heavier graph path only for precision-demanding workloads qualifies the note's files-first boundary.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) → source -- **evidenced-by**: the article is a useful terminology boundary case in which automatic persistence and retrieval are called learning without a visible acceptance, authority, or regression gate.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -- genuine but redundant with the sharper continual-learning and casebook-matrix connections; the article does add extraction and indexing after capture, so it is not simply a raw-accumulation example.
- [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md) -- the MCP/skills split resembles multiple surfaces, but both are described mainly as alternative harness integration paths rather than as surfaces for substantively different consumers.
- `kb/reference/agent-memory-coverage.md` -- Commonplace has an obvious local analogue, but only a broad `see-also` label fits and the reference adds no traversal value beyond the stronger theory and casebook candidates.
- `kb/agent-memory-systems/reviews/graphiti.md`, `mem0.md`, and `cognee.md` -- named by the article, but separate links would merely reproduce its product inventory; their existing reviews already carry the technical distinctions.
- `kb/agentic-systems/gbrain.md` -- the system also separates a host harness from durable memory, but its whole-system adoption, scheduling, and trust-boundary analysis is less direct than its separately reviewed memory subsystem and the Managed Agents source.

## Index Membership

None

## Synthesis Opportunities

- The article, [skills portability](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md), [memory-system design](../../../../notes/designing-agent-memory-systems.md), [LLM Wiki](../../../../agent-memory-systems/reviews/llm-wiki.md), and [OKF Harness](../../../../agent-memory-systems/reviews/okf-harness.md) jointly imply a three-boundary portability claim: canonical retained artifacts can be portable while access/business logic and harness execution policy remain separately coupled. Owning the data is necessary but insufficient; each boundary needs its own stable contract, synchronization rule, and degradation path.

## Maintenance Observations

- The snapshot faithfully retains several malformed `Explore Next` hyperlinks from the source page whose visible destination differs from the authored `href`; downstream analysis should cite the named durable KB artifacts instead of those broken links.

## Flags

- Split candidate: the source makes independent assertions about portability, storage substrate, retrieval/compression, continual learning, and database operations across more than three topic areas. Any promotion should isolate one mechanism rather than turn the whole article into one note.
- Sponsorship tension: MongoDB sponsored the article, and the strongest unsourced quantitative claims concern MongoDB RAM use and single-store scaling. Treat those as vendor-adjacent practitioner claims, not independent evidence for the database choice.
