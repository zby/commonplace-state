## Fix Report: mempalace

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Grounding alignment | scope-narrowed | Recast the stop-hook and diary paths as host-agent-mediated capture instead of automatic session mining | fixed |
| 2 | Internal consistency | scope-narrowed | Split the trace paragraph so the no-oracle claim applies only to miner/convo-miner paths | fixed |

### Warning-to-fix mapping
For each fix, quote or paraphrase the review warning that triggered it, so the fix can be audited against the original finding.

- **#1 (Grounding alignment):** “The stop-hook and diary paths ‘mine the current session,’ but the hook implementation ... supports ‘host-agent-mediated session capture’...”
- **#2 (Internal consistency):** “The stop hook asks the AI to write structured decisions/quotes/code into the palace ... This is resolvable if the latter is narrowed to the miner/convo-miner path.”

### Deferred items
- (none)

### New patterns
- (none)
