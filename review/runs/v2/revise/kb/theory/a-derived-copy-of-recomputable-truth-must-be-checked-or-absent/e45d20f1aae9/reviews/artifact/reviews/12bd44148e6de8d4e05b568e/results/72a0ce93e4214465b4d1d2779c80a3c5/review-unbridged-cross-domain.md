---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - a cache must never be the only copy
  reason: The note presents itself as the general form of a software-caching maxim
    without stating the shared mechanism. That maxim mainly concerns durability (the
    source must survive), while this note's rule concerns consistency (a retained
    copy must be verified against a surviving source). The relation is plausible,
    because both keep the source authoritative and the copy disposable, but the bridge
    is left implicit. It is a framing remark, not evidence the argument depends on.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/prose/unbridged-cross-domain.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/prose/unbridged-cross-domain.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 5f22f140a9b058b4c1ec8918857159da174cbb456c8294d47fa56c0f0021ec7f
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/12bd44148e6de8d4e05b568e/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/12bd44148e6de8d4e05b568e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 72a0ce93e4214465b4d1d2779c80a3c5
completed-at: '2026-11-16T22:18:58Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/72a0ce93e4214465b4d1d2779c80a3c5/outputs/review-unbridged-cross-domain.md
raw-output-sha256: 454ecb588772219311076ddc66e52949a5b405d8138ece13b10a9bb2e66a6e94
format: 2
---

# Review

The note cites no external studies or empirical results. Its evidence is internal to agent-operated KB and software-artifact maintenance: the shipped `complete`-mark validator, ADR 025, ADR 027, a logged skill edit and linked theory notes. These share the note's argument domain.

The memory-systems source (keep-compiled-views-aligned) is the closest domain shift. The note bridges it by stating the shared mechanism: a derived surface without provenance, regeneration rules and staleness detection becomes an independent authority. The closing appeal to "a cache must never be the only copy" imports a caching maxim without naming the shared mechanism. Because it serves as framing rather than support, it is recorded as INFO, and the gate passes.
