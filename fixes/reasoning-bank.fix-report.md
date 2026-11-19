## Fix Report: reasoning-bank

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | semantic/internal-consistency | new-pattern: retrieval-target-split | Clarified that prior task queries are the relevance target, while the current query is still appended to the cache and therefore participates in the similarity pool | fixed |

### Warning-to-fix mapping

- **#1 (semantic/internal-consistency):** The review said the retrieval paragraph and cache paragraph left it ambiguous whether similarity was over prior-only queries or prior-plus-current rows. I made the target-vs-cache distinction explicit in the retrieval paragraph and shortened the cache paragraph to match.

### Deferred items
- (none)

### New patterns
- **retrieval-target-split:** A retrieval description needs to separate the thing being ranked for relevance from the broader cache or candidate pool that the implementation still includes. Fix by stating both explicitly and naming which one actually feeds injection.
