---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The type spec asks that the claim's limits be stated under their own `## Scope` heading, omitting the section only when no limit is known. This note knows several limits but scatters them through the body: the Commonplace objective is 'not a claim that every project should use the same measure'; the release checks are 'not a survey of how often each reason applies'; an on-balance judgment 'does not override a binding requirement'; preferring the successor does not assign credit to a component; and the availability of reasons 'does not establish that any particular agent judges well'. With no `## Scope` section, a rescoping edit has to rewrite body prose, and scope-testing gates will not find these limits where they look."
    level: warn
  - scope: passage
    quotes:
      - "Is Python better than it was twenty years ago?"
    reason: "The spec asks that the main claim or mechanism come near the top. The opening reaches the claim through a Python example, and the general statement (preferences defended by reasons about which work changed, for whom, and why, without a score) is only implicit in the second paragraph. The title carries the claim, so this is acceptable, but stating the general mechanism in one sentence before or right after the example would make the claim recoverable without reading through the case."
    level: info
outcome: warn
---

# Review

The note mostly does what the `note` type spec asks. The title compresses the claim. The description says why to retrieve the note: deciding whether to keep a change with mixed gains and losses, and which uncertainties to investigate. The note links to adjacent notes both inline (the tag coverage trace, the factory comparison, the contrast note) and in the footer (the declared-objective note), and each link says what it contributes. It keeps to design rationale. Its few imperatives ("investigate an unknown only if a plausible answer could reverse the choice", "First ask what improved") are decision criteria with their reasons attached, not procedural steps that belong in an instruction.

The one unmet authoring instruction is the `## Scope` section. The spec allows omitting it only when no limit is known, and this note states several limits, all of them inline. Gathering them under `## Scope` would satisfy the spec without changing the argument. The info finding about where the main claim first appears is advisory: the claim is reachable from the title and the first two paragraphs, but it appears as an instance before it appears as a general mechanism.
