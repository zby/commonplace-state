---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/iep-liar-paradox.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Liar Paradox (IEP, Bradley Dowden)

**Source:** [Liar Paradox](../../../../sources/.snapshots/iep-liar-paradox.md)

The source is an immutable snapshot. Snapshots never author links, and durable links must not point at `.snapshots/`. Every candidate below is for the matching ingest, `kb/sources/iep-liar-paradox.ingest.md`. That ingest **does not exist yet**, so this report is the only place the candidates are recorded until it is written.

What the source contributes: a secondary survey (IEP, 2023) of the Liar. It covers the Classical and Strengthened ("revenge") Liars, Contingent, Curry and Yablo variants, Convention T, and Tarski's undefinability. It sorts treatments into five "ways out", depending on which step of the argument each rejects: ungrammatical, meaningless, truth-value gap (Kripke), a faulty other step, or dialetheism. It also discusses Russell's and Tarski's hierarchies, logical monism against pluralism, and the open question of whether natural language is semantically closed or inconsistent. Its main value to this KB is that it covers the post-1944 developments. The [Tarski 1944 ingest](../../../../sources/tarski-semantic-conception-of-truth.ingest.md) says it can state those only as "background knowledge, not from the source".

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` § Outbound links. Authorized destinations are theory, reference, agent-memory-systems, agentic-systems, tags (as scan surface), other sources, and external. `kb/work/` and `kb/instructions/` are excluded. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external).

**Existence check:** `ls kb/sources/ | grep -i liar`: no ingest exists. `ls kb/sources/.snapshots/ | grep -i liar` found only the target.

**Tag heads:** I listed `kb/tags/` and read the descriptions of `computational-model`, `claims-and-grounding` and `constraining`. None has an inclusion condition that a philosophical-logic survey of the Liar meets substantively, so no source tag is recommended.

**Body search** (scope: `kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/sources kb/tags`, `--glob '*.md'`, case-insensitive). These were run as a loop, `rg -il "$q" $D`:
- `\bliar\b`: one hit, `sources/tarski-semantic-conception-of-truth.ingest.md`. Strong candidate, kept.
- `tarski`: the Tarski ingest, plus `theory/agentic-systems-interpret-underspecified-instructions.md`. Kept. The hit is the line 42 "Tarski/Gödel/halting-style impossibility results" sentence.
- `metalanguage|meta-language|object language|object-language`: the Tarski ingest; three bitter-lesson theory notes (the hits use "meta" in a different sense, rejected); and the Smith, Wuyts–Ducasse and metaobject-protocol reflection ingests. Smith was evaluated and rejected, see below.
- `\bparadox`: unrelated uses (Ironies of automation, Amodei, epiplexity, semantic leakage). All rejected as keyword-only.
- `semantically closed`, `truth predicate|theory of truth|correspondence theory`, `dialethe|paraconsistent|ex falso|principle of explosion`: the Tarski ingest only, plus incidental hits in retained AAS results and `llm-generation-relaxes-goals-where-human-writing-stalls.md` (an "explosion" keyword hit, rejected).
- `kripke|gödel|goedel|curry.s paradox|yablo`: Gödel-machine and theory-builder notes (Gödel as an incompleteness or self-modification reference, not the Liar), and the `church-turing-thesis-sep` ingest (Kripke on provability). Evaluated and rejected, see below.
- `truth.?value gap|bivalen`: incidental only.
- `russell|type theory|vicious circle`: Russell–Wefald and Stuart Russell sources, `why-notes-have-types.md` (type in the KB-type sense). All rejected as name or keyword collisions.
- `convention t|t-sentence`: false positives from substrings of other words. Rejected.
- `diagonal|fixed.point`: unrelated uses. Rejected.

**Link following:**
- From the Tarski ingest: its Connections and Extractable Value point to `agentic-systems-interpret-underspecified-instructions.md` (the narrowing audit), `traditional-software-can-bracket-executor-conformance-llm-systems.md` (which inherits the wording), `definitions/codification.md`, `definitions/representational-form.md`, `natural-language-meaning-is-coordination-among-learned-approximations.md`, and the Church–Turing and Plotkin SOS ingests. Each was re-filtered against what the IEP survey adds beyond Tarski.
- `agentic-systems-interpret-underspecified-instructions.md` lines 38–46: I read the impossibility paragraph. The survey bears on it directly.
- `natural-language-meaning-is-coordination-among-learned-approximations.md`: I scanned the hypothesis lines (16–46). The overlap is the formal-versus-natural-language question.
- `kb/work/formal-semantics-and-codification/` (read for context only; it is an excluded destination). The `tarski-thread.md` and `sources.md` files show the occasion. The thread's open part concerns semantic closure, the universality of natural language and whether that language is inconsistent, and it waits on the 1933 monograph. The survey speaks to the same open question at a secondary level.
- `smith-reflection-and-semantics-in-lisp-1984.ingest.md` lines 22 and 53: the reflective tower.
- `popper-logic-of-scientific-discovery.ingest.md` and `kb/reference/epistemic-stance.md`: I grepped for `contradict` and `consisten`. Neither discusses explosion or the Liar.

## Connections Found

- [The Semantic Conception of Truth (Tarski 1944) ingest](../../../../sources/tarski-semantic-conception-of-truth.ingest.md) -- **compares-with**: on which assumption of the Liar argument a treatment gives up. Tarski fixes classical logic and gives up semantic closure. The survey sets out the five post-Tarski ways out, including Kripke's truth-value gaps, dialetheism and revisions of classical logic, and the Strengthened-Liar "revenge" test. Those are the developments the Tarski ingest marks as uncited background knowledge. The pairing gives a reader the primary 1944 statement next to a survey of what came after it.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **is-evidence-for**: the note says complete semantics for natural language "as a whole" is unattainable "even in principle" because of "Tarski/Gödel/halting-style impossibility results". The survey reports that experts "have never agreed" on a way out. It treats whether English is semantically closed, or even inconsistent, as open ("There is significant disagreement on this issue"). It also presents several ways out that keep a truth predicate within the language by revising logic. That bears materially on the claim, mostly by narrowing it, in the same direction as Tarski ingest Extractable Value item 3. The narrowing would then rest on a survey of the field, not only on one 1944 author.
- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **compares-with**: on whether natural language has one determinate semantics that formalization recovers. The survey gives the rival positions the hypothesis argues against or sidesteps. Russell holds that natural language is incoherent and that an ideal formal language is its sensible core. Formal languages are defended as "the best that can be done rigorously" if natural language is inconsistent. Logical pluralism is set against monism. Slater argues that formal languages mishandle indexicals. None of these addresses learned competence, so the comparison clarifies the hypothesis's position but does not test it.
- External: <https://iep.utm.edu/liar-paradox/> -- **derived-from**: the ingest's analysis is worked out from this IEP entry by Bradley Dowden (revised 2023-03-28).

## Bidirectional Candidates

- [Tarski 1944 ingest](../../../../sources/tarski-semantic-conception-of-truth.ingest.md) <-> source -- **compares-with**: return path from the Tarski ingest's Contribution assessment and Limitations. Those sections assert, as background knowledge, that "Kripke's 1975 fixed-point construction and paraconsistent treatments" relax assumption (II) or full disquotation. A link to this ingest would cite a source for those claims. Note that the Tarski ingest's Quotes section is append-only and its analysis belongs to its author. This is a candidate for a deliberate revision, not a mechanical edit.

## Reverse-edge Candidates

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) → future `iep-liar-paradox.ingest.md` -- **evidenced-by** (theory → sources, authorized in `kb/theory/COLLECTION.md`): this is the load-bearing direction. When the impossibility paragraph is rewritten, as the Tarski ingest's Recommended Next Action plans, the narrowed claim can cite this ingest. It shows that semantic closure for natural language is contested, not settled, and that non-classical treatments exist. Ground the specific wording through `cp-skill-ground` once the ingest has quotes.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Traditional software can bracket executor conformance](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -- it inherits the impossibility wording from the hub note. Any correction reaches it through that note, and a direct link would duplicate the hub edge.
- [Codification](../../../../theory/definitions/codification.md) -- the Tarski ingest already carries the approximation-by-specified-fragment precedent, with primary wording. The survey adds nothing codification-specific.
- [Church–Turing thesis (SEP) ingest](../../../../sources/church-turing-thesis-sep.ingest.md) -- the only overlap is genre: both are secondary encyclopedia entries used by the same workshop. The survey has no named shared axis with the procedural-rigour precondition.
- [Smith, Reflection and semantics in Lisp](../../../../sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md) -- the Russell/Tarski hierarchy of levels and the 3-Lisp reflective tower both stratify self-reference. No KB claim consumes that analogy, so the link would be association, not traversal value.
- [Gödel machines are a proof-governed case of reflective self-modification](../../../../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md) -- it concerns proof-gated self-rewriting. The survey's Gödel content is only the incompleteness background, so the overlap is keyword-level.
- [Popper, Logic of Scientific Discovery ingest](../../../../sources/popper-logic-of-scientific-discovery.ingest.md) and [epistemic stance](../../../../reference/epistemic-stance.md) -- the survey's explosion argument ("anything follows from a contradiction") would bear on Popper's case against tolerating contradictions. Neither target discusses explosion or the Liar, so I could not articulate a specific connection.
- [Vocabulary collision ledger](../../../../reference/vocabulary-collision-ledger.md) -- the survey cautions that explications of "true" must stay true to its ordinary core. Tarski ingest item 5 already covers the one-term-per-concept precedent with primary wording.

## Index Membership

None. No tag head's inclusion condition fits substantively. Source tags are optional and do not affect member listings.

## Synthesis Opportunities

None in the library. The workshop `kb/work/formal-semantics-and-codification/` (Tarski thread, open part on semantic closure and universality) is where the survey would be consumed. Connect does not link into it.

## Maintenance Observations

- The snapshot has no tracked ingest. `commonplace-validate kb/sources` will warn that no ingest matches its URL or checksum until `iep-liar-paradox.ingest.md` exists.
- In the snapshot, trafilatura dropped the text of every section heading (bare `##` / `###` lines at 43, 86, 106, 168, 228 and others), and the Table of Contents is empty. Section locators in the future ingest's quotes will need line ranges or nearby wording instead of section titles.

## Flags

- No authored surface exists yet. All Connections Found are for the future ingest. If another agent is writing that ingest now, hand this report to it.
- Tension, not resolved here: the survey supports narrowing the hub note's "even in principle" claim. The workshop's Tarski thread holds that the stronger, universality-based reading depends on the un-ingested 1933 monograph. The survey is secondary and cannot stand in for that primary source.
