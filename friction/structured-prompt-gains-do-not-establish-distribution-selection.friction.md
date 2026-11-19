# Friction check: Structured-prompt gains do not establish training-distribution selection

**Note:** kb/notes/structured-prompt-gains-do-not-establish-distribution-selection.md
**Central claim (one sentence):** Improvements observed under structured prompting do not by themselves identify selection of higher-quality training-data patterns as the cause because formatting compliance, added computation, and task decomposition can produce the same observations.

## Filter
**Verdict:** SURVIVES

## Signal — thinnest joints
1. **“A prompt or KB template should be justified by the work its structure requires or exposes”** — UNSUPPORTED — Failure to identify training-distribution selection does not establish this exclusive basis for adoption; a repeatable task-specific benefit could justify a template even while its causal mechanism remains unknown.
2. **“The distribution-selection hypothesis would gain distinctive support only if the structural or genre cue improved task quality beyond what the process and format controls explain.”** — THIN — The proposed controls remove the named rivals, but a residual heading effect would still not distinguish training-distribution selection from unmodeled mechanisms such as instruction salience or a change in inference-time representation.
3. **“This result makes the distribution-selection hypothesis plausible: reorganizing a task may change which learned structure a bounded model can use.”** — THIN — A bounded learner extracting different structure from differently ordered training data supplies an analogy, but the note does not give the bridge from that learning result to an already-trained model using different learned structure under an inference-time prompt.
4. **“These rival mechanisms predict many of the same observations.”** — HOLDS — The examples show that format constraint, required intermediate checks, and genre-driven style can all change outputs without selecting a higher-quality training subset, so prompt gains alone underdetermine the claimed cause.

## For the human
Look first at whether the design consequence merely rejects an unproven causal rationale or also claims that every useful template must expose a named piece of work; only the former follows from the mechanism critique.
