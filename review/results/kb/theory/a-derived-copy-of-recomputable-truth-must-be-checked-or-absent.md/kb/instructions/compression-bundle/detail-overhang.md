---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/compression-bundle/detail-overhang.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/compression-bundle/detail-overhang.md
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 1f71e54b77ec4042909cc72c2b216219
completed-at: '2026-11-16T22:20:15Z'
findings:
- scope: passage
  quotes:
  - root feeds wheel builds via `pyproject` `force-include`; `src/commonplace/_data`
    serves editable installs
  reason: The fourth instance only needs to show two tracked copies that must be byte-identical.
    The parenthetical explaining which build path consumes each copy is packaging
    background that the linked ADR 027 already carries; it does no work for the rule
    and can be cut to the bare fact of two copies plus the ADR link.
  level: warn
- scope: passage
  quotes:
  - and precondition 4's amortization argument is what keeps the pattern's authorship
    acceptable instead of a quiet regress
  reason: The tag-README instance restates the regress caveat that precondition 4
    already argues in full a few lines earlier. The instance needs only that the hand-authored
    sweep runs as a strict mechanical extraction (meeting precondition 4); the re-explanation
    of why that is acceptable can be compressed to a pointer.
  level: warn
- scope: passage
  quotes:
  - Any use-shaped artifact depends on its sources — whether its content is worked
    out from them (a derived copy) or generalizes beyond them (an abstracted rule,
    answerable to its sources as evidence).
  - 'The repair follows the regime: re-derive and compare where the content is recoverable
    from the source, re-examine the support where it exceeds it.'
  reason: The managed-staleness background paragraph is long for its job of setting
    up the contrast with the deterministic case. These two sentences elaborate the
    general dependent-knowledge taxonomy and repair modes beyond what the contrast
    needs. The rest of the paragraph (lineage, timestamps, Level B judgment) is probably
    needed to make the regime flip intelligible, so this is a light trim, not a rewrite.
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/d5b92e70da0b0220edc42687/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/d5b92e70da0b0220edc42687/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/1f71e54b77ec4042909cc72c2b216219/outputs/review.md
raw-output-sha256: bf19a61b82012531d6a655c4caf439ebb2abd0a1e33e10197c22bbce1be582e5
---

# Review

The note's core argument — the asymmetry between an absent and a false copy, the regime flip at Level A verification, the four preconditions and the consequences — is mostly proportional. The asymmetry section is short and does the persuasive work. Precondition 4 is the longest precondition, but it answers the strongest objection (that the validator reopens the regress), so its length earns argumentative force and is not flagged.

Two details outgrow their role and should be compressed in place. The `AGENTS.md.template` instance carries packaging detail about which build path consumes each copy, which the linked ADR already holds; the instance only needs "two copies, must be byte-identical, one comparison." The tag-README instance re-argues precondition 4's amortization point instead of pointing back to it.

The managed-staleness setup paragraph is borderline. Its contrast is necessary for the "what flips the regime" step, but its opening taxonomy of derived versus abstracted artifacts and its repair-modes sentence add background beyond that contrast. This is reported as INFO because trimming risks making the general regime harder to recognize.
