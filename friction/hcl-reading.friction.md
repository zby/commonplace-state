# Friction check: Reading HCL as deployment-time learning

**Note:** kb/work/causal-impact-selective-evaluation/hcl-reading.md
**Central claim (one sentence):** HCL counts as deployment-time learning under Commonplace's architecture-based definition, but HCL's evidence does not validate its four-part mutable-state partition as a causal basis for selective evaluation.

## Filter
**Verdict:** SURVIVES
The note asks one thing to hold at once: classify HCL as genuine learning without a weight update, while refusing two stronger readings the evidence does not earn, namely that `B_n = 0` establishes no regression beyond sampled anchors and that HCL's four retained parts are validated causal-local units for selective evaluation. Those commitments coexist because the architectural classification does not require either stronger conclusion.

## Signal — thinnest joints
1. **"HCL's independent textual budget sweep also exposes an evaluation-cost surface worth measuring."** — THIN — The note derives only a conditional count of proposal-anchor checks under one worst-case checking schedule, so "evaluation-cost surface" is still a proxy label rather than a shown property of the system.
2. **"The count supports comparing evaluation schedules; it does not show that selective evaluation is the right optimization or that HCL is infeasible."** — THIN — The count can compare schedules only on the narrow axis of case checks; the note has not yet shown why that axis is the operational bottleneck that should organize the comparison.
3. **"HCL therefore instantiates the search–evaluation–retention structure described in A proposal-selection improvement loop requires search, evaluation, and operative retention."** — HOLDS — The note gives a proposer driven by post-execution evidence, a reject-capable evaluator, and retained state that changes later executions, which is enough for the note's own definition.
4. **"Its update-permission ablations test bundles of allowed persistent updates; they do not establish those four parts as necessary components, as the correct causal units for predicting impact, or as boundaries within which behavioral effects remain local."** — HOLDS — Bundle ablations identify only the contrasts they run, so the negative conclusion that they do not validate those stronger causal claims is earned.
5. **"A zero budget therefore tightens acceptance over the observed checks; it does not enlarge the set of behaviors for which the evidence warrants a no-regression conclusion."** — HOLDS — The premises immediately before it support the inference: only sampled incumbent-solved anchors are protected, unsampled behavior is outside the count, and held-out forgetting still appears in reported regimes.

## For the human
Look first at the jump from the conditional 4,800 case count to an "evaluation-cost surface" and schedule-comparison claim; that is where the note most needs the author's missing concretization about which cost axis actually matters.
