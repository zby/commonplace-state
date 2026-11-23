---
type: types/edit-result.md
outcome: changed
changes:
- 'new-pattern (stock lead-in or signpost sentence that only announces what the heading
  and the next element already show): deleted ''The structural contrast with weight
  training is starkest when laid side by side:'' before the comparison table.'
- 'new-pattern (same): deleted ''This is where the second level of our thesis—the
  machine learning bet—enters.'' so the paragraph opens with the bolded bet sentence.'
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
input-sha256: ccaa90636b62517eb5b64530f1400ed819e872c69af7626206dfacbccd5adc00
candidate: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/calls/launches/d3665f419579453ebf7a055b51ec0fa6/outputs/candidate.md
candidate-sha256: 1335b0e97e515ab6067688700c1167230cc7df9b340d894fc8ef35a5882c4a11
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/artifact/edits/9d44dcac87a8da417b757a0e/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z
launch: d3665f419579453ebf7a055b51ec0fa6
completed-at: '2026-11-21T19:49:25Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/calls/launches/d3665f419579453ebf7a055b51ec0fa6/outputs/result.md
raw-output-sha256: 4551cce136aae7eac9aba3d91b13e548768c0d77ad129d36b0f009f15d020f13
---

# Report

Two deletions, one per WARN finding of the stock-phrases review. Strategy:
`new-pattern`. The pattern is a stock lead-in or signpost sentence whose only
job is to announce what the section heading and the following element already
make plain. No listed strategy covers it, so the fix deletes the sentence, as
the finding asks.

- Finding 1, `The structural contrast with weight training is starkest when
  laid side by side:`, under "Deliberative learning versus training weights":
  deleted. The heading names the contrast, and the paragraph before the table
  already sets up the comparison of conditions, so the table now follows that
  paragraph directly.
- Finding 2, `This is where the second level of our thesis—the machine
  learning bet—enters.`, under "Proof, formula, judgment: where the bet
  enters": deleted. The heading names the bet, and the bolded "We bet that ..."
  sentence now opens the paragraph. That sentence is a must-keep claim and was
  not changed.

Not touched: finding 3 (`One strict condition attaches.`, level info). It is
outside the supplied scope, which covers only the two WARN sentences.

No links, quoted spans, claims or must-keep items changed. The input has no
`user-verified` field.
