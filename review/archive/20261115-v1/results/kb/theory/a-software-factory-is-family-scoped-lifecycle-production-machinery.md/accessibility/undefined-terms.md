---
note: kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
note-sha256: cfa2051f5e127998e74593ee355a13d62a871d1cfb2b3ad2416e0a8b8111ea22
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: 3224c054f701239072486cdd66ab3929406feab114650468b44740091b4c875f
outcome: warn
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: e27202169d104ad691f645df90876be2
completed-at: '2026-11-12T08:28:01Z'
---
### Summary

The note explains its central factory, schema, template, and development-role distinctions in the text. A few supporting terms still assume familiarity with software product-line terminology or lifecycle documentation.

### Findings

- WARN: “Product-specific lifecycle work products” first appears in the introductory process comparison without a concrete gloss. It is central to the distinction between reusable factory machinery and a member’s state, but readers only receive examples much later under “The factory spans the lifecycle.” Briefly identify these as artifacts produced or maintained during a product’s life, such as requirements, code, tests, and deployment configurations.
- WARN: The family row introduces “variation points,” and the solution-development table later says “Select and bind anticipated variation,” without explaining the underlying operation. The surrounding references to features and variants suggest differences between products, but do not explain that variation points are designated choices and binding resolves those choices for one product.

### Suggested Revision

At the introductory occurrence, write “product-specific lifecycle work products—the requirements, code, tests, deployment configurations, and other artifacts produced or maintained during a product’s life.” In the family row, gloss “variation points” as “designated choices where family members may differ.” Replace “Select and bind anticipated variation” with “Choose among supported alternatives and fix those choices for the individual solution.”

## Result: WARN
