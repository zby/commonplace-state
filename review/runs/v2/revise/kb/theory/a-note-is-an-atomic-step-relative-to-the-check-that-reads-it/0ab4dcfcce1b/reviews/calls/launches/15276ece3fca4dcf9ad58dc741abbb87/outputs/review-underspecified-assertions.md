---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "eight cite more than five distinct sources"
    reason: "'Sources' has two reasonable readings: (a) any distinct linked artifact, including notes, ADRs and reports; (b) cited source ingests only, and of those either all or only the unquoted ones. The note itself argues that linked notes are not sources and that quoted sources do not count against the step. The unresolved choice is the counting population. It is material: under (a) or under 'all ingests', the conclusion that these eight notes are not atomic steps for the grounding check does not follow from the note's own unit. Under 'unquoted ingests' it does. The count of 344, the threshold of five and the date are also given without a method, so the evidence needed to support the assertion is unclear."
    level: warn
  - scope: passage
    quotes:
      - "A verdict resting on fourteen artifacts costs as much to audit"
    reason: "This contrasts with 'three sources and six quoted passages'. It is unclear whether the three sources are unquoted, which would mean opening them, or the sources of the six quotes, which would mean opening nothing. The difference changes how far auditability actually differs between the two cases, but the surrounding paragraph makes the intended reading likely, so this is informational."
    level: info
outcome: warn
---

# Review

Most load-bearing assertions are specific. The unit of cost is defined as the artifacts in which the reviewer must find the supporting passage. The experiment's numbers are given, the kind of number N is named while its value is left explicitly undecided, and the limits of quoting are stated with their consequence for the count.

The corpus paragraph is the one place where an unresolved choice changes the argument. It is the note's main evidence that the two bounds diverge in practice. Its count of "distinct sources" does not say which linked artifacts count, while the note's own mechanism makes that distinction decisive. Depending on the reading, the eight notes either support the claim that the bounds come apart or do not show it.
