---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/iep-liar-paradox.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: Liar Paradox (Internet Encyclopedia of Philosophy, Dowden)

**Source:** [Ingest: Liar Paradox (IEP, Dowden)](../../../../sources/iep-liar-paradox.ingest.md)

## Discovery Trace

**Linking rules read:** `kb/sources/COLLECTION.md` "Outbound links". Prospected destinations: theory (incl. theory/definitions), reference, agent-memory-systems, agentic-systems, tags, sources. Excluded per contract: `kb/work/`, `kb/instructions/`. External: the ingest's `source` URL is already the derived-from surface; no external prospecting performed.

**Source content analysed:** a secondary survey that (a) quotes Tarski 1944 on semantic closure and "ordinary laws of logic"; (b) states in its own voice that natural language is either not semantically closed or inconsistent; (c) presents Kripke's gappy truth predicate and says undefinability "does not apply" to gappy languages; (d) names classical-logic assumptions (bivalence, explosion, total predicates). The ingest already authors three edges: Tarski 1944 ingest (compares-with), agentic-systems-interpret-underspecified-instructions (is-evidence-for), natural-language-meaning-is-coordination (compares-with), plus Church–Turing and operationalism SEP ingests inline in Limitations.

**Description / body search (theory, reference, agentic-systems, agent-memory-systems, tags, sources; snapshots excluded):**
- `rg -l -i 'tarski'` -- 3 hits: agentic-systems-interpret-underspecified-instructions (theory), tarski-semantic-conception-of-truth.ingest, the source itself. Both non-self hits already linked.
- `rg -l -i 'liar'` -- ~30 hits, all "reliability"/"familiar"-type substring noise or unrelated; none about the paradox.
- `rg -l -i 'semantic(ally)? closed|semantic closure'` -- tarski ingest; pattee-evolving-self-reference-1995.ingest; pattee-physics-of-symbols-2001.ingest. Pattee's "semantic closure" is a different concept (matter-symbol closure in biology); evaluated and rejected (homonym).
- `rg -l -i 'kripke'` -- church-turing-thesis-sep.ingest (Kripke on provability, unrelated content), tarski ingest.
- `rg -l -i 'truth predicate|truth-value gap|bivalen'` -- only source-side hits plus incidental mentions (martin-fowler-llm-voice, AAS retained archives); none substantive.
- `rg -l -i 'undefinab'`, `rg -l -i 'paraconsist|dialethe'` -- only the source and the Tarski ingest.
- `rg -l -i 'metalanguage|object language'` -- bitter-lesson theory notes (different sense: meta-level of methods), smith-reflection-and-semantics-in-lisp-1984.ingest, tarski ingest.
- `rg -l -i 'self-refer'` -- reflection/self-improvement cluster (goedel-machines note, maes, smith, pattee). Evaluated for the ingest's item 3 "each treatment loses some self-description" pattern; rejected (see below).
- `rg -l -i 'gödel|godel|halting'` -- self-improvement cluster; formal-systems-assess-explanatory-reach; agentic-systems-interpret-underspecified-instructions (the Tarski/Gödel/halting appeal at line 42).
- `rg -l -i 'natural language.*(formal semantics|inconsistent)|semantics of natural language'` over theory/reference/agentic-systems -- natural-language-meaning-is-coordination, traditional-software-can-bracket-executor-conformance, definitions/codification.
- `rg -n -i 'natural language' kb/theory/definitions/codification.md` -- line 23 disclaimer: "not a claim that natural language could never have a complete formal semantics". Kept.
- `rg -n -i 'formal semantics' kb/theory/traditional-software-can-bracket-executor-conformance-llm-systems.md` -- line 29 inherits "no attainable formal semantics" from the hub note. Kept as a downstream/reverse-edge consideration.

**Curated heads / tags:**
- Source carries no `tags:`. Scanned `kb/tags/` listing: no head covers formal semantics, truth or logic. `reflection-README.md` (complete: true) read for the self-description pattern; its members concern causal self-representation, not semantic self-description limits. No tag fit.

**Link following:**
- Tarski 1944 ingest Connections Found -> codification definition (is-evidence-for), representational-form (compares-with), traditional-software-can-bracket (inherits hub wording), plotkin-origins-of-sos (compares-with on execution vs truth). Re-filtered against the IEP entry.
- reflection-README -> goedel-machines note, reflective-system definition: proof/self-theory sense, not truth-in-own-language.

**Reference, agentic-systems, agent-memory-systems:** no plausible trigger; searches returned no substantive formal-semantics or truth-theory content. Skipped.

## Connections Found

- [Codification](../../../../theory/definitions/codification.md) -- **is-evidence-for**: the definition deliberately disclaims "a claim that natural language could never have a complete formal semantics" (line 23). The IEP entry reports that natural-language semantic closure and consistency are unsettled and that undefinability is conditional on classical assumptions, which supports keeping that disclaimer neutral rather than strengthening it. The Tarski ingest already links this definition on the approximation move; this edge is on the neutrality of the disclaimer.

## Bidirectional Candidates

- [Tarski 1944 ingest](../../../../sources/tarski-semantic-conception-of-truth.ingest.md) <-> source -- **compares-with**: the IEP ingest already links Tarski 1944. The Tarski ingest says post-Tarski developments (Kripke, paraconsistency) are "background knowledge, not from the source"; a return link from there to the IEP ingest would give that statement a citable secondary source.

## Reverse-edge Candidates

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -> source -- **evidence** (under theory's own rules): line 42's "Tarski/Gödel/halting-style impossibility results ... not attainable even in principle" is the claim both ingests narrow. If that paragraph is revised, it should cite the IEP ingest for the conditionality of undefinability on bivalence/explosion and the unsettled status of natural-language closure.
- [Traditional software can bracket executor conformance](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -> source -- inherits "no attainable formal semantics" (line 29) from the hub note. No direct link needed; flag that a hub revision carries over here.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Pattee, Evolving Self-Reference](../../../../sources/pattee-evolving-self-reference-1995.ingest.md) and [Pattee, Physics of Symbols](../../../../sources/pattee-physics-of-symbols-2001.ingest.md) -- "semantic closure" there is matter-symbol closure in open-ended evolution, a homonym of Tarski's term. Linking would mislead.
- [Plotkin SOS ingest](../../../../sources/plotkin-origins-of-sos.ingest.md) -- the execution-vs-truth contrast is already carried by the Tarski ingest; the IEP entry adds nothing on operational semantics.
- [Gödel machines note](../../../../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md), [Reflective system](../../../../theory/definitions/reflective-system.md), [Smith 1984 ingest](../../../../sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md) -- self-reference in the sense of causal self-representation or proof under a self-theory. The ingest's "each treatment loses some self-description" pattern is marked just-a-reference and not argued as necessary; too weak for an edge.
- [Formal systems assess explanatory reach](../../../../theory/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -- Gödel hit concerns proof-gated acceptance, not undefinability; keyword match only.
- [Church–Turing SEP ingest](../../../../sources/church-turing-thesis-sep.ingest.md), [Operationalism SEP ingest](../../../../sources/operationalism-sep.ingest.md) -- already linked inline in Limitations as genre precedents; no further compares-with axis beyond "secondary encyclopedia source".
- [Representational form](../../../../theory/definitions/representational-form.md) -- linked by the Tarski ingest on exactly specified structure; the IEP entry does not discuss that axis.
- bitter-lesson theory notes (metalanguage hits) -- "meta-level" of methods, unrelated sense.

## Index Membership

None. No tag head covers formal semantics or theories of truth, and sources do not participate in tag membership.

## Synthesis Opportunities

The Tarski 1944 ingest and this IEP ingest jointly support a narrower replacement for the hub note's impossibility appeal: the undefinability barrier holds for classically interpreted, semantically closed languages, and whether natural language is such a language is open. This is a revision of an existing paragraph in agentic-systems-interpret-underspecified-instructions (owned by the codification workshop), not a new note.

## Maintenance Observations

- The KB has no tag or curated head for formal semantics / truth theory; the three relevant sources (Tarski 1944, IEP Liar, Plotkin SOS) are reachable only through each other and the hub note. Not yet enough members to justify a head.
- The term "semantic closure" is used in two unrelated senses across sources (Tarski vs Pattee). Any future theory text using it should disambiguate.

## Flags

- Tension (already recorded in both ingests, unresolved): the hub note's "not attainable even in principle" versus the IEP entry's report that natural-language closure and consistency are open and that gappy languages escape undefinability (with the "cannot state its own thesis" objection). The workshop decides the revision.
