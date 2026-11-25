---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Harness code may offload much of a selection loop, leaving three base LLM competences"
    reason: "Scope drift: the H1 does not say the loop is autonomous. The body limits its claim to an autonomous selection-based learning loop in open-ended work. It also says that a human-assisted bootstrap can have 'people temporarily supply the missing semantic step', and its Scope section proposes the competences as 'necessary for operating the loop autonomously'. So the body establishes that harness code can take over much of the loop's mechanical and structural machinery and that, for autonomous operation in open-ended work, three semantic competences remain on the frozen base LLM. Without 'autonomous', the H1 implies the competences stay on the base LLM in any selection loop, including human-assisted ones where the body says people can supply them. The filename slug and description both say 'autonomous'; the H1 drops it."
    level: warn
outcome: warn
---

# Review

## Summary

The body mostly supports the title. It lists three groups of work that harness code can offload: enforcement and context assembly, evidence capture and replay, and store bookkeeping. It then names three semantic competences that remain on the base LLM. It also argues that store maintenance and criterion revision reduce to competences 2 and 3 rather than adding a fourth. That supports the count of three. The hedge "may" matches the body's framing of the split as a working hypothesis.

The mismatch is scope. The body conditions the residue on autonomous operation in open-ended work, where new failure modes keep arriving. It says plainly that humans can supply the missing semantic steps during a bootstrap. The H1 says only "a selection loop," which is broader than what the body establishes. Adding "autonomous" to the H1 would align it with the body, the description and the filename.
