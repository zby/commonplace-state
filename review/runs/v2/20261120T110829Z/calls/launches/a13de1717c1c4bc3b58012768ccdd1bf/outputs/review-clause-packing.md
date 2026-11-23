---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Separately, the team's goal may not have changed, yet the extracted Python rule proves to be a brittle proxy theory that fails on edge cases or distribution shift—or a stronger, cheaper model now handles the broader task well enough"
    reason: "About 44 words packing four ideas: the unchanged goal, the contrastive 'yet' clause, the proxy-theory rule with its two failure conditions, and a second, independent trigger (a stronger, cheaper model) attached by a dash. The two relaxing triggers are separate conditions and read more easily as two sentences, e.g. 'The goal may not have changed. Either the extracted rule proves a brittle proxy theory that fails on edge cases or distribution shift, or a stronger, cheaper model now handles the broader task well enough.'"
    level: warn
  - scope: passage
    quotes:
      - "the mechanism whose movement across prompts and code a unified interface lowers call-site friction for"
    reason: "Distance problem: 'whose movement across prompts and code' opens a dependency that resolves only at the stranded final 'for', while the clause subject 'a unified interface' and verb 'lowers call-site friction' sit between. A reordering keeps every relation: 'the mechanism for which a unified interface lowers call-site friction when it moves across prompts and code'."
    level: warn
  - scope: passage
    quotes:
      - "But in a system that exposes agents and tools through different invocation surfaces, a codification step that moves a component from one surface to the other is a breaking change"
    reason: "About 48 words including the colon list. A long fronted condition and a subject with its own relative clause precede the main verb, then three consequences follow. The colon list is a separate unit, so the load is tolerable; noted rather than flagged."
    level: info
  - scope: passage
    quotes:
      - "treats an instruction as permitting a set of readings, from which an LLM executor produces one, and treats extracting a repeated operation into code as a separate intervention whose trade-off must be assessed"
    reason: "About 39 words joining two independent attributions, each with an embedded relative clause. Near the threshold and still retainable; splitting into two sentences would ease it slightly."
    level: info
outcome: warn
---

# Review

Most sentences in the note stay under the threshold or carry at most two ideas. Two passages overload the reader.

The relaxing bullet in "Why this matters for constraining" packs two independent relaxing triggers into one contrastive sentence. The reader must hold the unchanged goal, the proxy-theory rule and its failure conditions, and then a different trigger joined by a dash. Splitting it at the dash keeps the meaning.

The `Constraining` footer gloss strands its preposition at the end. The `whose movement ...` phrase stays unresolved across the embedded subject and verb. Moving to "for which" fixes it without dropping any word or relation.

Two further long sentences are noted at info level: the codification-step sentence and the opening attribution to the English account. Each is long, but its structure stays retainable.
