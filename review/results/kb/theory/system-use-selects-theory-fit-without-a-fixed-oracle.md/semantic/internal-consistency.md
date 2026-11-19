---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 0b6aab3bf2ce43d9808afc045b836a39
completed-at: '2026-11-16T18:57:58Z'
findings:
- scope: passage
  quotes:
  - This claim does not reserve global fit for permanent human judgment.
  reason: 'The opening defines fit at the claim level: ''whether a claim belongs in
    a working theory'', with claims and formulations earning standing. Later passages
    shift to the theory level: ''rival theory states'' and ''global fit''. ''Global
    fit'' is never defined. Whether it means a claim''s fit to the whole theory, or
    the whole theory''s fit to its problem, needs author confirmation. This is likely
    definition drift, not a contradiction.'
  level: info
- scope: passage
  quotes:
  - This does not make theory fit untestable. It changes the shape of the test.
  reason: Here 'test' names the assessment of fit. The self-confirmation section and
    its linked note reserve 'test' for an independent test, which system use is not.
    The two senses can be reconciled, because fit is assessed while the independent
    test record is separate. Still, the same word carries both senses without a marker,
    so this needs human confirmation.
  level: info
contract: verdict
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/93c0f2ff576b00aa1106eb45/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/93c0f2ff576b00aa1106eb45/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/0b6aab3bf2ce43d9808afc045b836a39/outputs/review-internal-consistency.md
raw-output-sha256: bbe5d3f4b26e2c856de2c2bf0f29746bac5ed9ef4ca982eaedd14238aacb21bf
---

# Review

## Summary

The sections agree on the main line. Live use is an initial and fallible selection environment for fit. It is not a final authority, and it is not an independent test. The "initial" section, the Scope section and the self-confirmation section restate this consistently. The description's "can provide" and the title's "is" differ only in register, because the body's "initial" and "provisional" keep the strength aligned.

There are two places where likely drift needs confirmation. Fit moves between the claim level and the theory level. "Test" is used both for assessing fit and, through the linked note, for independent testing. I found no contradiction.
