---
note: kb/work/sniadanie-ai-demo/demo.md
note-sha256: db0353df2ac0d2be43fc09c4aeb5e5f2b3c7d65cb511218ac651b4248791a686
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: b2930f2198c00862677777da136d1e12e0ca38fede54784dff8f6b211ee73963
outcome: fail
profile:
  harness: claude-code
  launch-model: sonnet
  effort: medium
model: claude-sonnet-5-5
run: kb/reports/state/review/runs/20261111T171156Z
launch: c8f2c8cbc01145acb9955709310bc9cf
completed-at: '2026-11-11T17:12:09Z'
---
### Summary

The H1 asserts that every added wiki note improves every answer. The body establishes something different: retention is distinct from loading into context, so a larger wiki does not require a larger context per request. The Scope section also explicitly disclaims the title's claim. This is claim drift, and the body contradicts the title.

### Findings

- fail: Claim drift. The title ("Every added wiki note improves every answer") is a universal quality claim. The body never argues it. The Scope section says "This argument does not establish that each added note improves answer quality" and notes that notes may be irrelevant, inaccurate or redundant. The body therefore denies the title's claim.
- fail: What the body establishes is that retaining a note and loading it into context are different operations, and that selecting only the relevant part of a wiki lets the wiki grow without growing every request's context. Nothing in the body supports a claim about answer quality.
- info: The description ("distinguishes retained knowledge from the context selected for one task") matches the body. The title is the only misaligned element. The `title-as-claim` trait makes the mismatch more serious, because the title is meant to be the claim the body supports.

### Suggested Revision

Retitle the note to the claim the body supports, for example: "Retaining notes in a wiki does not require loading them all into context". Alternatively, "A larger wiki does not require a larger context per task". Keep the Scope section as it is.

## Result: FAIL
