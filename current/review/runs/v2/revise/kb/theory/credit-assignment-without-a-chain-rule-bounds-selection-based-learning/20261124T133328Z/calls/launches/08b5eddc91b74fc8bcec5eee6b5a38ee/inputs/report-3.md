---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md
  against kb/instructions/premise-decomposition-gate.md
note: kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md
note-sha256: 445d4f9910c0a70b503081a3e06658de2e895f949e9930c9f7643aac8fa69e2f
criterion: kb/instructions/premise-decomposition-gate.md
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews
launch: 1b99120541284fb7bfd35130512a2685
completed-at: '2026-11-24T13:39:14Z'
findings:
- scope: passage
  quotes:
  - engineers and coding agents routinely localize faults across hundreds of interdependent
    modules
  reason: 'DOUBTFUL — premise (unqualified, so universal): fault localization across
    large interdependent codebases is routine for both engineers and coding agents,
    so lacking a chain rule does not block full automation — for engineers this holds,
    but coding agents usually start from a supplied failing test or issue and still
    fail a substantial share of repository-level localization tasks; the evidence
    supports assisted debugging, not routine autonomous localization, which is what
    the closing claim of a path to fully automated credit assignment consumes. Repair:
    weaken the automation clause or cite agent localization evidence — LOCAL — prevalence'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — unstated premise (universal): the faults to localize are commissions
    by retained artifacts, so traces of what loaded and replay with an entry withheld
    can find them — many failures come from omissions (a needed rule or note was never
    written or was not retrieved) or from base-model error with no store entry at
    fault; a trace of loaded artifacts cannot point at what was absent, and withholding
    entries cannot reveal a missing one. The debugging framing survives if omission
    and retrieval faults are named as a separate case — LOCAL — instance'
- scope: passage
  quotes:
  - Replaying the failing case with a shortlisted entry withheld or modified verifies
    causal responsibility directly
  reason: 'DOUBTFUL — premise (universal): single-entry withhold-and-replay verifies
    causal responsibility directly — the note''s own third property (noisy, diffuse
    failures under stochastic decoding) means one replay neither confirms nor refutes;
    verification needs repeated sampling with a success-rate comparison. Removing
    text also changes context length and framing nonspecifically, and a conjunctive
    cause (the note''s own combination of edits) is missed when entries are withheld
    one at a time. Statistical replay preserves the mechanism at higher cost — LOCAL
    — instance'
- scope: passage
  quotes:
  - explicit dependency links bound how many artifacts can interact
  reason: 'DOUBTFUL — premise (universal): explicit links and near-decomposability
    bound the interacting set — the note''s second property says prose conventions
    interact semantically without any explicit link, so declared links bound only
    the declared interactions; the implicit coupling that makes the store harder than
    software is exactly what they leave unbounded. Needs a condition such as links
    being enforced or coupling being detected, not only declared — LOCAL — instance'
- scope: passage
  quotes:
  - narrow suspects from the whole store to the active slice
  reason: 'DOUBTFUL — premise (universal): load traces narrow suspects meaningfully
    — in common agent setups a large always-loaded core (project instructions, routing
    tables, type specs) appears in every trace, so the active slice for any failure
    includes the most coupled artifacts and narrowing is weakest where coupling is
    highest. Holds for retrieved, task-specific entries; needs that scope condition
    — LOCAL — instance'
- scope: passage
  quotes:
  - a failed prediction names a specific premise to check
  reason: 'DOUBTFUL — premise (universal): a failed prediction of an addressable theory
    names a specific premise — by the Duhem–Quine point a failed prediction refutes
    the conjunction of the theory''s premises with auxiliary assumptions (here including
    the model''s interpretation of the prose), so it yields a suspect set rather than
    one premise. It still narrows suspects, which is all the mechanism needs if reworded
    — LOCAL — instance'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — unstated premise (universal): failures surface as observed,
    reproducible failing cases that debugging can start from — the note''s diffuse
    failures (quiet degradation of unrelated tasks) often produce no single failing
    case and may go unnoticed without a regression suite or outcome monitoring; debugging
    needs a detection oracle that the note does not list among the debuggability requirements.
    Adding evaluation fixtures as a requirement repairs it — LOCAL — instance'
- scope: passage
  quotes:
  - Exhaustive one-by-one ablation verifies causality cleanly on small stores, but
    becomes prohibitively expensive once hundreds of artifacts interact
  reason: 'DOUBTFUL — premise (universal): exhaustive ablation becomes prohibitively
    expensive at hundreds of artifacts — delta debugging (adaptive bisection over
    subsets) finds a single culprit in logarithmically many replays, and hundreds
    of model replays are often affordable; cost becomes prohibitive mainly through
    stochastic repetition and interaction effects. The premise motivates debuggability
    investment, so overstating it only weakens that motivation — LOCAL — instance'
- scope: passage
  quotes:
  - recording which files loaded does not prove which sentence steered the decision
  reason: 'HOLDS — premise (universal): a record of loaded context does not establish
    which content caused a decision — no counterexample found; attention and self-reported
    rationale are not faithful causal attribution, and the linked faithfulness note
    supports this.'
- scope: passage
  quotes:
  - codifying settled rules into deterministic scripts moves them back into ordinary
    software debugging
  reason: 'HOLDS — premise (universal): a rule moved into deterministic code is debuggable
    with ordinary software tools — the hunt found only the boundary where the script
    hands residual cases to model judgment, which the note already places in the prose
    side.'
- scope: passage
  quotes:
  - backpropagation applies the chain rule to compute how each parameter contributed
    to a loss
  reason: 'HOLDS — premise (universal): backpropagation gives per-parameter credit
    in one backward pass across tightly coupled weights — gradients are local sensitivities
    rather than global contributions, but the contrast the note draws (a scalable,
    compositional attribution rule that the store lacks) holds.'
contract: report
target-sha256: 445d4f9910c0a70b503081a3e06658de2e895f949e9930c9f7643aac8fa69e2f
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews/calls/launches/1b99120541284fb7bfd35130512a2685/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews/artifact/reviews/49a15ce2bb3d1d7e5725e520/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews/calls/launches/1b99120541284fb7bfd35130512a2685/outputs/review.md
raw-output-sha256: a4a7cea3b455e5a1cad0c1e5f235152a1d21e59c99e9618c119825a0d28daa21
---

# Premise decomposition: credit assignment as debugging over an interdependent store

**Register:** claim
**Central commitment (one sentence):** Credit assignment in selection-based learning over a growing, interdependent store lacks a chain rule but is a debugging problem: harder than software debugging because of softer traces, implicit coupling and diffuse failures, yet plausibly fully automatable over hundreds or thousands of artifacts if the store is made debuggable.

## Premises and counterexamples

The commitment has three parts, and each consumes premises. The **analogy** says software debugging shows that credit assignment without a chain rule can scale. It consumes the backprop contrast and the premise that agents debug large codebases routinely. The **difference** says the store weakens software's debugging tools. It consumes the softer-traces premise. The other two properties are the note's own concessions and are used against its remedies below. The **remedy** says debuggability restores tractability. It consumes four premises: load traces narrow suspects, explicit links bound interaction, failed predictions name a premise, and withhold-and-replay verifies causation. It also needs two unstated premises: faults are commissions by stored artifacts, and failures arrive as reproducible cases.

The dented premises fall mainly on the remedy side. Several remedies are undercut by the note's own three properties. Implicit coupling escapes explicit links. Noisy failures defeat single-replay verification and go undetected without an oracle. Always-loaded context blunts trace narrowing. None of these breaks the core mechanism, because statistical replay, enforced coupling checks and regression fixtures keep the debugging frame intact at higher cost. Every failure is therefore routed LOCAL. The analogy premise carries the most weight. If coding agents do not yet localize faults autonomously and routinely, the "fully automated" clause is no longer supported. The narrower claim that credit assignment is a debugging problem still stands.

## For the human

Look first at the claim that coding agents routinely localize faults: it alone carries the "fully automated" conclusion. Next, add omission faults (missing or unretrieved entries), which traces and withhold-replay cannot find.
