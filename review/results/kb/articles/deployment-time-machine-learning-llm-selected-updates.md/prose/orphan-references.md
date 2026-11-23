---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/prose/orphan-references.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/prose/orphan-references.md
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: b4e70f5925ff4ae894d0f33589d060fa
completed-at: '2026-11-22T09:34:29Z'
findings:
- scope: passage
  quotes:
  - On one model line the whole harness gain came from editing a natural-language
    lessons file.
  reason: The study is linked, but the note does not name the model line or say how
    large the gain was. A reader cannot tell whether this result is a substantial
    gain or a marginal one without opening the ingest. Naming the model line, or giving
    the gain's size, would make the claim legible on the page.
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b4e70f5925ff4ae894d0f33589d060fa/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/95b83ea80e8c0277d607ad82/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b4e70f5925ff4ae894d0f33589d060fa/outputs/review-orphan-references.md
raw-output-sha256: d7c7c6d1f1b6ee67cbb98696b4682468cbec004f5a62a4d1fdb936bcd65a0255
---

# Review

## Summary

Each specific figure, named study and historical claim has a source and
enough local context:

- AlphaGo Zero's 55% replacement margin links to the Nature paper and is
  explained.
- AlphaZero links to an ingest.
- PRODIGY (1988) and EURISKO (early 1980s) link to ingests and are described.
- The Greco, Mousseau and Słowiński method links to an ingest.
- The 2026 Sutton and Javed interview is linked.
- The 2026 "Harness Evolution Hits a Ceiling" study is linked. Its "quarter of
  runs" figure is placed within the study's own diagnosis.
- The Commonplace evidence status is a first-person report about the authors'
  own system.
- The routing-line episode, including "three similar over-broad rules", is
  explicitly hypothetical.

The one weak spot is minor. The harness study's model-line result lacks the
detail a reader would need to judge it from the article alone.
