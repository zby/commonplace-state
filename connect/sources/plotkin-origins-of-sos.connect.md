---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/plotkin-origins-of-sos.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: The Origins of Structural Operational Semantics

**Source:** [The Origins of Structural Operational Semantics](../../../../sources/.snapshots/plotkin-origins-of-sos.md)

The source is an immutable snapshot. Under `kb/sources/COLLECTION.md` it never authors links, and nothing may author a durable link to `.snapshots/`. Every outbound candidate below is meant for the future ingest `kb/sources/plotkin-origins-of-sos.ingest.md`, which did not exist when this report was written. Every reverse-edge candidate should target that ingest, not the snapshot.

Source content used for judging: Plotkin's 2004 reconstruction of how SOS arose. (1) Abstract interpreting machines such as VDL's PL/I machine and SECD "do not scale up well when used as a human-oriented method of specification". SOS is "like an abstract machine but without all the complex machinery in the configurations": the rules make the exploration of syntactic structure "implicit rather than drearily explicit", while machines stay important for implementation. (2) The rules are syntax-directed: behaviour is defined structurally (primitive-recursively in the syntax), not compositionally. (3) Scott asked "what is operational about it?", and the term's origin is the Scott–Strachey denotational/operational distinction. (4) Plotkin moved from proving denotational adequacy against operational semantics to treating rule-based operational semantics as a specification method in its own right. (5) Small-step versus big-step semantics: Kahn's TYPOL executes rules as Horn clauses in Prolog. (6) The theory was deliberately deferred ("a theory could come later: once we had the data!"). (7) A diagrammatic rule notation shows the flow of control. (8) The real-language lecture (PASCAL) "did not get very far".

## Discovery Trace

**Collection contract:** Read the `## Outbound links` section of `kb/sources/COLLECTION.md`. Destinations: theory, reference, agent-memory-systems, agentic-systems, tags (scan only) and other sources. Excluded: `kb/work/` and `kb/instructions/`. Labels by destination: theory gets is-evidence-for, abstracted-from, rests-on, compares-with, defined-in (theory/definitions only) and see-also. Sources get compares-with and see-also. Reference gets see-also only. Agentic-systems gets compares-with and see-also. External gets derived-from, and the external target is the source URL already in hand.

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'specif|interpret|machine|executab|composition|formal|rule|operational|semantic|compil|state|config'`: about 75 hits. Flagged: `statecharts-and-programs-differ-in-what-they-show-not-compute` (the representation choice concerns what is shown, not what is computed), `llm-executed-methodologies-are-metacircular-interpreters`, `specification-strategy-should-follow-where-understanding-lives`, `unformalized-improvements-need-a-pre-formal-stage-in-the-loop` and `agentic-systems-interpret-underspecified-instructions`. All other hits are about memory, factories or scheduling and have no bearing on SOS.
- `rg '^description:'` on the flagged files and on `kb/sources/operationalism-sep.ingest.md`, `norman-problem-of-automation-inappropriate-feedback.ingest.md` and `fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md`: used to evaluate the candidates below.

**Topic indexes:**
- `kb/tags/computational-model-README.md`: lists the statecharts note and the bounded-context orchestration model and conversion lemma cluster under Scheduling & Orchestration. It confirms that the statecharts note and the conversion lemma are the PL-concepts cluster where an SOS history would land.
- No other tag head applies. The snapshot has no `tags:`, and sources sit outside tag participation.

**Body search:**
- `rg -il 'operational semantics|plotkin|structural operational' kb --glob '*.md'` (excluding snapshots) returned 6 theory hits: the conversion lemma, `agentic-systems-interpret-underspecified-instructions`, `natural-language-meaning-is-coordination-among-learned-approximations`, `definitions/codification`, `definitions/constraining` and `definitions/representational-form`. It also returned the Fodor–Pylyshyn ingest, `kb/work/operationalization-executability-automation/exploration.md` (excluded destination), work packets (excluded) and retained analysis reports.
- `rg -n -i 'operational semantics|denotational|abstract machine|SECD|plotkin' kb --glob '*.md' --glob '!**/.snapshots/**'`: line 91 of the conversion lemma ("Small-step operational semantics represents execution as transitions over machine configurations"). It also found the "unique operational semantics" criterion in representational-form and codification, line 33 of frontloading-is-partial-evaluation ("Standard PE assumes precise denotational semantics") and `kb/work/ideal-interpreter/README.md` (excluded).
- `rg -n -i 'small-step|big-step|natural semantics|horn clause|prolog|attribute grammar|structural recursion|compositional' kb/theory kb/reference kb/agentic-systems kb/sources`: no SOS-relevant hits, only CLEVR and compositional-reasoning noise in the Sutskever's-list sources and the title-as-claim note.
- `rg -n -i 'operational semantics|plotkin|abstract machine' kb/sources/operationalism-sep.ingest.md`: no direct hit. Its Extractable Value item 7 ("Disambiguate 'operational'") lists the KB's uses of "operational" but not operational semantics.

**Link following:**
- From the conversion lemma's Known lineage to the statecharts note, which cites the lemma as "this encoding made deliberately" (control state reified as explicit `K`). That is the abstract-machine direction Plotkin argues against for human specification and keeps for implementation.
- From `representational-form` to `codification` and `agentic-systems-interpret-underspecified-instructions`. The three use "unique operational semantics" as the criterion for the symbolic form and say formal semantics is "sufficient but not necessary".
- From the workshop exploration's source table (row "Plotkin (2004)": "Operational semantics is formal rule-based execution, not general operationalization", disposition "Candidate if conceptual distinction proves load-bearing"). That row identifies the ingest's occasion and its partner, the operationalism ingest. It is not a link target.

## Connections Found

- [Any symbolic program with LLM calls is a select/call program](../../../../theory/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) -- **is-evidence-for**: the note's Known lineage paragraph rests on "small-step operational semantics" and "abstract-machine compilation". Plotkin is the primary historical account of both and of how they differ. SOS was designed to *remove* machine configuration detail and keep control implicit in rules, while abstract machines reify it for implementation. The lemma's explicit `K` is the abstract-machine move, so this source both supports the lineage and sharpens which half of it the lemma uses (see Flags).
- [Statecharts and programs differ in what they show, not in what they can compute](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) -- **compares-with** on the axis "which structure a representation shows natively and which it hides in state". SECD/VDL machines and SOS rules specify the same semantics. Plotkin rejects the machines as human-oriented specification because they make syntactic traversal "drearily explicit" in "grand state". His diagrammatic notation is a further move to show the flow of control directly. This is an independent, historical instance of the note's thesis outside workflow design.
- [Representational form](../../../../theory/definitions/representational-form.md) -- **compares-with** on the axis "what fixes an artifact's operational semantics". The KB's symbolic criterion uses "unique operational semantics" to mean rules fixed by an implementing consumer, with formal semantics "sufficient but not necessary". Plotkin's operational semantics is a mathematical rule system for specification, distinct from any implementation. Scott's question "what is operational about it?" shows that the term's own boundary was contested. An ingest reader needs this to avoid reading Plotkin's sense into the KB's criterion, or the reverse.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **is-evidence-for**: the note claims that for programming languages "formal semantics is a plausible ideal even when practice falls short". Plotkin supports both halves. SOS made rule-based specification simple enough to teach and robust across a very wide range of constructs. Yet his real-language (PASCAL) lecture "did not get very far", and the notes were never revised for publication. The support is moderate: it is one practitioner's account, not a survey of language-specification practice.
- [Operationalism (SEP ingest)](../../../../sources/operationalism-sep.ingest.md) -- **compares-with** on the axis "what 'operational' names". Bridgman's operations fix the meaning of empirical concepts by measurement procedure. Plotkin's operational semantics fixes a program's meaning by a transition relation given by syntax-directed rules. The workshop exploration pairs exactly these two as contrast sources for "operationalization", so the future ingest should state the comparison so that neither sense passes as the other.

## Bidirectional Candidates

- [Operationalism (SEP ingest)](../../../../sources/operationalism-sep.ingest.md) <-> source -- **compares-with**: the operationalism ingest's item 7 ("Disambiguate 'operational'") lists the KB senses of "operational" and omits operational semantics in the PL sense, which the KB uses as the symbolic-form criterion. A return compares-with from the operationalism ingest to the Plotkin ingest would complete that disambiguation. Both ingests sit in `kb/sources/`, where compares-with is authorised.

## Reverse-edge Candidates

- [Any symbolic program with LLM calls is a select/call program](../../../../theory/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) → future `kb/sources/plotkin-origins-of-sos.ingest.md` -- **evidenced-by** (theory COLLECTION authorises it for sources): the Known lineage paragraph currently names small-step operational semantics without a citation. The Plotkin ingest would source that sentence and bound it: SOS configurations are minimal and control is implicit in the rules, so "transitions over machine configurations" fits abstract machines better than SOS.
- [Statecharts and programs differ in what they show, not in what they can compute](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) → future Plotkin ingest -- **evidenced-by**: a historical case from language semantics corroborating "equal power, different visible structure" (abstract machine versus rules, and logical versus diagrammatic rule format). It is optional, and only worth adding if the note gains a lineage or precedent paragraph.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Codification](../../../../theory/definitions/codification.md) -- it uses "unique operational semantics" with the same criterion as representational-form. The representational-form link already carries the distinction, and linking both would be redundant.
- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- it mentions "a checker with a unique operational semantics" for Lean only in passing. Plotkin adds nothing to its claim about natural language.
- [Frontloading is partial evaluation, not divide-and-conquer](../../../../theory/frontloading-can-specialize-instructions-around-known-inputs.md) -- it mentions denotational semantics as a PE assumption. Plotkin's denotational/operational history does not bear on it.
- [LLM-executed methodologies are metacircular interpreters](../../../../theory/llm-executed-methodologies-are-metacircular-interpreters.md) -- the match is on interpreter and specification vocabulary only. TYPOL's executable rules (specification as interpreter) are suggestive, but the note's claim concerns re-interpretation of natural language per session, which Plotkin does not address.
- [Improvements outside the admitted formal language need a pre-formal stage](../../../../theory/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) -- Plotkin's "a theory could come later: once we had the data!" is a pre-formal stage in a loose sense. But the note concerns improvement loops with an admitted formal language, so the match would be an analogy, not evidence.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- its spec-first and spec-mining phases concern durable artifacts in software projects. The "rules before theory" anecdote is too thin to bear on it.
- [Norman ingest](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) and [Fodor–Pylyshyn ingest](../../../../sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md) -- the Norman ingest is a co-candidate in the same workshop, but on automation feedback, with no shared axis. Fodor–Pylyshyn is about structure-sensitive processing in cognition, and its classical-architecture sense does not meet SOS.
- `kb/work/operationalization-executability-automation/exploration.md` and `kb/work/ideal-interpreter/README.md` -- topically closest, but `kb/work/` is an excluded destination.
- reference, agent-memory-systems and agentic-systems -- no candidate passed the articulation test. The agentic-systems hit (napkin retained result, "operational semantics at the query consumer") is ordinary usage.

## Index Membership

None. Sources sit outside tag participation, so no index membership applies. If the future ingest carries optional source tags, `computational-model` is the plausible head: its inclusion condition covers PL concepts applied to execution, and an ingest would have to analyse SOS in that light to qualify.

## Synthesis Opportunities

The conversion lemma, the statecharts note and this source together suggest a narrower claim than either note states. The *explicit-state* representation (abstract machine, select/call `K`) is chosen for analysis and implementation. The *implicit-control* representation (SOS rules, source program) is chosen for human specification and reading. Both notes gesture at this split, and Plotkin states it for language semantics. The claim could become a scope sentence in the statecharts note rather than a new note.

## Maintenance Observations

- The workshop exploration's source table records Plotkin as "No matching ingest in targeted searches" and links a CiteSeerX URL. The snapshot uses the Edinburgh author-hosted PDF (`homepages.inf.ed.ac.uk/gdp/publications/Origins_SOS.pdf`). After ingest, that row is stale on both points. This is workshop-local, so it is not a link target.
- The KB uses "operational semantics" as a load-bearing criterion (representational form, codification, underspecification) but has no source anchoring the PL sense of the term. A Plotkin ingest would be the first.

## Flags

- Tension to resolve in the future ingest or in the lemma: the conversion lemma's lineage sentence says small-step operational semantics "represents execution as transitions over machine configurations". Plotkin presents SOS as the deliberate *removal* of machine configurations in favour of minimal configurations plus syntax-directed rules. The lemma's reified `K` follows the abstract-machine and defunctionalization line, not SOS proper. This report flags the tension and does not resolve it.
- Outbound candidates depend on the ingest existing. The snapshot cannot carry them, and no `plotkin-origins-of-sos.ingest.md` existed at report time.
