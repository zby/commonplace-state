---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Unlike proof-gated switches, empirical admission admits harmful changes"
    reason: "The contrast presents harmful admission as specific to empirical admission. The mechanism is that the last filter's false positives become operative. That mechanism also covers proof-gated admission whenever the formalization is inadequate, and the article says so earlier ('under an inadequate formalization, a proved switch need not deliver what its user wanted'). The framing excludes a case the mechanism covers. Contrast instead on what each filter can certify, for example: proof-gated admission excludes changes harmful under its axioms; empirical admission certifies nothing beyond its observed evidence."
    level: warn
  - scope: passage
    quotes:
      - "Training or fine-tuning runs"
    reason: "The table row presents the timing of updates as separating gradient training from selection over a readable store. Weight updates can also run online during deployment (the linked deployment-time adaptation note says so). The paragraph below qualifies 'deployment time' for the readable-store column, but not this column's restriction. This emphasizes the typical case rather than excluding the other outright."
    level: info
  - scope: passage
    quotes:
      - "on a task already near the model's effective context limit, extra prompt text can tip a correct answer into rework"
    reason: "Context cost is framed as a near-limit effect, while the stated cost is diffuse load on every task. The preceding clause ('every unrelated task also loads that extra line') keeps the general case, so this only emphasizes the most visible instance."
    level: info
outcome: warn
---

# Review

## Summary

Most mechanism statements are framed at the right generality: direct versus
selected updates, credit assignment without a chain rule, operative dependence,
open verdicts under necessary preference, and the Bitter Lesson's production-
method axis. One hazard bullet frames false-positive retention as unique to
empirical admission. The article's own Gödel machine paragraph shows that the
mechanism reaches proof-gated admission too, so that framing earns a warning.
Two other framings emphasize a typical case without excluding others.
