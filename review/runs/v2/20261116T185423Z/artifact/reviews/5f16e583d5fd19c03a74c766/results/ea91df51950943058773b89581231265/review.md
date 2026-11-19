---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '"Initial" means a starting environment under incomplete evaluation, not a permanent
    architecture or a promise that human holistic judgment remains necessary.'
  - The distinction is developed in the linked notes above.
  reason: The collection's 'Don't defend against objections you've already closed'
    convention is unmet. The first two Scope bullets restate exclusions the body has
    already settled. The opening paragraph and its link already separate theory fit
    from a claim's test record, and the 'Why "initial" matters' section already rules
    out the permanent-human-judgment reading. The bullets add no new boundary or gap.
    Cut them, or replace them with boundaries the body does not already state.
  level: warn
- scope: passage
  quotes:
  - is a statement about this research setting
  reason: The Formulation constraint asks that named local choices stay recoverably
    scoped. 'This research setting' points to an unnamed particular setting, so a
    reader citing the note elsewhere cannot tell which setting lacks a fixed oracle.
    The main claim is conditional ('When no complete fixed oracle decides...'), so
    this does not threaten placement. Naming the setting, or wording it as a condition
    on the claim, would fix it.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/theory/COLLECTION.md
contract: verdict
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
criterion: kb/theory/COLLECTION.md
note-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
criterion-sha256: 23ede037003607491dace7447a749ba3d1865aa8fd8cd08a03da6749af864112
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/5f16e583d5fd19c03a74c766/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/5f16e583d5fd19c03a74c766/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: ea91df51950943058773b89581231265
completed-at: '2026-11-16T18:56:47Z'
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/ea91df51950943058773b89581231265/outputs/review.md
raw-output-sha256: 349b6a247dd022e1fcc470435a7c35341dac5c504d817525cb7a65f1e1e4e584
format: 2
---

# Review

## Summary

The note belongs in `kb/theory/` and meets the collection's main conventions. Two conventions are only partly met.

**Placement and explanatory-reach.** The note makes a conditional claim about the design space: where no complete fixed oracle decides theory fit, distributed consequences of live use can act as an initial selection environment. It names no Commonplace selection, so the placement test leaves a substantive claim. It maps its own limits. Self-confirmation, blame assignment and the meaning of "initial" each get their own section, and real gaps go to `## Open Questions` instead of being hedged inside the claim. The tests for explanatory-reach are addressed. For example, changing the premise "no fixed oracle" (a narrow transformation with a test suite) predictably changes the conclusion, and the note says so.

**Hypothesis force and modality.** "Can provide" in the description and the conditional opening make the claim's possibility force recognizable. Because no mode is declared, it reads as universal, which matches its conditional existence-of-route shape.

**Outbound links.** All five links target existing `kb/theory/` notes and use labels this collection authorizes (`grounds`, `extends`, `mechanism`). Each footer entry has a context phrase. Two inline links use connective framing. There are no links into `kb/work/` and no source citations, so the source-grounding bound does not apply.

**Unmet conventions.** The Scope section partly re-defends exclusions the body has already closed, which the collection names as padding. One scope bullet also refers to an unnamed "research setting". Both are recorded as findings.
