## Fix Report: evolving-understanding-needs-holistic-rewrite-not-composition

All 13 adverse Luna review results from completed jobs 6677–6717 are fixed: 9 WARN and 4 FAIL. No review result is deferred.

| # | Review | Check | Strategy | Summary | Status |
|---|--------|-------|----------|---------|--------|
| 1 | 6678 WARN | Notation opacity | new-pattern: plain-language-substitution | Removed undefined `N` and described the burden in ordinary prose | fixed |
| 2 | 6680 WARN | Unidentified references | new-pattern: identify-named-entities | Identified `blader`, the MIT License, and Augment Code's role | fixed |
| 3 | 6682 FAIL | Connection inflation | new-pattern: remove-duplicated-edges | Removed the three footer edges whose relationships were already explicit in the body | fixed |
| 4 | 6688 FAIL | Title-body alignment | boundary-case-acknowledged | Replaced the categorical title with a claim bounded by whole-picture need, infeasible reconciliation, and narrative feasibility | fixed |
| 5 | 6692 WARN | Confidence miscalibration | hedge-own-framework; boundary-case-acknowledged | Presented the pressure model as qualitative and proposed, and carried the operative boundaries into the title and opening | fixed |
| 6 | 6693 WARN | Orphan references | unsourced-addition | Removed the uncited claim that teams report easier mid-project onboarding | fixed |
| 7 | 6695 FAIL | Pseudo-formalism | new-pattern: plain-language-substitution | Removed the two-dimension model, undefined variable, proportional relation, and unsupported threshold model | fixed |
| 8 | 6699 WARN | Completeness boundary cases | boundary-case-acknowledged | Required faithful compression and timely refresh, and put cases where both approaches fail outside the pattern | fixed |
| 9 | 6705 WARN | Clause packing | new-pattern: split-packed-clauses | Split the rewrite rule, dependency claim, and stale-on-change rule into separate sentences | fixed |
| 10 | 6707 WARN | Framing mismatch | boundary-case-acknowledged | Made whole-picture reconciliation the mechanism, treated rapid evolution as one high-cost case, and retained the workshop lifecycle for that case | fixed |
| 11 | 6709 WARN | Parsing ambiguity | new-pattern: frontload-condition | Put the source-change condition before the narrative's stale status | fixed |
| 12 | 6711 FAIL | Bullet capitalization | new-pattern: normalize-capitalization | Removed two duplicated lowercase entries and capitalized the retained `Agent context` entry | fixed |
| 13 | 6714 WARN | Collection contract | boundary-case-acknowledged; new-pattern: normalize-link-grammar | Scoped the headline and normalized footer labels and destination kinds | fixed |

### Warning-to-fix mapping

- **#1 (job 6678):** “Loading N fragments” used an undefined variable. The opening now uses qualitative prose with no variable shorthand.
- **#2 (job 6680):** The compact “MIT, blader, 2026” attribution and “Augment bidirectional spec” left named entities opaque. The Theorist passage now states that `blader` is the repository owner's GitHub username and that the repository uses the MIT License; the footer identifies Augment Code as an AI coding-tool company.
- **#3 (job 6682):** Three Relevant Notes entries duplicated relationships already made inline. The entries for the two-layer execution system, context efficiency, and the workshop layer were removed from the footer while their inline links remain.
- **#4 (job 6688):** The title generalized from a conditional body. The new title names a compact, refreshable whole-picture narrative and infeasible fragment reconciliation rather than making evolution alone sufficient.
- **#5 (job 6692):** The title and three scaling claims were stronger than the admitted evidence. The opening now states that the claim is qualitative, and the three pressures are explicitly proposed mechanisms expressed without scaling laws.
- **#6 (job 6693):** The note cited unidentified team reports of easier onboarding. That outcome claim was removed; Theorist remains an implementation illustration only.
- **#7 (job 6695):** The note used undefined dimensions, `N`, proportionality, and a three-variable threshold without operationalization. Those constructions were replaced by qualified prose about material, currency decisions, and interdependence.
- **#8 (job 6699):** Composition and rewrite can both be infeasible. Narrative compressibility and refresh cadence are now applicability conditions, and the opening explicitly places dual-infeasibility outside the pattern.
- **#9 (job 6705):** One sentence combined the action, prevented failure, dependency, staleness, and citation. These now appear as a short causal sequence across separate sentences.
- **#10 (job 6707):** Evolution and workshop status were treated as necessary despite a broader whole-picture mechanism. The note now covers stable, highly interdependent knowledge and limits the workshop lifecycle claim to evolving working knowledge.
- **#11 (job 6709):** “Stale until reworked when...” had ambiguous attachment. The revised sentence begins with “When that understanding changes” and then states the stale-until-reworked consequence.
- **#12 (job 6711):** Three footer labels began with lowercase words. Two duplicated bullets were removed, and the retained link begins with “Agent.”
- **#13 (job 6714):** The headline omitted operative boundaries and the footer used uncontrolled labels or an ineligible external `extends` edge. The headline is scoped; the remaining footer uses `grounds`, `contrasts`, and `evidence`, with the Augment edge pointing to the local source snapshot.

### Source verification

- Inspected the upstream Theorist repository's `README.md`, `SKILL.md`, and `LICENSE` on 2026-07-17. They support the retained facts: a Codex/Claude skill authored as `blader`, version 1.3.0 dated 2026-02-28, an MIT license, one repo-root `THEORY.MD`, holistic rewrites, change-in-understanding triggers, a roughly 200-line maximum, and brief retention of superseded views as pivots.
- The repository contains no controlled comparison supporting onboarding or agent-performance outcomes, so the onboarding claim was removed.
- Inspected `kb/sources/what-spec-driven-development-gets-wrong-2025993446633492725.md`; it identifies `@augmentcode` and supports the retained description of human-reviewed agent updates to a living specification.

### Deferred items

- None.

### New patterns

- **plain-language-substitution:** Replace undefined symbols and quantitative-looking relationships with qualified prose when the note supplies no operational model.
- **identify-named-entities:** Expand compact attribution metadata or surrounding prose so a reader can tell what each named entity is and why it appears.
- **remove-duplicated-edges:** Delete footer edges when the same destination and relationship are already explicit in the body.
- **split-packed-clauses:** Separate a rule, its mechanism, and its maintenance consequence when one sentence carries all three.
- **frontload-condition:** Put a condition before the state change it governs when final-clause attachment is ambiguous.
- **normalize-capitalization:** Repair list-item capitalization while preserving the linked title's wording.
- **normalize-link-grammar:** Replace uncontrolled relation labels and ineligible destination kinds with collection-approved edges.

### Known intentional non-fixes

- The filename and `distillation` tag are unchanged because they are deferred migration infrastructure, not defects in these review results.

### Sol follow-up

Both adverse Sol review results from completed jobs 6718–6758 are fixed: 1 WARN and 1 FAIL. No Sol review result is deferred.

| # | Review | Check | Strategy | Summary | Status |
|---|--------|-------|----------|---------|--------|
| S1 | 6721 WARN | Unidentified references | new-pattern: remove-unnecessary-proper-name | Removed the unnecessary Codex/Claude qualifier while retaining the repository, skill, author, version, date, and license identifications | fixed |
| S2 | 6750 FAIL | Parsing ambiguity | new-pattern: explicit-antecedent | Repeated `whole-picture narrative` in the description so the fit and refresh conditions cannot attach to effective context | fixed |

#### Sol warning-to-fix mapping

- **S1 (job 6721):** “Codex/Claude skill” named two products without identifying them. Because their identities do not contribute to the illustration, the sentence now says only that the Theorist repository contains a skill; all evidence-bearing implementation and provenance details remain.
- **S2 (job 6750):** In the description, “it” could denote either the whole picture or effective context. The description now names the `whole-picture narrative` as the subject of both fitting within effective context and being refreshed before the narrative goes stale.

#### Sol deferred items

- None.

#### Sol new patterns

- **remove-unnecessary-proper-name:** When an unidentified named product is nonessential to the claim or evidence, remove the name while retaining the role the surrounding sentence needs.
- **explicit-antecedent:** Replace a pronoun with its intended noun phrase when multiple plausible antecedents would impose different conditions.

## Sol residual follow-up

The sole residual Sol review result, job 6761 pair 13888 (`undefined-terms` WARN), is fixed: both findings are fixed and none are deferred.

| # | Review | Check | Strategy | Summary | Status |
|---|--------|-------|----------|---------|--------|
| SR1 | 6761 WARN | Undefined terms | new-pattern: first-use-gloss | Defined `currency decisions` at its first occurrence as decisions about which fragments or claims remain current | fixed |
| SR2 | 6761 WARN | Undefined terms | new-pattern: definition-link | Moved the existing workshop-layer link onto the first meaningful use of `workshop` while retaining its lifecycle gloss | fixed |

### Sol residual warning-to-fix mapping

- **SR1 (job 6761, pair 13888):** “Currency decisions” first appeared before the reader was told that the phrase means decisions about which fragment or claim is current. Its first occurrence now carries that meaning in a parenthetical gloss.
- **SR2 (job 6761, pair 13888):** The active-vocabulary term “Workshop” had a useful lifecycle gloss but no required definition link at its first meaningful use. That first use now links to the workshop-layer note; the existing gloss remains in place.

### Sol residual deferred items

- None.

### Sol residual new patterns

- **first-use-gloss:** Define a local coinage inline at its first occurrence when a later explanation arrives too late for first-pass comprehension.
- **definition-link:** Move an existing concept edge onto an active-vocabulary term's first meaningful use so the required definition is available without duplicating the link.
