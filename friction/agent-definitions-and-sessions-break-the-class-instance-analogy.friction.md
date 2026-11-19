# Friction check: Instantiation alone cannot model agent learning across sessions

**Note:** kb/notes/agent-definitions-and-sessions-break-the-class-instance-analogy.md
**Central claim (one sentence):** The class/instance analogy models how a durable agent definition initializes disposable sessions, but cross-session learning additionally requires a governed feedback relation that selects session-produced changes for later definitions and can revise where reusable content is retained and loaded.

## Filter
**Verdict:** SURVIVES

The startup relation, selected feedback relation, and revisable placement policy can coexist: the first creates a session from durable structure, while the second conditionally changes the durable structure or its loading boundary for later sessions.

## Signal — thinnest joints
1. **“It becomes learning when a selection process makes it operative for later runs.”** — UNSUPPORTED — Making a mutation operative establishes retention, not improvement; unless the selection process is constrained by evidence and evaluation, the same mechanism can retain a neutral or harmful change.
2. **“That is why routing stays architectural rather than learned within a fresh run.”** — UNSUPPORTED — Disposable sessions and absent prior familiarity establish a need to supply routing again at startup, but they do not prevent a fresh session from learning routes into session-local state during the run.
3. **“Learning across sessions requires a second relation … and the system may revise where reusable content belongs.”** — THIN — The second relation is necessary for session experience to affect later sessions, but the argument establishes only that revising placement is possible and sometimes useful, not that a revisable placement policy is required for every instance of cross-session learning; content can be updated within a fixed store and loading path.
4. **“A fixed class/instance shorthand tends to hide this policy decision, even when the implementation language can express the move.”** — THIN — Bare instantiation leaves placement policy unspecified, but nothing stated shows that the analogy biases users toward fixed placement rather than merely failing to represent placement at all.
5. **“If later sessions repeatedly reconstruct the same material, that recurrence is evidence for considering promotion.”** — HOLDS — Repeated reconstruction supports considering reuse, and the deliberately weak conclusion leaves rediscovery cost, context cost, task specificity, and maintenance burden for the later decision.

## For the human
Look first at the transition from retained mutation to learning: the note names evidence and evaluation as necessary, then lets selection-plus-retention carry the conclusion without specifying what makes that selection improvement-sensitive.
