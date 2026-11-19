---
type: types/edit-result.md
outcome: changed
changes:
- 'new-pattern (a link whose text is a full clause serves as the subject of a reduced
  relative clause, causing a garden-path parse): first paragraph, ''This is the saving
  [frontloading spares execution context] argues for results computed before an LLM
  call, extended here to persisted artifacts.'' became ''The note [frontloading spares
  execution context] argues for this saving in the case of results computed before
  an LLM call; this note extends the argument to persisted artifacts.'''
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
input-sha256: 0016a4549affaa386d8c873c18667878c84e5aaa1a7816819519747789f0dbca
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/artifact/edits/615e7eb1e94bc13841f4f642/results/235b35bf82514453857be11a6c96c079/candidate.md
candidate-sha256: ec6b0dad7ebf4453b1698bfd707f618c8330d5010cc90cc93bd0a8e8ee801122
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/artifact/edits/615e7eb1e94bc13841f4f642/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z
launch: 235b35bf82514453857be11a6c96c079
completed-at: '2026-11-18T16:12:08Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/calls/launches/235b35bf82514453857be11a6c96c079/outputs/result.md
raw-output-sha256: e95bf258e4ba12e13c069b1008ad7b27b07a8c07e6c89468671be3444fdbdb14
---

# Report

- `new-pattern` — a link whose text is a whole clause acts as the subject of an unmarked relative clause, so the following verb attaches to the wrong noun. Passage: "This is the saving [frontloading spares execution context](./frontloading-spares-execution-context.md) argues for results computed before an LLM call, extended here to persisted artifacts." Change: gave the link a noun head ("The note …"), made "this saving" the explicit object of "argues for", marked the case with "in the case of", and split the extension into its own clause ("this note extends the argument to persisted artifacts"). The link target, the claim and the extension are unchanged.

Findings not touched:

- Finding 2 (INFO, "A check that fully recomputes the result on every use largely defeats it"): outside the supplied scope, which is limited to the sentence containing the frontloading link. The antecedent of "it" remains "that saving" in the preceding sentence.
