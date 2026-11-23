---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - its scorer saw a failure mode in a quarter of runs that never reached the proposer
  reason: 'Modifier attachment: ''that never reached the proposer'' attaches most
    naturally to the nearest noun, ''runs'', giving ''runs that never reached the
    proposer''. The intended reading is that information about the failure mode never
    reached the proposer. Rephrase, for example: ''its scorer detected a failure mode
    in a quarter of runs, but that signal never reached the proposer''.'
  level: warn
- scope: passage
  quotes:
  - those domains stay with weights-only continual learning
  reason: 'Demonstrative reference: no domains have been named in the paragraph or
    the hazard list before it. The nearest candidate is ''work where no fixed criterion
    is adequate'', several sections earlier. A reader can plausibly take ''those domains''
    to mean the domains of the controlled runs or some unstated set. Name the work
    explicitly.'
  level: warn
- scope: passage
  quotes:
  - a third change revises the review check itself
  reason: Coming right after 'three similar over-broad rules', 'a third change' can
    be read as one of those three rules. It means the third change in the narrated
    sequence (add, narrow, revise the check). It is also unclear whether 'the review
    check' is the 'brevity check' just named. 'A third change in the sequence revises
    that check itself' would remove both readings.
  level: info
- scope: passage
  quotes:
  - the system can still act as a bounded decision
  reason: Read literally, the system acts as a decision. The intended meaning, acting
    and treating the step as a bounded decision, is recoverable, but 'can still take
    the step as a bounded decision' would read cleanly.
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/113c49a86250430da7cf4d1d3b227564/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/94047712ea43e5fa415689b1/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 113c49a86250430da7cf4d1d3b227564
completed-at: '2026-11-22T09:37:43Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/113c49a86250430da7cf4d1d3b227564/outputs/review-parsing-ambiguity.md
raw-output-sha256: dac79fd7f0dfaeb72bccee87ae3f5b235fac2e977c333eedd6c9f0771262351f
format: 2
---

# Review

## Summary

Most sentences parse one way. Pronouns in the definition and Bitter Lesson
sections have clear antecedents, and the negations ('need not', 'no … yet')
scope as intended. Two sentences allow a plausible wrong reading. In the
harness-evolution sentence, a relative clause attaches to the wrong noun.
The closing failure condition uses 'those domains' with no antecedent. Two
smaller ambiguities are recorded as information.
