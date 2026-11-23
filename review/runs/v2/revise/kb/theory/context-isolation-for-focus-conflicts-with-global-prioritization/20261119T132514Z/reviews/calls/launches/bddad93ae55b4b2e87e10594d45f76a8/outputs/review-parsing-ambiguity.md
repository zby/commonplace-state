---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "separates noticing a defect during reading from prioritizing and fixing it by emitting a one-line log entry for a later pass"
    reason: "'by emitting a one-line log entry' is meant to attach to 'separates', but it sits directly after 'fixing it', so a first pass reads 'fixing it by emitting a log entry'. Context corrects this quickly because emitting a log entry is not a fix. Fronting the means ('by emitting a one-line log entry for a later pass, separates noticing ... from prioritizing and fixing it') removes the garden path."
    level: info
  - scope: passage
    quotes:
      - "whose isolated task workers reliably make decisions whose right answer depends on unseen competing work—or that loads full live portfolio state"
    reason: "'or that loads' is meant to coordinate with the first relative clause on 'A system'. Because it follows a nested 'decisions whose right answer depends on ...', a reader can briefly try to attach it to 'decisions' or to 'competing work'. The verb 'loads' and the dashes make the intended attachment recoverable, so this is minor."
    level: info
outcome: pass
---

# Review

Negation scope is handled cleanly throughout. Examples are "does not by itself explain why the worker acts as if that priority is high", "does not resolve this conflict" and "it does not choose or revise objectives". Pronouns have clear antecedents, including "them" in the frontier bullet and "it" in the triage and residual-friction sections. Two modifier attachments can briefly misparse on a first read. Both resolve from context, so neither rises to a warning.
