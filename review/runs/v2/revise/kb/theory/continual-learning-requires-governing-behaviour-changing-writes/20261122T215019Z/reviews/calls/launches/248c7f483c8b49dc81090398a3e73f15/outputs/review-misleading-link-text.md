---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "because continual adaptation compounds silent degradation (see [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md))"
    reason: "The sentence cites the target as support for the claim that continual adaptation compounds silent degradation. The target is about moving workflow bookkeeping (task records, dependencies, completion state) into code because code enforces defined transitions while semantic judgments need fallible verification. It does not discuss continual adaptation, compounding, regression, or silent degradation. A reader following the link will not find the cited claim; at most the target supports why symbolic changes are cheaper to check, which is what the footer annotation says."
    level: warn
  - scope: passage
    quotes:
      - "[Only explicit retention is durable, writable, and addressable](./only-explicit-retention-is-durable-writable-and-addressable.md)"
    reason: "The link text asserts an exclusive claim that the target no longer makes. The target is titled 'Explicit retention provides direct targets for selective revision', and its description says durability, writability, and effective addressability still depend on the boundary and available operations. The annotation 'the form-level trade space this note defers to' also conflicts with the body, which defers the trade space to the representational-form coevolution note. Update the link text to the current title."
    level: warn
  - scope: passage
    quotes:
      - "[Constraining during deployment is continual learning](./constraining-during-deployment-can-produce-learning-outside-weights.md)"
    reason: "The link text states an unqualified identity; the target is titled 'Constraining during deployment can produce learning outside weights' and says retention alone does not establish a gain in adaptive capacity. The reader who does not follow the link gets a stronger claim than the target supports. Use the current title."
    level: warn
outcome: warn
---

# Review

## Summary

All links resolve, including the `#what-addressability-does-not-buy` anchor in Reflection buys addressability. Body links to the learning, behavioral-authority, knowledge-artifact, system-definition-artifact, representational-form, deployment-time-learning, coevolution, codification-and-relaxing, selection-based-learning, proposal-selection-loop and contextual-activation targets match what their link text and sentences lead the reader to expect. Footer links whose text is a shortened title (First-principles reasoning, Verifiability gradient) are fine.

Three links mislead. The inline Scheduler-LLM citation is offered as evidence for a claim (compounding silent degradation under continual adaptation) that the target does not discuss. Two footer link texts carry stale titles that state stronger or exclusive claims than their targets now make.
