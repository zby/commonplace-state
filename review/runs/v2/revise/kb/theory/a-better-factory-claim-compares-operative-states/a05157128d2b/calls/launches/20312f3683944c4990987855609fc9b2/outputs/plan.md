purpose: "Agents and maintainers who design or evaluate self-revising factories should be able to tell, on one read, what an auditable improvement claim compares and which requirements must be fixed before development, without working through caveats the note repeats."
must-keep:
  - "A candidate that is generated and discarded never enters the comparison, so a better-factory claim cannot be read off a construction event."
  - "Antecedence guards this claim's auditability; it is not constitutive of improvement."
  - "An independently supplied retrospective criterion can ground a legitimate improvement claim."
  - "The two-component relation (non-regression plus a named target) is the shape this framework declares, not the only declarable one; a relation permitting retirement of obsolete or unsafe prior capability can be declared, and the preserved-path consequence then no longer follows."
  - "A comparison judges the adopted states; whether an evaluator also controlled adoption is a separate causal question."
  - "If the checked prior scope includes an operative path for factory development, non-regression requires the successor to preserve that capability."
  - "Holding model weights fixed does not put the comparison out of reach."
  - "A passed comparison does not identify the experience-to-change link; the declared comparison judges improvement, and the experience-to-change link distinguishes learning."
passes:
  - pass: fix-strategy-taxonomy
    scope: "First mention of 'software factory' in the opening paragraph, and the phrase 'open production family'"
    finding: kb/reports/state/review/results/kb/theory/a-better-factory-claim-compares-operative-states.md/accessibility/undefined-terms.md
  - pass: readability-and-flow
    scope: "Whole body except the H1, the TODO line, the sentences 'Both are declared while only the predecessor exists.', 'Prior declaration prevents that form of post-hoc selection.' and 'In a continuously revised system, the successor can instead be the operative state at a named measurement boundary, after one change or a period of development.', the predecessor definition bullet, the Scope bullet beginning 'Antecedence guards this claim's auditability', and the Relevant Notes footer"
  - pass: fix-strategy-taxonomy
    scope: "The opening sentence's clause 'a retained change to its reusable machinery that later work depends on'"
    finding: kb/reports/state/review/results/kb/theory/a-better-factory-claim-compares-operative-states.md/sentence/parsing-ambiguity.md
  - pass: fix-strategy-taxonomy
    scope: "The sentence beginning 'Because the deployed system rather than the model alone is the unit of learning'"
    finding: kb/reports/state/review/results/kb/theory/a-better-factory-claim-compares-operative-states.md/sentence/clause-packing.md
  - pass: fix-strategy-taxonomy
    scope: "The phrase 'just not this audit-proof one' in Scope"
    finding: kb/reports/state/review/results/kb/theory/a-better-factory-claim-compares-operative-states.md/prose/mannered-prose.md
stop: null
