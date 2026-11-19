---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Sizing a step to its checker rather than to the material is old."
      - "His assessment of what the structure delivers is measured"
    reason: "The Descartes and Lamport precedents take about two paragraphs and five verbatim quotations. The note itself says they are 'an analogy about checker-relative sizing, not evidence that any particular N carries over', so they carry no premise or inference step in the support route. Their job is to show that checker-relative step sizing has precedent. One quotation from each source would do that job: Descartes' second precept and Lamport's 'depends on the sophistication of the reader'. The 'long chains' gloss, Lamport's self-check test and the 'possible, not inevitable' aside with its modesty sentence each add elaboration without adding force. Compress the section in place to a short paragraph that keeps the analogy disclaimer and the closing point about the validator."
    level: warn
  - scope: passage
    quotes:
      - "now archived, identified when it concluded that any partition would have to be by claim rather than by link"
    reason: "The joint-support paragraph stops to recount the history of an archived proposal before it reaches its point. The by-claim partition constraint matters, and the paragraph restates it later ('the split has to be by claim'), so the provenance clause could shrink to a brief attribution or be dropped. The same paragraph also ends with a separate aside about links to other notes, which makes it long. Probably compressible, but the attribution gives the objection some standing."
    level: info
  - scope: passage
    quotes:
      - "whether a passage was lifted out of a qualifying context still costs a trip to the source"
    reason: "This caveat repeats the 'Occurrence is not representativeness' limit from the mechanism section almost word for word. Here it only qualifies what the audit covers, so a short back-reference ('the representativeness limit above still applies') would do the same work. It may be kept to stop readers from over-reading the auditability claim."
    level: info
outcome: warn
---

# Review

## Summary

Most of the detail in the note carries the argument. The co-loading versus checking split, the reasons for an artifact-side bound, the derivation of the source-counting unit from ADR 046 and ADR 073, the corpus counts and the rereading of the five-link-cap experiment all supply a premise, a boundary condition or an inference step. The account of the two findings that were absences of retained passages is short and does real work: it turns reviewer findings into validator results. The opening rejection of reviewer degradation as the meaning of N also earns its length, because it heads off the obvious misreading of the experiment.

The clear overhang is the historical-precedent section. The note itself says the precedents are only an analogy and not evidence, yet they get about as much space as the mechanism section. That is out of proportion to their job, so this review reports WARN with a recommendation to compress them in place. The two INFO findings are smaller: one archived-proposal provenance clause and one repeated caveat. Each could become a phrase, but either may be worth keeping.
