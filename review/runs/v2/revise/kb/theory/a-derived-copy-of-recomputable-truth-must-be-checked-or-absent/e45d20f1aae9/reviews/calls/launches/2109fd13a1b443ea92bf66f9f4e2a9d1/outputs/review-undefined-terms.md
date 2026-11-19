---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Any use-shaped artifact depends on its sources"
    reason: "\"Use-shaped artifact\" is KB-internal phrasing that is neither defined nor paraphrased. The rest of the sentence explains derived versus abstracted content, but not what makes an artifact \"use-shaped\", so the reader cannot tell which artifacts the claim covers."
    level: warn
  - scope: passage
    quotes:
      - "the interrupt-placement problem dissolves"
    reason: "The note treats \"the interrupt-placement problem\" as already known, but never states it. The neighbouring clause (\"the validator is the edit-time surface\") hints at the meaning, but the reader still has to infer that the problem is where to put the signal that tells someone a dependent artifact needs review when its source changes."
    level: warn
  - scope: passage
    quotes:
      - "The sweep pattern is hand-authored"
    reason: "\"The sweep pattern\" appears with a definite article and no antecedent. The reader cannot tell that it means the validator's rule for collecting tag members across collections. The same sentence also uses \"head\" and \"one hop\" with only the earlier gloss \"curated per-tag heads\" for support."
    level: warn
  - scope: passage
    quotes:
      - "wants a recomputable value inlined, since re-deriving it on every call is a hot-path cost"
    reason: "Frontloading is a registered vocabulary term. Here it appears only as the title of a link, and the clause describes what it wants rather than what it is. A short inline gloss (computing a value ahead of time and inserting it into the instruction) would let the reader follow later uses such as \"frontloaded region\" without opening the link."
    level: info
  - scope: passage
    quotes:
      - "This looks like it reopens the regress"
    reason: "\"The regress\" has no earlier antecedent in the note. The intended meaning (who checks the checker) can be inferred from the sentence before, so this is minor."
    level: info
outcome: warn
---

# Review

## Summary

Most technical terms are glossed in place. "Completeness mark" carries both a link and a parenthetical definition, as do "compiled cue", "managed staleness" (via its colon list), Level A and Level B, and lineage. Preconditions 1–4 each define their own condition.

Three terms are used as if the reader already knew them: "use-shaped artifact", "the interrupt-placement problem" and "the sweep pattern". Each sits in a sentence whose claim depends on that term, so the reader either has to guess or leave the note to find out. Frontloading is a registered vocabulary term introduced only through a link title, with a partial functional paraphrase, so it is recorded at info level. "The regress" lacks an antecedent but can be recovered from its sentence.
