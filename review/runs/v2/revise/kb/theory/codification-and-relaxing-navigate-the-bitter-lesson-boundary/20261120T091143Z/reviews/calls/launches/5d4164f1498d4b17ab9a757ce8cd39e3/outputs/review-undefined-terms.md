---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The bitter lesson describes a trajectory, not a law of nature."
    reason: "\"The bitter lesson\" names the note's governing concept and appears in its title. The body never glosses it. Its one body mention comes at the end of a section, after the reader is assumed to know it. A newcomer needs one clause near the opening saying what it is, for example that general methods which scale with computation eventually beat hand-built domain structure."
    level: warn
  - scope: passage
    quotes:
      - "Merely writing the convention in natural language constrains without codifying it."
    reason: "\"Constrains\" uses the active vocabulary term constraining. Here it has neither an inline gloss nor a link to its definition. The sentence depends on the contrast between constraining and codifying, so the reader needs to know what constraining means, for example \"narrows the interpretations an agent may take\". This mention also needs a link to definitions/constraining.md."
    level: warn
  - scope: passage
    quotes:
      - "what relaxing reverses is the extraction, not symbolic membership"
    reason: "\"Symbolic membership\" is not defined. The reader has to infer that it means the component staying on the symbolic side of the codification definition. A plainer phrasing, such as \"not the component's status as a codified reference\", would remove the inference."
    level: warn
  - scope: passage
    quotes:
      - "seen from the author's side rather than the survivor's"
    reason: "Neither \"author\" nor \"survivor\" is introduced. The contrast makes sense only to someone who has read the linked conjecture note. Say who each party is, for example \"the person committing the rule\" and \"the method that outlasted scaling\"."
    level: warn
  - scope: passage
    quotes:
      - "isolation-vs-integration gaps"
    reason: "This relaxing signal is listed without explanation. Distribution shift and paraphrase brittleness can be inferred from their names, but this one cannot. Add a short gloss, for example \"a component passes in isolation but fails inside the whole system\"."
    level: info
  - scope: passage
    quotes:
      - "κ = 0.28 for CoT"
    reason: "\"CoT\" is not expanded. Chain-of-thought is common in LLM work but is less standard than the vocabulary the gate exempts. Expanding it once costs little."
    level: info
outcome: warn
---

# Review

Most technical terms are glossed where they first appear.

- Codification is linked and defined inline as moving a rule into symbolic form.
- The fixed-artifact distinction is paraphrased in the opening sentence.
- The arithmetic and vision-feature regimes are defined in the bullets right after their first mention.
- Relaxing is defined in bold where it is introduced.
- Spec mining is explained in the sentence after its link.
- Epiplexity and time-bounded entropy have parenthetical glosses.
- Induction bias is glossed as step-by-step decomposition.

The main gap is that the note never says what the bitter lesson is, although the title depends on it. The vocabulary term "constraining" also appears without its required gloss and link. Two internal phrases depend on context the reader has not been given: "symbolic membership" and the author/survivor contrast. One relaxing signal and the CoT abbreviation are minor.
