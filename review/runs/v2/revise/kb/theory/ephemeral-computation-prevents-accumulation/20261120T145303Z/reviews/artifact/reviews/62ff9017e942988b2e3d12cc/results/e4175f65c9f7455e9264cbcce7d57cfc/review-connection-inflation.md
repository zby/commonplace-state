---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '- [Codification](./definitions/codification.md) — contrasts: execution form is
    separate from artifact lifetime'
  reason: The body already links to ./definitions/codification.md inside a section
    titled 'Retention and codification are different choices' that defines codification
    as execution form and explicitly contrasts it with retention; the footer entry
    repeats the same link and framing without adding new navigational context.
  level: warn
- scope: passage
  quotes:
  - '- [The Flawed Ephemeral Software Hypothesis](https://www.blackhc.net/essays/future_of_software/)
    — evidenced-by: supplies the production-knowledge pressures motivating durable
    carriers'
  reason: The body already links to https://www.blackhc.net/essays/future_of_software/
    and articulates the exact same evidential relationship and framing—that Kirsch's
    critique identifies production knowledge that must survive replacement and motivates
    retaining that knowledge—so the footer entry adds no navigational value beyond
    the body.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/ephemeral-computation-prevents-accumulation.md
  against kb/instructions/review-gates/complexity/connection-inflation.md
contract: verdict
note: kb/theory/ephemeral-computation-prevents-accumulation.md
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
note-sha256: d3a6a9e3e3da3e9b0cfdf1f37204cd3f0a4037ff53011b0c118feabbef1ffbc3
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
target-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/e4175f65c9f7455e9264cbcce7d57cfc/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/artifact/reviews/62ff9017e942988b2e3d12cc/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews
launch: e4175f65c9f7455e9264cbcce7d57cfc
completed-at: '2026-11-20T14:56:31Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/e4175f65c9f7455e9264cbcce7d57cfc/outputs/review-connection-inflation.md
raw-output-sha256: 65ff6ccb309e467ce134492f5ff3785619ad08b1a214460f84e72cb1a83c4818
format: 2
---

# Review

Three of the five Relevant Notes entries add navigational value: the two entries for *Retained system-definition artifacts enable persistent deployment-time adaptation* and *Discarding software requires preserving the operational knowledge later work needs* do not appear in the body at all, and the entry for *The deployed system, not the model alone, is the unit of learning* supplies the target's full claim and explicit `grounds` relationship that are absent from the body's brief inline `[deployed system]` link.

The remaining two entries—for *Codification* and *The Flawed Ephemeral Software Hypothesis*—fail both checks of the gate because the body already links to each target and explicitly spells out the same contrast or evidential framing that the footer restates.
