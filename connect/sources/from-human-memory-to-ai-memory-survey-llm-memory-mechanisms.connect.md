---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.md"
source_has_frontmatter: true
date: "2026-06-09"
depth: standard
---

# Connection Report: From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs

**Source:** [From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](../../../sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.md)

This source is an **immutable snapshot** under `kb/sources/`. The source `COLLECTION.md` states the authoring signal for a snapshot is reverse-edge: which library notes should add `evidence`/`derived-from` links pointing at this snapshot. There is no `.ingest.md` companion yet, so this snapshot currently has no authored outbound surface; the `Connections Found` section below is therefore framed as recommendations for a future ingest report, and the load-bearing signal lives in `Reverse-edge Candidates`.

The source is a Huawei Noah's Ark survey proposing a **3D-8Q taxonomy** for LLM memory: three dimensions — *object* (personal vs system), *form* (parametric vs non-parametric), *time* (short- vs long-term) — crossed into eight quadrants, each mapped to a human-memory type (sensory, working, episodic, semantic, procedural). It is a landscape/paper-grade source with no inspectable repo, so it parallels the collection's lightweight-coverage tier rather than a code-grounded review.

## Discovery Trace

**Index scan:**
- Read [agent-memory-systems README](../../../../agent-memory-systems/README.md) and [agent-memory dir-index](../../../agent-memory-systems/dir-index.md) -- flagged the four-field review vocabulary (storage substrate / representational form / lineage / behavioral authority) and the [comparative review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) as direct conceptual parallels to the survey's form/object/time taxonomy. Noted the [lightweight coverage tier](../../../agent-memory-systems/lightweight/dir-index.md) as the structural analogue for a paper-only system.
- Scanned `kb/notes/` via concept-targeted `rg` rather than the full flat dir-index, since the survey's claims are concept-shaped (memory taxonomy, parametric/non-parametric) not title-matchable.

**Topic indexes:**
- Source carries only `tags: [academic-paper]`, which has no topic index. Used `learning-theory` / `agent-memory` tagged notes surfaced by body search instead.

**Body search:**
- `rg -li "parametric|kv.?cache|episodic|procedural memory|forgetting|consolidat" kb/notes/` -- returned ~40 notes; the discriminating hits were [three-space-tulving](../../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md), [psychology-to-agent-transfer](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md), [axes-of-artifact-analysis](../../../../notes/axes-of-artifact-analysis.md), [memory-design-adds-operational-axes](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md), [continual-learning-open-problem](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md), [deploy-time-learning](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), and the definition notes for [representational-form](../../../../notes/definitions/representational-form.md) and [storage-substrate](../../../../notes/definitions/storage-substrate.md).
- `rg -li "tulving|conway|cognitive science|human memory" kb/notes/` -- confirmed the human-memory-to-agent mapping cluster centers on the Tulving note and the psychology-transfer note; [llm-learning-phases-fall-between-human-learning-modes](../../../../notes/llm-learning-phases-fall-between-human-learning-modes.md) is adjacent (it is referenced as Component 2 of the transfer methodology).
- `rg -li "shared memory|collective privacy|cross-agent|multi-agent memory|stream memory" kb/notes/` -- the survey's "shared memory" / "collective privacy" future directions found no dedicated note; nearest hits ([agent-orchestration-needs-coordination-guarantees](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md), [make-authority-explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md)) are about coordination/authority, not shared-memory privacy. Recorded as a gap in Flags, not a candidate.
- `rg -l "2504.15965|From Human Memory to AI Memory|3D-8Q" kb/` -- the only other reference is the sibling survey [adaptation-of-agentic-ai](../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.md); no note yet cites this snapshot.

**Link following:**
- From [three-space-tulving](../../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) followed to [flat-memory-predicts...](../../../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) and [memory-management-policy-is-learnable](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md); both sit in the cognitive-analogy-skepticism cluster the survey is evidence in, but they make narrower empirical claims the survey does not directly bear on, so they were not kept.
- From [axes-of-artifact-analysis](../../../../notes/axes-of-artifact-analysis.md) followed to [the-four-field-record-exposes...](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) -- the survey's collective-privacy and parametric-vs-non-parametric discussions touch the security/sovereignty triad, but the survey treats these as future directions rather than evidence for the triad, so it is a weak fit (see Rejected).

## Connections Found

These are recommendations for a **future ingest report** (`.ingest.md`) authored next to the snapshot; the snapshot itself is never the link author. Labels are from the source `COLLECTION.md` outbound set.

- [three-space-agent-memory-echoes-tulvings-taxonomy](../../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) -- **evidence**: a peer-reviewed-style survey that systematically maps human memory types (sensory/working/episodic/semantic/procedural) onto AI memory, corroborating that the cognitive-taxonomy framing is widespread; the survey's own admission that quadrants reduce to object/form/time policy dimensions supports the note's "the analogy may be decorative" claim. (Target is `status: speculative`; `evidence` is additive/corroborating here, not load-bearing, so the seedling flag is informational.)
- [representational-form](../../../../notes/definitions/representational-form.md) -- **evidence**: the survey's *form* dimension (parametric vs non-parametric) and its explicit statement that the same KV-cache mechanism spans personal and system memory is external corroboration that representation must be separated from substrate and object/role. (Target is `status: current`.)
- [memory-design-adds-operational-axes-to-artifact-analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) -- **evidence**: the survey's four memory-processing stages (construction, management, retrieval, usage) plus consolidation/reflection/forgetting map onto this note's operational axes (capture, derivation, activation, lifecycle), corroborating that artifact-identity fields alone underspecify a memory system. (Target is `status: seedling`; `evidence` is additive.)

## Bidirectional Candidates

None. The snapshot is immutable and carries no authored outbound surface, so there is no return-link to author from the source side; any reciprocal value is captured as `Reverse-edge Candidates`.

## Reverse-edge Candidates

These are the load-bearing signal for a snapshot. Each is a library note that, under `kb/notes/COLLECTION.md` rules, could author an `evidence` link **to** this snapshot. Connect does not edit them.

- [three-space-agent-memory-echoes-tulvings-taxonomy](../../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) → source -- **evidence**: strongest reverse edge. The note already cites a single tweet for the Tulving-mapping claim; this survey is a second, paper-grade instance making the same human-taxonomy-to-agent-memory move, and its self-reduction to object/form/time dimensions is direct support for the note's "decorative analogy" hedge.
- [psychology-to-agent-transfer-needs-per-principle-failure-mode-testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) → source -- **evidence**: the note's thesis is that cognitive-science analogies (Tulving, Conway) need per-principle failure-mode testing rather than wholesale transfer; this survey is a large worked example of exactly the wholesale-mapping move the note warns against, supplying additional test cases (consolidation, reconsolidation, reflection, forgetting → AI mechanisms).
- [axes-of-artifact-analysis](../../../../notes/axes-of-artifact-analysis.md) → source -- **evidence**: the note's *representational form* axis (prose/symbolic/distributed-parametric) and its insistence that substrate ≠ form has an external parallel in the survey's *form* dimension (parametric/non-parametric); the survey is corroborating field evidence that a form axis is recognised independently.
- [continual-learning-open-problem-is-behaviour-not-knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) → source -- **evidence**: the survey's quadrant-VI (procedural/reflection-and-refinement, e.g. Reflexion, Voyager, ExpeL) and quadrant-VIII (parametric knowledge editing, e.g. WISE, MemoryLLM) populate exactly the note's two behaviour-change mechanisms (readable system-definition artifacts vs distributed-parametric updates), giving the note a survey-level catalogue of instances.
- [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) → source -- **evidence**: the comparative review classifies 129 systems on substrate/lineage/authority/activation; this survey independently classifies the same field on object/form/time and reaches a compatible "storage label predicts little" conclusion (the survey notes parametric short-term personal and system memory "overlap technically" and differ only by focus). The review could cite the survey as external corroboration that the discriminating axis is not storage form. (Note: the review lives in `kb/agent-memory-systems/`, whose own COLLECTION.md governs whether it authors source links; flagged as candidate only.)

## Off-authorisation Candidates

None. Every kept candidate's purpose is corroboration of an existing claim, which the `evidence` label covers; no candidate required a label outside the source's authorised set.

## Raw Text Candidates

None. All candidate targets carry frontmatter.

## Rejected Candidates

- [the-four-field-record-exposes-an-efficiency-security-and-sovereignty](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) -- the survey's collective-privacy future direction grazes the sovereignty/security concern, but the survey raises it as an open problem, not as evidence for the triad's existence; too weak for `evidence`.
- [memory-management-policy-is-learnable-but-oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- the survey mentions Reflective Memory Management (RL-trained) and the Ebbinghaus-curve forgetting in MemoryBank, but it does not make the oracle-dependence argument; the overlap is keyword-level (RL, forgetting), not claim-level.
- [deploy-time-learning-is-the-missing-middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- the survey's static-vs-stream-memory direction is timing-adjacent, but the survey does not articulate the training/in-context/deploy-time middle; the note's claim is sharper than anything the survey supports, so the survey is not evidence for it.
- [flat-memory-predicts-specific-cross-contamination-failures](../../../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) -- the survey advocates comprehensive/collaborative memory but does not predict or test cross-contamination failure modes; no claim-level support.

## Index Membership

- The survey is a paper-only landscape source with no inspectable repo. If a stable place in the agent-memory collection is wanted, the collection's lightweight-coverage path applies: run `/ingest` and optionally add a doc-grounded note under [agent-memory-systems/lightweight/](../../../agent-memory-systems/lightweight/dir-index.md). Connect does not create that entry; this is a routing observation for a future writer.
- [kb/sources/dir-index.md](../../../sources/dir-index.md) -- auto-generated; will pick up the snapshot on next `commonplace-refresh-indexes`. No manual membership edit needed.

## Synthesis Opportunities

The survey, the sibling [adaptation-of-agentic-ai survey](../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.md), and the [comparative review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) each propose a different top-level memory taxonomy (object/form/time; agent-vs-tool adaptation A1/A2/T1/T2; substrate/lineage/authority/activation) and each independently concludes that storage form/format under-determines the consequential design choices. A higher-order note on "competing memory taxonomies converge on form-is-not-the-fork" is implied, but [memory-design-adds-operational-axes](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) and [the-four-field-record](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) already cover much of that ground. Flagged for a future writer to judge whether a dedicated cross-taxonomy synthesis adds anything; do not author during connect.

## Maintenance Observations

- The survey's future-directions section names "shared memory" and "collective privacy" (multi-agent / cross-domain memory sharing and group-level privacy). No KB note currently addresses memory-sharing privacy; the nearest notes are about coordination guarantees and authority, not aggregated-data privacy. This is a possible collection-coverage gap, not a connection candidate.

## Flags

- **Split candidate (mild):** the source makes more than one independent assertion (human-memory mapping; object/form/time taxonomy; the four memory-processing stages; future directions) and connects to 4–5 notes across two topic areas (cognitive-analogy skepticism; artifact/operational axes). It is below the strict five-notes/three-areas threshold, so flagged as a mild split only — a future ingest report can cite it from multiple notes without needing to be split.
- **No `.ingest.md` companion exists.** The snapshot has no authored outbound surface. To act on `Connections Found`, a writer must first create the ingest report; until then the load-bearing deliverable is the reverse-edge list.
