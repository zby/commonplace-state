---
type: types/edit-result.md
outcome: changed
changes:
  - "Opening paragraph 1: led with the deployed agent learning by changing what it retains between tasks (an instruction its next run reads, or a criterion it uses to judge its own edits); moved fixed model weights into a trailing subordinate clause instead of a standalone second sentence."
  - "Opening paragraph 2: added one sentence stating the denied alternative: that selecting an update first requires collapsing every gain and loss into one number."
  - "Opening paragraph 2: introduced 'the judge' at first use as 'the judge that evaluates a proposed change'."
  - "Opening paragraph 2: 'every function in the set' became 'every weighting in the set', matching the term the paragraph had just introduced for the preference model's members."
  - "Opening paragraph 2: glossed 'addressable' at first mention with the definition link and introduced 'store' as the system's retained instructions and criteria kept as text whose parts can be inspected and revised one at a time."
  - "Opening paragraph 2: replaced the distant referent 'the term' with 'selection-based learning' in the closing reinforcement-learning sentence."
removed-links: []
---

# Report

Scope: the two opening paragraphs after the draft banner. The third
paragraph (the bet), the rest of the body, the title, H1 and description
are unchanged.

## Old TL;DR (paragraphs 1–2, abridged)

> A deployed agent can change how it handles its next task by revising an
> instruction its next run will read. Its model weights need not change. The
> question is which revisions to keep. [...] First, selection-based learning
> [...] needs a comparison, not a single score. The judge need only compare
> the candidates at hand [...] the comparison is robust when every function
> in the set gives the same answer. [...] The case argued here is the one
> where the changes are edits to the system's own readable, addressable
> store. [...] Like reinforcement learning, the term names a process with no
> built-in guarantee of improvement.

## New TL;DR (paragraphs 1–2, abridged)

> A deployed agent can learn by changing what it retains between tasks: an
> instruction its next run will read, or a criterion it uses to judge its
> own edits, while the model's weights stay as they are. The question is
> which revisions to keep. [...] The alternative denied here is that
> selecting an update first requires collapsing every gain and loss into one
> number. The judge that evaluates a proposed change need only compare the
> candidates at hand [...] robust when every weighting in the set gives the
> same answer. [...] edits to the system's own retained instructions and
> criteria, kept as a readable, [addressable] store: text whose parts can be
> inspected and revised one at a time. [...] Like reinforcement learning,
> selection-based learning names a process with no built-in guarantee of
> improvement.

## Must-keep check

- Learning by changing retained instructions or criteria now leads, and
  fixed weights are no longer the headline. The fixed-weights claim stays
  as a subordinate clause.
- "Needs a comparison among the candidates at hand, including leaving the
  system unchanged, not a single score" and "a robust comparison can select
  changes without anyone choosing one scalar weighting" are kept verbatim.
  The new denied-alternative sentence is about selecting an update, so it
  makes no claim about model training.
- The terms the body relies on (selection-based learning, preference model,
  robust, judge, store, addressable) are all introduced in the opening and
  keep their meaning.

## Title

I propose no title. Must-keep says "Keep the chosen title", so this run
makes no title proposal. The current title already states the central
contrast literally: the updates are LLM-selected and need no single score.
The current slug, `deployment-time-machine-learning-llm-selected-updates`,
is 53 characters, within the 70-character limit.

## Noticed, not applied

- The third opening paragraph (the bet) is outside scope. It reads cleanly
  with the new opening and needed no change.
- The body's table links `addressable` again. That link is redundant now
  that the opening glosses the term, but it is outside scope and harmless.
