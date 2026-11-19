---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: 59235341a958e65294c4656bfe1d2699b38544cfae3d4297cc2df141a8e10345
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: f89c39834f0641958aafe179fbb54945
completed-at: '2026-11-12T09:58:02Z'
---
### Summary

The note explains one mechanism: metadata read before a document is opened lets an agent decide whether to load it. Most sentences frame that mechanism at the right level. The opening problem statement credits the solution to types alone, while the note's own argument shows that description does most of the narrowing. This emphasis does not exclude the cases the mechanism covers, because paragraph three restores description's role, so it is informational.

### Findings

- INFO: "Without types, an agent must either load everything (wasteful) or guess what's relevant (error-prone)." followed by "Types solve this by giving agents structural hints..." The mechanism is pre-open metadata in general. Paragraph three says that description, not type, picks "which instance" is relevant and that the two together do the narrowing. Framing the problem as "without types" makes types look like the sole remedy and passes over descriptions, titles and search as other pre-open signals. Because the note later credits description explicitly, this emphasises one part of the mechanism rather than excluding the others.
- INFO: "'This is a design note' tells an agent nothing it can act on — every note in a design KB is about design." This is framed for a design KB, but the general point (subject-matter labels do not discriminate within a collection about that subject) stays clear from context. It is an example, not a narrowed claim.

### Suggested Revision

Optionally reframe the opening problem around pre-open metadata: "Without metadata it can read before opening a document, an agent must either load everything (wasteful) or guess what's relevant (error-prone). Types and descriptions solve this..."

## Result: PASS
