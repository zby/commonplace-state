---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Conversely, keeping the old files does not preserve the capability if the successor no longer permits or consumes their changes."
    reason: "This sentence is in the general section on non-regression, but 'old files' comes from the hypothetical agent's file-based instructions. Outside the example, the general point is that keeping the old components or artifacts does not preserve the capability. The residue is mild because the preceding paragraph ties it back to the example."
    level: info
  - scope: passage
    quotes:
      - "A maintainer may restore a path that the agent itself no longer has."
    reason: "The Scope list states general limits for 'a system', but this bullet uses the example's 'agent'. 'The system itself' would match the opening's claimed generality. This is minor because agent systems are the KB's primary domain."
    level: info
outcome: pass
---

# Review

The title and opening state the claim for any system that improves itself: "A system can improve at its current work while losing the ability to improve itself again." The agent-specific vocabulary (instruction changes, files, maintainer) is introduced inside an example that is explicitly marked "Consider a hypothetical agent", so most of it is framed correctly.

Two phrases carry the example's vocabulary into general statements, as recorded in the findings. Neither commits the claim to file-based agents. Each one reads as a loose reference back to the example, so both are INFO.
