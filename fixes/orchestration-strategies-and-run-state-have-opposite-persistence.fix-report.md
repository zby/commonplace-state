# Fix report: orchestration-strategies-and-run-state-have-opposite-persistence

Note: `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md`
Review model partition: `claude-opus-4-8`
Source review runs: 2139 (accessibility), 2144 (sentence)

## Findings → fixes

| Gate | Finding | Strategy | Status |
|---|---|---|---|
| `sentence/clause-packing` | Line 18 RLM-loss sentence (~40 words) chains three ideas; trailing "on a task where the same shape would have worked" restates the recurrence premise. | `redundant-clause-trimmed` (new-pattern) | fixed |
| `accessibility/notation-opacity` | Bare `K` reused throughout prose with no formal argument in this note. | — | deferred |
| `accessibility/notation-opacity` | Bare `select` / `select`-X reused throughout prose. | — | deferred |

## Fix detail

**`sentence/clause-packing`** — applied the reviewer's suggested revision verbatim: split the sentence at "is the loss" and dropped the trailing clause "on a task where the same shape would have worked," since the recurrence premise is already established in the same paragraph.

- Before: *"Discarding the `select`-strategy with it is the loss — a decomposition the model searched for and got right is gone before the next query arrives, so the same search is paid again on a task where the same shape would have worked."*
- After: *"Discarding the `select`-strategy with it is the loss. A decomposition the model searched for and got right is gone before the next query arrives, so the same search is paid again."*

Argument unchanged; only working-memory load reduced.

## Deferred

**`accessibility/notation-opacity`** (both findings) — deferred by maintainer decision. The `K` / `select` notation is shared anchored vocabulary across the orchestration cluster (`bounded-context-orchestration-model`, `rlm-…`, `the-practical-scheduler-is-the-host-language`), and `prose/pseudo-formalism` plus `semantic/grounding-alignment` both passed on the same usage, treating it as load-bearing cross-note continuity rather than decoration. Stripping the symbols would improve standalone readability at the cost of that continuity — a tradeoff the maintainer chose not to take. Left as a standing, accepted WARN.

## New patterns

- **`redundant-clause-trimmed`** — fix for `sentence/clause-packing` where a long sentence ends with a clause that restates a premise already established in the same sentence or paragraph; the fix splits the sentence and deletes the redundant tail. First observed instance; not yet promoted to `fix-strategy-taxonomy.md` (needs 3+ recurrences). A would-be "Sentence clarity" category currently has no entries.
