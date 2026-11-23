---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/zollo-winter-routines-to-dynamic-capabilities.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: From Organizational Routines to Dynamic Capabilities

**Source:** From Organizational Routines to Dynamic Capabilities (`kb/sources/.snapshots/zollo-winter-routines-to-dynamic-capabilities.md`; not linked because snapshots are ignored and the paired ingest does not exist yet)

The source is an immutable snapshot. Under `kb/sources/COLLECTION.md`, its authored connection surface is the name-paired ingest `kb/sources/zollo-winter-routines-to-dynamic-capabilities.ingest.md`, which did not exist when this report was written. Every outbound candidate below is for that ingest to author; none should be written into the snapshot.

Source claims used for judging candidates: dynamic capabilities (learned, systematic patterns that generate and modify operational routines) arise from the co-evolution of tacit experience accumulation, knowledge articulation (collective discussion, debriefs) and knowledge codification (manuals, post-mortems, tools). The three mechanisms rise in learning investment. Explicit articulation and codification gain relative effectiveness as task frequency falls, task heterogeneity rises and causal ambiguity rises (H1-H3). The cognitive benefit of codification lies in the act of writing, not only in later use of the artifact. Codification also carries inertia costs, with preliminary evidence of an inverted-U effect.

## Discovery Trace

**Contract reads:**
- `kb/sources/COLLECTION.md` outbound section: prospect `kb/theory/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/tags/` and other sources; excluded `kb/work/` and `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external).
- External prospecting skipped. The only known external target is the source URL itself (`derived-from`, owned by the ingest's frontmatter, not a candidate edge).
- `kb/theory/COLLECTION.md` and `kb/work/COLLECTION.md` labels read for reverse-edge candidates (`evidenced-by`, `see-also` from theory to sources; `evidenced-by` from work to sources).

**Pre-check for existing coverage:**
- `rg -l -i 'zollo|dynamic capabilit|nelson.{0,5}winter|organizational routine' kb --glob '*.md'` (excluding snapshots) -- hits: `kb/work/learning-method-name/README.md` (notes Zollo and Winter 2002, *Deliberate Learning and the Evolution of Dynamic Capabilities*, as "Noted and not ingested"); several agentic-system analyses and the memory-systems table where "dynamic capabilities" means Phantom's runtime capability definitions (keyword collision, rejected).

**Curated heads:**
- `kb/tags/learning-theory-README.md` (`complete: true`) -- routes to constraining (codification, decision heuristics), deploy-time-learning and agent-memory children. By-tag `rg` skipped for learning-theory because the head is complete. The snapshot carries no tags; the head was read for routing only.
- Tag list `ls kb/tags/` scanned; no organizational-learning tag exists.

**Titles listing:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'` (444 titles), filtered with `rg -i 'codif|tacit|explicit|writ|learn|routine|experien|frequen|rigid|distill|articul|procedure|skill|methodolog|deliberat|on-balance|on balance|crystal|stabil|trace|lesson|memory|organi|reflect|inert|abstract'`. Flagged and path-resolved with `rg -l -F -x '# <title>' kb/theory/`: Codification; An adversarial human-agent loop can reconstruct the writing-is-thinking filter; LLM generation can hide a relaxed goal where human writing exposes a stall; Instruction specificity should match loading frequency; Progressive constraining commits only after patterns stabilize; Codify-versus-LLM decision heuristics; Abstract an experience into a lesson only when you can state where the lesson stops; Raw accumulation does not create usable memory; Explicit retention provides direct targets for selective revision; The readable-artifact loop is the tractable unit for continual learning; Weight-resident methodologies provide context-efficient behavioral compression; System-definition artifacts are crystallized reasoning under context scarcity; Spec mining is codification's operational mechanism; Constraining during deployment can produce learning outside weights; Factory learning is experience-responsive retention that improves the factory; Maintenance operations catalogue should stage stable procedures for instructions; Methodology with incomplete coverage and its live theory fallback form a two-layer execution system; Preferential codification concentrates less predictable work at the agent boundary; Learning is not only about generality; Reflection buys addressability; Codification and relaxing navigate the bitter lesson boundary.

**Description listing scan:**
- Descriptions of the 21 flagged titles read in one pass. Kept for full reading: codification definition, writing-is-thinking note, progressive constraining, codify-versus-LLM heuristics, abstraction boundary, raw accumulation, explicit retention, factory learning. Rejected at description level: instruction-specificity (loading frequency of context, not task frequency), weight-resident methodologies, crystallized reasoning, spec mining, readable-artifact loop, two-layer execution, preferential codification, relaxing/bitter lesson (all use the symbolic-form sense of codification or address a different axis).

**Body search** (all over `kb/theory kb/reference kb/agentic-systems kb/tags kb/sources`, snapshots excluded):
- `rg -l -i -e 'tacit'` -- Argyris ingest, learning-by-writing, putting-ideas-into-words, several unrelated sources. Argyris kept; writing sources followed below.
- `rg -l -i -e 'writing.is.thinking|writing forces|act of writing'` -- writing-is-thinking note, reasoning-production note, how-to-think-in-writing, putting-ideas-into-words, learning-by-writing, Borretti ingest. Writing-is-thinking note and how-to-think-in-writing kept.
- `rg -l -i -e 'double.loop|Argyris'` -- Argyris ingest, learning-is-not-only-about-generality, soft-bound-traditions, Duguid ingest.
- `rg -l -i -e 'Nonaka|SECI'` -- soft-bound-traditions only.
- `rg -l -i -e 'exploration.{0,20}exploitation'` -- Darwin Gödel machine and Poetiq ingests, one archived agentic report; all about search allocation in self-improving agents, not Zollo and Winter's knowledge cycle. Rejected.
- `rg -l -i -e 'post.?mortem'` -- archived proposal, Sutskever list, archived report, Yegge ingest. None bear on organizational codification. Rejected.
- `rg -l -i -e 'organi[sz]ational learning'` -- learning-is-not-only-about-generality, soft-bound-traditions, Argyris ingest, Duguid ingest.
- `rg -l -i -e 'formali[sz]ation'` -- twelve theory notes on formal semantics or unformalized improvements; none about formalization-as-bureaucracy costs. Rejected.
- `rg -l -i -e 'infrequent|rare task|low.frequency'` -- Simon architecture of complexity, periodic hygiene note, others; none about frequency as a criterion for explicit learning. Rejected.
- `rg -l -i 'debrief|lessons learned|retrospective sense|sense-making|after-action' kb/theory kb/reference kb/agentic-systems` -- no hits.
- `rg -n -i 'repeated|reuse|cost' kb/theory/codify-versus-llm-decision-heuristics.md` -- located the "Repetition: is a reusable procedure worth its cost?" section.
- `rg -n -i 'experience|codif|articulat|zollo' kb/work/learning-method-name/draft-definition.md` -- no hits.

**Link following:**
- Codification definition -> its Terminology section and `kb/reference/vocabulary-collision-ledger.md`. The ledger has rows for allocation, operational, projection, provisional, refinement and worker, but none for codification.
- Writing-is-thinking note -> LLM-generation-relaxes-goals note (same filter, stated as a mechanism; the first note is the better landing point).
- learning-is-not-only-about-generality -> Argyris ingest (single-/double-loop). Zollo and Winter's double-loop remark is a one-sentence critique of Teece et al., too thin for an edge to the generality note.
- soft-bound-traditions -> its organizational-learning and knowledge-creation rows, where Zollo and Winter would fit as a source.
- Workshop `kb/work/learning-method-name/README.md` -> its Sources table (SEP practical reason, Fishkin-Mansbridge, Wooldridge-Jennings, Minton). Minton's utility formula includes application frequency, which makes a direct comparison with H1.

**Destinations with no plausible match:**
- `kb/reference/`: no system description concerns organizational learning mechanisms. Skipped after description-level check.
- `kb/agentic-systems/`: only keyword hits on Phantom's "dynamic capability" runtime objects. Skipped.
- `kb/agent-memory-systems/`: historical and frozen; no organizational-learning content found in body searches. Skipped.

### Candidate origins

- kb/theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md — titles, body-search
- kb/theory/raw-accumulation-does-not-create-usable-memory.md — titles
- kb/theory/abstract-an-experience-only-when-you-can-state-the-boundary.md — titles
- kb/theory/codify-versus-llm-decision-heuristics.md — titles, body-search
- kb/theory/only-explicit-retention-is-durable-writable-and-addressable.md — titles
- kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md — titles
- kb/theory/progressive-constraining-commits-only-after-patterns-stabilize.md — titles
- kb/sources/argyris-organizational-learning-and-mis-1977.ingest.md — body-search, link-following
- kb/sources/minton-utility-of-ebl-aaai88.ingest.md — known, link-following
- kb/sources/how-to-think-in-writing.ingest.md — body-search
- kb/theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md — body-search, link-following
- kb/work/learning-method-name/README.md — body-search

## Connections Found

All candidates are for the future `zollo-winter-routines-to-dynamic-capabilities.ingest.md`. In every context phrase, "codification" means Zollo and Winter's sense (writing manuals, post-mortems and tools), not the KB's technical term; see Flags.

- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) -- **is-evidence-for**: Zollo and Winter argue that codifying a task forces people to expose logical steps, unearth hidden assumptions and make causal links explicit, so the act of writing is a selection mechanism. This is an organizational-scale statement of the writing-is-thinking filter. It is argument plus preliminary outcome studies, not a test of where the filter lives, so it bears on the premise the note concedes, not on its loop claim.
- [Raw accumulation does not create usable memory](../../../../theory/raw-accumulation-does-not-create-usable-memory.md) -- **is-evidence-for**: the paper holds that the raw information from repeated task execution is "typically unusable" without effort to evaluate, classify, analyze and distill it. Its preliminary evidence (Singh and Zollo on bank acquisitions; Walston on hospital re-engineering) finds that codification effort, not accumulated experience, predicted performance on infrequent tasks.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../theory/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- **is-evidence-for**: H2 argues that task heterogeneity causes inappropriate generalization from past experience, which only explicit effort to identify the dimensions of heterogeneity can reduce. The Haleblian and Finkelstein U-shaped acquisition result is cited as support. This is the over-generalization failure the note names, observed in organizations.
- [Codify-versus-LLM decision heuristics](../../../../theory/codify-versus-llm-decision-heuristics.md) -- **compares-with**: on the axis of task frequency as a criterion for retaining a procedure. The note's "Repetition" section treats recurrence as a cost signal and allows one informative case to justify a procedure. Zollo and Winter go further: writing a procedure gains relative value as frequency falls, because the value lies in the understanding produced by writing it, which the cost comparison does not count.
- [Explicit retention provides direct targets for selective revision](../../../../theory/only-explicit-retention-is-durable-writable-and-addressable.md) -- **compares-with**: on the axis of tacit versus explicit retention. Zollo and Winter's HP-versus-Corning contrast (written alliance manual versus apprenticeship) and their point that tacit accumulation is vulnerable to personnel turnover correspond to the note's durability and addressability properties. Both apparently succeeded, which the paper calls equifinality; that limits any claim that explicit retention is always better.
- [Factory learning is experience-responsive retention that improves the factory](../../../../theory/factory-learning-is-experience-responsive-retention-that-improves.md) -- **compares-with**: on the axis of learning that modifies the machinery producing later work. A dynamic capability is "a learned pattern of collective activity through which the organization systematically generates and modifies its operational routines". This matches experience changing the factory's family-level machinery. Both exclude one-off adaptation: Zollo and Winter exclude disjointed crisis responses, and the note requires retained machinery changes.
- [Progressive constraining commits only after patterns stabilize](../../../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) -- **compares-with**: on the axis of when to commit a written rule. Progressive constraining waits for behaviour to repeat stably before committing to symbolic form. Zollo and Winter recommend codifying rare, heterogeneous tasks, where no stable pattern exists, for the understanding the writing yields. The two purposes differ (execution consistency versus internal selection), and the comparison is only safe if the ingest states the sense difference.
- [Organizational Learning and Management Information Systems (Argyris)](../../../../sources/argyris-organizational-learning-and-mis-1977.ingest.md) -- **compares-with**: on the axis of how organizations learn about action-outcome links. Zollo and Winter build knowledge articulation on Argyris and Schön's constructive confrontation and use the single-/double-loop distinction to criticize Teece et al. Argyris warns that formal control systems become self-sealing. Zollo and Winter make a similar point about codification inertia but treat it as a cost to weigh against benefits.
- [Quantitative Results Concerning the Utility of Explanation-Based Learning (Minton)](../../../../sources/minton-utility-of-ebl-aaai88.ingest.md) -- **compares-with**: on the axis of task frequency in deciding what to retain explicitly. Minton's utility rewards high application frequency (AvrSavings x ApplicFreq - AvrMatchCost) and counts only reuse savings. Zollo and Winter predict that explicit codification is relatively more effective at low frequency, because they also count the learning produced by writing the rule.
- [How to think in writing (Karlsson)](../../../../sources/how-to-think-in-writing.ingest.md) -- **compares-with**: on the axis of writing as a mechanism for exposing premises. Karlsson's loop fixes a conjecture and exposes its premises for counterexamples. Zollo and Winter's draft-paper example makes the same claim for groups writing manuals and adds the cost side: time, attention and inertia.

## Bidirectional Candidates

None. The useful return paths originate in other collections and are listed as reverse edges.

## Reverse-edge Candidates

- [Defining the learning process (workshop)](../../../../work/learning-method-name/README.md) → source ingest -- **evidenced-by** (work contract): the workshop records Zollo and Winter 2002 as "Noted and not ingested". This 1999 working paper sets out the same distinction between experience accumulation and deliberate articulation and codification. The Sources table could cite the ingest as the ingested precursor, while noting that it is not the 2002 article.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) → source ingest -- **evidenced-by** (theory contract): its organizational-learning and knowledge-creation rows treat externalization as blocked because agents lack tacit knowledge. Zollo and Winter locate the benefit of codification in the deliberate act of writing rather than in tacit-to-explicit conversion. That would qualify the "blocked" assessment, provided the theory note's unquoted-source limit allows another source.
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) → source ingest -- **evidenced-by** (theory contract): the note's conceded premise currently rests on Borretti's polemic. Zollo and Winter provide a scholarly organizational statement with outcome studies. The context phrase must say the evidence qualifies the premise and was not a test the loop claim could have failed.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Codification](../../../../theory/definitions/codification.md) -- `defined-in` would mislead. The KB term means moving a rule into symbolic form. Zollo and Winter's "knowledge codification" means writing prose manuals, memos and post-mortems, which the definition's Exclusions section classes as natural-language constraining. See Flags and Maintenance Observations.
- [Instruction specificity should match loading frequency](../../../../theory/instruction-specificity-should-match-loading-frequency.md) -- "frequency" there means how often context is loaded, not how often a task recurs. Keyword match only.
- [LLM generation can hide a relaxed goal where human writing exposes a stall](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) -- adjacent to the writing filter, but its claim is about LLM goal relaxation, on which the source is silent. The writing-is-thinking note is the better landing point.
- [Learning is not only about generality](../../../../theory/learning-is-not-only-about-generality.md) -- Zollo and Winter's double-loop remark is one sentence criticizing Teece et al. It does not bear on the generality axis.
- [Reflection buys addressability](../../../../theory/reflection-buys-addressability.md) -- the tacit/explicit contrast is better carried by the explicit-retention note, which has the durability axis that the turnover point needs. Linking both would duplicate.
- [Practical Reason (SEP)](../../../../sources/sep-practical-reason.ingest.md) -- the source uses "deliberative" for group discussion but offers no account of practical reasoning. The shared word is the only link.
- [Duguid on Suchman](../../../../sources/duguid-on-rereading-suchman-situated-action.ingest.md) -- plans as interpreted resources is adjacent to manuals as guidelines, but the source makes no claim about interpretation of codified routines.
- Exploration/exploitation hits (Darwin Gödel machine, Poetiq ingests) -- these concern search allocation in self-improving agents, not March's organizational knowledge cycle as the source uses it.
- Phantom "dynamic capabilities" hits in agentic-system analyses and the memory-systems table -- a runtime object name, not the strategic-management construct.
- Untracked `bdi-agent-architectures-a-survey.ingest.md` and `bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md` -- these concern individual-agent deliberation and plans, not organizational learning mechanisms. They are also in-flight work of other sessions.

## Index Membership

- [Learning theory tag head](../../../../tags/learning-theory-README.md) -- sources sit outside participating collections, so this is not membership. If the ingest carries optional search tags, `learning-theory` fits its substantive contribution (mechanisms by which retained explicit knowledge changes later capacity). `constraining` would mislead because of the codification sense collision.

## Synthesis Opportunities

Zollo and Winter (writing value is greater for rare tasks), Minton (retained-rule value grows with application frequency) and the codify-versus-LLM repetition section (frequency is a cost signal) together imply a claim not stated in the KB. The value of retaining a procedure has two components with opposite frequency dependence. Reuse savings grow with frequency, while the understanding produced by writing the procedure is relatively larger for rare, heterogeneous or causally ambiguous tasks. A retention decision that prices only reuse will under-retain for rare tasks. This would belong in `kb/theory/` as a note, after the ingest exists and quotes are retained.

## Maintenance Observations

- Vocabulary collision ledger gap: `kb/reference/vocabulary-collision-ledger.md` has no entry for "codification". The codification definition's Terminology section names ordinary and legal senses but not the organizational-learning sense ("knowledge codification" in Zollo and Winter, Kogut and Zander, Nonaka). Once an ingest cites this source, the KB will hold an established external literature that uses the term for prose manuals, which the KB classes as natural-language constraining. A ledger record would let writers who cite this literature scope the term.
- The workshop `kb/work/learning-method-name/README.md` lists Zollo and Winter 2002 as "Noted and not ingested". The workshop owner may need to know that a 1999 precursor is now captured, so the record does not imply nothing from these authors is in the KB.

## Flags

- Term collision (load-bearing): every edge from the ingest that uses "codification" must say it means Zollo and Winter's sense. Otherwise a reader following the link into `kb/theory/` will read the KB's symbolic-form definition and misjudge what the source supports. This matters most for the progressive-constraining and codify-versus-LLM comparisons.
- Tension, not resolved here: Zollo and Winter's recommendation to codify rare, heterogeneous tasks seems to conflict with progressive constraining's rule to commit only after stable repetition. Most of the apparent conflict comes from the two senses and purposes of codification. Whether any conflict remains once the senses are separated is open.
- Evidence strength: the empirical support in the source is "preliminary" and comes from cited studies (Singh and Zollo 1999, Walston 1998, Kale 1999, Zollo and Leshchinskii 1999), not from new data. `is-evidence-for` edges should not present it as more than that.
- No ingest exists yet. All outbound candidates assume the name-paired `zollo-winter-routines-to-dynamic-capabilities.ingest.md`.
