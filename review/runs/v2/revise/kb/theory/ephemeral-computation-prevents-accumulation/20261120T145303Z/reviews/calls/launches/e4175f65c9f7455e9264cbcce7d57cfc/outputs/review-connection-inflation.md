---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "- [Codification](./definitions/codification.md) — contrasts: execution form is separate from artifact lifetime"
    reason: "The body already links to ./definitions/codification.md inside a section titled 'Retention and codification are different choices' that defines codification as execution form and explicitly contrasts it with retention; the footer entry repeats the same link and framing without adding new navigational context."
    level: warn
  - scope: passage
    quotes:
      - "- [The Flawed Ephemeral Software Hypothesis](https://www.blackhc.net/essays/future_of_software/) — evidenced-by: supplies the production-knowledge pressures motivating durable carriers"
    reason: "The body already links to https://www.blackhc.net/essays/future_of_software/ and articulates the exact same evidential relationship and framing—that Kirsch's critique identifies production knowledge that must survive replacement and motivates retaining that knowledge—so the footer entry adds no navigational value beyond the body."
    level: warn
outcome: warn
---

# Review

Three of the five Relevant Notes entries add navigational value: the two entries for *Retained system-definition artifacts enable persistent deployment-time adaptation* and *Discarding software requires preserving the operational knowledge later work needs* do not appear in the body at all, and the entry for *The deployed system, not the model alone, is the unit of learning* supplies the target's full claim and explicit `grounds` relationship that are absent from the body's brief inline `[deployed system]` link.

The remaining two entries—for *Codification* and *The Flawed Ephemeral Software Hypothesis*—fail both checks of the gate because the body already links to each target and explicitly spells out the same contrast or evidential framing that the footer restates.
