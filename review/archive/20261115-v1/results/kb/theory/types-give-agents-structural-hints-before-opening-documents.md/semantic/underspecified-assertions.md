---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: fceae1c36463c5a49a01bf0b9ea7ef3355cb5412ace2f3aa2e160bcbbff0805f
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
