---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "These questions identify possible friction. They do not yet supply a scoring rule or universal threshold."
    reason: "The opening already states that this is 'a qualitative design criterion, not yet a metric', and the Open questions section asks which cost a measurement should use. This closing caveat adds nothing to either and only guards against a misreading the note has already ruled out. Cut it, or fold 'universal threshold' into the opening qualifier if that phrase matters."
    level: warn
  - scope: passage
    quotes:
      - "An artifact does not need an outbound link in every case. Backlinks, an index, or search may supply the outward route. Nor does every task need to return to a broad view after reading detail. Fluidity is relative to the task and to the navigation operations actually available to the reader."
    reason: "Most of this paragraph repeats earlier text. The third criterion question already accepts 'an available route such as an authored link, index, or search'. The opening already rejects 'a claim that every task needs the same sequence of views', and 'task-relevant switches' already makes fluidity task-relative. The second Open question repeats the backlinks-versus-outbound-link point. Only the explicit mention of backlinks is new; add it to the third question's list of routes and delete the paragraph."
    level: warn
  - scope: passage
    quotes:
      - "The link's relation does not by itself determine which artifact is more abstract; its role is to preserve the task-relative relationship across the transition."
    reason: "The first clause repeats the opening's definition of resolution as view scope and detail, not as 'an intrinsic abstraction rank assigned to an artifact'. It may still prevent readers from treating link direction as an abstraction hierarchy. The second clause repeats the paragraph's first two sentences. It is unclear whether the sentence does necessary work for this misreading."
    level: info
outcome: warn
---

# Review

The note is mostly compact. The four mechanism paragraphs each name a different
Commonplace surface and link to its support. The four questions turn the
criterion into checks that can be applied. The discovery section limits the
note's claim about recognition. The first Boundaries paragraph separates the
idea from addressability grain. Deleting any of these would make the note less
grounded or easier to misapply.

The redundancy is in the caveats. The note says it is qualitative and
task-relative in its opening. It says this again after the questions, then
again in the second Boundaries paragraph. The Open questions section covers
the same ground a fourth time. Each repeat is accurate, but each pre-empts a
misreading that an earlier sentence already rules out. That is the defensive
redundancy the criterion describes. Keeping the opening qualifier and the Open
questions, and adding "backlinks" to the third question's list of routes,
would keep everything these passages contribute in less space.

The sentence in the link-context paragraph about link relations and abstraction
is less clear-cut. It may answer a misreading specific to links, so it is
reported as INFO rather than WARN.
