---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/open-domain-memory-retention-needs-a-declared-output-spec.md"
source_has_frontmatter: true
date: "2026-07-17"
depth: standard
---

# Connection Report: Open-domain memory retention needs a declared output spec

**Source:** [Open-domain memory retention needs a declared output spec](../../../../notes/open-domain-memory-retention-needs-a-declared-output-spec.md)

Source claim: in an open domain, an inclusion criterion for retention cannot come from the input stream alone; only a *declared output spec* (purpose, scope boundaries, exclusions, quality bar) supplies an auditable criterion. Input-driven vs output-driven contrast table; input-driven fails because gaps are invisible, output-driven fails when the spec drifts. Existing footer edges already author: `distillation-is-transformation-not-selection` (contrasts), `raw-accumulation-does-not-create-usable-memory` (contrasts), `designing-agent-memory-systems` (extends), `definitions/context-engineering` (defined-in).

Authorised outbound from `kb/notes/` (theoretical profile): notes labels `extends`/`grounds`/`enables`/`exemplifies`/`mechanism`/`contradicts`/`contrasts`; `defined-in`→notes/definitions; `evidence`/`derived-from`→reference, agent-memory, agentic-systems, sources; `see-also`→same + instructions (sparingly). Do not link into `kb/work/`. Edges to instructions are rare (usual direction is inverse).

## Discovery Trace

**Description listing scan:**
- Scoped `rg '^tags:.*\bagent-memory\b'` + `context-engineering` over `kb/notes/` (tag-READMEs carry no `complete`/`covered_by` marks, so the by-tag sweep was run) — flagged: `kb-goals-in-always-loaded-context-guide-inclusion-decisions`, `elicitation-requires-maintained-question-generation-systems`, `evaluate-memory-by-effects`, `promote-only-when-value-exceeds-cost`, `knowledge-storage-does-not-imply-contextual-activation`, `three-space-agent-memory`, `agent-memory-needs-discoverable-composable-trusted-knowledge`. Already-linked notes (raw-accumulation, designing-agent-memory-systems, context-engineering) excluded from re-proposal.
- `rg '^description:'` over `kb/notes/definitions/` — no definition names "output spec"/"inclusion criterion"; `distillation`, `context-engineering` (already linked), `retained-artifact`, `knowledge-artifact` are adjacent but not a term the source uses undefined. No new `defined-in` candidate.

**Topic indexes:**
- `agent-memory-README.md` — source is NOT listed (README is selective). Nearest editorial groups: "Core Frame" and "Boundaries And Failure Modes". Read for routing signal; surfaced kb-goals via cross-tag path.
- `context-engineering-README.md` — source NOT listed; "Core Claims" cluster is where a lifecycle/what-enters-storage note would sit.

**Body search:**
- `rg -i "inclusion criterion|admission criterion|output spec|what to store|retention decision"` over notes → only source + `always-loaded-context-mechanisms` (unrelated) + `tool-loop-README` (unrelated).
- `rg -i "input-driven|output-driven|coverage gap|invisible gap|elicit"` over notes → `elicitation-requires-maintained-question-generation-systems`, `knowledge-storage-does-not-imply-contextual-activation`, `systematic-prompt-variation…`, `prompt-ablation…`. Evaluated: elicitation is a real hit (output-driven audits "drive targeted elicitation"); the prompt-variation notes are about review probes, not retention criteria — rejected.
- `rg -i "quality bar|goals section|declared purpose|declared spec"` over notes → `kb-goals-in-always-loaded-context-guide-inclusion-decisions` (strong: literally KB-goals-as-inclusion-criterion), `technical-constraints-make-kb-objective-choice-engineering`, `a-knowledge-base-holds-theories-descriptions-and-prescriptions`. First is the standout.
- `rg -i "output spec|inclusion|retention|coverage|admission|quality bar"` over `kb/reference/` → `agent-memory-coverage`, `control-plane-goals`, `commonplace-agent-memory-gap-plan` among others. Read heads: coverage is a worked requirements→realization→gaps audit; control-plane-goals is the shipped goals-as-spec realization.
- `rg -i "no.{0,10}spec|automatic.{0,15}captur|watches session|salience|what to store"` over `kb/agent-memory-systems/reviews/` → `virtual-context` (automatic trace capture), `hindsight`/`smriti-mcp` (salience-driven capture) as input-driven exemplars.

**Link following:**
- From `kb-goals-in-always-loaded-context…` one hop: it already links `raw-accumulation` (grounds) and `control-plane-goals` (current-state) — confirms kb-goals is the KB-authoring specialization of the source's general principle, and that `control-plane-goals` is reached through it.
- From `evaluate-memory-by-effects` one hop: links `designing-agent-memory-systems` (already the source's extends anchor) — the "Evidence sufficiency / coverage" dimension is the audit surface the source names.

## Connections Found

- [kb-goals-in-always-loaded-context-guide-inclusion-decisions](../../../../notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) — **extends**: source connects to it because kb-goals develops the same inclusion-criterion argument in the KB-authoring direction — where the output spec must live (always-loaded control plane), how it decomposes (purpose / scope / out-of-scope list / quality bar), and how it is revised. It is the fullest worked instance of "a declared spec makes 'does this belong?' answerable." (See Flags: the reverse direction — kb-goals `exemplifies` this source — is arguably the primary edge; a writer should pick one.)
- [elicitation-requires-maintained-question-generation-systems](../../../../notes/elicitation-requires-maintained-question-generation-systems.md) — **enables**: source connects to it because the source's output-driven mode ("declare need, elicit, fill"; "output-driven audits … drive targeted elicitation") and its Open Question 1 ("how should the output spec itself be kept current?") both need machinery the source does not build — and this note supplies it: a maintained question-generation loop (seed / enforce / log-misses / distill / prune) that keeps a coverage spec current instead of ossifying.
- [evaluate-memory-by-effects](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — **enables**: source connects to it because the source's claim that "gaps are checkable against the spec" needs an evaluation surface, and this note supplies it — the Evidence-sufficiency / coverage and Contract-fitness dimensions are exactly the output-driven audit the source describes at retention granularity. (Moderate; partly reached through the existing `designing-agent-memory-systems` extends anchor — a writer may judge it redundant.)
- [agent-memory-coverage](../../../../reference/agent-memory-coverage.md) — **evidence**: source connects to it because the coverage map is a worked output-driven audit in the shipped system — declared requirements as the spec, realization as what is served, "current limit" column as the checkable gaps — corroborating that a declared spec makes gaps auditable rather than invisible.
- [control-plane-goals](../../../../reference/control-plane-goals.md) — **evidence**: source connects to it because it documents the shipped `## KB Goals and Scope` output spec (purpose / scope / quality bar in always-loaded context), corroborating the source's practice claim that "this KB's own Goals section is an output spec." (Moderate; largely reached through the kb-goals note, which already owns this edge — consider whether a direct edge adds traversal value.)
- [virtual-context](../../../../agent-memory-systems/reviews/virtual-context.md) — **evidence**: source connects to it because virtual-context's write path is automatic trace capture/tagging/compaction with no declared retention spec — a concrete input-driven system corroborating the "accumulates whatever happens to come up" pole. (Weak-moderate: writer should confirm from the review that coverage gaps are in fact unsignalled, not merely that capture is automatic. `hindsight` and `smriti-mcp` are additional salience-driven input-driven exemplars if a second witness is wanted.)
- [What the matrix shows across 148 agent memory systems](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) — **evidence**: source connects to it because the review's "Capture and push usually travel together" finding empirically splits 148 real systems into an automatic camp (trace-learn + push, 81/148) and a curated pull-only camp (35/148, "does not mine traces and waits to be asked") — a stronger, aggregate-scale witness of the same input-driven/output-driven split than any single system review, and its "For us" section frames Commonplace's own posture ("authored, files-family, review-heavy... keeping durable memory authored") in exactly the source's output-driven terms. Consider this instead of, or alongside, the weaker single-system `virtual-context` evidence above.
- [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) — **extends**: source connects to it because that note's "Capture policy" axis row lists only input-driven choices ("write everything, heuristic trigger, LLM curator, user-marked item, post-session mining") — the source names and argues for the missing output-driven option ("declare need, elicit, fill") that row omits, situating the source's claim inside the fuller six-axis operational-memory framework that note establishes.

## Bidirectional Candidates

- [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) <-> source — **mechanism** (return path): a reader of that note's Capture policy row who wants to understand *why* the listed choices split the way they do, rather than just enumerating them, gains the source's input-driven/output-driven mechanism.

- [kb-goals-in-always-loaded-context-guide-inclusion-decisions](../../../../notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) <-> source — **exemplifies** (return path): a reader of kb-goals wanting the general principle behind "every write is an inclusion decision" gains the source's open-domain output-spec argument; the KB-goals case is one instance of it. See Reverse-edge Candidates and Flags for the direction question.

## Reverse-edge Candidates

- [kb-goals-in-always-loaded-context-guide-inclusion-decisions](../../../../notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) → source — **exemplifies**: under `kb/notes/` rules, kb-goals (a KB-authoring special case) can author an `exemplifies` edge to this source as the general claim it instantiates. This is arguably the more natural primary edge than the outbound `extends` above; a future connect run on kb-goals should surface it.
- [Evaluate a log entry for note creation](../../../../instructions/evaluate-log-entry-for-note-creation.md) → source — **rationale**: this instruction's five novelty tests (delta, mechanism, compression, traversal, prediction) are a concrete output-driven admission procedure for one specific case (promoting a `kb/log.md` entry to a note). Weaker fit than the kb-goals edge: the instruction operates one step downstream of the source's claim (evaluating candidates already captured in the log, not what enters the log itself), so this is real but not central — flagging for the instruction's author to judge, consistent with `kb/notes/COLLECTION.md`'s note that outbound edges into `kb/instructions/` are rare and usually run the other way (`instruction → note` via `rationale`).

## Off-authorisation Candidates

None — every kept candidate maps to an authorised label for its source→destination pair.

## Raw Text Candidates

None — all candidates carry frontmatter.

## Rejected Candidates

- [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — about *activation* (making stored knowledge action-relevant), which the source explicitly scopes out ("knowledge lifecycle — what enters storage — is one determinant" vs activation). Different lifecycle stage; linking would blur the admission/activation distinction the source relies on.
- [promote-only-when-value-exceeds-cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) — about the *value-vs-maintenance-cost* threshold for promoting candidates, a different axis from *where the inclusion criterion comes from*. Keyword overlap on "retain/promote" only.
- [the-second-brain-trap](../../../sources/the-second-brain-trap-2041486539067154753.md) — argues stored notes fail when they never *activate*; that is the activation failure mode, not the missing-inclusion-criterion one.
- [the-price-of-meaning-why-every-semantic-memory-system-forgets](../../../sources/the-price-of-meaning-why-every-semantic-memory-system-forgets.md) — interference-driven *forgetting/false recall* under finite dimensionality; a retrieval/capacity failure, not an admission-criterion argument.
- [how-we-built-our-knowledge-base](../../../sources/how-we-built-our-knowledge-base-2077822555159945507.md) (untracked) — a practitioner report on retrieval architecture (semantic search, planner pass, scoped projects); does not discuss what-to-store inclusion criteria. Not relevant to this claim.

## Index Membership

- [agent-memory-README](../../../../tags/agent-memory-README.md) — the source is a genuine agent-memory claim carrying the tag but is not in the selective curated head; a writer could add it under "Core Frame" (it frames a retention-design determinant) or "Boundaries And Failure Modes" (it separates two criterion sources with distinct failure modes). connect does not add the entry.
- [context-engineering-README](../../../../tags/context-engineering-README.md) — likewise tagged but unlisted; "Core Claims" is the fit (knowledge-lifecycle / what-enters-storage as a context-engineering determinant).

## Synthesis Opportunities

The source, `elicitation-requires-maintained-question-generation-systems`, and `evaluate-memory-by-effects` together suggest a higher-order claim not yet captured: *a declared need is the shared prerequisite for auditable coverage across the memory lifecycle* — the same "criterion must come from a declared spec, not from the incoming stream / stored existence" move recurs at admission (this source), at elicitation (probes vs undirected review), and at evaluation (effects vs existence). Worth considering for later promotion; do not author during connect.

## Maintenance Observations

- Two selective tag-READMEs (`agent-memory-README`, `context-engineering-README`) omit this source although it carries both tags — expected for selective heads, noted only so a maintenance pass can decide on inclusion. Not a defect.
- Overlapping ownership signal: the source's practice paragraph, `kb-goals-in-always-loaded-context…`, `control-plane-goals`, and `agent-memory-coverage` all speak to "declared goals/spec make inclusion/coverage auditable." No contradiction, but a maintainer should confirm the general claim lives in one note (this source) with the others as instances/realizations, to avoid the argument fragmenting across four artifacts.

## Flags

- **Direction decision (not a split):** the kb-goals relationship is legitimately authorable both ways — source `extends`→ kb-goals (outbound) or kb-goals `exemplifies`→ source (reverse). The reverse edge is arguably primary (kb-goals is the special case, source is the general claim). A writer should author one direction, not both, and prefer the reverse if forced to choose.
- Source makes essentially one assertion across one topic area — not a split candidate.
