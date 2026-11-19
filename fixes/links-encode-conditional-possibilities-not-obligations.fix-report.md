## Fix Report: links-encode-conditional-possibilities-not-obligations

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Undefined terms | new-pattern | Added a first-use gloss for "reachable readers". | fixed |
| 2 | Unidentified references | new-pattern | Identified `CLAUDE.md` as the repo instruction file on first mention. | fixed |
| 3 | Compound bullet | new-pattern | Split the combined agent-path/human-optimised-link claim into two ordered-list items. | fixed |

### Warning-to-fix mapping

- **#1 (Undefined terms):** "Reachable readers" was used as an operative category without defining what makes a reader reachable.
- **#2 (Unidentified references):** `CLAUDE.md` was named without saying what kind of artifact it is or what role it plays.
- **#3 (Compound bullet):** `## Focus: optimise for agents`, item 3 combined the claim that agent-optimised links still serve humans with the inverse claim that human-optimised links over-serve agents.

### Deferred items

- None.

### New patterns

- **first-use-operative-term-gloss:** Add a brief local gloss when a review flags an operative term that is understandable but doing rule-level work.
- **first-use-artifact-identification:** Identify a named project artifact by role on first mention when readers outside the immediate project context may not know it.
- **split-compound-scan-item:** Split a list item when it carries two independently scannable claims.
