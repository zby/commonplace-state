---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/work/explanatory-theories-deployment-time-learning/theory-mediated-improvement-loop.md"
source_has_frontmatter: false
date: "2026-08-21"
depth: standard
---

# Connection Report: A provisional theory-mediated improvement loop

**Source:** [A provisional theory-mediated improvement loop](../../../../work/explanatory-theories-deployment-time-learning/theory-mediated-improvement-loop.md)

## Discovery Trace

**Source and authorization:**

- Read the full final source and `kb/work/COLLECTION.md`. The source is raw text without frontmatter, so this report is provisional. The work contract authorizes outbound prospecting in `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/instructions/`, `kb/sources/`, peer `kb/work/`, and already-known external targets. Durable library artifacts are not allowed to author reverse edges into `kb/work/`; peer workshop artifacts were evaluated separately.
- Treated the source's existing links as encoded context rather than new candidates: the proposal-selection loop, explanatory-reach, checked-outcome versus explanation retention, theory-warrant granularity, HCL, the selective-evaluation model, theory-mediated self-improvement, experimental-contrast limits, the ablation proposal, later-improvement compounding, SPADE, and Exo. This removes five findings that appeared as recommendations in the older report but are now directly linked in the final source.
- The workshop README already indexes the source. The selective-evaluation model already links to it, and the typed experiment design already consumes it; only the still-missing source-to-experiment edge is recommended below.

**Curated heads and full title surfaces:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/instructions/README.md`, `kb/sources/README.md`, and `kb/work/README.md`. The source has no tags, so there were no tag READMEs to read.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` fresh over every authorized local destination. The sweeps returned 355 title rows in notes, 136 in reference, 173 in agent-memory systems, 12 in agentic systems, 46 in instructions, 532 in sources, and 589 in work. Promising title clusters concerned theory-mediated learning, consumption paths, methodology governance, reflective revision, learning gates, hypothesis search, and the workshop's own experimental artifacts.

**Description listing scan:**

- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over each of the seven authorized local destinations. The authored candidates that survived later inspection were six notes, two source ingests, and one typed workshop artifact. Reference descriptions led chiefly to the already-linked ablation proposal. Agent-memory and agentic descriptions exposed near cases without an independently selected and retained theory lifecycle. Instruction descriptions exposed generic review and experiment procedures rather than an operation this conceptual artifact asks its reader to perform.

**Body search:**

- Notes: ran `rg -n -i 'theory-mediated|retained theor|working theor|theory revision|improvement-process theor|object-level.*theor' kb/notes/ --glob '*.md'`; `rg -n -i 'proposal-selection|candidate (search|generation|selection)|search allocation|evidence selection|diagnos.*candidate|search.*evaluation.*retention' kb/notes/ --glob '*.md'`; `rg -n -i 'held-out|rival theor|correlated error|independent audit|post-hoc|sham theor|content intervention|causal uptake|causal trace' kb/notes/ --glob '*.md'`; `rg -n -i 'improvement-process|promotion (rule|gate)|promotion.*retention|lifecycle cost|applicability check|revise.*rescope|codif.*supersed.*retir|learning-value gate|retaining.*worth' kb/notes/ --glob '*.md'`; `rg -n -i 'stored but unused|retriev.*consum|stored.*inert|operative retention|activation.*retention|retention.*activation|addressable.*retriev' kb/notes/ --glob '*.md'`; and `rg -n -i 'object[- ]level theor|process theor|meta[- ]level theor|theory target|theory.*promotion|promotion.*theory|methodology.*theory|theory.*methodology' kb/notes/ --glob '*.md'`. These searches kept the theory-pathway, consumption, methodology-governance, second-order revision, faithful-rationale, and learning-gate notes below. The diagnostic-richness and theory/methodology layering notes were inspected but failed the articulation test for this source.
- Reference: ran `rg -n -i 'theory-mediated|retained theor|working theor|proposal-selection|candidate (search|generation)|evidence selection|explanatory-reach' kb/reference/ --glob '*.md'` and `rg -n -i 'later improvement|compounding|causal uptake|causal trace|retained.*(rationale|theory)|ablat|trajectory-aware|promotion.*authority' kb/reference/ --glob '*.md'`. The only load-bearing treatment design was the ablation-baselines proposal already linked by the source. Commonplace traces did not add a theory-specific claim.
- Agent memory: ran `rg -n -i 'theor(y|ies)|hypothes|world model|causal model|mechanis' kb/agent-memory-systems/ --glob '*.md'`; `rg -n -i 'candidate (search|generation|selection)|proposal|evaluation|retention|revision' kb/agent-memory-systems/ --glob '*.md'`; and `rg -n -i 'retained.*(theor|hypothes)|theor.*retention|revision.*theor|compounding|held-out|independent audit|post-hoc|rival theor' kb/agent-memory-systems/ --glob '*.md'`. Meta-Harness was the closest case, but its hypotheses are run-local proposal scaffolding rather than an independently gated retained theory object.
- Agentic systems: ran `rg -n -i 'theor(y|ies)|hypothes|world model|causal|mechanis' kb/agentic-systems/ --glob '*.md'` and `rg -n -i 'candidate|proposal|search|evaluation|retention|revision' kb/agentic-systems/ --glob '*.md'`. Autogenesis and Compound Engineering were inspected and rejected below. Exo is already linked from the source.
- Instructions: ran `rg -n -i 'theory|hypothesis|proposal-selection|candidate generation|evidence selection|held-out|independent audit|experimental|ablation' kb/instructions/ --glob '*.md'`. Hits were generic semantic-review, premise-review, and experimental procedures; none was a source-specific invocation or a useful traversal target.
- Sources: ran `rg -n -i 'retained theor|working theor|theory-mediated|theory revision|explicit theor|system theor|object-level theor|promotion theor' kb/sources/ --glob '*.md'`; `rg -n -i 'candidate search|evidence selection|value[- ]of[- ]information|experiment design|hypothesis proposal|hypothesis.*selection|theory.*candidate|discriminating experiment' kb/sources/ --glob '*.md'`; and `rg -n -i 'later improvement|fresh-start|causal uptake|causal trace|compounding|held-out|independent audit' kb/sources/ --glob '*.md'`. MDA survived as a worked separation of mechanism proposal, belief update, experiment selection, and held-out prediction. The number-game study survived because its generation, evaluation, prediction, and domain-extension probes do not expose one stable hypothesis state. Automata learning and Agent Optimizers remained boundary cases.
- Work: ran `rg -n -i 'theory-mediated|retained theor|ephemeral theor|on-the-spot theor|evidence selection|improvement-process theor' kb/work/ --glob '*.md'` and `rg -n -i 'proposal-selection|candidate search|later improvement|compounding|rival theor|independent audit|causal uptake' kb/work/ --glob '*.md'`. The typed experiment design passed as a missing outbound connection. The raw HCL reading and Exo case passed as raw-text targets. The workshop README and selective-evaluation model already carry the needed links.
- External: no web search was run. HCL, SPADE, and Exo were the only already-known external targets in scope, and all are already linked from the source.

**Link following:**

- Followed [Theory-mediated learning](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) one hop into proposal selection, representational form, formal reach-assessment, world-model assessment, and retained-substrate requirements. The source already carries the proposal-selection and retained-substrate edges; the broader observations-to-retained-theory pathway remained a missing foundation.
- Followed [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) into artifact analysis, behavioral authority, representational form, and action-conditioned world models. The consumption-path claim survived because it exactly explains why the source's stored-but-unused `T_n` is inert; the broader artifact axes were not needed as additional links.
- Followed [A methodology governs its own extension only as far as it settles](../../../../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) into behavioral authority, verification, and the theory/methodology two-layer note. The form-verification-authority criterion survived as a foundation for improvement-process theory; the two-layer note was rejected because its layers divide fast-path methodology from live theory fallback, not object theory from improvement-process governance.
- Followed [Reflection makes retained lessons second-order](../../../../notes/reflection-makes-retained-lessons-second-order.md) and [Selective revision needs a faithful rationale](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) through their shared theory-mediated-learning, addressability, scope, and reach-assessment neighborhood. Both survived: one supplies the revision operations and the other the condition under which those operations target the premise that actually failed.
- Followed [Model Discovery Agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) into theory-mediated learning, formal reach-assessment, world-model assessment, DiscoverPhysics, FALSIFYBENCH, and automata learning. MDA survived as the worked staged architecture; the more distant benchmark analogues did not add another load-bearing edge.
- Followed [Hypothesis generation and updating in large language models](../../../../sources/hypothesis-generation-and-updating-in-large-language-models.ingest.md) into explanatory-reach, proposal selection, fixed-decomposition limits, FALSIFYBENCH, and the experimental-contrast note. The first, second, and experimental-contrast targets are already linked by the source; the ingest itself remained useful empirical support for isolating theory search from assessment.
- Followed the local experiment-design neighborhood into the HCL reading, selective-evaluation model, Exo case, and workshop README. This produced one typed outbound candidate and two raw-text candidates; the selective model and README already have the needed source links.

## Connections Found

- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) -- **extends**: the source turns that note's observations -> theory search -> reach-assessment -> retained theory pathway into coupled system-change and theory-revision loops, then locates five distinct places where the working theory can change an improvement episode.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) -- **rests-on**: the source's distinction between inert stored `T_n` and behaviorally consequential retrieved `T_n` applies the note's participation condition to a theory that mediates self-improvement actions.
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../../../../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) -- **rests-on**: the source's improvement-process theory must govern retained form, verification, authority, retrieval, and lifecycle because leaving those meta-decisions to episode-local improvisation would not govern how theory or system changes become operative.
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../../../../notes/reflection-makes-retained-lessons-second-order.md) -- **mechanism**: addressable rejection, revision, and rescoping are the operations that make the source's `T_n` to `T_{n+1}` theory loop different from merely accumulating another episode-local explanation.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) -- **rests-on**: the source's premise-bearing theory contract and content-intervention controls are necessary because selective revision helps only when the recorded mechanism, assumptions, and scope expose what actually carried the theory.
- [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -- **rests-on**: the source explicitly separates whether an object theory is sound from whether retaining it is worth its authority and lifecycle cost, applying the note's validity-versus-learning-value distinction to theory promotion.
- [Model Discovery Agent: LLM-assisted Bayesian Experiment Design](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) -- **evidenced-by**: MDA is a worked component-level instance in which an LLM proposes explicit mechanisms while separate machinery updates beliefs, selects discriminating experiments, and scores held-out interventions; it supports separating theory search, assessment, and evidence acquisition without testing retained system theory across improvement episodes.
- [Hypothesis generation and updating in large language models](../../../../sources/hypothesis-generation-and-updating-in-large-language-models.ingest.md) -- **evidenced-by**: supplied-candidate evaluation, free generation, prediction probes, and domain extension yield different projected hypothesis states, supporting the source's isolation of candidate search from theory assessment and its demand for consequences outside the eliciting evidence surface.
- [Experiment design for theory-mediated deployment-time learning](../../../../work/explanatory-theories-deployment-time-learning/experiment-design.md) -- **produces**: the source's two loops, five theory roles, ephemeral-versus-retained distinction, and identification controls are operationalized by the staged comparisons in this typed workshop artifact; the experiment design already points back to the model, while the model lacks the useful path to its test design.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

- [From controlled HCL benchmarks to deployment-time learning](../../../../work/explanatory-theories-deployment-time-learning/hcl-reading.md) -- potential **draws-on**: the source's claim that HCL's harness-change gate cannot double as a theory-acceptance gate depends on this local reading's distinction between checked harness behavior and an unobserved, separately retained theory lifecycle; the reading already points to the source, so a source-side link would complete the useful path.
- [Exo case: from self-rewrite to compounding](../../../../work/explanatory-theories-deployment-time-learning/exo-case.md) -- potential **draws-on**: the source's object-theory versus improvement-process-theory distinction and later-improvement application are developed in this detailed case, whose promotion surfaces, lifecycle costs, evaluation boundary, and falsifiers supply the concrete boundary behind the compact model.

## Rejected Candidates

- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) -- rejected because its two layers are theory-derived fast-path methodology and live theory fallback; that is a different division from the source's object-level system theory and improvement-process theory.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- rejected because richer traces could help form or revise `tau_n`, but the source's abstract `z_n` neither requires a particular diagnostic substrate nor makes a claim about trace richness that would justify a direct edge.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) -- rejected because its proposer formulates hypotheses while producing benchmarked harness candidates, but those hypotheses are run metadata rather than a separately proposed, reach-assessed, selectively retained, and revised theory object.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- rejected because its evolution journal records hypotheses, predictions, outcomes, and attribution for code search, but it supports candidate optimization rather than an independent theory-selection loop with its own acceptance semantics.
- [Compound Engineering](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- rejected because it has hypothesis-driven experiments and retained project knowledge, but its review finds later-episode causal feedback mostly absent and no separately versioned theory lifecycle.
- [Can LLM Agents Infer World Models?](../../../../sources/can-llm-agents-infer-world-models-agentic-automata-learning.ingest.md) -- rejected because separating evidence collection, hypothesis construction, and exact verification is a useful benchmark analogue, but the system neither retains a theory across episodes nor uses one to revise the learning system itself.
- [Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -- rejected as a direct edge because the source already links the distilled later-improvement protocol; this study adds a no-fresh-start boundary example rather than another load-bearing premise for the model.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- **Provisional source:** the source has no frontmatter and remains an exploratory workshop text. Recheck the candidates if it acquires a type contract, changes disposition, or is split before promotion.
- **Split candidate:** the source connects to at least six notes across theory-mediated learning, consumption and authority, reflective revision, and promotion gates. It also makes independent claims about coupled-loop architecture, five intervention roles, object-versus-improvement-process theory, treatment identity, and causal measurement. A future writer should consider separating the architectural model from experimental identification and lifecycle-governance claims before promotion.
