---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/agentic-reasoning-for-llms-survey.md"
source_has_frontmatter: true
date: "2026-11-16"
depth: standard
---

# Connection Report: Agentic Reasoning for Large Language Models

**Source:** `kb/sources/.snapshots/agentic-reasoning-for-llms-survey.md` (Git-ignored snapshot; not linked because no paired `.ingest.md` exists yet)

The source is an immutable snapshot (arXiv:2601.12538v2). No tracked `agentic-reasoning-for-llms-survey.ingest.md` exists yet, so every outbound candidate below is a recommendation for that future ingest's `## Connections Found` footer, not for the snapshot. Per the sources contract, the ingest will link these targets; durable notes must link the ingest, never this snapshot.

Source reading (sections 1–2, 4 intro, 4.1, 4.1.3, 4.2–4.2.3, 5.3.2, 8): a survey organizing agentic reasoning into three layers (foundational: planning, tool use, search; self-evolving: feedback and memory; collective multi-agent), crossed with two optimization modes (in-context orchestration with frozen parameters vs post-training via RL/SFT). Its most KB-relevant parts are (a) the self-evolution meta-update `S_{k+1} ← U(S_k, τ_k, F_k)` classifying the evolvable state as verbal (reflections), procedural (tool/skill libraries) or structural (agent code), with weights optional; (b) the three feedback regimes — reflective, parametric, and validator-driven retry with independent resampling; (c) memory classed as flat, structured (graphs, trees, workflows), or post-training memory control (MemAgent, Mem1, Memory-R1, Mem-α, Memory-as-Action); (d) open problems including credit assignment across "tokens, tool calls, skills, and memory updates" and governance at model, agent and ecosystem level. The survey gives no account of who may authorize, review, or retire an update to `S_k`.

## Discovery Trace

**Setup:**
- Source collection `sources`; `kb/sources/COLLECTION.md` exists and its "Outbound links" section was read. Authorised: theory (is-evidence-for, abstracted-from, rests-on, compares-with, defined-in for theory/definitions, see-also); sources (compares-with, see-also); agent-memory-systems (is-evidence-for, compares-with, see-also); agentic-systems (compares-with, see-also); reference (see-also only); external (derived-from, see-also). Excluded: `kb/work/`, `kb/instructions/`. The snapshot is never the link author; the ingest carries the outbound surface.
- `abstracted-from` and `rests-on` were judged inapplicable: no theory claim was abstracted from this survey (it is new to the KB), and the survey is not a source-side design resting on a KB claim.
- External prospecting skipped: the only known external target is the source URL itself (`https://arxiv.org/pdf/2601.12538`), which the future ingest records as its `source`/`derived-from` origin.
- Existing references check: `rg -n -i '2601\.12538|agentic reasoning for large|Awesome-Agentic-Reasoning|weitianxin' kb/ --glob '*.md'` -- no hits; the survey is not yet cited anywhere.

**Curated heads (topic indexes):**
- `kb/tags/agent-memory-README.md` -- exposed [adaptation-survey-corroborates-memory-requirements](../../../../theory/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) (External Checks), [memory-management-policy-is-learnable-but-oracle-dependent](../../../../theory/memory-management-policy-is-learnable-but-oracle-dependent.md) (External Checks), [flat-memory-predicts-specific-cross-contamination-failures-that-are](../../../../theory/flat-memory-predicts-specific-cross-contamination-failures-that-are.md), the historical comparative review. Not `complete: true`.
- `kb/tags/continual-learning-README.md` (`complete: true`) -- exposed [treat-continual-learning-as-representational-form-coevolution](../../../../theory/treat-continual-learning-as-representational-form-coevolution.md), [continual-learning-requires-governing-behaviour-changing-writes](../../../../theory/continual-learning-requires-governing-behaviour-changing-writes.md), [the-deployed-system-not-the-model-is-the-unit-of-learning](../../../../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md). By-tag rg skipped (complete head).
- `kb/tags/deploy-time-learning-README.md` (`complete: true`) -- re-exposed the deployed-system note; nothing new. By-tag rg skipped.
- `kb/tags/self-improving-systems-README.md` (`complete: true`) -- exposed six-reported-self-improvement-paths evidence note and Autogenesis review; both judged weaker than the coevolution note for the survey's verbal/procedural/structural split. By-tag rg skipped.
- `kb/agentic-systems/README.md` -- exposed [agent-memory-landscape](../../../../agentic-systems/comparisons/memory/agent-memory-landscape.md); `kb/agent-memory-systems/README.md` confirmed that collection is frozen historical.

**Titles listing:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'` (436 titles), filtered with `rg -i 'in-context|weight|parametric|representational form|coevol|self-improv|reflect|validator|verif|oracle|retry|memory|multi-agent|survey|taxonom|reasoning|search|tool|evolv|trace|credit|retained|learn'`. Flagged: coevolution note; governing-writes note; deployed-system note; "Feedback-trained memory management is oracle-dependent even when its operations are hand-designed" (resolved to `memory-management-policy-is-learnable-but-oracle-dependent.md`); adaptation-survey note; error-correction note; boundary-of-automation note; weight-resident methodologies; borrowing via retained artifacts or weight activation; topology/isolation/verification chain; reasoning-production-is-not-evaluation; flat-memory cross-contamination.
- Paths resolved with `rg -l -F -x '# <title>' kb/theory/` for each flagged title; descriptions read.

**Descriptions listing:**
- `rg -l -i 'survey' kb/sources/*.ingest.md | xargs -r rg -N --no-heading -m1 '^description:\s*' -r '' | rg -i 'survey|taxonom'` -- flagged [adaptation-of-agentic-ai-survey ingest](../../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) (shared authors Jiaxuan You and Heng Ji; same in-context-vs-training split), [externalization-in-llm-agents ingest](../../../../sources/externalization-in-llm-agents-unified-review.ingest.md), [from-human-memory-to-ai-memory ingest](../../../../sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.ingest.md), agent-harness survey, RSI survey. Rejected agent-harness and RSI surveys (see below).
- `rg -N '^description:' kb/agentic-systems/comparisons/memory/*.md kb/agentic-systems/topics/*.md` -- kept agent-memory-landscape; rejected read-back-mechanisms and correction-propagation (too route-specific for a survey taxonomy).

**Body search:**
- `rg -l -i 'Reflexion' kb/theory` -- abstract-an-experience note only (uses Reflexion as an example of uncompressed reflection); not a connection target for the survey.
- `rg -l -i 'Voyager' kb/theory` -- claw-learning-loops, abstract-an-experience, agent-memory-is-crosscutting; mentions only, no survey-level overlap.
- `rg -l -i 'AlphaEvolve' kb/theory` -- no hits.
- `rg -l -i 'Memory-R1|MemAgent|Mem1\b|Mem-α|Memory-as-Action' kb/theory` -- no hits; the survey's post-training memory-control systems are new evidence for the oracle-dependence note.
- `rg -l -i 'post-training' kb/theory` -- adaptation-survey note, adaptation-agentic-ai-analysis research note, world-models note.
- `rg -l -i 'retry|resampl' kb/theory` -- 12 hits incl. verifiability-gradient, retry-versus-rewrite triage; read descriptions; error-correction note found via titles is the closer match for independent resampling against a validator.
- `rg -l -i 'Dec-POMDP|POMDP' kb/theory` -- no hits.
- `rg -l -i 'credit assignment' kb/theory` -- 9 hits incl. coevolution, governing-writes, deployed-system notes; confirms the survey's section 8.2 credit-assignment open problem matches the coevolution note's "cross-class credit assignment" difficulty.
- `rg -n -i 'independen|resampl|retry|best-of|majority' kb/theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` -- note's mechanism is independent sampling plus above-chance oracle; survey section 4.1.3 describes exactly that regime.
- Agentic-systems / agent-memory-systems: `ls kb/agentic-systems/reviews | rg -i ...` and `ls kb/agent-memory-systems/reviews | rg -i 'mem0|letta|...|voyager|reflexion'` -- historical reviews exist for a-mem, cognee, graphiti, letta, mem0, reflexion, voyager; no current agentic-systems reviews for the survey's cited systems.
- `ls kb/sources | rg -i 'alphaevolve|reflexion|voyager|memgpt|...'` -- reflexion, letta-memgpt, autogenesis ingests exist.

**Link following:**
- From the coevolution note: its "Loops today" list (DSPy, FunSearch, Meta-Harness, Symbolic Learning, Memento-Skills, Co-Harness, RLHF) and its credit-assignment and pace-mismatch difficulties -- the survey's verbal/procedural/structural/parametric split lines up against the note's natural-language/symbolic/distributed-parametric forms.
- From the adaptation-survey note: its reading dictionary and its conclusion that an optimization-locus taxonomy lacks substrate, form, lineage and authority -- the same gap appears in this survey's `U(S_k, τ_k, F_k)`.
- From the oracle-dependence note: AgeMem and AgentFly are its only cases; the survey's section 4.2.3 adds five more feedback-trained memory controllers with hand-designed operations (Memory-R1's add/update/delete).
- From the agent-memory tag head to the historical comparative review -- frozen; current landscape preferred.

### Candidate origins

- kb/theory/treat-continual-learning-as-representational-form-coevolution.md — curated-head, titles, body-search, link-following
- kb/theory/memory-management-policy-is-learnable-but-oracle-dependent.md — curated-head, titles
- kb/theory/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md — curated-head, titles, body-search
- kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md — curated-head, titles, body-search
- kb/theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md — titles, body-search
- kb/theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md — curated-head, titles, body-search
- kb/sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md — descriptions, link-following
- kb/sources/externalization-in-llm-agents-unified-review.ingest.md — descriptions
- kb/sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.ingest.md — descriptions
- kb/agentic-systems/comparisons/memory/agent-memory-landscape.md — curated-head, descriptions

## Connections Found

All edges below are for the future `kb/sources/agentic-reasoning-for-llms-survey.ingest.md`.

- [Treat continual learning as representational-form coevolution](../../../../theory/treat-continual-learning-as-representational-form-coevolution.md) -- **compares-with**: on the axis of how update targets are classified; the survey's verbal / procedural / structural evolution of `S_k` plus post-training maps onto natural-language / symbolic / distributed-parametric forms, and its section 8.2 open problem (credit across tokens, tool calls, skills, memory updates) is the note's cross-class credit-assignment difficulty stated from the ML side.
- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../theory/memory-management-policy-is-learnable-but-oracle-dependent.md) -- **is-evidence-for**: section 4.2.3 catalogues MemAgent, Mem1, Memory-R1 (hand-designed add/update/delete learned by RL), Mem-α and Memory-as-Action, each trained from task-outcome rewards; these add instances beyond the note's AgeMem and AgentFly, though as survey reports, not tests of the oracle claim.
- [The adaptation survey corroborates memory requirements but misses artifact governance](../../../../theory/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) -- **compares-with**: on the axis of taxonomy by optimization locus versus artifact governance; this survey, with overlapping authors, repeats the in-context/frozen versus trained split and has the same omission of authority, lineage and retirement for memory and skill updates.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../theory/continual-learning-requires-governing-behaviour-changing-writes.md) -- **compares-with**: on the axis of what conditions a retained update; the survey's meta-update `S_{k+1} ← U(S_k, τ_k, F_k)` folds selection into feedback `F_k` and has no step for validating, authorizing or coordinating writes, while its section 8.6 places governance at model/agent/ecosystem level rather than per update.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **is-evidence-for**: section 4.1.3 describes validator-driven feedback as independent resampling until a unit test, checker or environment signal passes, effective where validation is "reliable and inexpensive"; this is the note's amplification regime reported across program synthesis and embodied agents.
- [The deployed system, not the model alone, is the unit of learning](../../../../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: the survey's formalization treats the evolvable state as memories, tool libraries and agent code, with parameters "optionally" updated, so a mainstream ML survey locates self-evolution in system components outside weights.
- [Ingest: Adaptation of Agentic AI](../../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) -- **compares-with**: on the axis of where adaptation happens; A1/A2 versus T1/T2 against this survey's in-context versus post-training modes, from partly the same author group; a future ingest should state where the two taxonomies disagree (e.g. whether memory is a tool or a self-evolution substrate).
- [Ingest: Externalization in LLM Agents](../../../../sources/externalization-in-llm-agents-unified-review.ingest.md) -- **compares-with**: on the axis of weights versus externalized infrastructure; the externalization review argues progress moves from weights to context to harness, while this survey keeps post-training as a co-equal mode and treats internalization into weights as the consolidation route.
- [Ingest: From Human Memory to AI Memory survey](../../../../sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.ingest.md) -- **compares-with**: on the axis of memory taxonomy; flat / structured / policy-controlled memory here versus object / form / time there.
- [What the 243 current agentic-system analyses show about agent memory mechanisms](../../../../agentic-systems/comparisons/memory/agent-memory-landscape.md) -- **compares-with**: on the axis of memory admission, read-back and trace-fed updates; the survey classifies memory systems from papers, while the landscape counts code-grounded mechanisms across 243 analyses, so it checks which of the survey's categories appear in inspected systems.

## Bidirectional Candidates

None. The useful return paths go from theory notes to the future ingest; they are listed as reverse-edge candidates.

## Reverse-edge Candidates

These require a tracked ingest to exist first; theory notes must link the ingest, never the snapshot.

- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../theory/memory-management-policy-is-learnable-but-oracle-dependent.md) → future ingest -- **evidenced-by** (theory contract): the survey's section 4.2.3 list qualifies the claim's coverage with additional RL-trained memory controllers; the context phrase must say it is a survey catalogue, not a refutation attempt, and the systems' reward designs would need checking before counting them as cases.
- [Treat continual learning as representational-form coevolution](../../../../theory/treat-continual-learning-as-representational-form-coevolution.md) → future ingest -- **evidenced-by** (theory contract): qualifies the "Loops today" inventory by showing a 2026 survey frames self-evolution over verbal, procedural and structural state while naming cross-component credit assignment as open.
- [The adaptation survey corroborates memory requirements but misses artifact governance](../../../../theory/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) → future ingest -- **evidenced-by** (theory contract): bounds the note's scope; a second survey with overlapping authors shows the same governance omission, suggesting the gap belongs to the survey genre rather than one paper.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -- consistent with validator-driven feedback, but the error-correction note carries the specific mechanism; linking both would duplicate.
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) -- section 5 mentions communication topology as mechanism design, but the survey neither tests nor argues for a dependency chain; keyword overlap only.
- [Flat memory predicts specific cross-contamination failures that are empirically testable](../../../../theory/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) -- "flat" in the survey means unstructured retrieval buffers, not the note's collapse of memory roles; same word, different concept. Reported as a term mismatch, not a connection.
- [Weight-resident methodologies provide context-efficient behavioral compression](../../../../theory/weight-resident-methodologies-compress-behavior-in-context.md) and [Borrowing can operate through retained artifacts or weight activation](../../../../theory/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md) -- the survey's post-training "capability internalization" is training new behavior into weights, not activating pretrained methodology by cue; adjacent only.
- [Reasoning production is not reasoning evaluation](../../../../theory/reasoning-production-is-not-reasoning-evaluation.md) -- the survey's reflective-feedback section does not address process validity; this is a tension (see Flags), not a supporting edge.
- Agent-harness survey and RSI survey ingests -- different organizing question (harness components; demonstrated improvement capacity); neither shares a named axis tight enough for compares-with.
- Historical [agentic memory systems comparative review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) -- frozen; the current agent-memory landscape covers the same comparison.
- Historical reviews of Reflexion, Voyager, Letta, Mem0, Graphiti and the Reflexion/Letta ingests -- the survey only cites these as exemplars; a per-system link would add nothing the survey analysis can use unless the ingest compares the survey's characterization against the code-grounded review.
- Six reported self-improvement paths evidence note and Autogenesis review -- relate to the survey's "structural evolution" (AlphaEvolve), but the survey gives one sentence on it; too thin.

## Index Membership

- [agent-memory tag head](../../../../tags/agent-memory-README.md) -- the future ingest may carry `tags: [agent-memory]`: section 4.2 and 5.3.2 substantively treat memory organization and policy-controlled memory. Source tags do not create head membership.
- [self-improving-systems tag head](../../../../tags/self-improving-systems-README.md) -- candidate `tags: [self-improving-systems]`: section 4 and the `S_k` meta-update substantively treat systems changing their own memory, tools and code.
- [continual-learning tag head](../../../../tags/continual-learning-README.md) -- conditional: only if the ingest analyses the verbal/procedural evolution path as retained learning outside weights, which this tag requires; the survey's coverage alone spans both weights and artifacts.

## Synthesis Opportunities

The adaptation-survey note, this survey, and the externalization review together suggest a claim worth testing: ML surveys of agent learning classify updates by optimization locus and signal (in-context vs trained; agent vs tool) and consistently omit per-update governance (authority, lineage, retirement), so the governance layer is a gap in the genre rather than in one paper. Do not write it from connect; it needs a third independent survey reading to state where the omission stops.

## Maintenance Observations

- Term collision: "flat memory" in this survey (and likely other ML surveys) means unstructured retrieval storage, while the KB's flat-memory note means collapsed memory roles. A future ingest that uses the phrase should disambiguate; possibly a candidate for the vocabulary collision ledger.
- No ingest exists for this snapshot; all connection value is blocked until `cp-skill-ingest kb/sources/.snapshots/agentic-reasoning-for-llms-survey.md` runs.

## Flags

- Tension: the survey presents reflective feedback (self-critique of intermediate reasoning) as improving reliability, while [Reasoning production is not reasoning evaluation](../../../../theory/reasoning-production-is-not-reasoning-evaluation.md) argues self-critique can substitute answer reconstruction for evaluation. A future ingest should note this rather than cite the survey as support for self-critique.
- Not a split candidate: the target is a single-source snapshot.
