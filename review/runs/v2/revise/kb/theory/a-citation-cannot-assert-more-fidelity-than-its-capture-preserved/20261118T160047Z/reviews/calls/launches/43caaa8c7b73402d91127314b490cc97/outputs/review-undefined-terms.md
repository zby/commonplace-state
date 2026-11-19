---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A pin records identity"
    reason: "\"Pin\" appears here for the first and only time with no gloss. A reader can guess that it means the recorded checksum of a capture, but the sentence states that a pin records identity, so the reader needs the definition to evaluate the claim. Add a gloss, for example \"A pin (the recorded checksum of a capture) records identity\", or replace it with the plain phrase."
    level: warn
  - scope: passage
    quotes:
      - "trade-off between checking cost and reliance risk"
      - "not a universal rule for retained results"
    reason: "\"Reliance risk\" and \"retained results\" are KB-specific framings that are carried only by the link. The next sentence partly recovers the meaning (\"reuse the check's result, accepting the risk of changes since it ran\"). A short inline gloss would let the sentence stand alone, for example retained results as stored check outcomes reused later, and reliance risk as the cost of acting on an outcome that has gone stale or is wrong."
    level: info
  - scope: passage
    quotes:
      - "Quotations the extractor never recognized"
    reason: "\"The extractor\" is used with a definite article but is never introduced. Context implies it is the component that finds quote candidates in text, but naming that role once would remove the guess."
    level: info
  - scope: passage
    quotes:
      - "A locator the check does not test supplies context but is not evidence"
    reason: "\"Locator\" is not defined. The preceding line-range example makes it inferable, so this is minor. An example such as \"(a line range or page number)\" would make it explicit."
    level: info
outcome: warn
---

# Review

## Summary

Most technical terms are introduced with enough context. "Capture" is glossed at its first body use, "exact" gets its own definition section, and the four citation questions are each stated in one line. The note uses no active vocabulary term from `AGENTS.md` in its technical sense.

One term fails the test. "Pin" arrives unexplained in a sentence that makes a claim about what a pin does, and the reader has to infer its meaning from the earlier checksum sentence. The other gaps are minor: "reliance risk" and "retained results" depend on a link, while "the extractor" and "locator" are left for the reader to infer. Context mostly recovers these, so they are recorded as info.
