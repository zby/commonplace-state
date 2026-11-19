### Summary

The note's five short paragraphs do not directly contradict one another. One term drifts: "structural hints" first means type-provided hints about document structure. The final paragraph then makes the hints depend on descriptions, which the note itself classes as instance filters rather than structural properties. A smaller tension sits between the opening dichotomy and the credit given to descriptions.

### Findings

- INFO: Definition drift in "structural hints". Paragraph 2 introduces structural hints as what types give ("A `spec` tells an agent it can implement from this"). Paragraph 4 sharpens this: types "must assert structural properties, not subject matter". Paragraph 5 says "these structural hints only work if the metadata exists reliably" and goes on to discuss descriptions only. Descriptions, per paragraph 3, tell the agent "which instance" — they are subject-matter discriminators, not structural properties. A reader cannot tell whether "structural hints" covers descriptions or only types. A human should confirm which is meant.
- INFO: Tension between the opening and paragraph 3. The opening says "Without types, an agent must either load everything ... or guess". Paragraph 3 calls the description "the most important field" and gives it the work of narrowing "from hundreds of files to the few it needs". Taken together, an agent with descriptions but without types would not be forced into the dichotomy. Paragraph 5 partly reconciles this by saying the type system is what makes descriptions exist. The reconciliation is implicit, though, and the title still credits types with the hints.
- INFO: The description frontmatter says "the type says what operations a document affords". Paragraph 3 says "the type tells the agent *what kind of thing* a document is". Paragraph 2 links the two through examples, so this is compression rather than drift.

## Result: PASS
