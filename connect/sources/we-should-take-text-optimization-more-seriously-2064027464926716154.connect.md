---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/we-should-take-text-optimization-more-seriously-2064027464926716154.md"
source_has_frontmatter: true
date: "2026-06-09"
depth: standard
---

# Connection Report: We Should Take Text Optimization More Seriously

**Source:** [We Should Take Text Optimization More Seriously](../../../sources/we-should-take-text-optimization-more-seriously-2064027464926716154.md)

This source is an **immutable snapshot** (`type: snapshot`) in `kb/sources/`. Per `kb/sources/COLLECTION.md`, snapshots are never edited and never author outbound links. The active connection surface is the matching `.ingest.md` — which does **not yet exist** — so the load-bearing signal here is **reverse-edge candidates**: which `kb/notes/` should add `evidence`/`derived-from` links pointing at this snapshot. The `Connections Found` section therefore lists what the future `.ingest.md` should cite, not edits to the snapshot.

The article (by @yoonholeee, same author as the Meta-Harness paper already cited in this KB) argues that the "text layer" (prompts, context, filesystem state, memory, retrieval DBs, harness code) is (1) a legitimate update mechanism functionally equal to weight updates, (2) more sample-efficient in the low-data regime via a Kolmogorov-style compression/description-length prior, and (3) the enabler of a new scaling axis, "update-time compute" via reflective text optimization. It frames weights-vs-text as a **routing problem**, treats the text layer as a **staging ground** for eventual distillation into weights, and calls for theory, evals, and "architecture research" on the text-layer design space. This is a near-exact upstream restatement of this KB's continual-learning / substrate-coevolution / deploy-time-learning cluster.

## Discovery Trace

**Index scan:**
- Read [notes dir-index](../../../notes/dir-index.md) — flagged the learning-theory cluster: `continual-learning-open-problem-is-behaviour-not-knowledge`, `deploy-time-learning-is-the-missing-middle`, `treat-continual-learning-as-substrate-coevolution`, `constraining-during-deployment-is-continuous-learning`, `in-context-learning-presupposes-context-engineering`, `readable-artifact-loop-is-the-tractable-unit-for-continual-learning`, `definitions/distillation`. Also flagged `pointer-design-tradeoffs-in-progressive-disclosure`, `the-chat-history-model-...`, `agent-orchestration-occupies-a-multi-dimensional-design-space`, `llm-learning-phases-fall-between-human-learning-modes`, `codification-and-relaxing-navigate-the-bitter-lesson-boundary`.
- Read [agent-memory-systems README](../../../../agent-memory-systems/README.md) — flagged `trace-derived-learning-techniques-in-related-systems` and the design-space/"architecture research" framing.

**Topic indexes:**
- Source carries only `tags: [x-article]` (a capture tag, not a topic tag), so no topic-tag index applied. Used the learning-theory cluster from the dir-index instead.

**Body search:**
- `rg -i "text layer|text optimization|text-layer|staging ground|update-time compute" kb/notes/` — only `maintenance-operations-catalogue-...` and `periodic-kb-hygiene-...` match on "staging ground" (KB-local instructions-staging usage, different sense from the article's "text-as-staging-ground-for-weights"); the article's exact terminology is otherwise absent, confirming this vocabulary is not yet captured.
- `rg -i "amortiz|distill.*weights|weight.*distill|Kolmogorov|description length|sample-efficien" kb/notes/` — hit `definitions/distillation`, `information-value-is-observer-relative`, `rlm-has-the-model-write-ephemeral-orchestrators`, others. Confirms compression/description-length intuition lives in the distillation definition but the "text update = compact patch to pretrained prior" framing is not stated.
- `rg -i "progressive disclosure|design space|architecture research|reachable behavior|elicit and compose|headroom|extended mind|cognition in the wild|Memex|tools.for.thought" kb/notes/ kb/agent-memory-systems/` — broad hits; relevant ones evaluated below. "Extended mind / Cognition in the Wild / Memex" (the article's cognitive-science lineage) returned no note matches — not captured.

**Link following:**
- From `continual-learning-open-problem-...` followed to `deploy-time-learning-...`, `treat-continual-learning-as-substrate-coevolution`, `constraining-during-deployment-...`, and `memory-management-policy-is-learnable`. The substrate-coevolution note already cites the author's Meta-Harness paper as `evidence`, confirming this source is squarely in that note's evidence neighborhood.
- From `deploy-time-learning-...` confirmed it already carries a "staging ground" framing (prose → codified) and an external-source footer of the exact kind this snapshot would join.

## Connections Found

(Recommendations for the future `.ingest.md` outbound surface — the snapshot itself is never the link author. Labels drawn from the `kb/sources/` authorised set: `evidence`, `derived-from`, `rationale`, `compares-with`, `defined-in`, `see-also`.)

- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) — **evidence**: the article's central thesis (text layer is a legitimate update mechanism, functionally equal to weight updates) independently corroborates this note's split of behaviour-change into expensive distributed-parametric updates and cheap readable artifacts.
- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) — **evidence**: the article's "routing problem" framing (which update target fits a given piece of information) and its weights/text co-evolution argument directly support the coevolution frame; same author as the Meta-Harness paper this note already cites.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) — **evidence**: the article's "text layer as a flexible staging ground for information that may eventually be distilled into weights" is the same prose-then-codify staging argument; would join this note's external-source footer alongside the OSS-context and harness-engineering citations.
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) — **evidence**: the article argues text-layer edits "apply weaker optimization pressure while remaining highly auditable, and in many cases also composable" and accumulate adaptive capacity outside weights — direct corroboration of the constraining-as-learning claim.
- [In-context learning presupposes context engineering](../../../../notes/in-context-learning-presupposes-context-engineering.md) — **evidence**: the article's progressive-disclosure passage ("good text-layer systems do not dump all available information... they implement progressive disclosure... condition on a much larger context than the input window") supports the claim that in-context learning depends on selection machinery that is itself learned over deployment.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — **evidence**: the article's "update-time compute" axis (reflective text optimization can fork, test, and compare hypotheses where SGD's single parameter vector cannot) is empirical/argumentative support for prioritising the readable-artifact loop as the tractable improvement unit.
- [Distillation](../../../notes/definitions/distillation.md) — **evidence**: the article's "good text updates are compact patches to a pretrained world prior" and the Kolmogorov/description-length sample-efficiency argument corroborate distillation's compression-under-a-prior framing; it also names the recurring industry pattern of distilling the text layer into weights over time, which is exactly the ML-distillation sibling this note draws.

## Bidirectional Candidates

None. The snapshot is immutable and authors no links; any return path would be authored from the `.ingest.md`, which is itself the outbound surface listed above. No separate bidirectional edge applies.

## Reverse-edge Candidates

(Notes that should author an `evidence`/`derived-from` link **to this snapshot** under `kb/notes/`'s own `COLLECTION.md` rules. These are the strongest deliverable for an immutable source — they restate the `Connections Found` set as the inbound edges a notes-side author or a future connect run on each note would add. All targets are `status: current` except `in-context-learning-...` (`seedling`) and `readable-artifact-loop-...`; `evidence` is an additive label so seedling status is not a blocker.)

- [continual-learning-open-problem-is-behaviour-not-knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) → source — **evidence**: external corroboration that the text layer is a behaviour-change mechanism co-equal with weight updates.
- [treat-continual-learning-as-substrate-coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) → source — **evidence**: the article's weights/text routing-and-coevolution argument; pairs with the Meta-Harness citation already present.
- [deploy-time-learning-is-the-missing-middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) → source — **evidence**: text-as-staging-ground for eventual distillation into weights restates the deploy-time staging argument.
- [constraining-during-deployment-is-continuous-learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) → source — **evidence**: auditable, composable, weaker-pressure text-layer edits accumulating adaptive capacity outside weights.
- [in-context-learning-presupposes-context-engineering](../../../../notes/in-context-learning-presupposes-context-engineering.md) → source — **evidence**: progressive disclosure / implicit conditioning on much-larger-than-window context.
- [readable-artifact-loop-is-the-tractable-unit-for-continual-learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) → source — **evidence**: update-time compute and fork-test-compare reflective loops over text.
- [definitions/distillation](../../../notes/definitions/distillation.md) → source — **evidence**: compact-patch-to-prior framing and the industry pattern of distilling the text layer into weights.
- [trace-derived-learning-techniques-in-related-systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) → source — **evidence**: the article cites Reflexion, Trace, GEPA, Meta-Harness, ACE, ExpeL, AWM and others as reflective/trace-grounded text-layer learning loops — the same systems this survey catalogues — and frames update-time compute, a missing organising lens for the survey's reinjection stage.

## Off-authorisation Candidates

- [agent-orchestration-occupies-a-multi-dimensional-design-space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — the article's "architecture research" call (instruction hierarchy, DSPy programs, agent skills, harnesses, and memory systems as points in one large under-described design space) is a genuine connection to this note's design-space framing, but the article describes the *text-layer* design space, not the *orchestration* design space; the match is at the meta-level ("we lack a vocabulary for the space") rather than the object level. No `kb/sources/` label cleanly carries "parallel call for a design-space vocabulary in a sibling domain." Suggestion: reject as off-scope for a direct edge; if the `.ingest.md` wants to surface the "architecture research" theme it should land on the trace-derived survey (an `evidence` edge above) rather than this orchestration note.

## Raw Text Candidates

None. All candidate targets have frontmatter.

## Rejected Candidates

- [maintenance-operations-catalogue-should-stage-distillation-into](../../../../notes/maintenance-operations-catalogue-should-stage-stable-procedures.md) — matched on "staging ground", but the note uses the term for KB-internal staging of operations before promotion to `kb/instructions/`; the article uses it for the text-layer-before-weights sense. Keyword collision, not a conceptual connection.
- [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in](../../../../notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) — same "staging ground" keyword collision; no topical link.
- [pointer-design-tradeoffs-in-progressive-disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — the article's progressive-disclosure point is already better served by the `in-context-learning-presupposes-context-engineering` edge (which makes the in-context/selection-machinery argument the article actually states); this note is about pointer-design micro-tradeoffs the article does not touch. Avoid a redundant weaker edge.
- [llm-learning-phases-fall-between-human-learning-modes](../../../../notes/llm-learning-phases-fall-between-human-learning-modes.md) — adjacent (three-timescale framing), but the article does not make a pre-training/in-context/deploy-time phase argument; the genuine learning-timescale content is captured by the deploy-time and in-context edges.
- [memory-management-policy-is-learnable-but-oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — about a specific system (AgeMem) learning policy in distributed-parametric state; the article's only contact is the general weights-vs-text routing point, already carried by the substrate-coevolution edge.

## Index Membership

- [agent-memory-systems README / Patterns Across Systems](../../../../agent-memory-systems/README.md) — the article's "architecture research" call and its list of text-layer designs (instruction hierarchy, DSPy, agent skills, memory systems as one design space) align with this collection's survey purpose. A future curator could cite it as a landscape source, but membership is weak — it is an opinion/manifesto piece, not a system, and the collection covers systems, so this is a note for the curator rather than an action.

## Synthesis Opportunities

None that aren't already captured. The article's three pillars map one-to-one onto existing notes (legitimacy → continual-learning-open-problem; sample-efficiency → distillation; update-time compute → readable-artifact-loop), so it strengthens existing claims rather than implying a new higher-order one. The one candidate higher-order claim — "update-time compute is a scaling axis symmetric to inference-time compute" — is partially present in `readable-artifact-loop-...` and `treat-continual-learning-as-substrate-coevolution` but is not stated as its own claim anywhere; flagged below as a maintenance observation rather than a synthesis note to create here.

## Maintenance Observations

- **Missing ingest surface.** No `we-should-take-text-optimization-more-seriously-...ingest.md` exists. Until one does, this snapshot has no authored outbound surface and the `Connections Found` edges have nowhere to be written. Running `cp-skill-ingest` on the snapshot would create that surface and is the natural next step; the seven `evidence` edges above are the ingest's main payload.
- **Vocabulary gap — "update-time compute".** The article names a scaling axis (update-time compute, symmetric to inference-time compute) that the KB gestures at but never names. `readable-artifact-loop-...` and `treat-continual-learning-as-substrate-coevolution` both touch it without a handle. Candidate durable follow-up: a note or definition for "update-time compute" if the concept proves load-bearing.
- **Vocabulary gap — text-layer external-cognition lineage.** The article's cognitive-science grounding (Hutchins' *Cognition in the Wild*, Clark & Chalmers' *Extended Mind*, Bush's Memex, tools-for-thought) returned zero note matches. The KB grounds the same intuition in programming theory and information theory but not in the extended-cognition lineage. Possible source-review or note if that grounding becomes relevant.
- **Strong author/source overlap.** This snapshot, the Meta-Harness paper (cited in `treat-continual-learning-as-substrate-coevolution` and the trace-derived survey), and the `yoonholee.com/meta-harness` ingest are all the same author; the manifesto distills the same research program. Worth a `compares-with` cross-reference between this snapshot and any future Meta-Harness snapshot if one is captured.

## Flags

- **No `.ingest.md` yet** — the connection deliverable above cannot be authored until the snapshot is ingested. Recommend `cp-skill-ingest` on the snapshot path.
- **Split candidate** — the source connects to seven notes across the learning-theory / continual-learning cluster plus the trace-derived survey, and makes three independent assertions (legitimacy, sample-efficiency, update-time compute). It clears the five-notes / three-areas / multiple-assertions threshold, so the future `.ingest.md` should distribute its `evidence` edges across the three pillars rather than dumping them on one note.
