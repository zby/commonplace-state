---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'The qualifier ''between neural and symbolic'' in the title is not used
    by the central mechanism. A shared interface with name-based resolution hides
    the implementation from callers for any pair of interchangeable implementations.
    The deletion test leaves the argument intact. The note is plainly scoped to the
    LLM/code boundary, though: it is framed by constraining and codification, which
    concern that boundary. So this is intentional domain scoping rather than a narrowing
    that obscures a broader theorem.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note-sha256: cead3a2ab3223a39a27d524d121b933c37329874d980e453c9124a146044e75a
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/e766b5b3632325dc3ebd0f6f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 96c4eea5828c4089a10b19a54bdfd799
completed-at: '2026-11-20T09:44:59Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: fc6bed5542183c5363b7776e5b6d5faca1ad3de9bb24020395ed64aca238b010
format: 2
---

# Review

Qualifiers in the title, description and opening:

- **"Unified"** (calling conventions). Load-bearing. The argument depends on both kinds of component presenting the same interface.
- **"Bidirectional"**. Load-bearing. The note argues both directions: codification (steps 1–3) and relaxing (step 4, and the routing-rule test run).
- **"Between neural and symbolic"**. The mechanism does not use any property specific to neural or symbolic components. It is ordinary interface substitution. The application to constraining and codification needs the qualifier, and the note is domain-scoped to that boundary. INFO under the LLM-domain-scoping rule.
- **"Name-based dispatch"** (description and mechanism). Load-bearing for the LLM-caller case: the LLM emits a string, and the runtime must resolve it to either kind of implementation.
- **"llm-do demonstrates"** (description). Marks llm-do as an instance rather than a condition of the claim. It does not narrow the claim.

No qualifier narrows the central claim in a way that warrants WARN.
