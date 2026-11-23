---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/wooldridge-jennings-intelligent-agents.ingest.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Ingest: Intelligent Agents: Theory and Practice (Wooldridge and Jennings, 1995)

**Source:** [Ingest: Intelligent Agents: Theory and Practice (Wooldridge and Jennings, 1995)](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md)

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` "Outbound links". Destinations to prospect: `kb/theory/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/tags/`, other sources. Excluded: `kb/work/`, `kb/instructions/`. Authorised labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). No external target was supplied beyond the source URL already in frontmatter, so external prospecting was skipped.

**Existing links verified (known):** all eight inline links in the ingest resolve: `agent-is-a-tool-loop`, `usefulness-autonomy-warrant-and-power-are-separate-dimensions`, `human-llm-differences-are-load-bearing-for-knowledge-system-design`, `agent-statelessness-makes-routing-architectural-not-learned`, `constraining-and-extraction-both-trade-generality-for-reliability`, `russell-wefald-principles-of-metareasoning.ingest`, `provably-bounded-optimal-agents.ingest`, `agent-harness-large-language-model-agents-survey.ingest`, plus `definitions/program-refinement`. These are not re-proposed.

**Topic indexes:**
- `kb/tags/architecture-README.md` (source carries `tags: [architecture]`) -- groupings are runtime boundaries, control planes, storage authority. No classical agent-architecture taxonomy entry; nothing to add. Source tags do not create membership.
- `kb/sources/README.md` -- orientation only, no curated listing.

**Titles listing:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ kb/sources/ --glob '*.md' --glob '!*.brief.md' | rg -i "agent|autonom|definition|symbolic|plan|bound|ration|metareason|world model|harness|learn"` -- flagged: Chunking in Soar; Introspective multistrategy learning; PD of HCI - Plans and Situated Actions (Suchman); Human analogies can motivate functions without determining component boundaries; The Alberta Plan; World models assess explanatory-reach; The Agent Loop Architecture; Autonomous Agent Architecture. Paths resolved with `rg -l -F -x '# <title>' kb/`.

**Body search:**
- `rg -n -i "wooldridge|jennings|deliberative|reactive architecture|BDI|belief.desire|intentional stance|weak notion of agency|logical omniscience|transduction problem|genesereth|subsumption|brooks"` over theory, reference, agentic-systems, agent-memory-systems, sources, tags -- dominated by false `bdi` hits inside "subdirectory"; reran with word boundaries.
- `rg -n -i -w "wooldridge|deliberative|reactive|BDI|intentional stance|pro-activeness|proactive|logical omniscience|genesereth|bounded rationality|resource-bounded|anthropomorph"` (excluding retained archives) -- no prior citation of the survey anywhere outside `kb/work/`. Hits: `russell-wefald` ingest (already linked), `statecharts-and-programs-differ...` ("reactive controller", statechart sense, rejected), `information-value-is-observer-relative` (bounded rationality via Simon, rejected), `the-alberta-plan-for-ai-research.ingest`, `craik-hypothesis-on-the-nature-of-thought-1943.ingest`, various "proactive" product-feature hits in reviews (rejected, ordinary sense).
- `rg -n -i "agent defin|definition of agent|what is an agent"` over theory, agentic-systems, reference, tags -- only `instantiation-alone-cannot-model-agent-learning-across-sessions` (class/instance analogy, not a definition debate; rejected) and analysis-archive rows.
- `rg -n -i "planning|PRODIGY|deliberat" kb/sources/minton-utility-of-ebl-aaai88.ingest.md` -- PRODIGY is a symbolic planner with learned search-control rules over a fixed architecture.
- `rg -n -i "symbolic|problem space|architecture remains fixed|world model" kb/sources/chunking-in-soar-general-learning-mechanism.ingest.md` -- Soar learns production rules while problem spaces, decision procedure and representation stay fixed.
- `rg -n -i "plan|situated|reactive|symbolic" kb/sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md` -- Suchman's critique of the AI "planning model" and of world models holding common-sense background.

**Link following:**
- `kb/theory/agent-is-a-tool-loop.md` footer: computational-model tag, bounded-context orchestration, loop exposure -- none cite a definitional source; confirms the reverse-edge gap.
- `kb/theory/human-analogies-suggest-functions-not-component-boundaries.md` footer: psychology-to-agent transfer, human-LLM differences (already linked from the ingest). BDI's decomposition into belief, desire and intention stores is a classical instance of the boundary inheritance the note warns about.
- `kb/theory/COLLECTION.md` outbound labels read to check reverse edges: theory -> sources allows `evidenced-by`, `derived-from`, `abstracted-from`, `see-also`.

**Candidate evaluations:**
- Soar chunking ingest -- kept: symbolic, deliberative-in-the-survey's-sense architecture that learns; directly bears on Extractable Value item 5 ("deliberative learning" has no precedent in this source).
- Minton EBL ingest -- kept: PRODIGY is a STRIPS-style planner (the survey's paradigm deliberative case, 3.a) that learns control rules; same axis as Soar. Untracked at report time.
- Introspective multistrategy learning ingest -- kept: Meta-AQUA revises its own knowledge from explicit reasoning traces; answers the "revising its own model" gap the ingest records.
- Suchman summary ingest -- kept: the plan-based model the survey calls deliberative is what Suchman critiques; the survey cites Agre and Chapman's reactive work that drew on it.
- Human analogies note -- kept as compares-with on the mentalistic-decomposition axis, with a caveat that the ingest does not yet analyse BDI as a component decomposition.
- Craik ingest -- rejected (see below).
- Alberta Plan ingest -- rejected (see below).
- Agent Loop Architecture, Autonomous Agent Architecture ingests -- rejected: practitioner LLM-loop framings; the survey's agent-architecture definition already links the harness survey, which covers this axis more rigorously.

### Candidate origins

- kb/sources/chunking-in-soar-general-learning-mechanism.ingest.md — titles, body-search
- kb/sources/minton-utility-of-ebl-aaai88.ingest.md — known, body-search
- kb/sources/introspective-multistrategy-learning.ingest.md — titles
- kb/sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md — titles, body-search
- kb/theory/human-analogies-suggest-functions-not-component-boundaries.md — titles, link-following
- kb/theory/agent-is-a-tool-loop.md — known, link-following

## Connections Found

- [Ingest: Chunking in Soar](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md) -- **compares-with**: learning inside a symbolic architecture. Soar is deliberative in the survey's 3.a sense (explicit symbolic state, rule-based decision) and learns production rules, but its problem spaces, decision procedure and representation stay fixed. That qualifies Extractable Value item 5: the survey is silent on learning, yet the classical symbolic tradition did learn, within a fixed architecture. A reader checking "deliberative learning" for precedent needs this.
- [Ingest: Minton, The Utility of EBL (AAAI-88)](../../../../sources/minton-utility-of-ebl-aaai88.ingest.md) -- **compares-with**: learning inside a symbolic planner. PRODIGY is a STRIPS-style planner, the survey's paradigm deliberative agent, that retains learned search-control rules under an explicit utility formula. It also contrasts with item 3: the survey gives no utility account of action, while PRODIGY uses a utility measure to govern which rules to retain, not to choose actions.
- [Ingest: Introspective multistrategy learning](../../../../sources/introspective-multistrategy-learning.ingest.md) -- **compares-with**: an agent revising its own model. The ingest records that the survey describes only state updates in deliberative architectures, never revision of the world model or decision procedure. Meta-AQUA diagnoses failures from explicit reasoning traces and plans knowledge repairs, the nearest classical case of the revision the survey omits.
- [Ingest: PD of HCI - Plans and Situated Actions (summary of Suchman)](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) -- **compares-with**: plan-based versus situated action. The survey's deliberative/reactive split is the architectural form of the debate Suchman's critique of the AI "planning model" opened. Her objection that world models cannot hold common-sense background parallels the survey's transduction and representation/reasoning problems.
- [Human analogies can motivate functions without determining component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) -- **compares-with**: mentalistic concepts as design decomposition. The survey defends the intentional stance as a description tool, while BDI architectures such as PRS turn belief, desire and intention into separate runtime structures. That is the step from functional analogy to inherited component boundary that the note separates. Add this only if the ingest first gains a sentence on BDI as a component decomposition; the current analysis does not make that point.

## Bidirectional Candidates

- [Ingest: Chunking in Soar](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md) <-> source -- **compares-with**: the Soar ingest's "architecture remained fixed" point would gain a classical vocabulary anchor (symbolic world model plus pseudo-logical decision) by linking back. Sources -> sources `compares-with` is authorised.

## Reverse-edge Candidates

- [Agent is a useful technical convention, not a definition](../../../../theory/agent-is-a-tool-loop.md) → source -- **evidenced-by**: under `kb/theory/COLLECTION.md`, the note's opening claim that "agent" is too philosophically loaded to define cleanly is qualified by the survey's usable weak/strong property definitions. The context phrase should say the evidence qualifies the claim, not corroborates it. The ingest's Extractable Value item 6 already names the drops (autonomy, social ability, pro-activeness, persistent state) the note could make explicit.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Ingest: Craik, Hypothesis on the Nature of Thought](../../../../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md) -- the internal-model idea is an ancestor of the "world model" in the deliberative definition, but the survey does not cite Craik, and the link would only add a historical lineage with no claim either ingest uses.
- [Ingest: The Alberta Plan for AI Research](../../../../sources/the-alberta-plan-for-ai-research.ingest.md) -- a model-based, learning agent architecture, but it is reward-maximising RL. Its relation to the survey's symbolic deliberative category would need analysis neither ingest contains; Soar and PRODIGY carry the learning-in-deliberative-architecture axis more directly.
- [Statecharts and programs differ in what they show, not in what they can compute](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) -- "reactive" there means event-driven statechart control, a keyword collision with the survey's reactive architecture.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) -- cites bounded rationality via Simon; the survey's resource-bounded-reasoning gap is already routed to Russell and Wefald and bounded optimality.
- [Ingest: The Agent Loop Architecture](../../../../sources/the-agent-loop-architecture-2067677007140278630.ingest.md) and [Ingest: Autonomous Agent Architecture](../../../../sources/autonomous-agent-context-memory-2088234998654472340.ingest.md) -- practitioner LLM-loop framings; the existing harness-survey link covers the architecture-decomposition axis.
- [Instantiation alone cannot model agent learning across sessions](../../../../theory/instantiation-alone-cannot-model-agent-learning-across-sessions.md) -- matched an "agent" definition search but concerns the class/instance analogy, not the agency debate.

## Index Membership

None. `kb/sources/` has no curated listing, and source tags do not create tag-head membership.

## Synthesis Opportunities

The survey (no learning in its deliberative definition), Soar chunking (learning within a fixed symbolic architecture), Minton/PRODIGY (utility-governed retention of learned control rules in a fixed planner) and Meta-AQUA (trace-driven repair of its own knowledge) together suggest a candidate claim: classical symbolic agents learned content inside a fixed decision architecture, and revising the architecture itself stayed outside what they could learn. This bears directly on the occasion's "deliberative learning" naming question; it would belong in the workshop draft first, not in a theory note, until checked against further sources.

## Maintenance Observations

- `kb/sources/minton-utility-of-ebl-aaai88.ingest.md` is untracked at report time. The Minton candidate depends on that ingest being committed.

## Flags

- Tension for the occasion: the ingest correctly says "deliberative learning" has no classical precedent *in this source*. The Soar and Minton ingests show symbolic, deliberative-type architectures that did learn. A draft that cites only this survey could overstate novelty.
