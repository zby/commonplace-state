---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Narrow it to what the capture supports, by attributing a paraphrase instead of
    quoting or by making a narrower claim. Or return to the source and consult the
    evidence that supplies what is missing.
  reason: 'Basis: supplied-commission.md, Current direction: "Stop when the reader
    knows when to narrow the citation and when to return to the source"; Must keep:
    "To claim greater precision or broader support, consult evidence that supplies
    what is missing." The candidate presents the two exits as bare alternatives. It
    drops the must-keep''s condition ("to claim greater precision or broader support"),
    so the closing section does not tell the reader which exit fits which case; the
    reader must infer it from the earlier "When the capture is enough" section. Required
    change: state the selection condition in this section: return to the source when
    the citing text needs the stronger fidelity or broader support it currently claims;
    narrow when a claim at the fidelity the capture preserves serves the citing text
    (or the source is not at hand).'
  level: warn
- scope: document
  quotes: []
  reason: 'Basis: supplied-collection-contract.md, Title and body composability: "Add
    the `title-as-claim` trait when using one, so review gates check the promise."
    The candidate''s title is a contestable claim, but its frontmatter has no `traits`
    field (carried over unchanged from supplied-start.md). Required change: add `traits:
    [title-as-claim]` to the frontmatter.'
  level: warn
- scope: passage
  quotes:
  - Failing a quote on mismatch is a choice within the
  reason: This Scope bullet carries a commitment the claim account does not list.
    It is kept from the start text because supplied-kb-role.md lists it as relied
    on, and the candidate report flags it. Kept only as a limit on what the bound
    decides, it adds no new claim. Accepted; no change needed.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
note-sha256: e24cea9f0067865c07fe1d7eb07774f8b2d0c755a166254cad466a80ffd64e64
criterion-sha256: 6f5d24343fe9fd8387ed345957325abbae4ecf50e222df7b992b3b1b8ef484e2
target-sha256: e24cea9f0067865c07fe1d7eb07774f8b2d0c755a166254cad466a80ffd64e64
target-capture: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T164500Z/reviews/00d7a027c4fb/artifact/reviews/f2f804540839ba84f19fc9bb/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T164500Z/reviews/00d7a027c4fb/artifact/reviews/f2f804540839ba84f19fc9bb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T164500Z/reviews/00d7a027c4fb
launch: d443228a35524bd5a983531c1a8d6c16
completed-at: '2026-11-18T16:50:43Z'
raw-output: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T164500Z/reviews/00d7a027c4fb/calls/launches/d443228a35524bd5a983531c1a8d6c16/outputs/review.md
raw-output-sha256: e203d6b1caf87ac4f04a901151d1a86b9811b1695f3b4afecbaa4ad91fde301f
format: 2
---

# Review

The candidate makes the commissioned contribution. It opens with a constructed paraphrase-versus-quotation example and states the central claim as the note's own inference. The claim is that quotation marks cannot supply words the capture never kept. The candidate frames the limit as one of evidence, not a ban on assertion. It gives the bounded-versus-broad criterion from ADR 073 without inventing a finer test. It says what a passed wording check shows and does not show, and it treats missing evidence as unverified. It uses Commonplace's checker in exactly one scoped illustrative sentence and keeps the title and path.

Delta against the start text: the candidate report accounts for every material commitment of the old note. Kept, replaced and omitted items match the claim account, and omissions follow commission exclusions or point to the trade-off note. Every claim `kb-role` lists as relied on survives. The one kept commitment outside the claim account is noted above as info.

Evidence: each claim stays within the reconstruction's support or stated inference. "Narrow the citation" is not attributed to the sources. A pass is described as a match under the comparison rule, not as exact identity. The ADRs are linked `abstracted-from` with explicit "origin, not corroboration" phrasing. The Scope section names the open boundary question and how far the claim transfers. Outbound links resolve, and the linked trade-off note supports the enforcement-choice framing.

Neither warning blocks publication. One makes the exit choice explicit, which the commission's stopping condition requires. The other adds a trait the collection contract asks for.
