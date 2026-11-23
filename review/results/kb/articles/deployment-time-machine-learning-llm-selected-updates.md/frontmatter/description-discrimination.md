---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/frontmatter/description-discrimination.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 61aca13775c00eeeecc58b0475a1c6dba1bc0c2a6b9db4941af2a88d3a5c574a
criterion: kb/instructions/review-gates/frontmatter/description-discrimination.md
criterion-sha256: 17cbbd1fca45e6be71ce6750fe85980667f4958045e3610c4bb9378b13702bcf
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 985fe2ad5cc646c0af0e7ad2510f9b5b
completed-at: '2026-11-22T09:33:12Z'
findings:
- scope: document
  quotes: []
  reason: The leading label 'Lead article:' and the trailing comma list ('weight-training
    contrast, Bitter Lesson, empirical test') are a table of contents rather than
    claims; they aid recognition but add less retrieval value than the mechanism clause.
    The description still discriminates well because of its middle clause.
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/985fe2ad5cc646c0af0e7ad2510f9b5b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/a8c1a221481b08ee0c6b8394/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/985fe2ad5cc646c0af0e7ad2510f9b5b/outputs/review-description-discrimination.md
raw-output-sha256: 919ac11f54773cea59cc0995f9cd753ce6c79758a7f2bea2b9c86dcc2c61fe0e
---

# Review

The title, "Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score", names the topic: updates chosen by an LLM at deployment time without a scalar score. The description does more than paraphrase it. It adds:

- **Mechanism:** a deployed agent selects edits to its own instructions, and a fixed-weight LLM builds the preference model and makes the robust comparison. The title says neither "instructions/edits" nor "preference model / robust comparison".
- **Epistemic status:** it frames the LLM capability as a bet, which the title does not signal.
- **Scope and context:** it lists the weight-training contrast, the Bitter Lesson discussion and the empirical test, so an agent can tell this article apart from narrower theory notes on preference models or the Bitter Lesson and from the companion testing article.

An agent picking from a short result list could tell from the description that this is the broad framing article for the paradigm and its central bet, not a definition note or the experimental design. The gate passes. The info finding notes only that the trailing topic list adds less than the mechanism clause does.
