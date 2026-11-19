---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "a validator is centralized, versioned, reviewed on every change, and amortized across every copy it protects"
    reason: "The sentence beginning 'This looks like it reopens the regress, but it doesn't:' runs about 45 words and packs a concession, a contrast, a four-item property list, a consequence ('so its unit cost...') and a counterfactual comparison against N hand-maintained instances. The reader must hold the regress worry open across the whole list before reaching the conclusion. Split after the colon: one sentence for the validator's properties, one for the unit-cost comparison."
    level: warn
  - scope: passage
    quotes:
      - "the two tracked `AGENTS.md.template` copies"
    reason: "Distance problem: a two-clause parenthetical (root feeds wheel builds...; src/commonplace/_data serves editable installs) separates the subject 'the two tracked AGENTS.md.template copies' from its verb 'must be byte-identical', and a second parenthetical follows the predicate. Reorder so the predicate comes first ('must be byte-identical') and the two roles follow after it, or move the roles into their own sentence."
    level: warn
  - scope: passage
    quotes:
      - "too costly to run always and too noisy to block on"
    reason: "The Level B sentence states an identity (deciding invalidation is a Level B check), interrupts it with a dash gloss, then appends two cost judgments whose subject the reader must recover across the gloss. About 40 words with three ideas; tolerable but would read more easily with the cost judgments as a separate sentence."
    level: info
  - scope: passage
    quotes:
      - "the 2026-06-10 skill edits — logged in `kb/log.md` — chose read-the-contract per invocation"
    reason: "An Either/or sentence carries a parenthetical in each branch, and the second parenthetical nests a dash interruption inside it, so two unresolved dependencies are open at once. Moving the log location out of the parenthetical (or dropping it) would remove the nested interruption."
    level: info
outcome: warn
---

# Review

Most of the note's long sentences are front-loaded lists or parallel semicolon structures whose subject and verb resolve early, which the gate tolerates. Two sentences overload the reader: the precondition-4 sentence that defends the validator against the regress packs five ideas into one span, and the duplicated-build-artifacts bullet separates its subject from its verb with a two-clause parenthetical. Both can be fixed by reordering or a single split without losing any relation. The two INFO items are moderate peaks that do not require change.
