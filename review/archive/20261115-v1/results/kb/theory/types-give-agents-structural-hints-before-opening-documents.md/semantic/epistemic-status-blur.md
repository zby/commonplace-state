---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: 6c7d294d28b56d86ad38e9bc0ab4c3df40681be79745c798c3cc500862c27cbe
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
criterion-sha256: d8e3b463686cd2d7e0227e613a137fde6bb17c364e3317d995f2d082ac538f5a
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

The note is a short design argument. Premises about agents (stateless, finite context) lead to a derived consequence: pre-open metadata enables informed routing. Two supporting claims are delegated to linked notes (verifiability, enforcement). It reports no observations, so no evidence can spread onto a mechanism it does not support. Most claims read as consequences of the stated premises, which is their actual status. One capability claim reads more like an observed result than a derived expectation, but the derivation it rests on is visible in the same paragraph.

### Findings

- INFO: "Together they let an agent narrow from hundreds of files to the few it needs without opening any of them." This reads as an established capability, but no observation of agents doing this is presented. It is recoverable as a consequence of the preceding premises: types say what kind of document something is, and descriptions discriminate instances. However, "without opening any of them" depends on an unstated assumption that descriptions are discriminating enough. The linked enforcement note treats that as a judgment-level check that the type system does not guarantee. The status is recoverable with effort; it is not misrepresented.
- INFO: "Without types, an agent must either load everything (wasteful) or guess what's relevant (error-prone)." This dichotomy is presented as a plain fact, but it is a derived claim from the stated premises. Readers can recover this from its position as the opening premise of the argument.

## Result: PASS
