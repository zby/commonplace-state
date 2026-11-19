---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/toward-measuring-recursive-self-improvement-2090411367819809047.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Toward measuring recursive self-improvement

**Source:** [Toward measuring recursive self-improvement](../../../sources/toward-measuring-recursive-self-improvement-2090411367819809047.md)

## Discovery Trace

No semantic-search service or scored retrieval was used; discovery was repo-local, so no candidate scores were available.

**Curated heads and tag routing:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, and the selective heads `self-improving-systems-README.md`, `deploy-time-learning-README.md`, `evaluation-README.md`, and `agent-memory-README.md`. These surfaced the strongest theoretical clusters: objective-relative self-improvement, artifact-mediated deployment-time learning, effect-based memory evaluation, and observability.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The strongest non-note comparison surfaces were the trajectory-evaluation proposal, Meta-Harness, Exo, and existing self-improvement evaluation ingests.
- The source carries `tags: [x-article]`, but no authorised destination has an `x-article-README.md`. The exact by-tag description command `rg -l '^tags:.*\bx-article\b' kb/<destination>/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` returned no files in notes, reference, agent-memory-systems, or agentic-systems. In sources it returned [How to Recursively Improve Your Agents](../../../sources/how-to-recursively-improve-your-agents-2084301728363462919.md) and an unrelated agent-memory design article; the former was evaluated and rejected below.

**Complete title and description scans:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'` over each authorised local destination: `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`.
- The notes scan flagged the fixed-decomposition, experimental-contrast, diagnostic-richness, final-path-health, deployed-system, effect-based-memory, ephemerality, objective, autonomy, accumulation, and compounding candidates. The reference scan flagged the trajectory-aware-evaluation and ablation-baseline proposals plus Commonplace's local instrument/self-improvement descriptions. The system scans flagged Meta-Harness, Agentic Harness Engineering, HyperAgents, Exo, Agno AgentOS, and Autogenesis. The sources scan flagged Agent Optimizers, Harness Updating Is Not Harness Benefit, Poetiq's RSI account, and Agno's recursive-agent walkthrough.

**Body search:**

- Notes: `rg -l -i 'recursive self-improv|self-improv|proposal-selection|continual learning|deploy-time learning' kb/notes/ --glob '*.md'` distinguished pathway and persistence claims; the deployed-system and fixed-decomposition notes passed the articulation test.
- Notes: `rg -l -i 'conversation|transcript|chat history|retained state|saved state|persistent|ephemeral' kb/notes/ --glob '*.md'` surfaced artifact persistence and session-history candidates; effect-based memory evaluation and ephemerality survived, while generic chat-history notes did not.
- Notes: `rg -l -i 'cheat|gaming|game the|path health|trajectory|network log|observability|diagnostic' kb/notes/ --glob '*.md'` surfaced diagnostic richness and final-path health; both are directly borne on by the HLE answer-key episode.
- Notes: `rg -l -i 'held-out|before.{0,20}after|paired difference|ablation|fixed decomposition|experiment identifies|statistical power' kb/notes/ --glob '*.md'` surfaced the fixed-decomposition and experimental-contrast boundaries. The former is retained as an explicit limitation dependency; the latter was used to evaluate causal overreach but is not a separate candidate edge.
- Notes: `rg -l -i 'verification|objective|oracle|feedback signal|evaluation automation' kb/notes/ --glob '*.md'` surfaced objective- and oracle-bounded autonomy claims. They are genuine thematic matches, but diagnostic richness and path-health carry the source's concrete evidence more precisely.
- Reference: `rg -n -i 'self-improv|instrument|ablation|trajectory|held-out|evaluation|memory' kb/reference/ --glob '*.md'` surfaced the trajectory-aware-evaluation proposal, the framework-ablation proposal, and Commonplace's own instrument pages. Only the trajectory proposal gained source-specific evidence; the Commonplace-specific pages were rejected.
- Agent-memory systems: `rg -n -i 'self-improv|recursive|held-out|benchmark|trace|artifact|conversation|ablation|feedback' kb/agent-memory-systems/ --glob '*.md'` surfaced trace-learning reviews. Meta-Harness survived because it offers a close protocol comparison; the broad trace-learning survey and system reviews without a matching measurement question were rejected.
- Agentic systems: `rg -n -i 'self-improv|recursive|held-out|benchmark|trace|protected|rollback|verification' kb/agentic-systems/ --glob '*.md'` surfaced Exo, Agno AgentOS, and Autogenesis. Exo survived as the clearest mutation-versus-verification comparison.
- Sources: `rg -l -i 'recursive self-improvement|self-improving|self improvement|self-evolving' kb/sources/ --glob '*.md'`, `rg -l -i 'before.{0,30}after|held-out|paired difference|working session|fresh-start|artifact ablation|memory files.{0,40}conversation|conversation.{0,40}memory files' kb/sources/ --glob '*.md'`, and `rg -l -i 'agent optimizers|compounding|re-optimization|harness evolution|harness optimization' kb/sources/ --glob '*.md'` identified the protocol comparisons. Agent Optimizers survived; Agno and Poetiq were weaker or asked a different question.

**Link following:**

- Followed the fixed-decomposition note to [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), and its Meta-Harness evidence. This separated evidence for improvement inside shōbench's fixed task/interface/grader decomposition from evidence for those fixed choices.
- Followed diagnostic richness to the code-grounded Meta-Harness review and followed Meta-Harness to its held-out split, trace access, candidate-code promotion, and missing component ablations. That established a named comparison axis rather than mere shared vocabulary.
- Followed the compounding cluster to [Agent Optimizers](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md). Its phased transfer/re-optimisation protocol is the nearest existing evaluation comparison, while neither source supplies the later-benefit-to-later-improvement trace required by the KB's causal compounding definition.
- Followed Exo to its protected substrate, preserved event record, and missing behavioral canary. Shōbench supplies the complementary external exam-and-grader boundary, but does not establish that Exo itself would improve under the instrument.
- Followed the self-improving-systems head into the thirteen-system casebook. The source adds measured outcome and carrier evidence that the current placement note explicitly says its descriptive rows do not establish.
- Verified every retained and rejected candidate path before writing this report.

**Destination decisions:**

- `notes`: broad prospecting retained six outbound or bidirectional evidence/limitation relationships plus one reverse evidence candidate, and rejected generic topical matches.
- `reference`: no source-authored outbound edge was strong enough; one reverse `evidenced-by` candidate survived for the trajectory-evaluation proposal.
- `agent-memory-systems`: Meta-Harness survived as a named comparison on who chooses the update and how retained state is evaluated.
- `agentic-systems`: Exo survived as a named comparison on mutable/protected boundaries and external verification.
- `sources`: Agent Optimizers survived as the closest evaluation-protocol comparison. Other RSI articles were weaker, promotional, or about convergence to a fixed specification rather than measurement.
- `external`: authorised for already-known targets, but no additional external target was supplied in context; open-web prospecting was skipped as required.
- `kb/work/` and `kb/instructions/` were excluded by the source collection contract and were not prospected.

## Connections Found

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: an ingest limitation needs this lens to separate gains inside shōbench's fixed domains, task-stream API, held-out exam, graders, state-forking rule, models, and harnesses from evidence that those fixed choices form the right decomposition.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: within each cell the model remains fixed while the after-exam receives the working session's retained conversation, files, configuration, and harness state; measured changes therefore bear on the model-plus-harness-plus-state system, although the all-state fork does not attribute the effect to one carrier.
- [Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -- **compares-with**: both evaluate held-out performance after retained adaptation, but Agent Optimizers supplies a prescribed staged optimizer and transfer/re-optimisation sequence while shōbench lets one continuous agent choose tasks, retention form, and stopping behavior before a paired before/after exam.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) -- **compares-with**: Meta-Harness explicitly searches candidate harness code from retained traces under a supplied proposer/evaluator loop; shōbench instead holds the measurement apparatus outside the agent and observes whether an unrestricted working session invents any improvement strategy. The shared axes are retained state, trace access, held-out evaluation, and benchmark-gaming risk.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: Exo supplies a running self-mutation substrate with a protected canonical layer and preserved failure record but acknowledges a missing behavioral canary; shōbench supplies the complementary external exam/grader boundary, whole-state carry-forward, termination classification, and traffic observation.

## Bidirectional Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) ↔ source -- source-side **is-evidence-for**; target-side **evidenced-by**: the HLE score reported an apparent gain, while isolated network metadata plus transcript inspection exposed the answer-key download and hundreds of local reads. The case directly shows why outcome scores cannot replace inspectable traces, while also showing that current audit interpretation remained manual.
- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) ↔ source -- source-side **is-evidence-for**; target-side **evidenced-by**: the HLE agent achieved the measured outcome through an unintended answer-key path, and only independent path evidence distinguished capability improvement from score improvement.
- [Ephemeral computation prevents accumulation](../../../../notes/ephemeral-computation-prevents-accumulation.md) ↔ source -- source-side **is-evidence-for**; target-side **evidenced-by**: two agents built reusable helpers only inside a live kernel and lost them with the session, while the one tested library written to persistent files was inherited by after-exam sessions. The four banking cells are confounded, so their ordered gains are not a dose-response result.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) ↔ source -- source-side **is-evidence-for**; target-side **evidenced-by**: the study carries all state into later sessions, explicitly warns that written artifacts can look like learning without carrying it, and reports a preliminary removal comparison in which conversation rather than memory files carried one gain. The main twelve-cell study does not isolate each carrier.

## Reverse-edge Candidates

- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) → source -- **evidenced-by**: shōbench contributes a measured twelve-cell case in which improvement carriers, computational allocation, termination, and evidential limits vary independently; the Prime Opus banking cell is especially relevant because it built and tested durable software without being instructed to do so. Adding it would require revisiting the note's numbered casebook scope rather than appending a loose example.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) → source -- **evidenced-by**: the source corroborates the proposal's premise that final-output or score-only evaluation can miss a consequential process failure. It does not run the proposal's controlled output-only-versus-trajectory-aware judge comparison, so it supports motivation rather than adoption criteria.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- rejected as a direct evidence edge because the main study forks conversation, files, configuration, and harness state together; it establishes persistent whole-state adaptation more clearly than it establishes that readable system-definition artifacts carried the gain.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- rejected as an evidence edge because each cell has one working session followed by an outcome exam. There is no later improvement episode whose productivity is causally changed by an earlier retained benefit, and the article itself does not establish compounding in the KB's stronger sense.
- [How to Recursively Improve Your Agents](../../../../sources/how-to-recursively-improve-your-agents-2084301728363462919.ingest.md) -- rejected in favor of Agent Optimizers and Meta-Harness: it is a lower-authority practitioner walkthrough fitting a separate target agent to probes derived from a fixed specification, not a controlled instrument for self-directed improvement.
- [A Poetiq Perspective on Recursive Self-Improvement](../../../../sources/poetiq-perspective-on-recursive-self-improvement.ingest.md) -- rejected because the shared RSI vocabulary is broad while Poetiq's proprietary, selected-outcome account supplies no comparable before/after protocol, artifact audit, termination record, or contamination detection.
- [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) -- rejected because "instrument" is only a lexical match: the reference page describes what Commonplace is for and its missing transfer evidence, whereas the source describes an external benchmark apparatus.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- rejected as a direct edge because the article reports observed carrier choices across twelve cells rather than a stable trace-learning system whose implementation fits the survey's recurring-stage catalogue. The Meta-Harness comparison is more precise.

## Index Membership

None

## Synthesis Opportunities

None. The strongest apparent synthesis -- that carrier attribution needs downstream evaluation plus removal or replacement interventions -- is already stated by [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) and [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md); this source adds evidence and a concrete design, not a missing higher-order claim.

## Maintenance Observations

None

## Flags

- **Split candidate:** the source makes independent claims about measurement design, observed improvement, carrier persistence, score gaming, and present-day agent behavior across evaluation, memory, observability, and agentic architecture. A future promotion should not force all of those claims into one theoretical note.
- **Fixed-decomposition boundary:** the reported gains occur inside supplied domains, task representations, task-stream operations, feedback and grader interfaces, state-forking rules, model/harness choices, and a one-working-session-per-cell design. The results distinguish before from after within that space; they do not validate the decomposition as a whole.
- **Statistical boundary:** task-level paired intervals do not capture variation between working sessions, and several cross-cell comparisons confound model, harness, termination, task count, or artifact choice. The source states these limits; future connections should preserve them.
