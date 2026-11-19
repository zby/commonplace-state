# Assessment: A citation cannot assert more fidelity than its capture preserved

**Proposed purpose (no operator purpose given):** KB maintainers who design capture, citation and grounding rules (ADR 046's markers, span locators, ingest practice) should see what fidelity bound a captured source sets on a citation, why notation cannot raise it, and when they must act at capture time rather than later.

**Decision: stop. No pass is recommended.** All three depth 1 reports propose changing what the note claims, not how it says it. Several of the changes reach claims that dependents rely on. The passes do not change claims, and text that a rewrite will replace is not worth a pass.

## Why the run stops

1. **The central claim's temporal framing is proposed for restatement.** The critique (`kb/reports/state/review/results/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md/kb/instructions/critique-note.md`, attack outcome "partially lands") proposes restating the bound as "a citation's fidelity is bounded by the most faithful retained artifact it can be checked against", with "fixed at ingest" kept only as the special case in which the authoritative artifact is not retained. The premise decomposition (`.../kb/instructions/premise-decomposition-gate.md`) agrees: "re-capture" absorbs every operation that consults the source, so "only re-capture raises fidelity" is close to definitional, and "provenance quality is decided before any note is written" fails whenever the authoritative artifact is retained. The underspecified-assertions finding makes the same point: the reading of "re-capture" decides whether "no review gate can promote a passage" is true.
2. **The forcing argument is reported as unsupported or defeated.** All three depth 1 reports find that "The layering is not a design choice" reverses the direction of the rival-test note it cites: that note says finding no rival certifies nothing. The premise decomposition marks "a long source cannot be captured verbatim … because the consumer's context window is finite and because copyright forces trims" as DEFEATED: a full-text local snapshot is a verbatim capture that a finite-context reader loads in windows, and copyright does not force trims on openly licensed sources or private copies. The critique names this design as a boundary-preserving rival. Fixing this means narrowing "forced" to the LLM-facing snapshot or presenting the rival. That changes a section heading's claim and the description.
3. **The locator corollary is proposed for replacement.** The critique proposes "the layer must be resolvable from the locator, either derived from a layer-marked snapshot or encoded and validated" in place of "Any locator design must encode the layer", and calls the same-offset example impossible. The friction gate, framing-mismatch, conceptual-role-conflation and underspecified-assertions findings agree: within one snapshot, two spans at one offset are one passage.
4. **The second-hand layer is not produced by the stated mechanism.** The friction gate, completeness-boundary-cases and framework-decoration findings show that second-hand status is a property of the source chain, can coexist with verbatim capture, and survives on short sources. The proposed fix (two axes, or second-hand as a qualifier on the other layers) changes the three-layer taxonomy.
5. **The evidence paragraph supports less than it claims.** ADR 046's eighteen mismatches were mostly editorial edits inside genuine quotations, not paraphrase passages marked verbatim, and the ADR reports a prototype run rather than the shipped checker. The evidence supports "verbatim marks need a mechanical check", not the layering.

Items 1, 2 and 4 are claim changes. Item 1 in particular may show that a claim is wrong as stated, so the rewrite route applies: `commonplace-review run rewrite kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md --commission FILE`, with the commission prepared with `cp-skill-write-multistage`.

## Dependents the operator must weigh

From the role report (`kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/role`):

- `kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md` takes its marker names from the three-layer vocabulary and defers to the note for why non-verbatim markers stay unchecked. Restructuring the second-hand layer (item 4) reaches it.
- `kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md` uses the capture-time bound and "re-capture as the only remedy" as a premise. Restating the bound relative to retained ground truth (item 1) reaches it.
- `kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md` relies on the paraphrase layer being weak evidence (read as "unverifiable") and on promotion at capture. Item 1 reaches it.
- `kb/sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md` relies on a broad reading of the title. Any narrowing of the title reaches it.
- `kb/tags/claims-and-grounding-README.md` repeats the title claim in its gloss.

The forced-layering argument, the locator corollary, the Scope section, the history-note link and the evidence paragraph reach no dependent. Rewriting them affects only this note.

I found no sign that the contradictions come from a term a dependent uses in another sense. The Peters ingest reads the note more strongly ("unverifiable" for "not mechanically checkable"), and the ROME ingest reads the title as a claim-strength rule rather than a provenance-grade rule. Both are dependents' overreadings, not the cause of the reported problems.

## Ranked changes against the purpose (for the rewrite, not for passes)

1. Settle what "re-capture" covers and restate the bound relative to the retained authoritative artifact; keep "fixed at ingest" for the unretained case. Cost: rewrite of the opening and the Scope section's practical paragraph, plus dependent checks. Route: rewrite.
2. Narrow "forced" to the LLM-facing snapshot, or present the full-text snapshot as the rival; stop citing the rival test as certifying inheritance. Cost: rewrite of one section's opening and the description. Route: rewrite.
3. Restate the locator corollary as "the layer must be resolvable from the locator". Cost: one paragraph. Route: rewrite.
4. Treat second-hand as a source-chain qualifier on the capture layers, or justify it as a third layer. Cost: the layer list and ADR 046 coordination. Route: rewrite, with operator decision on ADR 046.
5. Describe ADR 046's mismatches accurately (editorial quoting edits, prototype run, 6 unresolved) and narrow the evidence claim. Cost: one footer sentence. Route: a stale qualification for the operator (below), or the rewrite.
6. After the rewrite: readability-and-flow for the Scope section's wrappers and the forced-layering paragraph order (compression synthesis), plain-wording for "earns its keep", "earns its boundaries", "bites", and the stock phrase "the reason is exact rather than merely practical". Cost: small. Route: passes on the rewritten text.

**Sentence a hostile reviewer would attack first:** "The layering is not a design choice — [a framework rule with a boundary-preserving rival is not an inherited constraint](…), and no rival capture design drops the layering while preserving the commitments the framework has already made." It reverses its cited note's logic, it is ambiguous to parse, and a rival (full-text snapshot kept for verification) exists.

**What reads well:** the "Why notation cannot repair it" mechanism — a paraphrase has no mechanical derivation rule back to its source, so a `verbatim` mark cannot make it verbatim — is clear, survives the premise hunt, and is what ADR 046 and the atomic-step note rely on.

## Overclaims: support or divergence

- "Fidelity is fixed at ingest and is non-increasing downstream … The only operation that raises fidelity is re-capture." — **divergence** (the note's central claim; dependents rely on it). Keep its substance; the operator decides through the rewrite whether to restate it relative to the retained artifact.
- "no citation syntax, no locator type, no review gate can promote a passage to a grade its capture did not preserve" — **divergence** for syntax and locators; the "review gate" clause is **support** and may be narrowed (a gate that consults the authoritative artifact is arguably re-capture).
- "A paraphrase-layer passage has no such rule — there is no mechanical comparison between a paraphrase and its source, only judgment." — **divergence** (survived the premise hunt; ADR 046, the atomic-step note and the Peters ingest rely on it).
- "The layering is not a design choice" / "Capture is layered because it is forced to be" / "Any framework whose consumer is an LLM and whose sources are real documents faces both" — **support**; may be narrowed. No dependent uses it.
- "This is the citation-fidelity instance of a general rule" and "what was not preserved verbatim then is permanently downgraded" — **support**; may be narrowed to analogy or to the unretained case.
- "it produces precisely the hand-maintained-and-trusted copy that rule forbids" — **support**; may be narrowed for the post-ADR 046 regime.
- "Any locator design must encode the layer." — **support**; may be narrowed to "resolvable from the locator".
- "The claim bites exactly where capture is lossy, which is to say wherever the sources are long." — **support**; may be narrowed (lossy ≠ long; second-hand is length-independent).
- "Evidence for the layering and for the failure of naive `verbatim` marking" — **support**; should be narrowed to what ADR 046 shows.

## Stale qualifications (claim questions for the operator, not passes)

- The evidence paragraph calls the run "the shipped verbatim-quote checker"; ADR 046 reports a prototype run with 63 match, 18 mismatch and 6 unresolved, and attributes the mismatches mainly to ellipsis, bracketed substitution, case and punctuation edits.
- "it produces precisely the hand-maintained-and-trusted copy that rule forbids" describes the state before ADR 046; since ADR 046 a paraphrase marked `verbatim` fails validation.
- The paraphrase-layer bullet defines the authoritative artifact as "(the sibling PDF)", the casebook corpus's storage convention, inside a general definition.
- The Scope section says short sources make "the layers collapse to one"; the second-hand layer does not collapse with length.
- "epistack casebook work in the sibling `epistack-casebooks` repository" is cited as evidence but is neither identified nor linked.

## Findings not acted on

None is planned, because the run stops. Each is listed once with its reason.

- `accessibility/undefined-terms` (gloss "inherited constraint" / "boundary-preserving rival") — the sentence using these terms is to be rewritten (item 2).
- `accessibility/unidentified-references` (identify epistack casebooks) — the evidence paragraph is to be rewritten (item 5); listed as a stale qualification.
- `complexity/connection-inflation` (five bare footer entries) — footer links depend on which inline links survive the rewrite (history-note and rival-test links may go or change).
- `complexity/framework-decoration` (second-hand layer unused) — a claim change (item 4).
- `kb/instructions/compression-bundle/marginal-value-redundancy` (Scope opener and closer) — the Scope section is to be rewritten (items 1 and the length/lossy narrowing).
- `prose/mannered-prose` ("earns its keep", "earns its boundaries") — both sit in the Scope section the rewrite replaces.
- `prose/orphan-references` (ADR 046 composition omitted) — a claim/evidence question (item 5).
- `prose/source-residue` ("the sibling PDF") — a stale qualification; the bullet may change with item 4.
- `semantic/completeness-boundary-cases` (second-hand as a second axis) — a claim change (item 4).
- `semantic/conceptual-role-conflation` (layer as region vs grade in the corollary) — a claim change (item 3).
- `semantic/epistemic-status-blur` (evidence spread; unreported rival search) — claim changes (items 2 and 5).
- `semantic/grounding-alignment` (rival-test direction; history-note instance) — claim changes (item 2, and the history-note link).
- `semantic/underspecified-assertions` (scope of "re-capture"; which file's offset) — claim changes (items 1 and 3).
- `semantic/unwarranted-scope` (forced for all LLM frameworks) — a claim change (item 2).
- `sentence/clause-packing` (rival-test sentence; evidence sentence) — both sentences are to be rewritten.
- `sentence/concept-attribution` (rival test; history note) — claim changes (item 2 and the history-note link).
- `sentence/framing-mismatch` (same-offset collision; lossy = long) — claim changes (items 3 and the Scope narrowing).
- `sentence/misleading-link-text` (rival-test link) — the sentence is to be rewritten (item 2).
- `sentence/parsing-ambiguity` (title-as-clause after the dash) — the sentence is to be rewritten (item 2).
- `sentence/stock-phrases` ("the reason is exact rather than merely practical"; Scope opener) — the first may survive the rewrite and is a candidate for a later plain-wording pass; the second sits in the Scope section the rewrite replaces.
