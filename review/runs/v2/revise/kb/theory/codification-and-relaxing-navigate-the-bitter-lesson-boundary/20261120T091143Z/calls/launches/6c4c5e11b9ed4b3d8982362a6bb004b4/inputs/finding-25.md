---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: c47a496a07e14123b60f65c12d35a61c
completed-at: '2026-11-20T09:15:25Z'
findings:
- scope: passage
  quotes:
  - one case-level conjecture offers as the diagnosis of a structured method's loss
    under scaling
  - Unsupported proxy scope may explain a structured method's loss under scaling
  reason: Both link texts promise a hedged, case-level conjecture ('may explain')
    about proxy scope. The target is titled 'The bitter lesson selects against unearned
    reach, not against structure'. Its opening says the criterion 'is claimed universally'
    and names the property 'earned reach' rather than proxy scope. A reader who does
    not follow the link will underestimate the target's scope and misname its concept.
    Use link text that matches the target's claim, e.g. 'the bitter lesson selects
    against unearned reach'.
  level: warn
- scope: passage
  quotes:
  - fixed artifacts split into exact specs and proxy theories
  reason: The footer link text says artifacts split into exact specs and proxy theories.
    The target's title and opening place exactness on the artifact–requirement link
    and proxyhood on the requirement–objective link, and they call artifact-level
    labels safe shorthand only when the path is named. The link text asserts the artifact-level
    partition the target qualifies. The inline 'fixed-artifact distinction' with its
    exact-spec/proxy-theory parentheticals is close enough.
  level: warn
- scope: passage
  quotes:
  - the bottom-up extraction method that avoids the vision-feature failure mode
  reason: The annotation promises a method that avoids the failure mode. The target
    presents spec mining as converting blurry-zone components into exact-spec artifacts
    and says mined specs can be relaxed when they break. This note's body says spec
    mining only 'improves the odds' and is 'still a bet'. 'Reduces the risk of' would
    match.
  level: info
- scope: passage
  quotes:
  - detects when codified components are encoding vision features
  reason: The target says its signals shift confidence and detect badly-fitting theories,
    'not the theory/spec distinction itself'. The annotation promises detection of
    vision-feature (proxy-theory) encoding as such.
  level: info
contract: verdict
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/c47a496a07e14123b60f65c12d35a61c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/7e4e9a1ba2c60999443d2dd8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/c47a496a07e14123b60f65c12d35a61c/outputs/review-misleading-link-text.md
raw-output-sha256: bda0c9e03c06027b05a202d6421178035523636b4a92b468c56c6bf399da558b
---

# Review

Links checked (repeated links to one target count once):

- `exact-implementation-does-not-validate-a-requirement.md`: the inline link is adequate; the footer link text asserts an artifact-level partition the target qualifies (warn).
- `definitions/codification.md`: matches.
- `constraining-and-extraction-both-trade-generality-for-reliability.md`: both link texts match the target's title claim.
- `bitter-lesson-selects-against-unearned-reach-not-against-structure.md`: both link texts describe a hedged case-level proxy-scope conjecture; the target makes a universal earned-reach claim (warn).
- `spec-mining-as-codification.md`: the link text matches; the footer annotation overclaims (info).
- `operational-signals-that-a-component-is-a-relaxing-candidate.md`: the inline "Relaxing signals" link matches; the footer annotation overclaims (info).
- `verifiability-gradient.md`: matches.

External targets not resolved within the reading scope: the Finzi et al. epiplexity paper (arxiv 2601.03220) and the Ebrahimi et al. induction-bias paper (arxiv 2602.18333). Their link texts are bibliographic names and were not judged against content.
