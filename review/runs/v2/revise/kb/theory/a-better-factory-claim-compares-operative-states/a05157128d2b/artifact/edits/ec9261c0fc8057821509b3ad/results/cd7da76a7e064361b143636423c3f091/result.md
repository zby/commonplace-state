---
type: types/edit-result.md
outcome: changed
changes:
- 'new-pattern (undefined term linked but not glossed at first mention): opening sentence
  ''A [software factory](...) undergoes'' — added the appositive gloss ''a production
  environment configured with reusable knowledge for building one declared family
  of software products'', taken from the linked definition.'
- 'new-pattern (KB-specific phrase used without definition): ''over its open production
  family'' — appended the gloss ''the open-ended range of products and production
  tasks the factory may face''.'
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/theory/a-better-factory-claim-compares-operative-states.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/theory/a-better-factory-claim-compares-operative-states.md
input-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/artifact/edits/ec9261c0fc8057821509b3ad/results/cd7da76a7e064361b143636423c3f091/candidate.md
candidate-sha256: 1c000cb05df5ca6b9e071f1cc1d75c2532c6557e0cf02ae358f0ae6aeb9879f2
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/artifact/edits/ec9261c0fc8057821509b3ad/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b
launch: cd7da76a7e064361b143636423c3f091
completed-at: '2026-11-18T00:30:57Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/calls/launches/cd7da76a7e064361b143636423c3f091/outputs/result.md
raw-output-sha256: 499e978cd566a6fcdfb7b302b6471dfa07207d4567d674288c5cc46bc158b938
---

# Report

Two glosses added within scope; no claim, link, quote or other passage changed. Both fixes are `new-pattern`: an accessibility finding that a term is used without an inline gloss, resolved by an appositive at first mention. No listed strategy covers undefined terms.

- Finding 1 (software factory): gloss follows the linked definition's stable core (an environment configured with reusable production knowledge for one declared family). It does not add the Greenfield lineage detail.
- Finding 2 (open production family): glossed at first use only. The later mentions in Scope ("over an open family") and Open Questions ("the declared family is open-ended") now resolve against that gloss and are left unchanged.

Not touched:

- Finding 3 (info, "factory development" at first use in the relata list): outside the supplied scope, which names only the first mention of 'software factory' and 'open production family'.

Noticed but not applied: the blockquote TODO about replacing "software factory" with "software house" is retained verbatim. Acting on it would change the note's compared object and lies outside this operation.
