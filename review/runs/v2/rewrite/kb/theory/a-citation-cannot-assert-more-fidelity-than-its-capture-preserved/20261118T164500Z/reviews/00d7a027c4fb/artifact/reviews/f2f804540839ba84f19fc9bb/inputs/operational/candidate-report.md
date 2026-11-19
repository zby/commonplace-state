# Reconciliation report

## Kept

- **Title claim (capture bounds citation fidelity).** Kept as the central claim (claim account 3, 10). `kb-role` lists it as relied on.
- **Marking a span as an exact quotation asserts that these words occur in the source.** Kept as "A direct quotation asserts that the quoted words are the source's own" (claim account 3; S2 Context ¶1).
- **Markers that never claimed exact wording, such as a paraphrase, give the check nothing to match.** Kept as "A paraphrase makes no wording claim, so a wording check has nothing to match". `kb-role` lists it as relied on; it follows from claim account 2 and 9.
- **A paraphrase needs a judgment of support rather than a wording check** (old "Context needs a reader of both texts"; old paraphrase-of-paraphrase passage). Kept as "checking it means judging whether the source supports it". `kb-role` lists it as relied on (claim account 2, 4).
- **A string check answers only the wording question; attribution, context and truth stay unverified.** Kept in compressed form: a pass does not certify the original author's words, meaning in context, or truth (claim account 8, as inference I3). The four-question enumeration itself is replaced (see below).
- **A pass means "agrees with the evidence this check used".** Kept as "The pass is relative to that evidence" (claim account 8). `kb-role` lists it as relied on.
- **Missing bytes report as unverified, never as passed; a silent fallback would make the result depend on ambient copies.** Kept, stated generally (claim account 7). `kb-role` lists it as relied on.
- **Failing a quote on mismatch is a choice within the cost/risk trade-off, not a universal rule.** Kept in `## Scope`, with the link to the trade-off note. The claim account does not list this commitment, but `kb-role` lists it as relied on and the commission does not ask to drop it. The candidate keeps it only as a scope limit (the bound does not decide enforcement), which is consistent with claim account 6 (the limit is evidential) and adds no new commitment beyond the existing note. Flagged here for the reviewer.
- **"Exact" means a match under the check's normalization rule, not identity.** Kept only as "a match under its comparison rule" / "under its normalization rule" (claim account 8, S2 internal tension). The normalization detail is omitted (see below).
- **Exactness and second-hand provenance are independent; paraphrase hops can change the proposition.** Partly kept: "Rewording can also change the proposition, and the result is an interpretation, not source text" (claim account 2, S1 Context ¶1–2). The chain-of-exact-checks part is omitted.
- **Scope: transfer beyond agent-operated KBs rests on reasoning, not external evidence.** Kept as the first Scope bullet, now naming the ADRs as origin (claim account 10).
- **Frontmatter `title`, `type`, tags and H1.** Kept unchanged. No `user-verified` field was present.

## Replaced

- **Description.** The old description presented the note as a general account of quote checking (wording, occurrence and source-identity checks). Replaced with one describing the commissioned contribution: deciding whether retained material supports a citation. `kb-role` notes the old description misrepresented how dependents use the note.
- **Opening paragraph (quote check as a test of one relation over span, source text and normalization rule).** Replaced by the constructed paraphrase-versus-quotation example and the principle it shows, as the commission's current direction requires (claim account 1–3).
- **"Four questions, one answered mechanically" enumeration.** Replaced by the single sentence on what a pass does not certify (claim account 8). `kb-role` lists the enumeration as unused; the commission asks for brevity and excludes surveying checking techniques.
- **ADR 046 as evidence for normalization judgements.** Replaced by one illustrative sentence on Commonplace's checker and `abstracted-from` footer links (claim account 9; collection contract "Origin is not corroboration").
- **Old Scope bullets.** Replaced by bullets for origin and transfer, the open boundary between bounded and broad, distributed or contextual uses (claim account 4, 10), and the enforcement-choice limit.

## Omitted

- **Wording agreement is deterministic, cheap and binary; judging support is costlier, noisier and its reliability unmeasured.** Omitted: not in the claim account; checking-cost reasoning lives in the linked trade-off note; the commission asks for brevity.
- **Later readers can reuse the check's result, accepting change risk.** Omitted: not in the claim account; belongs to the trade-off note.
- **Normalization rule errs in both directions; ADR 046's judgement on false mismatches; casebook mismatch kinds; typography and emphasis can affect meaning.** Omitted: teaching the validator and arguing from corpus evidence are excluded by the commission. `kb-role` lists the section as unused.
- **Occurrence is not location; uniqueness, checked ranges and the no-concatenation rule (ADR 094); untested locators are not evidence.** Omitted: validator mechanism, excluded by the commission; ADR 094 is not an authorized source. `kb-role` lists these as unused.
- **Source identity by checksum and name pairing; a pin detects change only at the next check; changed context with surviving words is missed.** Omitted: storage and validator mechanism, excluded by the commission and the claim account (do not rely on S1's mechanism details). `kb-role` lists these as unused.
- **Retained, accessible and used material differ (capture on another machine, text in a model's context).** Omitted as a separate point; its consequence (missing evidence is not a pass, no ambient fallback) is kept. The claim account forbids explaining the storage layers behind availability.
- **Multi-read context retrieval for sources exceeding a model's context budget.** Omitted: not in the claim account; `kb-role` lists it as unused.
- **Chained exact checks verify only their own pair; checking against verified source extracts avoids paraphrase-of-paraphrase.** Omitted: not in the claim account beyond the kept point that rewording can change the proposition; `kb-role` lists it as unused.
- **Scope: audio, images, oral quotation and lost originals out of scope.** Omitted: not in the claim account.
- **Scope: marked editorial alterations fail a strict wording assertion; segment-wise checking open.** Omitted: validator detail, excluded by the commission.
- **Scope: the extractor's unrecognized quotations and the "unresolved" outcome.** Omitted: the claim account forbids describing the `unresolved` rule or extraction heuristic.
