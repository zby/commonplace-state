---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "On a small workload whose comparison-sufficient live state fits inside one usable window—or a separable workload whose opportunity cost reduces to a locally calibrated metric such as a dollar cap or latency budget—the conflict disappears or can be handled by injected thresholds."
    reason: "Packs two independent scope exclusions—a small workload fitting in one window (where the conflict disappears) and a separable workload with a locally calibrated metric (where injected thresholds handle it)—into one 43-word bullet via em-dashes, burying the second exclusion during scanning."
    level: warn
  - scope: passage
    quotes:
      - "How much compressed global state (active bottlenecks, tolerances, budgets) can be injected into a focused worker's handoff—and what makes such signals locally calibratable—before context load degrades task solving?"
    reason: "Combines two independent open questions—the context-budget ceiling for injecting compressed global state and the design property that makes such signals locally calibratable—by interrupting the first question with an em-dash clause."
    level: warn
outcome: warn
---

# Review

Most longer bullets in the note develop a single failure mode, architectural role, mechanism, or friction point with supporting elaboration and examples. Two bullets in the closing sections instead merge two separable points with em-dashes—one bundling two distinct scope exclusions with separate consequents, and one wedging a second open question inside the syntax of another. Splitting each into standalone bullets would keep both points visible during scanning.
