---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "and treats extracting a repeated operation into code as a separate intervention whose trade-off must be assessed"
    reason: "The target does say this ('Extracting a repeated operation into code is a different intervention ... The code-extraction trade-off should be assessed'), but in its shared 'What the distinction changes in practice' section, which applies under both accounts, not as a feature of the English account specifically. The attribution is supported in substance; only its placement under 'the English account' is slightly narrow."
    level: info
  - scope: passage
    quotes:
      - "describe the learning mechanisms — narrowing the interpretation space, changing medium"
    reason: "'Narrowing the interpretation space' matches the constraining definition. 'Changing medium' is a loose gloss of codification: the definition says codification moves a rule into symbolic form either by rewriting it or by adopting a consumer as its reference, and in the adoption case 'the text does not change'. In this note's prompt-to-code context the rewrite case applies, so the gloss holds for the case in view, but it does not capture the definition in full."
    level: info
outcome: pass
---

# Review

I checked each sentence that identifies a concept in this note with one from a linked note.

- **English account of prompting.** The target's English account treats an instruction as permitting a set of behaviors from which the executor produces one. This matches. The extraction point is also in the target, though in its account-neutral practice section. Recorded as info.
- **Constraining and codification.** The constraining gloss matches. The codification gloss "changing medium" fits the rewrite case discussed here. It omits the definition's adoption case, where the text stays the same. Recorded as info.
- **Spec mining.** The target's pattern is to observe behavior and extract regularities into deterministic artifacts. The ticket example of checking decisions against resolving queues and keeping a rule matches.
- **Relaxing and proxy theory.** The bitter-lesson note defines relaxing as replacing an extracted component with a more general one and names the proxy-theory regime. The relaxing-signals note covers brittleness and distribution shift. The note's use matches both.
- **Typed callables.** The target says skills, tasks and workflows are callable in a limited sense, can declare signatures, and are not made into conventional functions by them. The paraphrase is accurate.
- **Footer glosses.** The RLM/Tendril/llm-do and host-language scheduler notes are consistent with their footer glosses.

No attribution is substantively different from its target.
