---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/work/causal-impact-selective-evaluation/experiment-design.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: Experiment design for causal selective evaluation

**Source:** [Experiment design for causal selective evaluation](../../../../work/explanatory-theories-deployment-time-learning/experiment-design.md)

## Discovery Trace

**Setup and source reading:**
- Read `.agents/skills/cp-skill-connect/SKILL.md`, `kb/cache/types/connect-report.md`, the full source, and `kb/work/COLLECTION.md`.
- Source collection: `work`. Its outbound section permits working links to `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `instructions`, `sources`, `external`, and peer `work`, with loose working-state labels; it also says library collections do not link into `kb/work/`.
- Source has YAML frontmatter. Core claim: a credible selective-evaluation test must (1) compare selector policies over a fixed trusted procedure registry, (2) test adaptive procedure generation as a separate factor, (3) build an independent audit surface for harmful misses and calibration, (4) count full evaluation cost, and (5) run a separate online comparison because different commitment decisions change later harness trajectories.
- External prospecting skipped: `external` is only for already-known external targets, and no new external target was supplied beyond already captured ingests.

**Curated heads and collection surfaces read:**
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/instructions/README.md`, `kb/sources/README.md`, and `kb/work/README.md`.
- No tag README pass: the source has no `tags:` frontmatter.
- `kb/work/README.md` already lists the `causal-impact-selective-evaluation` workshop, so no index-membership action is needed for the source.

**Title and description prospecting:**
- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' | rg 'selective|causal|impact|evaluation|procedure|audit|cost|SPADE|obligation|calibration|harness|adaptive'` and `rg '^description:' kb/notes/ --glob '*.md' | rg 'selective|causal|impact|evaluation|procedure|audit|cost|SPADE|obligation|calibration|harness|adaptive'`. Strongest note candidates: `an-experiment-identifies-only-the-contrast-it-actually-runs.md`, `localized-retention-pays-where-change-is-sparse-in-a-matching.md`, `warranted-autonomy-is-bounded-by-oracle-domain.md`, `evaluation-automation-is-phase-gated-by-comprehension.md`, `choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md`, and `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`.
- Ran `rg -n 'selective evaluation|causal impact|harmful miss|procedure availability coverage|end-to-end detection coverage|calibration|SPADE|adaptive procedure|obligation registry|independent audit|full cost accounting' kb/notes/ --glob '*.md'`. This kept the same note cluster and ruled out broader evaluation notes that only shared vocabulary.
- Ran `rg -n 'selective evaluation|harmful miss|trajectory-aware|selector|causal selection|adaptive procedure generation|obligation registry|independent audit|full cost accounting|held-out retention' kb/reference/ --glob '*.md'`. The most relevant reference hits were `proposals/calibrating-semantic-gates-against-labelled-fixtures.md` and `proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md`.
- Ran `rg -n 'selective evaluation|harmful miss|full cost accounting|trajectory-aware|offline comparison|online comparison|adaptive procedure generation' kb/sources/ --glob '*.md'`. This surfaced the HCL ingest as the concrete baseline source and confirmed that SPADE is already the source's explicit procedural-generation anchor.
- Ran `rg -n 'selective evaluation|causal impact|harmful miss|procedure availability coverage|end-to-end detection coverage|calibration|SPADE|adaptive procedure|obligation registry|independent audit|full cost accounting' kb/work/ --glob '*.md'` and `rg -n 'selective evaluation|causal selective|adaptive procedure generation|harmful miss|full cost accounting|trajectory-aware|offline|online comparison' kb/work/causal-impact-selective-evaluation/ --glob '*.md'`. Strongest raw-text neighbors: `README.md`, `hcl-reading.md`, and `for-hcl-authors.md`.

**Low-yield destinations checked:**
- Ran `rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg 'selective|causal|impact|evaluation|procedure|audit|cost|SPADE|obligation|calibration|harness|adaptive'` and `rg -n 'selective evaluation|causal impact|SPADE|adaptive procedure|obligation registry|independent audit|full cost accounting|calibration' kb/agent-memory-systems/ --glob '*.md'`. Hits were mostly system reviews with generic calibration or harness-learning language; none gave a more specific traversal target than the HCL/SPADE ingests and local theory notes.
- Ran the same pair over `kb/agentic-systems/`. The only substantive hit was `gbrain.md` on its calibration phase; rejected as too system-specific to this source's experiment-design question.
- Ran `rg -n 'selective evaluation|harmful miss|full cost accounting|trajectory-aware|offline comparison|online comparison|adaptive procedure generation' kb/instructions/ --glob '*.md'`. No relevant instruction artifact surfaced.

**Link following and candidate evaluation:**
- Read the source's already linked [SPADE ingest](../../../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) and [selective-evaluation model](../../../../work/explanatory-theories-deployment-time-learning/selective-evaluation-model.md) to confirm the live local cluster and avoid restating existing edges as new candidates.
- Read full candidate targets before keeping them: [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md), [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md), [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), [Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md), and [Ingest: Harness Continual Learning: Continual Adaptation Beyond Model Parameters](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md).
- Rejected `trajectory-aware-evaluation-of-transforming-agent-workflows.md` after full read: its trajectory question is output-only vs trace-aware workflow judging, while this source's online phase is about selector-caused divergence in later harness states and opportunities.
- Rejected `evaluation-automation-is-phase-gated-by-comprehension.md` after full read as a weaker traversal target than the labelled-fixtures proposal: both care about judge calibration, but the proposal is the more direct template for the source's seeded/held-out audit surface.

## Connections Found

- [Ingest: Harness Continual Learning: Continual Adaptation Beyond Model Parameters](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) -- **abstracted-from**: the source's baseline arm, historical-retention concern, and growing evaluation-cost surface inherit their concrete shape from HCL's candidate-evaluator setup and finite historical-anchor gate.
- [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -- **grounds**: the source's adaptive-generation factor explicitly separates technical and observational validity from decision value and cost worthiness, which is this note's validity-gate / learning-value-gate split in experiment-design form.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- **rests-on**: the source says selective evaluation is only plausible when effects stay local, dependencies are explicit, and downstream impact is bounded; this note is the durable statement of that locality condition.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **grounds**: the source's omitted-check policy and generated-procedure factor change what an acceptance claim can honestly warrant, so the experiment depends on which harmful misses and regressions its audit oracles can actually detect.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **grounds**: the source deliberately separates offline selector comparison, registry-vs-generation comparison, and the later online comparison because each is a different causal contrast.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **grounds**: the source treats adaptive procedure generation as a separate factor because success inside the supplied registry, impact theory, or procedure-construction boundary would not by itself validate those fixed design coordinates.
- [Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) -- **draws-on**: the source's independent reference surface of seeded known effects plus held-out human-audited obligations matches this proposal's split between known-case regression and separate field calibration.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

- [Causal impact and selective evaluation](../../../../work/explanatory-theories-deployment-time-learning/README.md) -- potential **rests-on**: the workshop framing states the open assumptions, closure criteria, and audit obligations that this experiment is meant to satisfy.
- [Reading HCL as deployment-time learning](../../../../work/explanatory-theories-deployment-time-learning/hcl-reading.md) -- potential **draws-on**: this file gives the HCL-specific meaning of historical anchors, evaluator growth, and why HCL's partition is not yet a validated causal graph.
- [An invitation to the HCL authors](../../../../work/explanatory-theories-deployment-time-learning/for-hcl-authors.md) -- potential **see-also**: it is the shorter outward-facing restatement of the same design, and it sharpens the repeated-run and omitted-check-audit requirements.

## Rejected Candidates

- [A provisional causal selective-evaluation model](../../../../work/explanatory-theories-deployment-time-learning/selective-evaluation-model.md) -- already linked directly from the source and clearly a current local dependency; not a missing connection.
- [Ingest: SPADE: Self-Play in Adaptive Synthetic Executable Environments](../../../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) -- already linked directly from the source as the adaptive-generation anchor.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- relevant to calibration, but the labelled-fixtures proposal is the more exact navigation target for the source's seeded-audit design.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) -- the shared word "trajectory" is misleading here; that proposal studies output-only vs trace-aware workflow judging, not selector-caused divergence in later harness state.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- useful background on oracle discrimination, but it is a looser traversal target than the more specific oracle-domain and labelled-fixtures artifacts above.
- [gbrain](../../../../agentic-systems/reviews/gbrain.md) -- has a calibration phase, but it does not help a reader reason about selective-evaluation experiment design specifically.

## Index Membership

None

## Synthesis Opportunities

- The source, the HCL ingest, the SPADE ingest, and `choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md` imply a durable claim not yet extracted: selective-evaluation systems that can synthesize procedures need at least three separable acceptance layers — procedure validity, decision value, and omitted-region audit — rather than one generic quality score.
- The source, `an-experiment-identifies-only-the-contrast-it-actually-runs.md`, and the HCL workshop files imply a durable methodological note: offline fixed-candidate selector studies and online adoption-trajectory studies are different experiment classes, so cost, retention, and safety claims should say which class produced them.

## Maintenance Observations

- Reverse-edge prospecting from library collections into this target was intentionally not pursued because `kb/work/COLLECTION.md` says library collections do not link into `kb/work/`; durable reverse edges should wait for promotion into a library artifact.
- The source now has a corrected connect report metadata fact: it does have frontmatter, so future regenerations should keep `source_has_frontmatter: true`.

## Flags

- The source is an in-workshop proposal with explicit "not yet established" status. Treat every candidate here as working-context signal, not durable graph state.
