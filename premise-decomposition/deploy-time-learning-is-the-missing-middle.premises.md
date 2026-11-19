# Premise decomposition: Retained system-definition artifacts enable persistent deployment-time adaptation

**Note:** kb/notes/deploy-time-learning-is-the-missing-middle.md
**Register:** claim
**Central commitment (one sentence):** A persistent deployment-time adaptation path exists outside model-weight updates when deployment evidence drives the evaluation and operative retention of changes to behavior-shaping system-definition artifacts.

## Premises and counterexamples

1. **An evidence-responsive proposal, evaluation, and operative-retention loop is sufficient to distinguish adaptation or learning from evidence-informed maintenance.** — DOUBTFUL — After one production refusal, a narrow evaluation could select and retain a global rule that permits the failed case but breaks many untested cases; deployment evidence influenced selection and the rule changes later behavior, yet the stated conditions do not establish that the change improved or even preserved the system's relevant adaptive capacity. — LOCAL
2. **Mutable system-definition artifacts outside the model's weights can causally determine deployed behavior.** — HOLDS — The strongest counterexample is an artifact that the runtime ignores or that a model treats as optional, but such an artifact is not consumed with the binding force the premise specifies; an active router, executable tool, schema validator, or governing configuration can mechanically change later behavior while weights remain fixed.
3. **A change to such an artifact can be produced while the system is deployed.** — HOLDS — Immutable production systems and changes prepared only for a later release are counterinstances to a universal claim, but they do not defeat this existence premise: a deployed runtime can revise versioned configuration, routing, tools, or rules between executions without entering a weight-training phase.
4. **The selected artifact change can persist beyond the run that produced it without being encoded in model weights.** — HOLDS — Ephemeral containers, failed writes, and rollbacks can prevent a particular change from persisting, but durable configuration or artifact storage provides a concrete retention mechanism independent of weight state.
5. **A retained artifact change can be operatively loaded in later executions and change their behavior.** — HOLDS — A saved but unrouted rule, stale cache, or retrieval miss would defeat mere storage as a behavioral mechanism, but it does not defeat operative retention; later executions that load a changed router, validator, tool, or governing prompt receive a different behavior-producing component.
6. **Deployment evidence can bear on both proposing and selecting an artifact change.** — HOLDS — A cosmetic edit or an operator's unsupported preference would not satisfy the premise, but a production failure can generate a candidate rule or tool revision whose replay or regression evaluation determines whether that revision is retained.
7. **A durable change in the non-parametric components of the deployed system can be attributed to the system's adaptive capacity rather than only to the model's unchanged capacity.** — HOLDS — The strongest counterexample is a human-authored patch that looks like external engineering rather than learning, but externally supplied updates also alter the capacities of systems whose learning algorithms do not originate their own data or objectives; once the deployed system is the stated unit, a binding component change changes that unit's available behavior.

## For the human

Look first at premise 1: the proposal-selection-retention conditions need a fidelity condition if they are meant to separate genuine adaptation from a durable change selected by a narrow or misleading evaluation.
