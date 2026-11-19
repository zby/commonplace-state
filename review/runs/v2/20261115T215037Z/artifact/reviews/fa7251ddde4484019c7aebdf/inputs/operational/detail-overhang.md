---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/compression-bundle/detail-overhang.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/compression-bundle/detail-overhang.md
criterion-sha256: 4f8310d51d4da48ce9463a4b50340b9e3293fc5f716a00de0d549d3b8e3e84e3
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T214849Z
launch: 418d302f8b6e47afbd8177272c576b57
completed-at: '2026-11-15T21:49:23Z'
findings:
- scope: passage
  quotes:
  - Any use-shaped artifact depends on its sources — whether its content is worked
    out from them (a derived copy) or generalizes beyond them (an abstracted rule,
    answerable to its sources as evidence).
  - 'The repair follows the regime: re-derive and compare where the content is recoverable
    from the source, re-examine the support where it exceeds it.'
  reason: The managed-staleness background paragraph carries a real boundary condition
    (judgment-priced Level B verification makes hand-maintained dependents unavoidable),
    but it also elaborates the general dependent-knowledge taxonomy and the repair
    split, which the rule does not use. The contrast could likely be made in about
    half the length; kept at INFO because the paragraph sets the scope against which
    the Level A flip is argued.
  level: info
- scope: passage
  quotes:
  - The sweep pattern is hand-authored, but it executes as a strict mechanical extraction
    — and precondition 4's amortization argument is what keeps the pattern's authorship
    acceptable instead of a quiet regress.
  reason: The instance only needs to show the enforced state; this sentence re-runs
    precondition 4's regress argument already made in full above. A short clause or
    a pointer to precondition 4 would do the same work.
  level: info
- scope: passage
  quotes:
  - (root feeds wheel builds via `pyproject` `force-include`; `src/commonplace/_data`
    serves editable installs)
  reason: The build-path gloss explains why two copies exist, which the linked ADR
    027 already records; the instance's role is only to show the trivially checkable
    file-identity case. Probably compressible to the ADR pointer, though the gloss
    is short.
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T214849Z/artifact/reviews/dfe2c5e3d4c41a59f722cf17/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T214849Z/artifact/reviews/dfe2c5e3d4c41a59f722cf17/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
raw-output: kb/reports/state/review/runs/v2/20261115T214849Z/calls/launches/418d302f8b6e47afbd8177272c576b57/outputs/review.md
raw-output-sha256: c78e219f966871f4a3a17e860a0acaba3bb44cedad76b0c0285c7c1407363896
---

# Review

## Summary

Detail is mostly proportional to its argumentative role. The asymmetry section is compact and carries the rule's justification. The four preconditions are long, but each carries a boundary condition or inference step; precondition 4's regress answer is needed to stop the obvious objection that the validator is itself an unchecked claim. The Consequences bullets cite evidence briefly. The four instances each do one job, showing the rule in a different state of application.

Three passages run somewhat beyond their job. None justifies a WARN. The managed-staleness paragraph contains a general taxonomy of dependent knowledge that the rule does not use, although the paragraph as a whole defines the scope. Instance 1 restates precondition 4's amortization argument. Instance 4 includes a build-layout gloss that the linked ADR already holds. Each is a candidate for light compression in place, not a structural problem.
