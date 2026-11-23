# Inbound contexts of `kb/articles/deployment-time-machine-learning-llm-selected-updates.md`

5 file(s) link to this note. Searched: Markdown files under kb/, except kb/reports/, kb/work/, hidden directories and the note itself.

## `kb/articles/README.md`

- Title: Articles
- Description: (none)

> - [Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score](./deployment-time-machine-learning-llm-selected-updates.md) — asks whether a deployed agent can use an LLM to select revisions to its own instructions without a single score. It distinguishes the decision to try an edit from evidence that the edit improved later work. No end-to-end automated run is reported.

## `kb/articles/testing-autonomous-selection-based-learning.md`

- Title: Testing Autonomous Selection-Based Learning
- Description: Research program article: separates membership, edit outcomes, and autonomous LLM judgment in Commonplace; defines comparisons for admission, targeted correction, criterion revision, and net gain, plus a proposed first routing-check experiment

> In [selection-based learning](../theory/definitions/selection-based-learning.md),
> a system learns by changes that are each proposed, judged inside the loop,
> and can be rejected. In Commonplace those changes are edits to a readable,
> addressable store—prose, structured text, and code consumed by its later
> work. The
> [lead article](./deployment-time-machine-learning-llm-selected-updates.md)
> argues that a fixed-weight language model could serve as that judge where
> no fixed test is adequate, using a robust comparison in place of a single
> value function.

> - [Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score](./deployment-time-machine-learning-llm-selected-updates.md)
>   — the lead article stating the paradigm, the weight-training contrast,
>   and the Bitter Lesson argument.

## `kb/index.md`

- Title: Commonplace
- Description: (none)

> - **Central thesis:** [Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score](./articles/deployment-time-machine-learning-llm-selected-updates.md) (draft) argues that selection-based learning needs a comparison but not a single score, and that a fixed-weight LLM can supply it in a way compatible with the Bitter Lesson. It is grounded in the [selection-based learning definition](./theory/definitions/selection-based-learning.md) and [necessary preference](./theory/necessary-preference-can-guide-improvement-without-a-global-measure.md).

## `kb/tags/improvement-loop-README.md`

- Title: improvement-loop
- Description: Curated head for the improvement-loop tag — proposal-selection loops: search for candidates, reject-capable evaluation, operative retention, search control, backtracking, and oracle quality

> Learning by this loop is [selection-based learning](../theory/definitions/selection-based-learning.md). Commonplace bets that a fixed-weight language model can do the selecting unaided; the [lead article](../articles/deployment-time-machine-learning-llm-selected-updates.md) argues it, untested so far.

## `kb/theory/automating-kb-learning-is-an-open-problem.md`

- Title: Automating KB learning is an open problem
- Description: The KB already learns through manual improvement; automating judgment-heavy mutations needs oracles for connections, groupings, and synthesis we cannot yet manufacture

> Commonplace now states a bet about this problem. [Selection-based learning](./definitions/selection-based-learning.md) needs a comparison between the KB with a mutation and the KB without it, not a score for every mutation. The [lead article](../articles/deployment-time-machine-learning-llm-selected-updates.md) bets that a fixed-weight language model can make that comparison from the KB's stated purpose. The bet is untested. If it holds, what is missing is a validated judge of single changes, not an oracle that scores the whole KB.
