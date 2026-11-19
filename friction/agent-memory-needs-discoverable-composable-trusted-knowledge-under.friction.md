# Friction check: Agent memory needs discoverable, composable, trusted knowledge under bounded context

**Note:** kb/notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md
**Central claim (one sentence):** Remembered knowledge can improve future work under bounded context only if it is discoverable when relevant, composable with the current task, and accompanied by enough status evidence for calibrated reliance, although those three conditions are not sufficient for a complete memory system.

## Filter
**Verdict:** SURVIVES
The three demanded properties can coexist: one remembered artifact can carry a retrieval handle, enough application structure, and calibrated status evidence, while the note leaves loadability and system operation as additional constraints rather than requiring any one property to displace another.

## Signal — thinnest joints
1. **“Remembered material can satisfy all three and still be too large or expensive to place in bounded context. When that cost follows from the material's size or representation, loadability is a separate artifact-level property.”** — UNSUPPORTED — Discoverability was defined as a usable route “into working context,” so material that cannot be placed there appears to lack that route; the note needs to concretize whether discoverability ends at locating a reference or includes making its payload available before it can establish loadability as separate.
2. **“These failure modes yield three necessary artifact-quality tests: remembered knowledge must be discoverable, composable, and trusted.”** — UNSUPPORTED — The three examples establish possible ways stored knowledge can fail, but they do not establish that every successful memory must itself supply all three properties rather than receiving missing structure, confidence, or routing from task context and system machinery; that matters because the conclusion classifies the tests as artifact quality.
3. **“A failure at any point breaks the path from storage to contextual competence.”** — UNSUPPORTED — Describing discoverability, composition, and reliance as a sequence does not show that an apparent artifact-level failure cannot be repaired at use time by search, restructuring, corroboration, or direct checking while the remembered material still changes the outcome.
4. **“Discoverability concerns whether remembered knowledge provides a usable route into context; activation concerns whether the system follows that route.”** — THIN — The affordance-versus-execution distinction is plausible, but the note also counts indexes, placement, and a context engine among discoverability mechanisms, so it supplies no operational test for deciding when a missed cue means that no usable route existed and when a scheduler merely failed to follow one.
5. **“Trust determines how much weight it should receive.”** — THIN — Stored rationale, provenance, status, and review signals can constrain reliance, but the weight appropriate in a particular task also depends on current evidence, stakes, and conflicts with other knowledge; the note does not establish that the remembered knowledge's trust signals determine that weight rather than inform it.

## For the human
Look first at whether a discoverability handle only locates remembered material or must also make its payload usable in bounded context, because that missing boundary controls both the separation from loadability and the claim that the triad consists of necessary artifact-quality tests.
