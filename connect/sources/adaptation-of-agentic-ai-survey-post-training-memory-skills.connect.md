---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.md"
source_has_frontmatter: true
date: "2026-06-09"
depth: standard
---

# Connection Report: Adaptation of Agentic AI

**Source:** [Adaptation of Agentic AI](../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.md)

This is a regenerated report. The source is an immutable snapshot under `kb/sources/`; its authored connection surface is the companion ingest report [adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md](../../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md). Per `kb/sources/COLLECTION.md`, the load-bearing signal for a snapshot is **reverse-edge**: which library notes should add `evidence`/`derived-from`/`compares-with` links pointing at this source. Since the first report (2026-04-27) the recommended synthesis note has been written and the cluster has grown, so the candidate set has shifted accordingly.

## Discovery Trace

**Collection rules:**
- Read [sources collection rules](../../../../sources/COLLECTION.md). Snapshots are immutable — never authored into. Outbound active surface is the ingest report. Authorised labels (for ingest reports/source reviews): `evidence`, `derived-from`, `rationale` (→ notes); `compares-with` (→ sources, agent-memory); `defined-in` (→ notes/definitions); sparse `see-also`. Do not link into `kb/work/` or `kb/instructions/`. The snapshot itself is never the link author, so the primary deliverable here is reverse-edge candidates plus maintenance observations.

**Index scan:**
- Read [notes index](../../../notes/dir-index.md). The learning-theory / agent-memory / evaluation cluster from the prior report is intact. New since 2026-04-27: subtree `agent-memory-requirements/` and `research/` both contain notes that already engage this survey.
- Read [agent-memory-requirements dir-index](../../../notes/agent-memory-requirements/dir-index.md). Found [The adaptation survey corroborates memory requirements but misses artifact governance](../../../../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) — this is the realized successor of the prior report's "Recommended Next Action", and it already authors an `evidence` link to the ingest report.
- Read [agent-memory-systems dir-index](../../../agent-memory-systems/dir-index.md). Candidate: [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) and [What the matrix shows across 129 agent memory systems](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) — both classify memory/learning by mechanism, parallel to the survey's T1/T2.

**Body search (notes + agent-memory-systems):**
- `rg -i "artifact.substrate|optimization locus|A1.*A2.*T1.*T2|four.paradigm"` → [research/adaptation-agentic-ai-analysis.md](../../../../notes/research/adaptation-agentic-ai-analysis.md) and the agent-memory-requirements corroboration note. Both are existing artifacts that derive from this survey.
- `rg -i "tool adaptation|agent-supervised|frozen agent"` → kept continual-learning, substrate-coevolution, and the two derived notes; rejected broad context-engineering hits.
- `rg -i "post-training|RLVR|verifiable reward|preference optimization"` → continual-learning, memory-policy, readable-artifact-loop notes confirmed as comparison targets.
- `rg -i "co-adapt|coevolution"` → [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md), [Axes of artifact analysis](../../../../notes/axes-of-artifact-analysis.md), [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
- `rg -i "counterfactual|forgetting|retention|dynamics-aware|ablat"` → confirmed the evaluation cluster ([Reliability dimensions map to oracle-hardening stages](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md), [Evaluate memory by effects](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md)).
- `rg -i "skill librar|skill acquisition|skill induction"` → confirmed skill-distillation/routing notes; sibling source [skillopt-...ingest.md](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) present.

**Link following:**
- From [adaptation-survey-corroborates-memory-requirements.md](../../../../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) followed one hop into the memory-requirements cluster (designing-agent-memory-systems, make-authority-explicit, evaluate-memory-by-effects, use-trace-derived-extraction). Confirms the survey's authored landing zone is now this subtree, not the loose top-level notes.
- Confirmed whether any note links the **raw snapshot** directly: none does. Only the corroboration note links the ingest. The `research/` analysis note cites a bare arXiv URL instead of the local artifacts (see Maintenance Observations).

## Connections Found

None to author from the source itself — the source is an immutable snapshot. Candidate outbound edges belong on the ingest report, which already carries the `compares-with`/`evidence` set recorded in the prior report and is unchanged. No new ingest-side outbound edge is required: the two derived notes now carry the cluster.

## Bidirectional Candidates

None. The source cannot author return links (immutable snapshot); the useful return paths are reverse edges below.

## Reverse-edge Candidates

- [research/adaptation-agentic-ai-analysis.md](../../../../notes/research/adaptation-agentic-ai-analysis.md) → source — **derived-from**: this note is an extended analysis of *this exact paper* (it names "arXiv:2512.16301" in its title) but cites only a bare external arXiv URL in its `Sources:` footer. It should author a `derived-from` (or `evidence`) link to the local [ingest report](../../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) so the snapshot is reachable from the note and the note participates in local staleness/lineage tracking. Highest-value reverse edge in this report.
- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) → source — **evidence**: the paper is mainstream confirmation that weight updates, external tools, memory, and skills are coupled adaptation targets, while exposing the KB's missing bridge between ML taxonomy and artifact taxonomy. Carried over from prior report; still unauthored on the note side.
- [Skills derive from methodology through distillation](../../../../notes/skills-derive-from-methodology.md) → source — **compares-with**: the survey's skill-acquisition taxonomy (demonstration, reflection, exploration, RL, programmatic induction) is the broader landscape in which methodology-to-skill distillation is one path. Carried over; still unauthored.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source — **evidence**: the A1/A2 split (execution-signal vs output-signal) is a domain-specific instance of the verification boundary — dense execution rewards enable different adaptation than sparse holistic rewards. Carried over; still unauthored.
- [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) → source — **evidence**: the survey generalizes AgeMem-like systems into T2 and ties learnable memory/tool policies to downstream agent-output or task-completion signals, reinforcing the oracle-dependency claim.

## Off-authorisation Candidates

- [What the matrix shows across 129 agent memory systems](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) and [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — both classify memory/learning by mechanism and would pair well with the survey's T1/T2. `kb/sources/COLLECTION.md` authorises `compares-with` from the ingest report to `agent-memory`, which fits, so these are better authored as `compares-with` edges *from the ingest report* than as evidence edges. Not off-authorisation in the strict sense — flagged here as candidates the ingest report could add if a reviewer wants the agent-memory cross-reference made explicit.

## Raw Text Candidates

None. The `research/adaptation-agentic-ai-analysis.md` note has frontmatter (`type: kb/types/note.md`), so it is a note candidate, not raw text.

## Rejected Candidates

- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) — relevant to the memory section but not specific enough; the paper surveys many adaptive-memory systems and does not centrally argue the ingress-quality thesis.
- [Distillation is transformation, not selection](../../../notes/distillation-is-transformation-not-selection.md) — skill/memory distillation appears throughout, but the paper does not make the shape-change argument this note needs.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — relevant but too broad; the source's distinctive contribution is adaptation taxonomy and evaluation, not context scarcity.
- [skillopt-...ingest.md](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) — a plausible `compares-with` sibling source (self-evolving skills overlaps the survey's T2/skill-library material), but the relationship is topical rather than load-bearing; left for the ingest author to decide rather than asserted here.

## Index Membership

- [Learning theory](../../../notes/learning-theory-index.md) — candidate external source for the adaptation-taxonomy area; bridges weight updates, memory, skills, and tool adaptation.
- [Agent memory](../../../notes/agent-memory-index.md) — candidate source for adaptive memory as T1/T2 tool adaptation.

## Synthesis Opportunities

- The prior report's primary synthesis ("agentic adaptation taxonomies need an artifact-substrate axis") has been realized as [The adaptation survey corroborates memory requirements but misses artifact governance](../../../../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md). No new synthesis note is needed for that thread.
- Open second thread (carried over): "adaptation evaluation must be component-counterfactual and dynamics-aware" — would connect oracle-strength theory, [Reliability dimensions map to oracle-hardening stages](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md), [Evaluate memory by effects](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md), and multi-agent scaling evaluations. Not yet captured as a standalone note.

## Maintenance Observations

- **Stale-prone external citation.** [research/adaptation-agentic-ai-analysis.md](../../../../notes/research/adaptation-agentic-ai-analysis.md) analyses this exact paper but references only a bare `https://arxiv.org/abs/2512.16301` URL in its `Sources:` footer, with no link to the local snapshot or ingest report. The local snapshot exists. This breaks local lineage/staleness tracking for a note that is entirely derived from the source. A maintenance pass should add a local `derived-from`/`evidence` link (see Reverse-edge Candidates).
- **Thin frontmatter on the research note.** `research/adaptation-agentic-ai-analysis.md` carries only `type:` — no `description:`, `status:`, `traits:`, or `tags:`. It would not surface in description/tag scans and may not pass validation's note requirements. Flag for triage; not a connection candidate.
- **Two notes engage the same source from different angles** — the agent-memory-requirements corroboration note (KB-methodology / artifact-governance framing) and the research analysis note (llm-do feature-design framing). No competing-ownership problem, but a future maintainer comparing them should note they are complementary, not redundant.

## Flags

- Split source: the survey carries at least three independent values (adaptation taxonomy, memory/skills landscape, evaluation methodology). This is already reflected by the two derived notes covering different slices.
- The source is a 2026-03-09 arXiv survey in a fast-moving area; treat coverage, prevalence estimates, and "strategic recommendations" as provisional.
- No genuine outbound or bidirectional edges to author from the source/ingest beyond what already exists; the actionable signal in this regeneration is the reverse edges and the citation maintenance observation.
