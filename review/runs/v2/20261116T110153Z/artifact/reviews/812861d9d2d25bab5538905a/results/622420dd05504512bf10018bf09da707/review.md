---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'Feasibility and commitment scope: the note never states whether the requested
    commitment is a bounded probe, a reversible trial, routine reliance, or a costly-dependency
    choice. The adoption criteria call for a trial and also for an operator choice
    about what register membership means, which reads as a change to the shared source
    contract consumed by workers, validators and judges. Without a stated scope the
    reader cannot tell how much support is needed or whether an entrenchment argument
    (what would depend on the change, what reversal would disturb) is owed.'
  level: warn
- scope: passage
  quotes:
  - Existing source-resolution and quote-generation code supplies the revision boundary
  reason: 'Feasibility and commitment scope: this is the whole feasibility case for
    the recommended option. It asserts that existing code supplies the revision boundary
    but names no witness and identifies no unresolved obstacles, such as which validator
    or judge instructions currently check citations against the register and would
    need changing, or how the inspected-scope field would be bounded once paths no
    longer appear in it.'
  level: warn
- scope: passage
  quotes:
  - A trial must demonstrate that a specialist can cite a newly inspected path at
    the same revision without reopening the boundary
  reason: 'Adoption criteria: the trial names its output (newly inspected paths cited,
    unknown IDs and missing paths still refused) but not its cost, its stop condition,
    or whether it can run without first changing the shared contract that it is meant
    to evaluate. The cost of waiting is not addressed either: the note does not say
    whether runs keep stopping on the inventory interpretation in the meantime.'
  level: warn
- scope: passage
  quotes:
  - Source membership and quotation occurrence do not establish semantic support.
  reason: 'Transferable theory stays in notes: this is a general, truth-apt claim
    stated inline as a force with no theory citation. It is short and directly constrains
    the options, so it is tolerable here, but if it is meant as transferable it should
    be cited from kb/theory/.'
  level: info
outcome: warn
description: Retained verdict review of kb/reference/proposals/source-registers-without-duplicated-path-inventories.md
  against kb/reference/types/design-proposal.md
contract: verdict
note: kb/reference/proposals/source-registers-without-duplicated-path-inventories.md
criterion: kb/reference/types/design-proposal.md
note-sha256: 54246266704736d97ee16733057fc50339ada823e0952926d210e4d1665ffaf2
criterion-sha256: ecf1501289ea51492dbed7d976f50816f6344643e805d5dc5355659696d5730e
target-sha256: 54246266704736d97ee16733057fc50339ada823e0952926d210e4d1665ffaf2
target-capture: kb/reports/state/review/runs/v2/20261116T110153Z/artifact/reviews/812861d9d2d25bab5538905a/inputs/target/kb/reference/proposals/source-registers-without-duplicated-path-inventories.md
observation: kb/reports/state/review/runs/v2/20261116T110153Z/artifact/reviews/812861d9d2d25bab5538905a/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T110153Z
launch: 622420dd05504512bf10018bf09da707
completed-at: '2026-11-16T11:02:31Z'
raw-output: kb/reports/state/review/runs/v2/20261116T110153Z/calls/launches/622420dd05504512bf10018bf09da707/outputs/review.md
raw-output-sha256: bb792b57c335c9a9a31ef2c9381138a7c9c59884fe88d875b731114dcc61248f
format: 2
---

# Review

The note meets the type spec's core requirements. The description leads with
"Proposal:", and the final sentence says the shipped contract does not change.
It has a dated current-state anchor that cites a concrete run and separates the
inventory fault from the run's other faults. The opening states the problem and
the intended outcome. It sets out three materially different options, and each
one gives an operativity path: what would consume the change, and as what
authority. The recommended option also says where the new check's warrant
stops: file existence is not treated as support. The forces separate the
boundary commitments (traceability to the frozen revision, a visible source
identity) from the open choices. The adoption criteria name the operator
decision on which selection depends, and they keep the unrelated
reconciliation and quote-integrity faults out of scope.

The gaps are in feasibility, commitment scope and the probe. The note does not
say how much it asks the operator to commit, and its feasibility case for the
recommended option is a single sentence with no named obstacles. The trial it
requires has an output but no cost, stop condition or account of waiting.
These are specific instructions that go unmet in an otherwise conforming
proposal, so the outcome is WARN, not FAIL.
