---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the captured text is itself another party's restatement"
    reason: "The three-layer taxonomy is framed as the stratification that lossy capture produces ('Capture is layered because it is forced to be'; 'it stratifies'), but the second-hand layer is defined by the source's own provenance chain, not by the capture step. The boundary case of a verbatim reproduction of a second-hand source (a court's restatement of a complaint, copied exactly into the snapshot) belongs to both the verbatim layer and the second-hand layer under the note's own criteria, so the layers are not one ordered scale. The same case also escapes the opening rule that 're-capture' is the only operation raising fidelity: when the original 'is no longer served', re-capture cannot raise it, and when it is served, the fix is capturing a different source rather than re-capturing this one. The taxonomy needs either two axes (capture fidelity versus source-chain position) or an explicit statement of how they combine."
    level: warn
  - scope: passage
    quotes:
      - "the source's own words, reproduced"
    reason: "Intermediate cases strain the verbatim/paraphrase boundary: a quotation trimmed with an ellipsis or a bracketed substitution, and a PDF-to-markdown conversion with OCR or formatting losses. Both are 'the source's own words' in part, neither is an own-words summary, and the note's linked ADR 046 reports that editorial omission and bracketed substitution dominated the observed mismatches. The note does not say which layer such passages occupy or whether a string-match failure demotes them to paraphrase."
    level: info
outcome: warn
---

# Review

The note's framework is the three-layer stratification of a captured source: verbatim, paraphrase and second-hand. Its grounding definition is the note's own framing. Layers arise because capture of a long source is forced to be lossy, and each layer fixes a ceiling on the fidelity a citation can assert.

Boundary cases tested:

- **Simplest instance — a short source captured losslessly.** The Scope section handles this: the layers collapse and the bound becomes vacuous. It maps cleanly.
- **Verbatim copy of a second-hand text.** It fails to map to one layer. The verbatim layer is defined by reproduction fidelity, and the second-hand layer by the source chain. A passage can satisfy both definitions, so the list is not a single ordered scale of fidelity grades. The forcing argument (context window and copyright) also does not produce the second-hand layer. This case falls outside the claimed coverage and is the WARN.
- **Between verbatim and paraphrase — an ellipsis-trimmed quote, a bracketed substitution or an OCR-damaged conversion.** These can be placed only with strain. The note's criteria do not settle whether they are degraded verbatim or paraphrase.
- **Adjacent concept — a translation.** A translation is neither the source's own words nor the snapshot's summary. It is closest to paraphrase, which is workable under the stated criteria, so no separate finding is raised.

The taxonomy is already short, so expanding it is not the obvious fix. Separating the source-chain axis from the capture-fidelity axis, or stating that second-hand is a qualifier applied on top of the other two layers, would resolve the main case without adding weight.
