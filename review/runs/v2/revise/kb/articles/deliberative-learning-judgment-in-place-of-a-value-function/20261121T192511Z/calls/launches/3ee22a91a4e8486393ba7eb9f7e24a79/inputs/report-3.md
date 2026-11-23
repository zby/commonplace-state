---
type: types/review-result.md
format: 2
description: Retained report review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/premise-decomposition-gate.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
criterion: kb/instructions/premise-decomposition-gate.md
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: 9cd5352c31464ac987f4c3f9aae1e8ec
completed-at: '2026-11-21T19:31:51Z'
findings:
- scope: passage
  quotes:
  - an on-balance judgment played the role a scalar loss or value function plays in
    weight training
  reason: 'DOUBTFUL — Universal (no stated mode): the judge occupies the same role
    a scalar loss or value function occupies in weight training. — In gradient training
    the loss does not accept or reject updates. It generates the update direction
    for every parameter, so it does the search work as well as the evaluation. In
    the article''s loop the proposer generates the edit and the judge only admits
    or rejects it. That role matches a fitness function in evolutionary search, a
    validation-set acceptance test or early stopping, and those are not what the title''s
    "value function" names. The routing-line example shows it: the judge never produced
    the routing line or the narrowing. A judgment could be good at admission and still
    provide none of the dense, per-entry directional signal that makes a loss powerful.
    — LOCAL: recast the slot as a selection or acceptance criterion and say what directional
    work the proposer does. The paradigm''s mechanism survives. — instance'
- scope: passage
  quotes:
  - Looking at three precedents shows that the bottleneck was always
  reason: 'DOUBTFUL — Universal ("always"): in the precedents, the bottleneck was
    what played the value-function role. An unstated corollary is that the proposer
    and the representation were not bottlenecks, so the novelty lies in the judge.
    — The article itself says EURISKO''s "symbolic heuristics remained brittle and
    repeatedly needed Lenat". Brittle stored content is a failure of representation
    or proposal, not of the gate. PRODIGY''s utility problem came from EBL generating
    rules whose match cost swamped their benefit, which is a problem on the proposal
    side that the formula only filtered. Language models are also new proposers of
    prose and code edits. So gains the bet credits to the judge could come from the
    proposer. — LOCAL: name the judge as one bottleneck among others, or argue why
    the proposer is not limiting. The bet can stay. — instance'
- scope: passage
  quotes:
  - Every machine learning loop needs two things
  reason: 'DOUBTFUL — Universal: every machine learning loop needs a modifiable substrate
    plus a selection signal that decides which updates stay. — Hebbian and other local-rule
    learning, and the article''s own "direct input-driven updates" such as a nightly
    click-ranking job, apply updates without any signal that decides which updates
    stay. The article treats the second of these as learning that fails only the deliberative
    condition. Even gradient descent has no keep-or-discard decision per update. The
    framing makes "judgment replaces the value function" look like a slot substitution
    when the slots differ. — LOCAL: restrict the frame to selection-based loops, or
    restate it as substrate plus update rule. — instance'
- scope: passage
  quotes:
  - Deployment time, taking effect on the next task that reads the store
  reason: 'DOUBTFUL — Definitional: the two stated conditions (legible, addressable
    store; rejectable decision in the loop) mark a paradigm distinct from weight training,
    and the side-by-side table''s axes follow from those conditions. — Decision-tree
    induction with reduced-error pruning on a validation set satisfies both conditions.
    The tree is readable and addressable, it is consumed by later prediction, and
    each split or prune is proposed and then rejected or kept by a fixed criterion.
    Genetic programming and FunSearch-style program search with a scalar evaluator
    satisfy them too. Yet these run at training time with no trace-based credit assignment,
    so the table''s "Deployment time" and "Inspecting traces" rows are not entailed
    by the definition. The boundary over-includes classical ML relative to the contrast
    the table draws. — LOCAL: mark the table as describing the intended deployed instance,
    or add a condition. — instance'
- scope: passage
  quotes:
  - a change is an improvement on balance when every reasonable measure of the declared
    work
  reason: 'DOUBTFUL — Universal standard: on-balance judgment decides edits by asking
    whether every reasonable measure defensible from the purpose favors the change.
    — Almost every additive edit to an always-loaded instruction carries the diffuse
    context cost the routing example names. Some defensible measure that weights context
    load or rare long-task failures will therefore disfavor most additions. Unanimity
    will rarely be reached, and most admissions will fall to the bounded-decision
    fallback (reversibility), as the article''s own worked example does. If so, the
    operative selector is a reversibility-weighted risk decision, not the unanimity
    standard the title advertises. Which measures count as "reasonable" is itself
    an unbounded judgment. — LOCAL: state that most admissions are decisions under
    open verdicts, and say how the set of reasonable measures is bounded. — prevalence'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — Unstated, universal: a fixed-weight language model judge''s
    errors are sufficiently independent of the proposer''s that judging filters what
    proposing gets wrong. — When proposer and judge are the same or similar models,
    self-preference and shared-blind-spot effects in LLM-as-judge setups are widely
    reported. A plausible-but-wrong edit that the proposer generates is the kind the
    judge is most likely to approve. The listed hazard "judgment reliability" treats
    errors as independent misses, not as errors correlated with generation. — LOCAL:
    add a judge-independence condition (different model, execution evidence or held-out
    tests) to the bet. — prevalence'
- scope: passage
  quotes:
  - recognize when an existing gate, validator, or review criterion is misleading
    and revise it
  reason: 'DOUBTFUL — Universal: the system can revise its own working criteria while
    the declared objective stays fixed, so criterion revision tracks the objective.
    — The declared objective is prose and is interpreted by the same judge that revises
    the gates. A system whose proposals keep failing a gate can judge that gate "misleading"
    and relax it. That is Goodhart drift through criterion revision, and it is hard
    to detect from inside because the relaxed gate now admits the proposals as improvements.
    The article''s example only shows tightening. The linked note licenses objective
    revision from outside, but nothing outside checks revisions of the working criteria.
    — LOCAL: require an outside or held-out check on criterion revisions, especially
    relaxations. — instance'
- scope: passage
  quotes:
  - Additional compute buys more candidate proposals, richer execution traces
  reason: 'DOUBTFUL — Universal: compatibility with the Bitter Lesson holds because
    additional compute buys better proposals, criticism and criteria. Being produced
    by computation is necessary, and so is outcomes improving as compute grows. —
    The cited harness-evolution study is an instance of an automated loop that stalled
    as compute was added. The article reinterprets the cause, but the reinterpretation
    shows that more compute did not by itself buy improvement; what the proposer was
    shown also decided the outcome. Production method settles which side of the Bitter
    Lesson a method is on only if the method also keeps scaling. — LOCAL: state scaling
    as part of the empirical bet, not as a consequence of placing an LLM in the loop.
    — instance'
- scope: passage
  quotes:
  - an addressable store lets later rounds point at the faulty line and fix it without
    wiping out unrelated work
  reason: 'DOUBTFUL — Universal: addressability gives targeted correction, so fixing
    one entry leaves unrelated work intact. — A language model consumes the store
    as context, and output on unrelated tasks is known to shift with small changes
    to prompt wording, formatting and ordering. Editing or removing one line of an
    always-loaded instruction can therefore change behaviour on tasks the line was
    never about. Addressability locates the edit, not its effects. The article concedes
    rule interactions under accretion but states the correction payoff without that
    qualification. — LOCAL: say that edit locality is not effect locality, and that
    targeted fixes still need regression checks. — prevalence'
- scope: passage
  quotes:
  - than with that change taken out (leaving unrelated later edits intact)
  reason: 'DOUBTFUL — Definitional: the "learned" verdict is well-defined as the system
    with versus without one change, holding unrelated later edits fixed. — In the
    article''s own example, the narrowing edit rewrites the routing line, and the
    review-check revision was prompted by over-broad routing rules. Removing the original
    routing line leaves the narrowing with nothing to apply to, and whether the check
    revision counts as "unrelated" is undetermined. For dependent edit chains, which
    are the article''s model of correction, the counterfactual either collapses the
    chain into one unit or is ill-defined. The operative-dependence test inherits
    this problem. — LOCAL: specify how dependent later edits are treated in the counterfactual.
    — instance'
- scope: passage
  quotes:
  - the bet fails—and weights-only continual learning wins those domains
  reason: 'DOUBTFUL — Universal: if automated LLM judgment cannot keep its error costs
    below its gains, weights-only continual learning wins. — Other outcomes remain:
    deliberative learning with fixed-criterion or execution-based judges (FunSearch-style
    scalar evaluators, test suites), human-judged deliberative loops, or hybrids that
    distil artifact gains into weights. The cited harness-evolution study reports
    one such hybrid, where a lessons file was trained into an adapter. Failure of
    the LLM-judge bet does not decide between the remaining alternatives. — LOCAL:
    name the alternatives that a failed bet leaves open. — instance'
- scope: passage
  quotes:
  - it says nothing about whether the retained result must live in floating-point
    weights
  reason: 'HOLDS — Universal: the Bitter Lesson essay contrasts human-supplied knowledge
    with methods that leverage computation, and it does not prescribe the representational
    form of the result. — The hunt found no passage in the essay restricting the result
    to weights. Its examples (search in chess and Go, learning in speech and vision)
    are framed by method. The article correctly separates the Sutton–Javed weights
    view as a rival hypothesis rather than a reading of the essay.'
- scope: passage
  quotes:
  - the system adapted across tasks at deployment time without changing a single model
    weight
  reason: 'HOLDS — Universal: a deployed system whose retained artifacts change can
    adapt across tasks with fixed model weights. — No defeater found. Retained instruction
    edits change later behaviour whenever the model consumes them, and the article
    separately requires operative dependence, which covers the case where loaded content
    is ignored.'
contract: report
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/9cd5352c31464ac987f4c3f9aae1e8ec/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/99574766717cda5bbbf8ab73/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/9cd5352c31464ac987f4c3f9aae1e8ec/outputs/review.md
raw-output-sha256: 2526541dee2315e6972bf7f39eecb2422b24c0c01315f17bcb1e867c7fac0e74
---

# Premise decomposition: Deliberative Learning: Judgment in Place of a Value Function

**Register:** claim
**Central commitment (one sentence):** Deliberative learning (rejectable edits to a readable, addressable store) is a distinct learning paradigm in which an on-balance judgment does the work a value function does in weight training; putting a fixed-weight language model in that judge slot is bet to make it an automated machine learning paradigm that learns at deployment time and scales with compute, compatible with the Bitter Lesson.

## Premises and counterexamples

The commitment has two levels, and the premises split along them.

The paradigm level consumes three things:

- a framing that every learning loop has a substrate slot and a selection-signal slot;
- a role equivalence: an admission judgment fills the slot a loss or value function fills;
- a boundary claim: the two defining conditions mark something distinct from weight training, with the payoffs the comparison table lists.

The judgment itself also rests on an operating standard: unanimity across reasonable measures, with a reversibility fallback. The correction payoff rests on an assumption that addressable edits have local effects.

The bet level consumes four things:

- a historical premise: the judge was the bottleneck in earlier systems, so the novelty lies there rather than in the proposer;
- an unstated independence premise: an LLM judge filters what an LLM proposer gets wrong;
- a premise that criterion revision under a fixed prose objective tracks that objective;
- a premise that adding compute keeps buying improvement, which compatibility with the Bitter Lesson needs.

The evaluation section consumes a counterfactual definition of "learned" and a two-way framing of what a failed bet concedes.

No counterexample breaks the core mechanism. The most important dents are the role equivalence and the bottleneck attribution. Both bear on the title's framing and on where the bet places its novelty. Both can be repaired by rewording the slot as an acceptance criterion and by crediting the proposer. The Bitter Lesson reading and the deployment-time adaptation claim survived the hunt.

## For the human

Look first at the role-equivalence premise. An admission gate over proposed edits is not doing what a loss does in gradient training. Decide whether "in place of a value function" should become "in place of a selection criterion", because the title and the bet's novelty claim both rest on that slot.
