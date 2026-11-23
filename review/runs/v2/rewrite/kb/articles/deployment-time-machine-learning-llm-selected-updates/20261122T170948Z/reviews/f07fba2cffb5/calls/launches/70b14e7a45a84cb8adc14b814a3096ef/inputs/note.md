---
description: "Lead article: how a deployed agent can select edits to its instructions without a single score; the bet that a fixed-weight LLM can build the preference model and make the robust comparison; weight-training contrast, Bitter Lesson, empirical test"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/theory/definitions/software-house.md
  - kb/theory/definitions/self-improving-system.md
  - kb/theory/definitions/selection-based-learning.md
  - kb/theory/definitions/single-loop-and-double-loop-learning.md
  - kb/theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/theory/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/theory/retained-theories-may-improve-sample-efficiency.md
  - kb/theory/definitions/addressable-theory.md
  - kb/theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md
---

# Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

A software house that improves a client's program has a development
capability: it can find candidate fixes, test them, choose one and ship it.
If the house turns that capability on how it does its own next job—searching
for, judging, installing and keeping changes to its own methods—it has a
learning loop. This article makes one empirical bet and two conditional
arguments about such a loop. The bet is that a large language model (LLM) can
make the needed choices, and help find the candidates, well enough that later
work improves without a person judging each edit. If the bet holds, a fully
automated loop may scale with computation. A stronger, more research-like
design may also need fewer new observations and give bounded explanations of
what it learned.

## One failure, two repairs

Take a hypothetical software house that maintains build pipelines for several
clients. Its test-selection workflow skips the build tests for edits it
classifies as documentation-only. One such edit changes a client's README, and
the client's build breaks: the packaging step reads that README to generate
the package description.

**The first repair fixes the product.** The house diagnoses the failure, adds
a test that builds the package, ships the fix and closes the report. The
client's software is better. The house is not: its test-selection rule is
unchanged, so the same kind of edit for another client will skip the same
tests. Fixing an external work product is not by itself evidence that the
producer learned.

**The second repair makes the house its own client.** The failure is now
evidence about the house's workflow, and the same capability goes to work on
it. Search produces candidate remedies:

- run every test on every edit;
- add an exception for this one file;
- before classifying an edit, inspect which files the build reads, and treat
  any file it reads as code;
- leave the workflow unchanged.

Search also produces tests that discriminate among these candidates. For
example, the house can replay last quarter's edits under each rule and count
which failures each would have caught.

Selection then compares the candidates on missed failures against cost.
Running every test catches everything but multiplies compute and latency on
every job. The file exception is cheap but catches nothing new. Dependency
inspection costs one analysis per edit. The judge can investigate the facts
these trade-offs depend on: how often documentation files feed builds across
clients, and what a full test run costs. It can reject every candidate, or try
a variant on trial with a scheduled review. Suppose it installs dependency
inspection on trial.

No single score was needed. Missed failures and compute fall on different
jobs and clients, and the comparison only had to decide among the four
candidates it actually had. Choosing a candidate is also not proof that it
helps. The choice is a decision made on current evidence.

Weeks later, on another client's job, an edit changes a changelog that the
release script includes in its archive. The old rule would have classified
the edit as documentation and skipped the build tests. The retained method
finds the dependency, runs the tests and catches a broken release. The later
job was causally changed by the selected method, not merely accompanied by a
record of it. The check is to rerun the same job with and without the
retained method and see whether the outcome differs. No model weights changed;
what the house keeps for later work did.

## What closes the loop

The second repair has the structure of
[selection-based learning](../theory/definitions/selection-based-learning.md):
a change to what the system retains for later work is proposed, evaluated and
can be rejected. Because the house does the selecting itself and the selected
method changes its own subsequent jobs, it is a
[self-improving system](../theory/definitions/self-improving-system.md) for
this class of changes.

The boundary matters for the claim of automation. Client requirements, bug
reports and acceptance decisions come from outside the
[software house](../theory/definitions/software-house.md); depending on them
does not make the loop human-assisted. The loop is human-assisted only if
people make the internal decisions at issue: which remedies to consider, how
to diagnose the failure, which candidate to install.

Two criteria must be kept apart. The client's test rule decides which tests a
client edit gets. The house also has a criterion for adopting revisions to its
own workflow, such as "adopt a revision if replay shows it catches the
observed failure at acceptable added cost." Editing the test-selection
workflow under that fixed adoption criterion is a self-edit of a procedure.
Suppose instead that several revisions pass replay and then prove too costly
across all clients. If the house then changes the adoption criterion itself,
for example to require a cost estimate across every client before adoption,
it has revised how it judges future self-edits. That is
[double-loop learning](../theory/definitions/single-loop-and-double-loop-learning.md),
a further capability, not a requirement for the basic loop.

Whether the loop helps is an empirical question. Compare the learning house
with a credible baseline, such as the original rule or running every test,
over further work it has not yet seen. Count compute, review time and the cost
of rolling back bad revisions, as well as failures caught.
[Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md)
sets out such comparisons.

## The bet

The bet is that an LLM can do the selection—comparing remedies, finding the
facts that decide between them, rejecting weak candidates—and can help
generate candidates and discriminating tests, reliably enough that later work
improves without per-edit human judgment.
[Can an LLM Judge Which Changes Are Worth Making?](./can-an-llm-judge-which-changes-are-worth-making.md)
develops the judgment side: what evidence the judge needs and how to tell a
robust comparison from a plausible one. The two arguments below are
conditional on the bet.

## First argument: the loop can sit on the compute side of the Bitter Lesson

Rich Sutton's Bitter Lesson is that general methods using computation beat
methods built on researchers' domain knowledge: "The two methods that seem to
scale arbitrarily in this way are search and learning"
([Sutton](../sources/sutton-the-bitter-lesson-original-essay.ingest.md),
verbatim). An objection follows quickly: a house editing its own prose and
scripts looks like hand-crafted knowledge.

The lesson contrasts how knowledge is produced, not
[how it is represented](../theory/the-bitter-lesson-selects-production-methods-not-representational.md).
Computation can produce code and prose as well as weights. Reading the lesson
this way is an interpretation; Sutton's own essay does not address
representation, and in later work he argues for continual weight updates.

The loop is compatible with the lesson only on one condition: additional
computation does the domain-specific discovery and selection. In the example,
that means finding the dependency diagnosis, generating the replay test and
reaching the verdict, rather than a person supplying each decisive step.
Unattended scripts do not meet the condition by themselves. A script that
runs unattended but encodes a person's diagnosis of each failure mode is still
hand-supplied knowledge. A system that starts from hand-written methods fits
the lesson
[only if its learning outgrows that starting point](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
Whether results actually improve as more compute is spent has to be measured.

## Second argument: retained hypotheses may buy sample efficiency and explanation

The basic loop needs only winning patches: the house keeps "inspect build
dependencies" because it won. A stronger design also keeps a revisable
hypothesis with its predictions, evidence and tests. For example: "a file the
build reads behaves as code for testing purposes; the build's configured
input list names every such file." That hypothesis predicts which future edits
need build tests, cites the README failure as evidence, and names the replay
test that checks it.

The hypothesis changes the next inquiry. Suppose a later failure comes from a
snippet that the build reaches through an include and that the input list
does not name. A patch-only house adds another exception. A house with the
hypothesis can locate the false premise—the list names entry points, not every
dependency—and revise it. The revision changes predictions for other included
files that have never failed. This works because the hypothesis is
[addressable](../theory/definitions/addressable-theory.md): its assumptions
and scope can be inspected and revised one at a time.

The conditional payoff is
[sample efficiency](../theory/retained-theories-may-improve-sample-efficiency.md).
Under a task shift that preserves structure, the house with hypotheses may
need fewer new target observations to reach comparable performance. The
comparison is with the same model and the same history, kept only as case
records from which the house must reconstruct explanations. This is not a
claim of lower compute; maintaining and checking hypotheses costs compute too.

The second payoff is a bounded kind of explanation. A retained hypothesis
claims that a particular rule governs the house's behavior. That claim can be
tested by intervention: run the next job with and without the hypothesis, or
change the dependency it states and check whether behavior moves as stated. A
readable hypothesis is legible, but
[legibility is not faithfulness](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md):
plausible text need not be what drove the behavior. Even a faithful rule
explains the house's operative method, not the model's internals.

## Mixed results and current evidence

The claims can come apart. A loop could beat its baseline on fresh work while
gains stop growing with added compute; that supports the bet but not the
scaling argument. Houses with and without hypotheses could need the same
number of new observations; that would leave the base loop's value intact and
count against the sample-efficiency conjecture in that setting. Intervening on
a retained hypothesis could fail to change behavior, so its explanations would
be unfaithful even where learning occurred.

Commonplace, the agent-operated knowledge-base framework behind this article,
is a human-assisted setting for trying these ideas: people still diagnose
failures and accept updates. No end-to-end autonomous loop has been
demonstrated. The bet and both arguments remain untested.
