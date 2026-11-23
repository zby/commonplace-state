---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
note-sha256: 6b9410142685c447424f1bfcc9f187405069541a6a0006b521ec43e2daea610e
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 2021ef15d4474341b7b3eafc0e8aa06b
completed-at: '2026-11-23T11:40:31Z'
findings: []
contract: verdict
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/2021ef15d4474341b7b3eafc0e8aa06b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/41178708d4aba1f91c9e17be/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/2021ef15d4474341b7b3eafc0e8aa06b/outputs/review-parsing-ambiguity.md
raw-output-sha256: 1709194c4d88f300e3cab529418cfe35ea59faa6ac2e5833e530d1b60c38e65e
---

# Review

I checked negation scope, modifier attachment and pronoun reference sentence by sentence.

- "The test is not whether the reviewer retrieved the incident. It is whether..." The negation clearly scopes over the whether-clause, and the contrast resolves it at once.
- "The incident shows what the review must distinguish, not that the review rule must change." The "not that" clause attaches unambiguously to "shows".
- "A reviewer following the original instruction could still recognize it." Here "it" refers to "that connection" in the previous sentence; "the original instruction" has no other plausible antecedent.
- "The lesson still applies if the new sources also share an origin and the claim relies on their independence." Both conditions attach to "applies"; reading "and the claim relies..." as an independent assertion is not plausible.
- In the title, "it" grammatically takes "a fixed review rule" and "they" takes "lessons". Any question about whether the rule or the reviewer identifies applicability is about framing, not a second syntactic parse, so this gate does not flag it.

No sentence has a plausible unintended reading.
