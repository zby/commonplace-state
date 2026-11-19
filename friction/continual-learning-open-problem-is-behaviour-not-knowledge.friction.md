# Friction check: Continual learning requires governing behaviour-changing writes, not just storing content

**Note:** `kb/notes/continual-learning-open-problem-is-behaviour-not-knowledge.md`
**Central claim (one sentence):** In a deployed system, continual learning is the governed selection, validation, authorization, and coordination of durable behaviour-changing updates across whatever representational forms actually control behaviour, not mere persistence of new content.

## Filter
**Verdict:** SURVIVES

The claim concretizes to one thing: once behaviour is determined by more than model weights, "continual learning" must govern writes to the whole behaviour-shaping surface rather than treat storage as sufficient. The properties it wants together — durable adaptation, deployment-time use, cross-form scope, and regression control — are not internally contradictory.

## Signal — thinnest joints
1. **"deployment evidence arrives online and is often sparse, so candidate writes must be cheap to propose and install; some lessons must take effect before a full retraining cycle"** — UNSUPPORTED — Sparse online evidence can motivate faster adaptation, but it does not by itself establish the operational requirement that writes be cheap to install or that waiting for retraining is unacceptable in the target class of systems.
2. **"Mature release engineering already governs hand-authored readable changes. Continual-learning systems must close the corresponding loop from deployment evidence at the cadence their environment requires."** — THIN — The analogy suggests a governance pattern, but the note does not show that release-engineering control over human-authored changes transfers cleanly to autonomous deployment-time learning across parametric, natural-language, and symbolic writes.
3. **"The forms differ in installation cost and verifiability, so a learning loop must decide which form a lesson belongs in and coordinate whichever forms that update touches."** — THIN — Different costs and verification properties do support form choice pressure, but the step to a mandatory coordination layer is asserted more than demonstrated; some lessons might be form-local without requiring explicit cross-form coordination.
4. **"Behavioral authority belongs to a consumption path, not to stored bytes... Persistence alone therefore does not create a governed behaviour-changing write."** — HOLDS — If stored content affects behaviour only through the path that interprets or enforces it, then mere storage is not yet a governed write with behavioural force.
5. **"if prompts, tools, validators, and runtime policy also determine behaviour, then an updater restricted to weights freezes consequential choices outside its reach"** — HOLDS — Given the note's system boundary, the conclusion follows: a weight-only updater cannot revise other behaviour-determining components.

## For the human
Look first at the online-sparse-evidence ⇒ cheap-install / pre-retraining-update step; that is where the note most needs explicit scope or a concrete deployment class.
