---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/operationalism-sep.ingest.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Ingest: Operationalism

**Source:** [Ingest: Operationalism](../../../../sources/operationalism-sep.ingest.md)

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `kb/work/` and `kb/instructions/` excluded. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external only). External prospecting skipped: the only external target is the ingest's own `source` URL, which is already in frontmatter.

**Existing links verified (all exist):** `theory/definitions/constraining.md`, `theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md`, `theory/generality-bought-to-avoid-counterexamples-is-paid-for-in.md`, `sources/popper-logic-of-scientific-discovery.ingest.md`, `theory/natural-language-meaning-is-coordination-among-learned-approximations.md`, `theory/abstract-an-experience-only-when-you-can-state-the-boundary.md`, `theory/definitions/codification.md`, `reference/epistemic-stance.md`, `reference/vocabulary-collision-ledger.md`. These are not re-proposed below.

**Topic indexes:**
- `kb/tags/constraining-README.md` (source tag `constraining`; head is not marked `complete: true`). Scanned definition/instance/deciding groups. Candidates surfaced: `exact-implementation-does-not-validate-a-requirement` (via codification-and-relaxing link), `agentic-systems-interpret-underspecified-instructions` (rejected, see below).

**Titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | grep -iE "proxy|measur|valid|goodhart|indicator|definition|concept|meaning|term|operation|executor|transfer|extend|general|falsif|content|abstract"` -- flagged `narrowing-bought-to-survive-review-is-paid-for-in-content`, `exact-implementation-does-not-validate-a-requirement`, `use-tests-a-decomposition-locally-rationale-makes-transfer-testable`, `traditional-software-can-bracket-executor-conformance-llm-systems`, `a-method-ceiling-bounds-the-method-not-the-transfer-already-made`, `definitions/lineage`, `fix-what-the-executor-cant-determine-not-what-it-will`.

**Body search:**
- `rg -il "operationali[sz]|bridgman|operational definition|construct validity|indicator" kb/theory kb/reference kb/sources kb/agentic-systems kb/agent-memory-systems kb/tags` -- ~60 files; most use "operationalize" as ordinary English (e.g. `spec-mining-as-codification`, `system-use-selects-theory-fit-without-a-fixed-oracle`). No KB artifact discusses Bridgman or construct validity.
- `rg -n -i "operationali[sz]|bridgman|operational definition|construct validity|operational meaning" ...` -- substantive hits: `reference/link-vocabulary.md` (`operationalized-from` lineage relation), `reference/adr/054-...`, `theory/definitions/constraining.md:27` (already linked), sibling ingests `church-turing-thesis-sep.ingest.md` and `plotkin-origins-of-sos.ingest.md` (same workshop occasion).
- `rg -n "proxy|Goodhart" kb/theory -l` -- 20 files; `exact-implementation-does-not-validate-a-requirement` and the already-linked proximate-target note are the ones whose claim is about a measurable stand-in versus its objective.
- `rg -n "operationalism-sep|church-turing-thesis-sep" kb -l` -- only `plotkin-origins-of-sos.ingest.md` links this ingest (line 32).
- `rg -n -i "operational" kb/reference/vocabulary-collision-ledger.md` -- no hits.
- `rg -il "operationali" kb/agentic-systems kb/agent-memory-systems` -- one incidental hit (`trace-learning-techniques-in-related-systems.md`), rejected as ordinary usage.

**Link following:**
- `church-turing-thesis-sep.ingest.md` -> `definitions/actionable-methodology.md`, `methodological-and-computational-closure-track-different-changes.md`. Actionable methodology's operator/available-operations relativity is the axis Margenau's dilemma presses on; kept.
- `narrowing-bought-to-survive-review-is-paid-for-in-content` -> `generality-bought-...` (already linked). The narrowing note supplies the symmetric analytic-emptiness failure; kept.
- `exact-implementation-does-not-validate-a-requirement` -> `codification-and-relaxing-navigate-the-bitter-lesson-boundary`. Exact-spec vs proxy-theory distinction; kept.

## Connections Found

- [Exact implementation does not validate a requirement against its objective](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) -- **compares-with**: axis is whether a checkable criterion is the target or a conjectured stand-in. Bunge's "indicator hypothesis" and the construct-validity critique (Extractable Value 2 and 5) are the measurement-theory form of the note's requirement-as-conjectured-proxy link; reductive Bridgman is the position the note warns against, where local exactness is mistaken for upstream validity. More directly on point than the proximate-target note for the "validity needs meaning beyond the operation" claim.
- [Narrowing bought to survive review is paid for in content](../../../../theory/narrowing-bought-to-survive-review-is-paid-for-in-content.md) -- **compares-with**: axis is emptiness by definition. Gillies' argument that an operation which exhausts its concept is valid by definition has the same shape as the note's subject shrunk into the predicate's extension: true by construction, forbidding nothing. Pairs with the already-linked generality note, which covers the widening direction only.
- [Copeland's Church-Turing thesis ingest](../../../../sources/church-turing-thesis-sep.ingest.md) -- **compares-with**: axis is how "operation" is fixed relative to an executor. The effective-method conditions (no insight, paper and pencil) are a precise instance of the restrictive horn of Margenau's dilemma (Extractable Value 3); operationalism's partial, provisional sense is the opposite end. Same workshop occasion, so a reader of either needs the other to see the range.
- [Actionable methodology](../../../../theory/definitions/actionable-methodology.md) -- **compares-with**: axis is relativity to an operator and its available operations. The definition makes actionability relative to operator and operations; Bridgman's doctrine and Margenau's dilemma show what goes wrong when "available operations" is left untyped (trivial if it includes judgment, too restrictive if only codified steps). Not `defined-in`: the ingest does not use the registered term.
- [Plotkin's origins of SOS ingest](../../../../sources/plotkin-origins-of-sos.ingest.md) -- **compares-with**: axis is the sense of "operational". Plotkin anchors "operational semantics" (rule-specified transition relation); this source anchors operationalism (concept fixed by measuring operations). Supports Extractable Value 7's disambiguation.
- [Link vocabulary](../../../../reference/link-vocabulary.md) -- **see-also**: the `operationalized-from` lineage relation is a third KB sense of "operational" (executable shape adding ordering, defaults, stopping conditions). Extractable Value 7 names it without linking its definition; a reader disambiguating needs the authoritative surface.

## Bidirectional Candidates

- [Plotkin's origins of SOS ingest](../../../../sources/plotkin-origins-of-sos.ingest.md) <-> source -- **compares-with**: Plotkin already links this ingest (line 32); the return edge completes the disambiguation pair.

## Reverse-edge Candidates

- [Exact implementation does not validate a requirement against its objective](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) -> source -- theory may cite the construct-validity and indicator-hypothesis tradition as an external precedent for the requirement–objective proxy link, under theory's own `COLLECTION.md` labels.
- [Constraining](../../../../theory/definitions/constraining.md) -> source -- the definition's "definition notes that replace vague terms with operational meanings" could cite this ingest for the partiality caveat (operational definitions constrain without exhausting meaning), if theory's contract authorises a source edge from definitions.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- spec-to-program projection is about interpretation of instructions, not about whether a measurable criterion exhausts a concept; the church-turing ingest already carries the executor-conformance link.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../theory/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- shares the "transfer needs more than local success" theme with Chang's §3.2, but the mechanisms differ (retained rationale vs overlapping operations) and the source's extension claim is flagged as an untested conjecture; too speculative for a load-bearing edge now.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -- the source has no account of executor conformance; Bridgman's privacy thesis is the rejected part of the doctrine.
- [Fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- body hit is only its `Operationalized into:` footer.
- [Lineage](../../../../theory/definitions/lineage.md) -- lists `operationalized-from` but the authoritative definition of that relation is in link-vocabulary; one link suffices.
- [A method's ceiling bounds the method, not the transfer already made](../../../../theory/a-method-ceiling-bounds-the-method-not-the-transfer-already-made.md) -- "transfer" means responsibility moving off humans, not concept extension; keyword match only.
- Incidental "operationalize" hits (`spec-mining-as-codification`, `system-use-selects-theory-fit-without-a-fixed-oracle`, `bitter-lesson-selects-against-unearned-reach-not-against-structure`, `agent-memory-systems/trace-learning-techniques-in-related-systems.md`) -- ordinary English usage.

## Index Membership

- [constraining tag head](../../../../tags/constraining-README.md) -- source already carries `tags: [constraining]`; sources are outside participating collections, so no head entry is expected.

## Synthesis Opportunities

The exact-implementation note, the proximate-target note, the narrowing note and this ingest jointly imply a claim not yet stated in theory: a checkable criterion is assessable only while part of its target stays outside it; collapsing target into criterion (by operational definition, by requirement adoption, or by redefinitional narrowing) removes the ground for asking whether the criterion is right. Candidate theory note once the workshop tests it.

## Maintenance Observations

- `kb/reference/vocabulary-collision-ledger.md` has no entry for "operational/operationalize", although the KB now carries at least four senses: `operationalized-from` lineage, PL operational semantics (codification's criterion), the constraining definition's "operational meanings", and the workshop's task- and executor-scoped operationalization. The ingest's Extractable Value 7 already flags this.

## Flags

- Tension (not resolved): the constraining definition counts operational definitions as constraining without caveat, while this source argues they are partial and cannot validate themselves. Also see the church-turing ingest's open tension over codification's notation-vs-non-reinterpreting-consumer criterion, which Margenau's dilemma bears on.
