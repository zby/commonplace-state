---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The rest falls to judgment against adequate evidence, which needs review and does not suppress recomputation."
    reason: "Basis: claim-account §12–§13 and reconstruction I4 support only that judgment-based checks have no derivation rule and are handled by review and managed staleness against the evidence they read. Neither the reconstruction nor the linked derived-copy note says that such a judgment 'does not suppress recomputation', and the clause is obscure here: the suppression mechanism in the preceding paragraph belongs to a trusted false copy, not to a judgment. A reader cannot tell what the clause asserts or why it holds. Required change: drop the clause 'and does not suppress recomputation', or restate it as the supported point that a support judgment is not a recomputable copy, so it is kept current by review against the evidence it read."
    level: warn
  - scope: passage
    quotes:
      - "Missing source bytes are reported separately and never count as verified. Missing source bytes are a different outcome from a mismatch: they leave the label unverified, not refuted."
    reason: "Basis: candidate, section 'A result means what the evidence it read allows'. Two consecutive sentences open with the same subject and restate one point: missing bytes are a separate outcome that does not verify the label. The collection's quality bar keeps a sentence only when it changes what the reader understands. Required change: merge the two sentences into one that says missing source bytes are reported separately from a mismatch and leave the label unverified, not refuted."
    level: warn
  - scope: passage
    quotes:
      - "They also fail for any check run where the source bytes are absent."
    reason: "Applying the derived-copy note's third precondition (ground truth existing at validation time) to locally absent source bytes is wider than that note's own example, which concerns evidence produced by execution. The claim account §12 and reconstruction N8 give this application, and the candidate marks the paragraph as its own inference, so no change is needed."
    level: info
  - scope: document
    quotes: []
    reason: "The H1 and path still carry the incumbent claim title while the body is a topic treatment and `title-as-claim` is removed. The commission's Reserved decisions make this a known transition constraint; the candidate report records that the authorized retitle to 'Quote checking' remains for the session agent after publication approval. No change is needed in this candidate."
    level: info
outcome: warn
---

# Review

The candidate makes the commissioned contribution. It rebuilds the note as an explanatory treatment of quote checking in general. It opens on the label-versus-check mechanism with three outcomes. It then explains that a match holds only relative to a span, a source text and a normalization rule, that finding the words is weaker than locating the passage, and that a match licenses nothing about context, support, relevance or truth. The evidence half keeps retained, accessible and used material apart and treats model context as a separate fourth thing. It covers semantic hops, intermediary chains, source identity and version, and extraction assumptions. Every Must keep item from the commission is present. In the context-budget passage, the subordinate constraint is stated correctly: selection loses surroundings, not exactness, and implies no lossy storage.

Delta and dependents. Each material commitment of the start text is accounted for in the candidate report. The capture-time ceiling, "re-capture is the only remedy" and the three-layer taxonomy are replaced, although `kb-role` lists them as relied on. The commission's Current direction explicitly authorizes this, and the report says so and lists the needed dependent changes without editing the dependents. The paraphrase-has-no-derivation-rule claim, which dependents rely on, survives in a generalized form. The fidelity/authority distinction, the forced-constraint argument, the locator corollary, the lossless-short-source scope and the epistack evidence paragraph are omitted with reasons. `kb-role` lists them as unused, and the commission excludes several of them. No commitment appears that the claim account does not give.

Exclusions and contracts. The candidate never uses "ingest" as a stage and does not treat second-hand provenance and verbatim wording as exclusive. It infers no support, authenticity or truth from matching and contains no procedure or command documentation. It presents ADR 094's uniqueness rule, source-kind normalization and the no-fallback route as one design's selections. The traits drop `title-as-claim` and `has-external-sources`, the type stays `types/note.md`, and a `## Scope` section states the limits. The ADRs are linked `abstracted-from` and the derived-copy note `extends`, which follows the origin-is-not-corroboration rule. Inferences beyond the sources are marked in place: over-normalization, attribution, source chains, the version trade-off and the derived-copy application.

Evidence. I checked the quotations and close paraphrases of ADR 046 ("load-bearing", "worse than no check", the mismatch categories, proximity pairing and code fences) and of the derived-copy note's asymmetry and preconditions against the linked files. They match. The two warnings are local prose repairs and do not block publication.
