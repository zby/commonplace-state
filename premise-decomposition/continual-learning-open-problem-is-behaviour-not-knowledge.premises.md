# Premise decomposition: Continual learning requires governing behaviour-changing writes, not just storing content

**Note:** kb/notes/continual-learning-open-problem-is-behaviour-not-knowledge.md
**Register:** claim
**Central commitment (one sentence):** For deployed systems, continual learning requires governance of durable behaviour-changing updates — selecting, validating, authorizing, and coordinating writes across the forms that control behaviour — rather than merely storing new content.

## Premises and counterexamples
1. **In deployed systems, continual learning is about durable changes in future adaptive behaviour, not just about accumulating retained content.** — DOUBTFUL — Much accepted continual-learning work still counts sequential adaptation inside one model as continual learning even when the system adds no explicit governance layer, so this behavioural framing is plausible but not the only live boundary. — LOCAL
2. **Persisting content by itself does not determine which retained item will shape behaviour or with what authority.** — HOLDS — The strongest apparent counterexamples rely on writing into an already authoritative slot or policy path, which concedes that authority comes from the consumption path rather than from persistence alone.
3. **When prompts, tools, validators, or runtime policy also determine behaviour, a learning loop restricted to weight updates leaves consequential behaviour-changing choices outside its reach.** — HOLDS — The counterexample hunt mainly finds systems that do not satisfy the premise's antecedent (single-form systems), not systems where the antecedent holds but weights-only updating is still sufficient.
4. **Deployment-time adaptation often needs cheap-to-install candidate writes and regression checks before a full retraining cycle.** — DOUBTFUL — Some deployed continual-learning loops can update safely in delayed offline batches from accumulated traces, so immediacy and install-during-deployment are not necessary in every case. — LOCAL
5. **For deployed continual-learning systems, the main unresolved problem is governance of behaviour-changing writes rather than storage or activation of retained knowledge.** — DEFEATED — A retrieval-centered deployed agent with a fixed, already-authorized memory write path can still fail chiefly because it cannot decide what to remember or cannot reliably reactivate the right retained item later; there the dominant open problem remains storage-and-activation behaviour, not cross-form governance. — GLOBAL
6. **Human release engineering for readable artifacts does not already solve the autonomous version of this problem.** — HOLDS — Existing release pipelines can validate and ship human-authored changes, but they do not by themselves choose and authorize behaviour-changing writes from online deployment evidence.

## For the human
Look first at premise 5: if some deployed continual-learning systems keep a fixed authority path and still bottleneck on memory selection or activation, the title claim overstates governance as the open problem.
