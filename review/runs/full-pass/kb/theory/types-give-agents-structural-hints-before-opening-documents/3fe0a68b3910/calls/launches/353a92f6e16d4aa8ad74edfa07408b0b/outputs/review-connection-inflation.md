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
