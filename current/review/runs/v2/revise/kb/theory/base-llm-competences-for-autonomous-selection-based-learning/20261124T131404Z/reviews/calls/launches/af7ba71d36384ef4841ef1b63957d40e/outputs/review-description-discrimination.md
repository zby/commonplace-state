---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "harness code can supply much of an autonomous selection-based learning loop, leaving three conjectured semantic competences on the frozen base LLM"
    reason: "The description mostly restates the title's structure: harness code takes over much of the loop and three competences remain. It adds the epistemic status ('working hypothesis') and the qualifiers 'autonomous', 'semantic' and 'frozen'. It does not name the three competences: interpreting unformalized text, diagnosing novel failures and synthesizing remedies, and judging unformalized trade-offs. It also does not say which work moves to harness code: enforcement, evidence capture and replay, and store bookkeeping. Those details would separate this note from nearby notes on scheduler–LLM separation, semantic-work relocation and on-balance judgment in a short result list."
    level: warn
outcome: warn
---

# Review

## Summary

Read with the title, the description adds some context. It says the split is a working hypothesis, the loop is autonomous and the remaining competences are semantic and sit on a frozen model. Its sentence shape still mirrors the title: harness code supplies much of the loop, and three competences remain.

The note's retrieval value lies in naming those three competences and saying which kinds of work move to harness code. The description gives neither. An agent searching for a list of base-model prerequisites, or for where diagnosis and trade-off judgment sit, would get little from it beyond the title. Naming the three competences in compressed form, such as "interpretation, diagnosis/synthesis, and trade-off judgment," would make it discriminating.
