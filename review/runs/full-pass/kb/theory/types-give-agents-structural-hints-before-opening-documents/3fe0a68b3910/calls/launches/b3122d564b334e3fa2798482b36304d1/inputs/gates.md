## accessibility/jargon-persistence: PASS

### Summary

The note is short (five body paragraphs) and its recurring vocabulary — "structural hints", "routing decision", "type", "description" — stays grounded where it is reused. "Routing" is introduced in paragraph two with its meaning spelled out ("the agent reads a type and description, then decides whether to load the full document"), and later uses ("routing decision informed rather than blind") sit close enough and carry enough local context to read without scrolling back. "Verifiability criterion" and "type-system enforcement" each appear once in the body and are glossed in their own sentence, so they never persist as ungrounded jargon.

### Findings

- info: "structural hints" / "structural promise" recur three times, but each use is anchored by a concrete example in the same or adjacent sentence (e.g. "This has Evidence and Reasoning sections"), so the grounding is not lost.
- info: "routing" appears in paragraphs two, four and the Relevant Notes; the term is close to its plain-language meaning (deciding which document to open) and stays recoverable at each use.

## Result: PASS

## accessibility/notation-opacity: PASS

### Summary

The note uses no formal notation or variable names borrowed from another note. The only backticked tokens are type names — `spec`, `structured-claim`, `index` — and each is immediately explained in its own sentence by what it tells an agent ("it can implement from this", "a developed argument with evidence", "a navigation hub"). The sentences are fully readable without consulting any linked note.

### Findings

- info: `spec`, `structured-claim` and `index` are identifier-style type names rather than symbolic notation, and each is locally decoded in the same sentence, so they do not create a notation-opacity barrier.

## Result: PASS

## accessibility/undefined-terms: PASS

### Summary

The note's technical terms are mostly defined or paraphrased where they first appear. "Routing decisions" is explained in the sentence that introduces it; the "verifiability criterion" is stated inline ("types must assert structural properties, not subject matter"); "type-system enforcement" is paraphrased ("descriptions don't appear spontaneously; the type system is what makes them exist"); and each example type is glossed. No active vocabulary term from `AGENTS.md` appears in the body prose (context engineering appears only as a tag). The one mild gap is that the note assumes the reader knows that "type" and "description" are metadata fields attached to each document; this is largely inferable from paragraph two ("the agent reads a type and description, then decides whether to load the full document") and paragraph three ("description is the most important field"), so it does not block understanding.

### Findings

- low: "type" and "description" are used from the first paragraphs as KB metadata fields without saying they are frontmatter fields every document carries. A reader new to the KB can infer this from context, but a short gloss on first mention would remove the guesswork.

### Suggested Revision

In paragraph two, a phrase such as "Types — a declared kind recorded in each document's metadata, alongside a one-line description — solve this by giving agents structural hints *before* opening a document." would make the fields explicit.

## Result: PASS

## accessibility/unidentified-references: PASS

### Summary

The note names no external system, tool, product, person or organization. Its references are to generic concepts (agents, types, descriptions, a "design KB") and to other KB notes via links, none of which are proper nouns requiring identification.

### Findings

- info: No proper nouns are introduced in the body; the gate has nothing to flag.

## Result: PASS

## complexity/claim-to-section-ratio: PASS

### Summary

The note has no section headings below the title: its body is five short paragraphs followed by a Relevant Notes footer. It carries several distinct non-obvious claims. Types let agents route before opening documents. Type and description split the filtering work into kind and instance. Routing works only if types assert structural properties rather than subject matter. Routing depends on enforced metadata. No section structure exists that could outnumber the claims.

### Findings

- info: Section count is zero (the footer is navigation, not an argument section). Each body paragraph adds a separate step: the problem, the type-as-hint claim, the type/description division, the verifiability condition, and the enforcement dependency. No paragraph only restates framing.

## Result: PASS

## complexity/connection-inflation: WARN

### Summary

The footer has four entries. Three of them add navigational value. `why-notes-have-types` does not appear in the body at all. The verifiability entry adds a typed "foundation" relation and a trust framing. The enforcement entry adds "enables" and a degradation consequence that the body does not state. The `note base type` entry largely restates the body's inline sentence: the same link, the same "most important field / retrieval filter" framing and no explicit typed relation. That entry is mildly inflated.

### Findings

- low: `[note base type](../types/note.md)` fails both questions. The body says "[description is the most important field](../types/note.md) — it's a retrieval filter, not a summary" and builds the routing argument on it. The footer says it "defines description as the most important field — the retrieval filter this note's routing argument depends on". It uses the same link and the same framing, and its only label is a loose verb ("defines") rather than a relationship type. It tells a reader nothing the inline citation did not.
- info: `document-types-should-be-verifiable` is linked inline with "what makes this work". The footer adds the typed "foundation" relation and frames the principle as what makes routing *trustworthy*, so it is not inflated, though the overlap is close.
- info: `type-system-enforces-metadata-that-navigation-depends-on` adds the "enables" relation and the consequence that routing data degrades without enforcement. The body does not state that consequence.
- info: `why-notes-have-types` appears only in the footer. It gives the overview context that places this note as the development of the navigation role. This is clear navigational value.

### Suggested Revision

Either drop the `note base type` footer entry, or give it a typed relation and new context. For example: "rests-on: the base type that requires description on every note; see it for what a good description must discriminate." A good description discriminates among documents of the same type.

## Result: WARN

## complexity/could-be-a-paragraph: PASS

### Summary

The note already lacks a multi-section structure: it is a title plus five short paragraphs and a footer. A one-paragraph rewrite would keep the core insight, but the gate's failure mode needs a multi-section structure that the content does not justify. That structure is absent. The paragraphs also carry a boundary condition (types must assert structural properties, not subject matter) and a dependency (routing needs enforced metadata). Both earn their place.

### Findings

- info: No section headings exist, so no section structure needs justifying. The body is about as compact as its content allows. The opening paragraph on statelessness is background, but it is one short paragraph and frames the routing problem the note answers.

## Result: PASS

## complexity/framework-decoration: PASS

### Summary

The note has no table, taxonomy, or named framework. Its only structured element is three inline examples of types (`spec`, `structured-claim`, `index`), each paired with the operation it affords. The examples make the claim concrete, showing that a type tells an agent what it can do with a document. They add no vocabulary the argument fails to use. The type-versus-description split ("what kind" versus "which instance") is a two-way distinction, and the note's routing argument uses it directly.

### Findings

- info: The three type examples are illustrations in prose, not a decorative structure. Each maps a type to an action, which is the inference the note claims types enable.
- info: The structural-versus-subject-matter contrast in the verifiability paragraph is load-bearing. It sets the condition under which type-based routing is informed rather than blind.

## Result: PASS

## frontmatter/claim-strength: WARN

### Summary

The title "Types give agents structural hints before opening documents" is a proposition, but most of it sits close to a truism. Any metadata field is visible before the document is opened, and few informed readers would deny that a type label carries some information. The contestable content is the word "structural": a type should signal structure and affordances, not subject matter, and type plus description is enough to route without loading. The body develops that point, but the title only hints at it, so a reader could take the title as "metadata is informative".

### Findings

- medium: The obvious opposite, "types give agents no information before opening documents", is not a position anyone informed would hold. That leaves "structural" as the only contestable element. Someone could argue that types in practice are topical labels, or that descriptions or search do the routing and types add little. The title does not state that position clearly enough to invite this disagreement.
- low: The note's stronger and more contestable claims stay in the body. One is that types must assert structural properties rather than subject matter to be useful for routing. The other is that type plus description lets an agent narrow from hundreds of files without opening any. The title states neither.

### Suggested Revision

Sharpen the title to the contestable point the body establishes, for example:

- `Types route agents only when they promise structure, not subject matter`
- `Type and description together let agents route without opening documents`

## Result: WARN

## frontmatter/description-discrimination: PASS

### Summary

The description goes beyond the title. It names a mechanism: the type says which operations a document affords, and the description filters among instances of that type. It also gives an implication: routing decisions can be made without loading full documents. An agent scanning a short result list could tell this note apart from neighbours about type verifiability or metadata enforcement.

### Findings

- low: The description adds the type/description division of labour, which the title does not contain. That division is the note's distinctive mechanism, so the description adds retrieval value and does not paraphrase the title.

## Result: PASS

## frontmatter/title-as-claim: PASS

### Summary

The title "Types give agents structural hints before opening documents" is a full proposition, with subject (types), verb (give), object (structural hints) and a temporal condition (before opening documents). It could be true or false, so it meets the promise of the `title-as-claim` trait.

### Findings

- None. The title is an assertion, not a topic label.

## Result: PASS

## frontmatter/title-body-alignment: PASS

### Summary

The body supports the title. Paragraph 2 states the claim directly ("Types solve this by giving agents structural hints *before* opening a document") with examples (`spec`, `structured-claim`, `index`). Paragraph 4 explains why the hints must be structural: the verifiability criterion requires types to assert structural properties rather than subject matter. The body also broadens to the pairing of type and description, and to the enforcement that makes the metadata reliable. These sections serve the title's claim and do not replace it.

### Findings

- low: There is mild scope widening. The body's culminating point is that type *and* description together let an agent narrow from hundreds of files without opening any, and the description field leads with "Types and descriptions". The H1 names only types. The description material is framed as a consequence ("This is why…"), so the drift is not large enough to misdirect a reader. If the joint claim becomes the note's centre, the title should name descriptions too.

## Result: PASS

## frontmatter/title-composability: PASS

### Summary

The title reads naturally inside linking sentence frames: "since types give agents structural hints before opening documents, descriptions can act as retrieval filters" and "because types give agents structural hints before opening documents, the type must assert structure". It needs no grammatical adjustment and works as a linkable prose fragment.

### Findings

- None. The title composes cleanly in `since [title]…` and `because [title]…` frames.

## Result: PASS

## prose/anthropomorphic-framing: PASS

### Summary

The note describes agent behaviour with verbs such as "tells", "decides", "guess", "act on" and "no memory of what they've read". In context these are conventional shorthand for an agent system's operations (loading files, selecting what to load), not claims about cognitive internals. The note does not argue about model cognition and makes no claim that depends on a mental-state reading.

### Findings

- INFO: "they start fresh every session with no memory of what they've read before" uses "memory" in the ordinary engineering sense of retained state across sessions; it is immediately glossed by "stateless", so it does not imply unsupported internals.
- INFO: "A `spec` tells an agent it can implement from this" and "tells the agent it can extract a citable argument" are conventional metonymy for metadata signalling which operations a document supports. No change needed.
- INFO: "guess what's relevant" and "decides whether to load the full document" describe selection behaviour, not belief or understanding. Acceptable shorthand.

## Result: PASS

## prose/bridge-paragraph-duplication: PASS

### Summary

The note body has no section headings below the title; it is five consecutive paragraphs followed by a Relevant Notes footer. There is no transition paragraph that previews a following section, so the failure mode cannot occur. The final body paragraph points to type-system enforcement and is not repeated by any later section; the footer annotation for that link is a link gloss, not a section that develops the same material.

### Findings

- None.

## Result: PASS

## prose/confidence-miscalibration: WARN

### Summary

The note's core mechanism (type signals affordances, description selects among instances) is a qualitative analytical move and is stated reasonably. However, the opening frames a forced dichotomy and universal premise as settled fact, and the payoff sentence makes an empirical-sounding scale claim with no evidence. These are the note's own constructions presented with assertive wording.

### Findings

- WARN: "Without types, an agent must either load everything (wasteful) or guess what's relevant (error-prone)." This asserts an exhaustive dichotomy the note does not support. Agents can also search, scan filenames, or read descriptions that exist without a type field; the note itself later credits the description, not the type, with instance-level filtering. "Must" overstates; the claim should propose that types reduce reliance on these fallbacks.
- WARN: "Together they let an agent narrow from hundreds of files to the few it needs without opening any of them." This is an empirical-sounding scale and outcome claim (hundreds → few, zero documents opened) with no cited observation or measurement. It is presented as a demonstrated result rather than an expected effect.
- INFO: "Agents are stateless — they start fresh every session with no memory of what they've read before." Stated as universal; it holds for the default session model but not for agents with persistent memory systems. A scope qualifier ("by default", "within this framework's session model") would calibrate it.
- INFO: "Types solve this" asserts a full solution where the note's own argument supports partial mitigation (routing still depends on descriptions and on enforcement, per the last paragraph).

### Suggested Revision

- "Without types, an agent falls back on loading broadly (wasteful) or selecting by filename and search hits (error-prone)."
- "Types reduce this cost by giving agents structural hints *before* opening a document."
- "Together they can let an agent narrow a large collection to a few candidates before opening any of them."
- "Agents start each session without state from earlier sessions unless a memory mechanism supplies it."

## Result: WARN

## prose/mannered-prose: PASS

### Summary

The note is written in plain, literal prose. The few figurative candidates are conventional and match their intended meaning; none adds unsupported connotations or translation effort.

### Findings

- INFO: "retrieval filter" — conventional technical term; its literal meaning (a field used to decide what to retrieve) is exactly what the note intends.
- INFO: "navigation hub" — conventional description of an index document; precise enough and used once.
- INFO: "structural promise" and "informed rather than blind" — "promise" maps cleanly to a verifiable guarantee about structure, which is the note's point; "blind" is a conventional contrast to "informed". Neither imports agency or certainty the note does not mean.
- INFO: "descriptions don't appear spontaneously" — literal enough; it means authors do not reliably add descriptions without a requirement.

## Result: PASS

## prose/orphan-references: PASS

### Summary

The note contains no numbers, percentages, named studies or cited empirical results. The only quantitative-sounding phrase is "narrow from hundreds of files to the few it needs", which is an approximate illustration of scale rather than a specific figure presented as data.

### Findings

- INFO: "hundreds of files to the few it needs" is illustrative magnitude, not a data point. It does not create the false specificity this gate targets. (Whether the claim is calibrated is a separate question for the confidence gate.)

## Result: PASS

## prose/proportion-mismatch: PASS

### Summary

The core claim is that types give agents structural hints before a document is opened, enabling routing without full loads. The body spends one paragraph on the problem, one on the core mechanism with three type examples, one on the type–description division of labour, one on the verifiability condition, and one on enforcement. The supporting paragraphs are each short and point outward to linked notes. The load-bearing material (paragraphs 2–3) gets the most development; no secondary topic outgrows it.

### Findings

- INFO: The description paragraph (paragraph 3) is about as long as the type-hint paragraph and leads with "description is the most important field", which slightly shifts emphasis from the title's subject (types) to descriptions. It still supports the core claim by explaining how type and description combine, and the frontmatter description names both, so this is not a mismatch.

## Result: PASS

## prose/pseudo-formalism: PASS

### Summary

The note uses no notation, equations or formal-looking decomposition. The type examples (`spec`, `structured-claim`, `index`) are concrete identifiers, not formal apparatus, and the type/description split is stated in ordinary prose.

### Findings

- None.

## Result: PASS

## prose/redundant-restatement: PASS

### Summary

The note has no internal section headings, so there is no section opening that could re-explain a previous section. Reading the paragraphs as a sequence, each advances: problem, type hints, type/description division, verifiability condition, enforcement dependency. Paragraph 3's "The type tells the agent *what kind of thing* a document is" briefly restates paragraph 2 but only as a one-clause setup for the new description contrast.

### Findings

- INFO: Paragraph 3 re-states the type's role in one clause before introducing the description's role. This is a short transition, not a full re-explanation.

## Result: PASS

## prose/source-residue: PASS

### Summary

The title and opening claim generality over agents working with typed document collections. Domain-specific vocabulary in the body — the type names `spec`, `structured-claim`, `index`, the "Evidence and Reasoning sections" example, and "every note in a design KB is about design" — is presented as illustration, introduced with "A `spec` tells..." or quoted as contrasting examples. None of it leaks in unmarked to narrow the claim.

### Findings

- INFO: "This has Evidence and Reasoning sections" ties the structural-property example to one particular type's section layout. It is quoted as an example of a structural assertion, so it reads as illustration rather than a commitment of the general claim to that type.

## Result: PASS

## prose/unbridged-cross-domain: PASS

### Summary

The note cites no studies or empirical results from any domain. Its support comes from internal KB links (verifiability, type-system enforcement, the note base type), all within the same domain as the argument: agent navigation of typed KB documents. No cross-domain transfer occurs.

### Findings

- None.

## Result: PASS

## semantic/completeness-boundary-cases: WARN

### Summary

The note sets up a two-part framework for pre-open routing. The description frontmatter states it: "the type says what operations a document affords, the description filters among instances of that type". The body illustrates the type half with three examples (`spec`, `structured-claim`, `index`). The examples are illustrative rather than an exhaustive list. The two-part division of labor is the framework under test. Most boundary cases map into it, but the simplest and most common case does not: the base `note` type, which this note itself uses. The linked verifiability note says that type does not tell an agent what it can do before opening.

### Findings

- WARN: Simplest instance — the base `types/note.md` type. The framework says the type tells the agent what operations a document affords before it is opened. The linked [verifiability note](./document-types-should-be-verifiable.md) describes the base type as "Default — read it to find out what you can do with it". Its gradient section also calls `note` the `Any` of the type system, with few body-shape claims. For this case the type half of the framework supplies almost no operational hint, so routing falls entirely on the description. This is the dominant case in the KB, and the note's own frontmatter is an instance of it. The note never acknowledges that the type contribution shrinks toward zero at this boundary. As a result, "Together they let an agent narrow from hundreds of files to the few it needs" overstates what the type contributes for most documents.
- INFO: Adjacent concept — traits. Under the linked verifiability model, much of the operational signal (`has-comparison`, `has-implementation`) is carried by traits layered on a base type, not by the base type itself. The note's "type says what operations a document affords" can absorb traits only if "type" is read loosely to include them. Coverage is possible but strained.
- INFO: Adjacent concept — title and collection path. Agents also route on titles (title-as-claim notes) and on directory or collection location before opening a document. The note's procedure ("the agent reads a type and description, then decides") does not place these signals. This is a boundary of the "type + description" pair rather than a contradiction; stating that the pair is not the only pre-open signal would be enough. Adding more categories is not warranted given the note's short argumentative role.
- INFO: Extreme instance — a structurally conforming document with the wrong semantic type, or a non-discriminating description. The note's last paragraph covers missing metadata (enforcement), but not present yet misleading metadata. The linked verifiability note treats misclassification as a review-quality problem. The framework can absorb this only by assuming that hints are trustworthy whenever they exist.

### Suggested Revision

State the boundary instead of extending the taxonomy. For the base `note` type, the type mainly signals "transferable claim; open to learn more", so the description (and title) carry the routing. Narrower types and traits are where the structural hint does real work.

## Result: WARN

## semantic/conceptual-role-conflation: PASS

### Summary

The note applies existing KB concepts (verifiability, type-system enforcement, the description as retrieval filter) to the navigation role of types. Each import is made through a link, and the note does not claim to define any of them. One compressed passage blurs the type specification and the validator that enforces it. Nearby wording and the linked note settle the roles, so the blur is not material.

### Findings

- INFO: "descriptions don't appear spontaneously; the type system is what makes them exist." "The type system" could name the type specification that creates the obligation, or the validation machinery that checks compliance. The linked enforcement note separates them ("the type creates the obligation, and `/validate` checks compliance"), and the same sentence's link text says "type-system enforcement". The attribution and the note's contribution are the same under either reading, so this falls below the materiality threshold.
- INFO: "The verifiability criterion is what makes this work: types must assert structural properties, not subject matter." This passage applies the linked criterion; it does not redefine it. The colon clause restates the imported criterion faithfully. No conflation between inherited and contributed content.

## Result: PASS

## semantic/epistemic-status-blur: PASS

### Summary

The note is a short design argument. Premises about agents (stateless, finite context) lead to a derived consequence: pre-open metadata enables informed routing. Two supporting claims are delegated to linked notes (verifiability, enforcement). It reports no observations, so no evidence can spread onto a mechanism it does not support. Most claims read as consequences of the stated premises, which is their actual status. One capability claim reads more like an observed result than a derived expectation, but the derivation it rests on is visible in the same paragraph.

### Findings

- INFO: "Together they let an agent narrow from hundreds of files to the few it needs without opening any of them." This reads as an established capability, but no observation of agents doing this is presented. It is recoverable as a consequence of the preceding premises: types say what kind of document something is, and descriptions discriminate instances. However, "without opening any of them" depends on an unstated assumption that descriptions are discriminating enough. The linked enforcement note treats that as a judgment-level check that the type system does not guarantee. The status is recoverable with effort; it is not misrepresented.
- INFO: "Without types, an agent must either load everything (wasteful) or guess what's relevant (error-prone)." This dichotomy is presented as a plain fact, but it is a derived claim from the stated premises. Readers can recover this from its position as the opening premise of the argument.

## Result: PASS

## semantic/explanatory-reach: PASS

### Summary

The central claim is that types give agents structural hints before they open documents. The note offers a mechanism. Agents start each session with no memory and have finite context, so the decision to load must be made from metadata. A type that asserts a structural property (not subject matter) tells the agent which operations the document affords, and the description discriminates among instances. The verifiability paragraph gives the mechanism some hard-to-vary content. Replace the structural type with a subject-matter label ("design note") and the conclusion fails, which the note itself shows. The claim is falsifiable: subject-matter types giving equally good routing, or types adding nothing beyond descriptions, would count against it. The mechanism for the type's own contribution, as distinct from the description's, is thinner.

### Findings

- INFO: Varying a premise the note uses: remove the type and keep the description. The note's own reasoning says the description does the instance-level filtering and calls it "the most important field". The note does not explain what routing decision the type changes once a discriminating description and title are present. The illustrations (`spec` → implement, `structured-claim` → extract argument) show the type selecting an operation. They do not show a case where the description alone would have led to the wrong load decision. So the type's half of the mechanism is plausible but not yet constrained enough to be hard to vary.
- INFO: The opening dichotomy ("load everything or guess") treats the type as necessary for informed routing. The final paragraph then makes the type's role partly indirect: the type system makes descriptions exist. That indirect route is a real mechanism, but it explains enforced descriptions rather than "structural hints". The note does not separate which of these two mechanisms the title claim rests on.
- INFO: No ad-hoc accommodation found. The note adds no escape-hatch qualifiers.

## Result: PASS

## semantic/grounding-alignment: WARN

### Summary

The note uses four linked library artifacts. Three are represented at the scope their targets claim: the verifiability note, the type-system-enforcement note, and the context link to the why-notes-have-types overview. The link to the note base type is used to ground a ranking claim, "description is the most important field". The target does not make that claim. It supports only the "retrieval filter, not a summary" characterization.

### Findings

- WARN: "This is why [description is the most important field](../types/note.md) — it's a retrieval filter, not a summary." The Relevant Notes entry repeats the claim: "defines description as the most important field". The target type spec lists `description` as a required field and gives its use as "Discriminating retrieval filter, not a summary". Its Description section says it "should answer 'why this document?' for a future retrieval decision". The target ranks no field above the others and never calls description the most important. The retrieval-filter half of the claim is grounded. The "most important" ranking is presented as defined by the target but is the note's own inference. (Whether the link text itself misleads is for `sentence/misleading-link-text`. The finding here concerns the Relevant Notes annotation and the sentence's evidential use: they present the ranking as coming from the target.)
- INFO: "The [verifiability criterion](./document-types-should-be-verifiable.md) is what makes this work: types must assert structural properties, not subject matter." This is accurately represented. The target's opening section makes this claim with the same "design note" contrast. The target also states the navigation link explicitly ("types and traits are precisely the hints that make those decisions informed rather than blind"). Note that the target credits *types and traits* jointly; this note says types alone. This is a minor narrowing, not an overextension.
- INFO: "That's the role of [type-system enforcement](./type-system-enforces-metadata-that-navigation-depends-on.md) — descriptions don't appear spontaneously; the type system is what makes them exist." This is accurately represented. The target's title and opening paragraph make this claim nearly verbatim. The target adds that validation checks presence, while whether the description is discriminating "remains a judgment-level check". This note's routing argument depends on discriminating descriptions, and the enforcement link does not supply that.
- INFO: [why-notes-have-types](./why-notes-have-types.md) is an adjacent context link with no evidential load. It passes.

### Suggested Revision

Either drop the "most important" ranking or present it as this note's own inference from the retrieval-filter role. Keep the link for the "retrieval filter, not a summary" characterization, which the target supports. Revise the Relevant Notes annotation to match.

## Result: WARN

## semantic/internal-consistency: PASS

### Summary

The note's five short paragraphs do not directly contradict one another. One term drifts: "structural hints" first means type-provided hints about document structure. The final paragraph then makes the hints depend on descriptions, which the note itself classes as instance filters rather than structural properties. A smaller tension sits between the opening dichotomy and the credit given to descriptions.

### Findings

- INFO: Definition drift in "structural hints". Paragraph 2 introduces structural hints as what types give ("A `spec` tells an agent it can implement from this"). Paragraph 4 sharpens this: types "must assert structural properties, not subject matter". Paragraph 5 says "these structural hints only work if the metadata exists reliably" and goes on to discuss descriptions only. Descriptions, per paragraph 3, tell the agent "which instance" — they are subject-matter discriminators, not structural properties. A reader cannot tell whether "structural hints" covers descriptions or only types. A human should confirm which is meant.
- INFO: Tension between the opening and paragraph 3. The opening says "Without types, an agent must either load everything ... or guess". Paragraph 3 calls the description "the most important field" and gives it the work of narrowing "from hundreds of files to the few it needs". Taken together, an agent with descriptions but without types would not be forced into the dichotomy. Paragraph 5 partly reconciles this by saying the type system is what makes descriptions exist. The reconciliation is implicit, though, and the title still credits types with the hints.
- INFO: The description frontmatter says "the type says what operations a document affords". Paragraph 3 says "the type tells the agent *what kind of thing* a document is". Paragraph 2 links the two through examples, so this is compression rather than drift.

## Result: PASS

## semantic/load-bearing-qualifiers: PASS

### Summary

The qualifiers in the title and description are "structural", "before opening documents", "agents", and "without loading full documents". Each does work in the argument. "Before opening" is the core of the routing claim. "Structural" is load-bearing through the verifiability paragraph: subject-matter labels are explicitly shown to fail ("This is a design note" tells an agent nothing it can act on). "Agents" ties to the premises the argument uses (stateless sessions, finite and expensive context).

### Findings

- INFO: "Agents" could arguably be widened to any reader with limited attention, since human readers also route by metadata. The note's premises, however, are agent-specific (no memory across sessions, context cost), and the KB is plainly scoped to agent-operated KBs. This is intentional domain scoping, not a narrowing qualifier without work to do.
- INFO: Deletion test on "structural": "Types give agents hints before opening documents" would admit subject-matter types. The note argues explicitly that such types do not support informed routing. The qualifier is therefore load-bearing and should stay.

## Result: PASS

## semantic/underspecified-assertions: WARN

### Summary

Most assertions are resolved by nearby context. The illustrations make concrete what each type tells the agent, and the verifiability paragraph defines what "structural" excludes. One premise in the opening paragraph remains open between two readings that change its truth and the role it plays in the argument.

### Findings

- WARN: "Without types, an agent must either load everything (wasteful) or guess what's relevant (error-prone)." Unresolved choice: the scope of "without types".
  - Reading A: without the `type` field specifically, with descriptions and titles still present. Under this reading the premise is doubtful by the note's own account. Paragraph 3 credits the description with narrowing "from hundreds of files to the few it needs", so an agent with descriptions but no types would not be forced to load everything or guess. The premise would then support a claim about the type field's direct routing value. That claim needs evidence that the type adds something beyond the description.
  - Reading B: without a type system at all, and therefore (per paragraph 5) without reliably present descriptions. Under this reading the premise is plausible. But it supports a claim about enforced metadata in general, and the type's contribution would be largely indirect: it makes descriptions exist. That is a different mechanism from the "structural hints" in the title.
  - Choosing a reading changes the conditions under which the premise is true, and changes which of the note's two mechanisms carries the title claim.
- INFO: "Together they let an agent narrow from hundreds of files to the few it needs without opening any of them." "Without opening any of them" could mean the agent reads no full document while selecting, or that the final selection is right with no corrective opening. The paragraph's framing ("decides whether to load") favors the first reading. The difference is probably not material to the note's argument.

### Suggested Revision

State which counterfactual the opening premise means. Either "without type metadata" (field-level, with descriptions present) or "without an enforced type system" (no reliable metadata at all). Then make sure the title claim rests on the matching mechanism.

## Result: WARN

## semantic/unearned-generality: PASS

### Summary

The central claim's vocabulary sits at the level the argument uses. "Types" means the KB's document types, and the examples are concrete types (`spec`, `structured-claim`, `index`). "Agents" means LLM agents with stateless sessions and finite context, which are the premises the argument uses. "Documents" covers notes, specs and indexes, which the examples span, so downgrading to "notes" would drop the `spec` and `index` illustrations. "Structural hints" is the one abstraction. The verifiability paragraph earns it: it names what the abstraction forbids (subject-matter labels such as "design note").

### Findings

- INFO: Forbids test on "structural hints". The abstract wording rules out subject-matter typing as a routing aid, and the concrete examples alone would not rule it out. This is an earned abstraction. Abstraction is concentrated in this one load-bearing site rather than spread across the prose.

## Result: PASS

## semantic/unwarranted-scope: WARN

### Summary

Claimed scope: for agents navigating a typed KB, document types (together with descriptions) supply structural hints before opening. These let an agent "narrow from hundreds of files to the few it needs without opening any of them". The title says "types" without restriction, so a reader would take the claim to cover every document type in such a KB. The support on the page is derivation from premises (stateless agents, finite context, verifiable structural types), plus inherited results from the verifiability and enforcement notes. There is no direct evidence or worked case.

The derivation reaches types that make a structural promise, illustrated by `spec`, `structured-claim` and `index`. It does not reach the base `note` type. The note does not acknowledge that type, yet it is the KB's default and the type of this note itself. The linked verifiability note describes it as "Default — read it to find out what you can do with it", which is a type that gives no pre-open operational hint. The derivation also does not cover the efficacy claim "without opening any of them". That claim depends on descriptions being discriminating, which the linked enforcement note says the type system does not guarantee ("remains a judgment-level check"). There is no Scope section, no transfer argument and no conjecture marking for either surplus.

### Findings

- WARN: The title and description invite reliance on "types" giving pre-open structural hints across all document types. The supporting derivation only covers types that assert a distinctive structural property. The note gives no transfer relation to the base `note` type, which most documents use, and marks no boundary for it. For those documents the hint comes almost entirely from the description, which is not what the title credits.
- INFO: "Together they let an agent narrow from hundreds of files to the few it needs without opening any of them" is a supporting claim. It presents an efficacy outcome that the derivation does not exercise. The premises establish that routing is *informed*, not that it is complete without opening. That would require discriminating descriptions, which linked material says are not enforced.

### Suggested Revision

Add a `## Scope` section. It should state that the structural hint is carried by narrower types and traits. For the base `note` type, routing rests mainly on the description and title. The "without opening any" outcome also depends on descriptions being discriminating, which validation does not check.

## Result: WARN

## sentence/clause-packing: PASS

### Summary

The note's sentences are short and mostly carry one or two clauses each. No sentence approaches 40 words with more than two or three independent ideas, and no long interrupting clause or list separates a subject from its verb or a verb from its object.

### Findings

- INFO: The longest sentence ("The type tells the agent *what kind of thing* a document is; the description tells it *which instance* among documents of that kind is relevant to the current task.") is about 30 words. It joins two parallel clauses with a semicolon, and each dependency closes quickly, so it is not overloaded.
- INFO: "These hints enable informed routing decisions: the agent reads a type and description, then decides whether to load the full document." The colon introduces a short two-step sequence; the reader holds no long dependency open.

## Result: PASS

## sentence/concept-attribution: PASS

### Summary

The note makes three identity-style attributions to linked notes: the verifiability criterion, type-system enforcement, and the note base type's treatment of description. All three targets resolve. The verifiability and enforcement attributions match their targets. The description attribution matches in its core concept (a retrieval filter, not a summary), though the target does not rank description as the most important field. That ranking is a link-text and annotation problem, not a different concept, so it does not fail this gate.

### Findings

- INFO: "The [verifiability criterion](./document-types-should-be-verifiable.md) is what makes this work: types must assert structural properties, not subject matter." The target's title and opening section state exactly this criterion, including the same "design note" example. Its body also says types are "the hints that make those decisions informed rather than blind", which matches this note's use. Valid.
- INFO: "That's the role of [type-system enforcement](./type-system-enforces-metadata-that-navigation-depends-on.md) — descriptions don't appear spontaneously; the type system is what makes them exist." The target opens with nearly the same sentence and assigns itself the role of "ensuring the routing data exists at all." Valid.
- INFO: "This is why [description is the most important field](../types/note.md) — it's a retrieval filter, not a summary." The target's frontmatter table defines `description` as "Discriminating retrieval filter, not a summary," so the identified concept (description as retrieval filter) matches. The target never calls description the *most important* field. That ranking is unsupported, but the concept itself is the same. The misleading-link-text gate covers this problem.

## Result: PASS

## sentence/framing-mismatch: PASS

### Summary

The note explains one mechanism: metadata read before a document is opened lets an agent decide whether to load it. Most sentences frame that mechanism at the right level. The opening problem statement credits the solution to types alone, while the note's own argument shows that description does most of the narrowing. This emphasis does not exclude the cases the mechanism covers, because paragraph three restores description's role, so it is informational.

### Findings

- INFO: "Without types, an agent must either load everything (wasteful) or guess what's relevant (error-prone)." followed by "Types solve this by giving agents structural hints..." The mechanism is pre-open metadata in general. Paragraph three says that description, not type, picks "which instance" is relevant and that the two together do the narrowing. Framing the problem as "without types" makes types look like the sole remedy and passes over descriptions, titles and search as other pre-open signals. Because the note later credits description explicitly, this emphasises one part of the mechanism rather than excluding the others.
- INFO: "'This is a design note' tells an agent nothing it can act on — every note in a design KB is about design." This is framed for a design KB, but the general point (subject-matter labels do not discriminate within a collection about that subject) stays clear from context. It is an example, not a narrowed claim.

### Suggested Revision

Optionally reframe the opening problem around pre-open metadata: "Without metadata it can read before opening a document, an agent must either load everything (wasteful) or guess what's relevant (error-prone). Types and descriptions solve this..."

## Result: PASS

## sentence/misleading-link-text: WARN

### Summary

I checked four distinct link targets: `../types/note.md`, `./document-types-should-be-verifiable.md`, `./type-system-enforces-metadata-that-navigation-depends-on.md` and `./why-notes-have-types.md`. All resolve. Three link texts match their targets. The link text "description is the most important field" asserts a ranking that the note base type spec does not make. The Relevant Notes annotation for the same target repeats that claim.

### Findings

- WARN: "This is why [description is the most important field](../types/note.md) — it's a retrieval filter, not a summary." The link text says the target establishes description as *the most important field*. The target, the `note` type spec, lists `description` as a required field ("Discriminating retrieval filter, not a summary"). Its Description section says the field "should answer 'why this document?' for a future retrieval decision." It never ranks description above other fields, and it lists `type` as required too. A reader who does not follow the link believes the type spec makes a priority claim it does not make. A reader who does follow it finds no such claim. The Relevant Notes entry ("defines description as the most important field") repeats the mismatch.
- INFO: "[verifiability criterion](./document-types-should-be-verifiable.md)": the target's title and first section define the criterion. Matches.
- INFO: "[type-system enforcement](./type-system-enforces-metadata-that-navigation-depends-on.md)": the target's title and opening say the type system makes descriptions exist. Matches.
- INFO: "[why-notes-have-types](./why-notes-have-types.md)" (Relevant Notes): the target is the overview of type-system roles, with Navigation as the first role. Matches the "context" annotation.

### Suggested Revision

Make the link text say what the target supports, for example: "This is why the [note type defines description as a retrieval filter, not a summary](../types/note.md)." If keeping the priority claim, assert it as this note's own conclusion, outside the link: "This makes description the most important field for routing: the [note type](../types/note.md) defines it as a retrieval filter, not a summary." Update the Relevant Notes annotation to match, for example: "defines description as a discriminating retrieval filter — the role this note's routing argument depends on."

## Result: WARN

## sentence/parsing-ambiguity: PASS

### Summary

I checked each sentence for negation scope, modifier attachment and pronoun reference. Pronouns and demonstratives resolve from local context, and no negation or modifier has a plausible second reading. One mixed direct and indirect phrasing is slightly awkward but not ambiguous.

### Findings

- INFO: "A `spec` tells an agent it can implement from this." The direct-speech "this" sits inside indirect speech. A reader could briefly look for an antecedent in the preceding text, but the only plausible reading is "from the spec document." The same holds for "An `index` tells it this is a navigation hub."
- INFO: "This is why [description is the most important field]..." opens a paragraph with "This". The antecedent is the routing mechanism described just before ("decides whether to load the full document"), and no competing antecedent is plausible.
- INFO: "But these structural hints only work if the metadata exists reliably." "Only" attaches to the condition ("work only if..."); no plausible reading takes it to restrict "hints" or "work".

## Result: PASS

## sentence/stock-phrases: PASS

### Summary

No sentence matches the listed stock patterns: elevation, "worth noting", "in other words", "at its core" or "key insight". One sentence that closes a paragraph is close to a summary restatement. Under the deletion test it is nearly removable, but it does not use a listed pattern, so it is noted rather than flagged.

### Findings

- INFO: "The structural promise is what makes the routing decision informed rather than blind." This closes the verifiability paragraph by restating its point in a cleft construction ("X is what makes Y"). Removing it leaves the paragraph almost as clear, because the preceding sentences already contrast a non-actionable label with an actionable structural one. It is not a listed stock pattern, and it ties the paragraph back to routing, so it is not reported as WARN.
- INFO: "This is why description is the most important field — it's a retrieval filter, not a summary." The "X, not Y" contrast is not the elevation move ("not just X — it is Y"). It states a definitional distinction that the paragraph relies on, so it fails the deletion test: removing it loses content.

### Suggested Revision

Optionally delete "The structural promise is what makes the routing decision informed rather than blind.", or fold it into the previous sentence: "'This has Evidence and Reasoning sections' tells the agent, before opening the document, that it can extract a citable argument."

## Result: PASS

## structural/bullet-capitalization: PASS

### Summary

The note's only bullet list is the "Relevant Notes" footer. Each of its four items begins with a link. Three link labels are lowercase file slugs, which count as identifiers. The fourth label, "note base type", is lowercase prose. It matches the lowercase link-label convention of the list, so it is a stylistic edge case, not a capitalization failure.

### Findings

- INFO: The bullet `[note base type](../types/note.md) — defines description ...` starts with a lowercase prose link label. The sibling bullets start with lowercase slug identifiers, so the lowercase start is consistent with the list. Capitalizing it as "Note base type" would be optional.

## Result: PASS

## structural/compound-bullet: PASS

### Summary

The note's only bullets are the four "Relevant Notes" entries. Each is well under 30 words and has the form of a link, a relation label and a short gloss. The type-system-enforcement entry joins two clauses with a semicolon: "descriptions exist because the type system requires them; without enforcement, routing data degrades". Both clauses state one dependency, once positively and once as its contrapositive. They are not two separable claims.

### Findings

- INFO: No compound bullets found.

## Result: PASS

## structural/general-before-specific: PASS

### Summary

The note has no internal section headings below the title, so there are no adjacent section pairs to compare. Its paragraph order already moves from general to specific. First comes the problem: stateless agents with finite context. Next comes the general mechanism, that types give structural hints before a document is opened. That paragraph then gives examples (`spec`, `structured-claim`, `index`). After it come the role of descriptions, the verifiability criterion and the enforcement dependency. No specific case comes before the rule it exemplifies.

### Findings

- INFO: No specific-before-general ordering found. The note has only one body section, and its paragraphs present the general claim before the examples.

## Result: PASS
