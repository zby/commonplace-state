---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/prose/source-residue.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/review-gates/prose/source-residue.md
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 304ff2b910374d728798b623f2a4a074
completed-at: '2026-11-18T16:02:23Z'
findings:
- scope: passage
  quotes:
  - no mechanism here checks that the capture faithfully represents the original or
    that the named author wrote it
  reason: '''Here'' refers to one particular checking system, the ADR-described implementation.
    The rest of the sentence reads as a general statement about quote checking. The
    note claims general scope (its description reads ''Quote checking in general'').
    The general point is that a capture-identity check does not establish the capture''s
    faithfulness or authorship. Say that, or mark the sentence explicitly as describing
    the cited implementation.'
  level: warn
- scope: passage
  quotes:
  - An "unresolved" outcome covers recognized quote candidates the checker could not
    pair with a source. Quotations the extractor never recognized appear in no outcome,
    and their rate is unmeasured.
  reason: The bullet uses one implementation's outcome vocabulary ('unresolved') and
    pipeline component ('the extractor') as if every quote checker had them. In a
    general note, it should either state the general limit or say whose checker it
    describes. The general limit is that a checker reports only on candidates it recognizes,
    so unrecognized quotations escape every outcome. The 'rate is unmeasured' claim
    applies only to a specific system.
  level: warn
- scope: passage
  quotes:
  - A checksum against a recorded capture, with explicit name pairing between citation
    and file, binds the compared bytes to that capture
  reason: Checksums and explicit citation-to-file name pairing are a concrete mechanism
    from ADR 073. They are presented as how source identity is established, not as
    one way to establish it. The general requirement, binding the compared bytes to
    a declared capture rather than to whatever sits at a path, transfers. The specific
    mechanism could be marked as an example.
  level: info
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/67f80dfa9e92a14becfd3eb3/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/67f80dfa9e92a14becfd3eb3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/304ff2b910374d728798b623f2a4a074/outputs/review-source-residue.md
raw-output-sha256: 7ff0b04049db456189d7e7b7c9324a69d0a167fee30aef61a5dc93a760e3c36f
---

# Review

## Summary

The title and description claim general scope for quote checking ("Quote checking in general"), and the Scope section says transfer rests on reasoning, not external evidence. Most of the body is phrased generally. It cites ADRs as instances, and the casebook corpus is introduced as "one" corpus, which marks it as an example.

Two passages carry vocabulary from the Commonplace implementation without framing it as an example. "No mechanism here" refers to an unnamed system. The final Scope bullet uses that system's outcome labels and extractor component. Each should be either restated as a general limit or attributed to the cited implementation. The checksum-plus-name-pairing passage is a milder case: the requirement generalizes, but the mechanism is presented as if it were the only one.
