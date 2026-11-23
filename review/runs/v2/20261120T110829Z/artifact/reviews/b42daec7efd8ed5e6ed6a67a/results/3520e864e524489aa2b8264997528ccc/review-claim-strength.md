---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'The H1 title asserts close to the definition of information hiding: a shared
    interface means callers need not change when the implementation is swapped. An
    informed reader would hardly argue the opposite of that literal statement. The
    contestable point the note actually establishes is that this prompt–code boundary
    leaks asymmetrically: prompt-to-code breaks loose LLM callers, and code-to-prompt
    breaks code callers'' cost, latency and error assumptions. That point appears
    in the description and body but not in the title. Sharpening the title toward
    the asymmetric leak, or toward the condition under which caller-free swapping
    holds, would give it a claim someone could dispute.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
note-sha256: 03383f1081ecc27ca0b3ffe1e15f8cf3d243a0d57720709b648091539a0f6cf7
criterion-sha256: 8e4666d11f54dfcb2ef8de2c1942bb8fa7d77bd1fb54fec00bb5794bf4642367
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/3520e864e524489aa2b8264997528ccc/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/b42daec7efd8ed5e6ed6a67a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 3520e864e524489aa2b8264997528ccc
completed-at: '2026-11-20T11:09:20Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/3520e864e524489aa2b8264997528ccc/outputs/review-claim-strength.md
raw-output-sha256: 4da0881e27a4c46d53e3d9a3c828e5308eb881f4651cd918b96e32be792a4d75
format: 2
---

# Review

## Summary

The title is a proposition, but its literal content is close to a truism. "A unified interface lets programmers choose prompts or code without changing callers" mostly restates what any shared interface does. The only contestable element is the implicit assumption that prompts and code *can* sit behind one interface. The note does not defend that assumption much; it takes it as given.

The note's non-obvious contribution is the asymmetric leakage across the two swap directions, together with the practical rule that follows: enforce schemas before codification, and write call sites for fallible, higher-latency calls if they may move back to prompts. A title built on that point would pass the "could someone argue the opposite?" test more clearly. For example, someone could argue that a unified interface makes prompt–code swaps transparent, and the note disputes exactly that.
