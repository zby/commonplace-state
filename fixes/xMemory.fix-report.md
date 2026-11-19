## Fix Report: xMemory

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Completeness boundary cases | boundary-case-acknowledged | Recast xMemory as adjacent to service-owned trace backends rather than a clean instance of that category | fixed |
| 2 | Grounding alignment | scope-narrowed | Reframed the survey-table reference as a new four-layer-ladder example and downgraded it to a benchmark-harness boundary case | fixed |
| 3 | Internal consistency | new-pattern | Separated retrieval resolutions from derived content artifacts so the ladder and export graph no longer share one list | fixed |

### Warning-to-fix mapping
For each fix, quote or paraphrase the review warning that triggered it, so the fix can be audited against the original finding.

- **#1 (Completeness boundary cases):** "The `service-owned trace backend` classification is strained."
- **#2 (Grounding alignment):** "The linked survey does not mention xMemory, `four-layer`, or `ladder`."
- **#3 (Internal consistency):** "The note first defines the four-level hierarchy and retrieval ladder as raw messages -> episode summaries -> semantic facts -> LLM-summarized themes."

### Deferred items
- (none)

### New patterns
- **new-pattern:** split retrieval-resolution terminology from persisted artifact terminology in hierarchy descriptions
