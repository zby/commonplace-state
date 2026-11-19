---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "This note uses \"test record\" where it earlier used \"warrant\". \"Warrant\" covered both truth and support, and the first two questions need to be kept apart."
    reason: "This paragraph records the note's own revision history. A reader without the earlier version gains nothing from it, and the reason it gives (truth and support must be kept apart) is the job of the next section, \"A test record is not truth\". Deleting it breaks no step of the argument. Change history belongs in commits. If readers arriving from older notes that say \"warrant\" need a bridge, a short clause in the test-record bullet would cost less than a standalone paragraph."
    level: warn
  - scope: passage
    quotes:
      - "It is not a guarantee that later tests will go the same way."
    reason: "The paragraph opens by saying that a claim which has survived every test so far is still a conjecture. The closing sentence restates that admission and adds nothing to it. The preceding sentence (\"the best available reason to rely on a claim\") does the new work. Cut the trailing sentence."
    level: warn
  - scope: passage
    quotes:
      - "So use of a claim inside the theory can be a test, and often it is not. What decides is whether the use could have gone against the claim, not where the evidence was produced."
    reason: "The preceding sentence already states the deciding condition: agreement counts only \"where the agreement was an outcome the claim could have failed\". Section 4 states it a third time (\"unless the help was a test it could have failed\"). The one new contrast here is \"not where the evidence was produced\", meaning that being inside the theory does not by itself disqualify evidence. Fold that phrase into the previous paragraph and drop the rest of this one."
    level: warn
  - scope: passage
    quotes:
      - "Fit has no single scale. Relevance, redundancy, scope, level of abstraction, agreement with other claims and usefulness in operation weigh differently in different working theories."
    reason: "The new point is that fit has no single scale and its components weigh differently. The enumeration repeats the definition of fit in the opening list and the failure kinds in the section \"A good test record does not make a claim fit\". The list may help as a nearby reminder, but it could probably shrink to \"its components\" with little loss. Uncertain whether the reminder is doing necessary reader work."
    level: info
outcome: warn
---

# Review

The note's core structure earns its space. The opening defines three questions. Three sections each separate one pair. A section on how the two kinds of evidence interact follows, then one on contradiction repair. Most restatements serve as section-closing stances. For example, "The claim's test record does not make that decision" and the paired slogans in "Neither may be substituted for the other" turn the mechanism into memorable decision rules. They are not flagged.

The warnings are about recap and history, not the argument:

- The "warrant" paragraph is revision history inside the note.
- One closing sentence repeats its paragraph's opening admission.
- The paragraph after the §82 citation restates the could-have-failed condition that the sentence before it just stated. Only its "not where the evidence was produced" contrast is new.

Two Scope bullets are not flagged. The bullet on objectives, commitments and authority adds a boundary the body does not draw. The "separate, not statistically independent" bullet prevents a likely misreading of "no answer to one settles another".
