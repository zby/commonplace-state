---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/plotkin-origins-of-sos.ingest.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Ingest: The Origins of Structural Operational Semantics

**Source:** [Ingest: The Origins of Structural Operational Semantics](../../../../sources/plotkin-origins-of-sos.ingest.md)

## Discovery Trace

Authorised destinations from `kb/sources/COLLECTION.md`: theory (incl. theory/definitions), reference, agent-memory-systems, agentic-systems, tags, sources. Excluded: `kb/work/`, `kb/instructions/`. External: authorised for `derived-from`/`see-also`, but no external prospecting performed (the `source:` URL already carries the external origin).

The ingest already authors five inline connections (representational form, operationalism ingest, select/call lemma, statecharts note, underspecified-instructions note). All five paths verified to exist. This run looks for additional candidates and checks labels for the existing ones.

**Description listing scan:**
- `rg -n "^description:"` on candidates surfaced by body search: `kb/theory/methodological-and-computational-closure-track-different-changes.md`, `kb/theory/traditional-software-can-bracket-executor-conformance-llm-systems.md`, `kb/tags/computational-model-README.md`, `kb/tags/constraining-README.md`, `kb/sources/operationalism-sep.ingest.md`, `kb/sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md`, `kb/sources/cmmn-1-1-specification.ingest.md`, `kb/theory/frontloading-is-partial-evaluation-not-divide-and-conquer.md`.

**Topic indexes:**
- `kb/tags/README.md` tag list scanned; read `kb/tags/computational-model-README.md` (inclusion: explains execution mechanisms of LLM-based programs via PL concepts). The source has no `tags:`; no complete-head skip applied.
- `kb/tags/constraining-README.md` line 13 glosses codification as "symbolic artifact with formal semantics".

**Body search:**
- `rg -n -i "operational semantics|plotkin|abstract machine|SECD|small-step|big-step|denotational|structural operational|natural semantics|defunctionaliz" kb/theory kb/sources kb/reference kb/agentic-systems kb/tags` -- hits: representational-form (lines 15, 25, 34, 52-53), codification (9-50), constraining (58, 76), select/call lemma (91), natural-language-meaning (16), underspecified-instructions (38), frontloading-is-partial-evaluation (33), church-turing ingest (41), fodor-pylyshyn ingest (59), napkin archived report (269). No reference or agentic-systems review hit is substantive.
- `rg -n -i "executable spec|compositional|syntax-directed|transition system|transition relation|horn clause|prolog|formal semantics"` over the same scope -- relevant hits: traditional-software-can-bracket-executor-conformance (unique semantics / conforming interpreter), theory-and-methodology-form-a-two-layer-execution-system (64), designing-agent-memory-systems (40), exact-implementation-does-not-validate-a-requirement (46), cost-sensitive-formalisms-for-tentative-theory-search (44, 78: weighted transition system). Most are glosses of codification, not claims about specification versus implementation.
- `rg -n -i "plotkin|operational" kb/sources/operationalism-sep.ingest.md` -- confirms the operationalism ingest's item 7 ("Disambiguate 'operational'") does not yet name Plotkin.

**Link following:**
- church-turing ingest lines 35-50: its open tension on codification's criterion (notation vs non-reinterpreting consumer) is the sibling of this ingest's spec/implementation split.
- select/call lemma "Known lineage" section (lines 89-92): the sentence the ingest proposes correcting.
- traditional-software note lines 20-40: "Code aims at a unique semantics" and the conformance bracket.

## Connections Found

- [Codification](../../../../theory/definitions/codification.md) -- **compares-with**: axis is what fixes an artifact's consequences. Codification requires "a unique operational semantics" implemented by a runtime or validator; Plotkin's operational semantics is a mathematical transition relation kept separate from any implementation. The ingest already makes this point against representational form; codification is the definition that most directly borrows the term and is where a reader checking the borrowing would land. Consider adding it beside the representational-form link rather than replacing it.
- [Church–Turing thesis (SEP) ingest](../../../../sources/church-turing-thesis-sep.ingest.md) -- **compares-with**: axis is where codification's "unique operational semantics" boundary sits. Copeland's source pulls it toward "any no-insight executor" (precise prose followed rotely counts as mechanical); Plotkin's pulls the term back to a rule-specified relation distinct from execution. Both are workshop sources bounding the same criterion from opposite sides.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -- **compares-with**: axis is specification separated from executor. SOS is the historical device that gives a language a meaning independent of any interpreter, which is what makes "interpreter conformance" a definable norm that classical stacks can then bracket. The ingest's Extractable Value item 1 (operational meaning vs implementation) is the concrete PL precedent for that note's two-norm decomposition.

Existing inline connections, labels checked:
- representational form -- the ingest's prose is a comparison on "what fixes an artifact's consequences"; **compares-with** fits better than `defined-in` (the reader is not missing the term; the point is that the KB and PL senses differ).
- operationalism ingest -- **compares-with** (axis named in prose). Fine.
- select/call lemma -- **is-evidence-for**. Fine; context phrase should say it qualifies/corrects the lineage sentence.
- statecharts note -- **compares-with**. Fine.
- underspecified-instructions note -- **is-evidence-for** (moderate). Fine.

## Bidirectional Candidates

- [Operationalism (SEP) ingest](../../../../sources/operationalism-sep.ingest.md) <-> source -- **compares-with**: the operationalism ingest's Extractable Value item 7 ("Disambiguate 'operational'") lists KB senses of "operational" but not the PL sense; a return link to this ingest would complete that disambiguation list. Source-to-source compares-with is authorised in both directions.

## Reverse-edge Candidates

- [Any symbolic program with LLM calls is a select/call program](../../../../theory/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) → source -- **evidenced-by** (theory → sources, qualifies/bounds): the "Known lineage" paragraph attributes "transitions over machine configurations" to small-step operational semantics; the ingest argues explicit control state belongs to the abstract-machine/defunctionalization line, with SOS keeping configurations minimal. The note should correct the sentence and cite this ingest (snapshot required if diagram/rule details are relied on, given the pdftotext capture).
- [Codification](../../../../theory/definitions/codification.md) or [Representational form](../../../../theory/definitions/representational-form.md) → source -- **evidenced-by** (qualifies): one sentence marking that "unique operational semantics" borrows a PL term whose original sense is a specification method, and that the KB criterion is implementation-anchored. Only worth adding if the workshop decides to state this departure; otherwise leave it in the ingest.
- [Statecharts and programs differ in what they show, not in what they can compute](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) → source -- **evidenced-by** (independent earlier instance): Plotkin chose rules over SECD/VDL machines by reader burden at equal expressive power, and kept machines for implementation. This is an instance recorded independently of how the note was built, so it can corroborate only if the note's claim could have failed against it; the context phrase should state that.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Frontloading is partial evaluation, not divide-and-conquer](../../../../theory/frontloading-can-specialize-instructions-around-known-inputs.md) -- mentions denotational semantics only as a PE assumption; the source says nothing about partial evaluation. Keyword match.
- [Natural language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- uses "unique operational semantics" for Lean's checker; same term borrowing as codification, but codification is the owning definition. Linking both would be redundant.
- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) -- closure concerns who supplies decisions; SOS fixes all decisions by definition and adds nothing to that axis beyond what the church-turing ingest already supplies.
- [Fodor & Pylyshyn ingest](../../../../sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md) -- also compares with representational form, but on structure-sensitive processing, not on what "operational" names. No shared axis with this source.
- [CMMN 1.1 ingest](../../../../sources/cmmn-1-1-specification.ingest.md) -- sibling workshop source on engine-tracked lifecycles; no shared axis with SOS.
- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md) -- uses a weighted transition system as a modelling scaffold; term overlap only.
- [Bounded-context orchestration model](../../../../theory/bounded-context-orchestration-model.md) -- the lineage sentence lives in the lemma, not here; the lemma link suffices.
- `kb/tags/computational-model-README.md` as a source tag -- inclusion condition requires explaining how LLM-based programs execute; the source is pure PL history and its analysed contribution is disambiguation, not an LLM execution mechanism. Do not tag.
- `kb/agentic-systems/reports/retained-archive/AAS-2026-09-27-napkin-03/result.md` -- incidental use of "operational semantics" for query filters.

## Index Membership

None. Sources sit outside participating tag collections, and no tag's inclusion condition fits the analysed contribution.

## Synthesis Opportunities

Three workshop ingests (this one, [operationalism](../../../../sources/operationalism-sep.ingest.md), [Church–Turing](../../../../sources/church-turing-thesis-sep.ingest.md)) together bound what "operational" can mean for the KB: Bridgman's operations fix an empirical concept by procedure; Plotkin's rules fix a program's meaning by a transition relation independent of execution; Turing's effective method fixes a procedure by executor-insight-free steps. Codification's "unique operational semantics" criterion currently sits between the last two without saying which. A definition-level clarification (or workshop disposition) could state which sense the criterion uses. Leave to the workshop.

## Maintenance Observations

- The select/call lemma's "Known lineage" sentence ("Small-step operational semantics represents execution as transitions over machine configurations") is arguably inaccurate per this source; flagged as a correction candidate (see Reverse-edge Candidates).
- `kb/tags/constraining-README.md`, theory-and-methodology, exact-implementation and designing-agent-memory-systems gloss codification as "formal semantics", while codification itself says formal semantics is "sufficient but not necessary". Mild gloss drift across surfaces; not caused by this source, but this source makes the distinction sharper.

## Flags

- No split candidate: the ingest makes one coherent contribution (disambiguating "operational" and the spec/execution split).
- Tension to leave open: the church-turing ingest pulls codification's criterion toward "non-reinterpreting consumer", this ingest pulls the term toward "specification independent of consumer". Both are compares-with; do not resolve in connect.
