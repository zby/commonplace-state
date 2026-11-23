---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - In eight paired runs, alternating which interpreter went first, 500 evaluations
    of `sum(x*x for x in range(10000))` took a median 0.46 seconds on 3.10 and 0.32
    on 3.11.
  reason: The timing figures give their method, workload, interpreter builds and an
    explicit scope limit, so a reader can interpret them. Nothing links to a retained
    record of the runs, and the note does not name the machine, so a reader can rerun
    the check but not inspect it. The note claims only a relative result for one workload,
    which keeps this from being unsupported specificity.
  level: info
- scope: passage
  quotes:
  - CPython 3.12.8 reported a likely circular import. CPython 3.13.1 named the local
    file that hid the standard library module and suggested renaming it.
  reason: These version-specific diagnostic observations come with an exact reproduction
    recipe, but the note does not say they came from a local check or link a record
    of them. A pointer to the record would make it possible to verify them without
    rerunning.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/prose/orphan-references.md
contract: verdict
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
criterion: kb/instructions/review-gates/prose/orphan-references.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/32816be3282745488aa71d2e6743f69c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/d22609216220124f98d0c8cd/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 32816be3282745488aa71d2e6743f69c
completed-at: '2026-11-20T18:53:20Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/32816be3282745488aa71d2e6743f69c/outputs/review-orphan-references.md
raw-output-sha256: aec7c789e81d351c89fedcbd5a5c8ddce7f2008aadb3fe228e7795a4dcc87702
format: 2
---

# Review

## Summary

The note's concrete figures have enough context to evaluate:

- **Python 3.11 checks.** The four 3.11 checks name the CPython builds they used, and the timing row states its pairing method and its scope limit.
- **Library hours.** The library-hours figures ("twice as many visits") are labelled hypothetical.
- **Tag coverage trace.** The tag coverage observation links to its evidence note.
- **Public Python facts.** The `asyncio.TaskGroup`, `tomllib` and `inspect.getargspec` changes can be checked in Python's public release history.

The remaining gap is provenance, not legibility. The two sets of local measurements can be reproduced from their descriptions, but neither points to a retained record. That gap supports INFO findings, not a warning.
