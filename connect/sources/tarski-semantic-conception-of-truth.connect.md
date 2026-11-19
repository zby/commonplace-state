---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/tarski-semantic-conception-of-truth.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: The Semantic Conception of Truth and the Foundations of Semantics

**Source:** [The Semantic Conception of Truth and the Foundations of Semantics](../../../../sources/.snapshots/tarski-semantic-conception-of-truth.md)

The source is an immutable snapshot (Tarski 1944). Under `kb/sources/COLLECTION.md` the snapshot is never a link author, so every outbound candidate below is meant for the future `kb/sources/tarski-semantic-conception-of-truth.ingest.md`. That ingest did not exist when this report was written. Line numbers refer to the snapshot.

Load-bearing source passages for the candidates:

- L181–189: truth "obtains a precise meaning and can be solved in a rigorous way only for those languages whose structure has been exactly specified"; for natural languages the solution is "approximate", replacing the language (or a portion) by an exactly specified one that "diverges from the given language 'as little as possible.'"
- L187: a language can have an exactly specified structure without being formalized.
- L223–235: semantically closed languages plus ordinary logic yield the liar. Tarski decides "not to use any language which is semantically closed". For everyday language he says "the problem of consistency has no exact meaning", and that one can at most "risk the guess" that an exactly specified language close to it would be inconsistent.
- L239–265: object language / metalanguage; a positive result depends on the metalanguage being "essentially richer".
- L427: the semantic conception is epistemologically neutral.
- L457: "no universal criterion of truth follows immediately from the definition".

## Discovery Trace

**Collection contract:** read the `## Outbound links` section of `kb/sources/COLLECTION.md`. Authorised destinations: theory, theory/definitions, reference (see-also only), sources, agent-memory-systems, agentic-systems, external. `kb/work/` and `kb/instructions/` are excluded. External prospecting was skipped: the only external target is the source URL itself, which becomes the ingest's `derived-from`.

**Description listing scan:**
- `rg -N -m1 '^description:'` over candidate theory notes and `kb/theory/definitions/` (directory listing read in full). Flagged: `definitions/codification.md` (formal semantics as the best intuition; "fragment that passes the clerk test"), `definitions/representational-form.md` (assigned-consequences axis), `natural-language-meaning-is-coordination-among-learned-approximations.md` (no external semantics), `traditional-software-can-bracket-executor-conformance-llm-systems.md` (no attainable formal semantics), `agentic-systems-interpret-underspecified-instructions.md`.
- Sources ingests: `rg -l -i 'formal semantics|montague|truth-conditional|model-theoretic|semantics of natural language|lampinen|philosophy of language|wittgenstein|grice|davidson' kb/sources --glob '*.ingest.md'` returned 14 files. Kept for evaluation: `plotkin-origins-of-sos`, `church-turing-thesis-sep` (found by following codification's links), `operationalism-sep`, `symbols-neural-networks-mathematical-intelligence`. Also checked the untracked `purver-...` and `schegloff-...` ingests.

**Topic indexes:**
- `kb/tags/` listing scanned. Read the heads of `constraining-README.md` and `computational-model-README.md`. Both list `agentic-systems-interpret-underspecified-instructions` and `codification` as foundations. Neither is `complete: true` in the portion read, and no by-tag rg was needed because the snapshot carries no tags.

**Body search:**
- `rg -il 'tarski' kb --glob '*.md'` (snapshots excluded): one library hit, `kb/theory/agentic-systems-interpret-underspecified-instructions.md:42`. The other hits are workshops (excluded): `formal-semantics-and-codification/*`, `institution-theory-import/import-assessment.md:53`, `ideal-interpreter/...`, and linking-contract packets.
- `rg -il 'metalanguage|meta-language|object language'` over theory/reference/agentic-systems/agent-memory-systems/tags: three bitter-lesson notes, using "meta" in an unrelated sense. Rejected.
- `rg -il 'semantically closed|liar|self-referen'`: 15 hits, all on self-reference in agent loops or unrelated "liar" senses, none on semantic closure. Rejected.
- `rg -il 'formal semantics'`: 12 hits. Evaluated codification, representational-form, natural-language-meaning, traditional-software-can-bracket, vocabulary-collision-ledger, frontloading, and system-definition-artifacts. Only the first four engage the question of whether a language can have a fixed semantics.
- `rg -il 'denotation'`: underspecified-instructions, document-types-should-be-verifiable, frontloading-is-partial-evaluation, changing-requirements. Only the first engages a semantics claim.
- `rg -il 'truth condition|correspondence theory|theory of truth'`: reference and link-vocabulary hits use "truth" for frontmatter semantics. Rejected.
- `rg -il 'precise semantics|exactly specified|specified structure'`: instructions-are-typed-callables, execution-indeterminism, commitment-not-derivation, underspecification-and-indeterminism, underspecified-instructions. None except the last makes a claim Tarski bears on.
- `rg -il 'Gödel|Godel|halting'`: 15 theory hits, mostly self-improvement and oracle limits. Only underspecified-instructions cites Tarski-style impossibility.
- `rg -n -i 'truth|correspondence|verisimilitude' kb/reference/epistemic-stance.md`: one hit (verisimilitude, in an exclusion list). There is no correspondence-truth commitment to link.
- `rg -il 'formal semantics|metalanguage|theory of truth|tarski' kb/agentic-systems kb/agent-memory-systems` (retained archive excluded): no hits.

**Link following:**
- From `definitions/codification.md` to `church-turing-thesis-sep.ingest.md` (clerk test), `plotkin-origins-of-sos.ingest.md` and `operationalism-sep.ingest.md` (terminology), and to underspecified-instructions.
- From `traditional-software-can-bracket-...md:29,72`, which inherits "no attainable formal semantics" from underspecified-instructions. That makes underspecified-instructions the hub the Tarski claim propagates through.
- From `natural-language-meaning-...md` to Lampinen, Fodor–Pylyshyn and Smolensky ingests, and the progressive-constraining note.
- Workshop `institution-theory-import/import-assessment.md:53` (read only for context, not linkable) already flagged the line 42 impossibility paragraph for a primary-source audit.

## Connections Found

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **is-evidence-for**: line 42 appeals to "Tarski/Gödel/halting-style impossibility results" to argue that natural language as a whole cannot have a complete executable semantics. The source bears on that claim directly, but only partly in its favour. Tarski supports the claim that truth has a precise meaning only for exactly specified languages, and that natural language only admits an approximation (L189). He does not assert that everyday language is inconsistent: for him consistency "has no exact meaning" there (L235). He also ties the liar to semantic closure under ordinary logic, not to "richness" in general. The ingest should state both the support and the limit.
- [Codification](../../../../theory/definitions/codification.md) -- **is-evidence-for**: the definition calls formal semantics "the best intuition", says the clerk-passing fragment of English is "a programming language in the making", and denies "that natural language could never have a complete formal semantics". Tarski's procedure (L189) is the classical form of that move: replace a portion of natural language by an exactly specified language that diverges as little as possible. L187, where an exactly specified structure need not be formalized, bears on the definition's choice of a criterion weaker than formal semantics.
- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **compares-with** (axis: whether natural language has a precise semantics that formalization recovers): the hypothesis says no external semantics exists to approximate, and that Montague-style semantics is a lossy retrospective codification. Tarski agrees that natural-language semantics can only be approximated, but he locates the gap in unspecified structure (unknown sentence class and assertibility), not in coordination. The comparison sharpens what the hypothesis adds beyond Tarski. `is-evidence-for` would overclaim, because Tarski says nothing about learned competence.
- [Representational form](../../../../theory/definitions/representational-form.md) -- **compares-with** (axis: what makes an artifact's consequences fixed): its "assigned consequences" axis says a written formal semantics is sufficient but not necessary. Tarski's exactly specified but non-formalized languages (L187) offer a precedent, from logic, for a middle case between formal semantics and per-consumption reinterpretation.
- [Church–Turing thesis (SEP)](../../../../sources/church-turing-thesis-sep.ingest.md) -- **compares-with** (axis: the precondition for rigorous treatment of a language or procedure): codification pairs Turing's "exact instructions without insight" with formal semantics. Tarski's "exactly specified structure" is the corresponding precondition on the semantics side. Read together, the two sources give the clerk test and the specified-structure test.
- [Plotkin, origins of SOS](../../../../sources/plotkin-origins-of-sos.ingest.md) -- **compares-with** (axis: how a metatheory fixes the meaning of a formal language): Tarski fixes meaning by truth/satisfaction defined in an essentially richer metalanguage. Plotkin fixes it by syntax-directed transition rules. The KB's collision ledger already separates its "operational semantics" sense from Plotkin's, so this pairing helps a reader telling the semantic senses apart.

## Bidirectional Candidates

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) <-> source -- the note currently invokes Tarski with no source link. When its impossibility paragraph is revised, it should cite the ingest under the theory collection's rules, probably on the specified-structure claim. The note is the hub through which `traditional-software-can-bracket-...` inherits the claim.
- [Codification](../../../../theory/definitions/codification.md) <-> source -- the definition already grounds the clerk test in the Church–Turing ingest. A matching citation of the Tarski ingest for "formal semantics is the best intuition" and for approximating natural language by a specified fragment would give the semantics side the same grounding.

## Reverse-edge Candidates

- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) → source -- it asserts "no attainable formal semantics" for natural language (L29) only through underspecified-instructions. It needs a direct link only if its own wording keeps the impossibility claim after that note is revised. Otherwise inheriting through the hub is enough.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Verification needs a typed target before it needs an oracle](../../../../theory/verification-needs-a-typed-target-before-it-needs-an-oracle.md) -- Tarski separates the definition of truth from any criterion of truth (L457), which loosely parallels the note's "ontology precedes oracle". The note's mechanism is artifact classification, not truth definition. The link would be a surface analogy.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- matched "ground truth" and "precise"; the note is about artifact authority, not semantic truth.
- [Epistemic stance](../../../../reference/epistemic-stance.md) -- Popper adopted Tarski's correspondence theory, but the stance document makes no claim about truth theory. A `see-also` would be historical trivia.
- [Operationalism (SEP)](../../../../sources/operationalism-sep.ingest.md) -- it is adjacent as another theory of fixing meaning, but codification already uses it only to separate terms. Tarski's paper does not address operational definition, so there is no shared axis worth naming.
- [Symbols, neural networks, and mathematical intelligence](../../../../sources/symbols-neural-networks-mathematical-intelligence.ingest.md) -- reached through natural-language-meaning. The comparison belongs to that note, which is linked above. A direct source-to-source edge would duplicate it.
- Purver/Ginzburg/Healey and Schegloff/Jefferson/Sacks ingests -- these cover repair and clarification in dialogue. They are siblings in the same workshop's source list, but they share no axis with truth definition. They connect through the workshop, which is excluded.
- Bitter-lesson notes matching "meta-language", and agent-loop notes matching "self-referen" -- keyword-only matches.

## Index Membership

- [constraining tag head](../../../../tags/constraining-README.md) -- a tag fits only weakly. The source does not discuss narrowing interpretation for artifacts; its approximation passage is the only constraining-adjacent content. If the ingest's analysis foregrounds "replace natural language by an exactly specified language" as the classical form of codification, `tags: [constraining]` becomes defensible. Otherwise leave the ingest untagged.

## Synthesis Opportunities

The Church–Turing ingest (exact instructions without insight), Tarski (exactly specified structure as the precondition for a precise semantics) and Plotkin (rule systems specifying meaning independently of an implementation) together suggest a higher-order claim. The claim would be that the codification boundary has two classical preconditions, procedural and semantic, which the KB currently grounds only on the procedural side. That claim belongs in theory once the formal-semantics workshop settles it; connect does not create it.

## Maintenance Observations

- `kb/theory/agentic-systems-interpret-underspecified-instructions.md:42` cites Tarski with no source link, and its blanket claim ("runs into Tarski/Gödel/halting-style impossibility results") is stronger than the primary text supports (L235: consistency of everyday language "has no exact meaning"; inconsistency is only a "guess" for a specified approximation). The institution-theory workshop (`import-assessment.md:53`) and the formal-semantics workshop already flag this. The primary source is now available locally, so the audit can proceed.
- `traditional-software-can-bracket-...md` inherits the same claim, so a revision of the hub note propagates to it.

## Flags

- Tension: the KB's library text treats Tarski as support for an impossibility claim about natural language, while Tarski's own text supports only a vagueness and approximation claim, and declines to settle consistency for unspecified languages. This report flags the tension and does not resolve it. The formal-semantics workshop owns the resolution.
- No tracked ingest exists yet. All outbound candidates assume a future `kb/sources/tarski-semantic-conception-of-truth.ingest.md`.
