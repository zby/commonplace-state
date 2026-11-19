---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A long source cannot be captured verbatim into markdown at full fidelity, because the consumer's context window is finite and because copyright forces trims."
    reason: "DEFEATED — premise (no stated modality, so universal): a long source cannot be captured verbatim at full fidelity, because the consumer's context is finite and copyright forces trims — Storage is not context. A full-text markdown conversion of a long CC-BY arXiv paper, kept as a local snapshot, is a verbatim capture of the whole source. A finite-context consumer reads windows of it by search, so the context window limits what is loaded, not what is captured. Copyright does not force trims on an openly licensed source, and in many jurisdictions it does not force them on a private research copy either; it constrains publication. The layering is therefore a product of capture choices or publication constraints, not of source length. That defeats the Scope's operative regime ('wherever the sources are long'). The central commitment survives, because it is conditional on which layer holds the passage. It should be rescoped to say the bound bites wherever capture actually was lossy. — LOCAL — instance"
  - scope: passage
    quotes:
      - "no rival capture design drops the layering while preserving the commitments the framework has already made"
    reason: "DOUBTFUL — premise (universal): the layering is an inherited constraint, certified by the absence of a boundary-preserving rival — The linked note says its test 'demotes; it does not certify' and that finding no rival leaves a rule 'only undemoted — not proven inherited'. Using it to establish that layering 'is not a design choice' reverses its direction. The full-text local-snapshot design in the previous finding is a candidate rival that preserves an LLM consumer and real documents. The note also states no independent boundary invariants against which a rival could be judged. The central commitment does not need layering to be forced, only that it exists where it occurs. — LOCAL — instance"
  - scope: passage
    quotes:
      - "The only operation that raises fidelity is re-capture."
    reason: "DOUBTFUL — premise (universal): fidelity is fixed at ingest, and raising it requires a distinct re-capture operation, so provenance quality is decided before any note is written — When the authoritative artifact sits beside the snapshot, as the note's own sibling-PDF case assumes, an author can check a paraphrase-layer passage against the PDF while writing and quote the PDF directly. The note counts that as re-capture. So 're-capture' absorbs every operation that consults the source, and the non-increase claim is close to definitional. The practical consequence, that quality is 'decided before any note is written', fails for any source whose authoritative artifact is retained. The commitment holds where the authoritative artifact is unavailable or costly to reach; that condition belongs in Scope. — LOCAL — instance"
  - scope: passage
    quotes:
      - "spans that did not appear in their cited snapshot, with no false mismatches on manual audit"
    reason: "DOUBTFUL — premise (universal, offered as evidence): the eighteen mismatches show that marking a paraphrase-layer passage `verbatim` fails — ADR 046 says the mismatches are 'dominated by editorial omission (`...`), bracketed substitution, case changes, and punctuation moved inside the quotation boundary'. Those are edited verbatim quotes, not paraphrase-layer passages promoted by notation. The evidence shows that verbatim marking is error-prone. It does not show that the layer boundary was crossed, which is the mechanism the note claims. — LOCAL — instance"
  - scope: passage
    quotes:
      - "A position-only locator would render them identical"
    reason: "DOUBTFUL — premise (universal): two passages of different layers can share a position, so a position-only locator cannot distinguish them — Within one snapshot, the verbatim block and the paraphrase summary occupy different offsets, so a position-only locator into the snapshot already distinguishes them. A consumer can recover the layer by looking up which block contains the offset. The collision exists only for a locator into the original source, such as a PDF page, where the verbatim span and the paraphrase of the same passage share a position. The corollary needs that condition stated. The core claim does not depend on it. — LOCAL — instance"
  - scope: passage
    quotes:
      - "A paraphrase-layer passage has no such rule — there is no mechanical comparison between a paraphrase and its source, only judgment."
    reason: "HOLDS — premise (universal): no mechanical derivation rule connects a paraphrase to its source, so notation cannot promote it into a checkable copy — The hunt looked at fuzzy matching, embedding similarity and LLM entailment checks. Each is either a judgment or a threshold heuristic that falls short of precondition 1 of the linked derived-copy rule ('natural-language summaries and judgments do not' qualify). ADR 046 agrees: paraphrase and second-hand markers 'remain unchecked by construction'. Marking a paraphrase `verbatim` now produces a validator failure rather than a promotion, which supports the claim that notation cannot move fidelity."
  - scope: passage
    quotes:
      - "capture sets a ceiling, and post-capture operations earn authority beneath it"
    reason: "HOLDS — premise (universal): fidelity and authority are separable axes; post-capture work raises authority without raising fidelity — The candidate counterexample is a paraphrase verified against the authoritative PDF, which seems to carry better provenance evidence than an unverified one. But that verification consults the original, which the note classifies as re-capture (see the re-capture finding), so it does not cross the ceiling within the note's terms. Verification against the snapshot alone cannot raise the layer. The premise holds as defined, and its strength is inherited from how broadly 're-capture' is drawn."
  - scope: document
    quotes: []
    reason: "HOLDS — unstated premise (universal): a citation's layer is visible to its consumer, so the fidelity bound can be 'made explicit and repaid deliberately' — This holds where a grounding-layer marker is used, which ADR 046 and the collection prototypes describe. Without a marker, the debt would be invisible. The note limits its practical claim to marked citations ('visible in the citation') and argues that a locator must encode the layer, so it already supplies this condition. No defeater was found inside the stated scope."
outcome: report
---

# Premise decomposition: A citation cannot assert more fidelity than its capture preserved

**Register:** claim
**Central commitment (one sentence):** A citation's fidelity is bounded by the capture layer (verbatim, paraphrase or second-hand) that holds the cited passage; no citation notation, locator or review gate can raise it, and only re-capture from the authoritative artifact can.

## Premises and counterexamples

The commitment rests on three groups of premises.

1. **Why the layers exist and where they occur.** The argument assumes long sources cannot be captured losslessly and that this layering is forced rather than chosen. These premises set the regime where the claim does work ("wherever the sources are long").
2. **Why the bound cannot be crossed.** The argument assumes paraphrase has no mechanical derivation rule, so the derived-copy rule turns a mislabeled paraphrase into a forbidden trusted copy. It also assumes that re-capture is a distinct operation separate from downstream citation work, and that fidelity is separate from authority.
3. **What follows and what supports it.** The argument assumes a position-only locator would conflate two passages from different layers. It cites the ADR 046 mismatch count as evidence, and it assumes without saying so that a citation's layer is visible to its consumer.

The core mechanism survives the counterexample hunt: there is no mechanical check from paraphrase to source, so notation cannot change a passage's layer. The weaknesses are in the parts around it. The claim that long sources force the layering confuses capture with context loading and treats publication limits as capture limits, and its citation of the rival test reverses that note's direction. The definition of re-capture is broad enough to make "fixed at ingest" nearly definitional, and it weakens the practical claim that quality is decided before any note is written. The cited evidence counts edited verbatim quotes, not paraphrase passages promoted by notation. All of these failures are local. Each one narrows the scope or corrects the support. None of them breaks the conditional bound.

## For the human

Look first at the premise that long sources force lossy capture. A full-text local snapshot defeats it, and it sets the regime the Scope section claims the note covers.
