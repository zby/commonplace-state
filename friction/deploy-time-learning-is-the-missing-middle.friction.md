# Friction check: Retained system-definition artifacts enable persistent deployment-time adaptation

**Note:** kb/notes/deploy-time-learning-is-the-missing-middle.md
**Central claim (one sentence):** A deployed system can learn persistently during deployment without updating model weights when deployment evidence drives the evaluation, selection, and retention of behavior-shaping system-definition changes that affect later executions.

## Filter
**Verdict:** SURVIVES
The claimed properties—production during deployment, evidence-responsive selection, persistence across runs, behavior change, and storage outside model weights—can coexist in one artifact-revision loop.

## Signal — thinnest joints
1. **“A human may still propose or approve the selected change. What matters is that deployment evidence bears on its selection and that the retained result affects later executions.”** — UNSUPPORTED — Evidence-responsive human editing can still be evidence-based engineering; the note does not establish that the deployed system owns the adaptation process or include the human within its learning boundary.
2. **“A proposal-selection improvement loop requires search, evaluation, and operative retention; these operations distinguish learning from arbitrary durable maintenance.”** — THIN — These operations exclude arbitrary persistence, but the note does not show that they are sufficient to distinguish system learning from an externally operated optimization process.
3. **“The relevant unit is the deployed system, not the model alone, because prompts, retrieval, tools, validators, and runtime policy jointly determine behavior.”** — THIN — Jointly determining behavior establishes the system's causal scope, but it does not by itself establish that this whole unit possesses the capacity to adapt rather than merely being modified.
4. **“Validation becomes more tractable only when the artifact's actual authority and dependency neighborhood bound the consequences that must be checked.”** — THIN — Bounding the consequence set narrows the validation surface, but tractability also depends on that set's size, observability, and available evaluation methods, which the note does not establish.
5. **“Progressive disclosure, skill routing, and retrieval economize each bounded context by selecting relevant artifacts across executions. This expands what the deployed system can retain and activate over time.”** — HOLDS — Given a persistent artifact library, routing different stored artifacts into bounded executions supports activation of more retained behavior-shaping state than any one context can contain.

## For the human
Concretize who or what owns proposal, evaluation, and incorporation when a human participates, because that boundary determines whether the retained change is deployed-system learning or evidence-based engineering.
