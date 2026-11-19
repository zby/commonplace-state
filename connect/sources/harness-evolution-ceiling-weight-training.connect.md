---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/harness-evolution-ceiling-weight-training.md"
source_has_frontmatter: true
date: "2026-10-11"
depth: standard
---

# Connection Report: Harness Evolution Hits a Ceiling: When Weight Training Should Begin

**Source:** [Harness Evolution Hits a Ceiling: When Weight Training Should Begin](../../../../sources/.snapshots/harness-evolution-ceiling-weight-training.md)

The source is an immutable snapshot (arXiv 2610.11655, Tian et al., 2026-10-08). No `harness-evolution-ceiling-weight-training.ingest.md` exists yet. Per the sources contract, every outbound candidate below is for that future ingest report; no durable link may target the `.snapshots/` file.

Source claims used for judging candidates:
- The first failure signal in each trajectory sorts failed trajectories into process failures (F2 harness interference, F3 loops or exhausted step budgets) and content failures (F4, a delivered plan that is poor). F1 covers unbacked assertions.
- Harness self-evolution (an AHE-style loop) repairs process failures. LoRA or full fine-tuning on evolved-harness trajectories internalizes those gains and targets content failures. On 9B the adapter alone matches the evolution line. A placebo adapter trained on answer-shuffled trajectories falls below the base model.
- The loop stops at F4 because its evidence package never showed the proposer the scorer's per-check failure composition. The metric-defining keys sat outside the directories the loop could edit. The authors attribute the ceiling to this loop, not to harness evolution in general, and one remedy attempt failed.
- The rule is applied twice. First, failure composition chooses the lever. Second, after a harness gain, the accepted edits show where the gain lives. Gains that changed what the model writes trained into the weights (DeepPlanning). Gains that changed what it sees stayed in the harness (WebArena-Lite: two pages of history; adapters added nothing).
- Ablations: tools, lessons and other capability-granting components carry the gain. Enforcement components are mostly within noise. The paper also gives a score identity S = r·q̄: a lever that only raises the delivery rate r is capped by the quality q̄ of what the model already writes.

## Discovery Trace

**Collection contract:** read `kb/sources/COLLECTION.md` → Outbound links. Authorised destinations: notes, notes/definitions, agent-memory-systems, agentic-systems, sources, reference (`see-also` only), external (`derived-from`, `see-also`). Excluded destinations: `kb/work/` and `kb/instructions/`. The snapshot never authors links; the ingest does.

**Topic indexes (tag heads):**
- `kb/tags/improvement-loop-README.md` (`complete: true`, so the by-tag rg was skipped) flagged [diagnostic richness](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), [weakly discriminated qualities](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md), [evaluation automation phase-gated](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) and [residue classes](../../../../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md).
- `kb/tags/continual-learning-README.md` (`complete: true`, by-tag rg skipped) flagged [form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md), [deployed system is the unit](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [fixed decomposition](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) and [readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md).
- `kb/tags/self-improving-systems-README.md` (`complete: true`): only parent routing; no new candidates.
- The `deploy-time-learning`, `trace-learning`, `failure-modes` and `evaluation` heads were checked by description only. Trace-learning concerns external system reviews, which are covered under agent-memory-systems below. Failure-modes concerns KB knowledge failures, not agent trajectory failures.

**Description listing scan:**
- Scoped `rg '^description:'` on the candidates in `kb/notes/` above and on 15 harness-related ingests in `kb/sources/`. Flagged ingests: co-harness, whale, harness-updating-is-not-harness-benefit, meta-harness, ecdysis, harnesscompass and harnessevolve.

**Body search:**
- `rg -l -i -e 'harness evolution|self-evolving harness|weight training|fine-tun|LoRA|weights vs|into the weights|AHE|agentic harness engineering'` over notes, tags, agentic-systems, agent-memory-systems and reference returned about 60 files. These were narrowed by intersecting with the next query.
- `rg -l -i 'weight' kb/notes | xargs rg -l -i 'harness'` returned 29 files. This surfaced [scaling absorbs scaffolding](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) and [parametric reproduction](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md).
- `rg -l -i 'agentic harness engineering|AHE\b' kb/sources kb/agentic-systems` returned 8 ingests that mention AHE. The paper's loop is "in the style of AHE", which led to the [AHE review](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md).
- `rg -n -i 'co-harness|whale|weight'` in the form-coevolution note found that Co-Harness is already in its inventory. The note names cross-form credit assignment as the open problem.
- `rg -n -i 'harness|weights|absorb'` in the scaling-absorbs note found line 27: "Functions may also migrate into weights or runtimes".
- `rg -n -i 'evidence|package|meta-harness|trace'` in the diagnostic-richness note found that the note already holds two bounded contrasts (Meta-Harness, AutoSaddler) plus AHE staging.
- `rg -l -i 'noise floor|rollout variance|four-rollout|per-rollout'` over notes and sources returned only the AutoSaddler ingest. No note covers the measurement-noise protocol.
- `ls kb/agentic-systems/reviews | rg -i 'harness|evol|trace'` returned no hits.

**Link following:**
- The diagnostic-richness note led to the AHE and Meta-Harness reviews in agent-memory-systems and to the trace-learning-techniques survey. The survey's promotion-target axis already separates readable artifacts from weights; Autocontext is the only system it records that bridges both.
- The deployed-system note led to the fixed-decomposition note (line 28) and the form-coevolution note (line 46): "the allocation among weights, prompts, and code ... should also remain computationally revisable."
- The scaling-absorbs note led to relaxing signals and parametric reproduction. Neither was kept (see Rejected).

## Connections Found

All are candidates for the future `kb/sources/harness-evolution-ceiling-weight-training.ingest.md`.

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **is-evidence-for**: Section 6.2 traces the F4 ceiling to what the evidence package showed the proposer. The scorer saw F4, so oracle strength was not the bottleneck. The per-check failure composition never reached the proposer, and the accepted edits targeted only what the package made visible. This is a third bounded case for the note's oracle-versus-diagnostic separation, beside Meta-Harness and AutoSaddler. Caveat: the one attempt to expose the failure composition (Gemma 4 12B) did not produce a resolvable gain.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) — **is-evidence-for**: The paper offers an operational answer to the note's cross-class credit-assignment problem. Failure composition picks the form (harness for process failures, weights for content failures). The accepted edits then decide which gains move into weights and which stay in the harness. The harness × weights cross design (seed/evolved × base/adapter) separates the forms' contributions better than the Co-Harness entry that the note says "does not isolate coevolution".
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) — **is-evidence-for**: The WebArena-Lite result shows a gain that lives in what the model sees. Adapters trained on those trajectories added nothing, so a model-only learning loop could not have captured it. The paper also gives an evidence-based rule for allocating work between weights and harness, which the note says should itself stay revisable.
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — **is-evidence-for**: This is direct evidence for the note's side remark that "functions may also migrate into weights". On 9B the trained adapter alone matches the evolved harness, and a placebo control rules out generic fine-tuning. Context-supply gains did not migrate, which bounds the absorption to what the model writes. The evidence covers absorption by training at fixed task difficulty, not absorption by scaling.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **is-evidence-for**: The keys that define which metrics the loop observes sat outside the four directories the loop could edit. The loop therefore could not change its own observation of F4, which matches the note's information-omission case. Use with care: the paper calls this a property of this loop, not a proof that F4 was unreachable.
- [Co-Harness ingest](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) — **compares-with** (axis: how the update form is assigned). Co-Harness's HarnessCritic sends each failure to a harness dimension or excludes it as `agent error`, then fine-tunes on repaired-harness trajectories. This paper assigns the lever from aggregate first-signal failure composition and adds a placebo-adapter control. Both distil harness gains into weights.
- [WHALE ingest](../../../../sources/whale-joint-harness-weight-optimization.ingest.md) — **compares-with** (axis: which lever pays in which domain). WHALE finds SearchQA harness-dominant and Math model-dominant and recommends short alternation. This paper predicts which lever will pay from seed measurements (delivery rate, quality, failure composition) and orders the levers harness first, then weights.
- [Harness updating is not harness benefit ingest](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) — **compares-with** (axis: cross-pairing as an attribution design). That paper crosses agents with evolvers. This one crosses harnesses with weights, to separate gains that need the runtime from gains the trained model keeps.
- [Agentic Harness Engineering review](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) — **compares-with** (axis: what the evolve agent's evidence package exposes). The paper's loop is modelled on AHE. The review documents AHE's staged package (pass rates, debugger reports, change attribution). The paper finds that a package of this kind, led by intervention metrics and lacking the scorer's per-check composition, bounded what the proposer could fix.
- External: `https://arxiv.org/abs/2610.11655` — **derived-from**: the ingest's analysis is worked out from this paper.

## Bidirectional Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) <-> source: the note would gain a case where the oracle is strong and the diagnostics are poor, which the existing contrasts do not show. See Reverse-edge Candidates.

## Reverse-edge Candidates

These links would be authored to the future ingest, never to the snapshot, under `kb/notes/COLLECTION.md` rules.

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) → ingest: a third bounded contrast paragraph and an evidence footer. This is the strongest reverse edge.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) → ingest: a new inventory entry beside Co-Harness, as a cross-form case whose design partly isolates per-form contributions.
- [Scaling absorbs scaffolding at fixed difficulty, not at the frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) → ingest: evidence for function migration into weights and for its limit (gains from what the model sees stay in the harness).

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md): the scorer does discriminate F4. The ceiling comes from proposer visibility, which belongs to diagnostic richness, not to oracle discrimination.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md): the paper's diagnose-then-intervene rule only resembles it on the surface. The note concerns building judges from observed failures; the paper chooses an intervention lever with an existing programmatic scorer.
- [Residue classes need different mechanisms](../../../../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md): its residue classes concern untransferred decisions, not trajectory failure classes. The match is a shared word.
- [Readable-artifact loop is the tractable unit](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md): adjacent, but the paper's contribution is the handoff into weights, which form coevolution covers better.
- [Operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md): enforcement components scored within noise in the ablations, which could suggest relaxing. But that note's signals concern proxy-theory brittleness, not the absence of an ablation effect.
- [Parametric reproduction cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md): the paper's absorbed gains are behavioural, not records, so the note's authority argument does not apply.
- [Ecdysis ingest](../../../../sources/ecdysis-training-runtime-harnesses.ingest.md): it shares the theme of harness accommodating model weakness, but has no named axis on which a comparison would help the reader.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md): it surveys systems, not papers. The paper's weights-promotion path would matter only if a system review were written.

## Index Membership

- [improvement-loop tag head](../../../../tags/improvement-loop-README.md) and [continual-learning tag head](../../../../tags/continual-learning-README.md) are marked `complete: true` over their participating collections. Check `kb/tags/COLLECTION.md` to see whether `kb/sources/` participates before listing the ingest.

## Synthesis Opportunities

Three results now converge on harness-then-weights handoff with a placebo or cross-pairing control: Co-Harness, WHALE and this paper. Together they suggest a claim for the form-coevolution note: the form a gain can move into depends on the channel it acts through. A gain in what the model writes can move into weights; a gain in what the model sees cannot. This would be a candidate refinement of that note, not a new note (per the fold-claims policy).

## Maintenance Observations

- No note covers measurement-noise protocol for harness or weight interventions (noise floor, four-rollout means, fresh anchors, same-night comparisons). The only hit is the AutoSaddler ingest. This is a first observation; log it rather than write a note.

## Flags

- No ingest exists yet. Every Connections Found entry targets the future `kb/sources/harness-evolution-ceiling-weight-training.ingest.md`. A concurrent `cp-skill-ingest` agent may be producing it.
- Split candidate (informational): the paper makes several independent assertions (lever selection by failure composition, the evidence-package ceiling, the sees/writes transfer rule, capability versus enforcement ablations) across several topic areas. This is normal for an ingest and needs no action.
- Tension: the form-coevolution and deployed-system edges use the paper as support for revisable allocation across forms, while the fixed-decomposition edge reads the F4 ceiling as structural. The paper itself attributes the ceiling to this loop's package; an ingest should keep that scope.
