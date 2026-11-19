---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The comparison names the predecessor and adopted successor, the requirements under
    which the successor counts as better, and how those requirements apply to the
    predecessor's prior capabilities.
  reason: The opening restates the claim's slots abstractly but withholds their content.
    The relation's two components — non-regression thresholds on the predecessor's
    prior scope and a declared improvement on a named dimension — only appear in the
    second section. Naming them here ('non-regression on the predecessor's prior capabilities
    plus a declared gain on a named dimension, both fixed before development') would
    make the core claim complete and memorable on first read, and the second section
    could then elaborate instead of introducing them.
  level: info
- scope: passage
  quotes:
  - undergoes experience-responsive retention when production experience causes a
    retained change to its reusable machinery that later work depends on
  reason: The first paragraph opens with two sentences restating the retention/learning
    definitions before reaching the note's own claim in its fourth sentence. The title
    carries the claim, so it stays findable, but compressing the retention setup into
    a single contrast clause (retention carries no quality requirement, so improvement
    is a separate claim) would put the comparison sentence closer to the top.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/69cb51e4edaebc3d6ab29709/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/69cb51e4edaebc3d6ab29709/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 4675402108cc41bcaddc97298b0377c9
completed-at: '2026-11-18T00:20:12Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/4675402108cc41bcaddc97298b0377c9/outputs/review.md
raw-output-sha256: f2065ef8795098a741db4882d96325c238e6a600d5c5b59f1aac27103e882f4e
format: 2
---

# Review

## Summary

Strongest claim, in one sentence using the note's own commitments: *a claim that a factory got better compares two operative states — the predecessor and the installed successor — under an assessment relation declared before development, requiring non-regression on the predecessor's prior capabilities and a declared gain on a named dimension, and it is distinct from both retention and learning.*

The note makes this findable. The title states it, the first paragraph states the operative-state comparison and the antecedent relation, and every later section is visibly subordinate: the relata section defines the endpoints, the assessment-relation section supplies the relation's content, the retention/improvement/learning section separates the claim from its neighbours, and the Scope bullets bound it. Nothing later competes with the main claim, so this is not a WARN.

The shape is less memorable than it could be in two places. The opening spends its first sentences on the retention definition before reaching the note's own contribution. The second paragraph lists the comparison's requirements only as placeholders, so the substantive two-component relation (non-regression plus declared improvement) — the part a reader most needs to remember — is deferred to the second section. Filling that summary sentence with the two components is the simplest way to make the full claim stick after one read.

The stray `TODO` blockquote before the opening is an editorial marker rather than claim-obscuring apparatus, but it does sit between the title and the claim and should be resolved.
