---
description: "Deciding whether retained material supports a citation: a paraphrase cannot be cited as a quotation, a passed wording check shows only a match against the text compared, and a citation that claims more than was retained must be narrowed or checked against the source"
type: types/note.md
tags: [document-system, claims-and-grounding, kb-maintenance]
---

# A citation cannot assert more fidelity than its capture preserved

A writer reads a paper and keeps a note: the authors found that the method breaks down on long inputs. Weeks later, drafting an argument, the writer wants to write that the authors report the method "breaks down on long inputs". The quotation marks say these are the authors' words. The note cannot back that. It records what the writer took the passage to say, in the writer's words. The paper may have said that accuracy degrades on inputs longer than those seen in training, which is a narrower claim. A second writer who kept that sentence word for word can quote it.

A paraphrase can preserve an idea without preserving the author's words; rewording is what makes it a paraphrase. Rewording can also change the proposition, and the result is an interpretation, not source text. A direct quotation asserts that the quoted words are the source's own. If the capture, meaning what the writer retained, holds only a paraphrase, it contains no source words for the quotation marks to point to. Adding the marks claims fidelity the capture did not preserve, and no notation added later can recover words that were never kept. The same bound holds for any fidelity a citation claims, whether exact words, the idea, or the passage's place in its context. It matters because a reader who trusts the claimed fidelity may skip comparing the citation with the source and so miss the error.

The limit is on what a citation asserts about its evidence, not on what the writer may claim: the claim can still be made at the fidelity the capture supports, or as the writer's own.

## When the capture is enough

A bounded exact passage can be enough to judge some uses of a source, when the quoted words carry what the citing text relies on. Other uses depend on broad, distributed or contextual material, such as an overall argument, a pattern across sections or what surrounds the passage. A few retained passages cannot represent that material soundly; those uses need the full source.

The kind of check follows the kind of fidelity claimed. An exact-wording claim can be tested by matching words. A paraphrase makes no wording claim, so a wording check has nothing to match; checking it means judging whether the source supports it.

## What a passed wording check shows

A passed wording check shows that the quoted span matches the text actually compared, under the check's comparison rule. The pass is relative to that evidence. It does not certify that the compared text is the original author's words, that the span keeps its meaning in context, or that the quoted claim is true. When the text needed for the check is missing, the citation is unverified, not passed; counting absence as success would make the same citation pass or fail according to whatever copy happens to be at hand. Commonplace's quote checker illustrates the point: it can falsify a `verbatim`-marked quotation by matching it against the Markdown source the quotation links, and a pass means only a match under its normalization rule against that linked text ([ADR 046](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)).

## Narrow the citation or return to the source

A citation that claims no more than the capture preserved can stand on the capture: exact words that were kept, or a bounded use the retained passage carries. A citation that claims more has two honest exits. Narrow it to what the capture supports, by attributing a paraphrase instead of quoting or by making a narrower claim. Or return to the source and consult the evidence that supplies what is missing. Relying silently on material that is not at hand is not a third exit.

## Scope

- The claim was abstracted from one system's citation design (Commonplace's ADRs 046 and 073). Its transfer to other citing practices rests on the reasoning above, not on corroborating evidence.
- No test finer than bounded versus broad, distributed or contextual material decides when a retained passage is enough. Where that boundary falls for a given claim is open.
- The bound does not decide whether a failed wording check should block or only warn. Failing a quote on mismatch is a choice within the [trade-off between checking cost and reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md).

---

Relevant Notes:

- [Checking retained results trades cost against reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md) — contrasts: this note bounds what a citation may claim; that note decides how strictly a check of the claim is enforced
- [ADR 046: verbatim quotes are validated against their cited source](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) — abstracted-from: the wording check used as this note's illustration; origin, not corroboration
- [ADR 073: untracked source snapshots require ingest grounding](../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md) — abstracted-from: the distinction between uses a retained passage can support and uses that need the full source, and missing evidence as failure; origin, not corroboration
