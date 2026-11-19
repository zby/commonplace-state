---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the rule rides entirely on that"
    reason: "Literal meaning: the rule depends entirely on this asymmetry. \"Rides on\" adds no precision or mapping that the note later uses, and the reader has to translate the idiom. Replacement: \"and the rule depends entirely on that asymmetry\" removes the translation step without losing anything."
    level: warn
outcome: warn
---

# Review

Most figurative wording in the note does useful work. "Collapse into one free step" (detection and verification) and "the interrupt-placement problem dissolves" are conventional, and the following clauses state their literal mechanism. "The forbidden state, just relocated one layer down, with a stronger trust signal attached" sharpens the regress argument in precondition 4. "A machine watches the situation on the author's behalf" is immediately made literal as "converting staleness into a validation failure at check time". "Degrade gracefully" is standard engineering vocabulary, and the same bullet defines it. "One missed edit away from the catastrophic state" has a strong connotation of scale. The preceding paragraph's "silent, unbounded wrongness" supports that connotation, so it is not flagged.

One local idiom, "the rule rides entirely on that", contributes nothing that the literal "depends entirely on" lacks, so the gate returns WARN for a single instance. The pattern is not pervasive.
