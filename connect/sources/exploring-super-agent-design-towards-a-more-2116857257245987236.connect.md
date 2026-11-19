---
description: "Connection discovery for DeepSeek Harness's Super-agent architecture proposal: routing, bounded context, continuity, supervision, and security comparisons."
type: types/connect-report.md
source: kb/sources/.snapshots/exploring-super-agent-design-towards-a-more-2116857257245987236.md
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Exploring Super-agent Design

**Source:** [Exploring Super-agent Design: Towards a More Autonomous Agent System](../../../../sources/.snapshots/exploring-super-agent-design-towards-a-more-2116857257245987236.md)

Discovery only, produced with `cp-skill-connect`. All edges below are candidates for future authoring, not existing KB state. The snapshot is immutable. The matching ingest does not currently exist; its future authored analysis, not the snapshot, would carry outbound connections. No durable artifact should link to this ignored snapshot.

The source proposes a long-lived interaction Router over task-isolated Workers, deterministic event filtering and subscription pass-through, pointer-based context recall, asynchronous operations, compute/state/environment separation, and an external model-driven Watchdog. Its main scope is concurrent, always-online work rather than decomposition of one tightly coupled task. It explicitly leaves long-term memory, cross-instance authority, and endpoint security unresolved. Its synthetic scheduling experiments use simulated coding work, not measured coding quality.

## Discovery Trace

### Setup and search coverage

- Read the source fully, the [source collection contract](../../../../sources/COLLECTION.md), the [connect-report type](../../../../types/connect-report.md), and the [report collection contract](../../../COLLECTION.md).
- Authorized local destinations: theory, reference, agent-memory-systems, agentic-systems, tags, and sources. Excluded instructions and work were not prospected. The tags destination is named for scanning but has no authorized outbound label; tag heads can supply discovery context without becoming ordinary edge targets.
- For each of those six destinations, read its root `README.md` and generated a fresh complete title listing with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. Recovered truncated title output before evaluating candidates. Brief matches were treated as matches on their owning documents, never as edge targets.
- For each destination, scanned descriptions with `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'context|schedul|rout(er|ing)|concurren|watchdog|spacebot|asynchron|permission|progress|state|human attention'`. Recovered the truncated description output. This was a scoped description scan, not a semantic similarity score; no scores were produced.
- Ran two focused body searches separately in every destination: `rg -l -i 'pass.through|router|inline.{0,8}spill|context.isolat|progressive disclosure' kb/<destination> --glob '*.md'` and `rg -l -i 'watchdog|progress monitor|compute.{0,20}state|decoupl.{0,30}(brain|execution)|full.duplex' kb/<destination> --glob '*.md'`.
- The snapshot has no `tags:` field. No by-tag enumeration or completeness shortcut applied. Read the context-engineering and architecture tag heads as additional curated discovery surfaces; neither declares `complete: true`.

### Theory

- Titles and descriptions surfaced scheduler–LLM separation, runtime responsibility separation, context efficiency, selective history loading, pointer design, coordination guarantees, and privilege quarantine. Read these seven notes fully.
- Body search found scheduler separation, pointer design, and related scoping notes; the supervision/state query returned no direct Watchdog note. The retained-theories proposal was a state-word match, not a supervision mechanism, and was not promoted.
- Followed the Managed Agents ingest's existing links to runtime responsibility separation and selective history loading. Followed the pointer note's context-efficiency link, and the coordination note's privilege/scoping neighborhood through the separately discovered quarantine note. These distinguished retrieval, execution authority, and shared-write guarantees rather than treating all as one memory problem.
- Kept six complementary theory edges below. Runtime responsibility separation was useful analytical scaffolding but redundant with the more concrete Managed Agents comparison for this report; it is recorded as a rejected edge, not a missing conceptual fit.

### Reference

- The root landing and title/description scans exposed navigation, storage architecture, review architecture, and deterministic write-context assembly. The routing/context query matched navigation and packaging documents; the supervision/state query returned no matches.
- Rejected write-context assembly at description resolution: assembling fixed authoring inputs is narrower than continuous event context injection and does not provide a useful source-specific implementation comparison. Storage and review state are Commonplace-specific lifecycle mechanisms, not evidence for the proposed cloud runtime. No reference edge retained.

### Agent-memory-systems

- The root landing identifies this as a frozen historical survey. Titles/descriptions surfaced Spacebot, Letta, Scroll, and Virtual Context. Broad progressive-disclosure hits were not treated as sufficient connections.
- Followed the [Spacebot ingest](../../../../sources/spacedriveapp-spacebot-ai-agent.ingest.md) to the full code-grounded Spacebot review. Kept the review as the stronger comparison target rather than adding a duplicate edge to the README ingest.
- Spacebot supplies a concrete comparison on user-facing versus background roles and pushed working context. Its historical review does not establish present-day parity with the proposed Super-agent or independent performance superiority. Scroll was not retained: executable context management is less directly matched than Chain of Recall versus pointer design.

### Agentic-systems

- The root landing separates authored accounts from archived generated analyses. Description and body scans surfaced Agno AgentOS, dynamic workflows, and historical memory wrappers. Read Agno AgentOS fully.
- Kept Agno on durable run/recovery and authority boundaries. Rejected a dynamic-workflows edge at description resolution: model-authored within-task orchestrators are not the source's continuous cross-task Router, and the source explicitly distinguishes those responsibilities.
- Did not treat archived tables or counts as current characterization. No search was expanded into the separately owned agentic-system-analyses collection, which the source contract does not name as a prospecting destination.

### Tags

- Read the tags landing, fresh titles and filtered descriptions, then the [context-engineering head](../../../../tags/context-engineering-README.md) and [architecture head](../../../../tags/architecture-README.md) fully. Their routing led to the theory distinctions above.
- The source is substantively about both topics, but sources are outside tag-index participating collections. No direct snapshot membership or durable snapshot link is proposed. A future ingest's optional search tags are distinct from index membership.

### Sources

- Titles/descriptions and body searches surfaced Managed Agents, Spacebot, folding subagents, Slate, and runtime-independent persistent agents.
- Read Managed Agents, Spacebot, and folding subagents fully. Followed Managed Agents into the runtime/history theory neighborhood and Spacebot into its stronger historical code review.
- Kept Managed Agents for the exact compute/state/execution comparison the source itself names, and folding subagents for a bounded architectural counterpoint. Rejected the duplicate Spacebot ingest edge in favor of the review. Slate's compressed worker returns are already represented in the selective-history note; a separate source edge would add little here.

### External

- No external prospecting, web access, semantic-search service, or agent launch was used. Evaluated only the original post URL already present in the snapshot for `derived-from`. Other external links discovered in local notes were not expanded into additional candidates.

## Connections Found

These labels apply to a future ingest or source review, never to the immutable snapshot.

- [Scheduler–LLM separation exploits an error-correction asymmetry](../../../../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — **compares-with**: the source's deterministic admission and subscription pass-through move repeated routing work out of model decisions while retaining semantic dispatch in the Router. This gives a concrete comparison between model-chosen policy and mechanically applied transitions. Its reported token savings do not test the note's reliability-cost conjecture.
- [Context efficiency is the central design concern in agent systems](../../../../theory/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **is-evidence-for**: Inline & Spill and task isolation are practitioner instances of managing per-window interference, while the pass-through ablation separately reports aggregate cache-read savings. The source bears on the feasibility/cost distinction, but its mock coding workload does not establish context as the sole bottleneck or prove task-quality gains.
- [Session history should not be the default next context](../../../../theory/session-history-should-not-be-the-default-next-context.md) — **is-evidence-for**: Chain of Recall retains references to prior tasks and sessions outside the Router's immediate window and retrieves context on demand. This is a concrete design instance of separating retained history from currently loaded context, not a test of long-term recall quality.
- [Pointer design tradeoffs in progressive disclosure](../../../../theory/pointer-design-tradeoffs-in-progressive-disclosure.md) — **compares-with**: the source inlines nearby object IDs and compact summaries, then exposes further summaries and IDs on each recall hop. The note supplies axes for judging those pointers' selection value, context cost, availability, and accuracy instead of assuming graph reachability guarantees useful recall.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../theory/agent-orchestration-needs-coordination-guarantees-not-just.md) — **compares-with**: many-to-many Thread subscriptions notify overlapping Workers of shared activity, but notifications only give them a chance to detect conflicts. The note distinguishes that delivery channel from ownership, atomic claim, and consistency guarantees needed for shared writes.
- [Agent orchestration needs a privilege quarantine, not just a permission scope](../../../../theory/orchestration-needs-privilege-quarantine-not-permission-scope.md) — **see-also**: section 8.4 explicitly connects untrusted event intake to command-capable endpoints and local credentials. The note supplies a reader/actor separation candidate for that open risk, including the residual risk of a poisoned reader deceiving the actor. It does not establish that the proposed architecture implements quarantine.
- [Spacebot](../../../../agent-memory-systems/reviews/spacebot.md) — **compares-with**: both architectures separate responsive external interaction from background task execution and selectively expose retained context. The historical code review lets a reader compare Spacebot's channel/branch/worker roles and pushed memory layers against a global Router and task-scoped Workers; it does not show an equivalent independent semantic Watchdog.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) — **compares-with**: AgentOS has durable run records, checkpoint and approval boundaries, database-claimed schedules, and separately scoped builder authority. These provide a concrete recovery/authority comparison for the source's cloud state separation and privileged Watchdog, while showing why persistence is not exactly-once side-effect execution or a universal least-privilege policy.
- [Scaling Managed Agents: Decoupling the brain from the hands](../../../../sources/scaling-managed-agents-decoupling-brain-from-hands.ingest.md) — **compares-with**: section 5.2 names the same brain/session/environment separation but contrasts a managed sandbox/VPC setting with intermittently connected personal machines holding uncommitted work and credentials. The ingest makes recovery, credential isolation, and interface assumptions inspectable without asserting equivalence of the two deployments.
- [Building agents: When to fold subagents into your main agent loop](../../../../sources/building-agents-fold-subagents-into-main-loop.ingest.md) — **compares-with**: the source enforces a non-executing Router for concurrent independent tasks, whereas the Anthropic account recommends folding unnecessary within-task specialists into one loop. Their shared axis is decomposition benefit versus context-transfer overhead. The latter preserves disposable parallel workers and conflict-based isolation, so this is a scope-sensitive counterpoint, not a blanket contradiction.
- [Original post](https://x.com/DeepSeekHarness/status/2116857257245987236) — **derived-from**: a future ingest's analysis would be worked out from this captured architectural article. This is source identity, not a claim of independently verified implementation.

## Bidirectional Candidates

None. A matching ingest is absent, and a return link to the snapshot would violate the source contract. Outbound comparison candidacy does not automatically warrant reciprocal edits.

## Reverse-edge Candidates

None at the current authored-surface state. Useful theory citations would need a tracked ingest or the external original, not this ignored reading copy. No reverse edge is proposed to the cache report either.

## Off-authorisation Candidates

None. The tag heads were discovery surfaces rather than useful source-authored edges requiring a new relation. There is no reason to extend authorization just to link them.

## Raw Text Candidates

None.

## Rejected Candidates

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../../theory/agent-runtime-analysis-should-separate-scheduling-context-state.md) — the three responsibilities map well to routing, Inline & Spill, and durable state/remote execution, but an additional edge would duplicate the more concrete Managed Agents comparison and the specific context mechanisms above. The mapping does not independently validate an exhaustive three-part architecture.
- [Spacebot README ingest](../../../../sources/spacedriveapp-spacebot-ai-agent.ingest.md) — useful discovery bridge, but the code-grounded review is the more informative comparison target; do not duplicate both edges by default.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) — a within-task, model-authored orchestration API is not the same scheduling problem as the article's lightweight global Router across independent tasks. Shared subagent vocabulary alone is insufficient.
- [Deterministic write-context assembly](../../../../reference/proposals/deterministic-write-context-assembly.md) — a fixed-input authoring-context proposal is not an implemented counterpart to event-driven recall. Similar context-assembly terminology would obscure the different problem boundaries.

## Index Membership

None. Do not index the snapshot. Sources are outside the participating collections for tag membership; optional search tags on a future ingest would not add it to tag member listings.

## Synthesis Opportunities

None. Existing notes already distinguish scheduling, context, retention, authority, and coordination guarantees. The source adds architectural instances and a bounded counterpoint, not a clearly missing higher-order claim.

## Maintenance Observations

- The name-paired ingest is absent at discovery time. A separately authorized ingest step is needed before local durable claims can cite Commonplace's analysis of this snapshot. This report does not create it or retain source quotes.

## Flags

- **Multi-claim / split signal:** the source connects across more than five notes and at least three areas: context selection, concurrency/coordination, and recovery/security. Do not split or rewrite the immutable capture. A future ingest should separate those claims, and future theory extraction should use distinct claim scopes rather than one all-purpose Super-agent note.
- **Evidence boundary:** the article calls itself architectural ideas, not a list of released DeepSeek Harness features. It is a machine translation with omitted diagrams. Its simulated coding tool measures scheduling and coordination, not real code quality. Batching and pass-through figures are indicative workload-specific results, not general throughput guarantees.
- **Unresolved tension:** a single global Router maximizes continuity but concentrates trust and context. Worker event sharing is not a write-conflict protocol; long-term memory and endpoint credential protection remain open in the source. Keep these limits beside any future comparison or evidence claim.
