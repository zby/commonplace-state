---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'bounds: movement can assemble candidate views but does not perform recognition'
  reason: The body already links this note and says that resolution-switching 'helps
    a reader assemble those views; it does not perform the recognition'. The footer's
    context phrase nearly restates that sentence. Only the typed label `bounds` is
    new, so under the gate's second question the entry is not inflated, but it is
    the thinnest entry.
  level: info
- scope: passage
  quotes:
  - 'enables: contextual articulation preserves why a target matters across a transition'
  reason: The body links this note inline at the end of a paragraph that already explains
    how a contextual phrase preserves why the target matters during a switch. Only
    the `enables` label is new, so the entry is not inflated, but it adds little beyond
    the body.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/complexity/connection-inflation.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/476078a1451bab7588b06dd8/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/476078a1451bab7588b06dd8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: 02997e7b519f4ab786c09b7c535f549e
completed-at: '2026-11-16T22:29:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/02997e7b519f4ab786c09b7c535f549e/outputs/review-connection-inflation.md
raw-output-sha256: 1950a3d6b5ecdb6601c49d730bbe2f789d590f59658c52bea0fe1e79f200c34f
format: 2
---

# Review

I checked each Relevant Notes entry against the gate's two questions.

- **Title as claim enables traversal as reasoning.** The body links it as the reason a reader can inspect a chain of assertions. The footer adds the `enables` label and frames titles as a lower-cost view. This framing is close to the body's but is typed. Not inflated.
- **Link-following and search impose different metadata requirements.** The body cites it for different metadata requirements. The footer adds the `enables` label and a new framing: the two entry routes have views that differ in scope and context. Not inflated.
- **Agents navigate by deciding what to read next.** The body does not link this note. The footer supplies a navigation edge that is not available elsewhere. Not inflated.
- **Link strength is encoded in position and prose.** The body restates this relationship almost fully. Only the label is new (info finding).
- **Pointer design tradeoffs in progressive disclosure.** The body cites the trade-offs. The footer adds the `grounds` label and the new framing that pointer tiers can form intermediate views. Not inflated.
- **Recognition, not linking, is the hard problem.** The footer's phrase nearly copies the body sentence. Only the `bounds` label is new (info finding).
- **Addressability grain sets a matched selective-read floor.** The Boundaries section discusses addressability grain without linking it. The footer supplies the only link to the note, with the `contrasts` label. Not inflated.
- **Knowledge-access architecture must be evaluated end to end.** The body does not link this note. The footer adds a wider evaluative context. Not inflated.

No entry fails both questions. Two entries carry only a typed label beyond what the body says, and they are recorded as info.
