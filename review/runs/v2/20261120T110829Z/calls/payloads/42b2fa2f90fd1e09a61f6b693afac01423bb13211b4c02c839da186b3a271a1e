---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Enforcing input schemas strictly at the call boundary while the implementation is still a prompt prevents callers from accumulating this hidden coupling."
    reason: "The coupling just described includes 'loosely phrased, slightly malformed, or context-dependent arguments'. Reading A: strict schema enforcement prevents all of it, so the recommendation is sufficient for safe prompt-to-code swaps. Reading B: schemas catch only structural malformation, while loosely phrased or context-dependent arguments that are schema-valid, such as free-text fields, still rely on the prompt's inference. Under B the coupling is only reduced. The unresolved choice is scope: which kinds of tolerance a schema can enforce. It decides whether the 'practical consequence' recommendation is sufficient or partial, and whether callers still need testing after codification."
    level: warn
  - scope: passage
    quotes:
      - "the programmer changes the implementation, not the rule"
    reason: "'The rule' may mean the topic-based routing regularity the team extracted, preserved on the cases the agent already handled consistently. It may also mean the full behavior of the prompt, including its handling of ambiguous tickets. The choice affects whether calling the move 'behavior-preserving' needs equivalence testing. The Scope section's distinction between call invariance and behavioral invariance partly resolves it, so this finding is INFO."
    level: info
outcome: warn
---

# Review

## Summary

Most load-bearing assertions are specific. The llm-do mechanism, the code-to-prompt leak with its named latency, cost, determinism and failure-mode dimensions, and the Scope boundaries all identify their mechanism and consequence.

The schema recommendation leaves its scope unresolved, and the difference is material (WARN). The sentence asserts prevention. Yet the coupling it is meant to prevent includes semantic tolerance that a schema may not express. The reader cannot tell whether schema enforcement is the complete safeguard or only a partial one.

"Changes the implementation, not the rule" leaves open what counts as the rule (INFO). Nearby context mitigates this.
