# Reconciliation report

The candidate replaces the old categorical argument with the commissioned cost–risk trade-off. It follows the approved shape: first the reuse benefit and the trade-off, then the completeness mark contrasted with the connect report, then the "no known change" conclusion, the compact numbered conditions and `## Scope`. The frontmatter `title`, `type` and traits are unchanged, and so is the H1. The note had no `brief` declaration and no `user-verified` field. The description was rewritten and is about 205 characters, under the 250 limit.

## Kept

- **The false-copy suppression mechanism** (old §"The asymmetry that forces the rule", first paragraph). It is kept as a conditional mechanism and linked inline to the indexes note: a consumer that stops on a copy it treats as exhaustive suppresses the search that would expose the copy's error. The candidate states both conditions, that the consumer actually stops and that the suppressed search would find more, so it does not call every error catastrophic. Reason: commission Must keep, claim account §4.
- **The four numbered preconditions, renamed "conditions", with numbering and recognizable concepts kept.** These are 1 derivation/comparison rule, 2 locatability, 3 ground truth available at check time, and 4 a trustworthy checker. Dependents cite them by number. Condition 1 is broadened from "derivation rule" to "derivation or comparison rule applied without judgment". Condition 2 drops the "marked region" and "human visibility not required" detail. Condition 4 shrinks to one sentence: testing or centralizing lowers the cost of assurance but does not prove correctness. Reason: commission Must keep, claim account §10.
- **The `complete` mark as the main instance** (old Instances, first bullet). It is now the first developed example and links to the actual contract. Reason: commission shape.
- **The distinction between mechanical checking and semantic review.** The old note had it implicitly in condition 1 and the managed-staleness section. The candidate keeps it through the mark's tag-fit point and the connect report's judgment versus its checkable properties. Reason: claim account §9.
- **The value side of retaining a copy** (old footer link to the LLM recompute-cost note, and the frontloading link). It is now the opening reuse and amortization premise. Reason: claim account §1.
- **Footer links that give navigation not supplied inline:** the LLM recompute-cost note, the enforced tag-README MOC note, and the history-has-one-chance note. The last one's label was re-scoped to condition 3. The tags are kept.

## Replaced

- **"Exactly two valid states (checked or absent); no safe middle"** (old opening paragraph). It is replaced by the claim that checking frequency depends on check cost relative to the risk of reliance, with accepted risk made an explicit choice. The commission's current direction explicitly authorizes dropping this rule and the forbidden middle. `kb-role` lists both as relied on.
- **The false-versus-absent asymmetry as a categorical justification** ("bounded vs silent, unbounded"; "forbidden rather than merely risky"; "one missed edit away from the catastrophic state"). It is replaced by the conditional suppression mechanism, which serves as the risk side of the trade-off. This is authorized by the commission. The asymmetry is listed as relied on.
- **The regime flip at check price and enforce-or-omit as "the rule"** (old §"Where the rule applies"). It is replaced by the statement that an inexpensive, defined check on a stop-authorizing claim makes enforcement attractive, together with the general point about how check cost relates to the saving. That point covers full recomputation largely defeating the saving, and the case where verification is cheaper than derivation. This is authorized by the commission. The regime flip and the Level A classification (ADR 046) are listed as relied on.
- **Managed staleness for judgment content** (old §"Where the rule applies", first paragraph). It is replaced by the connect-report example. That example presents reuse of a judgment-produced result as a risk choice: its dependencies are broad, a sufficient dependency set is hard to track, and some properties stay mechanically checkable. The lineage, make-like staleness and holistic-rewrite links were cut because the candidate no longer argues for that regime. This is authorized by the commission. It is listed as relied on.
- **"Validator expected to bottom out, not recurse", with its amortization-across-copies argument** (old condition 4). It is replaced by one sentence that keeps validator cost separate from computation amortization (claim account §11). The claim that the mark meets condition 4 is withdrawn: the candidate says nothing in the mark's contract establishes it.
- **"Ground truth exists at validation time" with the plan-executor illustration** (old condition 3). It is reduced to the bare condition. The executor illustration is not in the claim account.
- **Assurance from the mark's validator** (old Instances: "enforced and shipped"). It is replaced by reactive enforcement: the mark can be false between validations, and its assurance covers reach given the tags. A new section adds that the absence of a known change does not establish freshness.

## Omitted

- **"Checked copies degrade gracefully; dropping one costs a recomputation, never correctness."** This is excluded by the commission, which drops guaranteed graceful degradation, and by claim account "No guaranteed outcomes". It is listed as relied on, and its omission is authorized.
- **"Never write the unenforced natural-language version of a checkable claim … enforced as a check or not asserted at all."** This is excluded as a universal enforce-or-omit slogan. It is listed as relied on, and its omission is authorized.
- **"When a copy can't be checked, the resolution is omission",** with the ADR 025 and 2026-06-10 `kb/log.md` examples. This is excluded: there is no automatic omission of judgment-based material, and ADRs are not used as authority. `kb-role` lists the examples as unused.
- **Condition 1's exclusion that natural-language summaries and judgments "do not qualify … stay as live reads or are omitted."** This is excluded as a blanket statement about judgment-produced results. It is listed as relied on, in its mechanical/judgment boundary use. The candidate keeps the boundary in a narrower form: rules applied without judgment, and checkable properties distinguished from the judgment they do not reconstruct.
- **The "recomputable-and-checked" third class between arbitrary and situational** (old §"What enforcement buys"), with the fix-what-the-executor-can't-determine link. It is not in the claim account. The context-engineering tag head relies on it. The commission's direction narrows the categorical apparatus, and this class presents enforcement as the general resolution. Flagged for dependent correction below.
- **The compiled memory views, hardcoded hot-path contract values and duplicated `AGENTS.md.template` instances, and the ADR 027 link.** The commission excludes them, and `kb-role` lists them as unused.
- **The closing "a cache must never be the only copy" generalization.** The commission excludes it as the cache maxim, and it is listed as unused.
- **The old Open Questions** (the `status:` trust mark, the cheapest mechanism for checkable frontloaded regions). The commission excludes unrelated open questions. They are replaced by the two gaps the claim account names.
- **Footer links duplicated inline or tied to retired claims:** the indexes note, frontloading, and the tag-readme spec are all inline now. The others were the boundary-of-automation note ("omission is the only safe state"), the fix-what-the-executor note, the keep-compiled-views note, the lineage note, the make-like staleness note, the text-testing-framework note, the ADR 027 link and the local-materialization note. The commission asks for duplicative footer links to be cut. The rest carried labels for the retired rule, the Level A flip or excluded examples.

## Dependent corrections needed (not made)

The role report inspected only 30 of the 38 files that link to this note, so this is not a complete dependency audit. Classes of dependent rationale that would need correction:

- **Arguments that a check is obligatory, or that a copy must be enforced or removed.** These cite the two-state rule, the forbidden middle, "enforced as a check or not asserted" or enforce-or-omit. Examples are ADRs 038, 041 and 068 and the validation contract. They should be restated as a choice that weighs check cost against reliance risk.
- **The Level A classification and regime flip** (ADR 046). The candidate no longer supplies a check-price threshold at which enforcement becomes mandatory.
- **Uses of the asymmetry or of condition 1 to draw a hard mechanical/judgment line.** These include the theory notes on quoting, trust marks, lineage and commitment. The candidate keeps the distinction but not the claim that judgment content must be omitted or left unchecked.
- **The graceful-degradation and "never correctness" guarantee.** `kb/types/tag-readme.md` §Frontmatter calls this note the "safety half" with "enforced-or-omitted" and "never correctness". The candidate supports the mark as an attractive, reactively enforced case, not as a law.
- **The broader-rule citation in `kb/theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md` §Defenses.** The rule it cites is now a trade-off.
- **The third-class framing in the context-engineering tag head,** and source ingests that cite the old categorical claim as what their evidence supports or qualifies.

## Title

Keeping the title and H1 is a transition constraint. Their universal wording is no longer supported by the body. Proposed replacement title: **"How often to check a retained derived result depends on check cost relative to the risk of relying on it"**. Retitling and publication need the user's separate approval.

## Length

Counted by hand sentence by sentence, because no counting command was run. The body from the opening paragraph through `## Open Questions` is about 827 words including headings, and about 790 words of prose without them. Frontmatter and the footer are excluded. This is within the 850 ceiling and slightly above the 600–800 target once headings are included.
