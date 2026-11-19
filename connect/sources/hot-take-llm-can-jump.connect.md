---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/hot-take-llm-can-jump.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Hot Take: LLM can 'jump'

**Source:** [Hot Take: LLM can 'jump'](../../../sources/hot-take-llm-can-jump.md)

## Discovery Trace

**Source reading:**

- Read the complete 103-line snapshot. Its central move is to challenge the necessity of Einstein's sensory-abductive route by changing the available knowledge: once special relativity, quantum field theory, and empirical properties of gravity are available, a Feynman-style consistency argument can reconstruct general relativity largely deductively. The author explicitly limits this to reachability from later knowledge and concedes that reconstruction of a known result is easier than first discovery.
- The essay then generalizes from that example to an interconnected-knowledge account: cross-domain facts constrain candidate explanations, models propose connections, and tools or experiments verify them. It separately claims that censored knowledge may be reconstructed and predicts easier continual learning as model knowledge becomes denser. The essay's broad continual-learning definition includes task-time use of new context with no persistent update.

**Curated heads and complete title surfaces:**

- Read `kb/notes/README.md`, `discovery-README.md`, `learning-theory-README.md`, and `deploy-time-learning-README.md`. The discovery head has `complete: true`; no redundant discovery-tag `rg` sweep was needed. It foregrounded the discovery lifecycle, known-target reachability, recognition, and missing-oracle candidates. The learning heads foregrounded the system boundary, durable adaptation, and the distinction between pre-training, in-context use, and deploy-time learning.
- Generated the complete `# ` title listings for `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. Relevant titles appeared in notes and sources. The reference listing concerned shipped Commonplace state rather than the essay's theoretical claims. The agent-memory and agentic-system listings describe concrete systems; the essay does not analyze a memory implementation or harness closely enough to warrant those destinations.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md` to confirm those collection boundaries before skipping deeper prospecting there.

**Description listing scans:**

- `rg '^description:' kb/notes/ --glob '*.md' | rg -i 'discover|abduct|deduct|hypothesis|knowledge|continual|deploy-time|training|execution|fixed|decomposition|world model|verification|retention|interconnect|reconstruct'` -- kept the known-target, fixed-decomposition, deployed-system, continual-learning, and discovery-lifecycle notes; rejected generic knowledge-storage and context-retrieval matches that did not address premise generation or learning persistence.
- `rg '^description:' kb/sources/ --glob '*.ingest.md' | rg -i 'scientific|discover|insight|abduct|deduct|knowledge|continual|studying|reconstruct|multi-hop|unlearn|censor|implicit|interconnect|world model'` -- kept the direct `LLMs can't jump`, Machine Studying, and GIANTS comparisons. Model Discovery Agent and DiscoverPhysics were evaluated but rejected because the earlier `LLMs can't jump` ingest already supplies their more precise role as bounded empirical counter-pressure.
- No source tags were present, so no tag-derived destination scan was available from the artifact itself.

**Body searches:**

- `rg -n -i "abduct|deduct|scientific discover|known.target|hypothesis|interconnected|knowledge graph|reconstruct|censor|unlearn|continual learn|weight space|deploy.time|execution.time|training.time|fixed decomposition|update space|world model|proposal.selection|machine studying" kb/notes/ --glob '*.md'` -- confirmed that the Feynman route belongs under known-target reachability, while the essay's propose-check loop separates search from verification but does not establish open-ended candidate selection.
- `rg -n -i "training[- ]time|execution[- ]time|deploy[- ]time|pretraining|pre-training|weight space|in-context learning|new knowledge|knowledge.*training|training.*knowledge" kb/notes/ --glob '*.md'` -- found the durable-write and three-timescale distinctions that the essay's broad continual-learning definition collapses.
- `rg -n -i "censor|harmful knowledge|dangerous knowledge|unlearn|redact|dual.use|implicit information|reconstruct.*removed|remove.*knowledge" kb/notes/ --glob '*.md'` -- found memory-lifecycle redaction notes, but rejected them because they govern stored traces and artifacts rather than claims about reconstructing censored pre-training knowledge.
- `rg -n -i "Astra|unit-distance|algebraic number theory|discrete geometry|Feynman|general relativity|reconstruct.*knowledge|implicit knowledge|knowledge deletion|knowledge filtering|machine studying|interconnected knowledge|multi-hop" kb/sources/ --glob '*.md'` -- confirmed the direct dispute with the captured Zahavy paper and the existing Machine Studying treatment. No durable local capture of the Astra unit-distance announcement was found.

**Link following:**

- Followed [LLMs can't jump](../../../../sources/llms-cant-jump.ingest.md) into the fixed-decomposition, known-target, proposal-selection, formal-system, and world-model notes. The new essay directly bears on the ingest's limitation that Zahavy's categorical conclusion outruns a single historical route, but its later-knowledge setup does not answer Zahavy's narrower Einstein-era question.
- Followed [known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) into GIANTS and the verification boundary. The essay independently states the same critical limitation: Feynman's derivation reconstructs a known result and does not show inevitable first discovery.
- Followed [the deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) into fixed decomposition, proposal selection, and Machine Studying. The essay's tool-using scientist is a model-plus-simulators/checkers/wet-lab system, not an isolated LLM.
- Followed [continual learning requires governing behaviour-changing writes](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) into in-context learning and representational-form coevolution. This exposed a substantive terminology tension: task-time use of supplied information changes current behavior but is not by itself durable cross-session learning under the KB's criterion.

## Connections Found

- [Ingest: LLMs can't jump](../../../../sources/llms-cant-jump.ingest.md) -- **compares-with**: this is a direct counterpoint, but it changes the premise boundary from knowledge available to Einstein to later quantum-field-theory knowledge. It weakens the categorical claim that general relativity has only a sensory-abductive route without showing that a current system could originate the theory from Einstein-era inputs.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -- **rests-on**: the essay's own caveat that Feynman knew general relativity and was reconstructing a known result places its example squarely in the note's reachability category rather than closing prospective discovery.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) -- **rests-on**: the essay's general proposal-generation, consequence-checking, and iterative empirical-validation account instantiates the lifecycle's conjecture, deduction, and test stages even though it uses “jump” more broadly than the definition's accepted-discovery boundary.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **compares-with**: dense cross-domain knowledge and general-purpose tools can enlarge an agent's effective hypothesis and action space behind an unchanged interface. The Feynman route demonstrates a candidate path inside that enlarged space; it does not show that every representational change is reachable or validate the fixed ontology and tool basis that made the path expressible.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: the essay's proposed scientific reasoner explicitly combines model inference with code, Lean, simulation, and wet-lab feedback, providing a clear conceptual case where the relevant capability belongs to the deployed model-tool system rather than bare weights.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **compares-with**: the essay counts successful task-time use of unseen information as continual learning even when no weights or retained artifacts change. The KB reserves continual learning for a durable, evidence-responsive behavior change, so the essay's second prediction must be split into in-context adaptation and persistent learning.
- [Ingest: Machine Studying](../../../../sources/machine-studying.ingest.md) -- **compares-with**: both ask how a model-agent uses knowledge absent from its original training, but Machine Studying isolates corpus-only preparation before downstream tasks while this essay permits task-time background information and treats successful use itself as learning.
- [Ingest: GIANTS](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md) -- **compares-with**: GIANTS empirically tests a bounded version of the essay's interconnected-knowledge thesis by reconstructing a known downstream insight from selected parent papers; its manufactured target and fixed parent pair show both the plausibility and the reachability-only limit of cross-source synthesis.

## Bidirectional Candidates

- [Ingest: LLMs can't jump](../../../../sources/llms-cant-jump.ingest.md) <-> source -- **compares-with**: readers of either analysis need the other because the disagreement turns on a changed knowledge-time boundary, not simply opposing verdicts about one fixed task.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) <-> source -- source **rests-on** the note's distinction, while the note could use the essay as **evidenced-by** a critic who explicitly concedes that known-result reconstruction does not establish first discovery.

## Reverse-edge Candidates

- [Ingest: LLMs can't jump](../../../../sources/llms-cant-jump.ingest.md) -> source -- **compares-with**: add the response as the most direct durable counterpoint to the ingest's categorical-claim limitation, with the later-knowledge qualification stated in the link context.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -> source -- **evidenced-by**: the response supplies a particularly clean self-limiting reconstruction case because its author both offers a later-knowledge derivation and denies that this proves independent rediscovery.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) -- rejected because the response proposes a non-sensory route to one theory but does not challenge the note's distinct claim that interventions can test a retained world model's reach.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- rejected as a direct edge because the essay clearly describes proposal and verification but says little about operative retention; the discovery-lifecycle and continual-learning notes capture the useful distinctions more precisely.
- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) -- rejected because the essay's safety claim concerns reconstruction from implicit parametric knowledge after pre-training censorship, whereas this requirement governs artifact and trace lifecycle operations.
- [Ingest: Model Discovery Agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) -- rejected as duplicative: it is useful empirical pressure on hypothesis proposal inside a fixed space, but that role is already synthesized in the `LLMs can't jump` ingest and the fixed-decomposition note.
- [Ingest: DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) -- rejected as duplicative: its counterfactual-world results concern prediction/explanation separation, while the response's distinctive contribution is the later-knowledge route and its continual-learning extrapolation.

## Index Membership

None. This is a source snapshot whose durable authored surface will be its ingest report; the curated discovery and deploy-time-learning tag heads index notes, not raw sources.

## Synthesis Opportunities

None. The higher-order distinction implied by the two “jump” sources -- reachable reconstruction from later premises versus prospective invention from an earlier knowledge state -- is already stated by [known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md).

## Maintenance Observations

None

## Flags

- The headline disagreement is asymmetric. Treating this source as a simple contradiction would erase the changed temporal knowledge boundary: Zahavy asks about invention from Einstein-era knowledge, while Zheng-Xin's strongest worked route begins from later quantum field theory.
- “Continual learning” is used with a materially broader boundary than in the KB. Any ingest should preserve the author's prediction while separating ephemeral in-context use from durable weight or artifact updates.
