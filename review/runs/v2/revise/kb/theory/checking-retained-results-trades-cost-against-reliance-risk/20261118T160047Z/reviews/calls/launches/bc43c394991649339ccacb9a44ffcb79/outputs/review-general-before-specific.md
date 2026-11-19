---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A mechanical check derives a retained result from, or compares it against, identified available inputs."
    reason: "The general conditions for a mechanical check come after the completeness-mark section, which is the main instance of them (\"The mark's contract supplies the first three\"). The two sections are not adjacent, so the gate's adjacent-pair test does not flag them. Moving the conditions earlier would also split them from the two cases they are derived from, so the current order is defensible."
    level: info
outcome: pass
---

# Review

The opening section states the general trade-off before any case: retaining a result saves work, checking spends some of that saving, and how often to check depends on check cost relative to reliance risk. The two case sections, on the completeness mark and the connect report, then show how that trade-off plays out differently.

Adjacent pairs:

- Intro → completeness mark: general before specific.
- Completeness mark → connect report: two parallel cases.
- Connect report → "No known change does not establish freshness": the freshness section draws a conclusion from both cases. It is not a rule that the connect-report section is an instance of, so the order is not inverted.
- Freshness → "What a mechanical check requires": neither section is a specific case of the other.

No adjacent pair puts a specific case before the general rule it exemplifies. The one INFO finding notes a non-adjacent ordering: the mechanical-check conditions generalize the completeness-mark example but appear later in the note.
