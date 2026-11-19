---
note: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
note-sha256: 33ea153382746c3a6b92a7db4778b72bb1e524759e54c7c5c600faad6bf287f7
criterion: kb/instructions/review-gates/semantic/unwarranted-scope.md
criterion-sha256: 31cdbc14651bb88c165bd9600bc1f6b8c52f66677d88d7035e82056942940f2c
outcome: warn
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: 3f2ae03f3ebf4a3e8020bc9889ec722a
completed-at: '2026-11-12T08:26:00Z'
---
### Summary

The note explains why a KB that manages work in progress needs lifecycle support beyond durable artifact contracts. Its central claim extends that need to every functioning knowledge base, without arguing why functioning requires managing such work or marking that broader necessity as conjectural.

### Findings

- WARN: The title, “A functioning knowledge base needs a workshop layer,” and the opening assertion that “a functioning knowledge base also needs to support work in motion” invite reliance across functioning KBs generally. The presented support covers tasks and other processes with changing states, dependencies, expiry, and outputs that may become durable knowledge. That argument articulates why those processes need workshop support, but does not establish that every functioning KB must host or manage them. The later qualification, “when we want to build a knowledge base that supports real workflows,” identifies the domain the argument exercises; it does not limit the headline or explain transfer to KBs serving durable knowledge alone. The Scope section addresses hybrid documents, while the Open questions section concerns workshop design; neither marks the surplus necessity claim as conjectural.

### Suggested Revision

Qualify the central claim and opening to KBs that manage work in progress, or explicitly mark the broader claim that every functioning KB needs this capability as a conjecture. Preserve the existing lifecycle argument as support for the conditional claim.

## Result: WARN
