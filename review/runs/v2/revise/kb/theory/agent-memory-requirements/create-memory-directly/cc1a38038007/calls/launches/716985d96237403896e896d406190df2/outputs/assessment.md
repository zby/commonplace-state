# Assessment: kb/theory/agent-memory-requirements/create-memory-directly.md

Purpose (given): Make the note clear for a KB maintainer reading it for the first time.

## Ranked changes

1. **Replace the mental-state wording in the load-bearing condition with the working-context mechanism.** "understanding is already available during work", "structure the agent already had" and "while understanding was live" (Evaluation Questions) state the trigger as an agent state. The same paragraph already names the real mechanism: context, provenance and caveats that are "still live" in the working context. A first-time reader gets a condition they can check ("the needed context is loaded now") instead of one they cannot check. Cost: three or four phrase swaps. Pass: `plain-wording` (depth 5), scoped to the opening paragraph and the Evaluation Questions. It addresses finding 1 (`prose/anthropomorphic-framing`, depth 5). The same pass can make "fossilize" and "the natural operation" literal if the operator approves.
2. **Make the opening define its contrast term.** The opening and the description contrast direct creation with "later trace extraction", but the note never says what that is. A first-time maintainer cannot weigh the efficiency claim without it. The description also uses the "live understanding" figure. Cost: one clause in the opening, plus a description wording change. Pass: `opening-and-title` (depth 6), scoped to the description and the opening paragraph. The title is clear; leave it.
3. **Separate write-time aids from destinations in Methods.** Five bullets name artifact kinds to write. The sixth ("Routing cues, type-specific templates, quality requirements, validators, preview checks, and conversion helpers loaded before writing") names support that the system loads at write time. That bullet restates the second paragraph's "creation contract" point. A first reader takes Methods as a list of destinations, and the sixth bullet breaks that reading. Keep the sibling notes' shared section headings. Cost: one bullet moved or relabelled. Pass: `readability-and-flow` (depth 4), scoped to the second paragraph and the Methods section.

Run order is by depth: readability-and-flow, plain-wording, opening-and-title.

## Sentence a hostile reviewer would attack first

"Direct memory creation is the context-efficient path when understanding is already available during work." The note asserts the efficiency comparison with later trace extraction but gives no mechanism beyond one sentence ("spends future context on rediscovery") and no evidence. It is also the sentence whose "understanding" wording finding 1 flags.

## What reads well

The note is short and concrete. Its Failure Modes paragraph gives four distinct, specific ways a direct write goes wrong, and the Evaluation Questions map onto them.

## Overclaim candidates

- "Direct memory creation is the context-efficient path when [the needed context is loaded] during work." **Divergence (defend).** This is the note's thesis and the requirement this note exists to state. Passes may reword its figure but may not weaken the comparison.
- "Forcing the lesson through later trace extraction spends future context on rediscovery and risks losing structure the agent already had." **Divergence (defend).** This sentence carries the mechanism for the thesis. Passes may restate "the agent already had" as working-context content, but may not drop the rediscovery cost or the loss of structure.
- "the natural operation is to write the useful artifact" — **support.** It could be narrowed to "the efficient operation", but the gain is small; plain-wording may propose it. No `narrow-overclaims` pass is recommended.

## Stale qualifications (claim questions for the operator, not passes)

None found. The Relevant Notes gloss for the axes note ("representational-form and behavioral-authority distinction") still matches the body's "representational form and authority path".

## Review findings

- Finding 1, `kb/reports/state/review/results/kb/theory/agent-memory-requirements/create-memory-directly.md/prose/anthropomorphic-framing.md` (depth 5, warn): **acted on** through `plain-wording` (change 1). `fix-strategy-taxonomy` does not list this criterion in `responds-to`, so the finding points at the depth 5 pass.
- Finding 2, `kb/reports/state/review/results/kb/theory/agent-memory-requirements/create-memory-directly.md/semantic/underspecified-assertions.md` (depth 2, warn): **not acted on by a pass.** The unresolved threshold for "stable" decides when the requirement applies: write now or defer to corroboration. Choosing one reading changes what the note claims. The depth 2 pass, `narrow-overclaims`, narrows overstatement; it does not choose between two claims. This is a claim question for the operator: does "stable" mean the working agent's in-session judgment, or corroborated beyond the episode? The sibling note `promote-only-when-value-exceeds-cost.md` may already own the threshold, in which case a sentence pointing to it would resolve the finding. Apply the answer as its own commit after approval.

## Assessed but not recommended

- `abstractions`: the note uses "direct memory creation", "direct creation" and "direct memory" (the last for the artifact produced). The drift is mild and plain-wording can propose a fix if the operator wants one. A separate pass is not of clear value.
- "Governed learned artifacts embedded in work surfaces when that surface is the authoritative destination" is dense for a first-time reader. It depends on the KB's authority vocabulary, which the linked axes note grounds. Readability-and-flow may flag it as not-applied rather than rewrite it.
- No rewrite or restructuring is needed; the argument stands.
