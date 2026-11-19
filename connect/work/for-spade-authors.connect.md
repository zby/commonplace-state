---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/work/causal-impact-selective-evaluation/for-spade-authors.md"
source_has_frontmatter: false
date: "2026-08-21"
depth: standard
---

# Connection Report: An invitation to the SPADE authors

**Source:** [An invitation to the SPADE authors](../../../../work/explanatory-theories-deployment-time-learning/for-spade-authors.md)

## Discovery Trace

**Setup and source reading:**
- Read `.agents/skills/cp-skill-connect/SKILL.md`, `kb/cache/types/connect-report.md`, the full target, and `kb/work/COLLECTION.md`. The source collection is `work`; its outbound section authorizes loose working links to notes, reference, agent-memory-systems, agentic-systems, instructions, sources, external, and peer work, but says library collections do not link into `kb/work/`. The target has no YAML frontmatter, so this report is provisional over raw text.
- The source claim: SPADE's adaptive executable-environment mechanism could expand selective evaluation from choosing stored anchors to generating candidate-specific executable procedures, but acceptance evidence needs stronger gates than curriculum generation: execution validity, observation validity, decision value, and selection validity.
- External prospecting skipped: `external` is authorized by the work contract only for already-known targets, and no user-supplied external target was present beyond already captured source artifacts.

**Curated heads and title surfaces:**
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/instructions/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/work/README.md`. No tag READMEs applied because the source has no frontmatter tags.
- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/instructions/ kb/sources/ kb/work/ --glob '*.md'`. The large title surface flagged the local workshop cluster, the SPADE/HCL ingests, HCL/Meta-Harness/eval-engineering sources, and several theory notes on gates, contrasts, oracle domain, and fixed decompositions.
- `kb/work/README.md` already lists the causal-impact-selective-evaluation workshop and the source file in the workshop reading map, so no index-membership action is needed for the target.

**Description listing scan:**
- Ran `rg '^description:' kb/notes/ --glob '*.md'`; retained notes whose descriptions named validity/learning-value gates, oracle domain, fixed decompositions, experimental contrast, bounded impact, and observer-relative value. Rejected broad deploy-time-learning hits that only restated the general learning frame.
- Ran `rg '^description:' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/instructions/ --glob '*.md'`; found no reference, instruction, agent-memory-system, or agentic-system target that the source should link to directly. Agentic-system reviews such as Agno and Exo discuss regression/evaluation boundaries, but they are system-specific comparisons rather than scaffolding for this SPADE-facing invitation.
- Ran `rg '^description:' kb/sources/ --glob '*.md'`; retained the SPADE and HCL ingests as already-linked anchors, plus `towards-automating-eval-engineering-2079976006644072796.ingest.md` and `meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md` as source-side comparisons. Rejected broad continual-learning papers where the relation is only curriculum or retention vocabulary.
- Ran `rg '^description:' kb/work/ --glob '*.md'`; retained the same-workshop files as raw text candidates: `experiment-design.md`, `selective-evaluation-model.md`, `for-hcl-authors.md`, and `hcl-reading.md`.

**Body search:**
- `rg -n "SPADE|synthetic executable|executable environment|environment generation|paired.*hint|hint/no-hint|adaptive synthetic|Self-Play" kb/notes/ kb/reference/ kb/instructions/ kb/sources/ kb/work/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` -- found the target, the same-workshop files, the SPADE ingest and snapshot, and Voyager/executable-environment comparisons. Kept SPADE-linked workshop/source surfaces; rejected Voyager as already mediated by the SPADE ingest and not directly about acceptance evidence.
- `rg -n "Harness Continual Learning|HCL|selective evaluation|impact theory|impact-guided|acceptance evidence|evaluation obligation|procedure registry|full registered evaluation" ...` -- found the full workshop cluster and HCL ingest. Kept `selective-evaluation-model.md`, `experiment-design.md`, `for-hcl-authors.md`, and HCL-related theory/source anchors; rejected isolated HCL mentions in unrelated source comparisons.
- `rg -n "generated eval|eval.*generat|trace-to-eval|evaluation procedure|acceptance evidence|generated procedure|procedure generation" kb/notes/ kb/sources/ kb/work/ --glob '*.md'` -- surfaced the trace-to-eval source, Meta-Harness, and the same-workshop adaptive-procedure-generation thread.
- `rg -n "impact closure|bounded impact|impact theory|behavioral obligation|omitted checks|residual risk" kb/notes/ kb/sources/ kb/work/ --glob '*.md'` -- connected the workshop model to `localized-retention-pays-where-change-is-sparse-in-a-matching.md` and `information-value-is-observer-relative.md`.
- `rg -n "hint.no.hint|hint/no-hint|current-policy counterfactual|learning-value|validity gate|decision value" kb/notes/ kb/sources/ kb/work/ --glob '*.md'` -- supported the direct link to `choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md`.
- `rg -n "regression-gated|historical retention|retention gate|finite anchors|sampled anchors|historical anchor" kb/notes/ kb/sources/ kb/work/ --glob '*.md'` -- supported the HCL and oracle-domain connections.

**Link following:**
- Followed the source's existing links to the SPADE ingest, HCL ingest, and workshop README. The SPADE ingest already links to `choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md`, `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`, `an-experiment-identifies-only-the-contrast-it-actually-runs.md`, Co-Harness, and Voyager. The HCL ingest already links to `warranted-autonomy-is-bounded-by-oracle-domain.md`, fixed-decomposition, and proposal-selection notes.
- Followed the workshop README to `hcl-reading.md`, `selective-evaluation-model.md`, `experiment-design.md`, and `for-hcl-authors.md`. Those files are raw text, so they are routed to Raw Text Candidates rather than Connections Found.
- Followed `experiment-design.md` to the same SPADE-facing target, confirming the target is the shorter outward-facing version of the design rather than the design's primary owner.

## Connections Found

- [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -- **grounds**: the source's proposed split between generated-procedure validity and decision value is the acceptance-evidence analogue of this note's validity-versus-learning-value distinction.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **grounds**: the source's stronger acceptance gates rely on the claim that unattended generated evaluations warrant only what their execution, observation, and selection oracles can actually establish.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **grounds**: the source explicitly limits the SPADE analogy because SPADE learns environment design and model weights inside a fixed authored training decomposition, while the proposed acceptance loop concerns a separately versioned harness.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **grounds**: the source's central adaptation question is whether hint/no-hint learning value can be changed into incumbent/candidate discrimination without borrowing warrant from a different experimental contrast.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- **rests-on**: the proposed impact theory is useful only if candidate effects are sparse enough, dependencies explicit enough, and impact closures small enough to make selective evidence meaningful.
- [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md) -- **grounds**: the source's evidence-acquisition policy buys evidence only when it can change the current acceptance decision or improve the impact theory, which is the decision-relative side of information value.
- [Ingest: Towards Automating Eval Engineering](../../../../sources/towards-automating-eval-engineering-2079976006644072796.ingest.md) -- **evidenced-by**: the source is a practitioner case where traces are turned into executable regression targets and verifier trajectories are inspected, directly adjacent to the target's generated-evaluation proposal.
- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- **evidenced-by**: Meta-Harness shows diagnostic-richness and execution-trace access matter for harness search, giving a comparison point for the target's concern that generated procedures may shift rather than save evaluation work.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

- [Experiment design for causal selective evaluation](../../../../work/explanatory-theories-deployment-time-learning/experiment-design.md) -- potential **draws-on**: the target is the shorter SPADE-facing external account of this experiment-design branch, especially the adaptive procedure-generation factor and its validation/cost caveats.
- [A provisional causal selective-evaluation model](../../../../work/explanatory-theories-deployment-time-learning/selective-evaluation-model.md) -- potential **rests-on**: the target uses the model's objects (`S`, candidate intervention, impact theory, evidence-acquisition policy, commitment rule) in compressed form and inherits its acceptance-semantics and omitted-check risks.
- [An invitation to the HCL authors](../../../../work/explanatory-theories-deployment-time-learning/for-hcl-authors.md) -- potential **see-also**: the two invitations are paired outward-facing accounts of the same workshop, one anchored on HCL's regression-gated harness state and one on SPADE's adaptive executable environments.
- [Reading HCL as deployment-time learning](../../../../work/explanatory-theories-deployment-time-learning/hcl-reading.md) -- potential **draws-on**: the source's HCL setup relies on this workshop reading of sampled retention, evaluator growth, and why the four-part HCL partition is not a validated causal graph.

## Rejected Candidates

- [Ingest: SPADE: Self-Play in Adaptive Synthetic Executable Environments](../../../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) -- already linked directly from the source; retain in trace as the source's main evidential anchor, not a new candidate.
- [Ingest: Harness Continual Learning: Continual Adaptation Beyond Model Parameters](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) -- already linked directly from the source; retain in trace as the HCL setup anchor, not a new candidate.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) -- SPADE's ingest already uses Voyager for the curriculum-memory versus executable-skill-library comparison; linking the invitation directly to Voyager would distract from the acceptance-evidence question.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- relevant background for HCL-style candidate commitment, but the target already works through HCL and the selective-evaluation model; a direct link would duplicate better-targeted anchors.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) -- conceptually relevant to why generated evaluations need strong acceptance gates, but the source does not discuss retained false-positive acceptances directly enough to make this more than a secondary theory link.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) -- has live probes and regression evals in a builder loop, but it is a system-specific comparison rather than a source or theory anchor for generated acceptance procedures.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- discusses build/test oracle limits for self-modification, but the target's question is generated procedure design rather than broad self-rewriting safety.

## Index Membership

None

## Synthesis Opportunities

- SPADE ingest + HCL ingest + this invitation + `selective-evaluation-model.md` imply a synthesis claim not yet promoted: generated evaluation procedures need two independent layers of gates, one for executable/observation validity of the procedure and one for decision value under the current commitment rule. SPADE supplies the training-curriculum separation among breadth, validity, and learning value; HCL supplies regression-gated acceptance; the workshop asks how to combine them without importing either system's warrant wholesale.
- The target and `towards-automating-eval-engineering-2079976006644072796.ingest.md` point at a possible taxonomy of evaluation-procedure construction: production-trace-to-fixed-eval, fixed-registry selection, adapted procedure, and generated executable environment. The current workshop names the options but has not yet extracted the taxonomy into a durable note or proposal.

## Maintenance Observations

- Reverse-edge prospecting from library collections into this target was skipped because `kb/work/COLLECTION.md` states that library collections do not link into `kb/work/`; useful library uptake should wait until the workshop extracts a durable note, source analysis, instruction, or proposal.
- The strongest durable follow-up is not an edge but extraction: if the workshop promotes anything, the likely note/proposal should separate generated-procedure validity, observation validity, decision value, and selection/audit validity rather than treating "adaptive eval generation" as one mechanism.

## Flags

- The source is provisional raw workshop text with an explicit non-endorsement status. Treat all candidate edges as working-context recommendations, not durable graph state.
