purpose: "Judge whether the rewritten note states good theory, and improve its text where the reviews find real defects."
defend:
  - "A claim's test record does not determine its fit in a working theory"
  - "Three things can be asked about a claim in it, and no answer to one settles another."
  - "A well-tested claim may fit poorly."
  - "A false, overgeneral or weakly tested claim may fit smoothly, because the current implementation, the vocabulary or the neighbouring claims already assume it."
  - "Neither may be substituted for the other."
  - "Which repair to make is a decision, taken by comparing the test records of the claims involved and what each repair does to the theory's fit to its problem."
passes:
  - pass: narrow-overclaims
    scope: "The independence definition in the test-record bullet ('does not presuppose the working theory': narrow to not presupposing the claim under test or an auxiliary whose acceptance would make the outcome automatic) and the 'So use of a claim inside the theory can be a test … not where the evidence was produced' paragraph, made consistent with it; in 'The two kinds of evidence inform each other', the sentences 'has earned a new independent test' (separate failing to yield a useful prediction from yielding a wrong one; drop 'earned'), 'may require restructuring the working theory' / 'force a change of fit', and \"'This claim is well tested' is not a reason to retain it in this theory\" (narrow to not by itself a reason)."
  - pass: fix-strategy-taxonomy
    scope: "The truth bullet of the opening list and the first sentence of 'A test record is not truth': say what a derivation settles for a formal claim, or scope the conjecture claim to non-formal claims."
    finding: kb/reports/state/review/results/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md/semantic/completeness-boundary-cases.md
  - pass: fix-strategy-taxonomy
    scope: "The §82 citation sentence in 'Fit is not an independent test': mark the could-have-failed criterion as adapted from Popper's sincere-attempt condition, and cite §82 starred note *1 and Appendix *ix."
    finding: kb/reports/state/review/results/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md/semantic/grounding-alignment.md
  - pass: readability-and-flow
    scope: "Replace the 'This note uses \"test record\" where it earlier used \"warrant\"' paragraph with a short bridge clause in the test-record bullet (dependents still say 'warrant'); cut the trailing 'It is not a guarantee that later tests will go the same way.'; state the could-have-failed condition once in 'Fit is not an independent test', keeping the contrast 'not where the evidence was produced' and the section 4 slogan as a decision rule."
stop: null
