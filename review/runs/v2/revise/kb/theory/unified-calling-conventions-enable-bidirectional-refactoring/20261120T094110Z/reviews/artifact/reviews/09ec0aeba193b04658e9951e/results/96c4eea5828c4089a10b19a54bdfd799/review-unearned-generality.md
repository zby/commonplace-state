---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: '''Neural'' and ''symbolic'' in the title stand for ''LLM agents'' and ''Python
    functions'', the only instance class the note works with (llm-do). Substituting
    the concrete terms leaves the mechanism and example unchanged, and the abstract
    terms forbid nothing extra. The note does argue that the mechanism is independent
    of llm-do: it rests on interface sameness, not on any llm-do feature. ''Neural/symbolic''
    is also the KB''s conventional vocabulary for this boundary rather than a defensive
    widening. The note does not develop a second instance class beyond llm-do (it
    only gestures at Python-specificity in Open Questions), so the abstraction is
    probably slightly ahead of its evidence.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
note-sha256: cead3a2ab3223a39a27d524d121b933c37329874d980e453c9124a146044e75a
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/09ec0aeba193b04658e9951e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 96c4eea5828c4089a10b19a54bdfd799
completed-at: '2026-11-20T09:44:59Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/outputs/review-unearned-generality.md
raw-output-sha256: 4b1c5da98df89c0251e6bec03eedc637cbec80c7a81d618ad7c119cef958ecc2
format: 2
---

# Review

Central claim: unified calling conventions enable bidirectional refactoring between neural and symbolic components.

- **"Unified calling conventions"**. This stands in for "llm-do's shared namespace with name dispatch". Downgrading to llm-do would cut the argued generality. The note's mechanism ("if neural and symbolic components present the same interface, callers don't need to know") is explicitly independent of llm-do, which serves as a demonstration. This abstraction is earned by argument.
- **"Neural" / "symbolic"**. These stand in for LLM agents and Python functions. The downgrade test leaves the argument unchanged, and the forbids-test finds nothing the abstract wording excludes that the concrete wording allowed. The terms are the KB's standard names for the two sides of the constraining/codification boundary, and the note uses them concentrated in the claim rather than spread across every noun. INFO rather than WARN.

Abstraction is concentrated in the title and opening and is not distributed across the body. The body speaks concretely of `.agent` files, Python functions and `ticket_classifier`.
