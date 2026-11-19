---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This claim does not reserve global fit for permanent human judgment.
  reason: '''Global fit'' allows two readings. It may mean whether each claim fits
    the working theory as a whole, or whether the theory as a whole fits its problem
    or system. The first reading makes selection operate on claims and formulations,
    as in the opening. The second makes it operate on whole theory states, as in ''rival
    theory states''. Each reading calls for different comparative evidence. Because
    the sentence only denies a role for permanent human judgment, I cannot show that
    the difference changes the argument, so it stays INFO.'
  level: info
- scope: passage
  quotes:
  - Together they can discriminate among rival theory states more strongly than static
    coherence alone.
  reason: The comparison baseline 'static coherence alone' is not defined. It could
    mean inspection of mutual consistency among retained claims, or any assessment
    made without operational consequences. Either reading fits the text, and the note's
    argument proceeds the same way under both, so materiality is not shown.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/f80c37723b658d72328acccc/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/f80c37723b658d72328acccc/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 0b6aab3bf2ce43d9808afc045b836a39
completed-at: '2026-11-16T18:57:58Z'
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/0b6aab3bf2ce43d9808afc045b836a39/outputs/review-underspecified-assertions.md
raw-output-sha256: 8603690a9b147c019731ecce4470100860dd53eff6a53dbbbda3436c85a3f35c
format: 2
---

# Review

## Summary

Most load-bearing assertions are resolved nearby:

- **Selection environment.** The note says what it selects among (claims and formulations), by what (distributed consequences of use) and with what standing ("provisional" and "initial").
- **Evidence gradation.** The ordering of retrieval, then mediation, then selection evidence is tied to stated counterfactual operations.
- **"Initial".** The note defines it in its own section and in Scope.
- **Self-confirmation.** The note names the specific routes by which use can mislead.

Two phrases leave a choice open, but I cannot show that either choice is material. They are recorded as INFO findings. No assertion meets the WARN threshold.
