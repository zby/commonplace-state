## Fix Report: artifacts-produced-from-sources-need-lineage-recorded-at-the-source

`commonplace-warn-selector` returned 16 findings across 13 current warning review pairs. The table maps those pairs, including the older Claude title-alignment warning, plus all 18 required Luna results from completed jobs 6677–6717 (12 WARN, 6 FAIL).

| # | Review | Check | Strategy | Summary | Status |
|---|--------|-------|----------|---------|--------|
| 1 | Luna 6680 / pair 13356 (WARN) | Unidentified references | `new-pattern: identify-tool` | Identified `rg` as the ripgrep text-search command at first mention. | fixed |
| 2 | Luna 6682 / pair 13370 (FAIL) | Connection inflation | `new-pattern: deduplicate-links` | Removed three Relevant Notes entries that duplicated load-bearing inline links. | fixed |
| 3 | Luna 6684 / pair 13384 (WARN) | Framework decoration | `new-pattern: collapse-redundant-presentation` | Replaced the audience table with one prose statement. | fixed |
| 4 | Luna 6688 / pair 13410 (FAIL) | Title-body alignment | `new-pattern: align-title-to-invariant` | Retitled around change-time lineage signals rather than source-side storage. | fixed |
| 5 | Luna 6692 / pair 13437 (FAIL) | Confidence miscalibration | `hedge-own-framework` | Scoped the provenance claim, named interruption-first maintenance as a proposed criterion, qualified the behavioral premise, and made rankings conditional. | fixed |
| 6 | Luna 6695 / pair 13458 (WARN) | Pseudo-formalism | `new-pattern: collapse-redundant-presentation` | Removed the redundant audience table and arrow chain in favor of one prose account. | fixed |
| 7 | Luna 6697 / pair 13472 (FAIL) | Source residue | `unframed-domain-examples` | Distinguished locally edited sources from external or immutable sources whose successors are detected or adopted. | fixed |
| 8 | Luna 6699 / pair 13486 (WARN) | Completeness / boundary cases | `boundary-case-acknowledged` | Scoped source-link omission to consumers that do not inspect provenance and preserved citations for provenance-bearing artifacts. | fixed |
| 9 | Luna 6701 / pair 13499 (WARN) | Grounding alignment | `hedge-strength-mismatch` | Limited the indirection claim and no-link policy to the supported consumer scope; removed the circular implementation-evidence footer. | fixed |
| 10 | Luna 6702 / pair 13506 (WARN) | Internal consistency | `new-pattern: align-title-to-invariant` | Distinguished record storage from the change-time surface and made hidden artifact metadata explicitly viable. | fixed |
| 11 | Luna 6703 / pair 13513 (WARN) | Load-bearing qualifiers | `new-pattern: align-title-to-invariant` | Removed source-side storage from the H1 and kept source-side records as this KB's implementation. | fixed |
| 12 | Luna 6705 / pair 13525 (WARN) | Clause packing | `new-pattern: split-packed-sentences` | Shortened the description, split the opening, and separated database and artifact-side capabilities from their signal requirements. | fixed |
| 13 | Luna 6706 / pair 13532 (WARN) | Concept attribution | `hedge-strength-mismatch` | Restricted indirection and frontloading attributions to LLM instructions, leaving the broader effect as focus and maintenance cost. | fixed |
| 14 | Luna 6707 / pair 13539 (WARN) | Framing mismatch | `new-pattern: align-title-to-invariant` | Replaced the outside-the-artifact storage claim with a consumer-visibility distinction. | fixed |
| 15 | Luna 6711 / pair 13567 (FAIL) | Bullet capitalization | `new-pattern: capitalize-link-labels` | Capitalized the retained prose link labels; the redundant fourth affected entry was removed. | fixed |
| 16 | Luna 6712 / pair 13574 (FAIL) | Compound bullets | `new-pattern: split-compound-comparisons` | Split each lineage-location option into nested capability, requirement, benefit, cost, or limitation bullets. | fixed |
| 17 | Luna 6714 / pair 13588 (WARN) | Collection contract | `new-pattern: align-title-to-invariant` | Made the title state the weakest general claim the argument supports. | fixed |
| 18 | Luna 6715 / pair 13595 (WARN) | Note type | `new-pattern: align-title-to-invariant` | Replaced the inaccurate source-storage handle with the change-signal claim. | fixed |
| 19 | Claude 6616 / pair 13078 (WARN) | Title-body alignment | `new-pattern: align-title-to-invariant` | Aligned the H1 with the description and the body's storage-location alternatives. | fixed |

### Warning-to-fix mapping

- **#1 (Unidentified references):** The warning said `rg` was unexplained shorthand. Its first mention now identifies ripgrep and its text-search role.
- **#2 (Connection inflation):** The failure identified duplicate footer entries for indirection, checked derived copies, and `link-vocabulary.md`. All three were removed from Relevant Notes while their load-bearing inline uses remain.
- **#3 (Framework decoration):** The warning said the audience table restated the prose without adding a decision rule. The table is gone; a single sentence now distinguishes consumer content from the maintainer's lineage view.
- **#4 (Title-body alignment):** The failure said source-side storage in the H1 contradicted the accepted database and indexed-metadata designs. The H1 now claims change-time lineage signaling for artifacts that omit consumer-facing source links.
- **#5 (Confidence miscalibration):** The failure challenged the artifact-wide provenance claim, the claim that editors will not search, and unconditional design rankings. The opening now maps the provenance boundary, the behavioral claim is probabilistic, the interruption-first criterion is explicitly proposed, and comparisons are conditional on it and on repository context.
- **#6 (Pseudo-formalism):** The warning identified both the audience table and `source changes → ...` chain as notation-shaped repetition. Both were replaced by one prose account of the change-time flow.
- **#7 (Source residue):** The failure said source footers and edit-time tooling presupposed locally controlled mutable sources. The note now also covers immutable and externally owned sources at detection or adoption of a successor version.
- **#8 (Completeness):** The warning identified papers, legal analyses, audit records, and evidence-backed recommendations whose citations are consumer-facing content. The opening retains these examples and states that use-shaping preserves provenance when the consumer's warrant requires it.
- **#9 (Grounding alignment):** The warning said the LLM-instruction indirection note could not support an artifact-wide no-backlink default and that the implementation document was circular evidence. The attribution is now LLM-specific, the broad default is gone, and the duplicated `link-vocabulary.md` evidence entry was removed.
- **#10 (Internal consistency):** The warning found a contradiction between source/outside-artifact storage claims and viable database or indexed artifact metadata. Storage and presentation are now separate, and all three placements are evaluated against the same change-handling surface criterion.
- **#11 (Load-bearing qualifiers):** The warning said `recorded at the source` was a non-load-bearing title and filename restriction. The H1 no longer makes that restriction. The filename remains unchanged under the task's known-intentional deferred migration rule and is not treated as an actionable defect.
- **#12 (Clause packing):** The warning named four packed passages. The description is now one invariant; the executor/provenance passage is split; database capability is separate from integration; and artifact-side capability, signal requirement, and maintenance cost are separate nested bullets.
- **#13 (Concept attribution):** The warning said indirection and frontloading were identified too broadly. The indirection link now applies only to pointers resolved in LLM instructions, and the frontloading footer now describes producing an LLM instruction from already-known source material rather than equating all use-shaping with frontloading.
- **#14 (Framing mismatch):** The warning said consumer focus was wrongly converted into a storage constraint. The note now requires separation from consumer-visible content only where that consumer does not need provenance and permits hidden artifact metadata.
- **#15 (Bullet capitalization):** The failure named four lowercase prose link labels. The three retained labels are capitalized, and the fourth entry was removed as duplicate connection inflation.
- **#16 (Compound bullets):** The failure said each storage option buried independent benefits and limitations in one bullet. Each option now has named nested comparison dimensions.
- **#17 (Collection contract):** The warning said the title exceeded the proof's weakest assumptions. The title now omits the source-local storage restriction and states the consumer-visibility and change-signal boundary.
- **#18 (Note type):** The warning said the title was not an accurate compressed handle. The new title compresses the scoped invariant instead of this KB's implementation choice.
- **#19 (Older current title warning):** The selector's Claude warning made the same storage-versus-presentation distinction. The H1 and opening now state it directly.

### Deferred items

- None. The unchanged filename is known deferred migration infrastructure, not a deferred review defect.

### New patterns

- **`identify-tool`:** Identify named command shorthand at first use when its role is not common reader knowledge.
- **`deduplicate-links`:** Remove footer navigation that repeats a load-bearing inline relationship without adding a distinct reader need.
- **`collapse-redundant-presentation`:** Replace decorative tables or notation that merely restate adjacent prose.
- **`align-title-to-invariant`:** Replace a title's contradicted implementation restriction with the invariant supported by all admitted designs.
- **`split-packed-sentences`:** Separate characterization, capability, and requirement claims that share one working-memory unit.
- **`capitalize-link-labels`:** Capitalize prose-form Markdown link labels while preserving lowercase literal identifiers.
- **`split-compound-comparisons`:** Give benefits, requirements, and limitations separate nested positions in option comparisons.

## Sol follow-up

Reviewed all persisted Sol non-pass verdicts for this note in completed review jobs 6718–6758: 2 WARN and 1 FAIL. All 3 results are fixed; none are deferred. The Luna mapping above is preserved unchanged.

| # | Review | Check | Strategy | Summary | Status |
|---|--------|-------|----------|---------|--------|
| S1 | Sol 6720 / pair 13617 (WARN) | Undefined terms | `new-pattern: replace-graph-jargon` | Replaced the graph-specific “orphans” shorthand with “artifacts with no relevant lineage links.” | fixed |
| S2 | Sol 6744 / pair 13781 (WARN) | Load-bearing qualifiers | `new-pattern: align-title-to-invariant` | Removed the non-load-bearing consumer-facing-link restriction from the description, H1, and opening scope while retaining consumer visibility as a placement condition and preserving citation-bearing boundary cases. | fixed |
| S3 | Sol 6750 / pair 13821 (FAIL) | Parsing ambiguity | `new-pattern: explicit-antecedent` | Rewrote the description to say explicitly that an upstream change may render the artifacts stale. | fixed |

### Sol deferrals

- None.

## Sol residual follow-up

Reviewed the residual Sol verdict in review job 6767: 1 FAIL. The finding is fixed; none are deferred.

| # | Review | Check | Strategy | Summary | Status |
|---|--------|-------|----------|---------|--------|
| SR1 | Sol 6767 / pair 13927 (FAIL) | Claim strength | `new-pattern: sharpen-title-to-contestable-point` | Replaced the broad dependency-management truism with the note's interruption-first asymmetry: source changes should surface downstream review targets, while reverse lineage may remain searchable. | fixed |

### Sol residual warning-to-fix mapping

- **SR1 (Claim strength):** The failure said the title hid the non-obvious interruption-first asymmetry behind the uncontroversial need for lineage signals. The H1 now states that asymmetry directly.

### Sol residual deferrals

- None.
