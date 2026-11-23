---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/zollo-winter-routines-to-dynamic-capabilities.ingest.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Ingest: From Organizational Routines to Dynamic Capabilities (Zollo & Winter, 1999)

**Source:** [Ingest: From Organizational Routines to Dynamic Capabilities (Zollo & Winter, 1999)](../../../../sources/zollo-winter-routines-to-dynamic-capabilities.ingest.md)

## Discovery Trace

The ingest already links: Codification (definition), adversarial-loop writing-is-thinking, raw-accumulation, abstract-an-experience, codify-versus-LLM heuristics, Minton EBL ingest, progressive constraining, explicit retention, factory learning, Argyris ingest, Karlsson (how-to-think-in-writing) ingest, theory builder. These are treated as `known` and not re-proposed. This pass looks for edges the ingest does not yet carry.

**Collection contract:** `kb/sources/COLLECTION.md` outbound section. Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; external for `derived-from`/`see-also`. Excluded: `kb/work/` and `kb/instructions/`. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). External prospecting skipped: no external target supplied beyond the source URL (the 2002 *Organization Science* article is named in the ingest but not ingested; a `see-also` to its DOI is possible but adds nothing the Classification paragraph lacks).

**Topic indexes:**
- `kb/tags/learning-theory-README.md` (source carries `tags: [learning-theory]`). Head declares `complete: true`, so the by-tag rg over participating collections was skipped. Sources do not participate; `rg -l '^tags:.*learning-theory' kb/sources` returned Minton, Grünwald MDL, two A-MEM reports and this ingest. Only Minton is relevant, and it is already linked. The head's routes to self-improving-systems and theory builder pointed to the objective and reflection notes below.

**Titles listing (theory):**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md' | rg -i 'writ|retention|retain|reflect|routine|frequen|recur|second-order|meta|criteria|objective|tacit|explicit|experience|lesson|selection|evaluat|accumulat|distill|capabilit|improv'`. Flagged: "Revising an improvement objective is licensed from outside it or is not improvement" (kept); "Reflection makes retained lessons second-order" (kept); "A proposal-selection improvement loop requires search, evaluation, and operative retention" (kept); "Self-improving system" (kept); "Self-improvement is relative to a declared objective" (kept, also from body search); "On-balance judgments can guide improvement without a global measure" (rejected, below); "Instruction specificity should match loading frequency" (rejected); "Retaining episode evidence keeps a distilled rule open to re-examination" (rejected); "LLM generation can hide a relaxed goal where human writing exposes a stall" (kept, also from body search); "Reflective system" (rejected).

**Body search** (all over `kb/theory kb/sources kb/agentic-systems kb/agent-memory-systems kb/reference kb/tags kb/notes`, `rg -l -i -P`):
- `Zollo|Nelson and Winter|dynamic capabilit` -- only this ingest and `kb/agentic-systems/comparisons/memory/memory-systems-table.md` (incidental "dynamic capabilities" hit, not this paper). No existing inbound links.
- `organi[sz]ational learning` -- learning-is-not-only-about-generality (cites Argyris only), soft-bound-traditions (kept), Argyris ingest (known), Duguid ingest (rejected).
- `tacit` -- 18 files; relevant: soft-bound-traditions (kept), theory-and-methodology two-layer note (rejected), learning-by-writing ingest (kept). Others (concept-bottleneck, operationalism, CMMN) are keyword-only.
- `variation.{0,20}selection.{0,20}retention|blind variation|selective retention` -- proposal-selection loop note (kept), self-improving-system boundary cases (rejected), Ashby ingest (kept).
- `post-mortem|postmortem|retrospective|debrief` -- 25+ hits, mostly system reviews mentioning retrospectives as features; none makes a claim about writing as selection. No keeps.
- `Nonaka|SECI` -- soft-bound-traditions only (kept).
- `deliberat(e|ive) learning` -- sibling occasion ingests (SEP practical reason, Fishkin–Mansbridge, BDI survey, Bratman et al., Wooldridge–Jennings) and `kb/work/learning-method-name/` (excluded destination). Sibling ingests share the occasion, not a mechanism; rejected below.
- `writing (is|as) thinking|act of writing` -- adversarial-loop note (known), llm-generation-relaxes-goals (kept), Fowler and Borretti ingests (LLM-voice critiques, rejected).
- `March 1991|exploration.{0,10}exploitation|Polanyi|Schön|Schon\b|apprenticeship|staff turnover|turnover` -- soft-bound-traditions, Argyris (known); others keyword-only.
- `reuse frequency|usage count|frequency.{0,30}(retain|promot|skill)|(promot|retain).{0,40}(recurr|frequen)` -- trace-learning-techniques comparison (kept), specification-strategy note (rejected), individual system reviews (SkillRL, cortex, REM etc.; subsumed by the comparison).

**Description reads:** learning-by-writing, putting-ideas-into-words, how-to-think-in-writing, SEP practical reason, Wooldridge–Jennings, Duguid, Ashby, specification-strategy, trace-learning comparison, and the eight theory titles above.

**Link following:**
- From the proposal-selection loop note: links to self-improving-system definition, two-layer execution system and reflection-buys-addressability. Confirmed the self-improving-system definition uses Ashby's two-loop distinction ("operating a system is one loop, modifying the system that operates is another"), which matches Zollo–Winter's operational-routine versus learning-routine split.
- From revising-an-improvement-objective: links to self-improvement-is-relative-to-a-declared-objective and evidence-bearing definition. Its "proxy revision" subtraction bears on the ingest's finding that the paper does not treat its "improved effectiveness" criterion as revisable.
- From soft-bound-traditions: its Argyris and Nonaka rows place organizational learning in the "blocked" tier.

### Candidate origins

- kb/theory/revising-an-improvement-objective-is-licensed-from-outside-it.md — titles, link-following
- kb/theory/self-improvement-is-relative-to-a-declared-objective.md — body-search, titles, link-following
- kb/theory/definitions/self-improving-system.md — titles, link-following
- kb/theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md — body-search, titles
- kb/theory/reflection-makes-retained-lessons-second-order.md — titles
- kb/theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md — body-search
- kb/theory/llm-generation-relaxes-goals-where-human-writing-stalls.md — body-search, titles
- kb/sources/ashby-design-for-a-brain-ultrastability.md — body-search
- kb/sources/learning-by-writing.ingest.md — body-search
- kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md — body-search

## Connections Found

- [Revising an improvement objective is licensed from outside it or is not improvement](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) -- **compares-with**: on whether the criterion for keeping a change can be revised. The ingest records that the paper revises learning routines but leaves "improved effectiveness" fixed and undefined. The note explains why: revising a proxy check is ordinary empirical work against an unchanged objective, while revising the terminal objective needs a level outside it. Zollo–Winter's performance feedback and environmental selection revise proxies at most. This answers the occasion's fourth question more precisely than the ingest now does.
- [Self-improvement is relative to a declared objective](../../../../theory/self-improvement-is-relative-to-a-declared-objective.md) -- **compares-with**: on the improvement objective as a declared parameter. A dynamic capability is defined "in pursuit of improved effectiveness" without saying whose effectiveness or on which tasks. The note's requirement that the objective be declared with boundary and horizon names exactly what the paper leaves out. The ingest's Limitations already say "effectiveness" is not operationalized; this link gives a reader the KB's account of why that blocks attribution.
- [Self-improving system](../../../../theory/definitions/self-improving-system.md) -- **compares-with**: on second-order change to an organization's own machinery. A dynamic capability, a learned pattern that "generates and modifies its operational routines", is close to an operative, evidence-responsive change to behavior-determining organization with the firm as the declared boundary. Both draw the same two-loop line (operating versus modifying the operator). The paper's exclusion of "creative but disjointed" crisis adaptation parallels the definition's requirement of a live, repeatable pathway. Use `compares-with`, not `defined-in`: the ingest does not use the term, and the mapping is an interpretation.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **compares-with**: on the structure of the improvement cycle. Zollo–Winter's variation, internal selection, replication and retention cycle maps onto search, reject-capable evaluation and operative retention. Articulation and codification are the paper's evaluation stage, and the paper names their cost: reduced variety and added inertia. The note supplies the KB's requirement that evaluation must be able to reject; the paper's selection is described mostly by outcome feedback, so whether it can reject before replication is the point a reader should check.
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../../../../theory/reflection-makes-retained-lessons-second-order.md) -- **compares-with**: on tacit versus addressable correction. Experience accumulation corrects behavior "semi-automatically" through dispositions, without a represented commitment to revise; codified manuals make a prior routine an addressable object that a later lesson can reject or rescope. The paper's three-mechanism gradient is an organizational instance of the note's indirect-versus-explicit distinction, and its HP-versus-Corning equifinality case is a caution that the indirect route also works.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- **compares-with**: on what transfers from organizational learning to agents. The survey places Argyris and Nonaka in the blocked tier because they assume tacit-to-explicit conversion between humans. Zollo–Winter's codification claim is narrower and may sit in a different tier: its benefit comes from producing a written artifact that exposes action–outcome links, an operation an agent can perform. The paper is a test case for the survey's open question of whether organizational-learning transfer is "truly blocked or just harder".
- [LLM generation can hide a relaxed goal where human writing exposes a stall](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) -- **compares-with**: on what the act of writing does. The paper's case for codification rests on writing forcing a group to expose missing causal links; the note argues that LLM composition can bypass exactly that stall by relaxing the goal. Together they bound any transfer of Zollo–Winter's "writing as selection" to agent-written manuals: the selection effect depends on the writer being unable to proceed past a gap.
- [Ashby: Design for a Brain, ultrastability](../../../../sources/ashby-design-for-a-brain-ultrastability.md) -- **compares-with**: on the second loop that changes the first. Ashby's ultrastable system reorganizes when essential variables leave viable limits and retains by equilibrium, with no evaluator. Zollo–Winter's learning routines also act on operational routines but add an explicit internal selection stage. The pair locates the paper's contribution: the deliberate mechanisms are what replace Ashby's evaluator-free retention.
- [Learning By Writing (Karnofsky)](../../../../sources/learning-by-writing.ingest.md) -- **compares-with**: on writing as a learning mechanism. Karnofsky's first-person loop treats writing as control state for allocating evidence; Zollo–Winter make the organizational, cost-weighted version and add a contingency (writing pays more for rare, heterogeneous, ambiguous tasks). The ingest already pairs with Karlsson; Karnofsky adds the individual-practitioner contrast on evidence allocation, not only premise exposure.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **compares-with**: on frequency as a promotion criterion. Several compared systems promote observations by recurrence or frequency bonus (for example, promotion when seen on at least two dates). Zollo–Winter predict the opposite weighting for the understanding-producing value of writing: it rises as task frequency falls. This is the concrete external case for the ingest's Extractable Value item 3, that retention rules pricing only reuse under-retain for rare tasks.

## Bidirectional Candidates

- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) <-> source -- **compares-with**: the survey's organizational-learning rows cite only Argyris and Nonaka. A return link would give its "blocked or just harder" open question a source whose mechanism (writing as selection) is less dependent on human tacit knowledge. Authoring is subject to the theory collection's own outbound rules.

## Reverse-edge Candidates

- [Raw accumulation does not create usable memory](../../../../theory/raw-accumulation-does-not-create-usable-memory.md) → source -- label per theory COLLECTION.md: the ingest already cites this note as supported by the paper's "typically unusable" claim and its codification-over-experience findings for infrequent tasks. The note could cite the ingest as organizational evidence under the theory collection's own evidence label.
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) → source -- label per theory COLLECTION.md: the ingest notes the note grounds its writing-is-thinking premise in a polemic. A link from the premise to this ingest would add a scholarly, correlational source, scoped to the premise only.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../theory/abstract-an-experience-only-when-you-can-state-the-boundary.md) → source -- label per theory COLLECTION.md: the H2 heterogeneity argument (lessons transferred across dissimilar occurrences generalize wrongly unless the dimensions of difference are identified) is direct organizational support.
- [Codify-versus-LLM decision heuristics](../../../../theory/codify-versus-llm-decision-heuristics.md) → source -- label per theory COLLECTION.md: the note treats recurrence as a cost signal for symbolic codification; the paper's opposite frequency dependence applies to prose codification. A scoped return link would prevent a reader from reading the heuristic as a rule for when to write anything down. The source's "codification" must be scoped (see Flags).

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) -- addresses deciding to keep a change without a global measure, which touches the undefined "improved effectiveness", but its worked cases are software diagnostics; the objective notes above carry the point more directly.
- [Instruction specificity should match loading frequency](../../../../theory/instruction-specificity-should-match-loading-frequency.md) -- "frequency" here is context-loading frequency, not task-occurrence frequency; keyword match only.
- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) -- adjacent to codified post-mortems, but the paper says nothing about keeping episode evidence beside the distilled manual.
- [Reflective system](../../../../theory/definitions/reflective-system.md) -- the reflection-second-order note uses this definition and is the better link; a separate `defined-in` adds nothing since the ingest does not use the term.
- [The self-improving-system definition classifies its boundary cases](../../../../theory/the-self-improving-system-definition-classifies-its-boundary-cases.md) -- matched the variation–selection–retention query; the definition itself is the better target.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- recurrence-triggered promotion of symbolic specs; covered by the progressive-constraining comparison the ingest already makes.
- [Theory and methodology form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) -- mentions tacit knowledge and recurrence-triggered promotion, but at the level of agent execution paths; no shared axis beyond those already captured by progressive constraining.
- [Duguid on rereading Suchman](../../../../sources/duguid-on-rereading-suchman-situated-action.ingest.md) -- plans as interpreted resources bears on the paper's aside "if people actually follow the codified procedures!", but that aside is not a claim the ingest develops.
- [Putting ideas into words (Graham)](../../../../sources/putting-ideas-into-words.ingest.md) -- writing-as-thinking, but Karlsson (known) and Karnofsky (kept) already cover the axis; a third individual-writer source would be a spray.
- Sibling occasion ingests ([SEP practical reason](../../../../sources/sep-practical-reason.ingest.md), [Wooldridge–Jennings](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md), Fishkin–Mansbridge, BDI survey, Bratman–Israel–Pollack) -- share the workshop occasion and the word "deliberative", not a mechanism. Deliberation as weighing options is a different sense from Zollo–Winter's directed cognitive investment; linking would blur the term rather than compare it. The workshop itself (`kb/work/learning-method-name/`) is an excluded destination.
- `kb/agentic-systems/comparisons/memory/memory-systems-table.md` -- "dynamic capabilities" hit is incidental.

## Index Membership

None. Sources do not participate in tag-generated listings, and `kb/sources/README.md` is not a per-ingest index.

## Synthesis Opportunities

The ingest's Extractable Value item 3 (opposite frequency dependence of reuse value and writing-produced understanding) gains a second leg from this pass: [Minton](../../../../sources/minton-utility-of-ebl-aaai88.ingest.md) and [trace-learning promotion rules](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) price retention by recurrence, while Zollo–Winter predict a learning value that rises as recurrence falls, and [LLM generation can hide a relaxed goal](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) conditions that value on the writer actually stalling at gaps. A theory note could state when writing a procedure for a rare task pays in an agent KB, and why agent authorship may forfeit the selection effect.

## Maintenance Observations

- The paper's "codification" collides with the registered term [Codification](../../../../theory/definitions/codification.md). The ingest scopes it locally, but any return links from codify-versus-LLM or progressive constraining would carry the same risk. Check whether the [vocabulary collision ledger](../../../../reference/vocabulary-collision-ledger.md) should record the organizational-learning sense.

## Flags

- No split candidate: the ingest is one source analysis; its breadth reflects the paper, not independent assertions by the ingest.
- Tension (already noted in the ingest, not resolved here): progressive constraining waits for recurrence before committing; Zollo–Winter value writing more for rare tasks. The tension dissolves only if the two senses of "codification" stay scoped.
