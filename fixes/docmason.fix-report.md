## Fix Report: docmason

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | semantic/grounding-alignment | hedge-strength-mismatch | Narrowed the render-inspection claim to the provenance-trace workflow and moved commit-barrier enforcement to the constraints the code actually checks | fixed |

### Warning-to-fix mapping

- **#1 (semantic/grounding-alignment):** The review said the note claimed `admissibility.py` enforced render-inspection proof, but the code only supports the narrower tracing-and-inspection workflow plus other admissibility checks. I rewrote the sentence to match that boundary.

### Deferred items
- (none)

### New patterns
- (none)
