---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The bitter lesson describes a trajectory, not a law of nature.
  reason: '"The bitter lesson" names the note''s governing concept and appears in
    its title. The body never glosses it. Its one body mention comes at the end of
    a section, after the reader is assumed to know it. A newcomer needs one clause
    near the opening saying what it is, for example that general methods which scale
    with computation eventually beat hand-built domain structure.'
  level: warn
- scope: passage
  quotes:
  - Merely writing the convention in natural language constrains without codifying
    it.
  reason: '"Constrains" uses the active vocabulary term constraining. Here it has
    neither an inline gloss nor a link to its definition. The sentence depends on
    the contrast between constraining and codifying, so the reader needs to know what
    constraining means, for example "narrows the interpretations an agent may take".
    This mention also needs a link to definitions/constraining.md.'
  level: warn
- scope: passage
  quotes:
  - what relaxing reverses is the extraction, not symbolic membership
  reason: '"Symbolic membership" is not defined. The reader has to infer that it means
    the component staying on the symbolic side of the codification definition. A plainer
    phrasing, such as "not the component''s status as a codified reference", would
    remove the inference.'
  level: warn
- scope: passage
  quotes:
  - seen from the author's side rather than the survivor's
  reason: Neither "author" nor "survivor" is introduced. The contrast makes sense
    only to someone who has read the linked conjecture note. Say who each party is,
    for example "the person committing the rule" and "the method that outlasted scaling".
  level: warn
- scope: passage
  quotes:
  - isolation-vs-integration gaps
  reason: This relaxing signal is listed without explanation. Distribution shift and
    paraphrase brittleness can be inferred from their names, but this one cannot.
    Add a short gloss, for example "a component passes in isolation but fails inside
    the whole system".
  level: info
- scope: passage
  quotes:
  - κ = 0.28 for CoT
  reason: '"CoT" is not expanded. Chain-of-thought is common in LLM work but is less
    standard than the vocabulary the gate exempts. Expanding it once costs little.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/5d4164f1498d4b17ab9a757ce8cd39e3/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/da72f5ca6c3f86d527c8fd01/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 5d4164f1498d4b17ab9a757ce8cd39e3
completed-at: '2026-11-20T09:13:05Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/5d4164f1498d4b17ab9a757ce8cd39e3/outputs/review-undefined-terms.md
raw-output-sha256: b1e2c06d9fb59c1bd57c661cf2e85cdba9d69d29dc262e6b6dcab170ec78807f
format: 2
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
