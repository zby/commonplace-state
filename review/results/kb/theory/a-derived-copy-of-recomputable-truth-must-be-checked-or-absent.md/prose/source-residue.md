---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/prose/source-residue.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/prose/source-residue.md
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 72a0ce93e4214465b4d1d2779c80a3c5
completed-at: '2026-11-16T22:18:58Z'
findings:
- scope: passage
  quotes:
  - For dependent knowledge in general the KB runs
  reason: The title and opening state a general rule about any derived copy of recomputable
    truth, but the scope section defines the rule's boundary through this KB's own
    machinery ("the KB runs managed staleness", Level A/B of the KB's text testing
    pyramid). The section is readable as this KB's implementation of a general split
    between judgment-priced and mechanically priced verification, and the next paragraph
    states that general criterion ("mechanical derivation makes verification Level
    A — deterministic, near-zero cost, binary"). Framing the KB machinery explicitly
    as an illustration of that general split would remove the overcommitment.
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/877693d2a12eb4802bee1433/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/877693d2a12eb4802bee1433/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/72a0ce93e4214465b4d1d2779c80a3c5/outputs/review-source-residue.md
raw-output-sha256: ec938a501a936f4dc1605b47e4a1e63577f44f0cf68b3e9c8f307c12a2734371
---

# Review

Claimed generality: the title and description apply to any artifact carrying a copy of mechanically recomputable information. The opening lists heterogeneous examples (a tag-README mark, a memory system's compiled cue, an inlined contract list, a duplicated file), and they are explicitly framed as examples.

Commonplace-specific vocabulary in the body is mostly marked as illustration. The "Instances across four surfaces" section is labeled as instances, and the ADR and log references sit inside an explicit example of omission. The memory-systems material is cited as one instance, not as the frame. The one place where KB-local framing does structural work is the scope section, where the boundary is described as what "the KB runs" and as KB pyramid levels. The general criterion (deterministic, cheap, binary verification) is stated alongside, so the claim does not depend on the residue. It is recorded as INFO, and the gate passes.
