# Inbound contexts of `kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md`

5 file(s) link to this note. Searched: Markdown files under kb/, except kb/reports/, kb/work/, hidden directories and the note itself.

## `kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md`

- Title: 046-Verbatim quotes are validated against their cited source
- Description: `commonplace-validate` resolves every `verbatim`-marked quotation against the source it links; a false verbatim claim fails, and `unresolved` warns only where the convention is demonstrably in use

> The `verbatim` marker becomes load-bearing rather than decorative: it is now the cheapest of the three grounding-layer markers to assert and the only one that can be mechanically falsified. `paraphrase layer` and `second-hand` remain unchecked by construction — they never claimed exact text, and no derivation rule exists for them, which is precisely why [a citation cannot assert more fidelity than its capture preserved](../../theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md).

## `kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md`

- Title: Ingest: Generalization Bias in LLM Summarization of Scientific Research
- Description: 10 LLMs, 4,900 science summaries: models turn quantified, past-tense, descriptive results into generic, present-tense or action-guiding claims; accuracy prompts worsen it

> It is evidence for [A citation cannot assert more fidelity than its capture
> preserved](../theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md).
> That note treats a paraphrase-layer passage as unverifiable. The paper adds
> that LLM paraphrase of scoped claims is also *biased*, in a predictable
> direction toward broader scope. This argues for verbatim retention of
> scope-bearing qualifiers. In the same way, it is evidence for [An insufficient
> summary precedes the source rather than replacing
> it](../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md).
> For a question about population, time or recommendation strength, an LLM
> summary often fails the note's sufficiency condition, so the source must stay
> in the reading path.

## `kb/sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md`

- Title: Ingest: Locating and Editing Factual Associations in GPT
- Description: ROME localizes factual associations to mid-layer MLPs and edits them with a rank-one weight update — the nearest approach to our named explicit-retention falsifier, but it lacks scope-addressability

> The snapshot itself is the first limitation, and it bounds everything below. This is an abstract-level web-fetch of a 35-page paper: no causal-tracing methodology detail, no CounterFact numbers, no baseline table. The snapshot's own `description` — "evidence that factual knowledge is stored as identifiable, editable computation rather than diffuse distributed representation" — is stronger than both the captured body and the paper's stated scope, and a note inheriting that phrasing would assert more than the capture preserves, [which a citation cannot do](../theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md). Any note citing this ingest should restate the claim at the paper's strength: one class of subject-token factual association in two mid-size models, not knowledge in general.

## `kb/tags/claims-and-grounding-README.md`

- Title: claims-and-grounding
- Description: Curated head for the claims-and-grounding tag — claim titles, claim modality, ground truth and supersession, source grounding and quotes, and grounding evidence from review runs

> - [A citation cannot assert more fidelity than its capture preserved](../theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) — capture fixes the evidence a citation can claim; stronger notation cannot restore lost fidelity

## `kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md`

- Title: A note is an atomic step relative to the check that reads it
- Description: Two independent bounds on a note: one claim sized to the reader's bounded context, and one checkable inference sized to the checker's single pass — for the grounding check the unit is the unquoted source

> The reason is that Commonplace has moved that finding step into code. A
> quotation marked `verbatim` is resolved by substring match against the file it
> links, and a mismatch fails the note before any reviewer opens anything ([ADR
> 046](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md));
> the source-side material is itself held as retained quotes validated against the
> captured source ([ADR
> 073](../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)).
> This is the general rule that [a derived copy of recomputable truth must be
> checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)
> applied to citation: the quote is a copy of something held elsewhere, and it is
> admissible because a validator re-derives it and fails on mismatch. A paraphrase
> has no such derivation rule, and [a citation cannot assert more fidelity than
> its capture preserved](./a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md)
> — a passage never captured word for word cannot be quoted into this route
> without returning to the source.

> - [A citation cannot assert more fidelity than its capture preserved](./a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) — grounds: the capture-time bound that decides which sources can take the quoting route at all
