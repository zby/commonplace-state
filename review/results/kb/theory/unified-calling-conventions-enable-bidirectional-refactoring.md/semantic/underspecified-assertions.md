---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 96c4eea5828c4089a10b19a54bdfd799
completed-at: '2026-11-20T09:44:59Z'
findings:
- scope: passage
  quotes:
  - if neural and symbolic components present the same interface, callers don't need
    to know which they're talking to
  reason: 'Unresolved choice: the scope of ''the same interface''. Reading A: the
    same name plus the same argument and return schema, and the same description shown
    to the LLM caller. Reading B: the same name and the same invocation mechanism
    (one namespace, callable as a function), while signatures and descriptions may
    differ between the agent and its replacement. Under A the claim that call sites
    and invoking prompts do not change holds by construction, but it requires every
    codification step to preserve the schema. Under B the claim is false whenever
    codification changes arguments or descriptions. The choice changes when the central
    claim is true and which evidence would support it. Nearby text (''The LLM sees
    both as callable functions'', ''implementation-agnostic interfaces'') does not
    settle it.'
  level: warn
- scope: passage
  quotes:
  - refactoring across the boundary becomes a local operation
  reason: '''Local'' could mean that only the component''s definition file changes,
    or that the change is confined to one link of the call chain, though tests, observability
    and callers'' expectations about behavior may still change. The later ''call site
    doesn''t change'' points toward the first reading, so the ambiguity is probably
    not material.'
  level: info
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/11d94fe4553252a25da14737/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/outputs/review-underspecified-assertions.md
raw-output-sha256: 7d4520e26a50c4c9401ff087e544711524101b1f29d1dda80509466ccba42cca
---

# Review

The load-bearing assertion is the opening mechanism: a shared interface means callers need not know whether a component is neural or symbolic. Everything downstream depends on what counts as "the same interface": the four-step progression with unchanged call sites, the routing-rule test run, and "each link can be independently refactored".

For an LLM caller, the interface plausibly includes the tool description and argument schema that the model sees. The note never says whether those must stay fixed when an agent is replaced by a function. The two readings differ in the conditions under which the claim holds, and in whether interface-changing codifications count as counterexamples.

The routing-rule example does pin part of the interface ("receive the same set of queue labels"), which shows the author has the stricter reading in mind for outputs. The general statement still leaves inputs and descriptions open.
