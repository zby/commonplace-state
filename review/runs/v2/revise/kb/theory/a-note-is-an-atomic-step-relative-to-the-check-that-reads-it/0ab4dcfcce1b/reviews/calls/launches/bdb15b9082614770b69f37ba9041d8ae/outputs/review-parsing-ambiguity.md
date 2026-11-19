---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the audit the bound buys is of the step the validator did not do, not of the one it cannot"
    reason: "The elliptical 'the one it cannot' leaves the reader to reconstruct which step each phrase names. The validator neither performs the support judgment nor checks the qualifying context, so 'did not do' and 'cannot' can each be read as naming either step. On a plausible reading, the audit covers the context check, which is the opposite of the intended meaning. Name the steps: 'the audit covers the support judgment, not the context check that only the source can settle'."
    level: warn
  - scope: passage
    quotes:
      - "now archived, identified when it concluded"
    reason: "Garden path. After 'the hazard the review-side proposal *...*,' the reader meets 'now archived, identified' and can take both participles as adjectives on the proposal ('archived and identified'). The reduced relative clause ('the hazard that the proposal identified') is recovered only on rereading. Make the relative pronoun explicit or restructure."
    level: warn
  - scope: passage
    quotes:
      - "which is the behaviour an artifact-side bound depends on"
    reason: "Modifier attachment. 'which' can attach to the reviewer honouring its cap, to the notes putting their support beyond the cap, or to both. The artifact-side bound plausibly depends on reviewers honouring a limit. It cannot depend on notes putting support out of reach. Name the antecedent, e.g. 'a reviewer that honours its cap is the behaviour ...'."
    level: warn
  - scope: passage
    quotes:
      - "one was missing retained support for"
    reason: "'one was missing retained support' can first be read as the finding itself lacking support (progressive 'was missing'), not as the finding's content. Context resolves it quickly, but 'one found missing retained support' would avoid the momentary misreading."
    level: info
  - scope: passage
    quotes:
      - "each grounded in one quoted passage, is one step for the grounding check"
    reason: "The plural subject 'two independent claims' takes 'is'. The intended reading is a note holding two such claims, but the agreement mismatch makes the reader look for a different singular subject. Write 'a note holding two independent claims, each grounded ..., is one step ...'."
    level: info
outcome: warn
---

# Review

The note mostly avoids syntactic ambiguity. Negation scope is handled carefully in sentences such as "Its cost is not links, and not bytes" and "N is not the point at which ...". Pronouns such as "them" in "is not one of them" have clear antecedents.

Three places allow a plausible unintended reading. The first is the elliptical contrast at the end of the auditability paragraph, which can reverse which step the audit covers. The second is a reduced relative clause after an italic title, which reads first as a pair of participles. The third is a "which" whose antecedent can be either half of the preceding coordination, and one of those readings does not make sense. Two smaller cases are recorded as info.
