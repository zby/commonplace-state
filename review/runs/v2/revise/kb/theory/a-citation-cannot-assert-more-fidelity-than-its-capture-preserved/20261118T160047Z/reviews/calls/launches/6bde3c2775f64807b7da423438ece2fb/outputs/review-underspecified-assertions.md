---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Checking current bytes catches a changed or removed passage at the next check"
    reason: "Unresolved scope: current bytes of what. Reading 1: the current bytes of the retained capture file, compared with the pin, so the check catches a capture that was altered or replaced locally, and changes to the live original go undetected until someone recaptures. Reading 2: the current bytes of the live original, so the check catches changes in the source itself. The preceding sentence ('compares current bytes with it', the pin) and 'The binding stops at the capture' lean toward reading 1, but 'a changed or removed passage' reads like source drift and fits reading 2. The choice changes what the mechanism guarantees about freshness relative to the named source, what evidence would show it works, and whether a reader relying on a passing citation must still recheck the original."
    level: warn
  - scope: passage
    quotes:
      - "A mismatched or unreadable file is a failure, not an invitation to find another copy."
    reason: "Unresolved scope or threshold between 'unreadable file' (failure) and 'missing bytes' (unverified, later in the section). Reading 1: unreadable means the expected file is present but cannot be decoded or fails its checksum; absence is separate and only unverified. Reading 2: unreadable includes a file that cannot be opened because it is absent, so absence is a failure. The two readings assign different outcomes to the same situation (a capture held on another machine), which changes the consequence for the citing note."
    level: warn
  - scope: passage
    quotes:
      - "so it cannot simply block the way a wording check does"
    reason: "Possible ambiguity between 'support judgment must never block' and 'support judgment can block only with added safeguards'. 'Simply' and the surrounding cost/noise framing lean toward the second reading, and the note makes no recommendation that depends on the difference, so materiality is not shown."
    level: info
outcome: warn
---

# Review

Most load-bearing assertions are exact. The quote check is defined as one relation with its inputs named (quoted span, resolved source text, normalization rule, one occurrence or one occurrence inside a stated range). "Exact" is defined as equality after a stated normalization rule. The fail-not-warn severity is scoped to exact-wording claims and tied to an explicit trade-off. The identity binding is explicitly bounded at the capture, and the Scope section names what the account excludes and what it leaves unmeasured.

Two assertions in "Which evidence a pass is relative to" leave a material choice open. The change-detection sentence does not say whose current bytes are compared, which decides whether the mechanism detects source drift or only local capture drift. The failure rule for unreadable files does not separate unreadable from missing, which decides whether an absent capture fails or is merely unverified.
