---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/dreaming-with-a-dynamic-workflow-cookbook.md"
source_has_frontmatter: true
date: "2026-11-07"
depth: standard
---

# Connection Report: Dreaming with a dynamic workflow

**Source:** [Dreaming with a dynamic workflow](../../../../sources/.snapshots/dreaming-with-a-dynamic-workflow-cookbook.md)

The source is an immutable snapshot. Every outbound candidate below is for the future `kb/sources/dreaming-with-a-dynamic-workflow-cookbook.ingest.md`, which does not exist yet. Labels come from the `kb/sources/COLLECTION.md` outbound table. Ingest links never point into `kb/work/` or `kb/instructions/`.

**What the source claims.** An Anthropic cookbook recipe (2026-11-02) builds a "dream" as a Managed Agents dynamic workflow. A lead agent (Sonnet) turns a plain-language request into a workflow run. One Haiku analyzer per finished-session transcript runs **Verify** (check memory claims against the transcript; downgrade overconfident claims; fix or note contradictions), **Enrich** (exact identifiers, staleness and verification dates, process observations), and **Organize** (small linked files with frontmatter, `[[slug]]` links, a shared `_index.md`). One sequential organizer then merges duplicates, uses `MOVED TO` stubs, marks `CONFLICT` lines or dated supersessions, and completes the index. Future sessions mount the store read-only.

**Distinctive mechanisms:**

- Concurrency discipline: re-read before editing, make targeted index edits, read back after each write, and defer merges and renames to the single-writer organizer phase.
- Prompt-injection posture: transcripts and memory are treated as data; tools are file-only; the network allowlist is empty; the store is mounted read-only.
- An optional channel loads `_index.md` into the system prompt, capped at 4,096 characters.
- There is no review by default. A bad transcript reaches the agent the next morning.
- Raw transcripts and records live in a temp directory that is cleared by default.
- The reported cost is about $0.36 for 11 transcripts and about $8 for 50 long ones.

## Discovery Trace

**Collection contract:** Read `kb/sources/COLLECTION.md` → Outbound links. Authorised destinations are theory, reference, agent-memory-systems, agentic-systems, sources, tags and external. `kb/work/` and `kb/instructions/` are excluded. Labels: `derived-from` (external); `is-evidence-for` (theory, agent-memory-systems); `abstracted-from` (theory); `rests-on` (theory); `compares-with` (theory, sources, agent-memory-systems, agentic-systems); `defined-in` (theory/definitions); `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). The snapshot never authors links.

**External:** The only already-known external target is the source URL itself. It gets `derived-from` in the ingest frontmatter or body, which is routine. External prospecting was skipped as the skill requires.

**Titles listing (theory):**

- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` returned 442 titles. I filtered them with `grep -iE 'distill|consolidat|session|transcript|trace|stale|supersed|inject|poison|memory|index|offline|background|log|episode|always-loaded|wiki|merge|dedup|conflict|contradict|read-only|mutat|curat|maintenance|garbage|forget'`.
- About 60 titles were flagged. I then read the descriptions of 19 of them: trace-extracted-memory, open-domain-memory-retention, session-history, raw-accumulation, use-trace-extraction, retire-redact-supersede-relax, superseded-choices, make-authority-explicit, maintenance-capacity, always-loaded-context-mechanisms, retaining-episode-evidence, checked-outcome-licenses, preserve-evidence-without-loading-history, keep-compiled-views-aligned, wikiwiki-principle, designing-agent-memory-systems, evaluate-memory-by-effects, activate-behavior-changing-memory and stale-self-description.

**Body search:**

- `rg -il 'dream|sleep-time|sleep time|consolidat' kb/sources/*.md` returned about 40 ingests. Kept: components-of-agent-memory, language-models-need-sleep, a-harness-for-every-task-dynamic-workflows, memorylace, trajectory-informed-memory-generation. Rejected: DreamCoder, both wake-sleep ingests (program induction), and the RSI and self-evolving papers (weight or code self-modification, not a memory store).
- `rg -il 'managed agents|memory store|claude managed' kb/sources kb/agentic-systems kb/agent-memory-systems kb/theory kb/reference` surfaced scaling-managed-agents (via ls), letta, three-dimensions-agent-memory-store and others. Most are keyword-only hits.
- `ls kb/sources | rg -i 'karpathy|llm-wiki|wiki|sleep|letta|memgpt|managed|anthropic|poison'` surfaced karpathy-llm-wiki, building-self-correcting-memory-in-openwiki, scaling-managed-agents-decoupling-brain-from-hands and letta-memgpt-stateful-agents.
- `rg -il 'prompt injection|injected instruction|memory poisoning' kb/theory` matched only llm-context-interprets-instructions-and-content-through-one-medium.
- `rg -il 'concurrent (writer|edit)|single.writer|lost update|overwrit' kb/theory` matched agent-orchestration-needs-coordination-guarantees, accumulation-counts-dependence, make-authority-explicit and instantiation-alone. Kept: coordination-guarantees, whose body names the "who may overwrite what" inconsistency failure.
- `rg -il 'sleeptime|sleep-time|dreaming|offline consolidation|offline pass' kb/theory` matched only retaining-episode-evidence, which already cites components-of-agent-memory's Mt. Moon dreaming case.
- `rg -il 'dream|consolidat|transcript' kb/agentic-systems kb/agent-memory-systems` matched the letta review (sleeptime agents), trace-learning-techniques-in-related-systems and agent-memory-landscape.
- `rg -n 'sleeptime|sleep-time|dream' agent-memory-systems/reviews/letta.md ...` confirmed that Letta's sleeptime agent reads finished transcripts and edits shared blocks.
- `rg -il 'prompt injection|untrusted' kb/reference` found nothing load-bearing. `rg -il 'distill' kb/reference` surfaced ADR 053 (see Maintenance Observations).

**Topic indexes / tag heads:**

- Read the `kb/tags/` listing, plus the descriptions and inclusion text of `agent-memory-README.md`, `trace-learning-README.md`, `curation-README.md` and `deploy-time-learning-README.md`.
- curation and deploy-time-learning are `complete: true`, but sources sit outside participating collections, so completeness is irrelevant here.
- Destination READMEs were not read in full. Title and description listings plus targeted body search covered recall.

**Link following:**

- From `components-of-agent-memory.ingest.md` (untracked in the working tree, ingested 2026-11-07): its Connections already target retaining-episode-evidence, access-burden-and-transformation-burden and coordination guarantees. This confirms the cookbook is the operational companion of that conceptual report.
- From `language-models-need-sleep...ingest.md`: it already `compares-with` DreamCoder on representational form, which gives the cookbook a three-way contrast: weights vs symbolic library vs editable files.
- From `trace-extracted-memory-earns-authority...`: its body discusses TRACE's hypothesis-then-verify staging, which matches the analyzer's Verify step.
- `retaining-episode-evidence...` lines 45–49 cite the Mt. Moon correction.

**Reference destination:** No reference artifact describes Commonplace in a way this source bears on concretely. The destination was skipped for outbound links.

## Connections Found

- [The components of agent memory](../../../../sources/components-of-agent-memory.ingest.md) -- **compares-with**: same vendor, same "dreaming" term, same date window. Compare on what is evaluated vs what is shipped. The research report supplies selected experiments: the Mt. Moon correction, wiki-vs-search gains, and the per-contract single-writer repair. The cookbook supplies the executable recipe with fixed Verify/Enrich/Organize prompts and no evaluation. A reader judging the recipe needs the report's bounded evidence, and vice versa.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) -- **is-evidence-for**: the analyzer prompt encodes partial rung-climbing. It verifies memory claims against the transcript, downgrades confident claims the transcript shows were uncertain, and adds verification dates and staleness notes. Yet the recipe states "There's no review by default", so a bad transcript reaches the agent next morning. This is a concrete vendor case of a store where the verify rung is automated by a weak LLM oracle and the authority it grants goes unrecorded.
- [Retire, Redact, Supersede, And Relax Memory](../../../../theory/agent-memory-requirements/retire-redact-supersede-relax.md) -- **is-evidence-for**: the source implements several lifecycle operations concretely. Stale facts are dated and superseded rather than copied (the `TIDEWICK_DATA_DIR` case). The organizer keeps both values with a `CONFLICT:` line when it cannot decide. Merged files retire through `MOVED TO [[slug]]` stubs. Leaked secrets are handled by editing plus redacting memory versions, with 30-day version audit.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../theory/agent-orchestration-needs-coordination-guarantees-not-just.md) -- **is-evidence-for**: concurrent analyzers share one directory. The recipe's guarantee against inconsistency is explicit and layered:
  - re-read before edit;
  - targeted index edits, never full rewrites;
  - read-back after every write, because "a write that reports success can still be replaced";
  - link rather than merge during the parallel phase;
  - all merge and rename work deferred to a single sequential organizer, while "No other agent is writing".

  This names which guarantee the topology buys, not just the channel.
- [Open-domain memory retention needs a declared output spec](../../../../theory/open-domain-memory-retention-needs-a-declared-output-spec.md) -- **is-evidence-for**: the recipe's "what to keep" default is empty `INSTRUCTIONS`, and it tells users to "Say what the memory is for". The analyzer prompt meanwhile carries a built-in coding-agent spec: commands, identifiers, staleness and process observations. This is a practitioner instance of supplying the inclusion criterion from a declared output account rather than from input salience.
- [LLM context interprets instructions and content through one medium](../../../../theory/llm-context-interprets-instructions-and-content-through-one-medium.md) -- **is-evidence-for**: the injection section is an architecture-enforced role boundary for a one-medium system.
  - The transcript text never enters a prompt; analyzers open it with a read tool.
  - The system prompt declares transcripts and memory "data, not instructions".
  - Tools are file-only and the network allowlist is empty.
  - Output is mounted read-only.

  The recipe also states the residual: loading `_index.md` into `instructions` lets injected text "steer every session".
- [Keep Lineage And Compiled Views From Drifting](../../../../theory/agent-memory-requirements/keep-compiled-views-aligned.md) -- **is-evidence-for**: `_index.md` is a compiled catalog maintained by many analyzers and then completed by the organizer. Step 3 optionally promotes it into always-loaded `instructions` (4,096-character cap). The recipe warns that "a wrong line reaches every session" and "a growing store will outgrow the cap". This is a concrete compiled view acquiring behavior-shaping force, with the drift risk named by the vendor.
- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) -- **is-evidence-for** (bounding case): the recipe's design depends on transcripts as ground truth for Verify. Yet by default the session is deleted, and the records folder lives under the temp directory that "most systems clear when the machine restarts". A nightly store therefore normally retains distilled claims without the episodes that would let a later pass re-examine them. Retention requires the opt-in `COOKBOOK_RECORDS_DIR`. This is the opposite configuration to the components-of-agent-memory Mt. Moon case the note already cites.
- [Letta review](../../../../agent-memory-systems/reviews/letta.md) -- **compares-with**: on the axis of background transcript-to-memory agents. Letta's sleeptime agent edits shared core blocks after turns or at a set frequency. The cookbook batches finished sessions nightly, splits parallel per-transcript analyzers from a single organizer, and writes a linked file store mounted read-only by the consumer rather than shared editable blocks.
- [Claude Code dynamic workflows review](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- **compares-with**: on the model-authored orchestrator axis. Here the lead agent writes the workflow from a plain-language message over `predefined_agents` in Managed Agents rather than in Claude Code. The notebook then audits the run against platform thread records ("Where the run differed from what the message asked") instead of trusting the lead agent's report.
- [A harness for every task: dynamic workflows](../../../../sources/a-harness-for-every-task-dynamic-workflows.ingest.md) -- **compares-with**: a second Anthropic practitioner account of model-authored JS workflows. This one is a concrete production-shaped use: phases, grouping pace set in prose, 64-thread limits, and failure-tolerant steps. Compare on how the orchestrator is constrained and verified.
- [Karpathy LLM wiki](../../../../sources/karpathy-llm-wiki.ingest.md) -- **compares-with**: both build agent-maintained small linked Markdown pages with an index catalog. They differ on raw-layer retention: Karpathy keeps a persistent raw-sources layer plus a log, while the cookbook discards raw transcripts by default. They also differ on who maintains the wiki: an interactive agent vs an unattended nightly batch.
- [Language models need sleep](../../../../sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md) -- **compares-with**: both use the "dreaming" or offline-consolidation schedule. They differ on representational form: weight self-distillation vs editable, inspectable, versioned files. This extends that ingest's existing DreamCoder contrast to a third form.

## Bidirectional Candidates

- [The components of agent memory](../../../../sources/components-of-agent-memory.ingest.md) <-> source -- **compares-with**: the research ingest's Extractable Value item 3 ("per-contract single-writer pages") and its dreaming definition would benefit from pointing at the shipped recipe as the operational form. Because that ingest is currently untracked, the return link can be added before its first commit.
- [Letta review](../../../../agent-memory-systems/reviews/letta.md) <-> source -- **compares-with**: optional. The return path helps a reader of the sleeptime section see a vendor alternative with an explicit analyzer/organizer split. The agent-memory-systems collection is historical and frozen per AGENTS.md, so this is likely not actionable.

## Reverse-edge Candidates

- [Trace-extracted memory earns authority per operation, not at capture](../../../../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) → source ingest -- **evidenced-by** (theory label; qualifies or bounds): this is a shipped vendor recipe whose automated Verify step has no recorded rung and no default review. It is not corroboration, because the source was not a test the claim could have failed.
- [Retire, Redact, Supersede, And Relax Memory](../../../../theory/agent-memory-requirements/retire-redact-supersede-relax.md) → source ingest -- **evidenced-by**: concrete operation set: dated supersession, CONFLICT marking, MOVED-TO retirement stubs and version redaction.
- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) → source ingest -- **evidenced-by**: a bounding case where the default configuration discards episodes after distilling them. It pairs naturally with the already-cited Mt. Moon case. The note is currently modified in the working tree (see git status), so coordinate with that edit.

## Off-authorisation Candidates

- None

## Raw Text Candidates

- None

## Rejected Candidates

- [Scaling managed agents: decoupling brain from hands](../../../../sources/scaling-managed-agents-decoupling-brain-from-hands.ingest.md) -- same platform, but its axis (brain/hand/session interface decomposition) is not what the cookbook exercises. It is a keyword-level match only.
- [Trajectory-informed memory generation](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) -- also extracts tips from trajectories. But the cookbook reports no task-outcome evaluation, so there is no shared measured axis to compare. Revisit if the ingest's analysis frames a "what gets extracted" comparison.
- [MemoryLACE](../../../../sources/memorylace-lifecycle-aware-consolidation-evidence-retrieval.ingest.md) -- its lifecycle relations over atomic memories are adjacent to the CONFLICT and supersession marking. But retire-redact-supersede-relax is the stronger and more direct target. A third lifecycle link adds little.
- [OpenWiki self-correcting memory](../../../../sources/building-self-correcting-memory-in-openwiki-2092280107033616451.ingest.md) -- its staleness comes from source-code versioning, while the cookbook's staleness comes from later transcripts. The comparison is possible but weaker than the Karpathy wiki contrast.
- [Raw accumulation does not create usable memory](../../../../theory/raw-accumulation-does-not-create-usable-memory.md) -- the recipe is an instance of ingress work (handles, provenance dates, links). But the link would only restate the note's thesis without bounding it.
- [Session history should not be the default next context](../../../../theory/session-history-should-not-be-the-default-next-context.md) and [Preserve evidence without loading history](../../../../theory/agent-memory-requirements/preserve-evidence-without-loading-history.md) -- consistent with the recipe, but the recipe does not preserve evidence by default. retaining-episode-evidence carries that tension more precisely.
- [Use trace extraction as meta-learning](../../../../theory/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) and [Make authority explicit](../../../../theory/agent-memory-requirements/make-authority-explicit.md) -- accurate but generic. The trace-extracted-authority note and the one-medium note carry the specific mechanisms.
- [Always-loaded context mechanisms in agent harnesses](../../../../theory/always-loaded-context-mechanisms-in-agent-harnesses.md) -- the mount-`instructions` channel could be one row in its survey. As a link from the ingest it is weaker than keep-compiled-views-aligned. Consider it as a Maintenance input for that survey instead.
- [Maintenance capacity must match harmful-artifact inflow](../../../../theory/maintenance-capacity-must-match-harmful-artifact-inflow.md) -- nightly unreviewed writes are an inflow, but the source gives no rate or capacity data.
- [Access burden and transformation burden are distinct query dimensions](../../../../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) -- relevant to the companion research report's evaluations, not to this evaluation-free recipe.
- DreamCoder ingests and RSI/self-evolving sources -- "dream" or "self-improvement" keyword hits on program-library or weight/code modification. They are reachable through language-models-need-sleep.

## Index Membership

- [agent-memory tag head](../../../../tags/agent-memory-README.md) -- the ingest may carry `tags: [agent-memory]`. The cookbook substantively covers cross-session retention, lifecycle and governance of a memory store.
- [trace-learning tag head](../../../../tags/trace-learning-README.md) -- possible `tags: [trace-learning]`. Raw session traces are turned into durable memory by an extraction step. Check the head's inclusion condition first: it is phrased for system reviews.

## Synthesis Opportunities

The cookbook, components-of-agent-memory, and the Letta sleeptime review jointly suggest an unrecorded comparison: **offline memory consolidation designs differ mainly in whether the transcripts that serve as Verify's oracle are retained after consolidation.**

- Mt. Moon retained the transcript and could correct a note.
- The cookbook discards transcripts by default and can re-verify only against new transcripts.
- Letta keeps message history in its database.

This bears directly on retaining-episode-evidence and trace-extracted-authority. It is a candidate for a theory note or an extension of retaining-episode-evidence, not for creation during connect.

## Maintenance Observations

- **Terminology:** the source uses "distill" throughout ("distills it into small linked memory files", `memory_distill`). [ADR 053](../../../../reference/adr/053-retire-distillation-without-a-successor-term.md) retires "distillation" as a technical term. The ingest author should quote the source's wording in Quotes but use other terms in analysis (for example, extraction, or lineage labels).
- **Untracked sibling:** `kb/sources/components-of-agent-memory.ingest.md` is untracked in the current working tree. Links to it from the new ingest will break on publish if it is not committed alongside or first.
- **Survey gap:** [Always-loaded context mechanisms in agent harnesses](../../../../theory/always-loaded-context-mechanisms-in-agent-harnesses.md) may lack the Managed Agents memory-store mount `instructions` channel (system-prompt injection, 4,096-character cap). I did not verify this against the note's body.

## Flags

- Split candidate check: the source touches 5+ notes across memory lifecycle, orchestration coordination, injection/authority and compiled views. But it is a single recipe, not multiple independent assertions, so it is not a split candidate. The ingest should still prioritise 3–5 of the connections above rather than all of them.
- Tension: the recipe treats transcripts as "the source of truth" for verification, while the default configuration deletes them. Record this as an analytical point in the ingest's Limitations, not only as a link.
