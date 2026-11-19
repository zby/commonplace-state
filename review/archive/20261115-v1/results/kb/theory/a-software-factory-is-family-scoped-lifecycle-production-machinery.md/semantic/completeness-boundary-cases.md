---
note: kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
note-sha256: cfa2051f5e127998e74593ee355a13d62a871d1cfb2b3ad2416e0a8b8111ea22
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
criterion-sha256: c18370ae5ecffb6d5e1c129d4ddf44123ef1d7287ce60811d8f53542f7c17c0e
outcome: pass
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: 4195a7d58c58448db208342ff7597a93
completed-at: '2026-11-12T08:30:12Z'
---
### Summary

The frameworks cover their stated historical scope without a missing boundary category. The note distinguishes reusable family machinery from product state by target and intended reuse, preserves differences between the 2003 and 2007 accounts, and explicitly limits the operation list rather than presenting it as a formal calculus. Grounding checks used the linked 2007 ingest and the linked software-factory and factory-development definitions.

### Findings

- INFO: The versioned ontology and distributed-knowledge list handle five boundary cases: an uninstalled template is packaged machinery rather than a configured factory; a configured family environment is the factory; a schema or generator alone is a constituent; a reusable test prototype is an asset while its product-specific completion is member state; and a generated factory can be a member relative to its producer. The categories describe related roles and containment, so their overlap does not require mutually exclusive additional categories. The list explicitly includes other implementation assets and does not claim an exhaustive inventory.
- INFO: The two-process framework handles five boundary cases by its stated target and reuse criterion: initial construction of reusable machinery is factory development; binding one anticipated variant is solution development; changing a configured schema for one member remains solution development; promoting a discovered repair into a reusable test or rule is factory development; and one failed test can motivate work in both processes. A person performing both roles does not invalidate a distinction between processes. The note expressly covers that shared observation without conflating the resulting changes.
- INFO: The operation list handles five boundary cases: ordinary member generation, member-specific viewpoint changes, reusable viewpoint specialization, composition of product outputs, and composition of factory production structures. A feedback-driven reusable viewpoint change may be both specialization and revision; the list does not claim exclusivity, and its explicit statement that combination rules are unspecified prevents an unsupported completeness claim. Producing another factory is also explicitly distinguished from revising the producer.
- INFO: The lifecycle and inference limits handle four boundary cases: requirements or tests without generated code remain lifecycle work products; deployed realizations remain product state; a factory supplying only a portion of a deliverable is compatible with the stated optional lifecycle support and product composition; and human-directed feedback revision establishes neither autonomous learning nor computational acquisition of family knowledge. The wording “may supply” does not require every factory to implement every listed lifecycle stage. These boundaries do not justify expanding the already substantial taxonomy.

## Result: PASS
