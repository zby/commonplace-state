# Reconciliation report

The candidate replaces the old note's categorical argument with the commissioned cost–risk trade-off. It keeps the existing `title`, `type`, `traits`, `tags` and H1. The `description` is rewritten because the old one stated the forbidden-middle rule that the commission replaces. The old note carried no `user-verified` field, and the candidate adds none.

Body length, counted by hand per sentence: about 837 words from the first paragraph through `## Scope`, headings included, or about 808 without headings. The footer is not counted. This is above the 600–800 target and under the 850 ceiling. I did a sentence-level redundancy pass: I cut restated surface lists, a repeated "not whether the copy may be kept" framing, and a duplicated amortization clause. I also cut the Scope bullet on the conditional suppression mechanism, because the second paragraph already states that condition next to the claim.

## Kept

- **A false trusted copy suppresses the work that would expose its error** (old "asymmetry" section, the link to *indexes lower recall…*). Kept as a conditional mechanism. It applies when a consumer treats the copy as licence to stop and the suppressed route would actually find more. It no longer says the harm is unbounded or catastrophic.
- **The complete mark on tag-READMEs as the enforced instance.** Kept and developed as the first example. It covers the licensed skip of the `rg` sweep, the one-hop rule over participating collections, the mechanical check, and reactive enforcement. It adds that the mark can be false between a tagging change and the next validation, and that the check covers declared tags only. The link to the actual contract (`../types/tag-readme.md`) is kept at the example.
- **The four preconditions, with numbering and concepts preserved** (old "What 'checked' requires"). They are kept as the four conditions for a *mechanical* check: (1) derivation or comparison rule, (2) locatable copy and source via lineage, (3) source available at check time, (4) sufficiently trustworthy checker. They now decide whether checking is available and how cheap it is. They no longer decide whether a copy may exist. Precondition 1's exclusion of judgment-based results is kept as "a result produced by judgment has no such rule."
- **Mechanical versus judgment-based checking** (old precondition 1 and the managed-staleness paragraph). Kept as the commissioned definition of a mechanical check: it derives the result from identified, available inputs or compares the copy against them. It is set against semantic review, using the connect-report contrast.
- **The frontloading link as the value side.** Kept and recast as the amortization premise: one computation serves many uses. The candidate adds the commissioned inference that full recomputation on every use largely defeats that saving.
- **Footer links kept:** *indexes lower recall…* (grounds), *frontloading spares execution context* (grounds; context phrase rewritten), *LLM recompute cost inverts…* (grounds), *the boundary of automation is the boundary of verification* (grounds; the phrase no longer says "omission is the only safe state"), the tag-readme type spec (evidenced-by; the phrase now says it is the origin and a bound, not corroboration), *an enforced tag-README is a MOC…* (extends), *history has one chance to become checkable* (contrasts; reattached to condition 3).

## Replaced

- **The two-state rule: "exactly two valid states", checked or absent, "no safe middle", "hand-maintained-and-trusted is forbidden".** Replaced by the qualitative trade-off: how often to check depends on checking cost relative to the risk of relying on the result unchecked. The candidate states that this is not a rule about which copies may exist. Authorized by the commission's current direction.
- **The false-versus-absent asymmetry as grounds for prohibition** ("bounded, recoverable downside" versus "silent, unbounded" wrongness; "forbidden rather than merely risky"). Replaced by the conditional suppression mechanism on the risk side of the trade-off. The fallback's protection is narrowed: dropping the mark costs one `rg` sweep, but that protects only readers who fall back. It does not protect readers who trust a stale mark.
- **The regime flip at check price** (Level A versus Level B; "enforce-or-omit stops being aspirational and becomes the rule"; "detection and verification collapse into one free step"; "the interrupt-placement problem dissolves"). Replaced by this: a cheap, exact mechanical check makes enforcement attractive where it is inexpensive. Checking is no longer described as free. The "Level A" label is not used, but the concept of a deterministic mechanical check remains. Authorized by the current direction (enforce-or-omit regime flip).
- **Precondition 4's regress argument** ("expected to bottom out, not recurse"; a centralized, versioned, reviewed validator amortized across copies has lower unit cost of correctness-assurance). Replaced by the commissioned C9: testing or centralizing a validator lowers assurance cost but does not prove it correct. The candidate keeps validator-development amortization across artifacts separate from computation amortization across uses.
- **"Checked copies degrade gracefully … never correctness."** Replaced by the narrowed statement in the mark example (see the asymmetry entry above). Authorized (guaranteed graceful degradation).
- **Description.** Rewritten to describe the trade-off and the two examples. The old description stated the forbidden rule.
- **Footer label for *source changes should surface downstream review targets…*:** changed from `extends` to `contrasts`. The candidate no longer specializes a managed-staleness rule. It contrasts mechanical checking with review-based lineage.

## Omitted

- **Managed staleness for judgment-dependent knowledge**: the lineage, make-like timestamp and holistic-rework machinery, Level B checks, and the "hand-maintained dependent artifact is unavoidable" passage. Omitted because it was part of the regime-flip argument, which is authorized for removal. It is also outside the commissioned shape. The connect report now carries the judgment-based contrast.
- **"What enforcement buys": recomputable-and-checked as a third class between arbitrary and situational**, which reconciled frontloading with *fix what the executor can't determine*. Omitted. It is not in the claim account, and its core claim, that a checked copy is safe to pin, is a form of the checked-or-absent safety dichotomy that the commission excludes. kb-role lists it as relied on by the context-engineering tag head; see the dependents below.
- **Precondition 2's addendum** ("machine-followable suffices; human visibility is not required once the validator carries the interrupt"). Omitted as part of the interrupt-placement argument. The claim account does not give it.
- **Precondition 3's executor clause** (execution itself produces the evidence, so "that territory stays with the executor"). Omitted because the claim account gives condition 3 only as source availability at check time. The concept stays recognizable, and the footer link to *history has one chance to become checkable* keeps the no-later-source contrast.
- **Precondition 4's "judgment-call derivation rule is the forbidden state relocated one layer down."** Omitted because it depends on the forbidden-state framing.
- **"Never write the unenforced natural-language version of a checkable claim … enforced as a check or not asserted at all."** Omitted as the enforce-or-omit slogan the commission excludes.
- **"When a copy can't be checked, the resolution is omission"**, with the ADR 025 and 2026-06-10 log examples. Omitted. The commission authorizes dropping automatic omission and excludes ADRs as authority.
- **Instances: compiled memory views and cues, hardcoded contract values in hot-path skills, duplicated `AGENTS.md.template` files (ADR 027).** Omitted as the commission directs. Also omitted: the "four surfaces in four states" generalization argument.
- **"A cache must never be the only copy" generalization.** Omitted as the commission directs.
- **Open questions** (the `status:` field as an unvalidated trust mark; the cheapest mechanism for checkable frontloaded regions). Omitted as unrelated to the new argument.
- **Footer links dropped:** *fix what the executor can't determine* (third-class argument omitted), *keep compiled views aligned* (instance omitted), *link graph plus timestamps* (managed-staleness contrast omitted), *text testing framework* (Level A/B regime flip omitted), ADR 027 (instance omitted; ADRs not used as authority), *local materialization should outperform distant declarations* (its context phrase cited the checked-or-absent boundary, which no longer exists here). Added: the connect-report type spec, as the second example.

## Other notes on the claim account

- C2's distinction between context-loading cost and verification cost is not in the candidate. I removed it during the redundancy pass because no reader-relevant consequence followed from it in this compact form. The verification-versus-recomputation distinction stays as one sentence.
- C4's "attractive where inexpensive, not obligatory everywhere" is carried by "which makes enforcement attractive" together with the opening's statement that the note is not a rule about which copies may exist.

## Dependents needing correction (not edited)

Limitation: according to the commission, the role report inspected only 30 of the 38 files that link to this note. I did not audit dependents myself. The list below is not a complete dependency audit.

Classes of dependent rationale that the candidate no longer supports:

1. **The checked-or-absent / forbidden-middle rule**, cited with `rests-on` or `grounds` to rule out trusted hand-maintained copies. Per kb-role this includes validation-design ADRs (038, 041, 046, 068) and the validation contract, where this note is the reason a check is obligatory. Those dependents now need their own cost–risk justification for each check.
2. **The enforce-or-omit regime flip and "a checkable claim is enforced as a check or not asserted at all."** This covers the specific `kb/types/tag-readme.md` passage that calls a mark "recomputable, therefore never load-bearing" and "enforced-or-omitted" and calls this note the "safety half". It also covers the "the broader rule" cross-reference in `indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md`.
3. **Guaranteed graceful degradation** ("costs a recomputation, never correctness"). This now holds only for consumers that fall back. It does not hold for consumers that trust a stale mark.
4. **Automatic omission of judgment-based material**, and the false-versus-absent asymmetry as a prohibition. Per kb-role, theory notes on quoting, trust marks, lineage and commitment use the asymmetry and precondition 1 to draw the mechanical/judgment line. Precondition 1 still draws that line for *mechanical checkability*, but it no longer implies omission.
5. **The inline-safety third class** (recomputable-and-checked), cited by the context-engineering tag head.
6. **ADR 046's use of the four preconditions and the Level A classification.** The numbering and concepts are kept. The "Level A" label and the regress argument for precondition 4 are not.
7. **`local-materialization-should-outperform-distant-declarations.md`**, which says it keeps "this note's checked-or-absent boundary".
8. **Source ingests and two tag heads** that cite the note as the claim their evidence supports or qualifies. They need to be rechecked against the trade-off claim.

## Proposed replacement title (operator decision)

"How often to check a retained derived result depends on checking cost relative to reliance risk"

The current title and H1 are kept as a transition constraint, even though the body no longer supports their universal wording. Publication and any retitle need the user's separate approval.
