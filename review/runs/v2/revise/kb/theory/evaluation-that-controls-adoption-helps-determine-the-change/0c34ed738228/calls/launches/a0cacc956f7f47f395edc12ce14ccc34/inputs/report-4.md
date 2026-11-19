---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/synthesis
launch: 8367541968e04f369e6dfdd734bcd4b6
completed-at: '2026-11-17T07:24:15Z'
findings:
- scope: document
  quotes: []
  reason: 'The Scope section spends two of its three bullets on material that either
    repeats an earlier boundary or opens a separate mechanism: the first bullet restates
    the cases section''s rollback boundary less concretely, and the third bullet''s
    last sentence adds test optimization by the proposer (a different failure mechanism)
    and closes on a clause its own opening already entails. Together they dilute the
    section''s one distinctive boundary, the learner-boundary point that motivates
    the open question; a revision could cut the first bullet (folding ''other influence''
    into the earlier rollback sentence if wanted) and end the third bullet at ''Approval
    does not establish quality'' plus its harmful-revision example, rehoming the test-gaming
    point if the author wants it kept.'
- scope: passage
  quotes:
  - Adoption here means entering a live behavioral path on which later operation depends
  reason: The claim's key term is defined only at the end of the second section, after
    the opening claim and both cases already depend on it, while the second paragraph
    spends two sentences restating the opening contrast with 'human' added; a revision
    could rebuild the opening as claim, definition of adoption, and the use (attributing
    a system's improvement), letting the worked cases carry the contrast instead of
    the human-specific restatement.
contract: report
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/synthesis/artifact/reviews/07864812686aeab1939e0320/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/synthesis/artifact/reviews/07864812686aeab1939e0320/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/synthesis/calls/launches/8367541968e04f369e6dfdd734bcd4b6/outputs/review.md
raw-output-sha256: a05a310f0e6ad6df10e068894c2910229e832cbe62650a00bb47eb7d92202a38
---

# Simplification synthesis: Evaluation that controls adoption helps determine the change

The note's core claim is easy to find, and its two worked cases and the "one episode" section do distinct work. The gate findings cluster in two places: the Scope section and the order of the opening. Each cluster is small locally. Taken together, each one changes how cleanly the argument reads.

## Opportunities

### 1. Reduce Scope to the boundaries only it supplies

- Location: `## Scope`, first bullet ("This distinction concerns the causal role of a particular judgment…") and third bullet's final sentence ("A test available to the proposing system can be optimized … human approval does not remove the need to justify the assessment.")
- Reader problem: Of the three bullets, only the second bounds the claim in a way the body does not already cover. The first repeats the rollback boundary from the cases section in more abstract form. The third ends by introducing a Goodhart-style mechanism the note neither defends nor needs, then closes by restating its own opening. The reader's attention moves from the causal role of a judgment to the validity of an evaluation.
- Direction: Delete the first bullet, or fold "other influence" into the sentence "The later assessment could still cause a future revision or a rollback." End the third bullet after the harmful-revision example. One possible resolution: "Approval does not establish quality. An evaluator can select a harmful revision, just as a later assessment can misjudge its effects."
- Combines: branch-bloat (warn, test-optimization sentence); detail-overhang (info, same sentence); marginal-value-redundancy (warn, first Scope bullet; warn, trailing "human approval does not remove…" clause).
- Preserve or decide: The author must decide whether the test-optimization caveat matters to this note. If it does, its tie to the selection/assessment distinction needs to be made explicit. If it does not, it should be rehomed in a note on test gaming or evaluator independence rather than dropped silently. Keep the second bullet intact: it carries the learner-boundary condition, and the open question depends on it.

### 2. Define adoption at the start and let the cases carry the contrast

- Location: Opening two paragraphs, plus the definition sentence at the end of `## One episode can contain both roles` ("Adoption here means entering a live behavioral path on which later operation depends…")
- Reader problem: The claim turns on "enters use" and "adoption", but the note defines adoption only after the claim and both cases have relied on it. In the second paragraph, "A human approval required for adoption…" and "A later human assessment…" restate the opening contrast and narrow it to humans. The first paragraph has just said that the role does not depend on whether a person or a program judges.
- Direction: Order the opening as the claim, then a one-sentence definition of adoption that links to operative change, then the use: deciding whose contributions explain a system's improvement. The two human-specific sentences could go, since the approval case already shows a human approval selecting the instruction. The sentence about a never-adopted proposal could stay with the definition or remain where it is.
- Combines: core-claim-obscured (info, late definition); marginal-value-redundancy (info, human-specific restatement).
- Preserve or decide: Keep the operative-change link. The author should decide whether the human emphasis is deliberate. The supplement line and the open question about externally supplied judgments suggest that the paired note may need human approval named in particular. If so, keep one sentence that says so as an application, not as a second statement of the claim.
