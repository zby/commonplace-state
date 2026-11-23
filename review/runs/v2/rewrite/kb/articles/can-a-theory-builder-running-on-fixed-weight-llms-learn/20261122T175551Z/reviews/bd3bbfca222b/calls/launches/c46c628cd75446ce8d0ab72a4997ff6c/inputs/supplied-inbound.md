# Inbound contexts of `kb/articles/can-a-theory-builder-running-on-fixed-weight-llms-learn.md`

7 file(s) link to this note. Searched: Markdown files under kb/, except kb/reports/, kb/work/, hidden directories and the note itself.

## `kb/articles/README.md`

- Title: Articles
- Description: (none)

> - [Can a Theory Builder Running on Fixed-Weight LLMs Learn?](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md) — the earlier lead, to be rewritten. It introduces the theory builder, a system that runs Popper's cycle of problem, tentative solution, error elimination, and revised problem over explicit theories, defined by four conditions: stated theories, acted on, criticized for what they say, with the result shaping the next round. It states the bet that a fully automated theory builder that learns can be built with today's fixed-weight LLMs, argues that an LLM can apply precise definitions where formal proof cannot reach, gives the payoffs and costs of explicit learned state and three conjectured advantages, argues compatibility with the Bitter Lesson, states the two-part test that would count as learning, and says how Commonplace builds one: reflective from the start, moving operations from people to computation, on the conditional case that investing in the method pays over a long horizon. Testing, bootstrapping from Commonplace, the software-house arrangement, and the survey each point to a supplement.

## `kb/articles/an-automated-software-house-as-a-second-test-of-a-theory-builder.md`

- Title: An Automated Software House as a Second Test of a Theory Builder
- Description: Supplement: the automated software house conjecture (2026-09-02 fixed models) as a second test of a theory builder; Naur's program theory against the stated-content condition, software's stronger falsifier and harder claim, four witness conditions

> [The lead article](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md) bets
> that a fully automated theory builder that learns can be made from today's
> fixed-weight LLMs, and tests the bet first with a knowledge base, whose failures are slow
> and partly judged by people. This supplement states a second arrangement: an
> automated software house. Software gives the program a stronger falsifier
> than a knowledge base does, at the price of a harder claim. The arrangement
> is kept as a companion to the knowledge-base test, not a replacement for it.

## `kb/articles/bootstrapping-an-autonomous-theory-builder.md`

- Title: Bootstrapping an Autonomous Theory Builder with Commonplace
- Description: Bootstrap supplement: Commonplace starts as a reflective theory builder staffed partly by people, moves operations to computation one at a time, and judges progress by which kinds of improvement complete without the operator's decisions

> [The lead article](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md) bets that
> a fully automated theory builder that learns can be built with today's
> fixed-weight LLMs. A
> [theory builder](../theory/definitions/theory-builder.md) is a system that
> states its theories in natural or formal language, acts on them, criticizes
> and revises them, and keeps the results for its next round of work. This
> article describes how Commonplace, the knowledge base behind these articles,
> builds one that is autonomous.

> Throughout, what is learned must be retained in the system, change later
> behaviour, and change it for the better;
> [the lead article](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md) says how
> that last condition is tested. The bootstrap has advanced when a kind of
> improvement that needed the operator's decisions completes with those
> decisions withheld. It is working while the kinds of improvement that pass
> this test keep growing. [The last section](#the-bootstrap) states the test
> and what would count as failure.

## `kb/articles/testing-whether-a-theory-builder-learns.md`

- Title: Testing Whether a Theory Builder Learns
- Description: Testing supplement: show that a theory builder's retained revisions causally improve later capacity; seven tests, task families with seed, matched baseline, evidence interface, and controls, human-decision accounting, compounding, three hypotheses

> We are only starting to
> [build theory builders from today's language models](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md).
> A [theory builder](../theory/definitions/theory-builder.md) states its
> theories in text, acts on them, criticizes what they say, and lets the
> result of criticism shape its next conjecture. Whether a system that meets
> the definition learns, in the sense of improving its capacity for later
> work, is left to testing. The first testing goal should be modest. Before
> asking whether theory builders can learn broadly or indefinitely, we need to
> show that retained revisions cause later improvement at all.

> A system has learned only if experience produces a durable change in
> retained state that affects later capacity. The
> [lead article](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md) gives the
> causal structure:

## `kb/articles/what-an-automated-reviewer-should-measure.md`

- Title: What an Automated Reviewer Should Measure
- Description: Automated review with two testable claims: reach and economy indicate reader-relative compression progress, and that progress improves relevant task performance

> This experiment connects to [building a theory builder from today's
> LLMs](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md): that research program
> tests whether retained theories change later behaviour while model weights
> remain fixed. This experiment tests one article's effect, not whether
> criticizing and revising retained theories improves a whole system's
> capacity for future action.

> [Information value is
> observer-relative](../theory/information-value-is-observer-relative.md)
> develops the reader-relative baseline.
> [Explanatory reach](../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md)
> and [reach-assessment](../theory/definitions/reach-assessment.md) develop the
> property and its assessment.
> [Can a Theory Builder Running on
> Fixed-Weight LLMs Learn?](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md) develops the
> research program behind the retained-artifact comparison.

## `kb/articles/which-existing-self-improving-systems-are-theory-builders.md`

- Title: Which Existing Self-Improving Systems Are Theory Builders
- Description: Survey of eighteen self-improving systems placed against the four theory-builder conditions, with reported learning gains judged separately: five builders, one outside, twelve unsettled mostly on criticism; next experiments

> Existing self-improving systems already report gains from retained knowledge
> and revised skills. They also supply mechanisms for diagnosis, criticism,
> revision, and reuse. [Our program](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md)
> asks two separate questions of each system. Is it a theory builder, a system
> that states its theories, acts on them, criticizes what they say, and lets
> the result of criticism shape its next round? And does holding and
> criticizing those theories improve its later decisions? A third question is
> whether the whole process can run without people performing its internal
> roles.

## `kb/sources/harness-evolution-ceiling-weight-training.ingest.md`

- Title: Ingest: Harness Evolution Hits a Ceiling: When Weight Training Should Begin
- Description: Crosses evolved harnesses with trajectory-trained adapters to argue failure composition picks harness evolution or weight training; read here against Commonplace's fixed-weight learning bets

> The source is a bounded empirical case in the KB's cross-form learning cluster. Its role is twofold: evidence about diagnosis and allocation of gains between the harness and the weights, and a counterpoint to the headline of the lead article [Can a theory builder running on fixed-weight LLMs learn?](../articles/can-a-theory-builder-running-on-fixed-weight-llms-learn.md). The counterpoint is in the paper's title and decision rule, which send content failures to weight training. The paper's own §6.2 withdraws the general claim: the ceiling is "a property of this loop's evidence package, not of harness evolution in general". The Learning Claims section sets the paper's conclusions against our bets item by item.

> - [Can a theory builder running on fixed-weight LLMs learn?](../articles/can-a-theory-builder-running-on-fixed-weight-llms-learn.md) — is-evidence-for: counterpoint in its rule, support in its 9B data; see the bets table in Learning Claims
