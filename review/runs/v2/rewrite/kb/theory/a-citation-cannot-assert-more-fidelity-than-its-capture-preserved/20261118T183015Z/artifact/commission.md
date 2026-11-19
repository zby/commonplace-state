---
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
sources:
  - path: kb/reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md
    role: Distinguishes what can be supported from a retained passage from what requires returning to the source.
  - path: kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md
    role: Establishes what the Commonplace wording check actually tests, for one illustration only.
---

# Commission: What a citation can support

## Intended contribution

Help a writer decide whether the material they retained supports the citation they want to make. Make the limit one of evidence, not a claim that writers cannot make unsupported assertions.

## Must keep

A paraphrase can preserve an idea without preserving the author's words. Quotation marks cannot recover those words. To claim greater precision or broader support, consult evidence that supplies what is missing. A successful wording check verifies a match under its comparison rule against the text actually used; it does not certify the original author, context, or truth. Missing evidence is not a pass.

## Must exclude

Do not teach the validator, survey checking techniques, or explain the two-layer storage design or its copyright history. Do not argue from legal or empirical claims.

## Reserved decisions

Keep the existing title and path. Do not split the note or edit its dependents. Publication requires operator approval.

## Current direction

Keep it short. Lead with the paraphrase versus direct quotation example. Use Commonplace's quote checker only to illustrate the principle, preferably in one sentence. Stop when the reader knows when to narrow the citation and when to return to the source.
