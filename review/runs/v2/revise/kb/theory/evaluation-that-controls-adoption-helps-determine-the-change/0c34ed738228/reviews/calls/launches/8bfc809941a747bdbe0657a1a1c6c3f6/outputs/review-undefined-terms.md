---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Participation in selection does not by itself determine whether the evaluator counts as part of the learner. That depends on the declared system boundary."
    reason: "\"The learner\" and \"declared system boundary\" are used as if the reader already knows them. They are not glossed, and nothing earlier in the note introduces the idea that an improvement claim names a learning system with a declared boundary. Without that idea, a first-time reader cannot tell what being \"part of the learner\" would mean or who declares the boundary. Add a short inline gloss, such as \"the system credited with learning, whose extent the improvement claim declares\", and link the source note if one exists. The open question's \"declared learner boundary\" depends on the same unexplained concept."
    level: warn
  - scope: passage
    quotes:
      - "Supplement to the adoption-versus-measurement distinction in [the better-factory comparison]"
    reason: "\"The better-factory comparison\" names a KB-internal argument and gives no hint of what it compares. The body can be read without it, so the cost is low. A few words saying what that note claims would still tell the reader whether to follow the link."
    level: info
outcome: warn
---

# Review

## Summary

The core vocabulary works for a first-time reader. The two worked cases define "approval before adoption" and "assessment after adoption" through what the evaluator controls. "Adoption" receives an inline gloss, "entering a live behavioral path on which later operation depends", next to its link to the operative-change definition, so the link is not doing the defining.

The gap is in the Scope section. "The learner" and its "declared system boundary" import a framework concept from elsewhere in the KB without saying what it is. This is the one place where the reader would have to know KB context to follow the sentence. The supplement pointer's "better-factory comparison" is opaque but has little effect on comprehension.
