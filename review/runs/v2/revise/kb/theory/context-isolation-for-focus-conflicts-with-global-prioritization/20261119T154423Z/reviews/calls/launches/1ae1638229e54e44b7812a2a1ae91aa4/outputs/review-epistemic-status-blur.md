---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The *direction* of the failure comes from a separate mechanism when relative priority is unknown—most visibly the workflow's or policy's default action, reinforced by model-level thoroughness and salience biases."
    reason: >-
      Combines a structural derivation (that missing competing-work context yields indiscrimination rather than a specific failure direction, so a separate mechanism sets direction) with an unsupported empirical/mechanistic proposal ("most visibly the workflow's or policy's default action, reinforced by model-level thoroughness and salience biases") in the same flat declarative register. Neither cited evidence nor derivation establishes that defaults are "most visibly" responsible or that model-level thoroughness and salience biases reinforce them; the following bullet explicitly notes that the cited practitioner account does not isolate workflow defaults from worker behavior.
    level: warn
  - scope: passage
    quotes:
      - "compounding the oracle asymmetry—tests reward a present guard but rarely penalize an unneeded one—analyzed in [a guard against a conjectured requirement removes the experiment that would test it](./a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md)."
    reason: >-
      Presents both the linked note's conjectural oracle-asymmetry account and its compounding with missing global context declaratively without marking the conjectural status of the compounding claim, though this occurs inside an illustrative manifestation rather than the central thesis.
    level: info
outcome: warn
---

# Review

Most of the note separates epistemic statuses carefully: the central claim is marked as a conditional structural derivation (`Claim mode: universal` under three stated conditions), the practitioner quotes from Nostalgebraist/Anthropic are explicitly scoped as motivating origin rather than corroboration (including their confounding factors), the Commonplace mechanisms are explicitly scoped as local design examples rather than comparative evidence, and Scope disclaims controlled measurement of execution quality, triage error, or saved operator attention.

The main status collapse occurs in the transition from structural indiscrimination to the observed failure direction, where an uncorroborated empirical attribution (identifying workflow defaults as "most visibly" the mechanism and citing model-level thoroughness and salience biases) is stated with the same declarative confidence as the structural derivation immediately preceding it.
