---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/compression-bundle/detail-overhang.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion: kb/instructions/compression-bundle/detail-overhang.md
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: 0d85a83f4c3145a4a0143a9df39bf13c
completed-at: '2026-11-19T15:55:57Z'
findings:
- scope: passage
  quotes:
  - 'In a practitioner account that motivated this analysis, Nostalgebraist quotes
    a public Anthropic write-up about internal coding-agent use of Claude comparing
    multi-agent supervision to babysitting: "I need my juice box opened and it''s
    an emergency that my juice box is opened. And that is voiced with the same level
    of concern as the one who has sliced their finger and is bleeding." ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md),
    verbatim) and "When you are babysitting, every child brings to you concerns with
    an equal demand for your attention and the various [Claudes] also do that." ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md),
    verbatim). That example also reflects weak absolute-stakes calibration, and the
    account does not isolate whether worker behavior or a workflow that turns every
    stop into an immediate ping made interruption the default; either way, removing
    competing work leaves the isolated worker without live relative urgency.'
  reason: An illustrative origin anecdote outgrows its role (~150 words supporting
    a 20-word mechanism). The second verbatim babysitting quote restates the same
    point already made vivid by the juice-box/bleeding-finger quote, and the attribution
    chain plus full-sentence confound caveat can be compressed in place while preserving
    both the vivid contrast and epistemic caution.
  level: warn
- scope: passage
  quotes:
  - In the same practitioner account, Nostalgebraist describes coding agents as "liable
    to go off on silly low-value tangents (which they treat with the utmost seriousness)"
    ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md),
    verbatim) and observes that "Everything is flattened out; everything is assigned
    equal importance; every interaction looks and feels the same" ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md),
    verbatim).
  reason: Stacking a second verbatim quote and repeated citation onto the tangents
    bullet stretches a non-corroborative illustration, because the second quote restates
    general priority flattening rather than adding tangent-specific detail; it may
    still earn space if kept or moved to ground the flattening phenomenon.
  level: info
- scope: passage
  quotes:
  - once even a comparison-sufficient summary of competing work cannot sit beside
    deep task context without degrading focus—and no calibrated local threshold can
    replace side-by-side comparison.
  reason: Re-enumerates in full two boundary conditions already fixed in the claim-mode
    paragraph and defended in the immediately preceding paragraph; a brief back-reference
    would do the same work without repeating the caveat verbatim.
  level: info
contract: verdict
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/0d85a83f4c3145a4a0143a9df39bf13c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/18152160540b5537749a9848/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/0d85a83f4c3145a4a0143a9df39bf13c/outputs/review.md
raw-output-sha256: 5a6680a2f7e04e184b03ec2f2e46a1f8175d098f45ca62372e2224d2aee08e96
---

# Review

## Assessment

The note is generally well-proportioned: its thesis, causal separation between missing context and failure-direction defaults, architectural split, three-way decision unbundling, residual interface friction, and scope boundaries each carry distinct argumentative work without padding.

The main detail overhang sits in the practitioner-anecdote treatment under the failure-modes list. Because the note explicitly frames the Nostalgebraist account as motivating origin rather than corroborating evidence, devoting four full verbatim quotes (with repeated inline citation tags), a layered provenance setup, and a full-sentence methodological caveat across the first two bullets pulls disproportionate weight onto an illustrative example—most acutely in the uncalibrated-escalation bullet, where the second babysitting quote repeats the first quote's contrast verbatim. Compressing that bullet in place keeps the memorable juice-box contrast and the necessary confound qualification without letting the anecdote dominate the section.

## Details that earn their space

Two other substantial passages were checked and pass without flagging:

- **Static rules and injected cost signals:** Giving the concession for locally calibrated metrics (latency budgets, token caps, dollar costs) and contrasting them with an uncalibrated abstract bar answers the strongest counter-proposal to the thesis; compressing it further would weaken the argument against a fair objection.
- **Commonplace illustrations (mid-task noticing, ADR 138, unresolved frontier):** Each bullet is short and illustrates a distinct operational scale (mid-task, single-run stop, cross-surface portfolio), with the ADR 138 bullet concretizing the three-way unbundling immediately above it rather than over-elaborating implementation detail.
