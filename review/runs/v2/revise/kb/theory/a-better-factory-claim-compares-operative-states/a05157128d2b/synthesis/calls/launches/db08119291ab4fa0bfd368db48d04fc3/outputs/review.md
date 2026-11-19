---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The note states the same two boundaries in several places. It says four times that a declared comparison need not track real factory quality: in the opening paragraph, at the end of the assessment-relation section, and in the first two Scope bullets. It separates adoption control from the comparison three times: in the relata section, at the end of the improvement section, and in the fifth Scope bullet. A reader cannot tell whether each repetition adds a new limit, so the Scope section reads mostly as restatement and its two genuinely new bullets (retrospective criteria; a relation that permits retirement) are diluted. Direction: state each boundary once. Keep one plain quality-tracking caveat (in the opening or in Scope) and one adoption-versus-judgment sentence. Cut or merge the redundant Scope bullets and keep the bullets that add new limits."
  - scope: passage
    quotes: ["The comparison names the predecessor and adopted successor, the requirements under which the successor counts as better, and how those requirements apply to the predecessor's prior capabilities."]
    reason: "The opening names the claim's slots but not their content. The two-component relation (non-regression on the predecessor's prior capabilities plus a declared gain on a named dimension) appears only in the second section. That section then restates the non-regression scope in a separate paragraph whose only new content is that thresholds set permitted degradation. Before the claim, the opening also spends two sentences restating the retention and learning definitions. Direction: compress the retention setup to one contrast clause, fill the summary sentence with the two components, and fold the threshold gloss into the two-component sentence so the non-regression-scope paragraph can go."
  - scope: passage
    quotes: ["The third case requires evidence of that contribution, not just the sequence of a failure, a retained instruction and better results."]
    reason: "The retention/improvement/learning section first separates this claim from its neighbours, then branches into how to establish that experience caused an improvement (a with/without-instruction experiment). That method concerns the learning claim, not the state comparison this note makes. It needs different support and draws attention away from the note's own claim. Direction: reduce the paragraph to at most one clause stating that a passed comparison does not identify the experience link, and leave the evidence method to the factory-learning note."
outcome: report
---

# Simplification synthesis: better-factory claim compares operative states

## Opportunities

### 1. State each boundary once

- Location: Opening paragraph ("not a verdict on the factory's quality over its open production family"); "The assessment relation is antecedent and scope-indexed" ("Prior declaration prevents that form of post-hoc selection. It does not show that the requirements track factory quality."); "Improvement, retention and learning are different claims" ("Internal controls on what the factory retains govern adoption…"); `## Scope` bullets 1, 2 and 5; relata section ("A staging comparison can supply evidence for adopting a candidate…").
- Combines: detail-overhang (quality-tracking caveat recurrence); marginal-value-redundancy findings on the antecedence bullet, the oracle bullet and the adoption-control bullet; branch-bloat's adoption-control aside.
- Preserve or decide: Keep the two Scope bullets that add limits the body does not state. One says an independently supplied retrospective criterion can ground a legitimate improvement claim. The other says a relation permitting retirement of prior capability can be declared, and the preserved-path consequence then fails. The author must decide where the single quality-tracking caveat lives: the opening frames the claim as relation-relative, while Scope collects limits. The author must also decide whether "a description cannot change whether its judgment was required for installation" makes a distinct point. If it does, the point needs a clearer statement. If it does not, it can go with the other duplicates. Keep the first sentence of Scope bullet 6, which generalizes the framework to other systems. Its trailing sentence repeats the factory-development condition.

### 2. Put the two-component relation in the opening

- Location: Opening paragraphs, from "A software factory undergoes experience-responsive retention…" through "…how those requirements apply to the predecessor's prior capabilities", and the paragraph "Non-regression needs a declared scope…" in the assessment-relation section.
- Combines: both core-claim-obscured findings (retention setup before the claim; requirements given only as placeholders); marginal-value-redundancy finding on the non-regression-scope paragraph.
- Preserve or decide: Keep the gloss that thresholds specify how much degradation is permitted, and keep the framing that using the predecessor's prior capabilities as the scope is this framework's choice. Scope bullet 4 depends on it being a choice and not the only declarable shape. A possible resolution, offered only as one option: "It compares predecessor and installed successor under requirements fixed before development: non-regression on the predecessor's prior capabilities and a declared gain on a named dimension." The `TODO` blockquote about replacing "software factory" with "software house" is a terminology decision for the author, not a compression edit. Settle it before rewriting the opening so that the reworded opening uses the final term.

### 3. Narrow the learning branch to the boundary

- Location: "Improvement, retention and learning are different claims", the paragraph beginning "The third case requires evidence of that contribution…" and the Learning bullet.
- Combines: branch-bloat finding on the learning-evidence paragraph.
- Preserve or decide: The note's Relevant Notes cite the experiment note as grounding "why a passed comparison does not identify the experience link". The author must decide whether this note keeps that boundary in one clause, which retains the link's role, or moves it to the factory-learning note and drops or re-purposes the link. Keep the closing rule "The declared comparison judges improvement; the experience-to-change link distinguishes learning". Keep the three hypothetical cases too, which other checks found proportionate.
