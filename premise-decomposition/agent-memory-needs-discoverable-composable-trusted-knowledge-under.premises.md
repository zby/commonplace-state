# Premise decomposition: Agent memory needs discoverable, composable, trusted knowledge under bounded context

**Note:** `kb/notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md`
**Register:** claim
**Central commitment (one sentence):** Remembered knowledge improves future work under bounded context only when the remembered material is discoverable, composable, and trusted, with activation and loadability treated as separate concerns.

## Premises and counterexamples
1. **Discoverability is necessary: remembered knowledge must provide a usable route into working context that does not require scanning the entire store.** — DEFEATED — A small memory store can fit comfortably in bounded context and be scanned wholesale on every task; a relevant memory in that store can still change the outcome even though it has no separate retrieval handle and violates the note's "without scanning the entire store" condition. — GLOBAL — instance
2. **Trusted is necessary: remembered knowledge must carry enough role/status evidence for the agent to calibrate reliance without redoing the original work each time.** — DEFEATED — A saved hunch such as "check the auth cache first" can improve the next debugging session even with no provenance or review signal, because the agent can test it first as a cheap hypothesis and still benefit. — GLOBAL — instance
3. **If remembered knowledge never alters the material available inside the task's bounded working context, it cannot alter what the agent does on that task.** — HOLDS — Active counterexample hunt did not find a case where explicit remembered knowledge improved task behavior without being represented either directly in working context or through an always-loaded control surface the note already treats as part of that working material.
4. **Composable knowledge is necessary in the note's broad sense: once remembered material is what the agent is relying on, it must either integrate with task context or be usable as a coherent unit.** — HOLDS — The best counterexamples depended on some other artifact or retrieval mechanism supplying the missing scope and conditions; once that extra structure is removed, the remembered item stops being something the agent can reliably use as remembered knowledge.
5. **Artifact-level memory failures can be usefully separated from system-level activation failures and from loadability failures, even if the boundary is only diagnostic rather than absolute.** — DOUBTFUL — Hybrid cases exist where usability depends jointly on the artifact and the retriever or scheduler, so a miss is not cleanly attributable to remembered material alone. — LOCAL — instance

## For the human
Look first at premise 1: the note's ban on full-store scanning makes discoverability fail on small stores that can be loaded or scanned wholesale, so the necessity claim needs a scope condition if it is to survive.
