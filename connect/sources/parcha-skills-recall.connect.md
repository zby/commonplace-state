---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/parcha-skills-recall.md"
source_has_frontmatter: true
date: "2026-11-05"
depth: standard
---

# Connection Report: Recall skill (Parcha-ai/parcha-skills, recall subtree)

**Source:** [Recall skill (Parcha-ai/parcha-skills, recall subtree)](../../../../sources/.snapshots/parcha-skills-recall.md)

The source is an immutable snapshot (`kb/sources/.snapshots/`). Every outbound candidate below is a recommendation for the tracked ingest that will carry its authored surface, expected at `kb/sources/parcha-skills-recall.ingest.md` (not yet present at report time). Labels come from the `kb/sources/COLLECTION.md` outbound table; `kb/work/` and `kb/instructions/` are excluded destinations.

Source claim and mechanism, as read: an agent skill (instructions only; the engine is private) that searches a local SQLite index over raw Claude Code and Codex session transcripts. Key mechanisms: capture is the harness's own transcripts, not a new capture API; retrieval is ranked with an evidence gate and a per-hit `WHY` line; exact identifiers are the strongest evidence; `show` loads only bounded windows (`--prompts`, `--around`, `--tail`) rather than whole sessions; four outcome playbooks (find/verify, continue, repeat, skill-ify); empty output "does not prove the work never happened"; thinking blocks are never stored and secret-shaped lines are redacted at ingest; an optional central Brain adds deliberate user-requested capture (`recall_capture`), exact-receipt `recall_forget`, and receipt-cited answers; `session-export` serves a machine consumer (`/recap`) with complete ordered pages, distinct from human windows.

## Discovery Trace

**Setup:**
- Read `kb/sources/COLLECTION.md` "Outbound links": destinations theory, reference, agent-memory-systems, agentic-systems, tags, other sources; excluded `kb/work/`, `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). Snapshot is never the link author; candidates target the ingest.
- `external` prospecting skipped: no external target supplied beyond the source's own URL (the ingest's `derived-from` to the pinned GitHub tree URL is routine and handled by ingest).
- Note: `AGENTS.md` describes `kb/agent-memory-systems/` as historical and frozen. The sources contract still authorises it as a destination, so candidates there are kept, but no reverse edges are proposed from it.

**Description listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'session|history|trace|distill|skill|retriev|search|memory|evidence|receipt|recall|transcript|episod|identifier|lexical|absence|provenance'` -- flagged: session-history-should-not-be-the-default-next-context, preserve-evidence-without-loading-history, active-work-state-is-not-retrospective-memory-or-chat-history, raw-accumulation-does-not-create-usable-memory, trace-extracted-memory-earns-authority-per-operation-not-at-capture, use-trace-extraction-as-meta-learning, retire-redact-supersede-relax, create-memory-directly, retaining-episode-evidence-keeps-a-distilled-rule-open-to, a-retrieval-miss-is-a-local-reflective-path-failure, knowledge-access-architecture-must-be-evaluated-end-to-end, history-has-one-chance-to-become-checkable.
- `rg -m1 '^description:'` over each flagged theory file -- kept those whose claim the source's mechanisms directly instantiate or stress (see Connections Found).
- `rg -N '^description:' kb/sources/ --glob '*.ingest.md' | rg -i 'session|transcript|history|skill.{0,20}(from|extract|distill|creat)|recall|episod|trace'` -- flagged: scaling-managed-agents-decoupling-brain-from-hands, from-agent-memory-to-portable-skills, context-as-an-environment, letta-memgpt-stateful-agents, tulving-pearlstone-availability-versus-accessibility, skill-synthesis-materializing-knowledge-as-skills, skill-state-scalable-long-horizon-agent-skills.
- `ls kb/sources | grep -iE 'recall|session|transcript|history|parcha|episod|cass|claude-mem|memex'` -- no existing Parcha/Recall ingest (no duplicate).

**Topic indexes:**
- `kb/tags/agent-memory-README.md` -- Core Frame and Boundaries sections confirmed raw-accumulation, preserve-evidence, active-work-state, trace-extracted-memory as the curated cluster; Requirements Map surfaced activate-behavior-changing-memory and retire-redact-supersede-relax.
- `kb/tags/trace-learning-README.md` -- historical comparison is agent-memory-systems/trace-learning-techniques-in-related-systems.md; "session capture and transcript mining" is in its inclusion text. No by-tag rg needed for source (snapshot carries no `tags:`).
- `kb/agent-memory-systems/README.md` -- confirms historical/frozen status.
- `ls kb/agentic-systems/comparisons/*` -- memory comparison table and landscape are matrix-scale; not useful as targeted link targets.

**Body search:**
- `rg -l -i 'session transcript|session history|past sessions|prior sessions|transcript search|session search' kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/sources --glob '*.md'` -- ~60 hits; narrowed to agent-memory-systems reviews (deja-vu, hermes-agent, cass_memory_system, synapptic) and the theory cluster above.
- `rg -l -i 'claude/projects|\.codex/sessions|jsonl transcript|session jsonl|transcripts? (are )?indexed|index(es|ed)? (prior|past) sessions|session-search|session search' ...` -- deja-vu, hermes-agent, cass_memory_system, halo, synapptic, sage-wiki, pal, skillnote; plus reference ADR 006 (only a directory-name collision note -- rejected).
- `rg -n -i 'session (recall|search)|session_search|FTS' kb/agent-memory-systems/reviews/hermes-agent.md` -- Hermes `session_search` over SQLite FTS5/trigram with anchored windows and bounded whole-session reads: same design point as Recall.
- `rg -n -i 'cass (search|session)|session search' kb/agent-memory-systems/reviews/cass_memory_system.md` -- cass session search feeding diary/playbook distillation.
- `rg -l -i 'absence of (a )?(result|hit|match)|empty result|no hit does not|does not prove (the )?(absence|it never)' kb/theory` -- only an unrelated hit in natural-language-project-state-specializes-search-heuristics.md. No note owns "a retrieval miss is not evidence of absence".
- `rg -l -i 'lexical (search|retrieval)|exact identifier|identifier match' kb/theory` -- none. No note owns identifier-anchored retrieval.
- `rg -l -i 'skill.{0,30}(from|out of) (past |prior )?(sessions|traces|transcripts)|distill.{0,30}skill' kb/theory` -- none in theory; trace-to-skill comparison lives in sources (from-agent-memory-to-portable-skills).
- `rg -l -i 'transcript|session log|session history' kb/reference --glob '*.md' | grep -v adr` -- commands, navigation, validation-contract, archived harness-capture proposal, trajectory-aware-evaluation proposal; none is a direct Commonplace analogue to transcript search. Reference destination yields no candidate.
- `rg -n -i 'recall' kb/sources/letta-memgpt-stateful-agents.ingest.md`, `rg -n -i 'exact history|search|grep|retriev' kb/sources/context-as-an-environment.ingest.md`, `rg -n -i 'trace|skill|provenance' kb/sources/from-agent-memory-to-portable-skills.ingest.md`, `rg -n -i 'session log|getEvents|durable' kb/sources/scaling-managed-agents-decoupling-brain-from-hands.ingest.md` -- evaluated as compares-with candidates.

**Link following:**
- session-history-should-not-be-the-default-next-context -> preserve-evidence-without-loading-history -> active-work-state-is-not-retrospective-memory-or-chat-history -> serve-multiple-consumers: one chain on capture vs loading vs live state; Recall touches each link.
- raw-accumulation-does-not-create-usable-memory -> agent-memory-needs-discoverable-composable-trusted-knowledge-under, knowledge-storage-does-not-imply-contextual-activation: confirms the ingress claim Recall partially tests.
- trace-extracted-memory-earns-authority-per-operation-not-at-capture -> use-trace-extraction-as-meta-learning, from-agent-memory-to-portable-skills ingest: trace-to-skill cluster.
- deja-vu review -> `kb/agentic-system-analyses/retained/vshulcz--deja-vu/`: newer analyses of deja-vu, hermes-agent, cass_memory_system exist under agentic-system-analyses (not an authorised sources destination; see Off-authorisation).

## Connections Found

- [Preserve Evidence Without Making History The Next Context](../../../../theory/agent-memory-requirements/preserve-evidence-without-loading-history.md) -- **is-evidence-for**: Recall is a practitioner instance of the capture/loading split the note requires: harness transcripts are retained whole, secret-shaped lines are redacted at ingest, and `show` loads only bounded windows (prompts, ±3 turns, tail) with receipts for audit; it bears on the note's "Redacted trace stores" and "capture is not loading" methods without testing them.
- [Session history should not be the default next context](../../../../theory/session-history-should-not-be-the-default-next-context.md) -- **is-evidence-for**: the skill explicitly says "read only the best-supported session instead of searching entire transcripts" and warns sessions reach 80 MB, so persistence and loading are separate decisions made by a deliberate search-then-window selection step.
- [Active work state is not retrospective memory or chat history](../../../../theory/active-work-state-is-not-retrospective-memory-or-chat-history.md) -- **is-evidence-for**: the Continue playbook reconstructs live state from a retrospective transcript (`show --tail 30`, then check the branch/slot still exists, then ask the user where to resume), which is exactly the "each resumed session reconstruct[s] the real state from a trace" cost the note attributes to using chat history as active work state.
- [Raw accumulation does not create usable memory](../../../../theory/raw-accumulation-does-not-create-usable-memory.md) -- **is-evidence-for**: Recall puts ingress in the index rather than in authored artifacts (entity index, exact identifier matching, phrase-first matching, an evidence gate and a `WHY` line per hit); find/verify/continue/repeat work over raw traces, but skill-ify still needs a separate distillation step, which bounds where index-side ingress suffices versus where authored ingress is still needed.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) -- **is-evidence-for**: the skill-ify playbook goes straight from a working window to an abstracted recipe ("separate the durable recipe ... from one-off data") with no verify step, and search hits are explicitly "pointers to evidence" until opened; a concrete case of the abstract rung being reached without the verify rung.
- [Use Trace Extraction As Meta-Learning](../../../../theory/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) -- **is-evidence-for**: skill-ify is user-triggered, after-the-fact trace extraction into a readable artifact (SKILL.md), handed to the harness's skill creator; it illustrates the readable-artifact path and its signal-quality dependence on the user choosing a session that "worked".
- [Serve Multiple Consumers, Not One Retrieval Interface](../../../../theory/agent-memory-requirements/serve-multiple-consumers.md) -- **is-evidence-for**: Recall exposes distinct surfaces for distinct consumers: human-oriented ranked search and `show` windows, a machine `session-export` with stable evidence IDs, cursors, and completeness receipts for `/recap`, and a `session-relations` graph that excludes merely similar sessions.
- [Retire, Redact, Supersede, And Relax Memory](../../../../theory/agent-memory-requirements/retire-redact-supersede-relax.md) -- **is-evidence-for**: redaction at ingest, never storing thinking blocks, exact-receipt `recall_forget` ("do not infer record identity from search text"), and a `doctor` retention watchdog that warns when harness transcript deletion is re-enabled are concrete lifecycle operations, including the inverse case where upstream retention is the threat.
- [Activate Behavior-Changing Memory Before The Mistake](../../../../theory/agent-memory-requirements/activate-behavior-changing-memory.md) -- **is-evidence-for**: Recall is pull-only (explicit search, plus `related` at session start only "when the user references prior work"), so it is a clean instance of the retrospective-search surface the note says is insufficient for behavior-changing memory; contrast deja-vu, which adds session-start and per-prompt hooks.
- [deja-vu](../../../../agent-memory-systems/reviews/deja-vu.md) -- **compares-with**: same design point (local index over existing Claude Code/Codex session stores, redaction at ingest, MCP recall tools) on the axis of read-back activation: Recall is pull-only with an evidence gate and `WHY` explanations; deja-vu adds push hooks and a curated note layer.
- [Hermes Agent](../../../../agent-memory-systems/reviews/hermes-agent.md) -- **compares-with**: on the axis of raw-session search as an evidence surface: Hermes `session_search` over SQLite FTS5/trigram with anchored windows and bounded whole-session reads matches Recall's search-then-window design, but Hermes owns the session store while Recall indexes another harness's transcripts.
- [cass-memory](../../../../agent-memory-systems/reviews/cass_memory_system.md) -- **compares-with**: on the axis of what follows session search: cass feeds session search into diary summaries, LLM reflection and scored playbook rules automatically, whereas Recall's distillation (skill-ify) is user-triggered and unscored.
- [Ingest: From Agent Memory to Portable Skills](../../../../sources/from-agent-memory-to-portable-skills.ingest.md) -- **compares-with**: on the trace-to-skill axis: NAMS adds source-linked claims, automated gates, human approval, and drift re-grounding; Recall's skill-ify has none of these, which sharpens what provenance and currency checks buy.
- [Ingest: Scaling Managed Agents](../../../../sources/scaling-managed-agents-decoupling-brain-from-hands.ingest.md) -- **compares-with**: on the axis of durable session logs as context objects: Managed Agents designs the session log as a first-class interface (`getEvents()`), while Recall retrofits the same "store everything, load slices" posture onto harness transcripts it does not own.
- [Ingest: Context as an Environment (Scroll)](../../../../sources/context-as-an-environment.ingest.md) -- **compares-with**: on the axis of exact-history access: Scroll's failure trajectories leave records reachable but missed by bad query formulation, the same failure Recall's identifier-first query guidance and "empty output is not absence" rule are written against.

## Bidirectional Candidates

None. The return direction from theory notes is handled under Reverse-edge Candidates (theory is not the sources collection, so it is not a symmetric same-collection edge).

## Reverse-edge Candidates

All conditional on the ingest `kb/sources/parcha-skills-recall.ingest.md` existing; theory edges to sources target the ingest, never the snapshot.

- [Active work state is not retrospective memory or chat history](../../../../theory/active-work-state-is-not-retrospective-memory-or-chat-history.md) -> ingest -- **evidenced-by** (theory label): qualifies the claim with a practitioner tool whose Continue playbook pays the reconstruct-from-trace cost explicitly; not corroboration (no attempt to refute).
- [Preserve Evidence Without Making History The Next Context](../../../../theory/agent-memory-requirements/preserve-evidence-without-loading-history.md) -> ingest -- **evidenced-by**: bounds the Methods list with a retrofit case: the capture substrate is someone else's transcript store, so retention policy is outside the memory system's control (the `cleanupPeriodDays` watchdog).

## Off-authorisation Candidates

- [deja-vu analysis overview](../../../../agentic-system-analyses/retained/vshulcz--deja-vu/overview.md), [Hermes Agent analysis overview](../../../../agentic-system-analyses/retained/nousresearch--hermes-agent/overview.md), [cass_memory_system analysis overview](../../../../agentic-system-analyses/retained/dicklesworthstone--cass_memory_system/overview.md) -- these are the current (non-frozen) analyses of the three closest comparison systems; `compares-with` would fit, but `kb/agentic-system-analyses/` is not in the sources outbound destination list. Suggest extending the sources contract to authorise `compares-with` / `see-also` into `agentic-system-analyses` now that `agent-memory-systems` is frozen, or else keep pointing at the frozen reviews.

## Raw Text Candidates

None.

## Rejected Candidates

- [Ingest: Letta/MemGPT](../../../../sources/letta-memgpt-stateful-agents.ingest.md) -- Letta's "recall memory" tier is searchable conversation history, but it is agent-self-managed and owned by the platform; the overlap is mostly the word "recall". Too weak versus Hermes/deja-vu.
- [Ingest: Tulving and Pearlstone, availability versus accessibility](../../../../sources/tulving-pearlstone-availability-versus-accessibility.ingest.md) -- Recall's "empty output does not prove absence" and "thinking blocks are not findable" map loosely onto availability vs accessibility, but the source makes no claim about cue structure; linking would be decorative.
- [A retrieval miss is a local reflective-path failure](../../../../theory/a-retrieval-miss-is-a-local-reflective-path-failure.md) -- about missed KB artifacts leaving a represented aspect inert; Recall's miss guidance is about evidential inference from empty results, a different point.
- [Knowledge-access architecture must be evaluated end to end](../../../../theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md) -- Recall supplies no evaluation, only design; Scroll already carries this link.
- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) -- the skill-ify playbook does not say whether the generated skill links back to its session, so the source cannot bear on the claim either way.
- [Create Memory Directly](../../../../theory/agent-memory-requirements/create-memory-directly.md) -- the central Brain's user-requested `recall_capture` is adjacent, but it is an optional private service described in one paragraph; too thin to carry a load-bearing label.
- [Ingest: Skill synthesis](../../../../sources/skill-synthesis-materializing-knowledge-as-skills-2032179291031.ingest.md) -- synthesizes skills from domain source material (commits, OWASP), not from agent session traces; NAMS is the better trace-to-skill comparison.
- [Synapptic](../../../../agent-memory-systems/reviews/synapptic.md) -- also mines Claude transcripts, but into user profiles rather than session retrieval; comparison axis is weak.
- `kb/reference/adr/006-two-tree-installation-layout.md` -- mentions `~/.claude/projects/` only as a naming-collision note.

## Index Membership

- [Trace-learning tag head](../../../../tags/trace-learning-README.md) -- the ingest could carry `tags: [trace-learning]` if the analysis treats skill-ify as the substantive trace-to-distilled loop; the core of the source is retrieval, so check the head's inclusion condition before tagging. Sources do not affect tag member listings.
- [Agent-memory tag head](../../../../tags/agent-memory-README.md) -- stronger fit for an ingest `tags: [agent-memory]`: retention, recall and lifecycle across sessions are the source's substantive subject.

## Synthesis Opportunities

Recall, deja-vu, and Hermes `session_search` independently converge on one pattern: keep the harness's raw session store as the memory substrate, put ingress into a disposable lexical/entity index, and load only bounded, receipt-bearing windows. Together with raw-accumulation-does-not-create-usable-memory, they imply a candidate higher-order claim: index-side ingress (exact identifiers, evidence gates, match explanations) is sufficient for find/verify/continue/repeat over episodes, while authored ingress is needed only once a session must become a reusable rule. Not created here.

## Maintenance Observations

- Contract gap: `kb/sources/COLLECTION.md` authorises the frozen `kb/agent-memory-systems/` but not `kb/agentic-system-analyses/`, where the current analyses of the closest comparison systems now live. New source ingests in the memory space will keep pointing at frozen reviews unless the destination list is extended.
- Unnamed mechanism: no theory note owns "an empty or weak retrieval result is not evidence of absence" (Recall states it twice, and Scroll's failure analysis has the same shape), nor "exact identifiers are the strongest retrieval evidence". Both recur across session-search systems; log-level candidates rather than notes until a mechanism is stated.

## Flags

- No split candidate: the source makes one design assertion set (search-then-window over retained transcripts) with ancillary playbooks.
- Tension worth preserving in the ingest: Recall is evidence *for* the capture/loading split but *against* the strong reading of raw-accumulation-does-not-create-usable-memory for episode-recall tasks; record both without resolving.
- Evidence tier: the snapshot contains only the skill instructions; the engine is private, so every mechanism claim (entity index, evidence gate, redaction) is documentation-level, not code-grounded. Connections should be phrased as "bears on", not corroboration.
