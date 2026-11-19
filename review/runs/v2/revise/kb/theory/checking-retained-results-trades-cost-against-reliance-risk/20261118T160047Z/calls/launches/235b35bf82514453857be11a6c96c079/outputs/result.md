---
type: types/edit-result.md
outcome: changed
changes:
  - "new-pattern (a link whose text is a full clause serves as the subject of a reduced relative clause, causing a garden-path parse): first paragraph, 'This is the saving [frontloading spares execution context] argues for results computed before an LLM call, extended here to persisted artifacts.' became 'The note [frontloading spares execution context] argues for this saving in the case of results computed before an LLM call; this note extends the argument to persisted artifacts.'"
removed-links: []
---

# Report

- `new-pattern` — a link whose text is a whole clause acts as the subject of an unmarked relative clause, so the following verb attaches to the wrong noun. Passage: "This is the saving [frontloading spares execution context](./frontloading-spares-execution-context.md) argues for results computed before an LLM call, extended here to persisted artifacts." Change: gave the link a noun head ("The note …"), made "this saving" the explicit object of "argues for", marked the case with "in the case of", and split the extension into its own clause ("this note extends the argument to persisted artifacts"). The link target, the claim and the extension are unchanged.

Findings not touched:

- Finding 2 (INFO, "A check that fully recomputes the result on every use largely defeats it"): outside the supplied scope, which is limited to the sentence containing the frontloading link. The antecedent of "it" remains "that saving" in the preceding sentence.
