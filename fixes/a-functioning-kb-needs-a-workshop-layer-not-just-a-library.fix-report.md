## Fix Report: a-functioning-kb-needs-a-workshop-layer-not-just-a-library

### Outcome and authority

One bounded fix pass completed on `kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md`. Deterministic validation succeeded. **Closing review is pending**: by the operator's coordination deviation, the parent will rerun **all gates with Sol after both fixers finish**. No review or subagent was launched, and no commit was made. Applied fixes are not post-edit review verdicts.

- Input sweep: `kb/reports/state/review/runs/20261112T080231Z`.
- Fresh queue queried before editing with `commonplace-review status kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md --fresh --outcome warn fail --json`.
- Queue: **19 criteria: 3 fail, 16 warn**, all fresh, all model `gpt-6.1-sol`, all from the named sweep.
- Read all 35 Findings items, including one INFO within a WARN result. The collection comparison finding has two separately dispositioned components: **36 disposition items: 24 fixed, 12 deferred, 0 rejected**. These are overlapping reviewer observations, not 24 independent edits.
- Original-finding totals: 23 wholly fixed, 11 wholly deferred, 1 partially fixed/deferred.
- No existing fix report was present. Fixer model: `gpt-6.1-sol`.
- Instructions read fully: current `kb/instructions/FIX-SYSTEM.md`, `kb/instructions/fix-warnings/fix-review-warnings.md`, strategy taxonomy, `cp-skill-write`, `cp-skill-validate`, theory collection and note type contracts, and reports collection contract. Linked evidence is identified below.
- Write ownership was limited to the note and this report. Another fixer's note appeared in repository status during the pass; it was not edited or integrated here.

### Original result paths

These are the exact original result locations. The finding paraphrases below retain their substance independently of these replaceable files. Finding numbers in the disposition table refer to this report, not line numbers in the original results.

| Key | Criterion | Outcome | Original result path |
|---|---|---|---|
| A | accessibility/undefined-terms | fail | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/accessibility/undefined-terms.md` |
| B | accessibility/unidentified-references | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/accessibility/unidentified-references.md` |
| C | complexity/connection-inflation | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/complexity/connection-inflation.md` |
| D | complexity/framework-decoration | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/complexity/framework-decoration.md` |
| E | frontmatter/title-body-alignment | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/frontmatter/title-body-alignment.md` |
| F | prose/bridge-paragraph-duplication | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/prose/bridge-paragraph-duplication.md` |
| G | prose/confidence-miscalibration | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/prose/confidence-miscalibration.md` |
| H | prose/orphan-references | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/prose/orphan-references.md` |
| I | prose/pseudo-formalism | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/prose/pseudo-formalism.md` |
| J | semantic/grounding-alignment | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/semantic/grounding-alignment.md` |
| K | semantic/internal-consistency | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/semantic/internal-consistency.md` |
| L | semantic/unwarranted-scope | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/semantic/unwarranted-scope.md` |
| M | sentence/clause-packing | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/sentence/clause-packing.md` |
| N | sentence/concept-attribution | fail | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/sentence/concept-attribution.md` |
| O | sentence/framing-mismatch | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/sentence/framing-mismatch.md` |
| P | sentence/misleading-link-text | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/sentence/misleading-link-text.md` |
| Q | structural/bullet-capitalization | fail | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/structural/bullet-capitalization.md` |
| R | kb/types/note | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/kb/types/note.md` |
| S | kb/theory/COLLECTION | warn | `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/kb/theory/COLLECTION.md` |

Original recorded `note-sha256` values (watched-part hashes can differ by criterion): E `f5dcf66a3ade1abc10d70595a03955167f6e394140c16775be5196dffe17b8f5`; L `0869d9193dc7d867a86bd66e3acfaf3100f3c0dc2d4c7777fb0b6e4c8fae019f`; R and S `78372341f91e35b84c961e368ae0fcbba331ab263a1bd7f589a9c68b3f04916e`; all other listed results `aa3e6704fb2c8d2d9912c31ac628281966bf2bca675d4954aadd6e6d45d03d3b`.

### Findings and warning-to-fix mapping

Each row preserves the original finding and its local disposition. `new-pattern` means the applied presentation/accuracy fix has no named taxonomy strategy; the subtype is described under New patterns.

| # | Check / original finding | Strategy | Summary / action | Status |
|---|---|---|---|---|
| 1 | A.1 FAIL: opening `adr` / ADR is undefined | new-pattern | Expanded architecture decision record and its purpose at first mention, using the ADR contract | fixed |
| 2 | A.2 FAIL: footer identifies extraction with constraining without its technical meaning | qualifier-dropped | Glossed narrowing/ranking valid readings or behaviors and settling disputed boundaries; made the relationship conditional on those choices for an agent consuming the output | fixed |
| 3 | B.1 WARN: “Tulving mapping” identifies neither person nor taxonomy | new-pattern | Identified Endel Tulving's memory taxonomy from cognitive science, as described by the linked note; did not add a new cognitive-science claim | fixed |
| 4 | B.2 WARN: Claw category is unidentified | new-pattern | Added the linked note's short agent-category description inline | fixed |
| 5 | C.1 WARN: typed-callables footer duplicates the final open question and signature | new-pattern | Removed only that footer entry; retained the inline link, signature, and open question | fixed |
| 6 | D.1 WARN: six temporal categories exceed the distinctions used later; decision/collaborative threads overlap and periodic reviews already use tasks | — | Defer the suggested category reduction or new distinguishing design requirements to decision D3 | deferred |
| 7 | E.1 WARN: H1 requires a workshop for every functioning KB, whereas body supports workflow-oriented KBs | — | Defer central claim scope to D1; title unchanged | deferred |
| 8 | F.1 WARN: introduction previews lifecycles, dependencies, expiration, outcomes repeated in next table | — | Sentence split does not resolve this duplication; compressing the paragraph would select which task/example premises to remove. Defer to D4 | deferred |
| 9 | G.1 WARN: universal opening necessity exceeds support; later workflow condition is narrower | — | Same claim choice as D1; no necessity claim weakened implicitly | deferred |
| 10 | G.2 WARN: accumulating/consumed value and “Deletion is a signal something went wrong” are ungrounded; remaining work differs from retained evidence value | — | Defer value-model or retention-policy choice to D2 | deferred |
| 11 | H.1 WARN: “Current state” task-only, outside-KB, search-only, schema/validation/connect/backlink inventory lacks dated evidence | — | Verified current counterevidence but cannot reconstruct the intended historical case. Defer to D5 | deferred |
| 12 | H.2 WARN: lost decision discussion, `sources/` + `/ingest`, recurring-task coverage, and no session logs lack scoped observations | — | Checked paths/contracts; historical reference and treatment remain undecided. Defer to D5 | deferred |
| 13 | I.1 WARN: six lifecycle arrow chains look like transition specifications but specify no transition rules; outputs are mixed with states | new-pattern | Replaced chains with ordinary prose, calling proposed examples “Illustrative stages”; preserved stages, order, outputs, and examples | fixed |
| 14 | I.2 WARN: bridge arrows and footer refinement ladder duplicate adjacent prose without formal consequences | new-pattern | Removed redundant bridge-direction parentheticals and the footer ladder; preserved explanations and proposed skill signature | fixed |
| 15 | J.1 WARN: Claw note does not establish workshop origin of action-guiding material or require new document types; transfer and scope are unstated | qualifier-dropped; unsourced-addition | Restored retained-context subset, replaced attributed type-system requirement with action-guiding material, framed workshop use/production as a proposal, and kept evaluation as a question about KB contribution | fixed |
| 16 | J.2 WARN: holistic-rewrite footer drops active-evolution condition and classifies all narratives as workshop | qualifier-dropped | Restricted workshop example to current action during active evolution; acknowledged stable whole-picture knowledge | fixed |
| 17 | K.1 WARN: footer equates all extraction with deterministic spec mining, contradicting body's broader extraction category | qualifier-dropped | Restricted footer to deterministic extraction of rules/verifiers, matching the body | fixed |
| 18 | K.2 INFO: constraining identification drifts from definition; retention alone does not change valid interpretations | qualifier-dropped | Same conditional definition repair as #2; retention alone explicitly insufficient | fixed |
| 19 | L.1 WARN: local/proposed workflow cases do not support necessity across all functioning KBs | — | Same claim choice as D1; universal-vs-conditional-vs-conjectural choice deferred | deferred |
| 20 | M.1 WARN: 49-word introduction packs lifecycle, outcomes, external examples, disposal into one sentence | new-pattern | Split lifecycle and outcomes into separate sentences; retained all external-action examples and disposal alternative | fixed |
| 21 | M.2 WARN: first open question interrupts subject/predicate with directory-note aside | new-pattern | Moved aside after completed predicate, correcting plural agreement; no argument changed | fixed |
| 22 | N.1 FAIL: retention is not constraining without a consumer and permission/preference change | qualifier-dropped | Same agent-consumer conditional repair as #2, not an assertion that every bridge constrains | fixed |
| 23 | N.2 FAIL: spec mining target requires deterministic outputs; footer equates it with broader extraction | qualifier-dropped | Same deterministic-subset repair as #17 | fixed |
| 24 | N.3 WARN: narrative target permits stable knowledge; only active-evolution case is workshop | qualifier-dropped | Same conditional narrative repair as #16 | fixed |
| 25 | O.1 WARN: completing pending work is not declining document usefulness; archived records can gain provenance/diagnostic value | — | Requires deciding what “value” means and revising the model/table, not just restyling. Defer to D2 | deferred |
| 26 | O.2 WARN: footer substitutes retention for constraining and deterministic extraction for all extraction | qualifier-dropped | Repaired both annotations as in #2 and #17 | fixed |
| 27 | P.1 WARN: “constraining is learning” label and annotation imply promotion alone satisfies constraining/learning | qualifier-dropped | Label now “Constraining”; annotation states required consumer-relative change, not an unconditional learning claim | fixed |
| 28 | P.2 WARN: holistic-rewrite link label asserts necessity rejected by target's current conditional title | new-pattern | Used target's current title and conditional workshop annotation | fixed |
| 29 | P.3 WARN: Claw sentence attributes new knowledge-type requirement to note explicitly leaving type changes open | unsourced-addition | Replaced attribution with action-guiding retained material; preserved type-system choice as open | fixed |
| 30 | Q.1 FAIL: ten Relevant Notes bullets start with lowercase prose titles | new-pattern | Capitalized retained labels; removed duplicate typed-callables entry under #5, leaving nine footer entries | fixed |
| 31 | R.1 WARN: known hybrid/pole limits lack required `## Scope` heading | new-pattern | Inserted heading immediately before existing limits paragraph; did not move or rewrite paragraph or add a scope claim | fixed |
| 32 | S.1 WARN: title/opening/description do not preserve workflow condition or claim modality | — | Defer title/opening/description scope choice to D1; frontmatter unchanged | deferred |
| 33a | S.2 WARN component: comparison's conceded poles/hybrids lack ideal-type consequence bound and explanatory-dominance commitment | — | Defer model modality and adequacy commitments to D2; do not invent bounds | deferred |
| 33b | S.2 WARN component: library relationships are called bidirectional although `extends` is asymmetric | new-pattern | Changed only library cell to “Both symmetric and directional,” retaining the examples and the workshop cell | fixed |
| 34 | S.3 WARN: local task installation/version and absence claims are not recoverably scoped | — | Same evidence/source decision as D5; no historical state invented | deferred |
| 35 | S.4 WARN: footer lacks required relation labels, and constraining/spec-mining annotations overidentify mechanisms | new-pattern; qualifier-dropped | Added collection-authorized labels to retained edges; corrected mechanism annotations as above | fixed |

### Evidence and mechanism checks

Read the affected linked notes fully before repairing their attributions:

- `kb/reference/types/adr.md`: ADRs retain implemented architectural decisions, Context, Decision, Consequences, and, for newer decisions, considered alternatives. Supports #1, and is current counterevidence to categorical loss of alternatives.
- `kb/theory/definitions/constraining.md`: opening defines retained choices narrowing/ranking valid readings/behaviors or settling disputed boundaries; Exclusions reject result selection and retention without interpretation change. Supports #2/#18/#22/#26/#27, not a claim that every extraction constrains or learns.
- `kb/theory/spec-mining-as-codification.md`: “The pattern” mines repeated behavior into deterministic functions, schema rules, unit tests, and checkers. Supports the deterministic subset wording, also already explicit in this note's body.
- `kb/theory/evolving-understanding-needs-holistic-rewrite-not-composition.md`: current title is the conditional whole-picture narrative claim used in the repaired label. “Rapidly evolving working knowledge is an important case, not a requirement. In that case, the narrative's lifecycle is workshop rather than library.” Supports restoring that condition, not narrowing the target's general claim to changing knowledge.
- `kb/theory/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md`: opening describes the agent category and explicitly selects retained domain/user/project context; action-guiding examples are “not evidence that the document type system itself must change.” Evaluation distinguishes KB contribution from whole-agent outcomes. Supports repaired attribution and proposal framing. No claim that workshop material actually improves action capacity was added.
- `kb/theory/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md`: identifies Endel Tulving's memory taxonomy from cognitive science; supports identifying the existing reference, not independently verifying that taxonomy or its practical benefit.
- Also read `kb/theory/why-directories-despite-their-costs.md`, `kb/reference/collections-and-types.md`, `kb/theory/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md`, `kb/theory/automating-kb-learning-is-an-open-problem.md`, and `kb/reference/link-vocabulary.md` for existing footer relationships. Footer labels do not assert new lineage or corroboration. The narrative `evidenced-by` annotation explicitly bounds an example, rather than claiming a test of the workshop thesis.

**Stale-path/mechanism checks, not an implementation audit:**

- `ls` confirms no root `tasks/` or `sources/` and no `.agents/skills/ingest`, `codify`, `validate`, or `connect` at those exact names. `kb/tasks/`, `kb/sources/`, `kb/work/`, `kb/log.md`, and the `cp-skill-ingest`, `cp-skill-validate`, `cp-skill-connect` projections exist. A missing exact skill path does not prove no analogous operation exists.
- `kb/work/COLLECTION.md`, read fully, explicitly governs in-flight drafts, investigations, scratch notes, and migration plans inside the KB. It permits declared types and describes extraction on closure. Thus “tasks are the only workshop-like subsystem” is not a defensible description of the current checkout.
- `kb/reference/validation-contract.md`, read fully, states that the explicit `lifecycle` target inspects `kb/work/` and `kb/tasks/`; ordinary explicit artifact validation can validate workshop drafts. `kb/reference/commands.md` also documents `commonplace-task` under `kb/tasks/`. No task was run and no broad lifecycle validation was invoked.
- Scoped search found session-labelled observations in `kb/log.md`, including explicit operator/session identifiers. This rebuts an unqualified suggestion of no capture, but does **not** establish a formal session-log document type or prove the original historical observation false.
- These checks do not establish historic task schemas, original search indexing, recurring-task completeness, task↔note backlink tracking, or past connect coverage. `why-directories` describes lifecycle directories but includes its own old operational inventory; it is not a reliable substitute for a pinned implementation inventory.
- `/codify` is expressly proposed (“might include”, “Probably”), not an assertion that the operation exists. Its absence at the checked skill path does not justify removing the example. The `/ingest: source → source-review` signature is retained as the explicitly discussed interface example; this pass does not silently modernize its output identity.
- No dated historical case was inferred from the file's last commit date (`9c7563bf7`, 2026-10-23, a collection relocation); that date does not establish when the implementation assertions were true.

### Rejected findings

None. The questionable model, scope, structure, and implementation observations were deferred rather than rejected. Current counterevidence to an unscoped claim is not evidence that the review warning is spurious.

### Deferred items — substantive decisions for the parent/operator

**D1 — Central necessity claim and scope (#7, #9, #19, #32).** Affected passages: H1 “A functioning knowledge base needs a workshop layer,” opening “a functioning knowledge base also needs to support work in motion,” and description. Options: (a) authorize a conditional claim limited to KBs supporting ongoing workflows and align all surfaces; (b) retain the universal claim as an explicitly identified conjecture with its untested library-only extension; or (c) retain universal necessity and supply an argument excluding functioning library-only KBs. The body itself says the task arrangement is adequate for a primarily knowledge-focused KB. Choosing the intended central proposition is beyond this framing/accuracy pass. No title or description edit or rename was made.

**D2 — Value model and comparison modality (#10, #25, #33a).** Affected passages: two library/workshop definition paragraphs, the value/time/end-state table, and hybrid/consumption language (including the retained wikiwiki annotation). Options: (a) replace declining usefulness with discharge of pending work while separating retained provenance/evidence value; (b) explicitly propose a lifecycle/retention policy rather than an empirical value trajectory; or (c) retain an ideal-type model with authorized mechanism, consequence bound, and explanatory-dominance commitments, or evidence sufficient for another claim mode. The current record supplies no measured value trajectory or defensible invented bound. This decision changes the explanatory model and cannot be chosen by a local fix. Only the independently checkable relationship-direction error was corrected (#33b).

**D3 — Temporal inventory structure (#6).** Affected section: “Temporal document types beyond tasks.” Options: (a) retain illustrative categories but authorize a discriminating lifecycle/design rule, especially for decision vs collaborative threads and periodic reviews vs tasks; or (b) authorize consolidation into fewer examples as the reviewer recommends. The instruction forbids dropping examples or redesigning the structure in this pass. All six examples remain; only arrow presentation was changed.

**D4 — Introductory repetition (#8).** Affected paragraph: “This works well for durable knowledge…” through the task example. Options: (a) authorize deleting a specified subset of lifecycle/dependency/expiration preview details already supplied by the table; (b) preserve the concrete task mechanism example and accept some repetition; or (c) relocate the example in a structural revision. The review's proposed one-sentence transition would remove concrete external-action and task examples, contrary to this fix pass's example-preservation boundary. Sentence splitting resolves clause packing (#20), not this separate redundancy finding.

**D5 — Historical case versus current implementation account (#11, #12, #34).** Affected passages: introduction's `tasks/` example and type-gap claim; “Currently invisible” decision threads; `sources/` awaiting `/ingest`; recurring reviews; “Session logs…Currently not captured at all”; entire “Current state of the gap”; and task-template premise in the second open question. Options: (a) identify a pinned historical Commonplace state and retain only assertions verified there, in historical framing; (b) commission a present-day inventory and replace these assertions with a current, scoped application; or (c) authorize turning them into proposed capabilities/questions without empirical absence claims. Current paths, workshop contract, ADR alternatives requirement, log observations, and lifecycle validation contradict parts of the present-tense account. They cannot prove the intended historical state, and a path-only update would misleadingly transfer an old subsystem's properties to today's different mechanisms. No inventory replacement, source selection, or silent claim deletion was made.

### New patterns

No taxonomy or criteria were edited. Local strategy descriptions for `new-pattern` rows:

- **Inline identification/gloss** (#1, #3, #4): expand an acronym or identify a linked person/category using already available evidence.
- **Duplicate-footer removal** (#5): remove a footer entry already fully represented inline, retaining the actual question and example.
- **Illustrative-notation cleanup** (#13, #14): express stage examples in prose and remove redundant directional notation without inventing transition rules.
- **Clause unpacking / aside placement** (#20, #21): split overloaded syntax or move an interruption without selecting new premises.
- **Current-target link label** (#28): match the target's conditional claim rather than an obsolete necessity label.
- **Bullet capitalization** (#30): capitalize prose labels, preserving destinations.
- **Scope-heading repair** (#31): put a required heading immediately before existing limits without changing or relocating them.
- **Relation-direction accuracy** (#33b): do not call an explicitly asymmetric relation bidirectional.
- **Footer-label conformance** (#35): label already articulated edges with the collection's authorized reader-need labels; no discovery or new edge added.

### Validation and closing-review state

Command:

```bash
commonplace-validate kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
```

Output (exit 0):

```text
VALIDATION SUCCESS
Target: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
Scope: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects

Details: commonplace-validate --full kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
```

Reviewed the note diff and reread all edited passages. No `user-verified` field was present to remove. `git diff --check` produced no output. No code/tests changed; pytest was not run.

Read-only post-edit status: **44 applicable pairs, 40 stale, 4 fresh, 0 orphaned**. No stale result was treated as a post-edit verdict. All stale pairs, including previously passing gates, await the parent's all-gates Sol rerun. Previously passing pairs that newly warn cannot be reported until that rerun. The deferred choices above remain unresolved even if a subsequent review passes.

Broader graph discovery, if separately wanted after closure, belongs to `cp-skill-connect`; none was launched or written here because this pass owns only the note and this report.

### Closing-review evidence appended by trace audit — 2026-11-12

This appendix records the later parent-owned sweep; it does **not** replace the original findings, local dispositions, or deferred decisions above. Audit: `/tmp/commonplace-review-check/trace-audit.md`.

- Closing run: `kb/reports/state/review/runs/20261112T082159Z`; report: `/tmp/commonplace-review-check/closing.json`.
- This note: **40 pairs re-reviewed, 4 reused fresh; all 44 currently fresh; 34 PASS, 9 WARN, 1 FAIL**. Initial: 25 PASS, 16 WARN, 3 FAIL. All result files record model `gpt-6.1-sol`; new review launches record Codex medium effort. The four reused frontmatter results retain their initial PASS outcomes; closing JSON's null outcome on those rows does not mean an unknown verdict.
- Both notes together: 80 reviewed + 8 reused; all 88 fresh, no orphans, confirmed by read-only status during the audit. Closing command exited 1 because its checkout guard saw the unrelated `kb/theory/two-context-boundaries-govern-collection-operations.md` change, not because pairs were missing or launches failed. The guard does not attribute the change to a worker.
- Current note full-file SHA-256: `770f0cae7d043682e62ee7342f0c5d4ccbdddfc26f7215f8c0ef7114b00f8a61`, matching the closing captures and the original fixer's replayed edits.

#### Every applicable pair's closing outcome

Criterion IDs below resolve to current results under `kb/reports/state/review/results/kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md/<criterion-id>.md`. Exact initial outputs remain in run `20261112T080231Z`; they must not be recovered by treating a replaced current result as the original.

| Criterion | Initial | Closing current | Closing action |
|---|---|---|---|
| `accessibility/jargon-persistence` | PASS | PASS | reviewed |
| `accessibility/notation-opacity` | PASS | PASS | reviewed |
| `accessibility/undefined-terms` | FAIL | FAIL | reviewed |
| `accessibility/unidentified-references` | WARN | PASS | reviewed |
| `complexity/claim-to-section-ratio` | PASS | PASS | reviewed |
| `complexity/connection-inflation` | WARN | WARN | reviewed |
| `complexity/could-be-a-paragraph` | PASS | PASS | reviewed |
| `complexity/framework-decoration` | WARN | WARN | reviewed |
| `frontmatter/claim-strength` | PASS | PASS | reused fresh |
| `frontmatter/description-discrimination` | PASS | PASS | reused fresh |
| `frontmatter/title-as-claim` | PASS | PASS | reused fresh |
| `frontmatter/title-body-alignment` | WARN | WARN | reviewed |
| `frontmatter/title-composability` | PASS | PASS | reused fresh |
| `prose/anthropomorphic-framing` | PASS | PASS | reviewed |
| `prose/bridge-paragraph-duplication` | WARN | PASS | reviewed |
| `prose/confidence-miscalibration` | WARN | PASS | reviewed |
| `prose/mannered-prose` | PASS | PASS | reviewed |
| `prose/orphan-references` | WARN | WARN | reviewed |
| `prose/proportion-mismatch` | PASS | PASS | reviewed |
| `prose/pseudo-formalism` | WARN | PASS | reviewed |
| `prose/redundant-restatement` | PASS | PASS | reviewed |
| `prose/source-residue` | PASS | PASS | reviewed |
| `prose/unbridged-cross-domain` | PASS | PASS | reviewed |
| `semantic/completeness-boundary-cases` | PASS | PASS | reviewed |
| `semantic/conceptual-role-conflation` | PASS | PASS | reviewed |
| `semantic/epistemic-status-blur` | PASS | PASS | reviewed |
| `semantic/explanatory-reach` | PASS | PASS | reviewed |
| `semantic/grounding-alignment` | WARN | PASS | reviewed |
| `semantic/internal-consistency` | WARN | PASS | reviewed |
| `semantic/load-bearing-qualifiers` | PASS | PASS | reviewed |
| `semantic/underspecified-assertions` | PASS | PASS | reviewed |
| `semantic/unearned-generality` | PASS | PASS | reviewed |
| `semantic/unwarranted-scope` | WARN | WARN | reviewed |
| `sentence/clause-packing` | WARN | WARN | reviewed |
| `sentence/concept-attribution` | FAIL | PASS | reviewed |
| `sentence/framing-mismatch` | WARN | WARN | reviewed |
| `sentence/misleading-link-text` | WARN | PASS | reviewed |
| `sentence/parsing-ambiguity` | PASS | PASS | reviewed |
| `sentence/stock-phrases` | PASS | PASS | reviewed |
| `structural/bullet-capitalization` | FAIL | PASS | reviewed |
| `structural/compound-bullet` | PASS | WARN | reviewed |
| `structural/general-before-specific` | PASS | PASS | reviewed |
| `kb/types/note` | WARN | PASS | reviewed |
| `kb/theory/COLLECTION` | WARN | WARN | reviewed |

#### Remaining and newly reported findings

Launch IDs identify `kb/reports/state/review/runs/20261112T082159Z/calls/launches/<ID>/outputs/review.md`.

| Closing criterion / launch | Remaining or new finding; relationship to original work |
|---|---|
| `accessibility/undefined-terms` FAIL / `f30d85fe3a98495a9b5d8f8638bb893f` | **New findings within the same failing criterion:** `structured-claim`/its contract lack an inline explanation; Skills lacks a procedure gloss. Original ADR and constraining findings #1–2 are no longer reported after their edits. These newly flagged concepts already existed. |
| `complexity/connection-inflation` WARN / `4f7179fb3e0f4b0db4d9d9cca3ba0ffc` | **New findings within the same warning criterion:** Claw and spec-mining footer entries repeat inline relationships. Original typed-callables duplicate #5 was removed; this warning is not evidence that it remains. |
| `complexity/framework-decoration` WARN / `c53c5614e777471f969e16cf42464f5d` | Six categories/stages still exceed the design distinctions used. Original #6 / D3 remains deferred. |
| `frontmatter/title-body-alignment` WARN / `e5467b4dc521477e9424a83f9c7fa6ed` | Universal functioning-KB title versus workflow-conditioned argument. Original #7 / D1 remains. |
| `prose/orphan-references` WARN / `ea883dc135d1456ea9d4016fdbc15e6a` | Undated task integration inventory and unscoped decision/source/recurrence/session-capture assertions. Original #11–12 / D5 remain. |
| `semantic/unwarranted-scope` WARN / `3f2ae03f3ebf4a3e8020bc9889ec722a` | Universal necessity is unsupported outside workflow KBs and not marked conjectural. Original #19 / D1 remains. |
| `sentence/clause-packing` WARN / `061c70de9982450b95b1c9f6d3ed3fe9` | The revised first-question sentence is still considered overloaded despite #21's aside move. A **newly reported** second target is the unchanged “But this note exists to mark the gap” sentence. Original introduction target #20 is no longer reported. |
| `sentence/framing-mismatch` WARN / `a5dde6c71f7a46d999de0b947b1027aa` | Declining usefulness still conflates work resolution with document value, including the runbook hybrid. Original #25 / D2 remains; repaired footer mechanism finding #26 is no longer reported. |
| `structural/compound-bullet` WARN / `9b8728aaed3646ef9be9a64d26a30d96` | **Previously PASS criterion, now WARN:** first open question combines local subsystem conventions with shared-library linking. Both propositions predate the fix; the aside was moved, not these propositions added. No disposition is assigned here. |
| `kb/theory/COLLECTION` WARN / `6b1962f755124e78902b0e40745ee5be` | Universal thesis and unrecoverably scoped local reports remain (#32 / D1 and #34 / D5). The original comparison-modality component #33a is not repeated; its D2 decision was not made. Footer labels/deterministic restriction and relationship-direction repairs are no longer flagged. |

#### Disappearing warnings without corresponding resolution

- `prose/bridge-paragraph-duplication` now passes (`9bd9271d2bc3405fab69255840834b3f`). The fixer retained the preview's contents and explicitly deferred compression (#8 / D4); sentence splitting is not that compression. Closing review regards the sections as different-purpose passages. Record this as a changed judgment, not a completed deferred fix.
- `prose/confidence-miscalibration` now passes (`a6a508196da04559b9bde5fde446c5ab`). Its new rationale treats the value model as qualitative and bounded by Scope. The universal necessity claim, value assertions and deletion diagnostic remain unchanged (#9–10 / D1–D2). Other closing criteria still warn on the underlying scope/value problems.
- The collection review no longer asks for the comparison's ideal-type consequence bound/explanatory-dominance commitment (#33a). No such commitments or replacement model were supplied. The independently fixed asymmetric-relation error (#33b) does not resolve this deferred component.

**D1–D5 remain open as originally recorded.** Closing PASS outcomes are fresh reviewer judgments, not authority to alter original dispositions or treat unmade decisions as settled. No further note edit, review, graph discovery, or substantive disposition was performed by the audit.
