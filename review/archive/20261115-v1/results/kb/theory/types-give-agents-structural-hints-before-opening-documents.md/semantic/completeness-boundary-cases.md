---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
criterion-sha256: c18370ae5ecffb6d5e1c129d4ddf44123ef1d7287ce60811d8f53542f7c17c0e
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: fda83731e2314289ae9e403555a60d57
completed-at: '2026-11-12T09:59:11Z'
---
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
