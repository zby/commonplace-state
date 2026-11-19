## Fix Report: openviking

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Completeness boundary | boundary-case-acknowledged | Split URI scopes from stored/indexed content types and clarified that `session` is a scope, not a fourth content type | fixed |
| 2 | Grounding | new-pattern | Added a stable inspection basis with GitHub HEAD `37e106a958f4e427cfc922e32828f5c16d08c388` for the moving-repo claims | fixed |
| 3 | Internal consistency | hedge-own-framework | Unified the account/namespace/space vocabulary and clarified that candidate memories are proposed first, then promoted through dedup | fixed |

### Warning-to-fix mapping
- **#1 (Completeness boundary):** "The `Content types` row claims Resource / Memory / Skill as OpenViking's content taxonomy, but the note's own session-transcript section makes archived sessions a first-class context artifact that does not map cleanly into those three values."
- **#2 (Grounding):** "Precise empirical and implementation claims such as the post-March commit delta, LoCoMo numbers, and detailed codepath behavior are not anchored to a commit SHA, source snapshot, or linked artifact."
- **#3 (Internal consistency):** "The tenancy section says account namespaces can share sessions across users, then states that cross-user contamination is impossible by path construction. Those can both be true only if 'cross-user' means unauthorized cross-account/cross-space access."

### Deferred items
- (none)

### New patterns
- `inspection-basis-anchor`: add a stable commit or snapshot pointer when a note summarizes a moving upstream repository.
