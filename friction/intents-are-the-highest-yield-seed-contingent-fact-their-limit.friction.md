# Friction check: A specific intent may out-yield local rationales, but contingent facts stay separate

**Note:** kb/notes/intents-are-the-highest-yield-seed-contingent-fact-their-limit.md
**Central claim (one sentence):** When a specific governing intent is not otherwise recoverable, retaining it should reconstruct more local rationale per token than an equal-size set of local rationale snippets, but it cannot replace contingent facts that do not follow from that intent or available context.

## Filter
**Verdict:** SURVIVES
The claim wants three properties at once: retained design theory stores what the interpreter cannot recover, specific intent can have higher per-token yield for local rationale reconstruction than local rationale snippets, and contingent facts remain separately retained when purpose and context do not entail them. These can coexist because the yield comparison is scoped to reconstructable local rationales under an equal-token budget, not to all retained knowledge.

## Signal — thinnest joints
1. **"Given a specific intent and the implementation, an interpreter can reconstruct several local judgments."** — THIN — The note shows why intent gives the interpreter questions to ask, but not why the interpreter can answer them accurately from artifact plus intent; the Naur support concerns a theory-holder's ability to justify a program, not an outside interpreter's recovery from a retained intent.
2. **"A specific intent is plausibly high-yield because one purpose can constrain many parts, while one local rationale usually explains fewer."** — THIN — The upstream/downstream shape supports the conjecture, but the ranking still depends on the grain and specificity of both sides: a local rationale can encode a broad invariant, and an intent can be too vague to reconstruct much.
3. **"This is why an instruction can often retain its goal while omitting reasons that follow from the goal and the steps..."** — THIN — The inference transfers the design-theory yield conjecture into instruction-writing practice without showing that an instruction executor has the same artifact access, background knowledge, or reconstruction target as the design interpreter.
4. **"Losing the goal removes the seed for local reconstruction, which helps explain why [a goal-holding interpreter fails soft]."** — THIN — Losing a goal can remove an inference seed, but the link to soft failure depends on a further model of executor behavior under missing goals; the note points to another artifact for that model rather than establishing it here.
5. **"This note's narrower inference is to record the decision basis when later work must not reverse the choice by accident."** — HOLDS — The artifact can expose the selected alternative without exposing the rejected alternatives or binding status, so recording the decision basis is warranted when accidental reversal is a real maintenance risk; the remaining thinness is how an author identifies that risk at capture time.

## For the human
Look first at the bridge from "intent gives questions to ask" to "intent lets an outside interpreter reconstruct local judgments"; that is the main missing concretization behind the yield ranking.
