---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/prose/orphan-references.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/prose/orphan-references.md
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
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
  - the 2026-06-10 skill edits
  reason: A dated event is cited as evidence for the read-the-contract-live resolution.
    The location is given only as the unlinked path `kb/log.md`, and the note does
    not name which skills or which contract were changed, so the reader must search
    the log to evaluate the example. The sentence still states what the edits chose,
    which keeps the claim legible; naming the affected skill or linking a retained
    record would close the gap.
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/7805bba1ddefa057d36fbfb7/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/7805bba1ddefa057d36fbfb7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/72a0ce93e4214465b4d1d2779c80a3c5/outputs/review-orphan-references.md
raw-output-sha256: e39df5d0c9f891da49887a4ddf763cd10afe0f28897c66cabdcaf1c8a759a67d
---

# Review

The note contains few specific figures or empirical claims. Most of its concrete references are sourced and contextualized. ADR 025 (deleting committed generated indexes) and ADR 027 (the two-copy `AGENTS.md.template` layout) are linked, and the note states the relevant fact from each. The `complete` mark instance links the `tag-readme` type spec, and Level A and Level B checks link the text testing framework.

The one thin reference is the dated "2026-06-10 skill edits", which points to the log without identifying the skills or the contract. The note states what the edits did, so the reader can understand the example without checking it. It is recorded as INFO, and the gate passes.
