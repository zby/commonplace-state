# Premise decomposition: Soft degradation often constrains agent work before hard token limits bind

**Note:** kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
**Register:** claim
**Central commitment (one sentence):** For quality-sensitive agent work whose required evidence fits inside the provider window, soft degradation across volume, relevance/interference, and complexity often constrains usable context before hard token limits do.

## Premises and counterexamples
1. **There is a real soft-degradation regime below the hard token cap where task quality can fall through missed instructions, shallow reasoning, or unused context while outputs remain fluent and well-formed.** — HOLDS — The counterexample hunt did not find a reason this phenomenon must be reducible to only hard-cap failure; silent quality loss below the cap is an ordinary enough pattern to survive the hunt.
2. **Across the note's intended workload class, soft degradation before the cap is common enough to warrant the statistical claim that it often binds first.** — DOUBTFUL — The note's evidence comes from long-context retrieval, synthetic distractor math, a specific web-agent benchmark, and low-token symbolic composition. A plausible prevalence-shaped defeater is that well-scoped retrieval-heavy coding and operations workflows on current long-context models usually stay reliable until either the hard cap or some non-context bottleneck binds, which would make early soft degradation non-ordinary across the claimed class. — GLOBAL — prevalence
3. **Added context volume can by itself reduce usable context before the hard cap is reached.** — HOLDS — The counterexample hunt did not find a reason to treat long-context misses as only interference or only bad prompt design; positional-retrieval failures and usable-window results are enough to keep volume as a live load-bearing premise.
4. **Irrelevant, stale, or weakly relevant context can actively interfere with task execution rather than merely add harmless bulk.** — HOLDS — The counterexample hunt did not find a reason to collapse this into pure length effects; objective drift and stale-state reuse remain a distinct enough failure shape to survive the hunt.
5. **Compositional complexity is an independent soft-bound pressure, not just a separate reasoning deficit that happens to appear at low token counts.** — DOUBTFUL — A concrete defeater shape is a low-token symbolic task that fails because the model lacks the required reasoning procedure even when context management is not the bottleneck. The note itself leaves that alternative open, so the premise is not secure as stated. — LOCAL — instance

## For the human
Look first at premise 2: the note's "often" needs the strongest scrutiny, because if early soft degradation is not ordinary across the intended workload class, the central commitment needs narrowing rather than a local patch.
