---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/tarski-truth-and-proof.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: Truth and Proof (Tarski, Scientific American 1969)

**Source:** [Ingest: Truth and Proof (Tarski, Scientific American 1969)](../../../../sources/tarski-truth-and-proof.ingest.md)

The ingest already authors inline links in `## Connections Found` to nine targets. Its footer labels six of them plus the external `derived-from`. This report checks those edges, adds candidates the footer omits, and proposes reverse edges. An earlier report on the snapshot ([tarski-truth-and-proof.connect.md](./tarski-truth-and-proof.connect.md)) was used as a prior. Its candidates were re-checked against the ingest as written, not copied.

## Discovery Trace

**Setup reads:**
- `kb/sources/COLLECTION.md`, section "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources, external. Excluded: `kb/work/` and `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external).
- `kb/theory/COLLECTION.md` outbound table, for reverse edges: theory→sources allows `evidenced-by`, `derived-from`, `abstracted-from` and `see-also`.
- `kb/types/connect-report.md`; the target ingest in full.

**Title and description listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | grep -i -E 'proof|truth|formal|axiom|natural language|semantic|codif|definition|indexical|context-depend|oracle|criterion|decid'`. Flagged: Causal and proof obligations; Warranted autonomy; Improvements outside the admitted formal language; Gödel machines; Oracle strength spectrum; Reliability dimensions map to oracle-hardening stages; Codification; Representational form; Semantic work can be relocated but not eliminated; Verification needs a typed target; Commitment, not derivation.
- `rg -m1 '^description:'` on semantic-work-can-be-relocated, reliability-dimensions, operationalism-sep ingest and natural-language-meaning to confirm their claims.

**Topic indexes / tag heads:**
- The ingest carries `domains:` and no `tags:`, so no by-tag rg was run. The `computational-model` and `constraining` heads exist. Their fit was judged from the earlier report's reading and the ingest's content (see Index Membership).

**Body search:**
- `rg -l -i 'tarski' kb --glob '*.md' | grep -v '^kb/work'` found the target, [the 1944 ingest](../../../../sources/tarski-semantic-conception-of-truth.ingest.md), the **new untracked** [IEP Liar Paradox ingest](../../../../sources/iep-liar-paradox.ingest.md), and the hub note [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md).
- `rg -n -i 'semantic(ally)? (universal|closed|closure)|liar|metalanguage|object-language'` over theory, reference, sources, agentic-systems and tags. Apart from the IEP and 1944 ingests, every hit was a substring match ("familiar", "auxiliary"). No theory note discusses semantic universality.
- `rg -n -i 'tarski|gödel|impossib' kb/theory/agentic-systems-interpret-underspecified-instructions.md` found line 42 ("Tarski/Gödel/halting-style impossibility results"). The appeal is still unlinked.
- `grep -n 'truth-and-proof\|1969' kb/sources/tarski-semantic-conception-of-truth.ingest.md` returned no hits, so the 1944 ingest has no return link.
- `grep -n -i 'tarski|universal|1969|truth-and-proof' kb/sources/iep-liar-paradox.ingest.md`: it cites the 1944 ingest and Church–Turing, not the 1969 ingest.
- `rg -n -i 'indexical|context-dependen|"this"|deictic'` over codification, natural-language-meaning and representational-form found nothing. Tarski's no-indexicals condition is new to those notes.
- `rg -n -i 'harden' kb/theory/oracle-strength-spectrum.md`: there is a hardening section with examples (line 28) but no proof or formalization example. `rg -c -i proof` on that note returned 0.
- `rg -n -i 'upstream|axiom|proof|formal' kb/theory/semantic-work-can-be-relocated-but-not-eliminated.md`: the general placement claim (line 12) says a judgment moves upstream where its inputs exist. The note has no formal-proof instance.
- `rg -n -i 'truth|ideal|fallib|antinom' kb/reference/epistemic-stance.md`: only fallibilism (point 1). The stance says nothing about truth as a regulative aim.

**Link following:**
- From the 1944 ingest's Limitations: the universality argument "cannot be grounded here". The 1969 ingest's Extractable Value item 1 now grounds it, which supports a return edge.
- From the IEP ingest's Connections: it names the 1944 ingest as main partner on the axis "which assumption of the Liar argument a treatment gives up". The 1969 ingest's item 4(f) also discusses the dropped classical-logic assumption, so the three ingests form one cluster.
- From the Gödel machines note to warranted-autonomy, formal-systems and unformalized-improvements: the proof-gate cluster, already linked inline from the ingest body.

**agent-memory-systems:** skipped. The README is historical and frozen, and nothing there treats truth or proof.
**agentic-systems:** the earlier report's Eigenius candidate (Lean proof versus claim correspondence) was re-checked and is still rejected (see below). No other hits.
**external:** prospecting skipped by rule. The only known external target is the `source` URL, already labelled `derived-from` in the footer.

## Connections Found

The ingest already has these as inline links with labels named in the text. The footer omits four of them. Adding footer lines is optional; the inline prose already carries the edge.
- [Gödel machines are a proof-governed case of reflective self-modification](../../../../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md) -- **is-evidence-for**: section 3 gives the classical reason the note's "some claims may be unprovable under the axioms" holds for any arithmetic-containing formalization. Inline only.
- [Improvements outside the admitted formal language need a pre-formal stage somewhere](../../../../theory/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) -- **is-evidence-for**: it bounds the "different axiomatization" remedy, since truth stays an unreached "ideal limit" and truth guides the choice of axioms. Inline only.
- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../theory/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -- **is-evidence-for**: Tarski says formal proof reduces doubt to the axioms and rules, which matches the note's "move judgment upstream rather than abolishing it". The ingest's prose does not name a label for this edge; is-evidence-for fits.
- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **compares-with** (axis: whether natural language has a semantics that formalization recovers): labelled inline, missing from the footer.

New candidates not in the ingest:
- [IEP Liar Paradox ingest](../../../../sources/iep-liar-paradox.ingest.md) -- **compares-with** (axis: Tarski's own natural-language wording versus the secondary account of it). Both ingests serve the same occasion. The IEP entry puts "either not semantically closed or inconsistent" in its own voice, quotes only 1944, and records Kripke's truth-gap escape. The 1969 ingest supplies Tarski's own 1969 wording ("semantically universal", "compelled us to abandon all attempts"). It also notes that 1969 leaves the classical-logic assumption implicit (item 4f), and the IEP's Kripke point is what makes that assumption load-bearing. A citer needs to know which ingest grounds which part of claims (1)–(3). The IEP ingest is untracked; author this edge only after it is committed.
- [Semantic work can be relocated but not eliminated](../../../../theory/semantic-work-can-be-relocated-but-not-eliminated.md) -- **is-evidence-for**: Extractable Value item 6 says formal proof leaves doubt "reduced to possible doubts concerning the truth of the few sentences listed as axioms and the infallibility of the few simple rules of proof". This is a classical instance of the note's thesis that a meaning-dependent judgment is placed, not removed: proof checking becomes shape comparison because the judgment was paid upstream, in choosing the axioms. The note currently has no formal-proof case. This is weaker than the formal-systems edge, which states the same point for formal routes. Prefer one of the two if footer space matters.
- [Church–Turing thesis (SEP) ingest](../../../../sources/church-turing-thesis-sep.ingest.md) -- **compares-with** (axis: what makes a check mechanical). Formal proof checked "simply by comparing its shape", with no "reasoning and convincing", is the deductive counterpart of the effective method's rote, insight-free execution. The earlier snapshot report proposed this edge and the ingest dropped it. It is useful for the workshop's "precise semantics" decomposition (see Synthesis), but lower priority than the IEP edge.

## Bidirectional Candidates

- [Ingest: The Semantic Conception of Truth (Tarski 1944)](../../../../sources/tarski-semantic-conception-of-truth.ingest.md) <-> source -- **compares-with**: the forward edge exists. The 1944 ingest says the universality argument "cannot be grounded here" and has no link to 1969. A return link in its analytical Connections section would send readers to the text that grounds it. This is allowed because Connections Found is not part of the append-only Quotes pool.
- [IEP Liar Paradox ingest](../../../../sources/iep-liar-paradox.ingest.md) <-> source -- **compares-with**: the IEP ingest bounds the thread's claim (2) as a secondary source. Its reader should be pointed to the primary 1969 wording.

## Reverse-edge Candidates

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) → source -- **evidenced-by** ("qualifies, or bounds"): this is the main inbound edge. When the line-42 appeal is rewritten, cite this ingest for two points. Tarski ties the liar to semantic universality, and hedges it. Truth ≠ provability concerns arithmetic-containing theories, not natural versus programming languages. Ground the passages first (Quotes is empty), or use the `(snapshot required)` marker.
- [Gödel machines are a proof-governed case of reflective self-modification](../../../../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md) → source -- **evidenced-by**: the classical bound behind "unprovable under the axioms", with its scope (arithmetic-containing theories) and exceptions (elementary geometry, real algebra).
- [Warranted autonomy is bounded by oracle domain](../../../../theory/warranted-autonomy-is-bounded-by-oracle-domain.md) → source -- **evidenced-by**: the proof oracle's domain is a definable proper subset of the truths. Optional; the Gödel machines edge covers most of it.
- [Oracle strength spectrum](../../../../theory/oracle-strength-spectrum.md) → source -- **evidenced-by**: the note has hardening examples but none from formal proof. The history of proof from "convincing" to shape comparison would be a historical case. Add this only if the note gains a sentence on it.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -- it inherits the hub note's "no attainable formal semantics" wording. Fixing the hub fixes this note, so a separate edge would duplicate the hub edge.
- [Representational form](../../../../theory/definitions/representational-form.md) -- the 1944 ingest already carries the compares-with on fixed consequences. The 1969 article adds the no-indexicals condition, but that lands on codification, which the ingest already links.
- [Plotkin, origins of SOS ingest](../../../../sources/plotkin-origins-of-sos.ingest.md) -- the contrast between truth via a metalanguage and transition rules is already authored from the 1944 ingest. 1969 adds nothing on operational semantics.
- [Operationalism (SEP) ingest](../../../../sources/operationalism-sep.ingest.md) -- "operations fix a concept only partially" resembles definition versus criterion only on the surface. Tarski's point is that a definition carries no decision procedure, not that operations under-define. Keyword match only.
- [Reliability dimensions map to oracle-hardening stages](../../../../theory/reliability-dimensions-map-to-oracle-hardening-stages.md) -- it maps empirical agent-evaluation dimensions. Proof hardening belongs on the parent spectrum note.
- [Verification needs a typed target before it needs an oracle](../../../../theory/verification-needs-a-typed-target-before-it-needs-an-oracle.md) -- the analogy between definition-versus-criterion and target-versus-oracle is surface-level. The note's target is artifact classification.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- added axioms are guided by truth, not made true by commitment. The analogy would mislead.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) -- Lean validity versus claim correspondence is a formal-to-informal gap, not incompleteness.
- [Gödel machines (Schmidhuber) ingest](../../../../sources/goedel-machines-schmidhuber.ingest.md) -- the note carries the theory-level edge. A source-to-source link adds only "Gödel is mentioned".

## Index Membership

- [computational-model tag head](../../../../tags/computational-model-README.md) -- optional source `tags: [computational-model]`, only if the head's inclusion condition covers the semantic and computational limits behind the hub note. Read the head's condition first. Source tags only aid source-scoped search and do not affect membership. Otherwise `domains:` is enough.

## Synthesis Opportunities

The Church–Turing, Plotkin, Tarski 1944, Tarski 1969 and IEP Liar ingests together separate three senses of "precise semantics" that the hub note's line-42 appeal runs together. Procedural exactness (insight-free execution) comes from Church–Turing. Operational specification comes from Plotkin. Semantic specification (truth in a richer metalanguage, under classical logic) comes from Tarski, bounded by the IEP truth-gap alternative. The 1969 ingest adds a fourth point: the proof/truth gap tracks the theory's expressive strength, not natural versus formal language. This belongs in the formal-semantics-and-codification workshop before any note.

## Maintenance Observations

- The IEP Liar Paradox ingest is untracked (git status `??`), like the target. Edges between them should be authored only once both are committed.
- The hub note's line-42 appeal is still unlinked and now has three ingests (1944, 1969, IEP) that each narrow it. The rewrite is overdue relative to the evidence held.
- The target's Quotes section is empty, and its Recommended Next Action names exact passages. Theory reverse edges should wait for `cp-skill-ground`.
- The earlier report [tarski-truth-and-proof.connect.md](./tarski-truth-and-proof.connect.md) was made on the snapshot and says "No tracked ingest exists yet". That is now stale. Its own maintenance observation is resolved by this ingest.

## Flags

- Tension, not resolved: the hub note says a complete executable semantics for natural language is "not attainable even in principle". The 1969 ingest supports only a hedged claim about truth, not execution, and says nothing about halting. The coordination note reaches "no external semantics" on different, empirical grounds. Any revision should keep these grounds separate.
- No split candidate: the ingest is one coherent source analysis, though its targets span verification, codification and stance.
