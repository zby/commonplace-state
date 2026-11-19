---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: 6c7d294d28b56d86ad38e9bc0ab4c3df40681be79745c798c3cc500862c27cbe
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
criterion-sha256: 6fcc053826e6a769a4719412e2bb719863b59037bc0ae2c1b4e891402a88019a
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: fda83731e2314289ae9e403555a60d57
completed-at: '2026-11-12T09:59:11Z'
---
### Summary

The central claim's vocabulary sits at the level the argument uses. "Types" means the KB's document types, and the examples are concrete types (`spec`, `structured-claim`, `index`). "Agents" means LLM agents with stateless sessions and finite context, which are the premises the argument uses. "Documents" covers notes, specs and indexes, which the examples span, so downgrading to "notes" would drop the `spec` and `index` illustrations. "Structural hints" is the one abstraction. The verifiability paragraph earns it: it names what the abstraction forbids (subject-matter labels such as "design note").

### Findings

- INFO: Forbids test on "structural hints". The abstract wording rules out subject-matter typing as a routing aid, and the concrete examples alone would not rule it out. This is an earned abstraction. Abstraction is concentrated in this one load-bearing site rather than spread across the prose.

## Result: PASS
