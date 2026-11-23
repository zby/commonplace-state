---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/wooldridge-jennings-intelligent-agents.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Intelligent Agents: Theory and Practice (Wooldridge and Jennings, 1995)

**Source:** `kb/sources/.snapshots/wooldridge-jennings-intelligent-agents.md` (ignored snapshot; no paired ingest yet, so not linked)

The source is an immutable snapshot. No tracked `wooldridge-jennings-intelligent-agents.ingest.md` exists yet, so every outbound candidate below is a recommendation for that future ingest's Connections Found section. Under `kb/sources/COLLECTION.md`, no durable artifact should link the snapshot; durable links go to the ingest once it exists.

Source contribution, as read for this pass: the paper gives a weak notion of agency (autonomy, social ability, reactivity, pro-activeness) and a strong, mentalistic notion. It justifies the intentional stance as an abstraction tool, used when a mechanistic description is impracticable (McCarthy, Shoham, Dennett). It treats agent theories as specifications and notes that the relation between BDI logics and architectures such as PRS is not formalised. It contrasts deliberative, reactive and hybrid architectures, naming the transduction and representation/reasoning problems and the intractability of time-bounded symbolic reasoning. It quotes Ferguson's three preconditions for hardwired reactive control, and it observes that reactive systems are hand-crafted without a methodology. It also lists open problems in goal generation and conflicting-intention management.

## Discovery Trace

**Setup reads:**
- `kb/sources/COLLECTION.md` outbound section. Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags and sources. `kb/work/` and `kb/instructions/` are excluded. `external` is authorised for `derived-from`/`see-also`, but no external target was supplied, so external prospecting was skipped. Labels: theory {is-evidence-for, abstracted-from, rests-on, compares-with, defined-in (theory/definitions), see-also}; sources {compares-with, see-also}; agentic-systems {compares-with, see-also}; reference {see-also}; agent-memory-systems {is-evidence-for, compares-with, see-also}.
- `kb/types/connect-report.md`.
- Target snapshot read across sections 1 (definitions), 2.a–2.b and 2.e–2.i (intentional stance, theory discussion), 3.a–3.e (architectures), 4.a (language discussion) and 6 (conclusion). The reference list and the individual language/application catalogues were only skimmed.

**Titles listing:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'` (442 titles), filtered with `rg -i "agent|intention|specif|stance|deliberat|reactive|symbol|bounded|world model|architect|belief|goal|plan|abstraction|definition|refine|autonom|harness|runtime"`. Flagged: `"Agent" is a useful technical convention, not a definition` (direct counterpart on defining "agent"), `Tool usefulness, computational autonomy, warrant, and system power are separate dimensions` (autonomy as a property), `Agent statelessness makes routing architectural, not learned` (persistent-state assumption), `Bounded-context orchestration model` and `Program refinement` (specification-to-implementation framing), and `World models assess explanatory-reach...` (keyword only).
- Counted titles for reference (258), agentic-systems (156) and agent-memory-systems (175). No agent-definition or classical-architecture titles appeared in reference or agent-memory-systems.

**Description listing scan:**
- `rg '^description:' kb/sources/*.ingest.md | rg -i "agent theor|definition of agent|what an agent|BDI|intention|bounded optimal|metareason|symbolic AI|GOFAI|physical symbol|subsumption|reactive|deliberat|knowledge-level|newell|simon|planning|STRIPS|softbot|multi-agent system|expert system|knowledge engineering"` flagged `russell-wefald-principles-of-metareasoning` (which the survey cites as Russell and Wefald 1991 for time-bounded reasoning) and `herbert-simon-architecture-of-complexity` (layered hierarchy; weak). It also flagged `intention-is-all-you-need` (a different sense of intention), plus `the-alberta-plan` and `xinmingtu` (architecture keyword only).
- Description reads for `provably-bounded-optimal-agents`, `what-is-an-agent-harness`, `agent-harness-large-language-model-agents-survey`, `symbols-neural-networks-mathematical-intelligence`, `the-agent-loop-architecture` and `minton-utility-of-ebl-aaai88`.
- Theory descriptions read for program-refinement, codification, usefulness-autonomy, human-llm-differences, agent-statelessness (both notes), bounded-context-orchestration-model, implementations-do-not-establish-shared-semantics, spec-mining-as-codification, codification-and-relaxing, symbolic-form-holds-consumers, specification-strategy, traditional-software-can-bracket, agent-runtime-analysis, llm-frameworks-should-keep-the-tool-loop-optional and constraining-and-extraction.

**Topic indexes:**
- `kb/tags/` listing scanned. Read `computational-model-README.md` (description), `warranted-autonomy-README.md` (description), `architecture-README.md` (head and first two groupings) and `goal-prioritization-README.md` (inclusion condition). The source carries no `tags:`, so no tag-based by-tag rg was required. `architecture` fits as a possible ingest tag (see Index Membership). `goal-prioritization` fails its subtractive test because the survey mentions goal generation only as an open problem.

**Body search:**
- `rg -l -i "wooldridge|jennings" kb --glob '*.md'` (excluding work) — no existing KB citation of the paper.
- `rg -n -i "intentional stance|dennett|\bBDI\b|belief-desire|subsumption|brooks|physical.symbol|logical omniscience|resource.bounded|weak notion of agency|what is an agent|definition of (an )?agent" kb ...` — hits only in unrelated sources (Sutskever list chapters), the russell-wefald ingest ("resource-bounded agent"), an agentic-system analysis mentioning a `bdi-mental-states` skill (incidental) and prior connect reports. No theory note discusses BDI or the intentional stance.
- `rg -n -i "anthropomorph|mentalis|folk psycholog|intentional system|ascrib(e|ing) (belief|goal)|explicit world model|symbolic world model|situated|hand-crafted|handcrafted|reactive (architecture|agent|system)|deliberative" kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags` — kept `human-llm-differences-are-load-bearing...` (its "Naive anthropomorphism" and "Naive mechanism-ism" section) and `kb/agentic-systems/reviews/ai-agent-book.md` ("The agent is the situated loop" section). The Bitter-Lesson "hand-crafted" cluster was considered and rejected as an indirect match: the survey's hand-crafting complaint concerns reactive-system development method, not learned-versus-hand-crafted production.
- `rg -n -i "specification" kb/theory -l` — reviewed the listed specification notes by description. Kept `constraining-and-extraction-both-trade-generality-for-reliability` for Ferguson's preconditions. Rejected `implementations-do-not-establish-shared-semantics` (its subject is language semantics and conformance, not logic-to-architecture correspondence) and `program-refinement` (the survey asks the refinement question but offers no refinement relation).
- `rg -n -i "goal generation|generate (its|their) own goals|multiple.{0,20}conflicting goals|intention reconsideration" kb/theory kb/tags` — no hits.

**Link following:**
- From `agent-is-a-tool-loop.md`: followed to `computational-model` tag, `bounded-context-orchestration-model` and `subtasks-that-need-different-tools...`. These concern sub-agent framework design, so the definitional comparison stays with the tool-loop note alone.
- From `ai-agent-book.md` "situated loop" section: it links back to `agent-is-a-tool-loop` and `llm-frameworks-should-keep-the-tool-loop-optional`, confirming that the tool-loop note is the KB's canonical agent-definition surface.
- From `usefulness-autonomy-warrant-and-power-are-separate-dimensions.md`: it is linked to `warranted-autonomy` tag and `warranted-autonomy-is-bounded-by-oracle-domain`. The comparison axis is the definition of autonomy, so only the four-dimension note is kept.

### Candidate origins

- kb/theory/agent-is-a-tool-loop.md — titles, link-following
- kb/theory/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md — titles, link-following
- kb/theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md — body-search
- kb/theory/agent-statelessness-makes-routing-architectural-not-learned.md — titles, body-search
- kb/theory/constraining-and-extraction-both-trade-generality-for-reliability.md — body-search
- kb/sources/russell-wefald-principles-of-metareasoning.ingest.md — body-search, descriptions
- kb/sources/provably-bounded-optimal-agents.ingest.md — descriptions
- kb/sources/agent-harness-large-language-model-agents-survey.ingest.md — descriptions

## Connections Found

All are candidates for the future `kb/sources/wooldridge-jennings-intelligent-agents.ingest.md`.

- ["Agent" is a useful technical convention, not a definition](../../../../theory/agent-is-a-tool-loop.md) -- **compares-with**: the axis is how to define "agent". Wooldridge and Jennings give property-based weak and strong notions and warn that the term risks becoming a "noise" term. Commonplace instead sidesteps the debate with a code-structural unit (prompt, capability surface, stop condition) that says nothing about autonomy, goals or pro-activeness. The comparison shows which classical properties the tool-loop convention deliberately drops.
- [Tool usefulness, computational autonomy, warrant, and system power are separate dimensions](../../../../theory/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md) -- **compares-with**: the axis is what "autonomy" means. The survey's autonomy property ("operate without the direct intervention of humans", plus control over actions and internal state) is a single agent attribute. Commonplace's computational autonomy is an allocation reading over named functions against a declared boundary, kept separate from warrant and power.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- **compares-with**: the axis is when to describe an artificial agent in human terms. McCarthy's criterion, as quoted, holds that ascription is legitimate when it carries the same information and useful when it helps predict, repair or improve the machine. The note's "naive anthropomorphism" and "naive mechanism-ism" failure modes give a per-convention transfer test for the same question.
- [Agent statelessness makes routing architectural, not learned](../../../../theory/agent-statelessness-makes-routing-architectural-not-learned.md) -- **compares-with**: the axis is persistent internal state. The weak notion, and the quoted Genesereth–Ketchpel "persistent control", assume an agent that encapsulates state across interactions, as do IRMA/PRS belief, desire and intention stores. The note's design consequences follow from LLM agents lacking learned state across sessions, which is exactly the property the 1995 definition takes for granted.
- [Constraining and extraction can trade generality for reliability, speed, or cost](../../../../theory/constraining-and-extraction-both-trade-generality-for-reliability.md) -- **compares-with**: the axis is the scope within which fixed, precompiled behaviour is adequate. Ferguson's three preconditions for purely reactive architectures are activity that is situationally determined, no global run-time task constraints, and a goal ranking fixed at compile time. Those preconditions state when hardwired responses give reliability without losing required generality. Weaker candidate: this is the survey quoting Ferguson, so the ingest should present it as a classical instance, not as support.
- [Ingest: Principles of Metareasoning (Russell and Wefald, 1991)](../../../../sources/russell-wefald-principles-of-metareasoning.ingest.md) -- **compares-with**: the axis is time-bounded reasoning in agents. The survey cites Russell and Wefald 1991 for the problem that symbolic deliberation cannot guarantee useful results within a fixed time bound and names it an open problem of deliberative architectures. The metareasoning ingest records the decision-theoretic answer (value of computation minus time cost).
- [Ingest: Provably Bounded-Optimal Agents](../../../../sources/provably-bounded-optimal-agents.ingest.md) -- **compares-with**: the axis is resource-bounded agent theory. The survey states that possible-worlds logics model perfect reasoners (logical omniscience) although "all real agents are resource-bounded", and leaves resource-bounded reasoners as open work. Russell and Subramanian's contemporaneous paper formalises program quality relative to a machine and environment as one response.
- [Ingest: Agent Harness for Large Language Model Agents](../../../../sources/agent-harness-large-language-model-agents-survey.ingest.md) -- **compares-with**: the axis is what an agent architecture decomposes into. Maes and Kaelbling, as quoted, define an architecture as component modules plus data and control flow mapping sensor data and internal state to actions. The harness survey decomposes the modern LLM agent into an execution loop, tool registry, context manager, state store, hooks and evaluation interface. The comparison shows the transduction problem moving from perception into context assembly.

## Bidirectional Candidates

- ["Agent" is a useful technical convention, not a definition](../../../../theory/agent-is-a-tool-loop.md) <-> source -- the note's opening claim, that "agent" "carries too much philosophical weight to define cleanly", currently has no citation. Once the ingest exists, the theory note could cite it in its body as `evidenced-by` (theory contract), qualifying the claim with the canonical weak/strong definitional split. The context phrase must say it bounds the claim, not corroborates it. See Reverse-edge Candidates.

## Reverse-edge Candidates

- ["Agent" is a useful technical convention, not a definition](../../../../theory/agent-is-a-tool-loop.md) → future ingest -- **evidenced-by** (authorised theory→sources in `kb/theory/COLLECTION.md`): host the citation in the first paragraph. Example: the definitional debate the convention sidesteps is the one Wooldridge and Jennings document with their weak and strong notions of agency. This edge qualifies the note; it does not corroborate it. Author the edge only after the tracked ingest exists, and link the ingest, never the snapshot.

## Off-authorisation Candidates

- [The agent is the situated loop, not the model alone (AI Agent Book review)](../../../../agentic-systems/reviews/ai-agent-book.md) -- `compares-with` is authorised for sources→agentic-systems, so the label is not the issue. The candidate is routed here because its comparison runs through `agent-is-a-tool-loop`, which is already kept. A direct link would duplicate that edge at lower resolution. Reject unless the ingest needs a second, harness-allocation perspective on the agent definition.

## Raw Text Candidates

None

## Rejected Candidates

- [Program refinement](../../../../theory/definitions/program-refinement.md) -- the survey asks how a specification is refined into an implementation but defines no refinement relation. The ingest does not use the KB's term, so `defined-in` has no term to serve.
- [Implementations do not establish shared semantics](../../../../theory/implementations-do-not-establish-shared-semantics.md) -- the survey's point that the BDI logic is not used to give PRS a formal semantics looks similar. The note concerns language semantics and conformance claims, not logic-to-architecture correspondence, so a link would mislead.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- the deliberative/reactive debate is not the hand-crafted-versus-learned axis. The survey's complaint is that reactive systems are hand-tuned without a methodology, with ML suggested only in passing. The match is a keyword overlap.
- [Ingest: The Architecture of Complexity (Simon, 1962)](../../../../sources/herbert-simon-architecture-of-complexity.ingest.md) -- layered hybrid architectures resemble hierarchy only superficially. The survey makes no near-decomposability claim.
- [Ingest: Symbols, neural networks, and mathematical intelligence](../../../../sources/symbols-neural-networks-mathematical-intelligence.ingest.md) -- the physical-symbol-system hypothesis appears in both, but the survey only reports the hypothesis. It takes no position that would compare with Lampinen's connectionist reading.
- [Ingest: What is an Agent Harness](../../../../sources/what-is-an-agent-harness-2046980769747533830.ingest.md) -- a harness taxonomy with no agent-definition content. The agent-harness survey is the stronger architecture comparison.
- `world-models-assess-explanatory-reach...` -- "world model" means a learned predictive model there, not the survey's explicit symbolic world model. Keyword only.
- `intention-is-all-you-need` ingest -- shared human intent in coordination, not BDI intention. Keyword only.

## Index Membership

- [Architecture tag head](../../../../tags/architecture-README.md) -- sources are outside participating collections, so this is not membership. The future ingest may carry `tags: [architecture]` because sections 3.a–3.d explain structural choices (deliberative, reactive and hybrid layering; control framework between layers) and their consequences. Read the head's inclusion condition when writing the ingest.

## Synthesis Opportunities

The 1995 open problems (goal generation by autonomous agents, management of multiple conflicting intentions, time-bounded deliberation) reappear in present KB work on goal prioritization and controller cost (russell-wefald, minton). A future note could test whether LLM harnesses change any of these problems or only relocate them, for example by moving transduction into context assembly. This is only a hypothesis; do not write the note from this report.

## Maintenance Observations

- No tracked ingest exists for this snapshot (`kb/sources/wooldridge-jennings-intelligent-agents.ingest.md` absent at report time). All outbound candidates are blocked until it is written.
- `kb/theory/agent-is-a-tool-loop.md` asserts a claim about the definitional debate without any source citation. The KB had no classical agent-theory source before this snapshot.

## Flags

- The source is a broad survey spanning agent definition, logics, architectures, languages and applications. Most of its catalogue content (modal-logic formalisms, individual languages and applications) has no KB counterpart. The ingest should foreground sections 1, 2.a, 2.h and 3.d, where the transferable content is.
