---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 59a27bb0c8874f0eb150c9b50d4e9333
completed-at: '2026-11-22T09:36:20Z'
findings:
- scope: passage
  quotes:
  - Withholding or altering the retained entry must change later behavior
  reason: The two-part check is derived from the preceding definition of what a change
    is. That definition explicitly includes changes that removed content ('whether
    it added, revised or removed content'). For a removal there is no retained entry
    to withhold or alter. The operative-dependence test, as worded, does not apply
    to deletions or pruning, which the note itself recommends against accretion. Restoring
    the removed entry would be the counterpart test, but the stated criterion does
    not cover it.
  level: warn
- scope: passage
  quotes:
  - five hazards can defeat it
  reason: 'The hazard list and the falsification condition after it are not claimed
    to be exhaustive. Still, one boundary case the note itself raises fits them only
    by strain: a double-loop criterion revision that rewards itself. The EURISKO credit-hijacking
    example is that case, and revising working criteria is part of the bet. It can
    be read as false-positive acceptance of a criterion edit. But the falsification
    sentence names only false positives, unfaithful rationales and accretion, and
    nothing addresses criterion capture specifically.'
  level: info
- scope: passage
  quotes:
  - the judge can favor either version or leave the comparison open
  reason: The judge's outcomes are listed as favor either version or open. The linked
    necessary-preference account also distinguishes a tie, where every compatible
    measure scores the versions equally, and 'better on some, tied on the rest'. A
    purely neutral edit, such as a rewording that no measure tracks, maps only awkwardly
    onto 'open'. The coverage is strained rather than broken.
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/f030a8e5a0cd53e3c39ee020/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 3ed193ab76b24c2bd7c7824e22343acc17926ae7296017f3ea95017c06f0d1cf
---

# Review

## Summary

I tested the note's frameworks against boundary cases. These were the two-part empirical check, the self-improvement ladder (learns by selection / self-improving / double-loop), the proof–formula–heuristics–robust-comparison progression, the comparison table, the hazard list and the judge's verdict space.

Most of them hold. The ladder handles its simplest case (an externally picked checkpoint) and its most extreme case (a team revising its own criteria). The table's contrast survives selection over weights, because the AlphaGo Zero example places checkpoint gating in the selection column. The precedent progression is used as an illustrative sequence, not a claimed taxonomy.

The clear gap is the operative-dependence test. The note defines a change to include removals, then states a test that presupposes a retained entry. Deletion, which is the note's own remedy for accretion, therefore falls outside the test as worded.
