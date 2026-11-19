# Assessment: Removing approval waits can leave required human evaluation in place

**Proposed purpose (the operator named none):** An agent or maintainer who reports or designs the automation of a KB or agent process should be able to tell three things apart: removing a human approval wait, automating or retiring a required human task, and optional assessment. They should then be able to say which human tasks a claim of automation keeps and which requirements it retires.

The artifact declares no write brief.

## What reads well

The two paired hypothetical cases make the distinction concrete. The second section then turns it into a reporting rule ("moved, partly or wholly automated, replaced, or ceased to be required").

## Ranked changes

1. **Narrow the opening "must" to claims about the wider process.** Pass: `narrow-overclaims`, scoped to the sentence "A claim of full automation must say which tasks it preserves and which requirements it retires." Cost: one sentence. The opening states the obligation for any "full automation" claim. The body later concedes that "A claim about automated adoption alone need not include monitoring or revision." The friction report (`kb/reports/state/review/results/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md/kb/instructions/composition-friction-gate.md`) and the premise report (`.../premise-decomposition-gate.md`) both flag this. Narrowing the opening to claims that the whole process is automated, or that cover monitoring or revision, makes the opening consistent with the body. I class this sentence as **support** (may be narrowed). The narrowing restates the condition the body already gives; it does not change the note's claim.
2. **One term per concept for the two categories.** Pass: `abstractions`. Cost: a short proposal list for the operator to decide. One thing goes by "wait", "actual wait", "blocking dependency", "dependency" and "human stop". The other goes by "specified task", "required task", "unfulfilled requirement" and "requirement". The reader has to map these names onto two categories. One name each would make the distinction easier to apply. Scope the pass away from the weekly-review paragraph and the habitual-wait Scope bullet, because both have open claim questions (below).

Not recommended: `readability-and-flow`. The note is short and in order, and the simplification synthesis found no structural opportunity. Not recommended: `plain-wording`. The wording is already literal. Not recommended: `opening-and-title`. The title states the claim, and the opening uses no undefined terms.

## Sentence a hostile reviewer would attack first

"Calling the whole process automated would conceal an omitted task." The critique, friction and premise reports all attack it. "Conceal" holds only if the written weekly review is still in force once nothing enforces it. A review that nobody has treated as binding for a year is stale text, not an omitted task.

## Overclaim candidates: support or divergence

- "A claim of full automation must say which tasks it preserves and which requirements it retires." **Support.** It may be narrowed to claims about the wider process (change 1).
- "Calling the whole process automated would conceal an omitted task." **Support**, but it is held as a claim question (Q1) and is not passed.
- "Removing a human approval wait and removing a specified evaluation task are different changes." **Divergence.** This is the note's core distinction; every report that tested it found it holds. Keep it.
- "Retiring an unnecessary review may be justified, but it is a change in requirements, not automation of that review." **Divergence.** It is the note's distinctive classification of retirement and held in the premise hunt. Keep it.

## Claim questions for the operator

- **Q1. What keeps a specified task required once nothing enforces it?** Kind: unclear between defect and extension, so treated as a choice. It is not ranked first; no defect is shown, and the operator may decline it. The passage is the weekly-review paragraph: "Adoption continues if the maintainer does nothing, but the specified review goes undone. Calling the whole process automated would conceal an omitted task." The case: the specification still assigns a weekly review that nobody has done or treated as binding for a year. Under the reading "required means written in the specification", automating adoption conceals an omitted task. Under the reading "required means still endorsed by the process owner", it conceals nothing, and the specification is stale. One or two sentences would settle it. One option is to say the specification counts while its owner still endorses it or a person is still accountable for the task. Another is the critique's option: say that the reporting obligation holds on either reading, because a lapsed requirement is a retirement that must be reported. Reports: `kb/reports/state/review/results/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md/kb/instructions/critique-note.md`, `.../premise-decomposition-gate.md`.
- **Q2. Waits are identified from practice; requirements only from text.** Kind: choice (no defect shown; the operator may decline). The passage is the Scope bullet "A habitual wait for human input can block automation even without a written rule. It is an actual wait to remove, not evidence that the evaluation is needed to meet a stated requirement." The bullet counts unwritten habits as waits but gives no matching rule for unwritten requirements. It also has two readings of "to remove": "the wait whose removal is at issue" or "a wait that should be removed". The second is a normative conclusion the definitions do not supply. The reports ask the note either to justify the asymmetry or to say how unwritten or lapsed requirements are identified, or else to limit the note to processes with an explicit specification. Reports: `.../composition-friction-gate.md`, `.../critique-note.md`, `.../premise-decomposition-gate.md`.

The role report finds no inbound links, so no dependent relies on any term or claim these questions would change.

No stale qualifications were found.

## Findings not acted on

- `kb/reports/state/review/results/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md/kb/instructions/compression-bundle/marginal-value-redundancy.md` (warn: cut "This example establishes a gap against the specification, not that skipping review causes harm."). Not acted on now. The sentence sits in the weekly-review paragraph, which has the open claim question Q1. The critique cites it as part of how the note engages the stale-specification objection, and the answer to Q1 may rewrite that paragraph. Revisit after Q1 is decided. The same finding's INFO item (fold the first clause of the third paragraph) is INFO only and is not acted on.
- Human-in-the-loop versus human-on-the-loop precedent (critique, secondary). Extension: the claim as scoped stands without the citation, and the purpose does not ask for literature positioning.
- Mixed cases enforced by a deadline or an alert (critique, secondary). Extension: these are further cases, and the purpose does not ask for an enforcement spectrum.
- The "full automation" conventional-scope objection (premise report) is covered by change 1 rather than a separate claim change.
- Synthesis INFO items (shorten the early list of outcomes in the Required approval case). Local compression with no clear value against the purpose.
