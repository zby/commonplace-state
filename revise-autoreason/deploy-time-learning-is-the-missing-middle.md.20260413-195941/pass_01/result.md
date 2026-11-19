# Pass 1 Result

Valid judges: 3 / 3

## Parsed Rankings (after remapping via judge_mappings.md)

- judge_1 (mapping 1=A, 2=B, 3=AB) -> RANKING: 3, 1, 2 -> first=AB, second=A, third=B
- judge_2 (mapping 1=AB, 2=A, 3=B) -> RANKING: 1, 2, 3 -> first=AB, second=A, third=B
- judge_3 (mapping 1=B, 2=AB, 3=A) -> RANKING: 2, 3, 1 -> first=AB, second=A, third=B

## Borda Scores (first=3, second=2, third=1)

- A:  2 + 2 + 2 = 6
- B:  1 + 1 + 1 = 3
- AB: 3 + 3 + 3 = 9

## Winner

AB — unanimous across all three judges. No tie-break required.

## Outer Semantic Fidelity Check — REJECTED

Judge 1 flagged a "subtle reframing of scope" in AB. On inspection it is a
substantive claim change:

### Before (original A, end of mechanisms paragraph)

> Two mechanisms drive it: constraining (narrowing the interpretation space)
> and distillation (extracting procedures from reasoning). Codification — the
> far end of constraining — is where prompts undergo a phase transition into
> deterministic code. This note focuses on the verifiability gradient that
> runs across both.

### After (AB winner)

> Two mechanisms drive deploy-time learning: constraining (narrowing the
> interpretation space) and distillation (extracting procedures from
> reasoning). Codification sits at the far end of constraining, where prompts
> undergo a phase transition into deterministic code. Both mechanisms operate
> as a **constrain/relax cycle**: tighten when patterns across runs make the
> commitment safe, and be ready to loosen again when new requirements expose
> a wrong one.

### Why rejected

1. Drops the scoping sentence "This note focuses on the verifiability
   gradient that runs across both" — a forward-looking navigation signal
   pointing into the next section, not filler.
2. Adds a new claim: "Both mechanisms operate as a constrain/relax cycle."
   In the incumbent A the constrain/relax cycle appears only inside the
   Failure Modes bullet on premature codification, framed as the antidote
   to that specific failure mode. Generalizing it to a definitional property
   of both constraining and distillation is an unsanctioned claim promotion
   (and the relax half of the cycle is not obviously a property of
   distillation as defined in the original).
3. The Failure Modes bullet was rewritten to say "The antidote is the
   constrain/relax cycle introduced above," which compounds the promotion
   by making the failure-mode antidote reference the new upstream claim
   rather than standing on its own.

Under the outer fidelity rule ("Rejects the winner and stops if it changes
the meaning of any claim / alters qualifiers in a meaning-changing way"),
AB is rejected. Finalize with last_good (the original incumbent).
