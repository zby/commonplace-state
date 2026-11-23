---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "cross-run accumulation fails only when no experience-dependent state survives to affect later work"
    reason: "The causal-isolation derivation in 'What must survive' exercises only necessity (absent surviving experience-dependent state prevents cross-run behavioral change, and discarding one artifact leaves learning possible); it does not exercise cases where experience-dependent state survives and causally affects later runs yet fails to yield accumulation (such as stale, erroneous, or harmful state), and neither a transfer relation nor a conjecture marking covers that surplus sufficiency scope."
    level: warn
  - scope: passage
    quotes:
      - "A retained natural-language procedure accumulates knowledge without becoming executable code."
    reason: "Supporting claim that overreaches slightly beyond the exercised support, since retention alone does not establish accumulation without later causal use."
    level: info
outcome: warn
---

# Review

The title claim (`Discarding all experience-dependent state prevents cross-run accumulation`) and the opening boundary argument match the exercised domain of the causal-isolation derivation under the explicit assumptions stated in `## Scope`. However, the frontmatter description extends past that necessity derivation by stating that cross-run accumulation fails *only when* no experience-dependent state survives to affect later work, inviting reliance over cases of surviving causal state that the note's support does not exercise.
