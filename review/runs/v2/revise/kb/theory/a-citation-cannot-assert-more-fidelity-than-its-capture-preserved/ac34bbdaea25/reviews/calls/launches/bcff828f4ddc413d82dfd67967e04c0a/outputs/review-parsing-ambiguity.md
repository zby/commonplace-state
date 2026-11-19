---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The layering is not a design choice"
    reason: "After the dash, the sentence inserts a title-as-claim link as a bare clause: 'a framework rule with a boundary-preserving rival is not an inherited constraint'. Nothing signals its role. A plausible first reading asserts that clause of the layering, as if the layering had a boundary-preserving rival and so was not inherited. That is the opposite of the intended point. The intended reading, that the link names the test the layering passes, has to be reconstructed from the next clause."
    level: warn
  - scope: passage
    quotes:
      - "what was not preserved verbatim then is permanently downgraded"
    reason: "'then' can be read as temporal ('at ingest') or as consequence ('therefore'). The next words, 'recoverable only by…', also make 'permanently' look contradictory unless the reader takes 'permanently' to mean 'within this capture'."
    level: info
  - scope: passage
    quotes:
      - "A position-only locator would render them identical, which is the one distinction a consumer of the citation most needs."
    reason: "The 'which' clause attaches grammatically to 'render them identical', so the sentence literally calls the identity a distinction. Readers will probably recover the intended meaning, that the erased difference is the distinction consumers need, but the reference is loose."
    level: info
outcome: warn
---

# Review

Most sentences parse cleanly. Negation scope in 'This is a claim about fidelity, not authority' and 'is out of scope rather than in conflict' is clear. The pronouns in the Scope section ('that design', 'it') resolve to their nearest plausible antecedents. The warn finding is the title-as-clause construction: placed after a dash with no connective, the linked rule reads as something said about the layering, and that reading reverses the argument. Adding a connective that names the link's role (for example, 'by the rival test in …') would remove the ambiguity.
