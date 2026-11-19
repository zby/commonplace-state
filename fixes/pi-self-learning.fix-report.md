## Fix Report: pi-self-learning

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Completeness boundary | boundary-case-acknowledged | Qualified the hierarchy as git-backed by default only when git integration is enabled | fixed |
| 2 | Grounding | hedge-strength-mismatch | Recast monthly summaries as manual, removed unsupported scheduler language, and dropped the JSONL-style label for `index.json` | fixed |
| 3 | Internal consistency | hedge-own-framework | Reserved `trigger` for automatic capture and treated `/learning-now` / `/learning-month` as manual maintenance commands | fixed |

### Warning-to-fix mapping
- **#1 (Completeness boundary):** "The `git.enabled=false` boundary case means the hierarchy still exists, but it is no longer git-backed; auto-commit also depends on `git.autoCommit=true`."
- **#2 (Grounding):** "The source exposes `/learning-month [YYYY-MM]` and `generateMonthSummary(...)`, but no scheduler or cron-like trigger appears; the `all git-backed` phrasing also overreaches relative to source configuration."
- **#3 (Internal consistency):** "`Automatic task-end reflection as the sole learning trigger` conflicts with the later trace-derived placement, which says triggers include per-task `agent_end`, manual `/learning-now`, and `/learning-month`."

### Deferred items
- (none)

### New patterns
- (none)
