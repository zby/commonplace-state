# Bounded acquisition recovery — requirements foundations

Date: 2026-11-16

## Outcome and boundaries

Recovered one verified full **distinct conference-paper preprint**: Jureta,
Mylopoulos and Faulkner, *Revisiting the Core Ontology and Problem in
Requirements Engineering*, RE 2008, arXiv:0811.4364v1. Neither commissioned
journal article was recovered. No reference-model extended abstract was
recovered or substituted.

This was acquisition only. Read `foundations-results.md` before searching;
did not repeat its Crossref, OpenAlex, Semantic Scholar, publisher PDF,
handle-resolver, or CiteSeer requests. No ingestion, source analysis,
delegation, installation, payment, authentication, access-control bypass,
tracked-file edit, staging, or commit. Stopped after the bounded routes below.
This is not evidence that no public full journal copy exists elsewhere.

## Verified full source retained

- Title printed in PDF: *Revisiting the Core Ontology and Problem in
  Requirements Engineering*.
- Authors printed in PDF: Ivan J. Jureta, John Mylopoulos, Stéphane Faulkner.
- Identity/version: arXiv:0811.4364v1, submitted 26 November 2008. Author note
  on the title page identifies publication at RE 2008 and says this version
  is essentially the same as that published by IEEE. The arXiv landing page
  attributes DOI `10.1109/RE.2008.13` to this work.
- **Not** *A core ontology for requirements*, Applied Ontology 2009,
  DOI `10.3233/AO-2009-0069`.
- Date caveat: the served PDF prints **October 22, 2018** on its title page;
  PDF creation/modification metadata also dates to 2018. The PDF nevertheless
  bears the arXiv v1 / 26 November 2008 identifier. Retained exactly as served;
  do not describe these bytes as verified original-2008 bytes, a new 2018
  research version, or the 2009 journal article.
- Discovery: public arXiv title search for `Revisiting the Core Ontology`
  returned this title and all three authors. The landing page confirms the
  conference identity and links the PDF. An additional arXiv title search
  for `A core ontology for requirements` returned three hits, none the exact
  commissioned journal article: this conference paper and two unrelated works.
- Landing URL: https://arxiv.org/abs/0811.4364
- Pinned identity URL: https://arxiv.org/abs/0811.4364v1
- Download URL: https://arxiv.org/pdf/0811.4364v1
- Raw PDF: `kb/reports/state/snapshot-web/recovery.xkqSwo/revisiting-0811.4364v1.pdf`
  — 175474 bytes, SHA-256
  `64c1d287fde6ebbff536340c5d882f4ca60b0af9aba023397c081befefdaa457`.
- Complete pdftotext extraction:
  `kb/reports/state/snapshot-web/recovery.xkqSwo/revisiting-extracted.txt`
  — 55837 bytes, SHA-256
  `282625a8b4c176f7931bc4684fb37ddda9e54e5d1e493404311b0f3b8e9ae3e6`.
- Snapshot: `kb/sources/.snapshots/revisiting-core-ontology-requirements-engineering-2008.md`
  — 56621 bytes, exact Markdown SHA-256
  `3fd5ccf2031710b6ef8aafae9cd10dc890050d03be2207c83d2cd19c2a9895cf`.
- Scope: full served 22-page preprint, including concluding section and all
  21 references. Not an abstract-only capture. Every PDF page produced
  nonempty text; the complete extraction was copied locally, byte-for-byte,
  after the capture header. Original PDF retained for layout and any
  nontextual content; no claim of pixel-faithful Markdown rendering.
- Method: followed `cp-skill-snapshot-web` and `kb/types/snapshot.md`;
  curl download, pdfinfo inspection, pdftotext UTF-8 extraction, exclusive
  new-file assembly and exact body-byte comparison. No existing snapshot
  with this source identity found. No model-mediated source cleanup.

## Reference-model journal article — unresolved

Target: Gunter/Gunter/Jackson/Zave, *A Reference Model for Requirements and
Specifications*, IEEE Software 17(3):37–43 (2000), DOI `10.1109/52.896248`.

Public search queries used the exact title, with `pdf` (Google), without
`pdf` (DuckDuckGo), and with `Gunter` (Bing). Google returned a JavaScript /
challenge shell, DuckDuckGo a bot challenge, and Bing unrelated results.
No usable author PDF route was established from those responses. Challenges
were not solved or circumvented.

A few author/institution entry-point probes also failed:

| URL | Basis and result |
|---|---|
| https://www.cis.upenn.edu/~hol/ | Parent of the historical author-hosted PDF URL in the prior ledger; HTTP 404. Did not retry the already-failed PDF URL. |
| https://www.cis.upenn.edu/~gunter/publications.html | Guessed author-publications path, not a discovered paper link; HTTP 404. |
| https://cgunter.cs.illinois.edu/ | Candidate author institutional hostname, not a verified paper route; curl certificate hostname mismatch (exit 60). Did not disable certificate verification. |

Exact remaining blocker: no verified, accessible full journal manuscript
obtained within these attempts. No new journal-paper title-page evidence to
resolve the author-order discrepancy recorded in the prior ledger. The
separate ICRE 2000 extended abstract, DOI `10.1109/ICRE.2000.855609`, remains
separate and was not acquired. A supplied authorized journal PDF or a
verified accessible author/institution full-text URL would unblock capture.

## Core-ontology journal article — unresolved

Target: Ivan J. Jureta, John Mylopoulos, Stéphane Faulkner, *A core ontology
for requirements*, Applied Ontology 4(3–4):169–244 (2009), DOI
`10.3233/AO-2009-0069`.

Google, DuckDuckGo and Bing were queried with `Jureta`, `core ontology`,
`pdf`. Google returned a JavaScript / challenge shell, DuckDuckGo a bot
challenge, and Bing unrelated results. No usable full-text route established.
The public arXiv searches above recovered only the distinct 2008 paper.

Followed the coauthor's Toronto institutional route, consistent with the
Toronto affiliation and email printed in the recovered PDF:

1. https://www.cs.toronto.edu/~jm/ — accessible personal home page, frameset.
2. https://www.cs.toronto.edu/~jm/frame.html — accessible navigation frame,
   links research to `main.html#Selected Publications`.
3. https://www.cs.toronto.edu/~jm/main.html — accessible selected-publications
   page; no `Jureta` or ontology-title match and no link to this article.

Exact remaining blocker: no verified, accessible full **2009 journal** copy
obtained within these new public routes; the distinct 2008 preprint does not
remove that blocker. A supplied authorized journal copy or an accessible
full-text URL for that exact article is still needed.

## Route evidence, storage and verification

All downloaded response bodies and the raw full PDF remain local and ignored
under the unique directory `kb/reports/state/snapshot-web/recovery.xkqSwo/`.
Preserving raw bytes follows this invocation's explicit instruction rather
than the snapshot skill's default temporary-directory cleanup.

Evidence files in that directory:

- `search-reference.html`, `search-ontology.html`: Google response shells.
- `ddg-reference.html`, `ddg-ontology.html`: DuckDuckGo challenges.
- `bing-reference.html`, `bing-ontology.html`: unrelated search results.
- `arxiv-search.html`: conference-title query and result link.
- `arxiv-core-search.html`: journal-title query, three distinct result titles.
- `revisiting-abs.html`: arXiv title, authors, conference DOI, v1 submission
  history, and PDF link (article-level citation metadata included).
- `revisiting-pdfinfo.txt`: 22 pages, unencrypted, 2018 creation/modification.
- `revisiting-pdfmeta.xml`: empty (PDF has no metadata stream).
- `mylopoulos-home.html`, `mylopoulos-frame.html`, `mylopoulos-main.html`:
  institutional author-page chain.
- `header.md`, raw PDF and full extraction: capture assembly inputs.

HTTP-error and certificate-error requests left no response-body file because
curl used `-f`; their exact URLs and failures are recorded above.

Verified ignore coverage with `git check-ignore` before payload writes.
Verified snapshot body equality, total byte counts, and SHA-256 after assembly.
No pytest or collection validation run: no code, tracked KB artifact, ingest,
or analysis was authored. Git diff remains empty. Other workers' untracked
source ingests were not edited or incorporated.

## Subsequent authorized temporary cleanup — ingest run, 2026-11-16

The ingest orchestrator verified the saved snapshot's exact SHA-256
`3fd5ccf2031710b6ef8aafae9cd10dc890050d03be2207c83d2cd19c2a9895cf`
and byte equality with `header.md` (784 bytes) followed by the complete
`revisiting-extracted.txt` (55837 bytes), totaling 56621 bytes. It checked
the retained landing-page citation title, all three authors, conference DOI
`10.1109/RE.2008.13`, v1 submission date, and 22-page PDF metadata including
the 2018 timestamps. The snapshot retains the full text, identity/version
caveat and capture metadata; it is sufficient for this text-based ingest,
not a pixel-faithful replacement for the PDF.

Under the subsequent user's explicit cleanup authorization and the snapshot
skill's default cleanup rule, the exact temporary directory
`kb/reports/state/snapshot-web/recovery.xkqSwo/` was removed after these
checks. Thus the raw PDF and other evidence files listed above are no longer
present. Their route/failure summaries, original sizes and checksums remain
in this acquisition record; the immutable Markdown capture remains intact.
This supersedes only the earlier temporary-retention status, not any journal
acquisition blocker. No worker session or audit record was deleted.
