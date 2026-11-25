---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A bounded empirical illustration of a base-model floor appears in"
      - "Even within one benchmark and loop, an inadequate base model can block outer-loop learning before the store itself saturates"
    reason: "Evidential use of an unquoted ingest whose link text lacks the `(snapshot required)` marker. The ingest's `## Quotes` section states 'No source quotes have been retained yet', so no retained source material supports the claims that the three weakest models produced no held-out gains under the same loop that improved stronger models, or that a base model blocks learning 'before the store itself saturates'. Ingest analysis elsewhere does not count as support."
    level: fail
  - scope: passage
    quotes:
      - "recording which artifacts loaded during a run, annotating telemetry coverage gaps, replaying past cases, and running targeted ablations or bisects"
    reason: "The harness-offload list is introduced as following scheduler–LLM separation, and the footer says that note grounds why 'bookkeeping, replay, and enforceable checks belong in harness code'. The target argues for code maintaining explicit workflow state and enforcing sufficiently specified transitions (task records, counters, result identities, completion state). It does not discuss replay, telemetry coverage annotation, ablations, bisects, staleness tracking or failure-rate flagging. The transfer from bookkeeping and defined transitions to these evidence-capture and store-maintenance jobs is plausible but not articulated."
    level: warn
  - scope: passage
    quotes:
      - "turn an unanticipated failure and its trace into a causal diagnosis"
    reason: "The inline diagnostic-richness link sits on competence 2, a proposer capability. The target explicitly isolates evidence surfaces and says proposer capability is separate from them. The footer's 'extends: how the harness's evidence interface interacts with competence 2' represents it accurately, so the inline placement is only a mild over-reach."
    level: info
  - scope: passage
    quotes:
      - "recognize when an existing check is misleading"
    reason: "The on-balance judgment note covers tracing rival remedies against misleading directions in a design and comparing genuine trade-offs; it does not directly address recognizing that an existing check (validator, gate) misleads. The extension is plausible and non-load-bearing."
    level: info
outcome: fail
---

# Review

## Summary

Most linked library notes are represented at roughly their own scope. Semantic-work relocation supports the claim that harness offloading leaves semantic work in place. Operative change, single- and double-loop learning, and selection-based learning are used as definitions. The note's only empirical support comes from the Harness Evolution ingest, which has retained no quotes. Under this gate's rule, an evidential use of an unquoted ingest without retained extracts fails. The note does bound the illustration to one benchmark and loop, but that bound does not supply the missing source support.

The scheduler–LLM separation route is the second weakest. That note grounds code-enforced bookkeeping and state transitions. The note stretches it to cover replay, ablation, bisects and store hygiene without saying why the error-correction asymmetry carries over to those jobs.
