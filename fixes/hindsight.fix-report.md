## Fix Report: hindsight

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Completeness boundary cases | boundary-case-acknowledged | Scoped the policy-layer claim to reflect output behavior only | fixed |
| 2 | Grounding alignment | hedge-strength-mismatch | Separated distillation vocabulary from the trust claim and tied trust to the curation loop | fixed |
| 3 | Grounding alignment | unsourced-addition | Reframed PostgreSQL as less directly inspectable than markdown and made the symbolic-artifact wording relative rather than absolute | fixed |

### Warning-to-fix mapping
For each fix, quote or paraphrase the review warning that triggered it, so the fix can be audited against the original finding.

- **#1 (Completeness boundary cases):** “The ‘two-tier policy layer’ framing omits operation validators, auth/tenancy extensions, and middleware hooks...”
- **#2 (Grounding alignment):** “The `distillation` link is used to support the claim that ... curation point ... makes distillation trustworthy...”
- **#3 (Grounding alignment):** “The note says Hindsight’s production capabilities are ‘only possible because the substrate is opaque to humans’...”

### Deferred items
- (none)

### New patterns
- (none)
