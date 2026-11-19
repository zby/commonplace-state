---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - and no rival capture design drops the layering while preserving the commitments
    the framework has already made
  reason: 'The linked rival-test note says the test ''cuts in one direction only'':
    finding no rival leaves a rule ''only undemoted — not proven inherited''. The
    note uses it to certify that layering ''is not a design choice''. A rival also
    exists and the note mentions it: keep the full authoritative artifact (the sibling
    PDF or its extracted text) outside the context window as the verification ground
    truth, and give the LLM only excerpts. A substring checker does not spend context-window
    budget, and private retention of the full text is already the KB''s practice for
    external sources. So the forcing argument applies to the LLM-facing snapshot,
    not to the ground truth a citation can be checked against. Either state the invariant
    that excludes this rival or weaken ''forced'' to ''forced for the consumer-facing
    snapshot''.'
- scope: passage
  quotes:
  - is spent at capture and never replenished
  - The one chance here is ingest, and what was not preserved verbatim then is permanently
    downgraded
  reason: 'The temporal framing conflicts with the note''s own remedy. While the authoritative
    artifact is retained, re-capture is available at any time, so fidelity is replenishable.
    That is the recomputable regime (precondition 3 of the derived-copy rule: ground
    truth exists at validation time), not the history regime, where ''after production,
    the option is gone''. The defensible claim is that a citation''s fidelity is bounded
    by the most faithful ground truth still retained and reachable from the citation.
    Ingest is the one chance only when the authoritative artifact is not kept, for
    example when a served original disappears. That is the second-hand case, not the
    general case.'
- scope: passage
  quotes:
  - Two spans at the same file offset can differ in provenance quality by a full layer
  - Any locator design must encode the layer.
  reason: Two spans at the same offset in the same file are the same text and cannot
    differ in layer. If the offsets refer to different files, the file identifier
    already separates them. If the snapshot marks its layers structurally, a span's
    layer is a mechanical function of its position. A layer field in the locator would
    then be a derived copy, which the cited derived-copy rule requires to be checked
    or absent. The defensible corollary is that the layer must be resolvable from
    the locator, either encoded and validated or derived from a layer-marked snapshot.
    It is not that every locator must encode the layer.
- scope: passage
  quotes:
  - it produces precisely the hand-maintained-and-trusted copy that rule forbids
  reason: 'Once ADR 046 ships the verbatim-quote check, a paraphrase marked `verbatim`
    is not trusted unchecked. Unless it happens to match the snapshot as a substring,
    it fails validation. The note''s mechanism point still holds: the marker cannot
    raise fidelity and can only be falsified. But ''hand-maintained-and-trusted''
    describes the state before ADR 046, not the current one.'
- scope: passage
  quotes:
  - the shipped verbatim-quote checker, run over that corpus, found eighteen of eighty-seven
  reason: ADR 046 says the 18 mismatches were 'dominated by editorial omission (`...`),
    bracketed substitution, case changes, and punctuation moved inside the quotation
    boundary'. Those are quoting edits to verbatim-layer text, not paraphrase-layer
    passages promoted by notation. The evidence supports 'verbatim claims need a mechanical
    check'. It does not support the layering claim or the claim that paraphrase was
    marked verbatim. Say what the mismatches were, or cite evidence of cross-layer
    misattribution.
outcome: report
attack-outcome: partially lands
description: Retained report review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/critique-note.md
contract: report
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/critique-note.md
note-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/5c1a7b517c6bdcd5e9897a50/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/5c1a7b517c6bdcd5e9897a50/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 40bf81387d1e48b888061afa6fb4ff18
completed-at: '2026-11-16T22:12:07Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/40bf81387d1e48b888061afa6fb4ff18/outputs/review.md
raw-output-sha256: 127315627e0523d4b8cf0d3b6b2982d358c3fe0caeea9214c148abda480d8254
format: 2
---

# Critique: A citation cannot assert more fidelity than its capture preserved

**Note:** kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
**Central commitment:** A citation's fidelity is capped by the capture layer that holds the passage (verbatim, paraphrase or second-hand). The cap is fixed at ingest and never rises downstream. Notation cannot raise it; only re-capture can.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is a provenance engineer from reproducible-research and records-management practice, such as an archivist or the designer of a citation checker that runs against PDFs. They accept the narrow mechanism: writing `verbatim` beside a paraphrase does not make it verbatim. They reject the claim built around it. The note identifies "the capture" with the LLM-facing markdown snapshot. It then treats that snapshot's lossiness as the ceiling on every citation. Those are two different artifacts:

1. **The forcing argument covers only the consumer view.** The context window is a limit on what the LLM reads. Mechanical verification of a quote does not run in the context window; a substring test over extracted PDF text costs nothing there. The note already names the authoritative artifact ("the sibling PDF"), and the KB keeps full external copies in private snapshots. A design can therefore keep layered excerpts for the reader and retain full text as the check's ground truth. That is a boundary-preserving rival in the sense of the linked rival-test note. That note also says that failing to find a rival "certifies nothing", so it cannot support "the layering is not a design choice" even if no rival had been found.

2. **The ceiling is not fixed at ingest.** While the authoritative artifact is retained, a citation can quote it directly with a page locator, and a checker can verify the quote. The note's answer is that this is "re-capture". But if every operation that raises fidelity is renamed re-capture, "only re-capture raises fidelity" becomes true by definition. The substantive claim is then that fidelity is bounded by the most faithful retained ground truth reachable from the citation. That is precondition 3 of the derived-copy rule, a recomputable regime. It is not the history note's regime, in which the record is gone after production. The analogy to "history has one chance to become checkable" fits only when the original is not retained (dead URLs, unretained PDFs, intermediaries). Those are the second-hand cases, not long sources in general.

3. **The corollary contradicts the rule it relies on.** Within one file, layer is a function of position. If the snapshot marks its layers, a layer field in the locator is a derived copy of recomputable truth. The derived-copy rule says to check such a copy or omit it, not to require it in every locator.

On this view the note has a true local mechanism: a marker cannot upgrade the stratum it points into. But it presents that as a temporal law ("fixed at ingest", "one chance") and an inherited constraint ("forced"), and neither generalization survives retention of the authoritative artifact.

## How the note engages it

**Partially engaged.**

- Section "Why notation cannot repair it" fully answers the narrow version: no mechanical derivation rule links paraphrase to source, so a marker cannot move the bound. The attack concedes this.
- The opening paragraph ("The only operation that raises fidelity is re-capture") and the history paragraph ("recoverable only by returning to the authoritative artifact and capturing again") recognize the retained-artifact route. They file it as re-capture without noticing that this weakens "fixed at ingest" and "non-increasing" from a temporal claim to a claim about which ground truth the citation points at.
- Section "Capture is layered because it is forced to be" does not consider separating the LLM-facing snapshot from the verification ground truth. It also reverses the one-way logic of the rival-test note it cites.
- Section "Scope" handles short sources, where layers collapse. It does not handle long sources whose full text is retained for mechanical checking, which is the case the attack targets.
- The corollary does not engage the redundancy objection.

## Constructive findings

- Restate the central bound relative to the retained ground truth: "a citation's fidelity is bounded by the most faithful retained artifact it can be checked against". Make "fixed at ingest" a special case that holds when the authoritative artifact is not retained.
- Limit "forced" to the LLM-facing snapshot. Then either state the boundary invariant that excludes keeping out-of-context full text for verification, or present that design as the rival it is. Do not cite the rival-test note as certifying inheritance.
- Keep the history-note link only for the unretained or second-hand case. Elsewhere, link the claim to the derived-copy rule's precondition 3.
- Rewrite the corollary as "the layer must be resolvable from the locator: either derived from a layer-marked snapshot or encoded and validated". Drop the impossible same-offset example.
- Update the notation paragraph for ADR 046: a paraphrase marked `verbatim` is now a checked false copy that fails validation. It no longer survives as a trusted unchecked copy.
- Describe the ADR 046 mismatches accurately (editorial quoting edits). Alternatively, add evidence that paraphrase-layer passages were marked verbatim, if such evidence exists in the casebook corpus.

## Secondary objections (optional)

- "the two move in opposite directions": fidelity is non-increasing and authority is earned upward. That is a ceiling with growth beneath it, as the note's next sentence says, not opposite motion. The phrase overstates the contrast.
- The second Open Question (fidelity versus usefulness) concedes that the bound constrains verification, not the citation's value to a reader. The title's "cannot assert more fidelity" is safe on that reading. The opening claim that a claim "can be no better grounded than the capture step left it" conflates grounding with fidelity, which the authority paragraph had just separated.
