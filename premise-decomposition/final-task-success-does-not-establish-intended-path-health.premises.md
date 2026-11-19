# Premise decomposition: Final task success does not establish intended-path health

**Note:** kb/notes/final-task-success-does-not-establish-intended-path-health.md
**Register:** claim
**Central commitment (one sentence):** Whenever primary-path success and fallback success have the same observable terminal state and no independent execution signal is available, that state alone cannot identify whether the intended path was healthy.

## Premises and counterexamples
1. **At least one healthy primary-path execution and one execution in which the primary path failed but a fallback succeeded can produce the same observable terminal state.** — HOLDS — A runtime that reports path provenance in its terminal result would distinguish the executions, but it would not satisfy the premise's same-observation condition; the broken-helper/direct-retrieval case supplies a witness, and the counterexample hunt found no defeater to this existential premise.
2. **A fallback can produce an acceptable final artifact even though the prescribed path or its supporting infrastructure is unhealthy.** — HOLDS — Cases where fallback is a planned equivalent route or where a request-specific error leaves the infrastructure healthy do not refute this existential premise; a bad helper path or invalid credential followed by successful retrieval through another route is a concrete witness.
3. **In every execution covered by the commitment, no path trace, tool-attempt event, provenance marker, or other independent execution signal accompanies the terminal success observation.** — HOLDS — Trace-rich runtimes are concrete cases where this premise is false, but the commitment explicitly excludes them through its no-independent-signal condition, so the counterexample hunt found no in-scope defeater.
4. **The terminal success observation does not itself encode which of the compatible execution paths produced it.** — HOLDS — A success status whose schema guarantees that the primary path ran would encode the path, but fallback success could not share that status without violating the stated same-observable-state condition; no in-scope counterexample was found.
5. **An observation compatible with both a healthy and an unhealthy intended path cannot by itself identify which health state obtained in the particular execution.** — HOLDS — Strong base rates could make one state highly probable, but probability is not identification; any rule that conclusively selects one state must add information or exclude one of the two compatible executions, so the counterexample hunt found no defeater.
6. **Intended-path health is a fact distinct from whether some path produced an acceptable artifact.** — HOLDS — A system may define only end-to-end task health and treat all routes as interchangeable, but then it has no intended-path health property of the kind named by the commitment; no counterexample was found within the claim's stated subject.

## For the human
Look first at premise 5: it is the load-bearing identifiability principle, and the note correctly limits it to indistinguishable terminal outcomes without an independent execution signal.
