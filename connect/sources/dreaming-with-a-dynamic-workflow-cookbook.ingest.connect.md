---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/dreaming-with-a-dynamic-workflow-cookbook.ingest.md"
source_has_frontmatter: true
date: "2026-11-07"
depth: standard
---

# Connection Report: Ingest: Dreaming with a dynamic workflow

**Source:** [Ingest: Dreaming with a dynamic workflow](../../../../sources/dreaming-with-a-dynamic-workflow-cookbook.ingest.md)

## Discovery Trace

**Linking rules read:** `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `kb/work/` and `kb/instructions/` excluded. Labels: `is-evidence-for` (theory, agent-memory-systems), `rests-on` / `abstracted-from` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). External prospecting skipped (no external targets supplied; the source URL is already the `source` field).

**Existing outbound links verified (all exist):** components-of-agent-memory.ingest, retaining-episode-evidence…, trace-extracted-memory-earns-authority…, agent-orchestration-needs-coordination-guarantees…, retire-redact-supersede-relax, llm-context-interprets-instructions-and-content…, claude-code-dynamic-workflows review, karpathy-llm-wiki.ingest, language-models-need-sleep….ingest, theory-builder, addressable-theory, learning-inside-a-fixed-decomposition…, evaluate-memory-by-effects. Candidates below exclude these.

**Topic indexes:**
- `kb/tags/agent-memory-README.md` (not `complete: true`) -- flagged Preserve Evidence Without Making History The Next Context, Make Authority Explicit, Keep Compiled Views Aligned, Raw accumulation does not create usable memory, Memory management policy is learnable but oracle-dependent.
- `kb/tags/trace-learning-README.md` (not `complete: true`) -- flagged trace-learning-techniques-in-related-systems, memwiki, REM; pointed to Letta/Cludebot via body search below.

**Body search:**
- `rg -l -i 'consolidat|dream|sleep-time|offline memory|nightly' kb/theory kb/agentic-systems kb/agent-memory-systems kb/sources kb/reference` -- ~60 hits, too broad; narrowed.
- `rg -l -i '\bdream' kb` -- relevant: use-trace-extraction-as-meta-learning (cites Cludebot dream-cycle), cludebot review, components-of-agent-memory ingest, language-models-need-sleep ingest; others (DreamCoder, DreamTeam, Sutskever list, MDL) are name collisions, rejected.
- `rg -l -i 'sleep-time|sleeptime' kb` -- letta review, continual-learning-in-token-space ingest, Zikkaron review.
- `rg -l -i 'offline (memory )?consolidat|consolidation (pass|step|job)' kb/theory kb/sources kb/agentic-systems` -- automating-kb-learning-is-an-open-problem, trajectory-informed-memory-generation ingest.
- `rg -l -i 'managed agents' kb` -- scaling-managed-agents-decoupling-brain-from-hands ingest, the-log-is-the-agent ingest, from-harness-lock-in ingest.
- `rg -n -i 'dream|cookbook' kb/sources/components-of-agent-memory.ingest.md kb/theory/retaining-episode-evidence-…md` -- neither links back to this ingest yet.
- Theory title scan: `rg -N --no-heading -m1 '^# ' kb/theory | rg -i 'inject|untrusted|parallel|concurren|writer|merge|consolidat|unattended|oracle|verif|stale|always-loaded|index'` -- flagged Unattended work needs the functions that interaction supplied, Session history should not be the default next context, Oracle strength spectrum, Error correction works above chance with decorrelated checks.

**Link following:**
- use-trace-extraction-as-meta-learning -> Cludebot review (dream-cycle authority risk, line 129) and trace-learning-techniques comparison.
- preserve-evidence-without-loading-history -> session-history-should-not-be-the-default-next-context (capture/loading split).
- letta review lines 27/46/72: sleeptime agents edit shared blocks from transcripts; review recommends background memory agents only inside workshops.
- agent-memory-systems COLLECTION.md: collection is frozen, so reverse edges from its reviews are not proposed.

## Connections Found

- [Use trace extraction as meta-learning](../../../../theory/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) -- **is-evidence-for**: the recipe implements the requirement's "evolution, not only creation" operation (Verify/Enrich/Organize revises existing memory against each new transcript) while failing its signal-quality condition: corrections, process lessons and passing remarks all land in the store with the same unmarked authority and no review queue.
- [Preserve evidence without making history the next context](../../../../theory/agent-memory-requirements/preserve-evidence-without-loading-history.md) -- **is-evidence-for**: the recipe gets the loading half right (transcripts are opened by a read tool, never the consumer's context) but defaults to deleting sessions and writing records to a temp directory, a concrete vendor case of losing the capture half the requirement asks for.
- [Unattended work needs the functions that interaction supplied](../../../../theory/unattended-work-needs-the-functions-that-interaction-supplied.md) -- **is-evidence-for**: the nightly cron removes the operator and replaces only some of their functions (read-back checks, thread-record count of analyzed transcripts, report of where the run differed from the request) while leaving review absent by default; a worked case of which interactive functions an unattended consolidation does and does not replace.
- [Keep lineage and compiled views from drifting](../../../../theory/agent-memory-requirements/keep-compiled-views-aligned.md) -- **is-evidence-for**: `_index.md` is a generated view that may be loaded into the consumer's `instructions`, and the recipe names the risk that injected text there could "steer every session"; this bounds when an always-loaded compiled view is safe.
- [Letta review](../../../../agent-memory-systems/reviews/letta.md) -- **compares-with**: on unattended background consolidation from transcripts; Letta's sleeptime agents edit shared core blocks after foreground turns, this recipe runs a nightly batch over a file store; both write directly to consumed memory without a review state, and the Letta review's "only inside workshops" recommendation applies to both.
- [Cludebot review](../../../../agent-memory-systems/reviews/cludebot.md) -- **compares-with**: on scheduled "dream" consolidation; Clude dreams over stored memory records with evidence ids and contradiction resolution, this recipe dreams over raw transcripts with `CONFLICT:` lines; the review's "authority-risky" finding is the same gap the ingest names for Verify.
- [Scaling Managed Agents: decoupling brain from hands](../../../../sources/scaling-managed-agents-decoupling-brain-from-hands.ingest.md) -- **compares-with**: on durable session records; that report presents durable session logs as a Managed Agents design pillar, while this recipe on the same platform deletes sessions by default after consolidation, so a reader judging what the platform retains needs both.

## Bidirectional Candidates

- [The components of agent memory](../../../../sources/components-of-agent-memory.ingest.md) <-> source -- **compares-with**: this ingest already links there as its main counterpart; the components ingest does not link back, and a reader of the evaluated Mt. Moon correction would want the executable recipe (and its default transcript deletion) on the same evaluated-vs-shipped axis.

## Reverse-edge Candidates

- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) → source -- **evidenced-by**: the ingest's own Recommended Next Action; the recipe is a bounding contrast to the cited Mt. Moon case (transcripts are the Verify oracle yet are discarded by default). Context phrase should say it qualifies/bounds the claim, not corroborates it. Note is currently modified in the working tree; coordinate.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) → source -- **evidenced-by**: Verify is one automated rung with a weak oracle (small model vs one transcript) whose granted authority is not recorded per fact; bounds the claim.
- [Retire, redact, supersede, and relax memory](../../../../theory/agent-memory-requirements/retire-redact-supersede-relax.md) → source -- **evidenced-by**: concrete operating markers (dated supersession, `CONFLICT:`, `MOVED TO` stubs, version redaction) for the lifecycle operations.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../theory/agent-orchestration-needs-coordination-guarantees-not-just.md) → source -- **evidenced-by**: the parallel-analyzer/single-organizer split states its consistency guarantee explicitly (re-read, targeted edits, read-back, link-not-merge, deferred merges).

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Raw accumulation does not create usable memory](../../../../theory/raw-accumulation-does-not-create-usable-memory.md) -- the recipe does the ingress work the note asks for, but adds nothing the note lacks; would be confirmation-only.
- [Make authority explicit](../../../../theory/agent-memory-requirements/make-authority-explicit.md) -- read-only mounts and file-only tools are authority settings, but the per-operation authority point is already carried by the trace-extracted-memory link; redundant.
- [Session history should not be the default next context](../../../../theory/session-history-should-not-be-the-default-next-context.md) -- reached via preserve-evidence; the recipe conforms but provides no test of the claim; preserve-evidence is the sharper target.
- [Automating KB learning is an open problem](../../../../theory/automating-kb-learning-is-an-open-problem.md) -- topical (automated consolidation) but the note concerns oracles for connections/groupings/synthesis in a KB; the recipe's organizer merges without any such oracle, yet shows no outcome either way. Weak.
- [Oracle strength spectrum](../../../../theory/oracle-strength-spectrum.md), [Error correction works above chance with decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- Verify's oracle is weak, but the recipe gives no measured TPR/FPR; keyword-level fit.
- [Continual learning in token space](../../../../sources/continual-learning-in-token-space.ingest.md) -- Letta sleep-time framing; the Letta review is the stronger, code-grounded comparison target.
- [Trajectory-informed memory generation](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) -- trace-to-tips pipeline with a task-completion oracle; plausible compares-with on evaluation, but the components ingest already carries the evaluated-vs-shipped axis. Hold.
- [The log is the agent](../../../../sources/the-log-is-the-agent-2065129901427130678.ingest.md) -- opposite posture on logs, but an essay without mechanism; scaling-managed-agents is the same-platform comparison.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- frozen historical comparison; sources cannot be added to it, and a link from the ingest adds only a catalogue pointer.
- DreamCoder, DreamTeam (workspace-optimization), Sutskever list, MDL ingests -- "dream" name collisions.

## Index Membership

- [agent-memory tag head](../../../../tags/agent-memory-README.md) and [trace-learning tag head](../../../../tags/trace-learning-README.md) -- the ingest already carries both tags; sources are outside participating collections, so no head entry is expected.

## Synthesis Opportunities

Letta sleeptime, Cludebot dream cycles, the components-of-agent-memory Mt. Moon case and this recipe are four offline-consolidation designs that differ on two axes: whether the episodes the consolidator checks against are retained, and whether consolidated output reaches the consumer through a review state. Only the evaluated Mt. Moon case kept the transcript as a re-checkable oracle; none of the shipped designs has a default review. A comparison along these axes could test the retaining-episode-evidence note's prediction that discarding episodes limits later criticism to claims a new episode happens to touch.

## Maintenance Observations

- The components-of-agent-memory ingest and this ingest are a counterpart pair but the edge is one-way (see Bidirectional Candidates).

## Flags

- Reverse edge to retaining-episode-evidence coincides with an uncommitted working-tree edit of that note; coordinate before authoring.
