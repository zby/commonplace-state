---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/the-meta-harness-ablation-bounds-summarization-not-theory-formation.md"
source_has_frontmatter: true
date: "2026-07-29"
depth: standard
---

# Connection Report: The Meta-Harness ablation does not identify episode-backed theory formation

**Source:** [The Meta-Harness ablation does not identify episode-backed theory formation](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md)

## Discovery Trace

**Curated heads and tag routes:**
- Read `kb/notes/README.md`, `learning-theory-README.md`, and `deploy-time-learning-README.md`. `learning-theory-README.md` routes this note through the `deploy-time-learning` child; neither tag README declares `complete: true`, so both by-tag description scans were run. The strongest index fit is the deploy-time-learning head's feedback-and-signal-quality section.
- Read the destination heads `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. `kb/types/` has no `README.md`; its collection contract and complete title/description surface were used instead.

**Full title and description scans:**
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` once for each authorised local destination: `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, `instructions`, and `types`.
- Ran `rg '^description:' kb/<destination> --glob '*.md'` over all seven destinations and filtered for `summar`, `compress`, `episode`, `trace`, `theor`, `causal`, `diagnostic`, `attribution`, `evidence`, `retain`, `review`, `outer-loop`, and `conjecture`.
- Ran `rg -l '^tags:.*\blearning-theory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the corresponding `deploy-time-learning` query. These elevated the diagnostic-richness, theory-mediated-learning, process-verification, retained-episode, and trace-authority cluster.

**Body search:**
- Ran `rg -n -i 'summar(y|ies|ization)|compress(ed|ion)|episode|trace access|raw trace|theory formation|causal conjecture|attribution|diagnostic richness|reach-assessment|meta-harness'` across every authorised local destination. Broad results were re-filtered through the articulation test.
- Ran the narrower notes query `rg -n -i 'summaries replaced|summary.*episode|episode.*summary|summari.*discard|retain.*episode|episode-backed|consumer-blind|post-attribution|causal conjecture|scoped mechanism|unrun arm|hold raw|generic summary' kb/notes/ --glob '*.md'`.
- Ran `rg -n 'the-meta-harness-ablation-bounds-summarization-not-theory-formation|The Meta-Harness ablation does not identify' kb --glob '*.md'`. It found one already-authored inbound edge from the bitter-lesson production-method note; that edge is not repeated as a candidate.

**Per-destination evaluation:**
- `notes`: kept the process-verification premise and the production-history limit as missing outbound candidates. Kept return edges from diagnostic richness and theory-mediated learning because the source already uses both and the reverse direction independently supplies a necessary empirical qualification. Existing links to episode retention, decision-surface capture, abstraction boundaries, commitment, explanatory-reach, and reach-assessment were not repeated.
- `reference`: `proposals/ablation-baselines-for-the-declared-objective.md` shares an ablation shape but evaluates Commonplace's whole declared objective, not the episode-backed theory intervention; rejected as a different experimental object.
- `agent-memory-systems`: followed `reviews/meta-harness.md`; kept a return edge because its code-grounded component audit materially supports the note's release/provenance boundary. Other trace-learning systems were keyword matches without evidence about this ablation.
- `agentic-systems`: Fractal's summary-plus-retained-history architecture is a system comparison, not evidence about the treatment contrast; rejected. No other candidate passed the articulation test.
- `sources`: followed both Meta-Harness artifacts and `llm-agents-are-not-always-faithful-self-evolvers.ingest.md`. Kept the latter as independent adverse evidence about condensed experience, with its explicit limitation that it does not test actionability-designed or theory-forming condensation. Kept a reverse edge from the Meta-Harness ingest because the new note materially bounds the ingest's broad summaries-hurt reading.
- `instructions`: compression criteria and full-pass procedures concern editorial compression or workflow execution, not the tested learning treatment. The collection's frontloaded posture also makes such outbound links exceptional; none passed.
- `types`: note/type specs mention descriptions and compressed handles but supply no observation, case, or source that bears on the identification claim; none passed.
- `external`: authorised for already-known targets only; open-web prospecting was skipped, and no user-supplied external target was present.

**Link following:**
- Followed the source's links to diagnostic richness, retained episodes, preserved evidence, decision-surface capture, abstraction boundaries, the Meta-Harness review, and theory-mediated learning. From those neighborhoods, opened `an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md`, `history-has-one-chance-to-become-checkable.md`, `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md`, and the two relevant source ingests. Selective revision was rejected because this note establishes treatment identification, not the later mechanics of revising an accepted theory.

## Connections Found

- [An outcome check licenses replay; a rule needs the process verified](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) — **grounds**: explains why end-to-end harness scores can validate candidate behavior without validating the causal mechanism or scope asserted by a retained report, which is the note's review-operator distinction.
- [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) — **grounds**: explains why absent ablation-arm code and unrecorded generation history cannot be reconstructed later from the released artifacts, making the provenance limit principled rather than merely inconvenient.
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) — **evidenced-by**: independently finds a raw-trajectory/condensed-experience asymmetry under causal intervention while explicitly limiting the result to current summary forms, corroborating the adverse-evidence side without identifying reviewed episode-backed theory formation.

## Bidirectional Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) <-> source — **extends**: the return path takes readers from the general diagnostic-richness inference to the precise boundary that Table 3 tested summarize-and-discard, not an episode-preserving theory layer.
- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) <-> source — **evidenced-by**: the return path records direct adverse evidence motivating the conjecture's raw-episode-fixed and evaluator-ablation arms, while preserving that those arms remain unrun.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) <-> source — **is-evidence-for**: the review's code-grounded distinction between harness-level end-to-end evaluation and absent component-level causal attribution materially supports the note's claim that retained reports were not separately identified.

## Reverse-edge Candidates

- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) → source — **compares-with**: the ingest's broad "summaries hurt" interpretation should route readers to the note's treatment-level qualification, especially the difference between replacing traces with fixed digests and adding reviewed conjectures beside retained episodes.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Conversation vs prompt refinement in agent-to-agent coordination](../../../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — shares the trace-versus-compressed-handoff tradeoff, but its coordination setting supplies no evidence or mechanism specific to learning-treatment identification.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) — develops a later requirement for revising theories, but this note's comparison turns on episode access, attribution timing, and review before selective revision occurs.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) — includes episodes-only and no-review arms, but its experimental target is Commonplace's whole declared objective rather than the Meta-Harness treatment contrast.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) — retains full session history beside an always-visible summary, but it is an unablated system architecture and therefore neither identifies nor tests the claimed intervention.

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) — add under “Feedback and signal quality” as the adverse-result boundary note paired with diagnostic richness: it accepts the measured compression loss while separating that treatment from episode-backed theory formation.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- None
