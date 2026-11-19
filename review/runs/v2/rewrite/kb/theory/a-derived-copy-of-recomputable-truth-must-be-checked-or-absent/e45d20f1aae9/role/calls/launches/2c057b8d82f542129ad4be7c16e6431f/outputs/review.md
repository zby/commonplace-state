---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/agent-memory-systems/reviews/swamp.md — needs only a citation: a rule that Swamp's rebuildable catalog and on-disk verification match. The note's checked-or-absent rule is that rule."
  - scope: passage
    quotes: ["natural-language summaries and judgments do not — there is no comparison a machine can run, so they stay as live reads or are omitted"]
    reason: "PARTLY SUPPLIED — kb/reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md — rests on the note for why the gate must be the type spec rather than a restatement of it. A gate that restates a type spec in prose is not a mechanically recomputable copy, so it falls outside the note's main rule. Only this clause of precondition 1 says such content must be a live read. The note's regime section says the opposite for judgment-derived dependents: in that regime 'the hand-maintained dependent artifact is not forbidden; it is unavoidable'."
  - scope: passage
    quotes: ["natural-language summaries and judgments do not — there is no comparison a machine can run, so they stay as live reads or are omitted"]
    reason: "PARTLY SUPPLIED — kb/reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md — rests on the note for why the gate must be COLLECTION.md rather than a catalog gate that restates it. ADR 038 has the same gap: the restated gate is prose rather than a mechanically re-derivable copy. Only precondition 1's live-read clause supports the need, and the regime section allows hand-maintained judgment-derived dependents."
  - scope: passage
    quotes: ["Enforcement is available only when four preconditions hold:"]
    reason: "SUPPLIED — kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md — needs the forbidden state, the four preconditions (derivation rule, locatability, ground truth present at validation time, an amortized central validator) and the Level A classification so that it can argue the quote check is obligatory and deterministic. The note states all of them."
  - scope: passage
    quotes: ["the `status:` maturity field is a candidate trust mark with no validator"]
    reason: "SUPPLIED — kb/reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md — needs, as a see-also, the marks doctrine that rules out an unvalidated lifecycle frontmatter field. The note supplies it through the consequence 'A checkable claim is enforced as a check or not asserted at all' and this open question about an unvalidated status field."
  - scope: passage
    quotes: ["Such a copy has exactly two valid states."]
    reason: "SUPPLIED — kb/reference/adr/068-collection-contracts-stop-enumerating-available-types.md — rests on the rule that decides between removing a copy and enforcing it, and uses that rule to classify an unparsed type menu as the configuration the note rules out. The two-state rule and the forbidden middle supply this."
  - scope: passage
    quotes: ["a validator re-derives it from the source and fails on mismatch"]
    reason: "SUPPLIED — kb/reference/proposals/a-reader-facing-banner-for-user-verification.md — rests on the claim that a committed banner is safe only when it is mechanically checked against frontmatter. The note's definition of the checked state supplies that claim."
  - scope: passage
    quotes: ["a validator re-derives it from the source and fails on mismatch"]
    reason: "SUPPLIED — kb/reference/proposals/archive/atomic-step-grounding-bounds-unquoted-sources-per-note.md — needs the claim that an inline quotation is an admissible checked copy, not a second evidence store, because a validator re-derives it and fails on mismatch. The dependent paraphrases the note's checked-state definition almost word for word."
  - scope: passage
    quotes: ["or it is **absent**: deleted, or replaced by reading the source live"]
    reason: "SUPPLIED — kb/reference/proposals/archive/source-genre-is-one-open-field-on-the-snapshot.md — needs the single-ground-truth rationale for dropping the ingest report's copy of genre and reading the snapshot's copy instead. The note's absent branch, which includes reading the source live, supplies it."
  - scope: passage
    quotes: ["A checkable claim is enforced as a check or not asserted at all."]
    reason: "SUPPLIED — kb/reference/proposals/archive/tag-scope-is-declared-where-membership-claims-are-made.md — rests on the rule that a derived claim is either enforced or not made, and extends it so that scope is a parameter the check must enforce. The note supplies the enforce-or-omit rule. The extension to scope parameters belongs to the dependent; the note implies it only through instance 1's 'participating collections'."
  - scope: document
    quotes: []
    reason: "PARTLY SUPPLIED — kb/reference/proposals/channel-compiled-instruction-artifacts.md — rests on the note for the constraint that an install-time compiled procedure must satisfy. The note's absent branch is named as 'deleted, or replaced by reading the source live'. Generation at build or install time appears only through the ADR 025 example and the phrase 'a build-time or hot-path cost', not as a stated form of a valid copy."
  - scope: passage
    quotes: ["What is the cheapest general mechanism for marked, locatable, checkable frontloaded regions in instruction text?"]
    reason: "SUPPLIED — kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md — needs the rule that excludes a trusted, hand-maintained inline copy and the deterministic-oracle boundary. The note supplies both, together with precondition 2 (a marked region that names its source). The proposal takes up the question this open question leaves open."
  - scope: passage
    quotes: ["There is no safe middle where the copy is maintained by hand and trusted by consumers."]
    reason: "SUPPLIED — kb/reference/proposals/decisions-bind-their-consumers-through-site-back-pointers.md — rests on the note for why a back-pointer must be validator-checked and why a hand-maintained decision index is rejected outright. The forbidden middle supplies both."
  - scope: passage
    quotes: ["natural-language summaries and judgments do not — there is no comparison a machine can run, so they stay as live reads or are omitted"]
    reason: "PARTLY SUPPLIED — kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md — rests on the note for why each dependency document must be the gate rather than be restated in one. ADRs 038 and 041 have the same gap: a prose restatement is not a mechanically recomputable copy, and the note's regime section allows hand-maintained judgment-derived dependents."
  - scope: passage
    quotes: ["Enforcement cannot help where execution itself produces the evidence"]
    reason: "PARTLY SUPPLIED — kb/reference/validation-contract.md — needs two things: why a referential check is obligatory, and why a false copy fails while an absent one only warns. The asymmetry and the two-state rule supply both. The contract also calls 'a referential check's ground truth lives in a second artifact' the note's precondition 3. The note's precondition 3 is about whether ground truth exists at validation time, not about where it is stored, so the dependent uses the precondition in another sense."
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/sources/build-systems-a-la-carte-theory-and-practice.ingest.md — offers §3.6 as evidence that formally defines 'checked'. It needs only the note's claim as the target of that evidence, and the note states the claim. The passage was cut at 1200 characters."
  - scope: passage
    quotes: ["that is why hand-maintained-and-trusted is *forbidden* rather than merely risky"]
    reason: "PARTLY SUPPLIED — kb/sources/dagster-asset-versioning-and-caching.ingest.md — needs the note's 'forbidden' claim as the claim it qualifies. A production system ships a trusted, hand-declared code_version as its default and offers source hashing only as the checked option. The note states the claim but never addresses a deployed system that makes the trusted hand-declared copy its default. The rest of the passage was cut at 1200 characters."
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md — offers a generated handbook kept subordinate to its source (locator validation, fingerprints, diff-driven invalidation, freezing of unverifiable entries) as a technical basis for the note's claim. It needs only the claim, which the note states."
  - scope: passage
    quotes: ["The copy must occupy a marked region that names its source"]
    reason: "SUPPLIED — kb/sources/prov-overview.ingest.md — a connection marked just-a-reference: lineage records are themselves derived artifacts that can go stale. The note's rule applies to such records, and precondition 2 names lineage as what the validator follows. The dependent needs nothing more."
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/tags/claims-and-grounding-README.md — needs only a citation and a one-line gloss: a copy of recomputable information is machine-checked against its source or does not exist. The note's opening paragraph matches the gloss."
  - scope: passage
    quotes: ["Enforcement is the third class that lets both stand"]
    reason: "SUPPLIED — kb/tags/context-engineering-README.md — needs a citation for when a recomputable value is safe to inline for context economy: only when a validator re-derives it, otherwise as a live read. The 'What enforcement buys' section supplies that."
  - scope: passage
    quotes: ["can cause silent, unbounded wrongness when it tells consumers to stop looking"]
    reason: "SUPPLIED — kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md — needs the asymmetry (a false copy misleads silently, an absent one costs a recomputation) to explain why a wording mismatch fails rather than warns. It also limits that reasoning to wording, and states that the source bytes must be present, which is the note's precondition 3. The note supplies both."
  - scope: passage
    quotes: ["a trusted-but-stale claim suppresses the recomputation that would have exposed the mismatch"]
    reason: "SUPPLIED — kb/theory/a-consumption-channel-delivers-force-without-the-history-that.md — needs the claim that a stale or unbacked trust mark can suppress the check that would catch it, and therefore that a recomputable mark must be checked or absent. The note supplies this, and its open question names the same kind of mark (the status field)."
  - scope: passage
    quotes: ["natural-language summaries and judgments do not — there is no comparison a machine can run, so they stay as live reads or are omitted"]
    reason: "SUPPLIED — kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md — needs the grounds for trusting a validated quote as a copy while a paraphrase may not be trusted. The checked-state definition and precondition 1's exclusion of natural-language summaries supply them, although the note never names quotations."
  - scope: passage
    quotes: ["Dropping one costs consumers a recomputation, never correctness"]
    reason: "SUPPLIED — kb/theory/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md — cites the note for 'non-load-bearing validated copies that authorize particular shortcuts rather than replace canonical membership'. The note does not use the phrase 'non-load-bearing', but its graceful-degradation consequence and instance 1 supply the meaning."
  - scope: passage
    quotes: ["A validator re-derives membership across the participating collections and fails a mark whose head does not reach every member in one hop"]
    reason: "DUPLICATED — kb/theory/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md — the note's instance 1 summarizes the complete mark that this dependent develops. For readers who need to use the mark, the dependent's passage is better: it names the shortcut a valid mark authorizes, the fallback membership query, and the limit that this is a conditional control-flow mechanism. The note says itself that the dependent develops this instance."
  - scope: passage
    quotes: ["What flips the regime is the check price"]
    reason: "SUPPLIED — kb/theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md — needs two claims. First, that a lineage database derived from source-side pointers is itself a derived copy that must be checked or absent. Second, that where derivation is mechanical 'the check is free and the regime flips to enforce-or-omit'. The note's regime section supplies both."
  - scope: passage
    quotes: ["The repair follows the regime: re-derive and compare where the content is recoverable from the source, re-examine the support where it exceeds it."]
    reason: "DUPLICATED — kb/theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md — the note restates the derived-artifact / abstracted-rule split, which the dependent states as 'a derived artifact ... is stale until re-derived and compared; an abstracted rule ... is re-opened for support'. The dependent owns the lineage regime and states the split with its interruption-first context, so its statement serves the dependents better. The note's sentence is a summary."
  - scope: passage
    quotes: ["can cause silent, unbounded wrongness when it tells consumers to stop looking"]
    reason: "SUPPLIED — kb/theory/commitment-not-derivation-creates-new-ground-truth.md — needs two things. The first is the asymmetry: absence costs a recomputation, a false copy costs silent, unbounded wrongness. The second is precondition 1, which it reads as the mechanical zone's admission test. With these it argues that the rule does not apply past the commitment boundary. The note supplies both and does not contradict the scope limit."
  - scope: passage
    quotes: ["natural-language summaries and judgments do not — there is no comparison a machine can run, so they stay as live reads or are omitted"]
    reason: "SUPPLIED — kb/theory/design-rationale-must-preserve-unregenerable-decision-premises.md — needs the stricter rule for mechanically derived copies and its exclusion of natural-language explanations that need judgment. The note supplies both. The dependent's further statement, that what stands in for a mechanical check is an open design choice, agrees with the note's managed-staleness section."
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md — needs a safety boundary for exact copies whose source stays authoritative. The note's two-state rule and its degrade-gracefully consequence supply it."
  - scope: passage
    quotes: ["In that regime the hand-maintained dependent artifact is not forbidden; it is unavoidable"]
    reason: "SUPPLIED — kb/theory/files-defer-centralized-schema-commitment-until-invariants-stabilize.md — needs two claims: a retained and trusted recomputable copy must be checked, otherwise it exists only as live or build-time output; and judgment-derived prose instead needs managed staleness. The regime section supplies the second claim and the two-state rule supplies the first. Build-time output appears only through the ADR 025 example."
outcome: report
---

# Role in the KB: A derived copy of recomputable truth must be checked or absent

## Role
The note is a premise that other notes, ADRs and proposals argue from. Most cite it with `rests-on` or `grounds`, to rule out a trusted, hand-maintained copy and to choose between enforcing a copy and removing it. Validation design (ADRs 038, 041, 046 and 068, and the validation contract) uses it as the reason a check is obligatory. Theory notes on quoting, trust marks, lineage and commitment use its asymmetry and precondition 1 to draw the line between mechanical and judgment content. Source ingests cite it as the claim their evidence supports or qualifies. Two tag heads cite it.
Relied on: the two-state rule and the forbidden hand-maintained-and-trusted middle; the false-versus-absent asymmetry; precondition 1 (mechanical derivability, which excludes natural-language summaries); the four preconditions as a set and the Level A classification (ADR 046); precondition 3 (validation contract, citation note); the regime flip at check price and managed staleness for judgment content; "a checkable claim is enforced as a check or not asserted at all"; the degrade-gracefully consequence; the inline-safety third class (context-engineering head); the complete-mark instance. Unused by any visible dependent: precondition 4's regress argument beyond ADR 046's one-line use; the instances of hardcoded contract values, compiled memory views and the duplicated `AGENTS.md.template`; the ADR 025 and 2026-06-10 omission examples as examples; the closing "a cache must never be the only copy" generalization.

## Dependents
38 files link to the note. The supplied inbound contexts show the first 30 by path and cut 8, which fall alphabetically after `kb/theory/files-defer-…`. Several notes that this note links to sort in that range and probably link back: frontloading, fix-what-the-executor, history-has-one-chance, indexes-lower-recall, keep-compiled-views-aligned, link-graph-plus-timestamps, llm-recompute-cost, local-materialization, text-testing-framework, the-boundary-of-automation and `kb/types/tag-readme.md`. Their needs are unseen. The passages of the build-systems and Dagster ingests are cut at 1200 characters.

- `kb/agent-memory-systems/reviews/swamp.md`: citation only.
- `kb/reference/adr/038-…`, `041-…`, `kb/reference/proposals/factored-dependency-pairs-…`: the rule that a gate must be its source document rather than a restatement of it.
- `kb/reference/adr/046-…`: the four preconditions, the forbidden state and Level A.
- `kb/reference/adr/056-…`: the marks doctrine against an unvalidated lifecycle field.
- `kb/reference/adr/068-…`: the rule that decides between removing a copy and enforcing it.
- `kb/reference/proposals/a-reader-facing-banner-…`: the checked-state requirement for a banner derived from frontmatter.
- `kb/reference/proposals/archive/atomic-step-grounding-…`: an inline quote as a checked copy.
- `kb/reference/proposals/archive/source-genre-…`: the absent branch (drop the duplicated field).
- `kb/reference/proposals/archive/tag-scope-…`: enforce-or-omit, extended to scope parameters.
- `kb/reference/proposals/channel-compiled-instruction-artifacts.md`: the constraint on install-time compiled artifacts.
- `kb/reference/proposals/checked-inline-blocks-…`: the exclusion of unchecked inline copies and the oracle boundary.
- `kb/reference/proposals/decisions-bind-…`: a checked back-pointer, and rejection of a hand-maintained index.
- `kb/reference/validation-contract.md`: obligatory referential checks, failing versus warning, and precondition 3.
- `kb/sources/build-systems-a-la-carte-…`, `dagster-…`, `harness-handbook-…`, `prov-overview…`: the claim as the target of evidence or qualification.
- `kb/tags/claims-and-grounding-README.md`, `kb/tags/context-engineering-README.md`: citation and gloss.
- `kb/theory/a-citation-cannot-assert-…`: the asymmetry and precondition 3, for wording checks.
- `kb/theory/a-consumption-channel-…`: trust marks that suppress checks.
- `kb/theory/a-note-is-an-atomic-step-…`: a validated quote versus a paraphrase.
- `kb/theory/an-enforced-tag-readme-…`: validated copies that do not bear load.
- `kb/theory/artifacts-produced-from-sources-…`: a lineage database as a derived copy, and the regime flip.
- `kb/theory/commitment-not-derivation-…`: the asymmetry and precondition 1 as the admission test.
- `kb/theory/design-rationale-must-preserve-…`: the stricter rule for mechanical copies.
- `kb/theory/evidence/seven-documentation-cases-…`: the safety boundary for exact copies.
- `kb/theory/files-defer-centralized-schema-…`: checked or live/build-time output, and managed staleness for prose.

## Duplication
- **Instance 1 and `an-enforced-tag-readme-…`.** The note's complete-mark bullet summarizes what the dependent develops. The dependent's passage is better for use, because it names the shortcut, the fallback and the limit.
- **The regime sentence and `artifacts-produced-from-sources-…`.** The note's "The repair follows the regime" sentence restates the split between derived artifacts and abstracted rules, which the dependent owns and states with its lineage context.
- **Restatements in dependents.** `a-note-is-an-atomic-step-…` and the archived atomic-step-grounding proposal both restate the checked-state definition ("a validator re-derives it and fails on mismatch") almost word for word. `commitment-not-derivation-…` and `a-citation-cannot-assert-…` each restate the asymmetry in one sentence. These restatements apply the note's claim and do not compete with it, and the note's statement is the fuller one.

## Untaken recommendations
None stated explicitly in the visible passages. No inbound passage contains a "recommended next action", "revise" or "add this citation" instruction aimed at this note. Three items are close to recommendations:
- The Dagster ingest says it "qualifies the claim": a production system ships the trusted, hand-declared `code_version` as its default. The note's "forbidden" wording does not address such a counterexample. The passage is cut at 1200 characters, so an explicit recommendation may be in the unseen part.
- The build-systems ingest offers §3.6 as a formal definition of "checked", and the Harness Handbook ingest offers a concrete technical basis. The note cites neither. Neither visible passage asks for a citation, and the build-systems passage is cut.
- The 8 cut files may hold recommendations that this report cannot see.

## Reach
- **The two-state rule and the forbidden middle** ("Such a copy has exactly two valid states"; "no safe middle"): ADRs 038, 041, 046 and 068; the validation contract; the banner, back-pointer, checked-inline-blocks, channel-compiled, factored-dependency, source-genre, tag-scope and atomic-step-grounding proposals; seven-documentation-cases; files-defer; both tag heads; swamp.
- **The false-versus-absent asymmetry:** validation-contract (fail versus warn), a-citation-cannot-assert, commitment-not-derivation, a-consumption-channel, ADR 068 (through the link to indexes-lower-recall).
- **Precondition 1** (mechanical derivation; natural-language content excluded and kept as a live read): a-note-is-an-atomic-step, design-rationale, commitment-not-derivation, and ADRs 038, 041 and factored-dependency-pairs, which rely on its live-read clause for prose restatements. Changing that clause, or reconciling it with the regime section's allowance for hand-maintained judgment dependents, would reach those three.
- **Precondition 3:** validation-contract (which uses it in another sense) and a-citation-cannot-assert.
- **The four preconditions as a set, and Level A:** ADR 046.
- **The regime section** (managed staleness, the check-price flip, the derived/abstracted repair split): artifacts-produced-from-sources, files-defer.
- **"A checkable claim is enforced as a check or not asserted at all" and the status-field open question:** ADR 056, the tag-scope proposal, a-consumption-channel.
- **The degrade-gracefully consequence:** an-enforced-tag-readme, seven-documentation-cases.
- **The "What enforcement buys" third class:** the context-engineering tag head. The cut frontloading and fix-what-the-executor notes may also use it.
- **Instance 1 (the complete mark):** an-enforced-tag-readme. `kb/types/tag-readme.md` is probably among the cut files.
- **The title and the term "checked":** every dependent, and the source ingests that bear on the claim (build-systems, Dagster, Harness Handbook).
- **Reaches no visible dependent:** precondition 4's regress argument beyond ADR 046's mention; the instances of hardcoded contract values, compiled memory views and the `AGENTS.md.template` duplication; the closing cache generalization. The 8 cut files may rely on some of these.
