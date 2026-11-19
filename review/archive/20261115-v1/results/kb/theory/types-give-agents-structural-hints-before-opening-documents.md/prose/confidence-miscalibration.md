---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/prose/confidence-miscalibration.md
criterion-sha256: ebb030953d7a6ed78253a52b0fd52c417d139660b211400eb0cdf860fed6e390
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: b1cbd1adcc964c3a9cd5db25254b4b2d
completed-at: '2026-11-12T09:57:46Z'
---
### Summary

The note's core mechanism (type signals affordances, description selects among instances) is a qualitative analytical move and is stated reasonably. However, the opening frames a forced dichotomy and universal premise as settled fact, and the payoff sentence makes an empirical-sounding scale claim with no evidence. These are the note's own constructions presented with assertive wording.

### Findings

- WARN: "Without types, an agent must either load everything (wasteful) or guess what's relevant (error-prone)." This asserts an exhaustive dichotomy the note does not support. Agents can also search, scan filenames, or read descriptions that exist without a type field; the note itself later credits the description, not the type, with instance-level filtering. "Must" overstates; the claim should propose that types reduce reliance on these fallbacks.
- WARN: "Together they let an agent narrow from hundreds of files to the few it needs without opening any of them." This is an empirical-sounding scale and outcome claim (hundreds → few, zero documents opened) with no cited observation or measurement. It is presented as a demonstrated result rather than an expected effect.
- INFO: "Agents are stateless — they start fresh every session with no memory of what they've read before." Stated as universal; it holds for the default session model but not for agents with persistent memory systems. A scope qualifier ("by default", "within this framework's session model") would calibrate it.
- INFO: "Types solve this" asserts a full solution where the note's own argument supports partial mitigation (routing still depends on descriptions and on enforcement, per the last paragraph).

### Suggested Revision

- "Without types, an agent falls back on loading broadly (wasteful) or selecting by filename and search hits (error-prone)."
- "Types reduce this cost by giving agents structural hints *before* opening a document."
- "Together they can let an agent narrow a large collection to a few candidates before opening any of them."
- "Agents start each session without state from earlier sessions unless a memory mechanism supplies it."

## Result: WARN
