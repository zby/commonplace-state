---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/tarski-truth-and-proof.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Truth and Proof (Tarski, Scientific American, June 1969)

**Source:** [Truth and Proof](../../../../sources/.snapshots/tarski-truth-and-proof.md)

The source is an immutable snapshot. No tracked ingest exists yet: `kb/sources/tarski-truth-and-proof.ingest.md` is absent. Every outbound candidate below is meant for that future ingest, which is the authored surface under `kb/sources/COLLECTION.md`. The report never proposes a durable link to the snapshot itself.

**What the source asserts (as read for this report).** It has three sections.
1. *Truth.* It gives the T-schema as a set of partial definitions, and the finite-conjunction definition for a finite fragment. It argues that English cannot be handled this way: grammar does not fix which expressions are sentences, the set of sentences is infinite, and "true" belongs to the language. The liar (Łukasiewicz's form) is traced to the **semantic universality** of common language ("The common language is universal and is intended to be so"). Tarski treats an antinomy as a "symptom of disease": it calls for revising the system, and reconstructing the old antinomy in the new system is a test "akin to carrying out crucial experiments". He states the conditions for a formalized language: a complete vocabulary, purely formal syntax, and meaning that depends "exclusively on its form", which excludes "this" and "here". Formalized languages are meant as fragments of natural language. The definition needs an essentially richer metalanguage.
2. *Proof.* A definition of truth "does not carry with it a workable criterion for deciding". The axiomatic method developed by restricting "recourse to intuitive evidence". Proof moved from a psychological notion to a formal one. In a formal proof each step "can be directly recognized as a theorem, simply by comparing its shape". Doubt is reduced to doubt about the axioms and the rules.
3. *Relationship.* Provability can be defined inside arithmetic but truth cannot, so the provable sentences are a proper subset of the true ones. Adding axioms does not escape this for any theory that contains arithmetic. Elementary geometry and real algebra are exceptions in which provability and truth coincide. Truth is an "ideal limit" that we approximate by widening the provable set, and truth guides which axioms to add. Tarski suggests the same holds "in the realm of empirical knowledge".

## Discovery Trace

**Setup reads:**
- `kb/sources/COLLECTION.md`, section "Outbound links": the authorised destinations are theory, reference, sources, agent-memory-systems, agentic-systems, tags and external. `kb/work/` and `kb/instructions/` are excluded. The labels are `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions) and `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external).
- `kb/types/connect-report.md`.
- Reverse-edge labels: `kb/theory/COLLECTION.md` lines 118–122 allow `evidenced-by` and `see-also` toward sources. `kb/reference/COLLECTION.md` lines 99–103 allow `evidenced-by` and `see-also` toward sources.

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'`, filtered by `grep -i -E 'proof|truth|formal|verif|oracle|codif|defin|axiom|natural language|semantic|underspec|spec|test|falsif|conjecture|criterion|error|calculat|deduct|check|decid|context|reference'`. Flagged:
  - Gödel machines are a proof-governed case: about proof-gated admission and unprovable claims.
  - Warranted autonomy is bounded by oracle domain: a proof gate's domain.
  - Causal and proof obligations are two formal routes: the formalization boundary.
  - Improvements outside the admitted formal language: the warrant limit can move with a different axiomatization.
  - Agentic systems interpret underspecified instructions: contains the Tarski appeal.
  - Codification: formal semantics as the intuition.
  - Oracle strength spectrum and the verifiability gradient: formal proof as the cheapest check.
  - Verification needs a typed target: the definition comes before the oracle.
  - Commitment, not derivation: added axioms as unentailed commitments.
  - Natural-language meaning is coordination: a rival account of natural-language semantics.
- `rg -m1 '^description:'` run on each flagged file to confirm its claim.

**Topic indexes / tag heads:**
- Tag list via `ls kb/tags/`. Inclusion text read for `warranted-autonomy` (`complete: true`), `computational-model`, `evaluation` and `claims-and-grounding` (`complete: true`). The snapshot carries no `tags:`, so no tag rg was needed. No head was found whose inclusion condition the source meets substantively (see Index Membership).

**Body search:**
- `rg -l -i 'tarski' kb --glob '*.md' | grep -v '^kb/work'` found [the 1944 Tarski ingest](../../../../sources/tarski-semantic-conception-of-truth.ingest.md) and [agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md). Hits in `kb/work/formal-semantics-and-codification/` and `kb/work/institution-theory-import/` were noted but not used as candidates, because work is an excluded destination.
- `rg -n -i 'gödel|godel|incompleteness|metalanguage|object-language|liar|halting'` over theory, reference, agentic-systems, agent-memory-systems, tags and sources. This surfaced the Gödel-machine cluster (the goedel-machines note, open-ended-improvement, formal-systems, warranted-autonomy, an-omitted-loop-function) and the Sutskever's List chapters. Only the first four engage proof limits. The others are rejected or out of scope.
- `rg -n -i 'truth|regulative|verisimil|correspondence' kb/reference/epistemic-stance.md`: only line 42 matched ("verisimilitude measures" are not inherited). The stance does not yet mention truth as a regulative idea.
- `rg -n -i 'incomplete|sound|axiom|formaliz|provab'` over the goedel-machines, unformalized-improvements, warranted-autonomy and formal-systems notes. This confirmed the specific anchor sentences used below.
- `rg -n -i 'harden|proof|formal' kb/theory/oracle-strength-spectrum.md`: the oracle-hardening pipeline, which has no historical example of hardening by formalizing proof.
- `rg -n -i 'lean|axiom' kb/agentic-systems/reviews/eigenius.md`: Lean proof checking with a separate correspondence check.
- `rg -n -i 'tarski|impossib'` over the underspecified-instructions and bracket-executor notes: line 42 contains the "Tarski/Gödel/halting-style impossibility" appeal.

**Link following:**
- From the 1944 ingest: its Extractable Value item 3 lists what the library appeal can and cannot draw from Tarski. Its Limitations state that "the 'universality of colloquial language' argument is in the 1933 monograph and not here", so the 1944 ingest cannot ground it. This 1969 source states the universality argument explicitly, so it fills that gap. Its other links were followed: Church–Turing ingest (kept), Plotkin SOS ingest (rejected), Codification and Representational form (Codification kept).
- From the goedel-machines note to warranted-autonomy, formal-systems and unformalized-improvements: this is a tight cluster about the proof-gate limit, and the source supplies its classical logical anchor.

**agent-memory-systems:** skipped. `kb/agent-memory-systems/README.md` is historical and frozen (AGENTS.md), and nothing there treats truth or proof.
**external:** prospecting skipped by rule. The only known external target is the snapshot's own `source` URL, which is the ingest's `derived-from` target by construction.

## Connections Found

All of these are candidates for the future `kb/sources/tarski-truth-and-proof.ingest.md`.

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **is-evidence-for**: The source bears directly on that note's line-42 appeal to "Tarski/Gödel/halting-style impossibility", and mostly narrows it. It is the text where Tarski ties the liar to the *semantic universality* of common language. He hedges the natural-language conclusion: the reason "seems to preclude" a definition, and the supposition "appears to lead to a contradiction". He also shows that truth ≠ provability holds for formalized arithmetic itself. That last point means the result cannot be what separates natural languages from programming languages.
- [Gödel machines are a proof-governed case of reflective self-modification](../../../../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md) -- **is-evidence-for**: The note's admission limit says "Some claims may be unprovable under the axioms". Tarski's section 3 gives the classical reason this cannot be engineered away for any formalization that contains arithmetic. With sound axioms and infallible rules, true but unprovable sentences remain, and adjoining axioms does not remove them.
- [Warranted autonomy is bounded by oracle domain](../../../../theory/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **is-evidence-for**: A proof gate is the strongest oracle the note considers. Tarski shows that its domain, the provable sentences, is a definable proper subset of the truths in every arithmetic-containing theory. He also names theories (elementary geometry, real algebra) in which the two coincide. That gives the bound and its exceptions in classical form.
- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../theory/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -- **is-evidence-for**: Its section "The formalization boundary" says formal routes "move judgment upstream rather than abolishing it". Tarski says the same of formal proof: "doubts ... have not been entirely eliminated but have been reduced to possible doubts concerning the truth of the few sentences listed as axioms and the infallibility of the few simple rules of proof".
- [Improvements outside the admitted formal language need a pre-formal stage somewhere](../../../../theory/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) -- **is-evidence-for**: The note says a warrant limit is one "which better proof search or a different axiomatization can move". Tarski bounds that remedy. Axiom extension can be repeated "arbitrarily many times", but truth stays "an ideal limit which can never be reached". The choice of axiom is guided by truth, and that is a judgment made outside the formal gate, much like the note's pre-formal stage.
- [Codification](../../../../theory/definitions/codification.md) -- **is-evidence-for**: Tarski states what the formal-semantics intuition behind codification requires: a complete vocabulary, purely formal syntax, and meaning that depends "exclusively on its form", so no "this" or "here". He also says the formalized languages of interest are "fragments of natural languages" and nothing "essentially opposed" to them. This is classical support for the definition's "programming language in the making" view of a clerk-passable English fragment. It complements the 1944 ingest's support, which covers exact specification without formalization.
- [Oracle strength spectrum](../../../../theory/oracle-strength-spectrum.md) -- **is-evidence-for**: Tarski's history of the axiomatic method is a historical case of hardening an oracle. Proof moved from a psychological activity "aimed at convincing" to formal proof, where checking is "simply ... comparing its shape" and "no complex processes of reasoning and convincing are involved". The note's open questions say it has no worked case of hardening, and this would supply one.
- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **compares-with** (axis: whether natural language has a semantics that formalization recovers): Tarski presents formalized languages as fragments of natural language and claims his definition agrees with prevailing usage. His reasons why English resists definition are that sentencehood depends on context, the set of sentences is open-ended, and the language is universal. These are structural features, not claims about learned competence, so he neither supports nor refutes the hypothesis.
- [Ingest: The Semantic Conception of Truth (Tarski 1944)](../../../../sources/tarski-semantic-conception-of-truth.ingest.md) -- **compares-with** (axis: which Tarski text grounds which point): The 1944 paper is the technical exposition of truth and its assumptions (I)–(III). It says it cannot ground the "universality" argument and treats proof only in note 18. The 1969 text states universality explicitly, gives the full truth ≠ provability argument and the "ideal limit" thesis, and lists the formalized-language conditions (no indexicals). A future citer needs to know which ingest carries which passage.
- [Ingest: Church–Turing thesis (SEP)](../../../../sources/church-turing-thesis-sep.ingest.md) -- **compares-with** (axis: what makes a check mechanical): Tarski's formal proof is checkable by shape comparison without "reasoning and convincing". This is the deductive counterpart of the effective method, rote execution "needing no insight". The two together state the procedural and proof-checking preconditions for rigour.
- [Epistemic stance](../../../../reference/epistemic-stance.md) -- **see-also**: Tarski's method for antinomies matches the stance's fallibilism. An antinomy is a "symptom of disease" that forces revision of premises. The reformed system is tested by trying to reconstruct the old antinomy, "akin to carrying out crucial experiments". He also treats truth as an unreached "ideal limit", and suggests the same role in empirical knowledge. Popper adopted Tarski's theory, but that is background knowledge, not something in this source. Point 5 of the stance does not inherit verisimilitude *measures*. The ideal-limit thesis is not a measure, so the link creates no conflict.

## Bidirectional Candidates

- [Ingest: The Semantic Conception of Truth (Tarski 1944)](../../../../sources/tarski-semantic-conception-of-truth.ingest.md) <-> source -- **compares-with**: The 1944 ingest's Limitations section says the universality argument "cannot be grounded here". A return link would send readers to the text that does ground it. (Ingests are append-oriented, but Connections Found is analytical, not part of the Quotes pool, so a later revision may add it.)

## Reverse-edge Candidates

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) → future ingest -- **evidenced-by** (theory→sources, "qualifies, or bounds"): When the line-42 impossibility paragraph is rewritten, as recommended by the 1944 ingest's Recommended Next Action, it should cite this ingest for the universality argument and for the fact that truth ≠ provability does not separate natural from formal languages.
- [Gödel machines are a proof-governed case of reflective self-modification](../../../../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md) → future ingest -- **evidenced-by**: This bounds the "unprovable under the axioms" limit with the classical result and its arithmetic-containing scope.
- [Warranted autonomy is bounded by oracle domain](../../../../theory/warranted-autonomy-is-bounded-by-oracle-domain.md) → future ingest -- **evidenced-by**: This would ground "the limiting case of assurance obtained through strict acceptance" in a statement that the proof oracle's domain is strictly smaller than truth.
- [Epistemic stance](../../../../reference/epistemic-stance.md) → future ingest -- **see-also** or **evidenced-by** (reference→sources): The stance is a stub that "grows from the connections notes make to it". Tarski's antinomy-as-symptom method and the truth-as-ideal-limit thesis are candidate anchors for point 1 if it gains a sentence on truth as a regulative aim.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Ingest: Plotkin, origins of SOS](../../../../sources/plotkin-origins-of-sos.ingest.md) -- The 1944 ingest's contrast (truth by metalanguage versus syntax-directed transition rules) is already authored there. This source adds nothing on operational semantics.
- [Verification needs a typed target before it needs an oracle](../../../../theory/verification-needs-a-typed-target-before-it-needs-an-oracle.md) -- The note says a domain must be classified before an oracle can range over it. Tarski's definition-versus-criterion split looks similar, but the note's claim concerns artifact classification, not the gap between defining a property and deciding it. A link would mislead.
- [The verifiability gradient](../../../../theory/verifiability-gradient.md) -- It overlaps with the oracle-strength-spectrum candidate. The spectrum's hardening pipeline is the more specific landing for the historical proof-formalization case.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- A new axiom is an unentailed commitment, which matches only on vocabulary. The note concerns artifacts produced from sources, and Tarski's axioms are guided by truth rather than becoming ground truth by commitment. The analogy would confuse more than it helps.
- [Traditional software can bracket executor conformance](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -- It inherits the "no attainable formal semantics" wording from the hub note. Fix the hub and this note follows (the 1944 ingest already says so). A separate link is redundant.
- [Derivation and inheritance give starting warrant; evidence or proof earns scope](../../../../theory/derivation-and-inheritance-give-starting-warrant-earns-scope.md) -- It concerns the scope of a reusable decomposition's warrant. Tarski's proof is a different notion of scope, so the match is on keywords only.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) -- Lean's proof validity versus claim correspondence looks like provability versus truth, but Eigenius's gap is formal-to-informal correspondence, not incompleteness. A compares-with link would conflate the two.
- Sutskever's List chapters (`kb/sources/sutskevers-list/chapters/09-safe-superintelligence.md`, `12-references.md`): passing mentions of Gödel and halting only.

## Index Membership

None. The source falls outside every tag head's substantive inclusion condition. `warranted-autonomy` concerns AI-agent decisions, and `evaluation` concerns how KB claims and agent outputs are judged. The source is a general logic exposition and would be incidental in either. The future ingest may carry `domains: [semantic-theory-of-truth, liar-antinomy, truth-vs-provability, axiomatic-method, tarski]` instead of tags.

## Synthesis Opportunities

The goedel-machines, warranted-autonomy, unformalized-improvements and formal-systems notes each state one face of a proof gate's limit: admission, domain, warrant movable by axiomatization, and judgment moved upstream. Tarski's 1969 argument links three of them in one classical result. Provability is definable and sound but strictly narrower than truth. Repeated axiom extension guided by truth approaches truth without reaching it. Remaining doubt concentrates in the axioms. A higher-order claim could follow: no fixed or iterated formalization closes the gap, so any proof-gated improvement loop needs an extra-formal source of axiom choice. That claim is not yet stated in the KB. This is only a candidate. The unformalized-improvements note may already cover it as the "pre-formal stage", in which case Tarski is evidence and not a new synthesis.

## Maintenance Observations

- The authored surface is missing. `kb/sources/tarski-truth-and-proof.ingest.md` does not exist, so none of the candidates above can be authored until the ingest is written.
- The 1944 ingest says the "universality of colloquial language" argument "cannot be grounded here" and comes from the 1933 monograph. This 1969 source grounds a version of it in Tarski's own words ("The common language is universal and is intended to be so ... semantically universal"). The library appeal and the formal-semantics workshop's Tarski thread (point 3 of the 1944 occasion) can use this source. This is recorded here as a signal because `kb/work/` is not a link destination.
- The capture contains interleaved Scientific American advertisements (Questar, Lasertron, Sperry, Polaroid, LTV, JPL, Minolta) and OCR artefacts such as "logiC", "pOSSibly" and split words. A quote retained from this snapshot must be checked to occur exactly once, without an ad fragment inside it. The section 3 conclusion is especially at risk, because the JPL and Minolta ads split it mid-sentence.

## Flags

- Tension to keep visible, not resolve: the hub note says natural-language formal semantics is "not attainable even in principle". This source supports a narrower claim. A semantically universal, classical language that asserts all T-instances is inconsistent. Tarski himself hedges the English case ("seems to preclude", "appears to lead"). He also shows that truth ≠ provability for arithmetic, so that result does not contrast natural with programming languages.
- Not a split candidate. The future ingest will touch about 9 targets across verification, codification and epistemic-stance areas, but the source is one coherent exposition, and splitting applies to authored notes.
