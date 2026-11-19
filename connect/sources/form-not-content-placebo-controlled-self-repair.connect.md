---
description: "Pre-ingest connections for PoPE's placebo-controlled error-conditioning evaluation and its bounded null results"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/form-not-content-placebo-controlled-self-repair.md"
source_has_frontmatter: true
date: "2026-09-19"
depth: standard
---

# Connection Report: Form, Not Content?

**Source:** [Form, Not Content?](../../../../sources/.snapshots/form-not-content-placebo-controlled-self-repair.md)

Produced with `cp-skill-connect` for pre-ingest discovery. The immutable snapshot is the input; the matching ingest is the future authored surface. All edges below are candidates.

## Discovery Trace

- Read the sources collection contract, reports collection contract, connect-report type, and source paper, including methods, results, discussion, and appendices. Source has no tags. Read the notes, reference, agent-memory-systems, agentic-systems, and sources README heads; additionally read learning-theory and evaluation tag heads. Neither tag head declares completeness.
- Generated a fresh title surface using `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. Large combined output was truncated; scoped searches below supplied candidate resolution. No similarity scores were used.
- Notes: `rg -n -i 'placebo|falsification|self.repair|independent.*evaluat|content.*form' kb/notes/ --glob '*.md' --glob '!*-README.md'` and description filtering with `placebo|ablation|contrast|falsif|oracle|sampling|search.*evaluat` identified the experimental-contrast, activation, diagnostic-richness, oracle-accumulation, and mechanistic-Popperian notes. Read those candidates. Retained the contrast note as direct methodological evidence; retained oracle accumulation as a comparison separating proposal conditioning from independent tests. Rejected diagnostic richness as a contradiction: its necessity claim does not promise that a small generator can exploit every supplied diagnostic.
- Reference: `rg '^description:' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md' | rg -i 'ablation|falsif|self.correct|self.repair|reflexion|scientific|causal|evaluation'` found the ablation-baselines proposal. Read it and retained a sparse companion link: PoPE supplies a concrete control-design example, not evidence that Commonplace earns its cost.
- Agent-memory-systems: the same description query and README identified Reflexion. Read its code-grounded review; retained comparison of failure-derived prompt advice against PoPE's controlled attribution question, without treating different models or tasks as a direct replication.
- Agentic-systems: README/title scan plus `rg -n 'self.repair|placebo|falsif' kb/agentic-systems/ --glob '*.md'` yielded no comparably direct target. Generic self-improving harness matches would add topical rather than discriminating connections; none retained.
- Sources: description query found the self-evolver intervention ingest. Read it; retained comparison on content-preserving/form-preserving control design and the distinction between causal uptake and benefit.
- Link following: experimental-contrast note leads to the self-evolver ingest and diagnostic-richness note; oracle accumulation leads to oracle strength and warranted-oracle-domain concepts. The existing contrast note already states the general attribution bound, so a new general note is unnecessary.
- External: no prospecting. The source URL already supplied by the capture is the sole external candidate. Excluded instructions and workshops were not prospected.

## Connections Found

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **is-evidence-for**: the signal-versus-content gates and withdrawal of the unequal-draw allocation positive instantiate why credit depends on the actual control; preserved scaffold components do not imply exact token or lexical matching.
- [Oracle accumulation improves selection for later candidates](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) — **compares-with**: both separate failure information retained to guide generation from checks reapplied to new candidates. PoPE's interpretation concerns the operational position of criticism; it does not test long-term oracle accumulation.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) — **see-also**: its proposed Commonplace comparison needs controls that distinguish benefit from semantic contribution; PoPE offers an explicit two-gate design and matched-output-budget caution for that design work.
- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md) — **compares-with**: both return failure-derived material before retry, but PoPE specifically asks whether task-relevant error content beats its scaffold-matched placebo; the review's aggregate memory comparisons do not establish that finer attribution.
- [Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) — **compares-with**: both perturb semantic content while retaining parts of the delivery form. The self-evolver study measures behavioral dependence across memory representations; PoPE measures content-attributable public-screen superiority in small code models, which is a different endpoint.
- [Original paper](https://arxiv.org/abs/2607.12962) — **derived-from**: the future ingest analysis is worked out from this supplied paper.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) could cite the future name-paired ingest with **evidenced-by**, authorized by the notes contract, for the budget-confounded allocator positive and its preserved supersession. Citation must target the ingest, never this snapshot, and require its relevant quotes or `(snapshot required)`.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md): useful background, but failure to confirm superiority does not establish absence of causal activation. Keep the finer contrast and self-evolver connections instead.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md): this is not contradicted by PoPE. Available information and the generator's capacity to exploit it are distinct; no need to manufacture a disagreement.
- [Mechanistic constraints make Popperian KB recommendations actionable](../../../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md): shared Popperian vocabulary is insufficient. PoPE does not test falsifier blocks, contradiction-first connection, or rejected-interpretation capture.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md): PoPE evaluates conditioned generation, not whether a model can judge invalid arguments with correct conclusions.

## Index Membership

None

## Synthesis Opportunities

None. The attribution and proposal-versus-check distinctions already have note owners.

## Maintenance Observations

None

## Flags

- Preserve the narrow scope: 40-unit resistant band, 1.5B headline model, one scaffold and adapter setup, four output generations per arm-unit, public-tier screening. Hidden-tier confirmation was not spent. Equal output counts do not mean equal input tokens, FLOPs, or training cost.
- Non-significant and tied results do not establish equivalence, placebo superiority, or a general impossibility of useful error conditioning. Interpretation about the external role of criticism is not a mechanism identified by the experiment.
- Source artifacts and experiment records are available only on reasonable request; the paper reports them but does not provide a public experiment deposit. Cycle-log scale observations and inherited results must remain distinguishable from new frozen primary results.
- The snapshot's known DOI-as-date validator issue has an authorized exception. Do not edit snapshot bytes.
