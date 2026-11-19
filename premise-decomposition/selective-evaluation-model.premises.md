# Premise decomposition: A provisional causal selective-evaluation model

**Note:** kb/work/causal-impact-selective-evaluation/selective-evaluation-model.md
**Register:** claim
**Central commitment (one sentence):** An honest selective-evaluation model must distinguish mechanically inapplicable checks from applicable-but-omitted ones, keep impact prediction, observation, selection, and acceptance conceptually separate, and treat omission under uncertainty as changing what acceptance can warrant.

## Premises and counterexamples
1. **Mechanically inapplicable checks and applicable-but-omitted checks differ in kind: only the former can be removed from the candidate-relative evidence set without creating an evidence gap.** — DEFEATED — An applicable obligation can sometimes be discharged without running its named check because a stronger proof or validator already entails it; for example, a formally enforced serializer or type pipeline can make a standalone schema-conformance check redundant without making the obligation itself inapplicable. — LOCAL — instance
2. **Predicting that `Delta` may affect a function or obligation does not by itself identify a procedure that can observe the effect, so impact theory and observation mapping cannot safely be collapsed.** — DOUBTFUL — Some obligations are operationalized by a single canonical detector, so storing obligation-plus-detector pairs could preserve the needed behavior without a separately named `M` layer; the note shows conceptual usefulness, but not that a distinct object is always required. — LOCAL — instance
3. **Candidate-relative applicability can be fixed before cost enters the policy, and cost alone cannot honestly make a validity check inapplicable.** — DOUBTFUL — For adaptive or synthesized evaluations, whether the system can even realize an obligation as an executable check may depend on spending construction and validation budget, which entangles "applicable" with "selectable" more than the note allows. — LOCAL — instance
4. **If an applicable obligation is omitted under uncertainty, the ordinary HCL-style acceptance warrant no longer holds unless a new rule explicitly accounts for residual risk.** — HOLDS — No concrete defeater found: once an applicable check is left unrun under uncertainty, the ordinary "the relevant checks stayed within budget" warrant no longer says what it used to say.
5. **A selector mostly sees the checks it chooses, so omitted-check failures can stay hidden unless the system deliberately arranges counter-observation or has an equally strong structural guarantee.** — HOLDS — No concrete defeater found: without exploration, audit, monitoring, or a proof-quality substitute, selected-check success can self-confirm.

## For the human
Look first at premise 1: the note's opening two-way distinction misses the case where an applicable obligation is discharged by proof or stronger surrogate evidence, so that separation needs a third category or tighter scope.
