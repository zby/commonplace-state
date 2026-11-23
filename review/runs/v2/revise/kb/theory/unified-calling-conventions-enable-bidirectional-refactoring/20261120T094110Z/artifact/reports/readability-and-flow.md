
# Report

Structural moves:

- Surfaced the divergence: the core claim (shared interface → callers unaware → local refactoring with unchanged call sites) now opens the note, with both directions named next to it, using only what the body states.
- Split the former single opening paragraph at its argument boundary: claim first, then the English-account premise it answers.
- Deduplicated the scheduler recap sentence and its fragment "No graph topology to update." against the table's Refactoring row (scope-directed removal).
- Cut "Both are callables with defined interfaces." (scope-directed removal).

Sentence-level edits: 6 (codification-breaks-callers split, semicolon splice in the friction sentence, a missing "and" in the breaking-change list, two scheduler-introduction tightenings, the English-account sentence split).

Relied-on terms and claims from kb-role are kept: same name resolving to either implementation, local refactoring with unchanged call sites, reversibility back to a prompt, the hybrid VM example, the imperative-scheduler versus graph-DSL contrast and per-agent local scope (table rows untouched). All must-keep items are preserved. Steps 3 and 4 and the table rows are untouched, per scope.

Noticed but not applied: the must-keep statement that switching to a prompt "need not reflect brittleness or scaling" is not stated in the text; adding it would add a claim, which this pass does not do.
