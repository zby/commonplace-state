---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: The type spec asks notes to state the claim's limits under a `## Scope`
    heading (assumptions, applicability conditions, known failure cases) and to omit
    it only when no limit is known. The note has no Scope section, yet its own text
    shows known limits. The claim that call sites 'don't change' holds only when the
    neural and symbolic implementations accept the same arguments and return the same
    output set; the prompt-switching example has to stipulate this ('receive the same
    set of queue labels'). The claim also depends on name-based dispatch in a shared
    namespace. Its evidence is one system, llm-do. Neural and symbolic callees can
    also differ in determinism, latency, cost and failure modes, which callers may
    depend on even when the signature is unchanged. These conditions are stated inline
    or not at all, so a rescoping edit would have to rewrite the claim.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/types/note.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/types/note.md
note-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/f5ba28175f8a43cf96ac11bfad8650ae/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/03f390b2187a64ccf2f89e18/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: f5ba28175f8a43cf96ac11bfad8650ae
completed-at: '2026-11-20T09:43:10Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/f5ba28175f8a43cf96ac11bfad8650ae/outputs/review.md
raw-output-sha256: 5709041bf692408c4892f43a3a94d2b0f9d519f907f70b0a5ba440699af38660
format: 2
---

# Review

The note mostly meets the `note` type's authoring instructions. The title is a compressed handle for the claim. The opening paragraph states the main claim, that a unified calling convention makes the neural–symbolic boundary movable, and the mechanism comes next. The note links inline and in its footer to adjacent notes on constraining, codification, spec-mining and typed callables, and each link says how that note relates. Its content is design rationale. The numbered progression illustrates the mechanism and is not an imperative procedure, so it belongs in a note and not in instructions. The Open Questions section matches the template.

One instruction goes unmet. The note has no `## Scope` section, even though known limits exist, and the note itself shows some of them. Moving a component between neural and symbolic leaves call sites unchanged only when the two implementations share an input/output contract. The claim also relies on name-based dispatch, and its only evidence is llm-do. The Open Questions already raise scale and debugging. A Scope section is where the note should state the conditions under which the claim holds. That would let a later rescoping edit narrow the claim without rewriting the mechanism section.
