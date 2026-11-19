---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/tarski-semantic-conception-of-truth.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: The Semantic Conception of Truth and the Foundations of Semantics (Tarski 1944)

**Source:** [Ingest: The Semantic Conception of Truth (Tarski 1944)](../../../../sources/tarski-semantic-conception-of-truth.ingest.md)

The ingest already authors seven inline connections: the hub underspecification note, the bracket note, Codification, Representational form, the coordination hypothesis, and the Church–Turing and Plotkin ingests. All seven paths exist and their labels are in the sources outbound set. This report confirms them and adds what discovery found beyond them.

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md`, section "Outbound links". The authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags, sources and external. `kb/work/` and `kb/instructions/` are excluded. Labels for sources→theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in` (theory/definitions) and `see-also`. Labels for sources→sources: `compares-with` and `see-also`. For reverse edges, `kb/theory/COLLECTION.md` allows theory→sources with `evidenced-by`, `derived-from`, `abstracted-from` and `see-also`.

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'`, filtered with `rg -i 'semantic|meaning|formal|language|interpret|specif|truth|oracle|verif|definition|term|vocab|codif|executor|natural|clerk|underspec|decid|calculus|precise'`. Flagged: unformalized-improvements-need-a-pre-formal-stage-in-the-loop (concept not expressible in the admitted language), llm-executed-methodologies-are-metacircular-interpreters (self-application), verification-needs-a-typed-target-before-it-needs-an-oracle (definition vs criterion), vocabulary-collisions-prevented-at-write-time-not-read-time (section 14), goedel-machines-are-a-proof-governed-case-of-self-modification (truth vs provability), underspecification-and-indeterminism-complicate-programming-for, execution-indeterminism-is-a-property-of-the-sampling-process, commonplace-builds-a-theory-builder-and-tests-whether-it-learns ("no formal semantics").
- `ls kb/sources/*.ingest.md | rg -i 'semantic|formal|godel|goedel|turing|church|...|purver|schegloff|lean'`. Flagged: church-turing-thesis-sep, plotkin-origins-of-sos, smith-reflection-and-semantics-in-lisp-1984, goedel-machines-schmidhuber, the popper-* ingests, purver-ginzburg-healey-clarification-dialogue, schegloff-jefferson-sacks-self-correction-repair, formal-learning-theory.

**Topic indexes:**
- `kb/tags/computational-model-README.md`. Its inclusion condition covers "execution mechanisms or their computational limits". The hub note sits under Foundations. The ingest's audit bears on the hub's limits claim.
- `kb/tags/constraining-README.md`. Codification and the hub note are in "Definition and spectrum". Tarski's approximation by an exactly specified fragment is the classical form of codification.
- Other tag heads were checked only by filename. None plausibly fits (agent-memory, review-system, etc.).

**Body search:**
- `rg -il 'tarski' kb --glob '*.md' | grep -v '^kb/work'` matched only the source and kb/theory/agentic-systems-interpret-underspecified-instructions.md (line 42, the "Tarski/Gödel/halting-style" appeal).
- `rg -l -i '\btarski|\bmetalanguage|\bliar\b|semantically closed|disquot|formal semantics|precise semantics|truth predicate|object language|exactly specified'` over theory, reference, agentic-systems, tags, agent-memory-systems and sources ingests. This returned 28 files. Most matches are passing uses of "formal semantics". Kept for evaluation: codification, representational-form, natural-language-meaning..., traditional-software..., commonplace-builds-a-theory-builder... (line 63), instructions-are-typed-callables (line 31), and reference/vocabulary-collision-ledger.md (line 28, the "unique operational semantics" entry). The three agentic-systems retained-archive results matched "formal semantics" only incidentally and were rejected.
- An earlier variant with an unanchored `liar` produced noise from "familiar"/"auxiliary". It was re-run with `\bliar\b`.
- `rg -n -i 'tarski|correspondence|truth' kb/reference/epistemic-stance.md kb/sources/popper-*.ingest.md ...`. epistemic-stance has no truth/Tarski material. The Popper ingests mention truth only as the regulative idea of corroboration. None analyses Tarski's theory.
- `rg -n -i 'incomplet|unprovable|cannot prove|provab'` over the Gödel-machine note and ingest and the unformalized-improvements note. The Gödel-machine material is about unprovable improvements under the machine's axioms, not truth definitions.
- `rg -n -i 'underspecified-instructions|impossib|halting|precondition|insight'` over the Church–Turing and Plotkin ingests. Plotkin line 38 is already evidence for the hub note's PL-side claim ("formal semantics is a plausible ideal"). Church–Turing line 39 links the hub note's zero-underspecification condition.

**Link following:**
- Hub note lines 36–44: the appeal paragraph and its neighbours. This confirms the ingest's main target. It also shows the appeal is phrased as a limit on *executable* semantics, which is the point where Tarski's results do not reach.
- natural-language-meaning... lines 20–40: "Formalization runs the other way… Montague-style formal semantics is a later codification of the regions that stabilized". Tarski's "approximate" position is consistent with this. The existing compares-with is right.
- unformalized-improvements... lines 1–40: its antecedent ("a concept the admitted language does not contain") and "the pre-formal work was done by whoever designed the language rich enough". Tarski's essentially richer metalanguage is the classical formal instance of this.
- llm-executed-methodologies-are-metacircular-interpreters lines 8–30: natural-language rules govern edits to themselves. This is the self-application case where readers might expect a Tarski-style barrier. The ingest's item 3(c) says execution is not barred.
- Purver and Schegloff ingests (same workshop occasion): their connections centre on dialogue repair and silent disambiguation, not on specification.
- Agentic-systems and agent-memory-systems: no destination trigger matches a 1944 logic paper. Both were skipped after the body-search sweep found only incidental matches.
- External: no external targets beyond the source URL itself are in context. External prospecting was skipped as the skill requires.

## Connections Found

Already authored in the ingest (confirmed; no change needed):
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **is-evidence-for**: the source bears directly on the note's "Tarski/Gödel/halting-style impossibility" appeal, mostly by narrowing it to exactly specified, classical, fully disquotational languages.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -- **is-evidence-for**: this note inherits the hub's "no attainable formal semantics" wording, so the same narrowing applies.
- [Codification](../../../../theory/definitions/codification.md) -- **is-evidence-for**: Tarski's replacement of a natural language "(or a portion of it)" by an exactly specified language is the classical form of "a programming language in the making". His specified-but-unformalized languages are a precedent for codification's weaker-than-formal criterion.
- [Representational form](../../../../theory/definitions/representational-form.md) -- **compares-with**: on what makes an artifact's consequences fixed (assigned consequences vs exactly specified assertability conditions).
- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **compares-with**: on whether natural language has a precise semantics that formalization recovers. Both deny it, for different reasons.
- [Church–Turing thesis (SEP) ingest](../../../../sources/church-turing-thesis-sep.ingest.md) -- **compares-with**: the procedural precondition for rigour (exact no-insight instructions) vs the semantic precondition (exactly specified structure).
- [Plotkin, origins of SOS ingest](../../../../sources/plotkin-origins-of-sos.ingest.md) -- **compares-with**: fixing meaning by syntax-directed transition rules vs by truth defined in a richer metalanguage.

New candidates:
- [Improvements outside the admitted formal language need a pre-formal stage somewhere](../../../../theory/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) -- **compares-with**: on what happens when a concept has no expression in the admitted language. Tarski's undefinability is the classical formal instance: truth-for-L is not definable in L and requires choosing an essentially richer metalanguage. That choice is exactly the design-time "language rich enough to contain the answer" which the note names as relocated pre-formal work. Tarski also shows the alternative the note does not mention: take the missing concept as an undefined primitive and axiomatize it ("nothing essentially wrong in such an axiomatic procedure").
- [LLM-executed methodologies are metacircular interpreters, not compilers](../../../../theory/llm-executed-methodologies-are-metacircular-interpreters.md) -- **compares-with**: on self-application. The note describes natural-language rules that govern edits to themselves, the setting where a reader might expect a semantic-closure barrier. The ingest's Extractable Value item 3(c) says Tarski's barrier concerns defining truth within one language, not interpreting or executing it. That clarifies the note's metacircular claim does not contradict Tarski. It also shows where a barrier would bite: if the methodology tried to state its own complete correctness criterion internally.

## Bidirectional Candidates

- [Plotkin, origins of SOS ingest](../../../../sources/plotkin-origins-of-sos.ingest.md) <-> source -- **compares-with**: Plotkin's ingest is evidence for the PL half of the hub note's contrast ("formal semantics is a plausible ideal" for programming languages). This ingest bounds the natural-language half. A return link lets a reader of either ingest see both sides of the one paragraph that cites them.
- [Church–Turing thesis (SEP) ingest](../../../../sources/church-turing-thesis-sep.ingest.md) <-> source -- **compares-with**: lower priority. The Church–Turing ingest already links the hub note through condition 4 (zero underspecification). A return link to Tarski would pair the procedural and semantic preconditions for rigour from both directions.

## Reverse-edge Candidates

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) → source -- **evidenced-by**: this is the main inbound edge, and the ingest's Recommended Next Action already calls for it. When the impossibility paragraph (line 42) is rewritten, it should cite this ingest for the narrowed claim. The source *bounds* the assertion, which is within `evidenced-by`'s reader-need. The ingest's Quotes section is still empty, so grounding via `cp-skill-ground` on the four passages it lists must come first. Otherwise the link would need the `(snapshot required)` marker.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) → source -- **evidenced-by**: only if its inherited "no attainable formal semantics" wording is kept after the hub revision. If the bracket note simply defers to the hub, the hub link is enough.
- [Codification](../../../../theory/definitions/codification.md) → source -- **evidenced-by**: optional. The definition's "best intuition is formal semantics" and its weaker-than-formal criterion could cite Tarski's specified-but-unformalized languages as the classical precedent. This is worth adding only if the formal-semantics-and-codification workshop settles the criterion and promotes that wording.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Verification needs a typed target before it needs an oracle](../../../../theory/verification-needs-a-typed-target-before-it-needs-an-oracle.md) -- the analogy "definition is not criterion" ~ "target class is not oracle" is surface-level. The note's target class is artifact classification, not a truth definition. Following the link would mislead.
- [Load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../../../../theory/vocabulary-collisions-prevented-at-write-time-not-read-time.md) -- Tarski's section 14 ("different terms for different concepts") is historical precedent only. The ingest itself rates it just-a-reference. It adds no mechanism to the note.
- [Gödel machines are a proof-governed case of self-modification](../../../../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md) and [Gödel machines ingest](../../../../sources/goedel-machines-schmidhuber.ingest.md) -- the 1944 paper touches Gödel only through truth ≠ provability in note 18. The unprovable-improvement limit belongs to incompleteness and Schmidhuber's axioms, not to this source.
- [Smith, Reflection and Semantics in Lisp ingest](../../../../sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md) -- the reflective tower superficially resembles a metalanguage hierarchy, but Smith's subject is procedural reflection and causal connection, not truth definitions. The metacircular-interpreters note covers this better.
- [Purver, Ginzburg, Healey clarification dialogue ingest](../../../../sources/purver-ginzburg-healey-clarification-dialogue.ingest.md) and [Schegloff, Jefferson, Sacks repair ingest](../../../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md) -- same workshop occasion, but the axis "meaning fixed by prior specification vs by in-dialogue repair" lives in the workshop's where-meaning-is-settled.md, not in either ingest. Purver itself says most clarification requests are not about term meaning. The coordination note already mediates this contrast.
- Popper ingests ([Conjectures and Refutations](../../../../sources/popper-conjectures-and-refutations.ingest.md), [Logic of Scientific Discovery](../../../../sources/popper-logic-of-scientific-discovery.ingest.md)) -- Popper adopted Tarski's theory, but these ingests do not analyse it. A link would rest on the ingest's background-knowledge remark only.
- [Underspecification and indeterminism complicate programming for prompts](../../../../theory/programming-practices-for-prompts-need-question-specific-evidence.md), [Execution indeterminism is a property of the sampling process](../../../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md), [Instructions are typed callables](../../../../theory/instructions-are-typed-callables.md), [Commonplace builds a theory builder and tests whether it learns](../../../../theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md) -- each says natural language lacks precise or formal semantics only in passing and defers to the hub note. Linking each would duplicate the hub edge.
- [Vocabulary collision ledger](../../../../reference/vocabulary-collision-ledger.md) -- matched "operational semantics" only. Nothing in Tarski bears on that ledger entry.

## Index Membership

- [computational-model tag head](../../../../tags/computational-model-README.md) -- optional source `tags: [computational-model]`. The ingest's audit is about the computational and semantic limits behind the hub note in that head's Foundations. Sources stay outside participating collections, so this would only aid source-scoped search.
- [constraining tag head](../../../../tags/constraining-README.md) -- optional source `tags: [constraining]`. Tarski's approximation by an exactly specified fragment is the classical codification move. This is weaker than computational-model: the ingest supports codification but does not explain or apply constraining itself.

## Synthesis Opportunities

The Church–Turing, Plotkin and Tarski ingests together imply a three-part decomposition of "precise semantics". Procedural exactness (no-insight execution) comes from Church–Turing. Operational specification (a transition relation) comes from Plotkin. Semantic specification (truth or assertability conditions in a richer metalanguage) comes from Tarski. The hub note's appeal runs these together, and so does the codification criterion. A future writer revising the hub paragraph, or settling codification's criterion, could state which of the three is meant. This belongs in the formal-semantics-and-codification workshop first; it is not a note yet.

## Maintenance Observations

- The hub note (kb/theory/agentic-systems-interpret-underspecified-instructions.md, line 42) cites "Tarski/Gödel/halting-style impossibility results" with no link. This ingest now gives a reason to think the appeal overstates its premise. This is a known tension already flagged by the institution-theory import assessment and by this ingest's Recommended Next Action.
- The ingest's Quotes section is empty while its Recommended Next Action names four exact passages. Any reverse edge from theory should wait for `cp-skill-ground`, or else carry `(snapshot required)`.

## Flags

- Tension (not resolved here): the hub note claims complete executable semantics for natural language is unattainable "even in principle". The ingest argues Tarski licenses only a narrower, assumption-dependent claim about truth, not execution. The coordination note reaches a similar "no precise semantics" conclusion on different, empirical grounds. Any revision should keep the two grounds separate.
- No split candidate: the source has one subject (the reach of Tarski's results), even though it connects across theory and sources.
