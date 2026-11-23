---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/theory/COLLECTION.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
criterion: kb/theory/COLLECTION.md
criterion-sha256: 95ad0d6ce3828b25282f7610268c4e1aca006fa34526bc2b4e4056f3e271cccd
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 2ab268635d0e4defa8a56114fc7f2dba
completed-at: '2026-11-20T11:11:10Z'
findings:
- scope: passage
  quotes:
  - 'Abstracted into: [RLM, λ-RLM, Tendril, and llm-do separate restriction from persistence](./rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md)'
  reason: 'The footer entry uses `Abstracted into:`, which is not in the collection''s
    authorized label table. The contract''s only inverse-prefix form is the `Operationalized
    into:` footer for instruction procedures. The entry also departs from the footer
    shape `- [title](path) — label: context phrase` because it gives no context phrase
    stating the reader need. As the reverse of the target''s `abstracted-from` edge,
    it reads as a mirror of an existing edge. The contract allows a reciprocal link
    only when the reverse direction independently helps readers, and this entry does
    not say how it does. Either state that reader need using an authorized label and
    a context phrase, or drop the entry.'
  level: warn
- scope: passage
  quotes:
  - 'extends: extends typed-callable signatures across both prompt-backed agents and
    code functions'
  reason: 'In the contract, `extends` serves a reader who ''wants the argument developed
    further'' in the target. Here the target is the premise this note builds on: the
    body says ''This note extends that callable structure to tools.'' The edge therefore
    points from the extension to its base, so `extends` may be inverted. `grounds`
    would be a better fit. This is minor and does not affect the outcome.'
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/2ab268635d0e4defa8a56114fc7f2dba/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/87f58bfc1761d8305d57d34f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/2ab268635d0e4defa8a56114fc7f2dba/outputs/review.md
raw-output-sha256: 5a4a912a4d27e521f74377688a62ed3f0e0de6ca91d8277e78a790e9a205bb64
---

# Review

## Placement

The note belongs in `kb/theory/`. Its contribution is a claim about the design space. A shared call interface across prompt-backed and code-backed implementations lets programmers swap them without editing callers. The same interface leaks asymmetrically: prompt-to-code exposes loose LLM callers, and code-to-prompt exposes cost, latency and error assumptions in code callers.

llm-do is the only named system. The note introduces it as a runtime that implements the pattern and keeps it out of the title and description. Removing llm-do leaves the claim intact, so the note passes the theory-independence constraint. The note is not a record of what Commonplace selected, and it is not a description of llm-do's current construction.

## Explanatory-reach and claim formulation

The note explains why the interface leaks: a signature cannot express the execution regime or the caller model. From that mechanism it predicts which caller assumptions break in each swap direction. It also maps boundaries under `## Scope`:

- Call invariance is not behavioural invariance.
- Structural signature changes still need adapters.
- Swapping code back to a prompt needs latency, cost and error-handling headroom at the call site.

The note marks the one conjectural effect as conjectural: "That effect is an expectation, not an observed result." It leaves real gaps in `## Open Questions` instead of hedging around them. It does not pad its claims with defences against objections it has already closed.

## Linking and grounding

The inline links use connectives that fit the argument. Most footer labels are authorized and point to permitted destinations:

- `grounds` to theory notes
- `contrasts` to a theory note
- `defined-in` to `theory/definitions`
- `mechanism` and `enables` to theory notes

The note links nothing in `kb/work/` and cites no tracked sources, so the unquoted-source bound does not apply. The external llm-do link illustrates the mechanism; it is not offered as corroboration.

The convention gap is the `Abstracted into:` footer entry. It uses an unauthorized label and has no context phrase. It also looks like a mirror of the target note's `abstracted-from` edge rather than a link authored for a reader need, which the contract forbids. One `extends` edge may also point the wrong way. Neither problem undermines conformance overall, which gives a warn outcome.
