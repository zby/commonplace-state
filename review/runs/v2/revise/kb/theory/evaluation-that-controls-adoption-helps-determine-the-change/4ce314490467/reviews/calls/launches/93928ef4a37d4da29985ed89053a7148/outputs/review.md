---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "DOUBTFUL — Unstated premise, read as universal: for every process the note addresses, a specification exists, or can be reconstructed, that settles which human evaluation tasks are required. This premise lets the note sort a task as required, retired or optional. — Many agent and KB maintenance processes run on tacit norms with no written specification. Scope bullet 2 covers this case for habitual waits but not for habitual tasks. Suppose a maintainer has for months sampled adopted changes and rolled back bad ones, and no rule demands it. The note cannot then say whether stopping the practice 'retires a requirement' or merely 'ends an optional study'. An optional study can also drift into a tacit requirement when its findings routinely trigger rollbacks. Informal processes are common in the note's domain, so this is not a rare edge case. — LOCAL: the commitment survives if Scope says the task-side distinction applies where a specification exists or is made explicit, and that a habitual task needs the same treatment the note gives a habitual wait. — prevalence"
  - scope: passage
    quotes:
      - "Retiring an unnecessary review may be justified, but it is a change in requirements, not automation of that review."
    reason: "DOUBTFUL — Universal premise: a specified human task can disappear in only two ways, automation or retirement, so every full-automation claim can be split into 'performed automatically' and 'no longer required'. — Some changes fit neither category. In substitution, the weekly human sample review is replaced by metric-triggered automatic rollback, which serves the review's purpose by a different task. In partial automation, a machine triages and a human confirms only flagged changes. In the first case the requirement is reformulated, neither automated nor retired. In the second the task is split. Either way a reader applying the two-way split would mis-sort the change. — LOCAL: add substitution and partial automation as named cases, or say the two categories apply per requirement after it has been restated. — instance"
  - scope: document
    quotes: []
    reason: "DOUBTFUL — Unstated premise, read as universal: 'blocking dependency' and 'unfulfilled requirement' are disjoint, so each required human evaluation is either a wait or a non-blocking task. — Deferred or conditional blocking is both. Example: adoption proceeds now, but if the weekly review is not signed off within seven days, further adoptions pause. Other examples are an escalation rule that halts on an unreviewed backlog and a rate limit lifted only by review. The task is undone while execution continues, until it becomes a wait. A full-automation claim that lists such a review as merely a 'preserved task' would hide a dependency that will eventually block. — LOCAL: name conditional or deferred blocking in Scope, or classify a task by whether any execution path waits on it. — instance"
  - scope: passage
    quotes:
      - "The process depends on human intervention even if the maintainer always approves."
    reason: "HOLDS — Universal premise: a required approval stop is a dependency whatever its approval rate. — The hunt looked for a case where an always-approved stop is not a dependency. A rubber-stamp approval still halts execution while the maintainer is absent. The premise concerns structure, not outcome, so the approval rate cannot defeat it."
  - scope: passage
    quotes:
      - "A specified task can remain undone while execution continues."
    reason: "HOLDS — Possibility premise: some specified tasks do not block execution. — The note's own weekly-review example instantiates it, and post-hoc audits and monitoring duties in ordinary operations do too. The premise asserts only possibility, so no counterexample is available. The disjointness the note silently adds is attacked in a separate finding."
  - scope: passage
    quotes:
      - "A non-binding recommendation still creates a dependency if the agent must wait for it."
    reason: "HOLDS — Conditional universal premise: a wait creates a dependency whether or not the awaited input binds the decision. — The hunt looked for a non-binding input that the agent waits for without depending on it. The only candidate is a wait with a timeout default. That case is a bounded dependency, not a refutation."
  - scope: passage
    quotes:
      - "a program can apply human-authored acceptance rules without requiring a new human judgment for each change"
    reason: "HOLDS — Possibility premise: human-authored rules can gate changes without a per-change human judgment. — CI test suites and lint gates are ordinary instances. The premise does not say the rules stay adequate without human revision. Revision is a separate requirement, which the note handles."
  - scope: passage
    quotes:
      - "Calling the whole process automated would conceal an omitted task."
    reason: "HOLDS — Premise: a claim that the whole process is automated is read as covering its specified tasks, so leaving out an undone task misleads. — A possible counterexample is the common usage in which 'automated' means only the execution path. The note fences that usage explicitly ('A claim about automated adoption alone need not include monitoring or revision'), so the premise applies only to whole-process claims, where it holds."
  - scope: passage
    quotes:
      - "Using an optional study's available findings does not itself require future studies."
    reason: "HOLDS — Universal premise: consuming the findings of a past optional study does not turn future studies into requirements. — The hunt looked for consumption that creates a requirement. Each candidate, such as a rule saying 'revise only after the next study', makes the study a condition of revision. The next sentence of the note already sorts that case as a dependency."
  - scope: passage
    quotes:
      - "not by itself evidence that the system would fail or degrade without the task"
    reason: "HOLDS — Premise qualified by 'by itself': an unfulfilled requirement does not show that the task is needed. — Specifications routinely contain vestigial or precautionary tasks. The hedge already concedes cases where other evidence shows need, so no counterexample defeats the premise at its stated modality."
outcome: report
---

# Premise decomposition: Removing approval waits can leave required human evaluation in place

**Register:** claim
**Central commitment (one sentence):** Removing a human approval wait differs from removing a specified human evaluation task. Adoption can therefore run without a person while required human evaluation remains, and a full-automation claim must say which tasks it preserves and which requirements it retires.

## Premises and counterexamples

The title claim is modal ("can leave"), and the weekly-review example easily instantiates it. The weight therefore falls on the claim's normative half: the demand that a full-automation claim split its human tasks into preserved and retired. That demand consumes three things:

- a structural distinction between waits and non-blocking tasks;
- a reference point, the specification, that settles which tasks are required;
- a partition of how a required task can leave the process, by automation or by retirement.

The structural premises hold under an active hunt. A dependency is structural, so its approval rate does not affect it. A non-binding input that execution waits for is still a dependency. Human-authored rules can gate changes without per-change judgment.

The weak points are the three silent premises that make the classification usable. All three dents are local. None of them defeats the central distinction. Each one marks a case where a reader applying the distinction as stated would mis-sort a real process:

- a process with no written specification;
- a review replaced by a different mechanism;
- a review that is non-blocking until a deadline, after which it blocks.

Each can be repaired with a scope qualification or a named extra case.

## For the human

Look first at the unstated premise that a specification settles which tasks are required. Informal, tacit-norm processes are common in the note's domain. The note fences habitual waits but not habitual tasks.
