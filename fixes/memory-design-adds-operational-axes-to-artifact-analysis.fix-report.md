## Fix Report: memory-design-adds-operational-axes-to-artifact-analysis

| # | Check | Strategy | Summary | Status |
|---|---|---|---|---|
| 1 | accessibility/undefined-terms | new-pattern: plain-first-framework-term | Replaced early "system-definition policy" / "homoiconic context" table wording with plain role examples. | fixed |
| 2 | accessibility/unidentified-references | single-source-vocabulary | Linked and identified the Rosebud LLM-memory essay inline on first body mention. | fixed |
| 3 | frontmatter/title-body-alignment | new-pattern: broaden-title-to-proven-claim | Renamed the note to "Memory design adds operational axes to artifact analysis." | fixed |
| 4 | prose/bridge-paragraph-duplication | new-pattern: compress-preview-bridge | Replaced the long preview paragraph with a one-sentence boundary transition. | fixed |
| 5 | semantic/load-bearing-qualifiers | new-pattern: broaden-title-to-proven-claim | Removed the unnecessary "lifecycle and activation" title qualifier in favor of the broader operational-axis claim. | fixed |
| 6 | sentence/clause-packing | new-pattern: split-list-sentence | Split the dense same-artifact comparison into a claim plus grouped examples. | fixed |
| 7 | sentence/clause-packing | new-pattern: split-list-sentence | Split the Rosebud source sentence into identification plus grouped operational choices. | fixed |
| 8 | sentence/parsing-ambiguity | new-pattern: split-list-sentence | Replaced repeated "one..." clauses with a direct list of operational differences. | fixed |

### Warning-to-fix mapping

- **#1 (accessibility/undefined-terms):** The review warned that the first role example used "system-definition policy" and "homoiconic context" before local explanation. The table now uses "Reference knowledge, behavior-shaping instruction, or both."
- **#2 (accessibility/unidentified-references):** The review warned that "The Rosebud memory essay" lacked inline identification. The body now links to and names the "Rosebud LLM-memory essay" on first mention.
- **#3 (frontmatter/title-body-alignment):** The review warned that "lifecycle and activation axes" undernamed the actual claim. The note was renamed to "Memory design adds operational axes to artifact analysis."
- **#4 (prose/bridge-paragraph-duplication):** The review warned that the bridge paragraph previewed the next section's axis list. The bridge is now one sentence: artifact axes stop at the artifact boundary; memory design needs policy axes for how retained material enters, changes, and leaves use.
- **#5 (semantic/load-bearing-qualifiers):** The review warned that the title's "lifecycle and activation" qualifier narrowed the argument unnecessarily. The same rename fixes the qualifier problem.
- **#6 (sentence/clause-packing):** The review warned that the same-artifact comparison chained too many independent differences. The passage now groups the point as operational differences in write policy, activation path, drift control, and forgetting propagation.
- **#7 (sentence/clause-packing):** The review warned that the Rosebud source sentence packed too many design choices into one sentence. The passage now splits source identification from grouped operational choices.
- **#8 (sentence/parsing-ambiguity):** The review warned that repeated "one..." clauses made the same-artifact comparison hard to parse. The revised sentence removes that construction.

### Deferred items

- None.

### New patterns

- **plain-first-framework-term:** When a table introduces a framework axis before the note has explained local vocabulary, use plain examples first and reserve project terms for later prose.
- **broaden-title-to-proven-claim:** When a review shows that a title qualifier is narrower than the argument's actual proof, rename to the broader supported claim.
- **compress-preview-bridge:** When a transition paragraph duplicates the next section's enumeration, replace it with a single sentence naming the boundary or relation.
- **split-list-sentence:** When a sentence carries a long chain of alternatives, split into a short claim plus grouped examples.
