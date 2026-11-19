## Fix Report: a-software-factory-is-family-scoped-lifecycle-production-machinery

### Outcome and authority

One bounded pass: **14 findings across 8 fresh criteria; 8 fixed, 0 rejected, 6 deferred.** “Fixed” records an applied correction, not a new review verdict. Closing review is **pending**: the parent will rerun **all gates with Sol** after both fixers finish. No review, subagent, or commit was launched.

Only the target note and this report were written. Claims, argument order, source links, description, and unrelated passages were preserved. The arrow diagram was rendered in equivalent prose; one redundant footer link was removed while its inline link and argument were retained. No sections were regrouped. The note had no `user-verified` field.

- Target: `kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md`
- Original sweep: `kb/reports/state/review/runs/20261112T080231Z`
- Review model: `gpt-6.1-sol`; fixer model: `gpt-6.1-sol`.
- Instructions: current `kb/instructions/FIX-SYSTEM.md`, `kb/instructions/fix-warnings/fix-review-warnings.md`, and fix-strategy taxonomy; theory and reports collection contracts; note type; writing and validation skills.
- User deviation: no closing review in this worker; substantive claim, structure, source, and placement choices return to the parent/operator.
- Entry query: `commonplace-review status kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md --fresh --outcome warn fail --json`. All eight rows below were fresh, with `changed: []`. No existing fix report was present.
- Exact pre-edit file SHA-256: `3f257c2f0eaf5692058bd6a069d2369be3bff54ebb7dec4f83a69220e7dc91b3`.
- Exact post-edit file SHA-256: `f4dee748bce52437ff68f4d869d0e6fc751634016e471a7f12b0ccae36fadadd`.
- Body-watching gate results recorded `note-sha256: 8dcc978ed1e84f00c0e829edb88548fd92b95a9451124b55289b0a73f05d2511`; the type/collection results recorded the pre-edit full-file hash above. Freshness was established by the status query, not by comparing different watched-part hashes manually.

### Original results

These are the original replaceable result paths. The finding text is retained below so this report remains usable after the closing sweep overwrites them.

| Criterion | Original outcome | Finding IDs | Original result path |
|---|---|---|---|
| `accessibility/undefined-terms` | warn | 1–2 | `kb/reports/state/review/results/kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md/accessibility/undefined-terms.md` |
| `accessibility/unidentified-references` | fail | 3–4 | `kb/reports/state/review/results/kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md/accessibility/unidentified-references.md` |
| `complexity/connection-inflation` | warn | 5 | `kb/reports/state/review/results/kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md/complexity/connection-inflation.md` |
| `prose/pseudo-formalism` | warn | 6 | `kb/reports/state/review/results/kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md/prose/pseudo-formalism.md` |
| `semantic/grounding-alignment` | fail | 7–9 | `kb/reports/state/review/results/kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md/semantic/grounding-alignment.md` |
| `structural/bullet-capitalization` | fail | 10–11 | `kb/reports/state/review/results/kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md/structural/bullet-capitalization.md` |
| `kb/types/note` | warn | 12 | `kb/reports/state/review/results/kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md/kb/types/note.md` |
| `kb/theory/COLLECTION` | fail | 13–14 | `kb/reports/state/review/results/kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md/kb/theory/COLLECTION.md` |

### Dispositions

| # | Check | Strategy | Summary | Status |
|---|---|---|---|---|
| 1 | accessibility/undefined-terms | new-pattern | Glossed “viewpoints” at first occurrence in the schema row | fixed |
| 2 | accessibility/undefined-terms | new-pattern | Replaced “closed algebra” with the intended literal limitation | fixed |
| 3 | accessibility/unidentified-references | new-pattern | Identified Tool Factory and MDSoFa inline using the linked construction note | fixed |
| 4 | accessibility/unidentified-references | new-pattern | Gave Greenfield and Short's full names and identified them as authors of the reconstructed accounts | fixed |
| 5 | complexity/connection-inflation | new-pattern | Removed only the duplicate construction/acquisition footer entry | fixed |
| 6 | prose/pseudo-formalism | new-pattern | Replaced the heterogeneous-arrow chain with equivalent prose | fixed |
| 7 | semantic/grounding-alignment | — | Dynamic schema and individual-solution schema variation lack retained source passages | deferred |
| 8 | semantic/grounding-alignment | — | Integration-program/functions and 2003 schema-constraint details lack retained source passages | deferred |
| 9 | semantic/grounding-alignment | — | Book-preview integration claim has no retained quotations | deferred |
| 10 | structural/bullet-capitalization | new-pattern | Capitalized the five family-knowledge bullets | fixed |
| 11 | structural/bullet-capitalization | new-pattern | Capitalized the six non-implication bullets | fixed |
| 12 | kb/types/note | — | Grouping existing limits under Scope is a structural choice reserved to the parent/operator | deferred |
| 13 | kb/theory/COLLECTION | — | Historical reconstruction versus transferable theory is a placement/contribution decision | deferred |
| 14 | kb/theory/COLLECTION | — | Invalid `compares` label has no direct authorized synonym preserving the stated similarity | deferred |

### Warning-to-fix mapping and retained findings

1. **Undefined terms, warning:** The schema row introduces “family viewpoints” without explaining the organizing concept; the review proposed “perspectives that organize descriptions of a system around particular stakeholder concerns.” Added “perspectives organized around stakeholder concerns” at the first occurrence. The 2007 ingest's retained “Architecture Frameworks” extract explicitly associates a viewpoint with stakeholder concerns, related artifacts, activities, and assets. This gloss does not transfer the later schema's activities/assets into the 2003 account. The separately flagged 2003 constraints claim remains untouched and deferred (#8).
2. **Undefined terms, warning:** “Greenfield does not supply a closed algebra of these operations” does not explain what formal account is absent. Replaced only that sentence with “Greenfield does not give formal rules specifying how these operations combine and what their combinations produce.” This states the same limitation literally; it does not introduce a new formalism or change the operation distinctions.
3. **Unidentified references, FAIL:** “Greenfield, Cook and Kent, and MDSoFa” mixes people and a system without identifying the latter references. Replaced the list with Greenfield's factory-building example, Cook and Kent's Tool Factory proposal for generating language-development tools, and Langlois and Exertier's MDSoFa, a model-driven software-factory producer. Evidence: the linked `kb/theory/factory-construction-does-not-establish-knowledge-acquisition.md`, especially its Tool Factory and MDSoFa sections, describes exactly those roles. The original source links are unchanged; no additional external source dependency was introduced.
4. **Unidentified references, WARN:** The opening supplies only Greenfield and Short's surnames and dates, without identifying their role in the approach. It now identifies Jack Greenfield and Keith Short as the authors of the 2003 paper and Greenfield as the author of the 2007 account. The suggestion to call them “architects of the method” was not adopted: that additional historical characterization would need source support beyond the retained Quotes. Author identification is sufficient for the local reference repair.
5. **Connection inflation, WARN:** The construction/acquisition footer entry repeats the inline paragraph's link and explanation; its `extends` label adds no navigation or relationship information. Removed that one footer entry. Retained the inline link, its construction-versus-acquisition explanation, and the other three footer entries. This is not removal of an example or argument.
6. **Pseudo-formalism, WARN:** The opening chain uses identical `->` arrows for scope, organization, packaging, configuration, use, and representation without defined semantics; the review suggested a prose bridge. Replaced only the chain and its introduction with two sentences retaining family scope, factory development, schema/assets, configured environment, solution development, and member lifecycle work products. The retained 2003 configured-IDE/schema/template extracts and 2007 assets/two-process extracts support these same relationships. No argument was reorganized.
7. **Grounding, FAIL:** The 2007 Quotes do not establish a dynamic schema or changing a schema for an individual solution. This affects the 2007 schema cell and the paragraph beginning “Greenfield also describes changing a dynamic schema…”; it supports the distinction between member-specific variation and reusable factory specialization. Deferred; see choices below.
8. **Grounding, FAIL:** The four-technique integration program and its constituent functions are not established by the retained passages. The 2003 schema passage also does not retain support for associated constraints. This affects “Model-driven development is therefore…” and the 2003 schema cell. Deferred; see choices below.
9. **Grounding, FAIL:** The 2004 book-preview link affirmatively confirms the broad integration program although its Quotes section has no retained source quotations. The note's caution about detailed ontology does not repair that narrower affirmative use. Deferred; see choices below.
10. **Bullet capitalization, FAIL:** All five family-knowledge bullets start with ordinary lowercase prose (“family,” “schema,” “processes,” “tools,” “reusable”). Capitalized exactly those initial words; retained list contents and punctuation.
11. **Bullet capitalization, FAIL:** All six non-implication bullets start with lowercase “that.” Changed each to “That”; retained the propositions and punctuation.
12. **Note type, WARN:** Known limits appear under “What the imported ontology does not establish” and “Evidence limits,” not the required `## Scope`. The review proposes putting both under Scope with their titles retained as subheadings. Deferred as a section-hierarchy choice, not rejected as inapplicable.
13. **Theory collection, FAIL:** Description, opening, and tables reconstruct Greenfield's historical arrangement rather than establish a separate design-space claim surviving that scoping. The review proposes relocation to an external-system collection or independently arguing a substantive theory claim. Deferred; neither is a framing-only fix.
14. **Theory collection, WARN:** The final footer entry uses `compares`, absent from authorized labels. Its phrase expresses similarity between configured arrangements. Verified against the current theory contract: `compares` is absent; `contrasts` serves a neighboring-shape distinction, not a direct synonym for this similarity, and `see-also` is not authorized for theory destinations. Deferred rather than falsely relabeling the relation or moving/deleting it without a structural/relationship decision.

### Evidence and mechanism checks

Read all eight result files and the target note fully. Read the linked construction/acquisition note and all three direct ingests; only their Quotes sections were treated as external claim support, under the current grounding gate. The 2007 Quotes include environment/assets, template packaging, viewpoint concerns, two development processes, specialization, and composition. They omit the dynamic-schema/member-specific-variation and complete integration-program passages. The 2003 Quotes include the schema graph, DSL editing/transformation, configured IDE, production assets/developers, factory-building example, and family scope; they omit associated schema constraints. The preview explicitly says “No source quotes have been retained yet.” Ingest summaries and analysis were not substituted for missing source passages.

The three exact name-paired snapshot files exist, checked with `Path.exists()`. Their contents were **not** opened, and their hashes/source identities were **not** verified: no linked ingest was marked `(snapshot required)`, no earlier grounding route authorizing that marker was supplied, and selecting/creating a new source route is outside this pass. File existence does not establish support. None of the fresh findings alleged a stale file path; no paths or historical mechanisms were removed on an assumption of staleness. The source-mechanism findings above concern insufficient retained evidence, not demonstrated historical falsity.

A single targeted repository backlinks search confirmed dependent definitions and notes that rely on this historical ontology. They were not edited. No broad graph-discovery pass was run.

### Rejected findings

None. No evidence warranted treating a finding as spurious. In particular, the missing Quotes are real support gaps under the declared route, even if a fuller source might ultimately substantiate the history.

### Deferred items: exact decisions required

- **#7 — Dynamic schema and solution-specific variation.** Affected passages: 2007 schema cell (“dynamic, family-specific architecture framework”) and the paragraph under “Factory development and solution development update different things” that attributes individual-solution schema changes to Greenfield and uses them to distinguish solution development from specialization. Choose between (a) a separately authorized grounding run retaining the relevant 2007 extracts, (b) a valid snapshot-required route returned by the grounding procedure, or (c) narrowing/removing the attribution and reconsidering the resulting distinction. The present specialization extract concerns base-factory viewpoints only. This fixer cannot choose new source work or alter a load-bearing claim.
- **#8 — Integration program, constituent functions, and 2003 constraints.** Affected passages: the paragraph beginning “Model-driven development is therefore…” and the schema cell's “constraints.” Choose between separately retaining source extracts for each historical detail, a valid grounding-authorized snapshot route, or narrowing/removing unsupported details while preserving a warranted argument. The retained material supports parts of the program, not the complete four-technique/function account. Deleting details or recasting them as this note's inference is a source/claim decision, not an accuracy correction established by the available evidence.
- **#9 — Book-preview affirmative use.** Affected passage: opening evidence paragraph, “confirms the book and its broad integration program.” Choose between retaining relevant preview quotations through separate source work or reducing/removing its affirmative evidential use; a snapshot route would require the prescribed grounding decision and identity/hash checks. No retained quotation presently supports the claim. The local pass has no authority to write the ingest or select a replacement evidential route.
- **#12 — Scope hierarchy.** Affected headings: `## What the imported ontology does not establish` and `## Evidence limits`. Acceptable responses include authorizing the proposed `## Scope` parent with both existing headings demoted, or selecting another hierarchy that puts the known limits under Scope without losing distinctions. The user reserved structural decisions; no section hierarchy was changed merely to satisfy a gate.
- **#13 — Intended contribution and placement.** Affected artifact: description, opening, historical comparison tables, and the ontology's role for inbound dependents. Choose the appropriate descriptive collection and perform an authorized relocation with backlink handling, or commission a separate independently argued theory contribution. This pass cannot select a collection, rename/move the note, rewrite its purpose, or alter dependents. It cannot resolve the placement objection by cosmetic claim language.
- **#14 — Similarity relation.** Affected entry: final footer link to `the-deployed-system-not-the-model-is-the-unit-of-learning.md`, currently labeled `compares`. Choose whether to preserve the similarity in ordinary inline prose, remove the optional relationship, or establish a genuinely fitting authorized relationship based on a separate assessment. The contract must not be edited in this pass. A mere replacement with `contrasts` would change the asserted relation, not fix its spelling. This remains a known vocabulary defect pending the owner's relationship/structure choice.

### New patterns

All applied fixes are `new-pattern`: the existing taxonomy does not name these accessibility, redundancy, notation, or capitalization repairs. No taxonomy file was changed.

- **Term gloss / literal terminology:** #1–2 explain specialized terms without changing the represented distinction.
- **Inline reference identification:** #3–4 identify named authors and mechanisms without broadening historical claims.
- **Duplicate-edge removal:** #5 removes redundant footer navigation while retaining the substantive inline relationship.
- **Literal diagram rendering:** #6 expresses heterogeneous arrow relationships in prose without changing their content.
- **Bullet capitalization:** #10–11 capitalize prose fragments without changing propositions.

### Validation

Command (exit 0):

```text
commonplace-validate kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
```

Exact output:

```text
VALIDATION SUCCESS
Target: kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
Scope: kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects

Details: commonplace-validate --full kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
```

`git diff --check -- kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md` also exited 0 with no output. Re-read the entire edited note and reviewed its diff. No pytest was run: only Markdown content changed, not code or fixtures.

### Closing review and next steps

**PENDING — parent-owned all-gates Sol rerun after both fixers finish.** No new criterion outcomes are claimed, including for originally passing pairs. The body edit stales body-watching results; the parent must ask all gates, not only the eight worked criteria, and let freshness select the work. The six deferred findings remain unresolved even though deterministic validation succeeds.

For broader graph discovery after the reserved decisions are resolved, `cp-skill-connect` is the writing workflow's suggested next step, not an action authorized or run in this bounded pass.

### Closing-review evidence appended by trace audit — 2026-11-12

This appendix records the later parent-owned sweep; it does **not** replace the original findings, local dispositions, or six deferred decisions above. Audit: `/tmp/commonplace-review-check/trace-audit.md`.

- Closing run: `kb/reports/state/review/runs/20261112T082159Z`; report: `/tmp/commonplace-review-check/closing.json`.
- This note: **40 pairs re-reviewed, 4 reused fresh; all 44 currently fresh; 38 PASS, 5 WARN, 1 FAIL**. Initial: 36 PASS, 4 WARN, 4 FAIL. All result files record model `gpt-6.1-sol`; new review launches record Codex medium effort. The four reused frontmatter results retain initial PASS outcomes; null outcomes on closing JSON's fresh rows are not unknown verdicts.
- Both notes together: 80 reviewed + 8 reused; all 88 fresh, no orphans, confirmed by read-only status during the audit. Closing command exited 1 because its checkout guard saw the unrelated `kb/theory/two-context-boundaries-govern-collection-operations.md` change, not missing pairs or failed launches. The guard does not attribute the change to a worker.
- Current note full-file SHA-256: `f4dee748bce52437ff68f4d869d0e6fc751634016e471a7f12b0ccae36fadadd`, matching the closing captures and the original fixer's replayed edits.

#### Every applicable pair's closing outcome

Criterion IDs below resolve to current results under `kb/reports/state/review/results/kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md/<criterion-id>.md`. Exact initial outputs remain in run `20261112T080231Z`, independently of the replaced current result files.

| Criterion | Initial | Closing current | Closing action |
|---|---|---|---|
| `accessibility/jargon-persistence` | PASS | PASS | reviewed |
| `accessibility/notation-opacity` | PASS | PASS | reviewed |
| `accessibility/undefined-terms` | WARN | WARN | reviewed |
| `accessibility/unidentified-references` | FAIL | WARN | reviewed |
| `complexity/claim-to-section-ratio` | PASS | PASS | reviewed |
| `complexity/connection-inflation` | WARN | PASS | reviewed |
| `complexity/could-be-a-paragraph` | PASS | PASS | reviewed |
| `complexity/framework-decoration` | PASS | WARN | reviewed |
| `frontmatter/claim-strength` | PASS | PASS | reused fresh |
| `frontmatter/description-discrimination` | PASS | PASS | reused fresh |
| `frontmatter/title-as-claim` | PASS | PASS | reused fresh |
| `frontmatter/title-body-alignment` | PASS | PASS | reviewed |
| `frontmatter/title-composability` | PASS | PASS | reused fresh |
| `prose/anthropomorphic-framing` | PASS | PASS | reviewed |
| `prose/bridge-paragraph-duplication` | PASS | PASS | reviewed |
| `prose/confidence-miscalibration` | PASS | PASS | reviewed |
| `prose/mannered-prose` | PASS | PASS | reviewed |
| `prose/orphan-references` | PASS | PASS | reviewed |
| `prose/proportion-mismatch` | PASS | PASS | reviewed |
| `prose/pseudo-formalism` | WARN | PASS | reviewed |
| `prose/redundant-restatement` | PASS | PASS | reviewed |
| `prose/source-residue` | PASS | PASS | reviewed |
| `prose/unbridged-cross-domain` | PASS | PASS | reviewed |
| `semantic/completeness-boundary-cases` | PASS | PASS | reviewed |
| `semantic/conceptual-role-conflation` | PASS | PASS | reviewed |
| `semantic/epistemic-status-blur` | PASS | PASS | reviewed |
| `semantic/explanatory-reach` | PASS | PASS | reviewed |
| `semantic/grounding-alignment` | FAIL | FAIL | reviewed |
| `semantic/internal-consistency` | PASS | PASS | reviewed |
| `semantic/load-bearing-qualifiers` | PASS | PASS | reviewed |
| `semantic/underspecified-assertions` | PASS | PASS | reviewed |
| `semantic/unearned-generality` | PASS | PASS | reviewed |
| `semantic/unwarranted-scope` | PASS | PASS | reviewed |
| `sentence/clause-packing` | PASS | PASS | reviewed |
| `sentence/concept-attribution` | PASS | PASS | reviewed |
| `sentence/framing-mismatch` | PASS | PASS | reviewed |
| `sentence/misleading-link-text` | PASS | PASS | reviewed |
| `sentence/parsing-ambiguity` | PASS | PASS | reviewed |
| `sentence/stock-phrases` | PASS | PASS | reviewed |
| `structural/bullet-capitalization` | FAIL | PASS | reviewed |
| `structural/compound-bullet` | PASS | PASS | reviewed |
| `structural/general-before-specific` | PASS | PASS | reviewed |
| `kb/types/note` | WARN | WARN | reviewed |
| `kb/theory/COLLECTION` | FAIL | WARN | reviewed |

#### Remaining and newly reported findings

Launch IDs identify `kb/reports/state/review/runs/20261112T082159Z/calls/launches/<ID>/outputs/review.md`.

| Closing criterion / launch | Remaining or new finding; relationship to original work |
|---|---|
| `accessibility/undefined-terms` WARN / `e27202169d104ad691f645df90876be2` | **New findings within the same warning criterion:** lifecycle work products need an earlier concrete gloss; variation points and selecting/binding variation need explanation. Original viewpoint and closed-algebra findings #1–2 are no longer reported. The underlying terminology existed before the fix, although lifecycle work products now appear in the replacement prose bridge. |
| `accessibility/unidentified-references` WARN / `0c7e159641d8429793f340c196ca4830` | **New finding after original identifications:** the pre-existing Microsoft reference lacks an inline platform-vendor identification. Original author/Tool Factory/MDSoFa findings #3–4 are no longer reported. This appendix records the new reviewer finding without rejecting it or assigning a fix. |
| `complexity/framework-decoration` WARN / `99223f2f9e36478798faaf7fbdc685ff` | **Previously PASS criterion, now WARN:** the five-row development-process table repeats the family-machinery/member distinction; reviewer proposes prose while retaining boundary examples and the ontology table. This table was untouched. Initial review expressly found it useful for classification. This is judgment drift/newly reported criticism, not evidence of a newly inserted table. |
| `semantic/grounding-alignment` FAIL / `3c88f2be2a814f62a3729772b368645e` | Original #7–9 remain: no retained support for dynamic/member-specific schema variation; four-technique integration/functions; 2003 constraints; preview's affirmative evidential use. Closing separates these into four findings and **adds the stakeholder-concern gloss in the 2003 schema cell** to the 2003 support objection. See below. |
| `kb/types/note` WARN / `cd19b8152c3a4ddba2bcb9027004f35b` | Missing `## Scope` remains (#12). Closing proposes renaming Evidence limits, whereas initial review proposed grouping both limits sections. No structural choice was made. |
| `kb/theory/COLLECTION` WARN / `66640c54026e42fbbedca9655dacbb63` | Invalid `compares` remains (#14). **The original placement FAIL (#13) is no longer reported**, despite no relocation or independent theory-claim revision. Closing accepts the existing distinctions as a theory contribution. Original placement decision remains deferred. |

#### New grounding objection to an applied gloss

The fixer added “perspectives organized around stakeholder concerns” in the **2003 schema cell** while fixing #1. Its report supports that generic gloss from the **2007** Quotes. Closing grounding now says the retained **2003** passage establishes the graph/DSL transformations but not stakeholder concerns or constraints. The 2007 Quotes explicitly mention stakeholder concerns; the 2003 Quotes do not. Thus the gloss's location creates an unresolved version-attribution/support question even though the original accessibility finding is no longer reported. This is not a determination that the historical characterization is false, nor an automatic reversal of the original `fixed` disposition. A separate source or attribution decision is required.

Closing grounding also suggests retaining more quotations or marking links snapshot-required. That recommendation is **not** evidence that snapshot identity/hash/source checks occurred or permission to bypass the separate grounding decision. No snapshots were opened or verified by this fix pass, and no source work was performed by the audit.

#### Disappeared placement finding is not a completed decision

The collection verdict improved FAIL → WARN because closing review accepts the bounded historical distinctions for theory placement. The original contribution/placement question (#13) was expressly deferred; the description, historical scope, tables and argument remain materially the same. No relocation, independently argued replacement claim, or dependent-note edit occurred. Keep #13 open unless the parent/operator deliberately resolves it; the newer review alone does not supply that decision.

**All six original deferred items remain as recorded.** New findings have no disposition assigned by this appendix. No further note edit, review, source-grounding run, graph discovery, or substantive choice was performed by the audit.
