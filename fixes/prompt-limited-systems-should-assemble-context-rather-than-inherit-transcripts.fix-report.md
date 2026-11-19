## Fix Report: prompt-limited-systems-should-assemble-context-rather-than-inherit-transcripts

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | accessibility/notation-opacity | new-pattern: notation-to-prose | Replaced `select(K)` and bare `select` notation with "selection step" phrasing. | fixed |
| 2 | accessibility/undefined-terms | new-pattern: first-mention-gloss | Linked and glossed the first `distillation` mention as directed context compression. | fixed |
| 3 | prose/anthropomorphic-framing | new-pattern: agency-neutral-call-framing | Replaced "what the previous call already knew" with "what the previous call already resolved." | fixed |
| 4 | prose/pseudo-formalism | new-pattern: notation-to-prose | Replaced unnecessary formal notation with plain prose while keeping the bounded-context orchestration link. | fixed |

### Warning-to-fix mapping

- **#1 (accessibility/notation-opacity):** Review warned that lines using `select(K)` or `select` depended on notation from the linked model. The note now uses "selection step" and "future selection step" instead.
- **#2 (accessibility/undefined-terms):** Review warned that `distillation` appeared before its linked KB gloss. The first mention now links to the definition and includes "(directed context compression)."
- **#3 (prose/anthropomorphic-framing):** Review warned that a call does not literally "know." The sentence now says the next call reconstructs what the previous call already resolved.
- **#4 (prose/pseudo-formalism):** Review warned that `select(K)` made the prose more formal than necessary. The body and footer now describe the operation in prose.

### Deferred items

- None.

### New patterns

- `notation-to-prose`: Replace imported formal notation with plain-language operation names when the note uses the notation only as a label.
- `first-mention-gloss`: Add the definition link and short gloss at the first occurrence of KB vocabulary.
- `agency-neutral-call-framing`: Rephrase claims that attribute mental states to calls into claims about resolved information, available context, or produced artifacts.
