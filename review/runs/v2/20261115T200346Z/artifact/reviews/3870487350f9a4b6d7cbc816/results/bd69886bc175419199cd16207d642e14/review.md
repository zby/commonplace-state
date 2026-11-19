---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/sentence/stock-phrases.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 6e2bd9a71d2685b71fc1641640e684574da24f3115f005263a75367c0dc6c29c
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T200346Z/artifact/reviews/3870487350f9a4b6d7cbc816/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T200346Z/artifact/reviews/3870487350f9a4b6d7cbc816/observation.json
contract-sha256: 9969d7db1b8228822ac807fdc50483981fc6d62c7effbe601a7de3fac2e131a0
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T200346Z
launch: bd69886bc175419199cd16207d642e14
completed-at: '2026-11-15T20:04:11Z'
raw-output: kb/reports/state/review/runs/v2/20261115T200346Z/calls/launches/bd69886bc175419199cd16207d642e14/outputs/review.md
raw-output-sha256: 2b14082539487eaef7a1f0bd64493d2ca16711ae605b63f346aab89e7dbde569
format: 2
---

# Review

## Summary

The note's body contains none of the listed stock patterns: no "not just X — it is Y" elevation, no "it's worth noting", no "in other words" restatement, no "at its core", no "the key insight here is". I checked the closest framing sentences against the deletion test. Each one carries content that the surrounding text does not already supply.

## Sentences checked

- "The two failure modes are not symmetric, and the rule rides entirely on that." The heading already names the asymmetry. The sentence still adds the dependency claim: the rule depends *entirely* on the asymmetry. The paragraph after it relies on that claim when it calls hand-maintained copies forbidden rather than merely risky. The sentence is borderline but not removable without loss.
- "A bounded, recoverable downside on one side; a silent, unbounded one on the other — that is why hand-maintained-and-trusted is *forbidden* rather than merely risky." It summarises the previous paragraph, but it also draws the normative conclusion that paragraph leaves unstated.
- "This looks like it reopens the regress, but it doesn't:" This is a setup clause, not a standalone filler sentence. It introduces the amortization argument that follows it.
- "Two things change." and "The spread is what shows it generalizes." These are short signposts that carry structure or an evidential claim. They are not stock filler.
- "It is the general form of 'a cache must never be the only copy' …" It adds a comparison to a familiar principle and widens its scope. That point appears nowhere else in the note.

No sentence fails the deletion test.
