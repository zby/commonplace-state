---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "— defines: the three forms this note ranges over"
    reason: "`defines` is not in the collection's label table. The registered label for a link to a term in `theory/definitions/` is `defined-in`."
    level: warn
  - scope: passage
    quotes:
      - "— sharpens: the unit those cross-form writes range over"
      - "— sharpens: the discriminator between evidence-responsive learning writes"
    reason: "`sharpens` is not in the collection's label table. Footer edges must use one of the listed labels, such as `extends`, `grounds` or `contrasts`, or be written as unlabelled inline links with a connective."
    level: warn
  - scope: passage
    quotes:
      - "— exemplifies: versioned prompts, schemas, tools, and tests as one concrete system-definition loop"
    reason: "The contract defines `exemplifies` as asymmetric from instance to general: the reader is at the instance and wants the general claim it falls under. Here the general note points to its instance, so the label runs backwards. The reverse edge belongs on the instance note. If this direction helps readers, use a label that fits it, or an inline link."
    level: warn
  - scope: passage
    quotes:
      - "— evidenced-by: surveyed systems already split into weight-promotion and artifact-promotion loops"
    reason: "Under 'Origin is not corroboration', an `evidenced-by` context phrase must say what the claim risked and whether the evidence was recorded after the claim or independently of how it was built. Otherwise it must say that the evidence qualifies or bounds the claim. This phrase does neither, so readers cannot tell whether the survey corroborates the claim or is its origin, which would make the correct label `abstracted-from`."
    level: warn
  - scope: passage
    quotes:
      - "[Constraining during deployment is continual learning]"
    reason: "The link text does not match the target's title, 'Constraining during deployment can produce learning outside weights'. It also states a stronger claim than the target makes, so a reader would import a premise the linked note does not assert."
    level: info
outcome: warn
---

# Review

## Summary

The note is correctly placed in `kb/theory/`. It names no Commonplace selection. Its claim is about the design space for deployed learning systems: persistence is not enough, and governed behaviour-changing writes are required. Scoping system choices leaves that claim intact. The claim reads as universal by default. The note makes no statistical claim that would need a stated refuter. It bounds its scope by naming what governance does not replace: storage, activation and parametric adaptation. It defers the cross-form trade space to its sibling note rather than overreaching. Inline links mostly use connectives and serve the argument. No link points into `kb/work/`. The note cites no tracked sources, so the unquoted-source limit is not in play.

The unmet conventions are all in the outbound-link footer. Three label conventions are unmet. Two labels, `defines` and `sharpens`, are not in the collection's label table. `exemplifies` runs from the general claim to its instance, the reverse of its defined direction. The `evidenced-by` edge does not state whether the survey corroborates the claim or only bounds it, as 'Origin is not corroboration' requires. These are local repairs. They do not affect placement or the quality of the claim, so the outcome is WARN, not FAIL.

As a minor point, one link's text paraphrases its target's title in stronger terms than the target asserts.
