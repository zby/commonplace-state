---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Yet the authors' own diagnosis attributed the stall to what the proposer was not
    shown (its scorer saw a failure mode in a quarter of runs that never reached the
    proposer), though their single remedy run stayed within noise. On one model line
    the whole harness gain came from editing a natural-language lessons file.
  reason: The Bitter Lesson section needs only the point that weights-only continual
    learning is a rival hypothesis, not a corollary of the essay, and that one empirical
    study leaned that way. This passage goes further. It reinterprets that study's
    diagnosis, adds a hedge on its remedy run, and adds a separate observation about
    the lessons file. These claims need their own evidence and widen the article's
    attack surface. They do not advance the production-method versus representational-form
    argument. They may be worth keeping as a short pointer, with the detailed reading
    moved to the linked source ingest. It is unclear whether the article needs this
    counter-reading at all, so this is INFO, not WARN.
  level: info
outcome: pass
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/compression-bundle/branch-bloat.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/compression-bundle/branch-bloat.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/a087f2509efe415492f5c8b58755c980/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/947c93cd6b72fcf7b848d511/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: a087f2509efe415492f5c8b58755c980
completed-at: '2026-11-22T09:35:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/a087f2509efe415492f5c8b58755c980/outputs/review.md
raw-output-sha256: 14cc1d8953522f11e3bda2440bea657740059b3808c0b6a6dc520151e866d46d
format: 2
---

# Review

The article makes a two-part claim. First, selection-based learning needs a comparison, not a single score, and a robust comparison over a preference model can supply it. Second, a fixed-weight LLM can build that preference model from a stated purpose and make the comparison. The description also commits the article to the weight-training contrast, the Bitter Lesson and the empirical test. Material in those sections therefore serves a declared commitment and is not a branch.

Most side material earns its place under that claim:

- The AlphaGo Zero/AlphaZero contrast and the gradient-update paragraph set the boundary between selection and direct updates. The definition depends on that boundary.
- The Gödel machine, PRODIGY and EURISKO precedents form the proof–formula–judgment progression. This progression locates where the bet enters. The concession that the Gödel machine "is not rigid" stops the contrast from overclaiming.
- The stochastic-dominance example, the Greco et al. framing and "The analogy has a limit" paragraph supply the robust-comparison premise and bound it. The last of these marks where open-ended work departs from the decision-analysis method.
- The cost ledger, the consistency paragraph, the credit-assignment caveat and the five hazards (including *Weak proposals*) bound the bet or state how it can fail. They limit the main claim rather than compete with it.

One passage is a mild branch: the detailed counter-reading of the Harness Evolution study inside the Bitter Lesson section. The finding records it. It may be worth keeping as a short pointer, but its detail belongs more naturally in the source ingest. No branch clearly calls for removal or rehoming, so the outcome is PASS with one INFO finding.
