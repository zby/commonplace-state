---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Narrow it to what the capture supports, by attributing a paraphrase instead of quoting or by making a narrower claim. Or return to the source and consult the evidence that supplies what is missing."
    reason: "Basis: supplied-commission.md, Current direction: \"Stop when the reader knows when to narrow the citation and when to return to the source\"; Must keep: \"To claim greater precision or broader support, consult evidence that supplies what is missing.\" The candidate presents the two exits as bare alternatives. It drops the must-keep's condition (\"to claim greater precision or broader support\"), so the closing section does not tell the reader which exit fits which case; the reader must infer it from the earlier \"When the capture is enough\" section. Required change: state the selection condition in this section: return to the source when the citing text needs the stronger fidelity or broader support it currently claims; narrow when a claim at the fidelity the capture preserves serves the citing text (or the source is not at hand)."
    level: warn
  - scope: document
    quotes: []
    reason: "Basis: supplied-collection-contract.md, Title and body composability: \"Add the `title-as-claim` trait when using one, so review gates check the promise.\" The candidate's title is a contestable claim, but its frontmatter has no `traits` field (carried over unchanged from supplied-start.md). Required change: add `traits: [title-as-claim]` to the frontmatter."
    level: warn
  - scope: passage
    quotes:
      - "Failing a quote on mismatch is a choice within the"
    reason: "This Scope bullet carries a commitment the claim account does not list. It is kept from the start text because supplied-kb-role.md lists it as relied on, and the candidate report flags it. Kept only as a limit on what the bound decides, it adds no new claim. Accepted; no change needed."
    level: info
outcome: warn
---

# Review

The candidate makes the commissioned contribution. It opens with a constructed paraphrase-versus-quotation example and states the central claim as the note's own inference. The claim is that quotation marks cannot supply words the capture never kept. The candidate frames the limit as one of evidence, not a ban on assertion. It gives the bounded-versus-broad criterion from ADR 073 without inventing a finer test. It says what a passed wording check shows and does not show, and it treats missing evidence as unverified. It uses Commonplace's checker in exactly one scoped illustrative sentence and keeps the title and path.

Delta against the start text: the candidate report accounts for every material commitment of the old note. Kept, replaced and omitted items match the claim account, and omissions follow commission exclusions or point to the trade-off note. Every claim `kb-role` lists as relied on survives. The one kept commitment outside the claim account is noted above as info.

Evidence: each claim stays within the reconstruction's support or stated inference. "Narrow the citation" is not attributed to the sources. A pass is described as a match under the comparison rule, not as exact identity. The ADRs are linked `abstracted-from` with explicit "origin, not corroboration" phrasing. The Scope section names the open boundary question and how far the claim transfers. Outbound links resolve, and the linked trade-off note supports the enforcement-choice framing.

Neither warning blocks publication. One makes the exit choice explicit, which the commission's stopping condition requires. The other adds a trait the collection contract asks for.
