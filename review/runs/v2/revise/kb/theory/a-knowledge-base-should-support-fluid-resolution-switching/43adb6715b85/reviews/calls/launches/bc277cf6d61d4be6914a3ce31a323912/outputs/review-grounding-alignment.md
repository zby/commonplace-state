---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "its role is to preserve the task-relative relationship across the transition"
      - "the navigational value of"
    reason: "The linked note claims that a link's position and introducing prose encode its commitment level, producing a weighted graph. It gives that graph's navigational use as traversal priority: follow strong links before weak ones. This note presents bearing preservation during a change of scope as 'the navigational value' of that encoding. The target's table of relationship words does say that prose tells the reader what role the linked note plays, so the support is plausible. The transfer from commitment strength and traversal priority to preserving the relationship across a scope transition is not articulated, and 'the navigational value' also claims more than the target's own account of it."
    level: warn
outcome: warn
---

# Review

## Summary

All links resolve to library notes in `kb/theory/`. Each was checked by reading its title and opening.

- **Title as claim enables traversal as reasoning.** The target says claim titles make the first disclosure layer usable, so agents can choose what to load. This supports "a reader can inspect a chain of assertions before choosing which bodies to load." Aligned.
- **Link-following and search impose different metadata requirements.** The target contrasts local steps that carry source context with long-range search that lacks it. The note uses the target only to say that both routes can take part in a switch. Aligned.
- **Link strength is encoded in position and prose.** This is a modest extension that is not articulated (WARN above).
- **Pointer design tradeoffs in progressive disclosure.** The target names exactly the four axes the note cites. It describes pointers "at increasing resolution", with cheap ones scanned first, which supports the cost gradient. Aligned.
- **Recognition, not linking, is the hard problem.** The target makes recognition the expensive step and requires co-presence. The note claims only that switching helps assemble views and "does not perform the recognition". Aligned and appropriately bounded.
- **Footer links.** These comprise agents-navigate, addressability grain and end-to-end evaluation. The note's one-sentence paraphrase of grain ("the smallest amount one access path can retrieve for a matched target") matches the target's definition. The other footer relations are adjacent and make no stronger support claim.

The only issue is the link-strength attribution.
