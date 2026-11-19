---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/gibson-dependency-locality-theory.ingest.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Ingest: The Dependency Locality Theory (Gibson 2000)

**Source:** [Ingest: The Dependency Locality Theory (Gibson 2000)](../../../../sources/gibson-dependency-locality-theory.ingest.md)

Post-ingest pass after re-ingest with the dependency-length writing-guidance occasion. The ingest already carries eleven labelled footer links; this report checks those and looks for gaps. All eleven existing targets resolve. The main gaps are two batch siblings that already link to this ingest without a return edge, and one batch sibling with no edge in either direction.

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md`, section "Outbound links". Destinations to scan: theory, reference, agent-memory-systems, agentic-systems, tags, other sources. Excluded: `kb/work/`, `kb/instructions/`. Authorised labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external; sparingly). External prospecting skipped; the only external target is the already-present `derived-from` PDF.

**Existing-link verification:**
- `test -e` on all seven repo-local KB-side targets in the footer (two-rewrites, human-writing-structures, human-llm-differences, local-materialization, soft-bound-traditions, skill-and-working-memory, attention-is-all-you-need) -- all OK. The three sibling ingests (Temperley 2007, Futrell-Levy-Gibson, Gibson 2019) exist as untracked files in the working tree.

**Title listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory kb/reference --glob '*.md' | rg -i "writ|prose|sentence|reader|read |human|style|wording|repetition|attention|distance|adjacen|local|operator|term|metaphor"` -- flagged: `design-for-the-first-time-human-except-on-access-cost` (kept, see below), `writing-styles-are-strategies-for-managing-underspecification` (rejected), `warranted-reader-update-is-the-objective-of-substantive-writing` (rejected), `link-strength-is-encoded-in-position-and-prose` (rejected; "position" is link position, not word order), `adr/011-notes-must-be-accessible-to-external-readers` (rejected), `adr/116-one-word-per-concept-across-prose-and-code` (rejected).

**Topic indexes:**
- `kb/tags/document-system-README.md` -- Foundations and Writing Conventions sections. Confirms `human-llm-differences` and `design-for-the-first-time-human` as the dual-audience writing anchors; no syntax or sentence-processing entry exists. Index membership is not applicable to a source ingest.
- No tag head covers psycholinguistics or writing style (`ls kb/tags | rg -i "writ|lang|prose|read"` -> none).

**Body search:**
- `rg -n -i "dependency|center-embed|nested clause|parsing load|parse cost|garden.path|right-branching|working memory|psycholinguist|sentence processing|readability" kb/theory kb/reference kb/tags kb/agentic-systems kb/agent-memory-systems -l` -- too broad ("dependency" matches software dependencies); discarded and narrowed.
- `rg -n -i "center-embed|parsing load|parse cost|right-branching|psycholinguist|sentence processing|readability|plain language|syntax|word order|sentence length|long sentence|lost in the middle|positional" ...` -- no psycholinguistic or word-order hit outside the already-linked two-rewrites note. Hits are code syntax, positional replay, and "local readability" in a proposal (rejected, keyword-only).
- `rg -n -i "gibson|temperley|futrell|dependency.length|locality" kb --glob '*.md' -l` -- found two further batch siblings: `gibson-1998-linguistic-complexity-locality.ingest.md` and `temperley-gildea-2018-minimizing-dependency-lengths.ingest.md`, plus the untracked `futrell-dependency-length-minimization.ingest.md`. Other hits are unrelated uses of "locality" (code locality, memory locality) or are in excluded `kb/work/`.
- `rg -n 'gibson-dependency-locality-theory' <gibson-1998> <temperley-gildea-2018>` -- both already link this ingest with `compares-with`; this ingest does not link back. `futrell-dependency-length-minimization` has no edge to or from this ingest.
- `rg -n -i "necessary conditions next|short, literal sentences|ASD-STE|simplified technical english|one main point" kb/theory kb/reference kb/tags kb/sources` -- no reference or theory artifact owns the AGENTS.md sentence rules; the ASD-STE100 instruction is in excluded `kb/instructions/`.
- `rg -l -i "lost in the middle|long-context|context rot|syntactic|readability|plain language|working memory|cognitive load" kb/sources --glob '*.ingest.md'` -- no LLM-side syntactic-distance or position-sensitivity source that would supply the missing LLM half. `skill-and-working-memory` is already linked.

**Link following:**
- `two-rewrites-exposed-a-syntax-or-repetition-tradeoff` footer -> ASD-STE100 instruction (excluded), frontloading, Toulmin sections, short composable notes. None adds a distance-cost axis.
- `human-writing-structures-transfer-to-llms` footer -> Toulmin, structured-prompt gains, content-effects source. Confirms the per-convention transfer test is the governing connection; nothing new for this source.
- `futrell-dependency-length-minimization` Connections section -> two-rewrites, local-materialization, human-writing-structures: the same KB-side cluster as this ingest, which confirms the batch shares one landing set.
- `design-for-the-first-time-human-except-on-access-cost` body -> "readable prose can serve both consumers ... transfers one property at a time"; sentence-level word order is such a property and does not involve access cost.

**Other destinations:**
- `kb/agentic-systems/`, `kb/agent-memory-systems/` -- no plausible match for a human sentence-processing model; skipped after the narrowed body search returned no relevant hit.
- `kb/reference/` -- no artifact owns writing-style rules; ADR 011 and ADR 116 considered and rejected.

## Connections Found

- [Gibson 1998 SPLT ingest](../../../../sources/gibson-1998-linguistic-complexity-locality.ingest.md) -- **compares-with**: SPLT is DLT's direct predecessor by the same author, and the two differ on storage cost (distance-based in 1998 versus a fixed count of predicted heads in 2000). A writer choosing the storage-minimization tie-break (Extractable Value 6) needs to know the metric changed between versions. This is the return edge for an existing `compares-with` from the 1998 ingest.
- [Temperley and Gildea 2018 review ingest](../../../../sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md) -- **compares-with**: the review supplies rivals (EIC, end-weight, predictability) and contested comprehension evidence for DLT. This ingest's Limitations section names the missing rivals but cites only Futrell-Levy-Gibson and Temperley 2007, so the review is the more direct pointer. This is the return edge for an existing `compares-with` from the review.
- [Futrell, Mahowald and Gibson 2015 treebank ingest](../../../../sources/futrell-dependency-length-minimization.ingest.md) -- **compares-with**: on comprehension cost versus its imprint on word order. DLT supplies the per-sentence cost mechanism; the 37-language treebank study shows that languages shorten dependencies below random baselines but measures distance in words, not new referents. This bears on Extractable Value 3, which asks any lint check to choose a metric. Neither ingest links the other.
- [Design for the first-time human, except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md) -- **compares-with**: on per-property transfer of human ergonomics. The note says that readable prose transfers to agent consumers only property by property; DLT names one concrete human-side property (head-dependent distance) for which no access-cost exception applies. Weaker than the existing human-llm-differences edge; author only if the theory note planned in Recommended Next Action does not absorb it.

## Bidirectional Candidates

None. The two return edges above complete pairs that the other side already authored; they are listed under Connections Found because the missing half is on this ingest.

## Reverse-edge Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → source -- **evidenced-by** (theory label): the note says the rewrites reduced "parsing load" but names no mechanism; DLT qualifies that term as integration plus storage cost for human readers. Grounding needs retained quotes first, because this ingest's Quotes section is empty; otherwise the link text must carry `(snapshot required)`.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) → source -- **evidenced-by** (theory label): DLT bounds the human half of the transfer test for word-order conventions. The same quote precondition applies.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- concerns the illocutionary style of context files (prescriptive, prohibitive and similar), not syntax or processing cost.
- [Warranted reader update is the objective of substantive writing](../../../../theory/warranted-reader-update-is-the-objective-of-substantive-writing.md) -- concerns contribution selection, not sentence form.
- [Link strength is encoded in position and prose](../../../../theory/link-strength-is-encoded-in-position-and-prose.md) -- "position" means link placement in a note; keyword-only match.
- [ADR 011: Notes must be accessible to external readers](../../../../reference/adr/011-notes-must-be-accessible-to-external-readers.md) -- establishes an external human audience, where DLT evidence applies, but its decision concerns vocabulary glosses. A `see-also` would add little.
- [ADR 116: One word per concept across prose and code](../../../../reference/adr/116-one-word-per-concept-across-prose-and-code.md) -- terminology consistency; DLT's given-referent effect is adjacent but too indirect to help traversal.
- [Model signals could guide harness-level context unloading and recall](../../../../theory/attention-can-be-reused-as-a-kind-of-soft-reference-count.md) -- about attention weights as harness signals; it does not test distance cost for LLM readers.

## Index Membership

None. Source ingests are not entries in tag heads, and no tag covers sentence processing.

## Synthesis Opportunities

The batch of seven dependency-locality ingests (Gibson 1998, Gibson 2000, Temperley 2007, Futrell 2015, Futrell-Levy-Gibson, Temperley-Gildea 2018, Gibson 2019) all land on the same three theory notes (two-rewrites, human-writing-structures, local-materialization) and all record the same missing LLM half. That convergence supports the theory note proposed in this ingest's Recommended Next Action. Citing all seven would exceed the ADR 082 limit of five distinct tracked sources without paired verified quotations, so the note needs either a subset or retained quotes.

## Maintenance Observations

- The batch's cross-links are incomplete in a way that depends on ingest order. Earlier-ingested siblings do not link later ones (this ingest lacks Gibson 1998, Temperley-Gildea 2018 and Futrell 2015). A batch-level connect pass after all siblings land would close these gaps in one step.
- This ingest's Quotes section is empty. Every reverse edge from `kb/theory/` would need quotes retained (cp-skill-ground) or a `(snapshot required)` marker. The Limitations section also records that the pdftotext capture is scrambled in the ambiguity-resolution section.
- No tag head covers writing conventions beyond the one-entry "Writing Conventions" section of `document-system-README.md`. If the planned theory note is written, that section is its natural home.

## Flags

- Tension to keep visible, not resolve: DLT measures distance in new discourse referents and uses peak cost, while Temperley 2007 and Futrell 2015 use word counts and summed length. Any writing guidance has to pick one metric.
- No split candidate: the ingest makes one coherent source analysis.
