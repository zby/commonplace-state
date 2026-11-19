---
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
sources:
  - path: kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md
    role: Historical Commonplace quotation-checking design and observed mismatch cases; distinguish its assertions from independently supported theory and later amendments.
  - path: kb/reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md
    role: Distinction between retained source material, source analysis, direct semantic checks and source availability; historical syntax is amended by ADR 094.
  - path: kb/reference/adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md
    role: Occurrence, uniqueness, containment, normalization and their limits; example of a checking design, not universal authority for its chosen policies.
  - path: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
    role: Existing argument for mechanical checking when derivation, source identification and source availability permit it; assess its applicability rather than importing its strongest claims uncritically.
---

# Commission: Quote checking

## Intended contribution

Rebuild the existing artifact as a theory note about quote checking in general for readers designing or operating agent-operated knowledge bases. Explain what different checks establish, the assumptions that make their results meaningful, and what remains unverified. This is an explanatory topic treatment, not an operator procedure and not an effort to invent one overarching claim to justify a claim-shaped title. General reasoning must stand beyond Commonplace's selected implementation, which may supply bounded cases.

## Must keep

Keep the distinctions among wording agreement, attribution, contextual interpretation and truth of a quoted claim. Distinguish original and intermediary sources, retained material and material currently accessible to a checker, and mechanical matching from semantic judgment. Preserve the useful insight that a label alone cannot establish fidelity, but do not preserve the incumbent wording or taxonomy for its own sake. Explain mechanisms and limits rather than merely list these distinctions. A source larger than the available model context budget requires a selective or compressed representation in that context; this does not imply lossy storage in the larger system, nor loss of exactness in every selected passage. This constraint is subordinate to the note's purpose, not a required organizing argument.

## Must exclude

Do not conflate current model context, retained source evidence and the particular evidence a check actually used. Do not use 'ingest' as an unexplained universal stage that fixes fidelity permanently. Do not force second-hand provenance and verbatim wording into mutually exclusive categories. Do not infer semantic support, upstream authenticity or truth from string matching. Do not preserve the universal forced-lossy-retention claim, the mandatory locator-layer field or the same-offset argument merely because they occur in the incumbent. Do not reproduce a procedural checklist or turn this into documentation of Commonplace's current commands. No new named external-source claims are commissioned: the authorized basis is the listed repository artifacts and explicit reasoning. If external evidence is necessary, report the gap rather than invent support or browse uncommissioned sources.

## Reserved decisions

The user authorized a topic title, 'Quote checking', and explicitly approved an exception to this note's collection claim-title convention. Do not modify the collection contract. Keep type types/note.md; remove the title-as-claim trait. The workflow mechanically preserves the incumbent title/H1 and path: keep them temporarily for this candidate and report that the separately authorized retitle remains for the session agent after publication approval. Do not reshape the body to defend that temporary heading. Treat it as a known transition constraint when reviewing, not as a demand for the old claim.

Do not change dependents, source documents, tags/indexes or ADRs. Report specific dependent changes needed, including those needed to remove invalid implications. Publication of the candidate requires the user's separate approval. A lasting write brief is not yet authorized; propose its content after the candidate rather than silently adding one.

## Current direction

The user explicitly chose a theory note on quote checking in general, agreed to multistage writing, authorized reconsideration of the capture-time ceiling and layer taxonomy, and authorized this note's topic-title exception. The author may replace or drop the old 'fixed at capture/ingest' claim and 're-capture is the only remedy' formulation, and replace the three-layer taxonomy even though the role report says dependents rely on them. Preserve justified explanations, not known conflations. In the reconciliation report identify the impacts on ADR 046, the atomic-step note, the Peters–Chin-Yee and ROME ingests and the claims-and-grounding tag head, without editing them. Their use of the old note is compatibility information, not evidence that its claims are true. The role report is supplied separately by the workflow to the author/reviewer; reconstructors must not use the incumbent or its reviews as evidence.

The user found the first candidate too long and explicitly requested: 'rewrite it, compact it, remove the redundancies'. This revision must be substantially shorter, not a sentence-polish pass. Aim for about 650–850 words of body as an editorial target, not a reason to omit a necessary condition. Combine related distinctions into a few explanatory sections. State each limit once; do not repeatedly restate that string matching cannot establish meaning, attribution or truth. Keep the central mechanisms and useful distinctions from Must keep, but compress their presentation.

Lead with the explanation, not with a tour of ADRs. Cite ADRs at the claims or examples they support without repeatedly saying that they are merely one system's choices. Do not introduce an ADR then immediately discount its relevance. Remove drafting-process narration such as 'the following is this note's inference', 'no supplied source states it', 'the terms below are this note's definitions' and repeated source-scope disclaimers. Present explicit reasoning directly; put evidential accounting in the reconciliation report. Keep real uncertainty beside the affected claim, but do not substitute attribution disclaimers for reasoning. Avoid duplicative footer links and open questions that merely restate distinctions already explained. Drop peripheral branches rather than compressing every branch into a dense inventory. In particular, the full derived-copy argument, historical mismatch measurements, extraction heuristics and version-policy comparisons need not each have their own treatment; retain them only where they materially explain quote checking.

Exactness under normalization, source identity, occurrence/context selection and checks along a source chain are investigative avenues, not a mandatory section outline. The source-first workers choose a compact supported argument. Do not repeat the prior candidate's unsupported phrase 'does not suppress recomputation'. Do not imply that unresolved-case reporting detects quotations an extractor misses entirely, that a version pin by itself detects every later edit, or that locating a unique occurrence proves authorial intent. Preserve the distinction between a check's tested property and conclusions it cannot establish.
