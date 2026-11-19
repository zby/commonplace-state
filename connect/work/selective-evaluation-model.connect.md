---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/work/causal-impact-selective-evaluation/selective-evaluation-model.md"
source_has_frontmatter: false
date: "2026-08-21"
depth: standard
---

# Connection Report: A provisional causal selective-evaluation model

**Source:** [A provisional causal selective-evaluation model](../../../../work/explanatory-theories-deployment-time-learning/selective-evaluation-model.md)

This closing-cycle report is provisional because the byte-stable source is a raw workshop document without frontmatter.

## Discovery Trace

**Collection rules and curated heads:**

- Read `kb/work/COLLECTION.md`. It authorises prospecting in `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `instructions`, `sources`, and peer `work`. Workshop labels are permissive, but every connection still has to pass the articulation test. The contract also forbids durable library collections from linking into `kb/work/`.
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/instructions/README.md`, `kb/sources/README.md`, and `kb/work/README.md`. The source has no `tags:`, so there were no matching tag READMEs or `complete: true` marks to inspect.
- Generated each complete fresh title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: 355 note titles, 136 reference titles, 173 agent-memory-system titles, 12 agentic-system titles, 46 instruction titles, 532 source titles, and 582 workshop titles.
- Ran the complete description listing `rg '^description:' kb/<destination>/ --glob '*.md'` for every authorised local destination. No search score was available from repo-local tools.
- External prospecting was skipped. `external` is authorised, but no already-known external target was supplied and connect does not browse the open web.

**Notes:**

- Body searches were `rg -n -i "applicab|inapplicab|selective evaluation|evaluation obligation|evidence acquisition|residual risk|impact closure|theory error|omitted (check|evaluation)|counterfactual" kb/notes/ --glob '*.md'` and `rg -n -i "evaluation (set|procedure|policy|budget)|selector|uncertain(ty)?|calibrat|value of information|risk tolerance|acceptance criterion|commitment rule" kb/notes/ --glob '*.md'`.
- Kept [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md): `pi` uses impact beliefs to route expensive assessment, so the candidacy/verdict evidence distinction prevents that routing signal from deciding acceptance. Kept [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md): it states the source's matching, dependency, and bounded-impact locality preconditions directly. Kept [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md): it supplies the warrant boundary that changes when applicable evidence is omitted.
- Kept [Verification needs a typed target before it needs an oracle](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md): the open choice among functions, obligations, causal relations, or a layered registry must be settled enough for `M` to map a declared target class to a procedure. Kept [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md): it supplies the assumption-relative boundary for `C`, `S`, and theory error. Kept [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md): its definite-miss, uncertain-membership, and missed-boundary-error discipline transfers directly to mechanical inapplicability versus uncertain evaluation omission.
- Rejected [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md): it governs evidence available to the next proposer, not which obligations are observed for the current candidate. The source's existing links to the three-way diagnosis, observer-relative information value, and theory-mediated sample efficiency already carry those connections and were not duplicated.

**Reference:**

- Body search was `rg -n -i "selective evaluation|evaluation (set|procedure|obligation|policy|budget)|selector|applicab|inapplicab|evidence acquisition|residual risk|impact closure|dependency.*review|acceptance criterion|commitment rule|calibrat" kb/reference/ --glob '*.md'`.
- Kept [Generalized validation invalidation and imperative extension](../../../../reference/proposals/generalized-validation-invalidation-and-imperative-extension.md): its worked inverse-selector analysis states the old/new state, deletion, path-existence, dependency-closure, and conservative-fallback requirements that deterministic reachability must satisfy. Kept [Gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md): its fixed-token-budget loading policy is a direct consumer of this model and must not treat budget-omitted applicable gates as mechanically inapplicable. Kept [Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md): its self-concealing false-negative mechanism and independently sampled field calibration sharpen the source's omitted-region audit problem.
- Rejected [Factored dependency pairs for review freshness](../../../../reference/proposals/factored-dependency-pairs-for-review-freshness.md): it tracks when review evidence becomes stale, not whether a behavioral obligation is causally reachable or may be omitted from candidate evaluation.

**Agent-memory systems:**

- Body search was `rg -n -i "selective evaluation|evaluation (policy|budget|set|procedure)|gate(s|d)? changes|regression checks|selector|causal|impact|held-out|calibrat|false negative|full suite|acceptance" kb/agent-memory-systems/ --glob '*.md'`; the exact-name search `rg -n -i "continual harness|harness continual learning|HCL" kb/agent-memory-systems/ --glob '*.md'` returned no match.
- Kept [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md): it supplies a code-grounded comparator with a promoted regression suite, test-score gate, and explicit promotion boundary over retained evaluation obligations. Rejected [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md): its strongest relevance is diagnostic access for candidate generation, not candidate-specific evaluation selection.

**Agentic systems:**

- Body search was `rg -n -i "evaluation|regression|gate|acceptance|selector|causal|impact|held-out|calibrat|rollback|verification" kb/agentic-systems/ --glob '*.md'`.
- No candidate passed. [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) has a cheap failed-probe inner loop and a fuller release profile, but neither is selected by an explicit impact theory; retaining it would imply a stronger causal-selection mechanism than the analysis establishes. Exo, Eigenius, Autogenesis, and GBrain likewise provide gate or verification cases without the source's obligation-selection mechanism.

**Instructions:**

- Body search was `rg -n -i "selective evaluation|evaluation (policy|budget|set|procedure)|applicab|inapplicab|selector|residual risk|full suite|all gates|acceptance criterion|calibrat|false negative" kb/instructions/ --glob '*.md'`.
- No candidate passed. [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) implements the conservative all-applicable-gates baseline and lets the selector skip only mechanically inapplicable gates, but its note-review procedure is a cross-domain example rather than evidence for harness-impact selection. `run-review-batches.md` is the lower-level execution procedure for that same policy.

**Sources:**

- Body search was `rg -n -i "selective evaluation|evaluation selection|evaluation budget|regression checks|residual risk|theory error|omitted (check|evaluation)|impact theor|causal impact|impact closure|evidence acquisition|full(-| )suite|sentinel|randomized exploration|calibrat.*selector|selection.*evaluation" kb/sources/ --glob '*.md'`. A focused follow-up used `rg -n -i "SPADE|adaptive synthetic executable|procedure generation|synthesi[sz].*procedure|causal"` over the SPADE, DoWhy, invariant-prediction, and invariant-risk ingests.
- Kept [DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions](../../../../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md): it makes causal assumptions explicit while showing that validation remains partial, directly supporting the source's distinction between conditional modeled risk and impact-theory error.
- Rejected [Ingest: Harness Continual Learning](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) as a new edge because the source already routes to it through the linked HCL reading. Rejected [Ingest: SPADE](../../../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) as a new edge because the linked experiment design already scopes it as a procedure-generation analogy rather than evidence for causal selection. Invariant prediction and invariant-risk minimization remain better reached through the retained formal-systems note.

**Peer workshops:**

- Body search was `rg -n -i "selective evaluation|evaluation (policy|budget|set|procedure|obligation)|applicab|inapplicab|residual risk|impact theor|causal impact|impact closure|evidence acquisition|omitted (check|evaluation)|full(-| )suite|sentinel|randomized exploration|calibrat.*selector|selection.*evaluation" kb/work/ --glob '*.md'`.
- Read the containing workshop README, HCL reading, experiment design, and both author invitations. The source already links the HCL reading and experiment design; the README already routes to the two invitations, so those sibling restatements do not need additional source edges.
- Kept one reverse edge from [Continual Harness governance experiment](../../../../work/continual-harness-governance-experiment/README.md): its direct-update architecture deliberately lacks a separately rejectable candidate, so this proposal-selection model is a useful explicit contrast rather than an assumed universal gate.

**Link following:**

- Followed the localized-retention link to [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md). It confirmed that bounded validation radius is the larger payoff, while localized retention states the source's three preconditions more precisely.
- Followed candidacy evidence to [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md). It confirmed the non-distribution rule behind keeping impact beliefs in a routing role.
- Followed verification-target to warranted autonomy, and formal-systems to DoWhy and invariant-risk. Followed gate learning to its calibration proposal. These neighborhoods supported the retained candidates without adding weaker duplicate edges.
- Followed Auto Harness into the trace-learning comparison; the concrete review remained the better target because it carries the actual suite-promotion and gate mechanism.

All candidate and rejected-candidate paths named below were verified to exist.

## Connections Found

- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) — **rests-on**: impact beliefs can route costly evidence acquisition, but candidacy-grade routing evidence cannot itself warrant adoption or turn omitted obligations into satisfied ones.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) — **rests-on**: it supplies the matching units, explicit dependencies, and bounded impact closure under which the locality hypothesis could actually reduce evaluation work.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — **rests-on**: selecting only some applicable checks narrows or changes the gate's warranted domain; it cannot silently preserve a full-set acceptance claim.
- [Verification needs a typed target before it needs an oracle](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md) — **rests-on**: `M` cannot provide reusable procedure coverage until functions, obligations, causal relations, or another registry object define the target class each procedure verifies.
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — **rests-on**: causal exclusions are warranted only inside declared variables, assumptions, intervention classes, and translation boundaries, which is the source's separate theory-error term.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) — **extends**: its definite-miss versus uncertain-membership discipline maps onto mechanical inapplicability versus uncertain omission, while its missed-boundary errors motivate auditing false exclusions rather than only observed fallback.
- [Generalized validation invalidation and imperative extension](../../../../reference/proposals/generalized-validation-invalidation-and-imperative-extension.md) — **draws-on**: its inverse-selector case shows why current reads do not determine precise impact and why deterministic reachability needs old state, deletion handling, dependency closure, and conservative fallback.
- [Gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md) — **constrains**: its budget-based gate loader is a concrete design to which the model applies; a relevant gate omitted for token cost remains an evidence gap unless a different commitment rule accounts for it.
- [Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) — **extends**: a gate that never fires and a selector that never audits omitted checks share a self-concealing false-negative problem, so both require independently sampled observations outside the path that produced the apparent success.
- [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) — **evidenced-by**: this code-grounded system supplies a promoted regression suite, test-score gate, and retained obligation case against which a selective procedure registry can be compared.
- [DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions](../../../../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) — **evidenced-by**: DoWhy makes causal assumptions explicit while stressing that they can be validated only partially, grounding the distinction between modeled residual risk and error in the impact theory itself.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Continual Harness governance experiment](../../../../work/continual-harness-governance-experiment/README.md) → source — **contrasts**: that workshop studies governance for a direct-update architecture without a separately rejectable candidate; a link to this model would make the proposal-selection alternative and its changed acceptance semantics explicit.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — concerns evidence available to the next proposer, not current-candidate obligation selection.
- [Factored dependency pairs for review freshness](../../../../reference/proposals/factored-dependency-pairs-for-review-freshness.md) — tracks staleness of accepted evidence rather than causal reachability or selective evidence acquisition.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) — provides rich diagnostic traces for candidate generation but no impact-based evaluation selector.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) — its failed-probe inner loop and full release profile are useful evaluation schedules, but neither is justified by a candidate-impact theory.
- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) — implements the full-applicable-set baseline in a different domain; the cross-domain analogy is not load-bearing enough for a source edge.
- [Experiment design for causal selective evaluation](../../../../work/explanatory-theories-deployment-time-learning/experiment-design.md) — already linked and already carries the selector-comparison and adaptive-procedure details.
- [Ingest: Harness Continual Learning](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) — already routed through the linked HCL reading and its source-analysis passage.
- [Ingest: SPADE](../../../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) — already routed through the linked experiment design, where it is scoped as a procedure-generation analogy rather than evidence for the selector.

## Index Membership

None.

## Synthesis Opportunities

None. The strongest combinations—impact beliefs route assessment without becoming verdict evidence, mechanical non-applicability differs from uncertain omission, and omitted regions require independent observation—are already explicit in the source and are better treated as split candidates during promotion than as new synthesis notes now.

## Maintenance Observations

None.

## Flags

- **Provisional source:** the target has no frontmatter and explicitly presents unvalidated workshop machinery.
- **Split candidate on promotion:** the document independently develops an evaluation ontology, impact-model objects, selector taxonomy, acceptance semantics, selective-observation/calibration failure, and locality/cost bounds. If the workshop closes by promoting durable conclusions, those claims likely need separate artifacts even though keeping them together remains useful in the workshop.
- **Evidence-role boundary:** probabilistic impact beliefs can carry candidacy-grade routing force; only a mechanically complete non-influence proof could carry verdict-grade exclusion force. A future write should preserve that distinction.
- **Closing-cycle stability:** the source checksum remained `fa3e28b088a15538f75eea89b6542348b76b7c673a7ad0dce351fe767524e612` throughout discovery; this report therefore reflects repository-state discovery over unchanged target bytes.
