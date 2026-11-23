---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The epiplexity framework ([Finzi et al., 2026](https://arxiv.org/html/2601.03220v1)) separates information into time-bounded entropy (irreducible randomness) and epiplexity (learnable structure within computational bounds). High-epiplexity regularities are genuinely structural — codifying them is safer because they reflect real patterns, not artefacts of the observer's computational budget. Low-epiplexity patterns that appear regular may be accidents visible only at current scale."
    reason: "The epiplexity branch is not needed for the main claim, and it also works against it. The note's premise is that you can't reliably tell which regime you are in until scale tests it, so systems must codify and relax. This paragraph offers an information-theoretic criterion for judging in advance whether a regularity is structural. The note does not connect that criterion to its exact-spec/proxy-theory split or to its spec-mining and relaxing-signal mechanism. It needs its own evidence, namely how epiplexity would be measured for a codified rule, and it adds attack surface without serving as a premise or boundary. Either cut it, or make it an open question ('could a computational-learnability measure separate structural regularities from accidental ones before scale tests them?'), or move it to a separate note or workshop lead about advance criteria for codification bets."
    level: warn
  - scope: passage
    quotes:
      - "Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats — they learn length-specific solutions in isolation, with training diversity actively hurting (κ = 0.28 for CoT)."
    reason: "The induction-bias result does support a boundary claim in the note: arithmetic-regime bets stay safe under scaling. That support can stay. This sentence, though, adds experimental detail (the sharing factor, the length-specific solutions, the training-diversity effect and the CoT value) that the main argument never uses. That detail belongs in a source ingest. One sentence would carry the point here: architectural step-by-step bias stays an advantage for calculator-class tasks. Where to put the detail is unclear, so this is info, not a removal demand."
    level: info
outcome: warn
---

# Review

## Summary

The main claim is in the description and opening paragraph. You can't reliably tell exact-spec decompositions from proxy-theory decompositions until scale tests them. So practical systems codify code-extractable regularities as bets and relax them when signals show the bet lost. Spec mining improves the odds because it starts from a system that already works.

Most side material supports that claim where it sits:

- The edge-detection, FlashAttention and tokenizer examples show that the trajectory runs in both directions.
- The vision-researcher contrast sets up why spec mining narrows the bet.
- The link to the unsupported-proxy-scope diagnosis is explicitly marked as conjectural and frames the bet from the author's side.
- The relaxing-signals paragraph supplies the detection half of codify-and-relax.
- The working heuristics derive from the regime distinction.

The epiplexity paragraph is the one branch that needs action. It brings in a separate theory of when regularities are structural. That theory implies a way to tell the regime in advance, which cuts against the note's founding premise, and the note never reconciles the two. The Ebrahimi paragraph earns its place as support for the arithmetic regime. Its sentence of experimental parameters is excess detail that could be compressed, but where that detail should go is unclear, so it is recorded as info.
