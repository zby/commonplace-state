# Friction check: Local materialization should outperform distant natural-language declarations

**Note:** kb/notes/local-materialization-should-outperform-distant-declarations.md
**Central claim (one sentence):** For LLM tasks where a canonical natural-language declaration is distant from its use or non-obvious to apply, rendering its exact value or a fixed derived label beside the use site should increase correct, non-contradictory application relative to declaration alone while retaining the canonical value as the sole maintenance authority.

## Filter
**Verdict:** SURVIVES

## Signal — thinnest joints
1. **Implicit inference from “Natural-language content has no equivalent operation with assigned consequences” to “local materialization should produce a higher rate of correct, non-contradictory application”** — UNSUPPORTED — The absence of formal resolution semantics makes locality a plausible intervention, but it does not establish the predicted improvement; local text may still be ignored or misapplied, and the note identifies no prior result that resolves those competing possibilities.
2. **“Even deterministic decoding does not uniquely specify this application: agentic systems can produce behavior consistent with an interpretation that the instruction does not determine.”** — THIN — Instructional underspecification explains why an instruction may permit several interpretations, but it does not show that deterministic decoding of a fixed model and complete context fails to select one output; the sentence slides from normative underdetermination by the instruction to operational determination by the decoder.
3. **“A contextual natural-language consequence generally cannot be certified by deterministic equality. It needs explicit lineage and judgment-based review”** — UNSUPPORTED — Failure of equality checking establishes only that literal comparison is insufficient, not that explicit lineage plus judgment-based review is necessary; executable constraints, task tests, or other semantic checks could provide assurance without that specific maintenance regime.
4. **“What can be materialized safely depends on representational form”** — THIN — Representational form affects which checks are available, but safety also depends on the derivation rule, source relationship, renderer, validator, and consumer; the stated contrast does not establish form itself as the deciding variable.

## For the human
Look first at the unsupported step from lacking formal dereference to predicting a measurable improvement from locality; that is the conjecture's missing concretization and the experiment's main burden.
