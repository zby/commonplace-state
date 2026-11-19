## Fix Report: napkin

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Grounding alignment | hedge-strength-mismatch | Reframed the distill path as weakly governed distillation instead of implying it falls outside the definition | fixed |
| 2 | Internal consistency | qualifier-dropped | Restored the “described as zero preprocessing” qualifier so the later critique can stand | fixed |

### Warning-to-fix mapping
For each fix, quote or paraphrase the review warning that triggered it, so the fix can be audited against the original finding.

- **#1 (Grounding alignment):** “Napkin's distill extension ... plausibly fits [distillation] ... The critique should target missing verification, deduplication, and measurement...”
- **#2 (Internal consistency):** “The Core Ideas section presents the LongMemEval numbers as achieved with ‘zero preprocessing,’ while the Curiosity Pass later says the benchmark setup preprocesses the haystack...”

### Deferred items
- (none)

### New patterns
- (none)
