---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: 3fe0a68b3910f29f1cfa9d267064142fabbddb9a9348e514bd179871862e098b
criterion: kb/instructions/critique-note.md
criterion-sha256: 6a402875150a2649f57275adda6ca69ae7669f0b06ef57a14b0685e5ff6ab220
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: ee3a330d62144a4db422efd273ab1b2a
completed-at: '2026-11-12T09:58:42Z'
---
# Critique: Types give agents structural hints before opening documents

**Note:** kb/theory/types-give-agents-structural-hints-before-opening-documents.md
**Central commitment:** A document's type, paired with its description, lets an agent make informed routing decisions without loading the full document: the type says what operations the document affords, and the description picks the relevant instance.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

An informed opponent would take the **search-first agent-navigation stance**: agents route by lexical or semantic search over titles, descriptions and body text, and genre labels carry little routing signal. This is the stance behind grep-first coding agents and much RAG practice. Applied to this KB, the argument runs as follows.

1. **The modal type carries almost no structural hint.** The note's own linked foundation, [document-types-should-be-verifiable](./document-types-should-be-verifiable.md), puts `types/note.md` at the `Any` end of the gradual-typing spectrum. Its table describes this type as "Default — read it to find out what you can do with it." Most theory notes, including this note and both notes it links for support, are `types/note.md`. For the bulk of the collection, then, the type field tells the agent nothing that changes a routing decision. The agent still has to read the content, or at least the description and title, to learn what the document affords. The note's examples (`spec`, `structured-claim`, `index`) are exactly the minority types that do assert structure, so the illustration overstates the typical case.

2. **The routing work is done by the description and title, not the type.** When `type` is near-constant across candidates, it cannot discriminate among them. The note's own decomposition ("type says what kind of thing; description says which instance") implies that the type does no work when every candidate has the same kind. Only the description then filters, and this KB's navigation guidance ("scan scoped titles and descriptions") reflects that. Title-as-claim titles also carry much of the filtering, and the note does not mention them. Where a type does differ, it is often redundant with location: ADRs live in `kb/reference/adr/` and generated indexes are recognisable by path. The directory has already done the routing before any type is read.

3. **The type's real contribution is indirect.** On this reading, types matter for navigation mainly because the type contract *forces descriptions to exist*. That is the claim of the sibling note [type-system-enforces-metadata-that-navigation-depends-on](./type-system-enforces-metadata-that-navigation-depends-on.md). It is not the claim made by this note's title. The title says the type itself is a pre-opening hint, and for most documents that is false.

This objection can't be dismissed in one sentence. It uses the KB's own type-spec description of `types/note.md` and the actual distribution of types in the collection the note sits in.

## How the note engages it

**Partially engaged.**

- Paragraph 3 separates the type's role ("what kind of thing") from the description's role ("which instance"). This concedes that the description does the instance-level filtering, but it never says how often the type is uninformative.
- Paragraph 4 (verifiability) argues that types must assert structural properties to be useful. That supports the attack more than it answers it: by that standard, the default `note` type asserts almost nothing.
- Paragraph 5 hands off to the enforcement note. It recognises that the indirect role exists, but presents it as a precondition for the type-as-hint mechanism rather than as possibly the main mechanism.

The note never addresses the base-type-as-`Any` case, the near-constant type distribution, or redundancy with path and title.

## Constructive findings

- State the scope of the claim. Specialised types (structured-claim, ADR, generated index, instruction) give an operation-level hint before opening. The base `note` type mostly does not, and for those documents routing depends on title and description. One sentence acknowledging that `types/note.md` is the `Any` case would turn the objection into a stated boundary.
- Include traits explicitly as the mechanism that adds hints to base-typed notes. The verifiability note says traits (`has-comparison`, `title-as-claim`) carry the operation-level signals that a bare `note` type lacks. Without traits, the note's claim depends on rare specialised types.
- Name the title as a routing field next to the description, given the title-as-claim convention. Otherwise the "type + description" pair understates what an agent actually scans.
- Consider retitling or adding a qualifier so the headline does not imply that every type gives a useful hint. For example: types and descriptions let agents route before opening, and specialised types add operation-level hints.

## Secondary objections (optional)

- **Grounding of "the most important field."** The note links [description is the most important field](../types/note.md), but the linked type spec calls the description a "Discriminating retrieval filter, not a summary." It does not rank it as the most important field. The link supports the retrieval-filter claim but not the superlative.
- **Stale type examples.** `spec` and `index` are written as current type names, but the verifiability note records `spec` as part of the retired flat enum and lists the current listing type as `generated-index`. A reader routing by these names would not find them as path-valued types.
- **"Without opening any of them" is overstated.** Type and description are in the file's frontmatter, so an agent still reads part of each file, whether through a grep over frontmatter or a generated index. The saving is real (frontmatter costs far less than the body), but it is a cost reduction, not avoiding the file. The note should say which access path it assumes.
- **"Agents are stateless" is too general.** Many agent harnesses keep memory or session state. The argument only needs the narrower premise that the agent has not yet read the candidate documents in the current context.

## Result: REPORT
