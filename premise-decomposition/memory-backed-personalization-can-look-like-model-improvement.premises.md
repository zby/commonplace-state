# Premise decomposition: Memory-backed personalization can look like model improvement

**Note:** kb/notes/memory-backed-personalization-can-look-like-model-improvement.md
**Register:** claim
**Central commitment (one sentence):** A better response to the same short request can result from retained user-specific intent being reactivated rather than from a more capable interpreting model, while still appearing to the user as model improvement.

## Premises and counterexamples
1. **At least some short requests admit several intended outcomes, so the request by itself does not determine which outcome this user wants.** — HOLDS — Fully specified requests defeat a universal version, but not this possibility-shaped premise; a request such as “revise this” can leave the audience, purpose, and acceptable tradeoffs open.
2. **A system can retain user-specific intent from an earlier interaction and reactivate it while processing a later repetition of the short request.** — HOLDS — Systems without persistence and retrieval failures show that this does not always happen, but they do not defeat the possibility; an external store that retrieves an earlier, still-applicable style preference supplies a concrete witness.
3. **Supplying applicable, authoritative retained intent can improve a fixed model's response without improving that model's general capability.** — HOLDS — Stale or irrelevant memory can worsen a response, but those cases violate the premise's applicability and authority conditions; holding the model fixed while adding a correct omitted preference gives a concrete witness.
4. **A user who sees the better response need not observe whether retained intent changed the assembled context, so the user can attribute the gain to a smarter model.** — HOLDS — A transparent interface can disclose the memory contribution, but the premise is possibility-shaped; an opaque system exposes no output-only means of distinguishing the two causes.
5. **Whenever several outcomes remain compatible with the request, only user-specific evidence can make one outcome authoritative.** — DEFEATED — A non-user-specific but binding application context can select an outcome: for example, an organization-wide system instruction can require every underspecified rewrite request to follow the same house style. — LOCAL — instance
6. **Retained intent as an input and the interpreter's ability to use supplied input are distinct causal roles even when an implementation bundles or co-adapts them.** — HOLDS — Personalized weights can prevent independent component interventions, but that blocks clean attribution rather than erasing the distinction between which user-specific information is available and how effectively the system uses it; the note explicitly routes such implementations to bundled evaluation.

## For the human
Look first at premise 5: qualify the user-specific-evidence requirement so that shared authoritative constraints can also select among request-compatible outcomes without weakening the central possibility claim.
