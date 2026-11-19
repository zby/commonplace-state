# Premise decomposition: Instantiation alone cannot model agent learning across sessions

**Note:** `kb/notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md`
**Register:** claim
**Central commitment (one sentence):** Instantiation alone models only session startup, so cross-session agent learning needs an additional retained, evidence-responsive update relation to later starting structure, and that relation may also revise where reusable content is stored or loaded.

## Premises and counterexamples
1. **For a process to count as learning across sessions, something produced or evidenced in one session must persist in a way that changes later sessions.** — HOLDS — An active counterexample hunt did not find a genuine case of cross-session learning where later sessions inherit no changed retained state, artifact, or policy from earlier ones.
2. **Instantiation alone is a one-way startup relation from a durable definition to a session and does not itself supply a retained path from session evidence back into what later sessions inherit.** — HOLDS — Putative counterexamples such as reflective mutation, monkey-patching, or hot code swap all add a write-back mechanism beyond mere startup instantiation rather than showing startup alone is sufficient.
3. **In the agent systems the note targets, retained artifacts such as skills, memory stores, routing rules, and validators are part of the behavior-shaping starting structure for later runs, so changing them can change later capacity.** — HOLDS — No concrete counterexample showed these retained and reloaded artifacts to be behaviorally inert once later sessions consult or load them.
4. **Episode-scoped influence from material introduced during one session is not by itself cross-session learning unless some resulting effect is retained for later sessions.** — HOLDS — A note, prompt fragment, or derivation that helps only the current run but leaves later runs unchanged does not defeat the note's contrast between current-session guidance and durable learning.
5. **Reusable-content placement among retrieval, startup loading, durable retention, and local derivation can be a writable policy whose revision changes later-session behavior or budget, so omitting placement can omit part of the update surface.** — HOLDS — A concrete counterexample hunt did not overturn the weaker claim the note actually needs here: not that every learner must revise placement, but that some agent systems can learn by revising it.
6. **Reflective or stateful computational systems do not rescue instantiation-alone as a full learning model, because their learning-relevant behavior still depends on a retained state or definition update relation in addition to startup.** — HOLDS — Persistent object graphs and state machines can model the second relation, but that confirms the note's distinction instead of refuting it.

## For the human
Look first at premise 5: it is the easiest place for scope drift, so keep clear that placement revision is a possible update surface, not a requirement for every cross-session learner.
