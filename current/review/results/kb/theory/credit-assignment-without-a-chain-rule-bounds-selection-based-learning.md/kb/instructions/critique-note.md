---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md
  against kb/instructions/critique-note.md
note: kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md
note-sha256: 445d4f9910c0a70b503081a3e06658de2e895f949e9930c9f7643aac8fa69e2f
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews
launch: 2bc57c4c16cd49d48fdad5ae338bceaa
completed-at: '2026-11-24T13:37:10Z'
findings:
- scope: passage
  quotes:
  - Replaying the failing case with a shortlisted entry withheld or modified verifies
    causal responsibility directly
  reason: The note treats replay as a direct causal check, but LLM execution is stochastic
    and the diffuse failures it names have small effect sizes. Each withheld-entry
    replay is therefore a statistical comparison whose sample cost grows with output
    variance and shrinks with effect size. That cost, not suspect count, is what the
    chain rule avoids, and the note does not price it. State that replay verifies
    causality only with a sample budget sized to variance and effect size, and say
    what the budget is when the failure is a quiet degradation rather than a reproducible
    crash.
- scope: passage
  quotes:
  - Without backpropagation's chain rule, attributing failures in a growing, interdependent
    store is a debugging problem
  reason: 'Credit assignment in a learning process also allocates positive and graded
    credit: which retained artifacts contribute to success, and which are marginal
    or dead weight. Debugging is triggered by an observed failure and localizes a
    discrete fault; it gives no signal when nothing fails but the store carries low-value
    or mildly harmful entries. Either scope the claim explicitly to failure attribution
    (blame) and name positive or marginal credit as a separate unsolved problem, or
    argue how debugging practice covers it.'
- scope: passage
  quotes:
  - engineers and coding agents routinely localize faults across hundreds of interdependent
    modules by **debugging**
  reason: 'Routine software debugging, and agentic debugging in particular, typically
    starts from a crisp failure oracle: a failing test, a crash or a reproducible
    issue. The readable-artifact note the article links says the KB case runs under
    softer oracles. The analogy therefore transfers the localization tools but not
    the oracle that makes them reliable. Name the oracle as a precondition and say
    what plays its role in a selection-based store.'
- scope: passage
  quotes:
  - over a modular store of hundreds or thousands of artifacts it gives a plausible
    path to fully automated credit assignment
  reason: The conclusion depends on the store staying modular, but the second Open
    Question leaves open whether an autonomous loop can keep it modular. The linked
    near-decomposability note is itself a conjecture that requires a worked case.
    'Plausible path' should be conditioned on that unresolved maintenance problem
    in the conclusion itself, rather than only in Open Questions.
- scope: passage
  quotes:
  - '[Near-decomposability](./near-decomposability-may-make-local-inspection-affordable.md)
    and explicit dependency links bound how many artifacts can interact.'
  reason: The linked note presents near-decomposability only as something that 'may
    make' local inspection affordable, and it treats the transfer to artifacts as
    unworked. This sentence states that it bounds the number of interacting artifacts.
    Under the note's own 'implicit coupling' property, declared links also cannot
    bound undeclared semantic interaction. Soften the sentence to a conditional, or
    limit the bound to declared dependencies.
contract: report
target-sha256: 445d4f9910c0a70b503081a3e06658de2e895f949e9930c9f7643aac8fa69e2f
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews/calls/launches/2bc57c4c16cd49d48fdad5ae338bceaa/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews/artifact/reviews/e5e30d6991a2a18b55926491/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews/calls/launches/2bc57c4c16cd49d48fdad5ae338bceaa/outputs/review.md
raw-output-sha256: 76adb813e62660718b4645bffc8fde018eb1584f2ef24100f26b040b7a39ee86
attack-outcome: partially lands
---

# Critique: Credit assignment without a chain rule is a debugging problem over an interdependent store

**Note:** kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md
**Central commitment:** Selection-based learning lacks a chain rule, but credit assignment over its store reduces to debugging, so a debuggable, modular store of hundreds or thousands of artifacts offers a plausible path to fully automated credit assignment.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is someone trained in reinforcement learning or experimental statistics. They hold that credit assignment is counterfactual estimation: how much would the outcome change if this component were different? The chain rule matters not because it finds a culprit but because it computes every component's marginal contribution from one forward and one backward pass. Without it, each component's contribution must be estimated by intervention. The cost of an intervention depends on how noisy the outcome is and how large the effect is.

On this view, the software analogy borrows its tractability from two properties that the store lacks:

1. **A deterministic, crisp oracle.** Software debugging starts from a failing test or crash. A replay reproduces the same failure, and one run with a suspect removed is decisive. Coding agents' debugging success is likewise measured on tasks that come with a reproducing test. In the store, the model's execution is stochastic. The note itself says failures can "quietly degrade unrelated tasks" rather than crash. Every "replay with a shortlisted entry withheld" is then an A/B comparison. Detecting a small degradation reliably needs many samples per suspect, and the number of required samples rises as the effect gets smaller. Combinations of suspects multiply the cost. The diffuse failures that the note calls hardest are exactly those with the smallest effects. Its third difference, "noisier, diffuse failures," therefore does more than make debugging noisier. It breaks the verification step that the whole argument rests on.
2. **Failure as the only signal.** Learning needs credit for success and graded contribution as well as blame for faults. A selection-based learner must decide which retained artifacts are worth keeping, which helped, and which are dead weight inflating context. Debugging has nothing to say until something visibly fails. A debugging frame can localize discrete faults while leaving most of the credit-assignment problem, which is graded marginal value, untouched.

The objection concludes that "a debugging problem" changes the vocabulary without changing the difficulty. Without crisp oracles, the scaling bottleneck is sample complexity of counterfactual estimation, not suspect narrowing. Debuggability shrinks the suspect list. It does not make each check cheap. So the step from "debuggable" to "plausible path to fully automated credit assignment" is unsupported.

## How the note engages it

**Partially engaged.**

- The note concedes the noise. "Noisier, diffuse failures" says reproduction and bisect-style isolation become "noisier than a failing unit test." The conclusion concedes that debugging "will not match backpropagation's scale." Its distinction between "cheap suspect narrowing" and "targeted causal checks" is the correct structure for answering the objection. Narrowing really does reduce how many expensive checks are run.
- The note does not price the targeted check. It says replay "verifies causal responsibility directly," which assumes deterministic reproduction. Nothing in it addresses sample budgets, variance or effect size. Codifying rules into scripts ("moves them back into ordinary software debugging") answers the objection only for the codified portion.
- The note does not engage the positive or graded half of credit assignment. Its description and body narrow credit assignment to "attributing failures," and the Scope section never marks that as a narrowing. A reader could take the title as covering credit assignment in the learning-theory sense.
- The oracle question is not addressed. The linked readable-artifact note names "softer oracles" as the main missing piece, but this note does not connect that gap to the debugging analogy.

The objection therefore lands on the conclusion's strength ("plausible path to fully automated"), not on the core reframing. Treating blame attribution in a store as a debugging problem that becomes cheaper with traces, dependency links and addressable premises survives. Calling the resulting credit assignment scalable to full automation does not survive without a cost account of stochastic verification.

## Constructive findings

- Add an explicit condition to the replay step. A withheld-entry replay is a statistical test whose cost grows as variance rises and as effect size shrinks. Say how the approach handles quiet degradations, for example by escalating only to suspects that pass a cheap screen, by using fixed replay fixtures with pinned sampling, or by codifying the steps that need verification.
- Scope "credit assignment" to failure attribution in the Scope section, and name positive or marginal credit (what to keep, what is dead weight) as a separate open problem. Alternatively, argue how debugging-style tools reach it, for example periodic ablation of low-use entries.
- Name a crisp failure oracle as a precondition of the software analogy, and say what supplies it in a selection-based store: tests, validators, stated predictions of an addressable theory, or pinned replay fixtures.
- Condition the conclusion on the store staying modular and on verification being affordable. The open question about autonomous maintenance of modularity carries weight in the argument and should appear in the conclusion's own sentence.

## Secondary objections (optional)

- "[Near-decomposability] and explicit dependency links bound how many artifacts can interact" overstates the linked note, which is a conjecture that "may make" inspection affordable and calls for a worked case. Under the note's own "implicit coupling" property, declared links cannot bound undeclared semantic interactions.
- Execution traces narrow suspects to the loaded slice, but two failure kinds escape that slice. Failures of omission involve a missing or unretrieved artifact. Failures of volume involve context saturation caused by the aggregate size of the slice rather than any one entry. Neither has a single suspect inside the active slice.
- "Far less scalable than gradient learning" is asserted rather than argued. The comparison basis (number of components, cost per attribution, or wall-clock time) is unnamed.
