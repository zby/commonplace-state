---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 6bde3c2775f64807b7da423438ece2fb
completed-at: '2026-11-18T16:04:09Z'
findings:
- scope: passage
  quotes:
  - Checking current bytes catches a changed or removed passage at the next check
  reason: 'Unresolved scope: current bytes of what. Reading 1: the current bytes of
    the retained capture file, compared with the pin, so the check catches a capture
    that was altered or replaced locally, and changes to the live original go undetected
    until someone recaptures. Reading 2: the current bytes of the live original, so
    the check catches changes in the source itself. The preceding sentence (''compares
    current bytes with it'', the pin) and ''The binding stops at the capture'' lean
    toward reading 1, but ''a changed or removed passage'' reads like source drift
    and fits reading 2. The choice changes what the mechanism guarantees about freshness
    relative to the named source, what evidence would show it works, and whether a
    reader relying on a passing citation must still recheck the original.'
  level: warn
- scope: passage
  quotes:
  - A mismatched or unreadable file is a failure, not an invitation to find another
    copy.
  reason: 'Unresolved scope or threshold between ''unreadable file'' (failure) and
    ''missing bytes'' (unverified, later in the section). Reading 1: unreadable means
    the expected file is present but cannot be decoded or fails its checksum; absence
    is separate and only unverified. Reading 2: unreadable includes a file that cannot
    be opened because it is absent, so absence is a failure. The two readings assign
    different outcomes to the same situation (a capture held on another machine),
    which changes the consequence for the citing note.'
  level: warn
- scope: passage
  quotes:
  - so it cannot simply block the way a wording check does
  reason: Possible ambiguity between 'support judgment must never block' and 'support
    judgment can block only with added safeguards'. 'Simply' and the surrounding cost/noise
    framing lean toward the second reading, and the note makes no recommendation that
    depends on the difference, so materiality is not shown.
  level: info
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/e6b384e568c088e606326de2/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/e6b384e568c088e606326de2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/6bde3c2775f64807b7da423438ece2fb/outputs/review-underspecified-assertions.md
raw-output-sha256: 869350fbc869c15402933ea16bebf07f10664a2dd04f8518c582a8388036e94d
---

# Review

Most load-bearing assertions are exact. The quote check is defined as one relation with its inputs named (quoted span, resolved source text, normalization rule, one occurrence or one occurrence inside a stated range). "Exact" is defined as equality after a stated normalization rule. The fail-not-warn severity is scoped to exact-wording claims and tied to an explicit trade-off. The identity binding is explicitly bounded at the capture, and the Scope section names what the account excludes and what it leaves unmeasured.

Two assertions in "Which evidence a pass is relative to" leave a material choice open. The change-detection sentence does not say whose current bytes are compared, which decides whether the mechanism detects source drift or only local capture drift. The failure rule for unreadable files does not separate unreadable from missing, which decides whether an absent capture fails or is merely unverified.
