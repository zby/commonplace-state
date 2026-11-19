---
disposition: revise
update: determined
merge-target: null
---

## Warranted contribution

**Reader and prior:** The note names no intended reader. The reader therefore comes from the KB purpose in `AGENTS.md`: agents and maintainers deciding KB architecture, types and context engineering. `kb/theory/COLLECTION.md` narrows this to readers who need transferable claims. Existing-KB baseline, from connect: `kb/types/note.md` defines description as a "Discriminating retrieval filter, not a summary". `kb/theory/document-types-should-be-verifiable.md` supplies the verifiability criterion and calls types and traits "the hints that make those decisions informed rather than blind". `kb/theory/type-system-enforces-metadata-that-navigation-depends-on.md` argues that the type system makes descriptions exist. `kb/theory/agents-navigate-by-deciding-what-to-read-next.md` supplies the follow/skip decision model. `kb/theory/addressability-grain-sets-a-matched-selective-read-floor.md` explains why routing by description saves reads. `kb/reference/navigation.md` and `kb/instructions/fix-warnings/fix-descriptions.md` restate the description-as-filter rationale but do not cite this note.

**Update:** Before opening a document, an agent can decide whether to load it from frontmatter: the type says what kind of document it is and what operations it affords, provided the type asserts verifiable structure; the description selects the relevant instance among documents of that kind.

**Why a generic treatment would not supply it:** A generic treatment says that "metadata helps retrieval". This note divides the work between the two fields. The type gives a structural, operation-level prior and the description discriminates between same-type instances. It also names two conditions for the hints to work: the type must assert structure rather than subject matter, and the metadata must be enforced so that it exists. All three method readings of the central commitment state this pair. Critique: "A document's type, paired with its description, lets an agent make informed routing decisions…". Friction: "Reading a document's type … and its description … lets an agent decide whether to load". Premises: "Document types, together with descriptions, give a stateless agent structural hints…". The frontmatter description says the same: "the type says what operations a document affords, the description filters among instances of that type". Compression calls this split "the note's most memorable and actionable commitment" and notes that it is missing from the title.

**Warrant:** The warrant comes from derivation, not observation. The premises are finite context and agents that have not yet read the candidates; premise 5 (statelessness) HOLDS at the level needed. The verifiability criterion is imported by link and grounded (grounding-alignment INFO: "accurately represented"). The enforcement dependency is imported by link and grounded. The contrast between structural types and subject-matter labels holds (premise 7). The description-as-filter role holds when descriptions are written as discriminating filters (premise 6, with that caveat). The note has these repairable limits:
- The type's own share of the routing result is unconstrained. semantic/explanatory-reach: the note "does not explain what routing decision the type changes once a discriminating description and title are present".
- The ranking "description is the most important field" is attributed to `kb/types/note.md`, but that file does not make it (grounding-alignment WARN, misleading-link-text WARN).
- The opening dichotomy "Without types, an agent must either load everything … or guess" is DEFEATED (premise 4, LOCAL) and miscalibrated (confidence-miscalibration WARN).
- "narrow from hundreds of files to the few it needs without opening any of them" presents an efficacy outcome without evidence. It also depends on descriptions that discriminate, which validation does not check (unwarranted-scope INFO, friction joint 3, confidence-miscalibration WARN).
- The examples `spec` and `index` are not current type specs. Only `structured-claim` resolves (connect maintenance observation; critique secondary objection).

**Collection/type fit:** FITS. This is a transferable claim about agent-operated KB navigation, written as a `types/note.md` note with a claim title and the `title-as-claim` trait. No method reported a misfit.

**Strongest objection:** requires a claim change. The title credits *types* with pre-open structural hints. The warranted update is the type+description pair, and the type half holds only for types that assert structure. Evidence:
- Premise 2 is DOUBTFUL, "close to DEFEATED for this KB's own theory collection", GLOBAL, prevalence: "In `kb/theory/`, about 395 of about 440 files declare `type: types/note.md` … Inside a collection, which is where most routing decisions happen, type is nearly constant and carries almost no bits. Title, description, directory placement and traits do the narrowing."
- Critique, partially lands: the linked verifiability note puts `types/note.md` at the `Any` end ("Default — read it to find out what you can do with it"), so "for most documents" the title's claim "is false". The routing work is done by description and title, and the type's real contribution may be indirect, by forcing descriptions to exist.
- semantic/unwarranted-scope WARN: "The supporting derivation only covers types that assert a distinctive structural property … For those documents the hint comes almost entirely from the description, which is not what the title credits."
- semantic/completeness-boundary-cases WARN: the base `note` type is the "simplest instance" and the dominant one, and for it "the type half of the framework supplies almost no operational hint".
- compression/core-claim-obscured and frontmatter/title-body-alignment (low): the body's central claim is the pair, while the H1 names only types. Compression says the author "must decide whether this note argues for types, with description as a supporting filter, or for the type+description pair".

On its own, a DOUBTFUL premise is at most answerable. The claim change rests on two other grounds. First, under the decision table, the warranted Update differs from the title in scope: it is the type+description pair, with the type's contribution conditional on structural assertion, while the title credits types without restriction. Second, the hedge test: if the objection were fully valid, the claim would have to become "type and description jointly route, and the type adds an operation-level hint only for structured types and traits". That narrows the title's scope and adds a load-bearing precondition. A `## Scope` passage added under the current title would therefore be a hedge, not an extension of warrant. Whether a base-typed note's `type: types/note.md` still counts as a "structural hint" in the sense the note means (for example, "transferable claim; open to learn more") is the author's judgement. The counterexample is premise 2, quoted above. The passage it targets is paragraph 2: "Types solve this by giving agents structural hints *before* opening a document. A `spec` tells an agent it can implement from this…"

## Disposition

**revise** — The objection requires a claim change: the warranted update is the type+description pair, with the type's hint conditional on structural assertion, which differs in scope from the title "Types give agents structural hints before opening documents". The objection is that for the modal `types/note.md` document the type carries almost no routing signal (premise 2 GLOBAL; unwarranted-scope and completeness-boundary-cases WARNs).

## Body edits

None are applied, because the disposition is `revise`. The rows below are local repairs the method reports support. They are for the author's revision and are independent of which claim the author chooses.

| Location | Source method(s) | Finding | Action | Rationale |
|---|---|---|---|---|
| Para 1, "Without types, an agent must either load everything (wasteful) or guess what's relevant (error-prone)." | prose/confidence-miscalibration (WARN); semantic/underspecified-assertions (WARN); sentence/framing-mismatch (INFO) | The dichotomy is not exhaustive. Descriptions, titles, paths and search route without types. "Without types" is ambiguous between the field and the whole type system. | compress (restate the counterfactual: "without metadata readable before opening" or "without an enforced type system") | The opening premise must match the mechanism the claim rests on. The current wording contradicts paragraph 3's credit to the description. |
| Para 2, "Types solve this" | prose/confidence-miscalibration (INFO) | Asserts a full solution, while the note's own argument supports partial mitigation. | compress ("reduce this cost") | Calibrates the claim to its derivation. |
| Para 2, `spec` and `index` examples | critique (secondary); connect maintenance observation | `spec` and `index` are retired flat-enum names. Only `kb/theory/types/structured-claim.md` resolves. | compress (replace with current types, e.g. `kb/reference/types/adr.md`, `kb/types/generated-index.md`, `structured-claim`) | The illustrations of the type half should name types a reader can find. |
| Para 2, closing sentence "the agent reads a type and description, then decides…" | compression/marginal-value-redundancy (WARN, minor) | Introduces the description before para 3 explains its role, and previews para 3. | compress (fold into one statement of the type+description routing step) | Brings the pair, which is the selected update, to the front instead of spreading it over two paragraphs. |
| Para 3, "This is why [description is the most important field](../types/note.md)" | semantic/grounding-alignment (WARN); sentence/misleading-link-text (WARN); friction joint 2 (THIN, routed only) | The target says "Discriminating retrieval filter, not a summary" and ranks no field. "This is why" points at the wrong ground. | compress (link text states what the target supports; any ranking stated as the note's own inference from the instance-filter role) | Removes a misattributed premise from the warrant. |
| Para 3, "without opening any of them" | prose/confidence-miscalibration (WARN); semantic/unwarranted-scope (INFO); critique (secondary) | An efficacy and scale claim without evidence. Frontmatter is still read, and it depends on discriminating descriptions that validation does not check. | compress (e.g. "narrow a large collection to a few candidates before reading any body") | Keeps the claim within what the derivation reaches. |
| Para 4, "The structural promise is what makes the routing decision informed rather than blind." | compression/marginal-value-redundancy (WARN); sentence/stock-phrases (INFO) | Restates the paragraph's own opening and the "informed routing" phrase from para 2. | remove (or merge "rather than blind" into the opening sentence) | Does no job for the update or its warrant. |
| Para 5, "the type system is what makes them exist" | semantic/conceptual-role-conflation (INFO) | Ambiguous between type spec and validator. The linked note separates them. | keep | Below materiality. Recorded so the revision does not sharpen it into a stronger causal claim. |
| Relevant Notes, `note base type` entry | complexity/connection-inflation (WARN, low); semantic/grounding-alignment (WARN) | Repeats the inline link and the unsupported "most important" ranking, with no typed relation. | compress (e.g. "rests-on: defines description as a discriminating retrieval filter — the role this note's routing argument depends on") | Removes the misattribution and adds a relation the reader can use. |
| Frontmatter description | frontmatter/description-discrimination (PASS) | Already states the pair. | keep | It already matches the selected update. If the title is revised it should still be checked against the new title. |

## Revision brief

**Objection and evidence.** The title credits types with the pre-open hint. For the KB's modal document (`type: types/note.md`, about 395 of about 440 files in `kb/theory/` per premise 2), the type is near-constant within a collection and asserts almost no structure. The linked verifiability note calls it "Default — read it to find out what you can do with it". For those documents, routing is carried by description, title, directory and traits. The note's own paragraph 3 already gives the instance-level filtering to the description. The note's body and frontmatter description argue for the type+description pair, conditioned on structural types and enforced metadata. Deciding evidence: premise 2 (DOUBTFUL/GLOBAL/prevalence); critique's strongest case (partially lands); semantic/unwarranted-scope WARN; semantic/completeness-boundary-cases WARN; compression/core-claim-obscured INFO with its "author must decide" note; frontmatter/claim-strength WARN (the title sits "close to a truism" and leaves its contestable point, "structural", unstated).

**Candidate replacement claims:**

1. *"Type and description together let agents route before opening documents"* (or close to the frontmatter description). **Mode: universal.** Guard: a checkable counterexample refutes it. One example would be a set of documents with discriminating descriptions where type and description still fail to support a correct load/skip decision, or where the type adds nothing when description and title are held fixed. The body must say what the type contributes beyond the description. The opening dichotomy and the "without opening any" outcome must be restated so they do not overreach. frontmatter/claim-strength suggests a similar title: `Type and description together let agents route without opening documents`.

2. *"Types give agents an operation-level hint before opening only when they promise structure, not subject matter"* (frontmatter/claim-strength suggestion: `Types route agents only when they promise structure, not subject matter`). **Mode: universal**, scoped to structured types and traits. Guard: a refuter would be a structured, verifiable type that does not change a routing decision, or a subject-matter label that routes as well as a structured one. The base `note` type must be named as the `Any` boundary, where description and title carry routing. Traits should appear as the mechanism that adds hints to base-typed notes (critique constructive finding; completeness-boundary-cases INFO).

3. *"In a KB where most documents share a base type, descriptions and titles do most pre-open routing; types add a coarse affordance prior across collections"* (premise gate's "For the human" option). **Mode: statistical.** Guard: state the refuting prevalence in the claim text. For example: the claim fails if, within collections, held-out routing accuracy from type alone (or type's marginal gain over description and title) is comparable to that from description. `kb/theory/quality-signals-for-kb-evaluation.md`'s pruning-accuracy signal (connect Flags) describes a test that could be set up for this. This candidate changes the note's direction toward the description, and would overlap with `kb/theory/type-system-enforces-metadata-that-navigation-depends-on.md` if the type's role is reduced to the indirect, enforcement one.

The premise gate's other option, arguing for a richer populated type set, is a design proposal rather than a claim about current types. If chosen, it belongs in `kb/reference/proposals/`.

**Citer scope** (inbound links whose visible text or summary states the current claim; `kb/work/` and `kb/reports/retained/` hits excluded):
- `kb/theory/why-notes-have-types.md:13`: link text is the full title, followed by the stale `spec`/`index` examples and "The type plus description let an agent narrow from hundreds of files to the few it needs without opening any of them."
- `kb/theory/why-notes-have-types.md:72`: "develops: the navigation role of types".
- `kb/theory/type-system-enforces-metadata-that-navigation-depends-on.md:9` ("navigation argument", which "assumes documents *have* descriptions"), `:22` ("that's the navigation claim"), `:28` ("depends on: the navigation argument that assumes descriptions exist").
- `kb/theory/addressability-grain-sets-a-matched-selective-read-floor.md:90`: link text is the full title, with the summary "the description layer's win is the routing mechanism that note describes".
- `kb/tags/type-system-README.md:17`: "navigation: type + description let agents route without loading full documents". This already states the pair and fits candidate 1.

Retitling would also rename the file, update these link texts and require keeping the `title-as-claim` trait.

## Routed attention (composition-friction-gate and premise-decomposition-gate — not auto-resolved)

**Composition friction — filter verdict:** SURVIVES

Filter note (verbatim substance): the four required properties can coexist because the note splits the work. Structure-only types cannot filter by topic relevance, so the description must. "However, it moves most of the relevance-filtering load onto the description … the note opens by framing types as the thing that solves routing."

**Composition friction — thinnest joints:**
1. "Without types, an agent must either load everything (wasteful) or guess what's relevant (error-prone)." — UNSUPPORTED — This is a false dichotomy. Without types, an agent can still route by description, title, filename, directory or search. The note never shows what routing failure remains when descriptions exist but types do not.
2. "This is why [description is the most important field]" — THIN — The preceding paragraph promotes the *type*. The description's primacy follows from its instance-level filtering role, which is only asserted in the next sentence. The connective points at the wrong ground.
3. "Together they let an agent narrow from hundreds of files to the few it needs without opening any of them." — THIN — This needs descriptions that discriminate among same-type documents. It also needs the agent to know what each type name affords, which has its own context cost. "Without opening any" is too strong: the few documents selected must still be opened, so this is pruning.
4. "The verifiability criterion is what makes this work: types must assert structural properties, not subject matter." — THIN — The example shows that subject-matter types are uninformative. It does not show that *verifiability* is what makes routing work. "Verifiable" and "structural" are merged, and "what makes this work" claims necessity where the argument supports only usefulness.
5. "descriptions don't appear spontaneously; the type system is what makes them exist." — THIN — Enforcement guarantees presence, not filter quality, and joint 3 depends on quality.

For the human (verbatim): "Look first at the opening dichotomy (joint 1). Concretize what a type adds to routing beyond what a good description already does. If the answer is small, the title's credit to types, and the 'This is why' link to description primacy, both need to be reworked."

**Premise decomposition — premises:**
1. "An agent can read a document's type without opening the document" — DOUBTFUL — `type:` is a frontmatter field. The navigation surfaces in use (`rg` over titles/descriptions, generated indexes, tag READMEs) usually show title and description, not type. The note never names the surface that delivers the type before opening. — LOCAL — instance
2. "Types discriminate among the documents an agent is choosing between, so knowing the type changes the routing decision" — DOUBTFUL, close to DEFEATED for this KB's theory collection — about 395 of about 440 `kb/theory/` files are `types/note.md`. Within a collection the type is nearly constant. `spec` and `index` are not current shared types. Across collections, directory placement already conveys most of the signal. — GLOBAL — prevalence
3. "The type's structural promise maps onto an operation the agent wants to perform" — DOUBTFUL — This holds for strongly structured types (`structured-claim`, `instruction`, `ingest-report`). The base `note` type promises little, and "the most common type commits to the least". — LOCAL — prevalence
4. "Without types, an agent must either load everything or guess" — DEFEATED — A third route is titles, descriptions, directory placement, search hits and link context, none of which needs types. Only "without any pre-open metadata" forces the dichotomy. — LOCAL — instance
5. "Agents are stateless across sessions, so they cannot route from memory of prior reads" — HOLDS — Persistent memory is itself pre-open metadata, and the hunt found no case where it removes the need to decide what to open.
6. "Descriptions function as instance-level retrieval filters" — HOLDS with a caveat — The premise depends on the filter-form rule being followed. Filter quality depends on writing discipline, not on type.
7. "Verifiable (structural) types are what make type-based routing informed rather than blind" — HOLDS — This strengthens premise 3 but does not rescue premise 2.
8. "The type system is what makes descriptions exist reliably" — DOUBTFUL — A universal schema or linter rule could enforce descriptions without a type taxonomy. — LOCAL — instance

For the human (verbatim): "Look first at premise 2. In this KB's own theory collection almost every document is `types/note.md`, so type barely discriminates during routing, and descriptions, titles and directories do the narrowing. Decide whether the note should claim that types give a coarse affordance prior across collections, or argue for a richer populated type set."

## Gate findings

### compression
| Gate | Result | Finding |
|---|---|---|
| compression/core-claim-obscured | INFO | The type/description split, which is the sharpest claim, sits in para 3 and is missing from the title and opening. The author must choose between types and the pair. |
| compression/branch-bloat | PASS | Each side paragraph supports the routing claim and delegates by link. |
| compression/detail-overhang | PASS | The examples are one clause each and do contrastive work. |
| compression/marginal-value-redundancy | WARN | "Informed routing" closes three paragraphs. The last sentence of para 4 restates its opening. The closer of para 2 previews para 3. |

### accessibility
| Gate | Result | Finding |
|---|---|---|
| accessibility/jargon-persistence | PASS | Recurring terms stay grounded. |
| accessibility/notation-opacity | PASS | Type names are decoded locally. |
| accessibility/undefined-terms | PASS | low: "type" and "description" are not glossed as frontmatter fields on first mention. |
| accessibility/unidentified-references | PASS | No proper nouns. |

### complexity
| Gate | Result | Finding |
|---|---|---|
| complexity/claim-to-section-ratio | PASS | No sections. Each paragraph adds a step. |
| complexity/connection-inflation | WARN | The `note base type` footer entry repeats the inline link and its framing, with no typed relation. |
| complexity/could-be-a-paragraph | PASS | Already compact. |
| complexity/framework-decoration | PASS | The examples are illustrative, not decorative. |

### frontmatter
| Gate | Result | Finding |
|---|---|---|
| frontmatter/claim-strength | WARN | The title is close to a truism. The contestable points (structure rather than subject matter; type+description enough to route) stay in the body. Suggested titles: "Types route agents only when they promise structure, not subject matter" and "Type and description together let agents route without opening documents". |
| frontmatter/description-discrimination | PASS | The description adds the type/description division of labour. |
| frontmatter/title-as-claim | PASS | The title is a proposition. |
| frontmatter/title-body-alignment | PASS | low: mild scope widening. The body culminates in the pair, while the H1 names only types. |
| frontmatter/title-composability | PASS | Composes in since/because frames. |

### prose
| Gate | Result | Finding |
|---|---|---|
| prose/anthropomorphic-framing | PASS | Conventional shorthand. |
| prose/bridge-paragraph-duplication | PASS | No sections. |
| prose/confidence-miscalibration | WARN | The forced dichotomy "must either load everything or guess". The scale/outcome claim "hundreds … without opening any" has no evidence. INFO: "Agents are stateless" is stated universally. "Types solve this" overstates. |
| prose/mannered-prose | PASS | Plain prose. |
| prose/orphan-references | PASS | "Hundreds" is illustrative. |
| prose/proportion-mismatch | PASS | INFO: the description paragraph shifts emphasis slightly toward descriptions. |
| prose/pseudo-formalism | PASS | None. |
| prose/redundant-restatement | PASS | INFO: para 3 restates the type's role in one clause. |
| prose/source-residue | PASS | The examples are marked as illustration. |
| prose/unbridged-cross-domain | PASS | None. |

### semantic
| Gate | Result | Finding |
|---|---|---|
| semantic/completeness-boundary-cases | WARN | The base `types/note.md` type is the simplest and dominant case, and there the type half supplies almost no operational hint. INFO: traits, title and path are unplaced. Present but misleading metadata is not covered. |
| semantic/conceptual-role-conflation | PASS | INFO: "the type system" is ambiguous between spec and validator. Below materiality. |
| semantic/epistemic-status-blur | PASS | INFO: "narrow … without opening any" reads as an established capability, but its status is recoverable. |
| semantic/explanatory-reach | PASS | INFO: the type's own half of the mechanism is not hard to vary. No case shows the description alone leading to a wrong load. Two mechanisms (direct hint versus enforced descriptions) are not separated. |
| semantic/grounding-alignment | WARN | "description is the most important field" is attributed to `kb/types/note.md`, which only says "Discriminating retrieval filter, not a summary". INFO: the verifiability note credits types *and traits*. Enforcement guarantees presence, not discrimination. |
| semantic/internal-consistency | PASS | INFO: "structural hints" drifts to cover descriptions in para 5. There is tension between the opening dichotomy and para 3's credit to descriptions. |
| semantic/load-bearing-qualifiers | PASS | "Structural", "before opening" and "agents" are load-bearing. |
| semantic/underspecified-assertions | WARN | "Without types" can mean (A) without the type field, with descriptions present, which makes the premise doubtful, or (B) without a type system at all, which makes the type's role indirect. The reading chosen changes which mechanism carries the title. |
| semantic/unearned-generality | PASS | "Structural hints" is an earned abstraction. |
| semantic/unwarranted-scope | WARN | The title invites reliance across all types. The derivation covers only types that assert structure, not the base `note` type. Suggests a `## Scope` section. INFO: the "without opening any" efficacy outcome is not derived. |

### sentence
| Gate | Result | Finding |
|---|---|---|
| sentence/clause-packing | PASS | Short sentences. |
| sentence/concept-attribution | PASS | Concepts match. The ranking problem is left to link text. |
| sentence/framing-mismatch | PASS | INFO: the "Without types" framing makes types look like the sole remedy. |
| sentence/misleading-link-text | WARN | The link text "description is the most important field" asserts a ranking that `kb/types/note.md` does not make. The footer repeats it. |
| sentence/parsing-ambiguity | PASS | Direct-speech "this" inside indirect speech is slightly awkward but not ambiguous. |
| sentence/stock-phrases | PASS | INFO: "The structural promise is what makes the routing decision informed rather than blind" is nearly removable. |

### structural
| Gate | Result | Finding |
|---|---|---|
| structural/bullet-capitalization | PASS | The lowercase "note base type" label is consistent with the list. |
| structural/compound-bullet | PASS | None. |
| structural/general-before-specific | PASS | General before specific. |

## Connection candidates

- grounds -> `kb/theory/agents-navigate-by-deciding-what-to-read-next.md` — the note's "informed routing decision" is that note's follow/skip decision. It also supplies the missing condition: a cue helps only when its diagnosticity repays its context cost.
- grounds -> `kb/theory/agent-statelessness-makes-routing-architectural-not-learned.md` — argues the opening statelessness premise, which this note asserts without support.
- extends -> `kb/theory/pointer-design-tradeoffs-in-progressive-disclosure.md` — descriptions are fixed write-time pointers that can go stale, which bounds "without opening any".
- extends -> `kb/theory/link-following-and-search-impose-different-metadata-requirements.md` — scopes where type and description carry the whole decision: in search, yes; in link-following, surrounding prose adds hints.
- extends -> `kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md` — beyond per-document filtering, descriptions become the compressed representation used for orientation.
- mechanism -> `kb/theory/addressability-grain-sets-a-matched-selective-read-floor.md` — explains why routing by description saves reads and when that fails (the description must suffice). Reciprocal of an existing inbound edge.
- extends -> `kb/theory/rule-based-context-selection-needs-a-pre-existing-signal.md` — separates the two halves: `type` is a rule-ready signal, while description-based instance choice needs inference.
- defined-in -> `kb/theory/definitions/context-engineering.md` — "routing" is used in this definition's technical sense, without a link.
- exemplifies -> `kb/theory/information-value-is-observer-relative.md` — type and description are observer-shaped views for the "should I read this?" decision.
- Bidirectional: `kb/theory/information-value-is-observer-relative.md` (its unlinked "Descriptions as retrieval filters" bullet could link here); `kb/theory/rule-based-context-selection-needs-a-pre-existing-signal.md` (names "type" as a rule-ready signal without saying where it comes from).
- Reverse edges (rests-on): `kb/reference/navigation.md` line 25 (descriptions as "fixed, agent-facing filters"); `kb/instructions/fix-warnings/fix-descriptions.md` (restates the rationale nearly verbatim and links no theory).
- Index membership (optional): `kb/tags/context-engineering-README.md` under "Core Claims"; the head is selective.

Add these only after the claim is settled, because several (pointer-design, link-following, addressability-grain) supply the failure conditions a revised claim would need.

## Open items

- **Author decision (deciding the revise):** which claim the note makes: candidate 1 (the pair), candidate 2 (types scoped to structural promises, with base `note` as the `Any` boundary), or candidate 3 (statistical: descriptions and titles do most routing, types give a coarse prior). The friction and premise "For the human" lines both point here.
- Premise 1 (routed): name the surface that shows `type` before opening. The usual surfaces (`rg` over titles/descriptions, generated indexes) show title and description, not type. This bears on every candidate claim.
- Titles are a pre-open routing layer the note does not mention (connect Flags; critique constructive finding; completeness-boundary-cases INFO). See `kb/theory/title-as-claim-enables-traversal-as-reasoning.md`.
- Traits as the hint carrier for base-typed notes (critique; completeness-boundary-cases INFO; grounding-alignment INFO: the verifiability target credits "types and traits").
- Present but misleading metadata (a non-discriminating description, a misclassified type) is not covered by the enforcement paragraph (completeness-boundary-cases INFO; friction joint 5).
- Stale examples propagate: `kb/theory/why-notes-have-types.md:13` repeats `spec`/`index` and "without opening any of them". `kb/theory/document-types-should-be-verifiable.md` line 14 may still route subject matter to a retired `areas` field (connect, unverified).
- "Agents are stateless" could be narrowed to "has not yet read the candidates in the current context" (critique secondary; confidence-miscalibration INFO). Premise 5 HOLDS at the level the note needs, so this is optional.
- Corroboration opportunity: the pruning-accuracy signal in `kb/theory/quality-signals-for-kb-evaluation.md` describes a test of the type's marginal routing value (connect Flags).
