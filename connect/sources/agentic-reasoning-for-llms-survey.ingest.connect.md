---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/agentic-reasoning-for-llms-survey.ingest.md"
source_has_frontmatter: true
date: "2026-11-16"
depth: standard
---

# Connection Report: Ingest: Agentic Reasoning for Large Language Models

**Source:** [Ingest: Agentic Reasoning for Large Language Models](../../../../sources/agentic-reasoning-for-llms-survey.ingest.md)

## Discovery Trace

Rules read: `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, sources, theory/definitions, external (`derived-from`, `see-also` only). `kb/work/` and `kb/instructions/` are excluded. `kb/tags/` is listed as a scan surface, but no label authorises tags as a destination, so tag heads were used only as curated routing heads. External prospecting was skipped: the only external target, the arXiv PDF, is already linked `derived-from`.

The source already has 11 footer links: the arXiv URL, five theory notes, three source ingests and one agentic-systems comparison. Its body also links three theory notes inline that its footer omits: reasoning production, fixed decomposition and flat memory. All are `known`. The search below looks for gaps beyond them.

**Curated heads:**
- `kb/tags/agent-memory-README.md` (not complete): surfaced the External Checks group (adaptation-survey note, oracle note). Both are already linked. It also surfaced the flat-memory note and memory-system comparisons such as `kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md`, which is not in the head but is reachable through the systems table neighbourhood.
- `kb/tags/self-improving-systems-README.md` (`complete: true`; by-tag rg skipped): pointed to the child heads and to the Autogenesis review ("versioned mutation with rollback").
- `kb/tags/improvement-loop-README.md` (`complete: true`; by-tag rg skipped): surfaced `a-proposal-selection-loop-requires-search-evaluation-and-retention.md`, `an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md` and `diagnostic-richness-constrains-outer-loop-learning-quality.md`.
- `kb/tags/continual-learning-README.md` (`complete: true`; by-tag rg skipped): confirmed that the coevolution, governing-writes, deployed-system and fixed-decomposition notes are the area's core. The source already links all of them except fixed decomposition, which it links only inline.
- `kb/tags/reflection-README.md` (`complete: true`): `reflection-buys-addressability.md` was evaluated and rejected (see below).

**Titles listing:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/sources/ --glob '*.md' --glob '!*.brief.md' | rg -i 'survey|self-evol|memory|reflex|voyager|alphaevolve|mem|skill librar|credit|agentic reason|continual|evolv|lifelong|experience'` returned about 65 titles. These were followed up: Reflexion; Agentic Memory (AgeMem); The What & When of Self-Evolving Agents; LLM Agents Are Not Always Faithful Self-Evolvers; Harness Continual Learning; Multi-Agent Memory from a Computer Architecture Perspective; Letta (MemGPT); Symbolic Learning; Next-Generation Agentic RL Systems; Continual Learning in Token Space; Agent Plasticity; Memory Scaling. Paths were resolved with `rg -l -F -x '# <title>' kb/sources/`, and each ingest's description and Summary section were read.
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md' | rg -i 'credit|self-critique|self-correct|reflect|weights|parametric|survey|taxonom|skill librar|resampl|retry|verbal|in-context|post-train|governance|multi-agent|fixed decomposition|learning outside|consolidat|evolv'` returned 17 titles. Kept or evaluated: fixed decomposition, reflection buys addressability, reflective coverage, and Adaptation signals choose pressure.

**Descriptions:**
- `rg -m1 '^description:'` was run on the resolved candidate paths listed above, plus `kb/theory/definitions/{theory-builder,representational-form}.md` and `kb/agentic-systems/reviews/autogenesis.md`.

**Body search** (theory, reference, agentic-systems, agent-memory-systems):
- `rg -l -i "credit assignment"` found the coevolution, governing-writes and deployed-system notes, which are already linked. It also found `factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md`, which was rejected because its subject is factory learning, not survey credit assignment.
- `rg -l -i "self-critique|self-refine|self-reflection"` found `kb/agent-memory-systems/reviews/reflexion.md` and `trace-learning-techniques-in-related-systems.md`.
- `rg -l -i "Voyager"` found `kb/agent-memory-systems/reviews/voyager.md` and `claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md`.
- `rg -l -i "AlphaEvolve"` and `rg -l -i "Memory-R1|MemAgent|Mem1"` returned no hits. The KB has no analysis of the survey's structural-evolution exemplar or of most of its RL memory controllers.
- `rg -l -i "validator-driven|resampl"` found `llm-output-deviation-requires-three-way-diagnosis.md` and archived analysis results. The diagnosis note was rejected because it concerns diagnosis of output deviations, not selection by retry.
- `rg -l -i "in-context.*post-training|post-training"` found `kb/theory/research/adaptation-agentic-ai-analysis.md` and the adaptation-survey note, which is already linked.
- `rg -l -i 'self-evolv' kb/agentic-systems/comparisons kb/agentic-systems/reviews` found `kb/agentic-systems/reviews/autogenesis.md`.
- `rg -n -i 'flat memory|flat-memory' kb/reference/vocabulary-collision-ledger.md` returned no entry for the "flat memory" collision.
- `rg -n -i 'localized|consumption|persistence' kb/theory/definitions/theory-builder.md` confirmed that the source's five "theory-builder conditions" are the definition's numbered conditions.
- `rg -l 'agentic-reasoning-for-llms-survey' kb --glob '*.md'` found no inbound links to the source.

**Link following:**
- From the coevolution note: its source list (Symbolic Learning, Memento-Skills, Co-Harness) cites self-evolution sources with `evidenced-by` but does not yet cite this survey. This makes it a reverse-edge target.
- From the adaptation-survey note: it cites the Adaptation of Agentic AI ingest as evidence. The source's recommended next action is an update to this note, so it is a reverse-edge target.
- From `kb/theory/COLLECTION.md`: theory-to-sources edges use `evidenced-by`, and a phrase must say whether the evidence corroborates, qualifies or bounds the claim. Both reverse edges below bound their target claims; they do not corroborate them.

### Candidate origins

- kb/sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md — titles, descriptions
- kb/sources/next-generation-agentic-reinforcement-learning-systems.ingest.md — titles, descriptions
- kb/sources/the-what-and-when-of-self-evolving-agents.ingest.md — titles, descriptions
- kb/sources/reflexion-verbal-reinforcement-learning.ingest.md — titles, descriptions
- kb/sources/agentic-memory-learning-unified-long-term-and-short-term.ingest.md — titles, descriptions
- kb/sources/multi-agent-memory-computer-architecture-perspective.ingest.md — titles, descriptions
- kb/theory/definitions/theory-builder.md — known, body-search
- kb/theory/definitions/representational-form.md — known, descriptions
- kb/theory/reasoning-production-is-not-reasoning-evaluation.md — known
- kb/theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md — known, titles, curated-head
- kb/theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md — curated-head
- kb/theory/diagnostic-richness-constrains-outer-loop-learning-quality.md — curated-head
- kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md — body-search
- kb/agent-memory-systems/reviews/voyager.md — body-search
- kb/agentic-systems/reviews/autogenesis.md — curated-head, body-search
- kb/sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md — known
- kb/theory/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md — known, curated-head
- kb/theory/treat-continual-learning-as-representational-form-coevolution.md — known, curated-head, link-following

## Connections Found

- [LLM agents are not always faithful self-evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) -- **compares-with**: compares the two on whether retained verbal experience is actually consumed. The survey says reflections "condition future reasoning", which the source counts toward the theory-builder *Consumption* condition. The faithfulness paper finds that agents largely ignore condensed experience across 13 backbones. This is the strongest available check on the survey's verbal-evolution class.
- [Next-generation agentic RL systems](../../../../sources/next-generation-agentic-reinforcement-learning-systems.ingest.md) -- **compares-with**: compares the two on governance of the self-evolution update. This architecture puts an explicit evolution control plane that chooses among memory, skill, harness, tool, weight, rollback and no-op updates. That is the selection and authorization step the survey's `U(S_k, τ_k, F_k)` folds into feedback. It sharpens the source's "governance gap is in the framework" finding.
- [The What & When of Self-Evolving Agents](../../../../sources/the-what-and-when-of-self-evolving-agents.ingest.md) -- **compares-with**: compares the two on how self-evolution updates are classified. That essay crosses update substrate (files, harness, weights) with horizon (intra-task, inter-task, inter-agent). This survey splits updates into verbal, procedural and structural classes and separates intra-test-time from inter-test-time evolution. The two maps cut the same space on different axes. Neither is a representational-form split.
- [Reflexion: verbal reinforcement learning](../../../../sources/reflexion-verbal-reinforcement-learning.ingest.md) -- **compares-with**: the survey's exemplar of verbal evolution, compared on what the method's evidence supports. The KB's primary-paper ingest finds that self-test errors and uneven diagnosis fidelity limit Reflexion's evidence for learning through retained explanations. The survey relays the method without these caveats.
- [Agentic Memory (AgeMem)](../../../../sources/agentic-memory-learning-unified-long-term-and-short-term.ingest.md) -- **compares-with**: compares the two on RL-trained memory control. "Agentic Memory" appears in the survey's section 4.2.3 list. The KB's primary ingest of it is the one controller whose reward design has been checked, so it is the model for checking the survey's other candidate cases (Extractable Value 3).
- [Multi-agent memory from a computer-architecture perspective](../../../../sources/multi-agent-memory-computer-architecture-perspective.ingest.md) -- **compares-with**: compares the two on multi-agent memory management (survey section 5.3.2). The position paper names standardized memory access permissions and consistency as unsolved protocol gaps. The survey reports per-entry provenance with access policies (Collaborative Memory) and replay-gated write admission (SEDM). This bears on how far the source's bounded governance claim reaches.
- [Theory builder](../../../../theory/definitions/theory-builder.md) -- **defined-in**: the source's Learning Claims section judges the surveyed systems against the "theory-builder conditions" (localized content, consumption, criticism, iteration, persistence) but does not link the definition that states them.
- [Representational form](../../../../theory/definitions/representational-form.md) -- **defined-in**: the source maps verbal, procedural and structural evolution onto "natural-language, symbolic and distributed-parametric forms" and says the survey mixes form with role. A reader needs the definition to follow why procedural and structural evolution are the same form.
- [Reasoning production is not reasoning evaluation](../../../../theory/reasoning-production-is-not-reasoning-evaluation.md) -- **compares-with**: compares the two on whether same-model self-critique evaluates reasoning. The source cites this tension inline twice, in Connections Found and in Limitations, but its footer does not list it. Adding the footer entry makes the warning against citing the survey as support for self-critique discoverable.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **compares-with**: compares the two on whether reported gains separate learning within a fixed operation set from the choice of that set. The source's Fixed decomposition paragraph applies this note to Memory-R1, MemAgent and the reflection methods, but the link is inline only. `is-evidence-for` would overclaim, because the survey gives descriptions without reward or baseline detail.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **compares-with**: compares the survey's three feedback regimes on which loop functions each has. Validator-driven retry has search and reject-capable evaluation but no operative retention, so it is selection on outputs. The source says this but does not name the loop function that is missing. The note gives the reader the vocabulary to reject the survey's "continuum" reading.
- [Diagnostic richness constrains outer-loop learning quality](../../../../theory/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **compares-with**: compares the two on diagnostic richness. The survey explicitly calls validator-driven feedback "non-diagnostic" and effective only where validation is cheap and reliable. The note explains why a winner-picking oracle without inspectable failure evidence gives an outer loop little to learn from.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **compares-with**: compares the two on how learning from trajectories is classified. The KB comparison classifies systems by representational form, behavioral authority and evidence tier from code reviews. The survey classifies the same family of methods by the role of the changed artifact, using paper descriptions. This complements the existing agent-memory-landscape link at the level of individual mechanisms.
- [Voyager review](../../../../agent-memory-systems/reviews/voyager.md) -- **compares-with**: the survey's exemplar of procedural evolution, compared on what the skill library actually retains and consumes. The code-grounded review gives the reader a checked account of executable skill libraries, retrieval and curriculum that the survey summarizes in one line.
- [Autogenesis review](../../../../agentic-systems/reviews/autogenesis.md) -- **compares-with**: compares the two on governance of updates to evolvable state. Autogenesis is a code-grounded self-evolving framework with versioned mutation and rollback. It is an inspected instance of the retire and roll back step that the survey's general update rule lacks.

## Bidirectional Candidates

- [Ingest: Adaptation of Agentic AI](../../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) <-> source -- **compares-with**: the adaptation ingest predates this one, and a reader of it would benefit from learning that a second survey with two of the same authors repeats the locus-of-optimization framing. The return edge is independently useful; it does not merely mirror the existing one.
- [The What & When of Self-Evolving Agents](../../../../sources/the-what-and-when-of-self-evolving-agents.ingest.md) <-> source -- **compares-with**: the return edge gives a reader of the essay's 3×3 map an academic survey's taxonomy of the same space to compare against.

## Reverse-edge Candidates

- [The adaptation survey corroborates memory requirements but misses artifact governance](../../../../theory/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) → source -- **evidenced-by** (bounds): the source's Recommended Next Action. A second survey repeats the framework-level omission of update governance. Its section 5.3.2 reports governed write admission (SEDM) and provenance (Collaborative Memory), which bounds the note's claim to survey frameworks rather than the catalogued literature. Under `kb/theory/COLLECTION.md`, the context phrase must say that this qualifies or bounds the claim rather than corroborating it.
- [Treat continual learning as representational-form coevolution](../../../../theory/treat-continual-learning-as-representational-form-coevolution.md) → source -- **evidenced-by** (bounds): section 8.2 names credit assignment across "tokens, tool calls, skills, and memory updates" as an open problem. It is an outside ML statement of the note's cross-form credit-assignment difficulty (Extractable Value 2). It was not produced as a test of the note, so it bounds rather than corroborates. The note's existing source list (Symbolic Learning, Memento-Skills, Co-Harness) is the natural place for it.

## Off-authorisation Candidates

- [Vocabulary collision ledger](../../../../reference/vocabulary-collision-ledger.md) -- the source's Extractable Value 6 proposes a ledger entry for "flat memory": in this survey it means an unstructured retrieval buffer, while in the KB it means collapsed memory roles. The only authorised sources→reference label is `see-also`. The reader-need is not an adjacent companion: the ledger should record the collision, and the ingest should not cite the ledger. Reject as an outbound link and route it as a ledger-maintenance candidate (see Maintenance Observations).

## Raw Text Candidates

None

## Rejected Candidates

- [Flat memory predicts specific cross-contamination failures](../../../../theory/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) -- already linked inline. The source explicitly says the two senses of "flat memory" must not be cited as mutual support, so a labelled footer edge would invite exactly that misreading.
- [Reflection buys addressability](../../../../theory/reflection-buys-addressability.md) -- relevant to the *Localized content* condition (verbal and procedural evolution are addressable, parametric adaptation is not). The defined-in edge to the theory-builder definition already covers that condition. A second edge would mostly restate the condition.
- [An omitted improvement-loop function and a frozen one need different repairs](../../../../theory/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) -- overlaps with the proposal-selection-loop candidate. The establishing note is the better single target for "validator retry lacks retention".
- [Adaptation signals choose pressure; artifact analysis chooses the retained surface](../../../../theory/research/adaptation-agentic-ai-analysis.md) -- it analyses the Adaptation of Agentic AI survey. Its link to this source would go through the adaptation ingest, which is already linked. Adding it would double the path without a new axis.
- [Claw learning loops must improve action capacity, not just retrieval](../../../../theory/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) -- matched only on "Voyager". Its claim concerns the target domain of Claw learning loops, not survey taxonomy.
- [Reflexion review](../../../../agent-memory-systems/reviews/reflexion.md) -- relevant, but the Reflexion ingest candidate already carries the primary-paper evidence caveats. Keep one Reflexion edge to avoid a cluster of links for one exemplar.
- [Harness Continual Learning](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md), [Symbolic Learning](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md), [Continual Learning in Token Space](../../../../sources/continual-learning-in-token-space.ingest.md), [Letta (MemGPT)](../../../../sources/letta-memgpt-stateful-agents.ingest.md), [Agent Plasticity](../../../../sources/agent-plasticity.ingest.md), [Memory Scaling](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md) -- each is a primary system or experiment on learning outside weights. Without a named axis particular to this survey, any one of them would be a topical `see-also`. The coevolution note already collects several of them.
- [Factory learning mechanisms should be compared on the same causal job](../../../../theory/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md) -- it matched "credit assignment", but its subject is factory learning.
- [LLM output deviation requires three-way diagnosis](../../../../theory/llm-output-deviation-requires-three-way-diagnosis.md) -- it matched "resampl", but it concerns diagnosis of individual output deviations, not retry as a feedback regime.

## Index Membership

None. `kb/sources/` is outside the tag-participating collections (`kb/sources/COLLECTION.md`, "Topic search tags"), so the `agent-memory` and `self-improving-systems` heads do not list sources.

## Synthesis Opportunities

The faithfulness paper, the Reflexion ingest and this survey together suggest a candidate claim. ML surveys classify verbal self-evolution by what is written to state. The two primary sources show that what is written may not be consumed (condensed experience is ignored) or may be diagnosed poorly (self-test errors). If so, "verbal evolution" is a write class, not evidence of learning, unless the source also shows consumption. This may already be implied by `trace-extracted-memory-earns-authority-per-operation-not-at-capture.md`. Check that note before drafting anything.

## Maintenance Observations

- `kb/reference/vocabulary-collision-ledger.md` has no "flat memory" entry. This source documents a concrete collision (survey sense: unstructured retrieval buffer; KB sense: collapsed memory roles). It is a candidate ledger entry if the phrase recurs in other sources.
- The KB has no ingest or review for AlphaEvolve, Memory-R1, MemAgent or Mem1 (`rg -l -i "AlphaEvolve"` and `rg -l -i "Memory-R1|MemAgent|Mem1"` returned nothing in theory, reference, agentic-systems or agent-memory-systems). The source's Extractable Value 3 depends on reading those primary papers.
- The source body links `reasoning-production-is-not-reasoning-evaluation.md`, `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md` and `flat-memory-predicts-specific-cross-contamination-failures-that-are.md` inline but omits them from its Relevant Notes footer. The first two are proposed above. The third is deliberately excluded.

## Flags

- Split candidate: no. The source makes several observations, but all of them serve one analysis of one survey.
- Tension, not resolved here: the survey presents reflective feedback, parametric adaptation and validator-driven retry as a "continuum". The source and the proposal-selection-loop note read them as distinct operations that differ in what is retained.
