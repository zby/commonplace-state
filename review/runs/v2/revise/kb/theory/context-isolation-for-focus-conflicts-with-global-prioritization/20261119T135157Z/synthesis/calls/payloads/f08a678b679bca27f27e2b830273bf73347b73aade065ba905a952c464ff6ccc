---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/compression-bundle/detail-overhang.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion: kb/instructions/compression-bundle/detail-overhang.md
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/reviews
launch: b5d3710818ec496f9eaa6b15b07bf671
completed-at: '2026-11-19T13:55:02Z'
findings:
- scope: passage
  quotes:
  - 'In a practitioner account that motivated this analysis, Nostalgebraist quotes
    a public Anthropic write-up about internal coding-agent use comparing multi-agent
    supervision to babysitting: "I need my juice box opened and it''s an emergency
    that my juice box is opened. And that is voiced with the same level of concern
    as the one who has sliced their finger and is bleeding." ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md),
    verbatim) and "When you are babysitting, every child brings to you concerns with
    an equal demand for your attention and the various [Claudes] also do that." ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md),
    verbatim). The account reports equally demanding interruptions; it does not isolate
    whether worker behavior or a workflow that turns every stop into an immediate
    ping made interruption the default.'
  - In the same practitioner account, Nostalgebraist describes coding agents as "liable
    to go off on silly low-value tangents (which they treat with the utmost seriousness)"
    ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md),
    verbatim) and observes that "Everything is flattened out; everything is assigned
    equal importance; every interaction looks and feels the same" ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md),
    verbatim).
  reason: Two adjacent bullets spend roughly 185 words, four verbatim quotes, and
    four identical citation links elaborating a single practitioner anecdote that
    the note scopes as motivating origin rather than corroboration. In each bullet,
    the second quote restates the point already made by the first (translating the
    juice-box analogy into abstract prose, then repeating general priority flattening
    under tangents). Compress in place by keeping the vivid juice-box contrast with
    a tighter attribution and caveat in the first bullet, and keeping only the short
    tangent phrase in the second with a single shared attribution.
  level: warn
- scope: passage
  quotes:
  - '- *Single-artifact workflow stops:* [ADR 138](../reference/adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md)
    unbundles the three decisions for unattended note revision—a run ends at its first
    stop with a typed continuation record, an operator''s answer to a stop can be
    recorded so the next run does not re-ask, and commissioning follow-up work such
    as a rewrite remains a separate decision.'
  reason: This example replays all three clauses of the unbundling just defined eight
    lines earlier (nearly repeating 'so the next run does not re-ask') and runs noticeably
    longer than its two sibling scale examples. It could be tightened into a compact
    parallel gloss of the three artifacts, though keeping the concrete mapping may
    help readers apply the split.
  level: info
contract: verdict
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/reviews/calls/launches/b5d3710818ec496f9eaa6b15b07bf671/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/reviews/artifact/reviews/fcde1dc8e403ed26147da9d2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/reviews/calls/launches/b5d3710818ec496f9eaa6b15b07bf671/outputs/review.md
raw-output-sha256: ca3e58091fdfa49333cac7027e336e95f963daafc6e4267fcd8a5df24641e3e9
---

# Review

Most of the note is tightly proportioned to its argument, with one clear source-quotation overhang and one minor example-detail overhang recorded in frontmatter.

The main imbalance sits in the first two failure-mode bullets, where practitioner quotation absorbs nearly half the causal section despite playing an illustrative rather than corroborative role. Retaining the vivid juice-box/bleeding-finger contrast and the brief tangent phrase preserves both grounding and memorability; dropping the redundant restatement quotes, duplicate citation links, and excess provenance wording restores proportion without weakening the point.

Several other details are non-obvious passes and should be kept as-is:

- The human-specialist contrast and the rebuttal to standing priority instructions in the first section are short and prevent the most obvious objections from landing.
- The three-decision unbundling list and the three-scale Commonplace example structure (mid-task noticing, workflow stops, cross-surface queueing) make the architectural split concrete and actionable rather than abstract.
- The three residual-friction bullets and the Scope section carry real boundary conditions and trade-offs that prevent overclaiming.
