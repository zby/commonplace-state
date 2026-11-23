---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: bcdab9a9707244b8a3b307957cd61085
completed-at: '2026-11-20T11:12:21Z'
findings:
- scope: passage
  quotes:
  - Enforcing input schemas strictly at the call boundary while the implementation
    is still a prompt prevents callers from accumulating this hidden coupling.
  reason: 'The coupling just described includes ''loosely phrased, slightly malformed,
    or context-dependent arguments''. Reading A: strict schema enforcement prevents
    all of it, so the recommendation is sufficient for safe prompt-to-code swaps.
    Reading B: schemas catch only structural malformation, while loosely phrased or
    context-dependent arguments that are schema-valid, such as free-text fields, still
    rely on the prompt''s inference. Under B the coupling is only reduced. The unresolved
    choice is scope: which kinds of tolerance a schema can enforce. It decides whether
    the ''practical consequence'' recommendation is sufficient or partial, and whether
    callers still need testing after codification.'
  level: warn
- scope: passage
  quotes:
  - the programmer changes the implementation, not the rule
  reason: '''The rule'' may mean the topic-based routing regularity the team extracted,
    preserved on the cases the agent already handled consistently. It may also mean
    the full behavior of the prompt, including its handling of ambiguous tickets.
    The choice affects whether calling the move ''behavior-preserving'' needs equivalence
    testing. The Scope section''s distinction between call invariance and behavioral
    invariance partly resolves it, so this finding is INFO.'
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/a61637f9427766a9413157dc/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/outputs/review-underspecified-assertions.md
raw-output-sha256: 42b2fa2f90fd1e09a61f6b693afac01423bb13211b4c02c839da186b3a271a1e
---

# Review

## Summary

Most load-bearing assertions are specific. The llm-do mechanism, the code-to-prompt leak with its named latency, cost, determinism and failure-mode dimensions, and the Scope boundaries all identify their mechanism and consequence.

The schema recommendation leaves its scope unresolved, and the difference is material (WARN). The sentence asserts prevention. Yet the coupling it is meant to prevent includes semantic tolerance that a schema may not express. The reader cannot tell whether schema enforcement is the complete safeguard or only a partial one.

"Changes the implementation, not the rule" leaves open what counts as the rule (INFO). Nearby context mitigates this.
