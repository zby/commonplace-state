---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/harness-evolution-ceiling-weight-training.ingest.md"
source_has_frontmatter: true
date: "2026-10-11"
depth: standard
---

# Connection Report: Ingest: Harness Evolution Hits a Ceiling: When Weight Training Should Begin

**Source:** [Ingest: Harness Evolution Hits a Ceiling](../../../../sources/harness-evolution-ceiling-weight-training.ingest.md)

The ingest already carries ten outbound edges (derived-from, five is-evidence-for notes, four compares-with). All ten targets exist. This report adds candidates beyond that set.

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` "Outbound links". Destinations to scan: notes, reference, agent-memory-systems, agentic-systems, tags, sources. Excluded: `kb/work/`, `kb/instructions/`. Labels for an ingest: `is-evidence-for` (notes, agent-memory-systems), `compares-with` (notes, sources, agent-memory-systems, agentic-systems), `abstracted-from`/`rests-on`/`defined-in` (notes), `see-also` (sparingly), `derived-from` (external). No label names `tags` as a destination; `kb/tags/COLLECTION.md` lists participating collections `[notes, reference, instructions, agent-memory-systems, agentic-systems]`, so sources are not tag carriers. External prospecting skipped (arXiv URL already present as derived-from).

**Existing-link verification:** `test -e` on all nine local targets in the footer: all OK. `rg -l 'harness-evolution-ceiling' kb` -- no inbound links anywhere yet.

**Tag heads read:** `continual-learning-README.md`, `improvement-loop-README.md`, `self-improving-systems-README.md` (all `complete: true`, so by-tag rg skipped). Used for routing signal only.

**Title listing:** `rg -N --no-heading -m1 '^# ' kb/notes --glob '*.md' | rg -i 'weight|fine-tun|noise|selection|oracle|evaluat|credit|distill|absor|harness|scaffold|ablation|placebo|benchmark'` -- flagged: weight-resident-methodologies, a-proposal-selection-loop-requires-search-evaluation-and-retention, evaluation-automation-is-phase-gated-by-comprehension, compounding-is-tested-in-later-improvement, prompt-ablation-converts-human-insight, oracle-strength-spectrum.

**Body search:**
- `rg -il 'harness evolution|harness-evolution|self-evolving harness|harness search|evolve.*harness' kb/notes kb/sources kb/agentic-systems kb/agent-memory-systems kb/reference kb/tags` -- ~50 hits; sources and notes followed below.
- `rg -il 'noise floor|selection optimism|winner.s curse|regression to the mean'` -- only the target itself.
- `rg -il 'placebo' kb/notes kb/sources` -- `form-not-content-placebo-controlled-self-repair.ingest.md`, `scaffold-not-vocabulary-popperian-code-generation-skill.ingest.md`, `notes/definitions/theory-builder-checks.md`.
- `rg -il 'STaR|rejection.sampling fine' kb/notes kb/sources` -- hits were all false positives on the token "star" (e.g. design-for-the-first-time-human); none on self-training.
- `rg -n 'Co-Harness|WHALE' kb/notes -l` -- five notes, four already linked from the ingest plus `the-bitter-lesson-selects-production-methods-not-representational.md` and `readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md`.
- `rg -n -i 'noise|weight|fine-tun|aggregat|diagnos|lever|accommodat'` over ecdysis, harnessdev, the-what-and-when, harnesscompass ingests -- evaluated below.

**Link following:** From diagnostic-richness neighbours: meta-harness ingest (raw traces vs summaries), harnesscompass (grounded self-feedback), harnessevolve (reference trajectories), ecdysis (failure grouping). From the form-coevolution cluster: readable-artifact-loop note (cites Co-Harness as the only all-three-form loop), bitter-lesson note (cross-artifact credit assignment as open problem), the-what-and-when ingest (harness-to-weights consolidation path as hypothesis).

## Connections Found

- [The Bitter Lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **is-evidence-for**: the note names cross-artifact credit assignment as the decisive open problem; the crossed seed/evolved x base/adapter design with a placebo is a small, concrete attribution method across two forms, and the 9B result (adapter alone matching the evolved harness) is a case of learned localized content moving into the parametric row.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: the note's "distributed-parametric" bullet treats Co-Harness as the only harness-to-weights loop in its evidence set; this paper is a second, sequential (not recurrent) harness-then-weights pipeline whose crossed design isolates the weight contribution that Co-Harness does not.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- **is-evidence-for**: the F4 ceiling is a case where an automated judge improved score along visible process metrics without access to the failure composition, and inert edits passed the judge four times until the authors required evidence that the code path fired; both bear on the note's demand for diagnostic access and demonstrated judge discrimination before automation.
- [Ingest: Form, Not Content? Placebo-Controlled Self-Repair](../../../../sources/form-not-content-placebo-controlled-self-repair.ingest.md) -- **compares-with**: placebo adapters as a content-attribution control. PoPE's deranged-error adapter found no content effect; this paper's answer-shuffled 9B adapter fell below base, supporting content attribution for the genuine adapter. Same control logic, opposite outcome.
- [Ingest: Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- **compares-with**: what the harness proposer's evidence package exposes. Meta-Harness shows raw traces beat summaries; this paper's evidence package summarised process counts and omitted per-check failure composition, and locates its ceiling there.
- [Ingest: The What and When of Self-Evolving Agents](../../../../sources/the-what-and-when-of-self-evolving-agents.ingest.md) -- **compares-with**: promotion of capability from harness to weights. The essay proposes a consolidation path inward toward weights as a hypothesis; this paper gives one empirical test and a candidate gate (edit surface: writes trains in, sees stays).
- [Ingest: HarnessDev](../../../../sources/harnessdev-llms-create-and-evolve-agent-harnesses.ingest.md) -- **compares-with**: noise-aware selection in harness development. HarnessDev measures unchanged-commit spread and held-out reversal; this paper adds a calibrated noise line, fresh anchors after each accept and a selection-optimism bound.
- [Ingest: Ecdysis](../../../../sources/ecdysis-training-runtime-harnesses.ingest.md) -- **compares-with**: aggregating failures across tasks to direct harness repair. Ecdysis groups recurring failures for attribution; this paper aggregates first-signal composition to choose the lever. Secondary; author only if the ingest wants a diagnosis-aggregation axis.

## Bidirectional Candidates

- [Ingest: Form, Not Content? Placebo-Controlled Self-Repair](../../../../sources/form-not-content-placebo-controlled-self-repair.ingest.md) <-> source -- **compares-with**: the PoPE ingest would gain a positive counterpart for its adapter-placebo control logic.
- [Ingest: Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) <-> source -- **compares-with**: Co-Harness's ingest cannot isolate the weight contribution; a return link points to a design that does.
- [Ingest: WHALE](../../../../sources/whale-joint-harness-weight-optimization.ingest.md) <-> source -- **compares-with**: schedule-based versus diagnosis-based lever switching.
- [Ingest: Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) <-> source -- **compares-with**: evidence-package composition as the binding constraint.

## Reverse-edge Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) → source -- the ingest's Recommended Next Action: a bounded strong-oracle, poor-diagnostics contrast paragraph citing this ingest, keeping the caveat that the remedy run was within noise.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) → source -- the edit-surface rule as a recorded conjecture on its open credit-assignment question, scoped to one DeepPlanning-versus-WebArena-Lite contrast.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) → source -- second harness-to-weights example beside Co-Harness in the "distributed-parametric" bullet.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) → source -- the review could cite the paper as external criticism of an AHE-style evidence package (intervention metrics without failure composition).

## Off-authorisation Candidates

- [continual-learning tag head](../../../../tags/continual-learning-README.md) / [improvement-loop tag head](../../../../tags/improvement-loop-README.md) -- the source substantively fits both, but no label authorises sources -> tags and sources are not a participating tag collection. Reject as off-scope; the notes that absorb the evidence carry the tags.

## Raw Text Candidates

None

## Rejected Candidates

- [Execution indeterminism is a property of the sampling process](../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) -- the noise floor is a measurement protocol; the paper says nothing about the source of variance. Topical only.
- [Weight-resident methodologies provide context-efficient behavioral compression](../../../../notes/weight-resident-methodologies-compress-behavior-in-context.md) -- about activating pretrained methodology by a cue, not training harness behaviour into weights.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- held-out reporting is not a later improvement episode; the fit is loose.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- the AHE-style loop is a routine instance; no new bearing on the three-function claim.
- [Ingest: HarnessCompass](../../../../sources/harnesscompass-guiding-automatic-harness-evolution.ingest.md), [Ingest: HarnessEvolve](../../../../sources/harnessevolve-reference-trajectories.ingest.md) -- diagnostic-richness siblings, but Meta-Harness is the clearer comparison axis; adding all would spray.
- [Ingest: Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md), [Ingest: ModularRSI](../../../../sources/modularrsi-generalizable-harness-self-improvement.ingest.md) -- harness-only evolution; no shared axis beyond "harness evolution".

## Index Membership

None (sources are not tag carriers; see Off-authorisation Candidates).

## Synthesis Opportunities

Several harness-to-weights sources now exist: Co-Harness (recurrent, critic-routed), WHALE (scheduled alternation), this paper (diagnosis-routed, crossed design), plus the What-and-When consolidation hypothesis. Together they could support a note on when a harness gain can be promoted into weights. The candidate gate is the edit-surface conjecture, and the required control is a crossed harness x weights evaluation with a placebo. Evidence is thin (one contrast per source), so this belongs in the log until a second contrast appears.

## Maintenance Observations

None

## Flags

- The ingest is dense (six extractable-value items across diagnosis, cross-form transfer, measurement protocol). It is a source analysis, so the split rule does not apply, but the reverse edges span three note clusters; a writer should land each in its own note rather than summarising the whole paper in one.
- Tension to keep visible: the edit-surface rule (sees stays in the harness) supports the deployed-system note, while the 9B adapter-matches-harness result supports absorption into weights. Both readings are bounded to one setup each.
