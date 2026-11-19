# Friction check: Experiment design for causal selective evaluation

**Note:** kb/work/causal-impact-selective-evaluation/experiment-design.md
**Central claim (one sentence):** A credible test of selective evaluation must isolate selector quality from procedure-source effects, score against an independent audit surface with full cost accounting, and add a separate trajectory-aware online phase, because otherwise doing fewer checks can be mistaken for better performance.

## Filter
**Verdict:** SURVIVES

## Signal — thinnest joints
1. **"Coverage needs two separate measures... Together, these measures distinguish bad impact prediction from missing procedures, invalid observations, and selection failure."** — UNSUPPORTED — The two named coverage measures do not by themselves separate all four failure modes; the note does not specify what extra observations would let the experiment tell an invalid procedure apart from a bad selector rather than just observing a miss.
2. **"Before selector outputs are revealed, the study should build an independent reference surface from seeded known effects and held-out human-audited obligations."** — THIN — An independent reference surface is clearly needed for harmful-miss claims, but the note does not show that these two sources are sufficient to make the surface representative rather than a narrow probe.
3. **"A separate online comparison should therefore start repeated runs from common checkpoints, standardize candidate and operator inputs where possible, and record every branch that cannot be controlled."** — THIN — The need to observe trajectory effects follows from the note's setup, but it does not establish that repeated runs from shared checkpoints can keep the branches comparable enough to support the intended inference.
4. **"The first comparison should keep the procedure registry fixed so that it isolates selector quality. A second comparison can then cross qualifying selectors with two procedure-source conditions..."** — HOLDS — Holding the registry fixed does support isolating selector quality, though the note leaves the selector-qualification rule and crossover threshold unstated.
5. **"The inspected SPADE loader executes generated Python... Construction, validation, sandboxing, execution, and reuse should therefore be measured parts of the generation factor, not presumed savings."** — HOLDS — Once generated code execution and extra validation work are admitted, counting those costs follows, but the note relies on source-backed SPADE details it does not restate here.

## For the human
Look first at the claim that the proposed coverage and audit scheme can actually distinguish the experiment's failure modes; that is where the note most needs the author's missing concretization.
