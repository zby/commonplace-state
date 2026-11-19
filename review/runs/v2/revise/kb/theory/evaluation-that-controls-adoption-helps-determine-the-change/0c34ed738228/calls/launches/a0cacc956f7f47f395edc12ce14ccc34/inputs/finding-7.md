---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 858d17d044f34df5abd77e29f9ec3e32
completed-at: '2026-11-17T07:21:57Z'
findings:
- scope: passage
  quotes:
  - helps determine which system results
  reason: The word 'results' can be read as a plural noun ('which system results',
    meaning outputs or test results) or as a verb ('which system results', meaning
    which system comes to exist). The paragraph is about evaluators reading results,
    which makes the noun reading likely on a first pass. Under that reading the sentence
    says that evaluators determine outputs, not that they select the resulting system.
    The opening claim of the note therefore garden-paths. A rewording such as 'helps
    determine which system comes into use' or 'helps determine the resulting system'
    removes the ambiguity.
  level: warn
- scope: passage
  quotes:
  - human approval does not remove the need to justify the assessment
  reason: '''The assessment'' could refer to the test''s measurement of capability
    in the same sentence, or to the ''later assessment'' in the previous sentence.
    Both readings are available. The practical difference is small because either
    assessment needs justification, but naming the referent, for example ''justify
    the test-based assessment'', would make it explicit.'
  level: info
contract: verdict
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/737b4f56075cd04272e4f10e/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/737b4f56075cd04272e4f10e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/858d17d044f34df5abd77e29f9ec3e32/outputs/review-parsing-ambiguity.md
raw-output-sha256: 24ec52f845ee7154c694a7a76a7a8ef930c4db232b917b7d3854bd859b8734c2
---

# Review

Most sentences parse unambiguously. Negation scope in "does not, through that assessment alone, determine its adoption" and "not whether a person or a program makes it" is clear. In "That would give it a causal role in a different transition", the pronouns resolve to the preceding sentence's later assessment and its effect.

The opening sentence has a noun/verb ambiguity on "results". Because it is the note's lead claim and the evaluation context invites the wrong reading, this is a WARN. One definite reference in the Scope list is underspecified, which is INFO.
