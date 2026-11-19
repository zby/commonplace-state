---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
criterion-sha256: 2bd8ea31d13e86a99f11ef7fa12cf3bdd56d3ba71a8e96ccda9ca7331af8c5e5
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

I checked each sentence for negation scope, modifier attachment and pronoun reference. Pronouns and demonstratives resolve from local context, and no negation or modifier has a plausible second reading. One mixed direct and indirect phrasing is slightly awkward but not ambiguous.

### Findings

- INFO: "A `spec` tells an agent it can implement from this." The direct-speech "this" sits inside indirect speech. A reader could briefly look for an antecedent in the preceding text, but the only plausible reading is "from the spec document." The same holds for "An `index` tells it this is a navigation hub."
- INFO: "This is why [description is the most important field]..." opens a paragraph with "This". The antecedent is the routing mechanism described just before ("decides whether to load the full document"), and no competing antecedent is plausible.
- INFO: "But these structural hints only work if the metadata exists reliably." "Only" attaches to the condition ("work only if..."); no plausible reading takes it to restrict "hints" or "work".

## Result: PASS
