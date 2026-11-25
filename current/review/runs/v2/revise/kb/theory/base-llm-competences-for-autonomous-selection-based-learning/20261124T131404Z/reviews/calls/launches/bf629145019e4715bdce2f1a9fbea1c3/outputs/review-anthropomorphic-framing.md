---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the frozen model does not need to keep track of budgets, traces, or regression suites in its head"
    reason: "\"In its head\" attributes a private working memory to the model. The technical claim is that the model need not hold budgets, traces or regression results in its context window or reproduce them from its own outputs, because harness code records and supplies them. A literal phrasing such as \"the frozen model does not need to track budgets, traces, or regression suites within its context\" states the mechanism without implying internal mental bookkeeping."
    level: warn
  - scope: passage
    quotes:
      - "The model must read natural-language procedures, hypotheses, and constraints that have not yet been codified into code and let them govern its behavior"
    reason: "\"Read\" and \"let them govern its behavior\" are close to agency language, but the sentence is defining a functional competence and links operative change, which specifies behavioral dependence on loaded text. The verbs describe observable conditioning of outputs on context, not a claim about comprehension, so no change is required."
    level: info
  - scope: document
    quotes: []
    reason: "The competence labels (interpreting, diagnosing, judging, recognizing missing evidence) and the phrase \"overclaiming certainty\" name output-level capabilities that the note proposes to test through transfer tests. The note is explicitly arguing about which functions a model must perform, so these are functional descriptions rather than unsupported claims about cognitive internals."
    level: info
outcome: warn
---

# Review

The note is about which semantic functions a frozen base LLM must perform in an autonomous loop, so most cognitive-sounding verbs are functional competence labels tied to testable behaviour (operative change, transfer tests). Those are acceptable.

One idiom goes beyond that: "in its head" implies an internal mental store. The intended contrast is between harness-maintained records and the model's own context, and a literal phrasing would state that more precisely.
