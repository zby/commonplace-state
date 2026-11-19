# Friction check: Formal systems assess reach only through causal and proof obligations

**Note:** kb/notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md
**Central claim (one sentence):** Formal systems can assess a commitment's reach only after the commitment's claimed generality has been translated into checkable causal or proof obligations, and even then the warrant holds only inside the supplied assumptions, variables, axioms, and modeled domain.

## Filter
**Verdict:** SURVIVES

The note wants three properties to hold at once: formal systems can contribute to reach assessment, the contribution must be mediated by causal or proof obligations, and the result remains bounded by the model or assumptions rather than validating the original natural-language claim. These coexist because the second and third properties narrow the first; they do not require formal systems to both judge arbitrary natural-language claims and avoid judging them.

## Signal — thinnest joints
1. **"That is the route a formal reach assessor can use: a proposed commitment is accepted not because it predicts the training cases, but because the mechanism it asserts supports the intended intervention, counterfactual, or shift claims."** — THIN — The reason shows what a causal obligation would need to certify, but it still hides the hardest operation: deciding that the asserted mechanism is the right formalization of the natural-language commitment's intended reach rather than a narrower substitute that happens to be checkable.
2. **"Causal theories have reach because they do not merely fit one observed distribution."** — THIN — Not merely fitting one distribution is too weak to establish reach by itself; the support comes only if the causal representation captures stable mechanisms that remain valid under the named interventions or shifts, which the next sentences assume rather than derive for any candidate commitment.
3. **"The result is genuine reach assessment inside that model: the evaluator checks not just sampled cases, but the claim's quantified consequence."** — HOLDS — Within a specified formal model, proving or model-checking a quantified consequence really does test more than sampled cases; the remaining gap is not inside the proof route but at the boundary where the natural-language claim is translated into that formal consequence.
4. **"If its axioms included the relevant causal assumptions and its utility function rewarded correct intervention or counterfactual generalization, the proof gate could in principle license adopting a causal-theory learner, graph, or inference rule."** — THIN — The conditional is coherent, but it moves most of the reach work into "relevant causal assumptions" and "rewarded correct generalization"; without a concrete target theorem, the proof gate may be licensing utility under the axiomatization rather than independently assessing causal reach.
5. **"The natural-language case remains different. A natural-language claim whose reach has not been reduced to causal or proof obligations still needs semantic judgment about what the claim means and where it breaks."** — HOLDS — This follows from the formalization boundary the note has already established: if the obligation has not been specified, the system has no formal object whose consequences can be checked.

## For the human
Look first at joint 1: the note needs the missing concretization of how a natural-language reach claim becomes the specific causal mechanism, intervention class, or proof obligation being checked without losing the claimed generality in translation.
