## Fix Report: decomposition-heuristics-for-bounded-context-scheduling

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Notation opacity / pseudo-formalism | new-pattern | Replaced the formal-looking optimization statement and undefined `M` bound with plain prose about effective per-call context budget. | fixed |
| 2 | Undefined terms | new-pattern | Added inline glosses for clean frames, hard-oracle tasks, soft-oracle tasks, and distillation. | fixed |
| 3 | Unidentified references | new-pattern | Identified ConvexBench as a benchmark for convex symbolic expressions and MAKER as a maximal-decomposition agent system on first mention. | fixed |
| 4 | Connection inflation | new-pattern | Removed two footer links whose navigational value duplicated inline opening links. | fixed |
| 5 | Grounding alignment / internal consistency | hedge-strength-mismatch | Replaced the inaccurate "first two" empirical-grounding statement with a more exact status map naming the supported heuristics and the conjectural remainder. | fixed |
| 6 | Clause packing | new-pattern | Split dense empirical-grounding sentences for ConvexBench and MAKER into shorter claim, mechanism, and caveat sentences. | fixed |
| 7 | Bullet capitalization | new-pattern | Capitalized the objective-term and trade-off bullet starts. | fixed |
| 8 | Flow / cohesion | sentence-unpacking | Reworked the opening and empirical-grounding transitions so the note reads as a scheduling argument rather than a sequence of review-warning patches. | fixed |

### Deferred items
- None.

### New patterns
- **plain-language-substitution:** Replace formal-looking notation or optimization wording with direct prose when the note does not operationalize the symbol.
- **inline-gloss:** Add a short parenthetical or appositive when a KB term, benchmark, system, or source name is load-bearing but not locally identified.
- **connection-pruning:** Remove footer links that duplicate already-linked body claims without adding navigational context.
- **sentence-unpacking:** Split empirical sentences that combine the result, mechanism, comparison, and caveat into separate sentences.
- **structural-normalization:** Apply mechanical formatting fixes such as bullet capitalization without changing the argument.
