---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A claim of full automation must say which tasks it preserves and which requirements it retires."
    reason: "Syntactically, 'it' refers to 'a claim', but a claim neither preserves tasks nor retires requirements; the intended agent is the automation change. 'Preserves' can also be read two ways: the task stays human work, or the task is kept in some form, possibly automated. Most readers will recover the intended meaning from the previous sentence, so this is minor. One possible fix: 'must say which human tasks the change keeps and which requirements it retires.'"
    level: info
  - scope: passage
    quotes:
      - "Optional assessment creates neither when the process can proceed without it and its specification does not require it."
    reason: "The sentence has three pronouns. 'It' (after 'without') and the final 'it' refer to the assessment. 'Its specification' is meant to be the process's specification, but it can be read as the assessment's own specification. Context makes the intended reading likely, so this is minor. One possible fix: 'the process specification'."
    level: info
outcome: pass
---

# Review

## Summary

No sentence has a plausible unintended reading that would change the note's claim. Two sentences have pronoun-reference looseness that the reader can resolve from context. They are recorded as INFO. Negation scope is handled carefully throughout, for example "not by itself evidence that the system would fail" and "not automation of that review". Modifier attachment is also unambiguous, for example in "though not of the earlier adoption" and "A claim about automated adoption alone".
