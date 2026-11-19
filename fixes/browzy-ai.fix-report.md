## Fix Report: browzy-ai

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Grounding | unsourced-addition | Reworded the session-digest claim so it says the digest becomes a markdown wiki article and only enters FTS through the normal indexing path. | fixed |
| 2 | Grounding | qualifier-dropped | Reworded the crystallizer claim to say at most one saved crystallized insight per session, with failed or NONE attempts eligible for later retries. | fixed |

### Warning-to-fix mapping
For each fix, quote or paraphrase the review warning that triggered it, so the fix can be audited against the original finding.

- **#1 (Grounding):** "The note says session digests are written as wiki articles so they enter FTS and become queryable, but the linked app logic does not immediately index them into FTS."
- **#2 (Grounding):** "The note says the crystallizer runs at most once per session, but the grounded claim should be 'at most one saved crystallized draft per session' or 'attempted after multi-source answers until one is saved.'"

### Deferred items
- (none)

### New patterns
- (none)
