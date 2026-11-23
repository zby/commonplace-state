---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Withholding or altering the retained entry must change later behavior"
    reason: "The two-part check is derived from the preceding definition of what a change is. That definition explicitly includes changes that removed content ('whether it added, revised or removed content'). For a removal there is no retained entry to withhold or alter. The operative-dependence test, as worded, does not apply to deletions or pruning, which the note itself recommends against accretion. Restoring the removed entry would be the counterpart test, but the stated criterion does not cover it."
    level: warn
  - scope: passage
    quotes:
      - "five hazards can defeat it"
    reason: "The hazard list and the falsification condition after it are not claimed to be exhaustive. Still, one boundary case the note itself raises fits them only by strain: a double-loop criterion revision that rewards itself. The EURISKO credit-hijacking example is that case, and revising working criteria is part of the bet. It can be read as false-positive acceptance of a criterion edit. But the falsification sentence names only false positives, unfaithful rationales and accretion, and nothing addresses criterion capture specifically."
    level: info
  - scope: passage
    quotes:
      - "the judge can favor either version or leave the comparison open"
    reason: "The judge's outcomes are listed as favor either version or open. The linked necessary-preference account also distinguishes a tie, where every compatible measure scores the versions equally, and 'better on some, tied on the rest'. A purely neutral edit, such as a rewording that no measure tracks, maps only awkwardly onto 'open'. The coverage is strained rather than broken."
    level: info
outcome: warn
---

# Review

## Summary

I tested the note's frameworks against boundary cases. These were the two-part empirical check, the self-improvement ladder (learns by selection / self-improving / double-loop), the proof–formula–heuristics–robust-comparison progression, the comparison table, the hazard list and the judge's verdict space.

Most of them hold. The ladder handles its simplest case (an externally picked checkpoint) and its most extreme case (a team revising its own criteria). The table's contrast survives selection over weights, because the AlphaGo Zero example places checkpoint gating in the selection column. The precedent progression is used as an illustrative sequence, not a claimed taxonomy.

The clear gap is the operative-dependence test. The note defines a change to include removals, then states a test that presupposes a retained entry. Deletion, which is the note's own remedy for accretion, therefore falls outside the test as worded.
