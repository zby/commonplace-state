---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/skill-discovery-re-fires-in-every-sub-agent-context.md"
source_has_frontmatter: true
date: "2026-07-06"
depth: standard
---

# Connection Report: Skill discovery re-fires in every sub-agent context

**Source:** [Skill discovery re-fires in every sub-agent context](../../../../notes/skill-discovery-re-fires-in-every-sub-agent-context.md)

The source already carries five footer links (`skills-are-instructions-plus-routing-and-execution-policy` extends, `llm-context-is-composed-without-scoping` extends, `topology-isolation-and-verification-form-a-causal-chain-for-reliable` extends, `session-history-should-not-be-the-default-next-context` contrasts, `write-agent-memory-system-review/SKILL.md` see-also). Those are excluded from Connections Found below and treated only for return-edge purposes.

## Discovery Trace

**COLLECTION.md outbound rules read:** `kb/notes/COLLECTION.md`. Authorised note-destination labels: `extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts`, `defined-in`. Reference/agent-memory/agentic-systems/sources: `evidence`, `derived-from`, `see-also`. Instructions: `see-also` only, and the usual direction is inverse (`instruction → note` via `rationale`). Do not link into `kb/work/`. Source has empty `tags: []`, so no tag-README shortcut was available.

**Description listing scan:**
- `rg '^description:' kb/notes/` filtered on skill/sub-agent/delegate/context/isolation/harness/discover/invocation/leak/worker/scoping/orchestrate/frontload -- surfaced the always-loaded, capability-placement, instruction-specificity, feasibility, fix-what-the-executor, and agent-statelessness notes as leading candidates.

**Topic indexes:**
- Read `always-loaded-context-mechanisms-in-agent-harnesses.md` head + "Capability descriptions" section -- documents skill descriptions as always-*listed* menu items whose bodies load on demand. This is the exact premise the source relies on ("the harness advertises the whole skill menu regardless of what the parent chose to pass"). Kept.
- `computational-model-README.md` scanned as an index membership candidate (source is skills/sub-agent/scheduling territory).

**Body search:**
- `rg '20%|~100%|slash command|reliably trigger|autonomous.*rout'` -- confirmed the `~20%` routing figure lives only in the already-linked `skills-are-instructions-plus-routing-and-execution-policy`; no new target.
- `rg 'always-advertised|capability description|capability listing|advertise'` -- hits: skills-are-instructions (linked), always-loaded-context-mechanisms (kept), capability-placement (kept), agents-md-should-be-organized-as-a-control-plane (rejected, control-plane framing not about the leak), agent-context-is-constrained-by-soft-degradation (rejected).
- `rg 'task text|task string|task prompt|worker'` -- hits: fix-what-the-executor-cant-determine (kept: worker task text == orchestrator task prompt), session-history (already linked), symbolic-context-engineering (rejected).

**Link following:**
- From `capability-placement` footer -> `agents-md-should-be-organized-as-a-control-plane` and `skills-are-instructions` (latter already linked). Control-plane note is about AGENTS.md inventory placement, not the sub-agent discovery leak -- no new edge.
- Checked all five existing targets and the delegating SKILL.md for return links to the source: none exist yet (see Bidirectional / Reverse-edge sections).

## Connections Found

- [always-loaded-context-mechanisms-in-agent-harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- **grounds**: its "Capability descriptions" section establishes that skill descriptions are always *listed* (bodies load on demand) as a harness-injected always-loaded surface — the exact premise the source builds on when it claims the harness "advertises the whole skill menu regardless of what the parent chose to pass." A reader doubting that premise verifies it here. **Load-bearing-label flag:** `grounds` is load-bearing and the *target* is `status: seedling`; confirm the survey actually asserts always-listed-in-every-context (it documents always-listed, but does not itself assert re-firing in sub-agent contexts — that gap is the source's contribution) before committing this as `grounds` rather than `extends`.

- [capability-placement-should-follow-autonomy-readiness](../../../../notes/capability-placement-should-follow-autonomy-readiness.md) -- **extends**: capability-placement routes an autonomy-ready capability to the **skills** tier precisely for autonomous discovery/injection; the source adds an unstated cost of that top tier — autonomous discovery re-fires inside any sub-agent the skill's own procedure spawns, so promoting a delegating procedure to a skill leaks its own trigger into the worker. Develops the placement argument with a caveat on its top tier.

- [fix-what-the-executor-cant-determine-not-what-it-will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **extends**: that note treats "the task prompt an orchestrator hands a subagent" as an authored-before-execution artifact whose job is to fix only what the executor can't determine. The source's mitigation #2 is a concrete new obligation on that same surface — the worker *cannot* determine on its own that an auto-loaded skill resembling its brief is a trap, so the author must fix that in the task text. Extends the task-prompt-authoring argument with the inoculation case. (Alternative label `exemplifies` if the source is read as an instance of the general fix-what rule rather than a development of it.)

## Bidirectional Candidates

- [skills-are-instructions-plus-routing-and-execution-policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) <-> source -- **extends**: the source is already linked outbound as the "missing entry (cost of the structured-discovery affordance)" in that framework. A return link from the framework note to the source is worth adding so a reader of the framework reaches the documented cost, closing the pair. (Return edge would be authored from the framework note in a future edit; connect does not write it.)

## Reverse-edge Candidates

- [write-agent-memory-system-review/SKILL.md](../../../../instructions/write-agent-memory-system-review/SKILL.md) → source -- **rationale**: the SKILL.md now carries the reactive mitigation in its worker task text, but authors no link explaining *why*. Per `kb/notes/COLLECTION.md` the usual note↔instruction direction is inverse (`instruction → note` via `rationale`), so the natural durable edge is a `rationale` link from the SKILL to this note. The source already points *at* the SKILL as see-also; the return `rationale` edge is unwritten. Authorable only under the instructions collection's own rules — surfaced here, not written.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [instruction-specificity-should-match-loading-frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md) -- shares the "skill descriptions are always-loaded" premise, but its argument is specificity-vs-loading-frequency, not per-context re-firing. Topical overlap without a concrete traversal gain; following the link teaches nothing the source needs.
- `agent-statelessness-makes-routing-architectural-not-learned` -- lists skills and activation triggers as permanent routing architecture; too general, no purchase on the sub-agent leak mechanism.
- `feasibility-is-the-heaviest-forks-net-load` -- concerns sub-agent decomposition but on the token-feasibility axis, unrelated to discovery-surface leakage.
- `agents-md-should-be-organized-as-a-control-plane` / `agent-context-is-constrained-by-soft-degradation` -- surfaced on "advertise"/"capability" keyword hits but address AGENTS.md inventory and soft-degradation respectively, not always-advertised skill matching.

## Index Membership

- [computational-model-README](../../../../tags/computational-model-README.md) -- the source is a skills/sub-agent/scheduling-substrate claim and would fit the computational-model tag's editorial scope. Membership is blocked today because the source carries `tags: []` (see Maintenance Observations); a future writer would tag it and could then add the curated entry.

## Synthesis Opportunities

None. The three kept candidates are additive developments, not a latent higher-order claim beyond the source's own.

## Maintenance Observations

- **Source carries no tags (`tags: []`).** It therefore appears in no `<tag>-README.md` and is invisible to by-tag `rg` discovery — a real discoverability gap for a `structured-claim` note. Candidate tags by content: `computational-model` (skills, sub-agents, scheduling substrate) and/or `architecture` (harness discovery surface). Tagging is a source-side edit outside connect's scope; flagged for a later maintenance pass.
- The delegating `write-agent-memory-system-review/SKILL.md` mitigation and this note are a tight bidirectional pair (source see-also → SKILL; SKILL rationale → source unwritten). Worth a single maintenance pass to author the inverse `rationale` edge so the mitigation's justification is one hop away.

## Flags

- One kept candidate (`always-loaded-context-mechanisms`) is proposed with the load-bearing `grounds` label against a `status: seedling` target — resolve `grounds` vs `extends` when authoring (see the inline flag in Connections Found).
- Not a split candidate: the source makes one claim (per-context re-firing of discovery) and the kept candidates cluster in one topic area (skills / sub-agent isolation).
