---
description: "PAST-Bench connection candidates for effects-based memory evaluation, activation, supersession, and bounded persistence attribution"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/past-bench-recursive-self-improvement-personal-agents.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: PAST-Bench

**Source:** [PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents](../../../../sources/.snapshots/past-bench-recursive-self-improvement-personal-agents.md)

This report supplies candidates for the later authored ingest. The snapshot is immutable. Durable source-dependent links must target the eventual tracked ingest, not this snapshot or this cache report. Discovery used the cp-skill-connect procedure with repo-local reads and searches; model identity supplied by the runtime is GPT-6. No web browsing or implementation reproduction was performed.

The captured paper is a partial-source HTML extraction: prose and appendices survive, but mathematical notation, many numeric table cells, and figure contents do not. Connections below rely on retained prose and intact data, not reconstructed equations or rankings.

## Discovery Trace

**Authorization and breadth:** Read the source collection contract and report type before prospecting. Sources authorize notes, reference, agent-memory-systems, agentic-systems, and other sources. The contract's `agent-memory` label destination denotes the agent-memory-systems collection. Instructions and work are excluded. External URLs already in context are allowed, but external prospecting is not. Read notes and agent-memory collection contracts for possible return edges. The snapshot has no tags, so tag-matching searches were not required; topical heads were used manually. No complete-tag mark caused a skipped search.

**Curated heads:** Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. Followed the notes navigation into `kb/notes/agent-memory-README.md`, `kb/notes/evaluation-README.md`, and `kb/notes/agent-memory-requirements/README.md`. The memory head identified effects, activation, and lifecycle as distinct requirements; the evaluation head offered prompt-testing methods but no closer persistence benchmark entry.

**Complete title surface:** Generated the fresh title listing with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. The first combined display truncated; reran with a larger capture and read its complete output in slices. Flagged the storage/activation, effects, personalization, contrast-grain, and diagnostic-richness notes; the memory gap plan; Hermes; LongMemEval; faithful self-evolvers; and the fragility study. Autogenesis and Exo were examined as possible broader-system comparisons, then rejected as insufficiently specific for this ingest.

**Notes:** Ran `rg -n '^description:.*(persist|activation|behavior|behaviour|causal|memory|skill|ablation|harness)' kb/notes/ kb/reference/ --glob '*.md'`. This identified the same principal claims plus flat-memory contamination, skills packaging, and final-task-success/intended-path-health. Read the principal notes and requirements in full. Ran `rg -n -i 'persistence.on|persistence.off|mechanism.evidence|matched (ablation|control)|PAST.Bench' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`; no existing PAST-Bench analysis surfaced. The contrast-grain note was kept because it supplies the exact limit on attributing a persistence-toggle effect to one artifact. Flat-memory and skill-packaging notes were rejected as stronger or different claims than the source tests.

**Reference:** The shared description and title scans found the Commonplace memory gap plan. Ran `rg -n -i 'hermes|fresh.session|stale.*(rule|memory)|memory.*ablation' kb/agentic-systems/ kb/agent-memory-systems/reviews/hermes-agent.md kb/reference/ --glob '*.md'`. The gap plan's step 8 explicitly calls for WITH/WITHOUT and perturbation checks. Read the whole plan; kept one sparing companion link to that unmet evaluation requirement. Review freshness and collection-contract proposals do not test retained user-state benefits and were not promoted from title hits.

**Agent memory systems:** The collection head and title surface led directly to Hermes. The Hermes body query above exposed its separate memory, skills, session-search, and background-review paths; full review reading plus a bounded reread covered the initially truncated middle. Kept a comparison on persistence surfaces and read-back evaluation, explicitly preserving the paper's April release versus the review's pinned July code boundary. Other system names mentioned in the paper do not justify a spray of comparisons. No matrix or historical verdict update is proposed.

**Agentic systems:** Ran `rg -n '^description:' kb/agentic-systems/ --glob '*.md'`, then `rg -n -i 'persistence|evaluation|ablation|benchmark|held.out' kb/agentic-systems/reviews/autogenesis.md kb/agentic-systems/reviews/exo.md`. These results concern mutation/rollback and weak adoption gates rather than the paper's matched retained-state evaluation. Rejected both for this standard-depth report; there is no retained outbound candidate for this destination. Pond's Hermes adapter is a name match, not evidence about the benchmarked Hermes configuration.

**Other sources:** Ran `rg -n '^description:.*(Hermes|evol|memory|faithful|attribution|harness)' kb/sources/ kb/agentic-systems/ kb/agent-memory-systems/ --glob '*.md'`; the broad output was narrowed with `rg -n '^description:.*(LongMemEval|Faithful|faithful|Fragility|attribution|Attribution|Updating|update|persistence)' kb/sources/ --glob '*.md'`. Read LongMemEval, faithful self-evolvers, and fragility ingests in full. Ran `rg -n -i 'mechanism|ablation|variance|causal|persistence'` over those three ingests and `kb/notes/agent-memory-requirements/`. Kept comparisons on evaluation unit, causal intervention grain, and sequence/repetition coverage. These are comparisons of retained source analyses, not independent verification of their papers.

**Link following:** From the memory head followed the requirements hub into effects, activation, and retirement. From effects and the storage/activation note followed the faithful-self-evolvers ingest; from that ingest followed the contrast-grain note. From the intended-path-health note followed diagnostic richness. From Hermes followed its storage/activation link. These hops sharpened the distinction between a visible pathway, causal use of specific content, and beneficial downstream results. Rejected a separate intended-path-health edge because its failed-helper/fallback setting would add a less direct analogy beside the memory-specific links.

**External:** The source URL is already in the snapshot and can be cited as `derived-from` by the ingest. No external search was run and no further external candidate was needed. Search results have no semantic scores. Every local Markdown target in this report was checked to exist.

## Connections Found

All entries are recommendations for the future ingest's authored surface.

- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — **is-evidence-for**: the paper separates persistence-on task outcomes, matched persistence-off gaps, and trace-based mechanism evidence across fresh sessions (§§3.1–3.2, Appendix B). This gives the requirement a concrete multi-capability evaluation design. Mech indicates consistency with an expected pathway; it does not establish causal necessity of an individual memory.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: §4.3 diagnoses saved state that is not consulted during planning or before action, while §3 separates retained artifacts, reads, and later performance. This instantiates the storage-to-context/use distinction without claiming that trace presence proves semantic uptake.
- [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) — **is-evidence-for**: preseeded information-gathering tasks test whether the agent retrieves at the needed moment, and E1/E4 add plan-time consultation and a retrieval-before-answer check (§§3.1, 4.3). The paper reports capability-specific effects; it does not establish a universally effective retrieval gate.
- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) — **is-evidence-for**: Update families test correction, scoped migration, and expiry; E2 renders valid bindings while E5 writes and synchronously flushes corrected state (§§3.1, 4.3). This supports the supersession/temporal-validity part of the requirement, not redaction or every lifecycle operation.
- [Memory-backed personalization can look like model improvement](../../../../notes/memory-backed-personalization-can-look-like-model-improvement.md) — **is-evidence-for**: fixed-model persistence toggles and separate fixed-framework model comparisons distinguish retained-user-state benefit from model capability (§§3.2, 4.2, Appendix E.1). Their effects remain conditional on the model, adapter, synthetic family, and native context policy; they do not identify an intrinsic memory contribution across systems.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **is-evidence-for**: the source explicitly distinguishes isolated interventions, focused full-minus-one interactions, and cross-model transfer (§4.4), and proposes artifact deletion/replacement/corruption as a stronger future attribution test (§6). Its existing persistence-toggle comparison does not isolate one artifact's semantic influence.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **is-evidence-for**: the authors used low-gain traces to identify five runtime failure classes and formulate Hermes+ (§4.3); Appendix D.2 exposes a concrete skill-creation/read failure behind procedural regression. This is a diagnosis-to-design case, not an ablation of diagnostic access itself.
- [Hermes Agent](../../../../agent-memory-systems/reviews/hermes-agent.md) — **compares-with**: compare the reviewed memory/skill/history surfaces and absence of inspected behavioral faithfulness tests with PAST-Bench's external persistence experiment. The paper uses Hermes v2026.4.16 and frozen adapters; the review uses commit `d59b79fadd1e9edd7afc5c679cc3b143838e7c01`, checked 2026-07-18. Neither result should overwrite the other's implementation boundary.
- [LongMemEval](../../../../sources/longmemeval-benchmarking-chat-assistants-long-term-memory.ingest.md) — **compares-with**: conversational QA and indexing/retrieval/reading ablations versus fresh-session executable task families with persistence controls. Both separate memory-path stages; PAST-Bench adds procedural reuse and action/update tests without subsuming every LongMemEval ability.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) — **compares-with**: artifact-content perturbations test behavioral dependence, whereas PAST-Bench combines retained-state access toggles with expected-path telemetry. The comparison clarifies why PAST-Bench's Mech score is not a substitute for content-level causal interventions.
- [On the Fragility of Self-Improving Agents](../../../../sources/on-the-fragility-of-self-improving-agents.ingest.md) — **compares-with**: repeated runs and shuffled learning orders test path dependence that PAST-Bench's isolated synthetic families leave outside their current scope. PAST-Bench itself warns that the Hermes+ aggregate gain is smaller than run-to-run variation (§4.4); no cross-paper numerical ranking is warranted.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) — **see-also**: step 8 names the local need for behavioral activation and WITH/WITHOUT evaluation; PAST-Bench supplies an external protocol to consider for that gap. This is a future design input, not a claim that Commonplace implements or has passed the benchmark.

## Bidirectional Candidates

None. Return evidence links are separated below; no reciprocal link is recommended merely to mirror an outbound entry.

## Reverse-edge Candidates

The notes contract authorizes `evidenced-by` into sources. These candidates would link to the eventual tracked ingest after the needed source support is retained or the link explicitly requires its pinned snapshot. They must not link durably to the current snapshot.

- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) → future ingest — **evidenced-by**: strongest return edge; add the matched cross-session protocol as a concrete example while retaining the distinction between expected-path evidence and causal uptake.
- [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) → future ingest — **evidenced-by**: use the preseeded weak-trigger tasks and E1/E4 interventions as bounded evidence for testing delivery before action.
- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) → future ingest — **evidenced-by**: use Update families and the E2/E5 design as an example where supersession must affect the next fresh session.

No return edit to the historical Hermes review is proposed. Its recorded code boundary should not be silently expanded by a differently pinned external benchmark.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) — conceptually useful, but its concrete scope is primary-tool failure and fallback success. Memory-specific outcome/path links above convey the source's contribution more directly.
- [Flat memory predicts specific cross-contamination failures](../../../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) — Appendix D.2 suggests competition between structured memory and skill routing, but the paper does not compare flat versus separated stores or establish this note's three contamination predictions.
- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) — E3 supports procedural storage, ranking, and patching, but does not test this note's harness-specific invocation and execution-policy distinctions.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) — its evolvable resource and smoke-gate architecture is too broad a comparison for the paper's retained-state attribution question; neither source evaluates the other's runtime.
- [Exo](../../../../agentic-systems/reviews/exo.md) — shared self-improvement terminology is insufficient. Executor rewriting and protected rewind address different update and recovery boundaries.

## Index Membership

None. The sources landing describes the workflow rather than enumerating every ingest. The agent-memory and evaluation tag heads are useful navigation during discovery, but this source has no note-tag membership and does not require a new entry there.

## Synthesis Opportunities

None promoted. The existing effects, activation, and experimental-contrast notes already express the strongest cross-source distinction. The E2/E3 procedural interaction could motivate a later hypothesis about ownership across memory surfaces, but one focused diagnosis does not yet establish a general synthesis.

## Maintenance Observations

The [faithful-self-evolvers ingest](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md), Extractable Value item 7, still recommends replacing external citations with a local snapshot path. That is incompatible with the current sources contract requiring durable links to tracked ingests. Its Connections Found text also calls snapshots reverse-edge-only, whereas the current connect contract recommends outbound candidates for an authored ingest. These are maintenance signals for a separate authorized edit; nothing was changed here.

## Flags

- **Capture boundary:** Do not recover missing formulas, table cells, numerical rankings, or figure trace contents from inference. Appendix D.4 retains the Overall 0.66/0.66 scores and +0.13/+0.15 gaps, but the source's prose says the gap difference is smaller than run-to-run variation. The largely empty variance table does not permit reconstructing uncertainty.
- **Attribution boundary:** Persistence-on/off measures access to a bundle of retained state. Mech uses expected artifact types, keyword/count signals, and read/update traces; the paper expressly says it is not causal proof. Alternative valid persistence pathways may be penalized by the expected-path contract.
- **Benchmark boundary:** All 26 families and 204 episodes are synthetic; families are isolated, and longer cross-family interference is future work. Native context policies differ across systems. Agent-Zero has a longer time budget, and ZeroClaw is its Python companion, so avoid unqualified framework rankings.
- **System boundary:** Hermes+ mechanisms are researcher-designed runtime changes, while the evaluated online adaptation is retained-state use without weight updates. Do not treat this as evidence that the agent autonomously improves its own learning mechanism.
- **Split candidate for later theory writing:** Seven note connections span evaluation/attribution, activation/routing, and temporal lifecycle. The source makes several independent assertions. Keep one ingest for source identity, but separate any later claim notes rather than promoting all findings into one theory artifact.
- **Verification:** All report sections are present; all candidate file paths exist; the immutable snapshot was only read. No blocker prevents the later ingest draft within this partial-source boundary.
