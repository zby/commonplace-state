# Assessment: Create Memory Directly

Purpose (as supplied): Make the note clear for a KB maintainer reading it for the first time.

The note is short, and its claims are stated plainly. No rewrite or restructuring of the argument is needed. The passes below work on text expected to survive.

## Ranked changes

1. **Replace the cognitive phrasing of the trigger condition with the working-context mechanism.** Opening paragraph ("understanding is already available during work", "structure the agent already had") and evaluation question 1 ("while understanding was live"). A first-time reader has to infer what "understanding" means here. The same paragraph already names the mechanism: context, provenance and caveats still present in the working context. Cost: three phrase swaps. Pass: `fix-strategy-taxonomy` on finding 1 (`prose/anthropomorphic-framing`, depth 5).
2. **Separate write-time aids from memory destinations in the Methods list.** Five bullets name kinds of artifact to write. The last bullet ("Routing cues, type-specific templates, quality requirements, validators, preview checks, and conversion helpers loaded before writing") names support given to the writer instead. It belongs with the second paragraph's claim that destinations should expose their creation contract. A first-time reader otherwise reads it as a sixth destination. Cost: moving one bullet or adding one lead-in line, scoped to the Methods section and the paragraph before it. Pass: `readability-and-flow` (depth 4).

## Sentence a hostile reviewer would attack first

"Direct memory creation is the context-efficient path when understanding is already available during work." The comparison with later trace extraction rests on an argued cost (rediscovery, lost structure), not on measurement. This is the note's thesis, so it is marked divergence: passes may clarify its wording but may not narrow it.

## Candidate overclaims

- "Direct memory creation is the context-efficient path when understanding is already available during work." — divergence (defend). It is the requirement the note exists to state.
- "Forcing the lesson through later trace extraction spends future context on rediscovery and risks losing structure the agent already had." — support. It is already hedged ("risks"). It may be narrowed only if a pass needs to, but no pass is recommended for it.

## Claim questions for the operator (not passes)

- **The stability threshold (finding 2, `semantic/underspecified-assertions`, depth 2).** "When current work reveals a stable claim…" leaves open whether "stable" means the working agent's in-session judgment or corroboration beyond the episode. The two readings recommend different actions: write now or defer to later extraction. Choosing one decides when the requirement applies, so it is a claim decision, not a wording fix. The operator should state which reading is meant. A follow-up edit can then apply it.
- **Stale qualification in the evaluation questions.** Question 2 asks about the "authority path", but the body never mentions authority. Only the link annotation for "Axes of artifact analysis" mentions behavioural authority. Either the body should say what the authority path is, or the question should drop it.

## Findings not acted on

- `kb/reports/state/review/results/kb/theory/agent-memory-requirements/create-memory-directly.md/semantic/underspecified-assertions.md` — resolving it requires choosing a threshold, which changes when the requirement applies. Raised above as a claim question for the operator.

## Considered, not recommended

- `plain-wording` for "Governed learned artifacts embedded in work surfaces" and "the natural operation". The first phrase is the least clear in the note for a new reader. But it likely mirrors terms from the parent note "Designing a Memory System for LLM-Based Agents". Rewording it here without that note could break the shared vocabulary, so I would not defend the change without that check. The per-item approval stop also costs more than the gain from one phrase.
- `opening-and-title`. The title and description are literal and match the body. After change 1, the description's "live understanding" carries the same cognitive phrasing. The finding's fix strategy can extend to it if it judges the description in scope. A separate pass is not justified.

## What reads well

The Failure Modes paragraph gives one concrete way each artifact type can go wrong, and that makes the requirement's limits easy to see.
