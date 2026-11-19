# Friction check: LLM recompute cost shifts the store-vs-recompute balance

**Note:** kb/notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md
**Central claim (one sentence):** Costly model-side derivation shifts the store-versus-recompute balance toward a source-bound, deterministically checked materialization only when that materialization beats model-side and external on-demand derivation on total expected cost and actually substitutes for work.

## Filter
**Verdict:** SURVIVES
Lower expected cost, direct model readability, and subordination to the live source can coexist in one artifact: a derived cache that a deterministic validator checks against its source and that the model consumes instead of repeating the derivation.

## Signal — thinnest joints
1. **“A model may read an answer and then inspect the source or rerun the derivation because the answer is insufficient or untrusted for the task. In that case, materialization adds cost instead of removing it.”** — UNSUPPORTED — A later source read or derivation does not establish that the materialized answer removed no work: it may narrow the source read, reduce the derivation, or otherwise substitute partially, so only the net cost ledger can establish addition.
2. **“When code consumes the derived value, the ordinary software presumption applies.”** — UNSUPPORTED — The identity of the consumer does not establish that recomputation is cheap; an expensive deterministic code derivation can also favor caching, so the boundary classifies the computation path but does not by itself restore the presumption's direction.
3. **“If validation fails, the system must withhold the copy from trusted use and fall back to recomputation.”** — THIN — The stale-copy argument supports withholding the failed copy, but it does not establish recomputation as the required response rather than failing closed, regenerating the copy, or using another authoritative path.
4. **“A trusted copy needs a machine-locatable boundary, an explicit binding to its source and derivation, deterministic comparison semantics, and enforcement before the model consumes it.”** — THIN — The consistency liability supports an enforceable check against ground truth, but the note does not show that every listed mechanism is independently necessary for every trusted materialization or rule out equivalent source-versioned or generation-time designs.

## For the human
Concretize the substitution joint first: state how partial narrowing or partial recomputation enters the ledger before claiming that any later source access makes materialization purely additive.
