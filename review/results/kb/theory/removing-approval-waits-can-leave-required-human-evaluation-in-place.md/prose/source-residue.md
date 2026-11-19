---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/prose/source-residue.md
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion: kb/instructions/review-gates/prose/source-residue.md
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: af9c036c66d64c64b1f4131a1ad4fcc1
completed-at: '2026-11-18T16:01:59Z'
findings:
- scope: passage
  quotes:
  - Adoption may proceed without a person while the process specification still assigns
    monitoring or later revision decisions to one.
  reason: The title covers approval waits in general, but this opening sentence introduces
    adoption, monitoring and revision without framing. Those terms come from change-adoption
    processes, such as adopting an agent instruction. The rest of the note works within
    that domain. One clause stating that the note concerns processes that adopt and
    revise changes would align the stated generality with the vocabulary. Alternatively,
    the sentence could be marked as an instance. This is minor because the vocabulary
    also reads naturally as general process language.
  level: info
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/54fd9e291f0a609f04f9d404/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/54fd9e291f0a609f04f9d404/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/af9c036c66d64c64b1f4131a1ad4fcc1/outputs/review-source-residue.md
raw-output-sha256: 5817175a51aee1adfa1275483831b1aa59d828075742ea034e5b6dd08373f9df
---

# Review

The title and description make a general claim about approval waits and specified evaluation tasks. The concrete material is mostly framed as illustration. The agent-instruction scenario is introduced as "two hypothetical cases". The weekly-review example begins with "Suppose". "Maintainer", "agent" and "instruction" appear only inside those framed cases. Scope returns to general terms: required human intervention, human influence and habitual waits.

The only unframed domain vocabulary is the change-adoption lifecycle of adoption, monitoring and revision in the opening and in the revision paragraph. It narrows the note to processes that adopt changes and does not tie it to one source. That narrowing is plausibly intended. The finding is informational.
