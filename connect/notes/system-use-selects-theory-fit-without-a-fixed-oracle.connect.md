---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/system-use-selects-theory-fit-without-a-fixed-oracle.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: System use selects theory fit without a fixed oracle

**Source:** [System use is an initial selection environment when theory fit lacks a fixed oracle](../../../../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md)

## Discovery Trace

**Authorisation and curated heads:**

- Read the source note, `kb/reports/types/connect-report.md`, and `kb/notes/COLLECTION.md` in full. The notes contract authorises prospecting in notes, types, reference, agent-memory systems, agentic systems, sources, instructions, and already-known external targets; it excludes `kb/work/`. No external target was supplied, so external prospecting was skipped.
- Read `kb/notes/README.md` and the three source-tag heads: `learning-theory-README.md`, `deploy-time-learning-README.md`, and `evaluation-README.md`. None declares `complete: true`, so no by-tag search was skipped. `learning-theory-README.md` routes this note through its `deploy-time-learning` child.
- Read the destination heads `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. The types surface had no plausible trigger beyond the already-resolved note contract; instructions were treated with their exceptional-outbound posture and inverse `instruction -> note` direction.

**Complete title and description scans:**

- Generated the complete title surface once per local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` across all seven local destinations.
- Ran the required tag-specific description queries for `learning-theory`, `deploy-time-learning`, and `evaluation`, in the form `rg -l '^tags:.*<tag>' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`. These surfaced the truth/value gate, weak-discrimination, oracle-accumulation, autonomy, and evaluator-construction candidates.

**Focused body search:**

- Notes: `rg -l -i "global[- ]fit|theory fit|fixed oracle|selection environment|validity.*learning-value|truth.*fit|operator.*judg|human-assisted|self-confirm|withhold|credit assignment|delayed feedback" kb/notes/ --glob "*.md"` -- kept the theory-mediated functional account, validity/value comparison, local-use limit, weak-discrimination mechanism, accumulating-oracle path, autonomy boundary, human-residue consequence, and bootstrap strategy.
- Reference: `rg -l -i "declared objective|ablat|human judgment|composition test|selection environment|oracle" kb/reference/ --glob "*.md"` -- kept the declared-objective ablation proposal; rejected the Commonplace instrument account as duplicative of the source's existing evidence-note link plus the more general local-use limit.
- Agent-memory systems: `rg -l -i "oracle|human.*(select|review)|feedback.*(select|learn)|self-improv" kb/agent-memory-systems/ --glob "*.md"` -- evaluated the comparative trace-learning surface, Pi Self-Learning, AgentFly, Meta-Harness, and Incremental Self-Improvement. Their memory-specific policy and ranking cases added less than the selected general oracle notes and the KSI source case, so none was retained.
- Agentic systems: `rg -l -i "oracle|human.*(select|review)|feedback.*(select|learn)|self-improv" kb/agentic-systems/ --glob "*.md"` -- kept Compound Engineering as a code-inspected case with heterogeneous gates, computational search, retained artifacts, and an explicit human/frozen boundary.
- Sources: `rg -l -i "validity and learning value|payoff|global fit|human judgment|selection environment|held-out transfer|distillation" kb/sources/ --glob "*.md"` -- kept Knowledge-Centric Self-Improvement for its split hard-outcome/soft-curation oracle and held-out artifact transfer; rejected the fixed-payoff Incremental Self-Improvement report as a contrast whose scalar oracle removes the target's defining difficulty.
- Instructions: `rg -l -i "blind|judge|accept|human|oracle|selection" kb/instructions/ --glob "*.md"` -- evaluated `cp-skill-revise-autoreason`, the full-improvement pass, and multistage writing. None needs this theory to execute, and their meta-reader rationale is already carried by narrower warrant and error-correction notes; no reverse `rests-on` edge was kept.
- Types: title and description scans found only structural contracts, so body prospecting was skipped for lack of a destination trigger.

**Link following and inbound check:**

- Ran `rg -n --fixed-strings 'system-use-selects-theory-fit-without-a-fixed-oracle.md' kb --glob '*.md' --glob '!reports/cache/connect/**'`. The bootstrap note, Bitter Lesson portfolio, and Commonplace revision evidence note already link to the source; the source already links back to the evidence note, but not to the bootstrap.
- Followed one hop from the theory-mediated functional note, validity/value gate, exact-implementation note, weak-discrimination note, oracle-accumulation note, warranted-autonomy note, and bootstrap. This exposed the existing local-use limit and the human-residue selection effect, and showed that the proposal-selection, delayed-feedback, fixed-decomposition, and sample-efficiency notes are already linked by the source.
- Loaded every kept target's substantive claim and caveats, then verified all kept, reverse-edge, rejected, and index paths with `test -f`.

## Connections Found

- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) -- **grounds**: separates semantic interpretation from independent exposure and read-back, locating global-fit selection as a missing evaluative function rather than as missing computation or retention.
- [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -- **contrasts**: its candidate-validity versus system-relative learning-value split is the nearest neighbouring decomposition; following it prevents the source's truth-versus-theory-fit distinction from being mistaken for an identical pair.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- **grounds**: shows why a hard local conformance oracle cannot establish that its target serves the larger objective, which is the same inferential break the source places between claim truth and global theory fit.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- **grounds**: bounds what the live system's use can establish by showing that one successful whole-configuration use licenses local replay, not a general rule or transfer claim.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) -- **mechanism**: explains how a proposal-selection loop can enrich mechanically checkable qualities more strongly than global coherence when the latter has a weaker discriminator.
- [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) -- **extends**: develops the source's proposal to convert recurring operator corrections into reusable checks, while bounding that growth to formalizable and independently calibrated failure domains.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **extends**: distinguishes merely handing high-level selection to an unattended model from earning computational selection over the cases its oracle can actually warrant.
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](../../../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) -- **extends**: predicts how growing selection machinery changes the remaining operator role: the residual judgments become enriched for missing premises, unsettled criteria, weak checks, and delayed consequences.
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- **extends**: turns the source's initial selection environment into a conditional strategy, comparison program, and explicit set of failure conditions; its existing `grounds` link back to the source makes both directions independently useful.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) -- **see-also**: supplies concrete matched arms for the source's proposed withheld/replaced-theory test and explicitly meters the human-judgment denominator that an internal-use comparison can conceal.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- **evidenced-by**: code inspection finds computational proposal, metric and test evaluation, retained project knowledge, and operator gates in one human-inclusive loop while the installed harness and semantic lesson acceptance remain partly frozen or externally selected.
- [Knowledge-Centric Self-Improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) -- **evidenced-by**: provides a bounded automated case in which symbolic task outcomes and LLM-mediated claim curation govern different parts of selection, while held-out transfer tests the retained bundle and leaves open-ended theory fit unresolved.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) -> source -- **extends**: the source supplies the explicit truth-versus-global-fit distinction and live-use selection strategy behind that note's unresolved oracle for judgment-heavy KB mutations.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -> source -- **extends**: the source broadens its comprehension-to-verifier sequence by explaining what remains when local evaluators exist but no complete evaluator decides fit within a working theory.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- rejected as a narrower memory-policy application whose delayed-feedback mechanism is already imported through the selected general oracle and human-residue notes.
- [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) -- rejected as a duplicative current-system account: the source already cites the episode evidence directly, while the selected local-use note states the transferable limit more cleanly.
- [On Learning How to Learn Learning Strategies](../../../../sources/on-learning-how-to-learn-learning-strategies.ingest.md) -- rejected because its scalar payoff-per-time gate is useful as a fixed-oracle contrast but does not bear directly on selection where global theory fit lacks such an oracle.
- [Experimentally revise a note with fresh critic, author, synthesizer, and blind-judge agents](../../../../instructions/cp-skill-revise-autoreason/SKILL.md) -- rejected as a reverse `rests-on` candidate: its prose-preservation tournament has a narrower acceptance contract and does not claim to decide global theory fit.
- [The Bitter Lesson defense portfolio has one load-bearing member for the form-only rebuttal](../../../../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) -- rejected as an additional outbound edge because it already links to the source and the bootstrap note gives the source reader the strategy-level development without importing the whole synthesis portfolio.
- The source's existing targets for proposal-selection machinery, delayed-feedback program theory, sample efficiency, fixed-decomposition risk, the production-method/form distinction, and the Commonplace episode were not re-proposed because those edges are already authored.

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) -- candidate entry under `Feedback and signal quality`: the source separates bounded truth checks from distributed theory-fit consequences and explains how recurring judgments can harden into selection machinery.
- [Evaluation](../../../../tags/evaluation-README.md) -- candidate entry because the source is a central evaluation claim under the tag: it distinguishes local warrant from relational fit and states the intervention evidence needed to test retained theory's causal contribution.

## Synthesis Opportunities

None. The higher-order implication that transferred work leaves a harder-to-warrant human residue is already owned by [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](../../../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md).

## Maintenance Observations

- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) has a legacy footer that predates the current notes link contract: it uses unregistered labels including `foundation`, `describes`, `addresses`, `sharpens`, `confirms`, `synthesis`, and `develops`, and several entries have no label. This is a separate maintenance issue, not a connection candidate.

## Flags

- **Split candidate:** the source makes several independently citable assertions across at least three clusters: truth versus theory fit and the live-use selection environment; the already-computational human-inclusive loop and its progress measures; and the provisional bootstrap strategy with non-uniqueness and failure conditions. The discovery pass found more than five useful targets across theory-mediated learning, oracle design, autonomy, and experimental evaluation. A future writer should test whether the first cluster remains here while the computational-loop accounting and strategy comparison move to or are fully delegated to their existing notes.
