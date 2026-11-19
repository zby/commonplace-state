## Fix Report: two-context-boundaries-govern-collection-operations

Source results: 16 fresh `warn` pairs from run `kb/reports/state/review/runs/20261112T073040Z` (profile `opus`, model `claude-opus-5-5`). Findings are numbered per WARN/low/medium/minor item; INFO items acted on are folded into the row they share a passage with.

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | accessibility/undefined-terms | new-pattern | Glossed "areas" as "read-together note sets" (the areas note's own definition) | fixed |
| 2 | accessibility/undefined-terms | new-pattern | Linked and glossed first body use of "collection" | fixed |
| 3 | accessibility/undefined-terms | new-pattern | Glossed "workshop artifacts" at first mention | fixed |
| 4 | accessibility/unidentified-references | stale-paths | Identified `WRITING.md` as Commonplace's former writing guide, since replaced by per-collection contracts | fixed |
| 5 | prose/anthropomorphic-framing | new-pattern | "build a mental model" → "form an overview of the collection" | fixed |
| 6 | prose/confidence-miscalibration | hedge-strength-mismatch | "operational necessity" → "keeps index-scan discovery viable" / "has an operational role", with portioned loading named as the degraded fallback | fixed |
| 7 | prose/confidence-miscalibration | temporal-residue | ADR 003 material moved to past tense and marked superseded by ADR 025; dropped "exactly" from the footer | fixed |
| 8 | prose/confidence-miscalibration | hedge-strength-mismatch | Quality-scores note now "identifies a related limit from the candidate-evaluation side", not "the same threshold" | fixed |
| 9 | prose/mannered-prose | new-pattern | "work at full power" / "runs without friction" → "Neither operation needs partitioning" / "runs without sub-passes" | fixed |
| 10 | prose/orphan-references | stale-paths | Same edit as #4; the figure is now stated as the guide's split heuristic; "retrieval filters" quotation now points to the [note type](../../../types/note.md), where the convention lives | fixed |
| 11 | prose/source-residue | single-source-vocabulary | ~40 notes attributed to one KB's former guide as a heuristic, not as the boundary's setting | fixed |
| 12 | prose/source-residue | scope-narrowed | Library/workshop conclusion scoped to "a system whose candidate discovery scans the whole collection index, as `/connect` did under ADR 003" | fixed |
| 13 | semantic/grounding-alignment | temporal-residue | Same edit as #7; added that ADR 025 removed complete-index reads from agent discovery (its stated reason: dominant per-fork cost) | fixed |
| 14 | semantic/grounding-alignment | hedge-strength-mismatch | Same edit as #6 | fixed |
| 15 | semantic/grounding-alignment | — | Parent/child area layering conflicts with the areas note's "no specific cardinality or parent/child membership rule" | deferred |
| 16 | semantic/grounding-alignment | new-pattern | "volume/complexity distinction" → the context-efficiency note's own "feasibility face — soft degradation as the window fills" | fixed |
| 17 | semantic/underspecified-assertions | — | Boundary criterion (capacity vs productive use) is unresolved and the window-growth prediction depends on it | deferred |
| 18 | sentence/clause-packing | new-pattern | Split the library/workshop closing sentence; moved the workshop-note link after the claim | fixed |
| 19 | sentence/clause-packing | new-pattern | Split the window-growth sentence after "moves upward" | fixed |
| 20 | sentence/concept-attribution | new-pattern | Opening now says the areas note already draws the resolution difference; this note develops it. Footer updated to match | fixed |
| 21 | sentence/concept-attribution | new-pattern | Same edit as #16 for link text ("complexity costs" → "per-window degradation") | fixed |
| 22 | sentence/concept-attribution | new-pattern | Removed "isn't just about curation quality"; now says the workshop note grounds the separation in value trajectory and lifecycle | fixed |
| 23 | sentence/concept-attribution | new-pattern | Instruction-specificity footer now uses the target's tiers (always-loaded router → on-demand skill bodies → task docs) | fixed |
| 24 | sentence/framing-mismatch | — | Boundaries defined as fit limits while the window-growth argument uses a complexity mechanism (same choice as #17) | deferred |
| 25 | sentence/framing-mismatch | hedge-strength-mismatch | Same edit as #8; footer now "quality scores address a related limit" | fixed |
| 26 | sentence/misleading-link-text | new-pattern | Same edit as #20 | fixed |
| 27 | sentence/misleading-link-text | new-pattern | Same edit as #21 | fixed |
| 28 | sentence/stock-phrases | new-pattern | Deleted "The parent index is not a taxonomic convenience — it's a distinct operational layer…" | fixed |
| 29 | sentence/stock-phrases | new-pattern | Folded "isn't just hard to find — it's invisible…" into the preceding sentence as "so a note with a poor description drops out of every operation that works at index resolution" | fixed |
| 30 | kb/types/note | new-pattern | Added `## Scope` restating limits the note already states inline (boundary dependencies, description-quality assumption, widening gap as prediction) | fixed |
| 31 | kb/theory/COLLECTION | stale-paths | Scoped the named Commonplace choices: `WRITING.md` (#4), `kb/theory/` → "the main collection (then `kb/notes/`)", `index.md` → `kb/notes/dir-index.md` | fixed |
| 32 | kb/theory/COLLECTION | temporal-residue | Same edit as #7 (ADR dated 2026-03-05, superseded by ADR 025) | fixed |
| 33 | kb/theory/COLLECTION | new-pattern | ADR 003 footer label `evidenced-by` → `abstracted-from`, phrase says the consequence was built from it | fixed |
| 34 | kb/theory/COLLECTION | new-pattern | Footer labels `foundation` → `grounds` (context efficiency) and `parallel` → `contrasts` (instruction specificity) | fixed |

INFO items also acted on: "reliably detect" in the opening (confidence INFO); ADR 003 glossed as an architecture decision record (unidentified-references INFO); virtuous cycle explained inline (undefined-terms INFO); line 33 now says which operations move to index resolution and names titles as well as descriptions (framing-mismatch INFO). INFO items not acted on: "namespace" in an open question; `title-as-claim` trait; `extends` label for the quality-scores link; softening "are operationally distinct layers" (bound up with deferred #15).

### Warning-to-fix mapping

- **#1:** "'areas' ... is never defined."
- **#2:** "'collection' is an active vocabulary term ... with neither a gloss nor a link."
- **#3:** "'workshop' ... Its first mention ... has no gloss."
- **#4:** "`WRITING.md` ... appears without identification."
- **#5:** "'Mental model' implies an internal representation the note does not mean to defend."
- **#6:** "'Library/workshop separation is an operational necessity' overstate[s] the note's own inference ... ADR 003 lists [portioned loading] as a fallback."
- **#7:** "The note describes a superseded mechanism in the present tense ... and 'exactly' claims a tighter fit."
- **#8:** "'identifies the same threshold from the other direction' ... is stronger than its source."
- **#9:** "'Both operations work at full power' and 'the virtuous cycle ... runs without friction' use energy and mechanical images."
- **#10:** "'WRITING.md sets this at ~40 notes' ... its source is an unlinked bare filename."
- **#11:** "The general definition of the full-text boundary is anchored to a local artifact."
- **#12:** "The heading ... states a general conclusion, but the section that follows is about one system."
- **#13:** "The note treats a superseded ADR as current behaviour."
- **#14:** "'Operational necessity' claims more than ADR 003 says."
- **#15:** "The parent/child area model conflicts with the cited areas note."
- **#16:** "The footer credits the context-efficiency note with a distinction it does not draw."
- **#17:** "The criterion that defines each boundary is unresolved, and the note's prediction about growing context windows depends on it."
- **#18:** Line 57 sentence of ~42 words with an eight-word linked title between subject and verb.
- **#19:** Line 17 sentence chains five clauses.
- **#20:** "The 'But…' contrast therefore credits the target with a gap it no longer has."
- **#21:** "The target has no volume/complexity distinction."
- **#22:** "the 'curation quality' contrast points to the wrong source."
- **#23:** "The parenthetical paraphrase does not match the target's tiers."
- **#24:** "The volume framing in the definition does not match the complexity mechanism the argument uses."
- **#25:** "Framing it as the index boundary narrows the quality-scores rationale."
- **#26:** "The surrounding sentences ... present this note's contribution as a correction of something the target does not claim."
- **#27:** "'complexity costs' ... point[s] to a distinction the target does not draw."
- **#28:** "The 'taxonomic convenience' foil is not set up anywhere in the note. Deleting the sentence loses nothing."
- **#29:** "This sentence only restates that point in dramatic form."
- **#30:** "The note has known limits but no `## Scope` section."
- **#31:** "The body names Commonplace choices without scoping them."
- **#32:** "The note describes the superseded ADR 003 as present Commonplace state."
- **#33:** "Origin is not corroboration ... The link should be `abstracted-from`."
- **#34:** "`foundation` ... and `parallel` ... are not in the label table."

### Verification notes

- `WRITING.md` does not exist in the current tree. History shows it existed as `kb/WRITING.md` when the note was written (commit ccaa0df27, 2026-03-08); its split guidance read "Split when an index exceeds 40 notes — that's the approximate point where an area stops fitting in working context", and it called the description "a retrieval filter, not a summary". It moved to `kb/instructions/WRITING.md` and was deleted in c55e8faf5 (2026-04-12), replaced by per-collection `COLLECTION.md` files. The retrieval-filter convention now lives in `kb/types/note.md`. The attribution was accurate but stale, so it was rescoped, not removed.
- ADR 003 has `status: superseded`, superseded by ADR 025 (`025-complete-generated-indexes-are-build-time-only.md`, accepted 2026-06-09). ADR 025 retires complete generated listings from the agent read path. It states that ADR 003's curation-plus-portioned-loading bet "no longer holds" because the complete-index read became the dominant per-fork cost.
- ADR 003 names `kb/notes/dir-index.md` and `kb/notes/`, not `index.md` or `kb/theory/`.

### Rejected findings

- (none)

### Deferred items

- **#15 (grounding: parent/child layering).** Affected passage: section "Parent/child area relationships are operationally distinct layers" and its two bullets. The claim is that parent areas operate at index resolution and child areas at full-text resolution. The cited areas note says "bounded context does not imply any specific cardinality or parent/child membership rule", and ADR 004 replaced parent/child `areas:` membership. Acceptable responses: (a) reframe the section as one optional implementation (a parent index at index resolution over child cohorts sized for full-text comparison) and acknowledge the areas note and ADR 004; (b) keep the claim and argue why the two-boundary model overrides the areas note's position; (c) drop the section. Each changes the note's claim or structure, so this pass cannot choose.
- **#17 and #24 (underspecified boundary criterion / framing mismatch).** Affected passages: the two boundary definitions ("can be loaded together") and the window-growth paragraph, plus "stops fitting productively" in the top regime. The choice is which criterion defines the boundaries: (a) capacity (token fit) for both, with a separate statement that productive-use limits bind earlier for full text; or (b) productive use for both, in which case the claim that the index boundary moves upward with window size, and the widening-gap prediction, need separate support or weakening. Either choice changes the note's definitions and its central prediction, so it is a substantive author decision.

### New patterns

- **gloss-at-first-use** (#1–#3): add a short inline gloss, and a definition link for registered vocabulary, at first use of an undefined term.
- **literal-replacement** (#5, #9): replace an anthropomorphic or figurative phrase with the literal operation it stands for.
- **attribution-to-target-terms** (#16, #20–#23, #26, #27): restate what a linked note says in that note's own terms when the note credits it with a distinction or gap it does not have.
- **sentence-split** (#18, #19): split an over-packed sentence at its main relation without dropping content.
- **stock-phrase-removed** (#28, #29): delete or fold an "isn't just X — it's Y" sentence that fails the deletion test.
- **scope-section-added** (#30): restate inline limits under `## Scope` to satisfy the note type.
- **link-label-corrected** (#33, #34): replace an off-vocabulary or corroboration-implying footer label with one from the collection's label table.

### Re-review

Run `kb/reports/state/review/runs/20261112T075538Z` (`commonplace-review run gates … --profile opus`, 15 criteria: every worked gate plus `type` and `collection`). Counts: 15 reviewed, 0 problem, 0 out-of-attempts, not stopped, guard clean, exit 0.

| Pair | Before | After |
|---|---|---|
| accessibility/undefined-terms | warn | warn |
| accessibility/unidentified-references | warn | pass |
| prose/anthropomorphic-framing | warn | pass |
| prose/confidence-miscalibration | warn | warn |
| prose/mannered-prose | warn | pass |
| prose/orphan-references | warn | pass |
| prose/source-residue | warn | warn |
| semantic/grounding-alignment | warn | pass |
| sentence/clause-packing | warn | warn |
| sentence/concept-attribution | warn | pass |
| sentence/framing-mismatch | warn | warn |
| sentence/misleading-link-text | warn | pass |
| sentence/stock-phrases | warn | pass |
| kb/types/note | warn | pass |
| kb/theory/COLLECTION | warn | warn |

`semantic/underspecified-assertions` (only deferred #17) was not re-reviewed; its result is now stale.

Remaining warnings. They are new findings, not ones this pass left open, except framing-mismatch:
- **undefined-terms:** `/connect` and "library" not glossed; the gloss for "workshop" comes before its link.
- **confidence-miscalibration:** the rewritten #29 sentence ("the only content those operations see", "drops out of every operation") ignores body-level search as a channel.
- **source-residue:** open questions still name "the KB" and its "current flat index" (stale since ADR 025) and `/connect`. The library/workshop section is still mostly ADR 003 history and does not state the general mechanism first.
- **clause-packing:** three sentences introduced by this pass's edits (#7, #8 and #9) are over-packed: the ADR 003 opener, the quality-scores sentence and the virtuous-cycle sentence.
- **framing-mismatch:** the boundary-definition finding is deferred item #17/#24 and stays open.
- **COLLECTION:** `extends` label on the quality-scores link (now "related limit"); the "current flat index" open question; the missing `title-as-claim` trait.

## Fix Report: two-context-boundaries-govern-collection-operations — second pass (2026-11-12)

Source results: 8 fresh `warn` pairs after the all-gates sweep `kb/reports/state/review/runs/20261112T082018Z` (profile `opus`; 44 pairs, 36 pass, 8 warn, 0 fail). Five result files date from run `20261112T075538Z` and stayed fresh (undefined-terms, confidence-miscalibration, source-residue, clause-packing, framing-mismatch). Three are new from `20261112T082018Z` (load-bearing-qualifiers, underspecified-assertions, parsing-ambiguity). Numbering continues from the first pass.

Operator direction for this pass: "collection" in this note is not a binding Commonplace term. The general subject is a bounded subset of a knowledge base that an agent reads as a unit, where a knowledge base is a general category of software and Commonplace's collections are one application. The title and filename stay unchanged; a retitle goes through `commonplace-relocate-note` in its own commit.

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 35 | accessibility/undefined-terms | new-pattern | Glossed `/connect` at first use: "finds existing notes that a given note should link to" | fixed |
| 36 | accessibility/undefined-terms | new-pattern | Glossed "library" as the curated main collection, where everything is worth connecting against (ADR 003's library principle) | fixed |
| 37 | accessibility/undefined-terms | new-pattern | First meaningful mention of "workshop" now carries both the gloss and the link | fixed |
| 38 | prose/confidence-miscalibration | boundary-case-acknowledged | Middle-regime passage: candidate discovery narrowed to "index-scan candidate discovery"; a poorly described note is "effectively lost to operations that work at index resolution", reachable only through body-level search | fixed |
| 39 | prose/source-residue | unframed-domain-examples | Open questions generalized: "a knowledge base", flat index until index-resolution operations degrade (dropped the stale "current flat index"); whole-collection candidate discovery, with `/connect` under ADR 003 named as one instance | fixed |
| 40 | prose/source-residue | unframed-domain-examples | Library/workshop section now states the general mechanism first and introduces ADR 003 as the historical case it was abstracted from; the old closing conditional moved to the top | fixed |
| 41 | semantic/load-bearing-qualifiers | new-pattern | Removed the registered-definition link and gloss from the full-text boundary definition; added a paragraph stating the general subject once and treating "collection" as ordinary English; description updated (see below) | fixed |
| 42 | semantic/load-bearing-qualifiers | — | Gate's proposed retitle to "…operations on read-together note sets" | deferred |
| 43 | semantic/underspecified-assertions | boundary-case-acknowledged | Framing only, no side chosen: Scope says the widening-gap prediction depends on an open criterion (full-text set by productive use while index tracks fit, or index scanning degrading less) and needs separate support otherwise; added an open question on which criterion sets each boundary. The definitional choice stays deferred (#17/#24) | fixed |
| 44 | sentence/clause-packing | new-pattern | Split the ADR 003 opener: identification and status, then the `/connect` gloss, then the design claim | fixed |
| 45 | sentence/clause-packing | new-pattern | Quality-scores sentence: condition completes first; the candidate-list contents go in a second sentence | fixed |
| 46 | sentence/clause-packing | new-pattern | Virtuous-cycle sentence: split after "most productive"; the cycle's mechanism follows the verb after a colon | fixed |
| 47 | sentence/framing-mismatch | — | Full-text boundary defined as fit, while the window-growth argument uses degradation; this is deferred #17/#24 again | deferred |
| 48 | sentence/parsing-ambiguity | new-pattern | "proposed portioned loading when it wasn't" → "proposed portioned loading as the fallback for when the index outgrew that size"; "worked only while" | fixed |

INFO items not acted on: "per-window degradation" gloss (undefined-terms); "usually needs full note bodies" (load-bearing-qualifiers INFO); the `WRITING.md` sentence and first strategy bullet reorderings (clause-packing INFO); conditional heading for the library/workshop section (framing-mismatch INFO).

### Warning-to-fix mapping

- **#35:** "`/connect` first appears ... without saying what the skill does."
- **#36:** "'Library' in 'Library/workshop separation' ... is never glossed."
- **#37:** "The criterion asks for both the gloss and the link at first meaningful mention."
- **#38:** "'the only content those operations see' ... 'drops out of every operation' ... ignores body-level search", which ADR 003 kept as a secondary channel.
- **#39:** "Open questions are framed as questions about this KB's current tooling ... the 'current flat index' premise reads as residue."
- **#40:** "The general mechanism ... appears only after the source-specific detail."
- **#41:** "'Collection' ... is not load-bearing ... No step of the argument uses the subtree or the text contract."
- **#42:** Same finding; suggested title "Two context boundaries govern operations on read-together note sets".
- **#43:** "The boundary criterion is unresolved between raw fit and productive use, and the asymmetry argument depends on it."
- **#44–#46:** Three sentences with long subject–verb interruptions while another dependency is open (ADR 003 opener, quality-scores sentence, virtuous-cycle sentence).
- **#47:** "A reader who applies the definition will predict the opposite of the note's claim in the 'As context windows grow' paragraph."
- **#48:** "The `when it wasn't` clause can attach to 'proposed' ... [and] would wrongly suggest that the index had already outgrown a single read when ADR 003 was written."

### Generalization of "collection" and the description

- New second paragraph of the opening: the model applies to knowledge bases in general. Its subject is any bounded subset of a knowledge base that an agent reads as a unit (an area, a directory, a tag slice, a query result, or a whole small knowledge base). The note calls this a collection "in the ordinary sense of the word". It links [Commonplace's collections](../reference/definitions/collection.md) only as one application, whose subtree and text-contract properties the argument does not use. That link names an application. It does not bind the subject.
- The first-pass link and gloss on "collection" in the full-text boundary definition were removed. Every later use reads correctly in the ordinary sense, so no other occurrence was replaced. "Main collection" in the library/workshop section is ordinary English for a KB's curated core, and "sub-collection" in the parent/child section is ordinary English for a split subset.
- Description: the load-bearing-qualifiers finding's suggested revision targets the description. In this KB, an unlinked "collection-size regimes" in a retrieval filter reads in the registered sense that the body now disclaims. Following fix-descriptions, I made the smallest change: "three collection-size regimes with different consequences for …" → "three size regimes for any note set an agent reads as a unit, with consequences for …". The mechanism and the consequence list are kept, and the new description is 219 characters, one clause with no terminal punctuation.

### Rejected findings

- (none)

### Deferred items

- **#42 (retitle).** The title "Two context boundaries govern collection operations" and the filename stay. The gate proposed "Two context boundaries govern operations on read-together note sets". Recommendation: adopt that title through `commonplace-relocate-note` in its own commit. It reuses the areas note's own name for the subject (an area is a read-together set), drops the word the body now has to disclaim, and keeps the claim the same. An alternative closer to the operator's wording is "Two context boundaries govern operations on bounded knowledge-base subsets", but it is longer and does not echo the areas note. After a retitle, the description's "any note set an agent reads as a unit" could be shortened.
- **#47, with #17/#24 (boundary criterion).** This is unchanged from the first pass and still undecided by the operator. #43 made the dependency explicit, which this pass could do without choosing a side. The definitions still say "can be loaded together". Recommendation: option (a′), define the full-text boundary by productive use and the index boundary by fit. This is the reading the window-growth argument already uses (the reviewer's "Reading C"). The asymmetry question added to the open questions would then become the stated assumption. Note that framing-mismatch now passes, but the finding remains valid until the definitions change.
- **#15 (parent/child layering against the areas note).** Not re-raised as a warning this pass; grounding-alignment repeats it only as INFO. It is still undecided. My recommendation remains option (a): reframe the section as one optional implementation and acknowledge the areas note and ADR 004.

### New patterns

- **gloss-at-first-use** (#35–#37): 6 instances across both passes. This meets the 3+ threshold for taxonomy promotion.
- **sentence-split** (#44–#46): 5 instances across both passes. This meets the threshold.
- **unneeded-restriction-unbound** (#41): drop a registered-term binding from a subject the argument does not need it for, state the general subject once, and keep the specific system as one application.
- **attachment-disambiguated** (#48): rewrite a trailing clause so it can attach only to its intended head.

### Re-review

Run `kb/reports/state/review/runs/20261112T082659Z` (`commonplace-review run gates … --all-gates --profile opus`; freshness selected the pairs). Counts: 41 reviewed, 3 fresh and skipped (frontmatter/claim-strength, title-as-claim and title-composability, which watch only the unchanged title), 0 problem, 0 out-of-attempts, not stopped, guard clean, exit 0. Final status: 44 pairs, all fresh, 36 pass, 8 warn, 0 fail.

Worked pairs:

| Pair | Before | After |
|---|---|---|
| accessibility/undefined-terms | warn | warn |
| prose/confidence-miscalibration | warn | pass |
| prose/source-residue | warn | pass |
| semantic/load-bearing-qualifiers | warn | pass |
| semantic/underspecified-assertions | warn | pass |
| sentence/clause-packing | warn | warn |
| sentence/framing-mismatch | warn | pass |
| sentence/parsing-ambiguity | warn | warn |

Previously passing pairs that now warn:

| Pair | Before | After | Finding |
|---|---|---|---|
| complexity/framework-decoration | pass | warn | The ADR 003 three-bullet strategy list now restates the new opening paragraph of the library/workshop section, and its semantic-search item goes unused. This was caused by #40. |
| prose/mannered-prose | pass | warn | "a neighbouring shape to the index/full-text resolution gradient" in the instruction-specificity footer annotation. That text is unchanged since the first pass, so this is reviewer variance. |
| prose/proportion-mismatch | pass | warn | The library/workshop section is now the longest unit and is mostly ADR 003 history. It duplicates the workshop gloss and the workshop-note pointer. #36, #37, #40 and #44 added to it. |
| semantic/grounding-alignment | pass | warn | "Keeps index-scan discovery viable" rests on ADR 003's bet, which ADR 025 says failed. The note should say "delays" rather than "keeps" and reconcile per-fork cost with the index boundary. #40 made the claim more prominent by moving it to the top. This is a claim-strength change, so it needs operator review before a fix. |
| kb/theory/COLLECTION | pass | warn | The `extends` label on the quality-scores footer link. This was INFO in the first pass and was left alone there; the label is unchanged. |

All other re-reviewed pairs passed: 33 pairs, every catalog gate not listed above plus `kb/types/note`.

Remaining warnings and their source:
- **undefined-terms:** new findings: "candidate discovery" is used before its gloss; also "text-contract properties", "per-fork cost" and "portioned loading". The first comes from #38's wording, the second from #41's paragraph.
- **clause-packing** and **parsing-ambiguity:** both flag #38's rewritten sentence "…effectively lost to operations that work at index resolution and can be reached only through body-level search", where the trailing predicate can attach to "operations". The fix is to split it: "A note with a poor description is therefore effectively lost to operations that work at index resolution; it can be reached only through body-level search." Clause-packing also flags the repeated workshop gloss in the first strategy bullet.
- **framework-decoration**, **proportion-mismatch** and **grounding-alignment:** all point at the library/workshop section. The reviewers suggest collapsing the ADR 003 history and the bullet list into two or three sentences and restating the consequence as a delay. Grounding-alignment changes claim strength, and proportion-mismatch would remove the quality-scores paragraph, so the next pass should take operator direction on that section.
- **mannered-prose** and **COLLECTION:** footer annotation and label wording only; both are framing fixes for a next pass.
