---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Yet the authors' own diagnosis attributed the stall to what the proposer was not shown (its scorer saw a failure mode in a quarter of runs that never reached the proposer), though their single remedy run stayed within noise. On one model line the whole harness gain came from editing a natural-language lessons file."
    reason: "The Bitter Lesson section needs only the point that weights-only continual learning is a rival hypothesis, not a corollary of the essay, and that one empirical study leaned that way. This passage goes further. It reinterprets that study's diagnosis, adds a hedge on its remedy run, and adds a separate observation about the lessons file. These claims need their own evidence and widen the article's attack surface. They do not advance the production-method versus representational-form argument. They may be worth keeping as a short pointer, with the detailed reading moved to the linked source ingest. It is unclear whether the article needs this counter-reading at all, so this is INFO, not WARN."
    level: info
outcome: pass
---

# Review

The article makes a two-part claim. First, selection-based learning needs a comparison, not a single score, and a robust comparison over a preference model can supply it. Second, a fixed-weight LLM can build that preference model from a stated purpose and make the comparison. The description also commits the article to the weight-training contrast, the Bitter Lesson and the empirical test. Material in those sections therefore serves a declared commitment and is not a branch.

Most side material earns its place under that claim:

- The AlphaGo Zero/AlphaZero contrast and the gradient-update paragraph set the boundary between selection and direct updates. The definition depends on that boundary.
- The Gödel machine, PRODIGY and EURISKO precedents form the proof–formula–judgment progression. This progression locates where the bet enters. The concession that the Gödel machine "is not rigid" stops the contrast from overclaiming.
- The stochastic-dominance example, the Greco et al. framing and "The analogy has a limit" paragraph supply the robust-comparison premise and bound it. The last of these marks where open-ended work departs from the decision-analysis method.
- The cost ledger, the consistency paragraph, the credit-assignment caveat and the five hazards (including *Weak proposals*) bound the bet or state how it can fail. They limit the main claim rather than compete with it.

One passage is a mild branch: the detailed counter-reading of the Harness Evolution study inside the Bitter Lesson section. The finding records it. It may be worth keeping as a short pointer, but its detail belongs more naturally in the source ingest. No branch clearly calls for removal or rehoming, so the outcome is PASS with one INFO finding.
