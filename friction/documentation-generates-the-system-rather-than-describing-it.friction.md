# Friction check: Attempted recovery identifies informational gaps, not provenance or authority

**Note:** kb/notes/documentation-generates-the-system-rather-than-describing-it.md
**Central claim (one sentence):** Attempted recovery, scoped to a declared source set, decision-relevant content unit, and consumer goal, establishes only recoverability; provenance and current authority require independent evidence, and a system/documentation pair is bidirectionally irrecoverable only when each uniquely retains content the other does not determine.

## Filter
**Verdict:** SURVIVES
The claim asks recoverability, provenance, and authority to remain distinct while allowing either artifact to retain unique content. These properties can coexist: an availability assay can succeed or fail in either direction without purporting to establish production history or present governance.

## Signal — thinnest joints
1. **“Failure to recover one therefore establishes an information gap in the tested sources”** — UNSUPPORTED — A failed attempt can also result from an incapable reconstructor, a poor reconstruction procedure, or failure to assemble dependencies that were present. The note defines faithful recovery but gives no completeness condition under which failure licenses the conclusion that the declared sources do not determine the content.
2. **“Once the production relation is known, that distinction settles maintenance and disposal.”** — UNSUPPORTED — Derivation versus commitment does not settle whether another source preserves the content, whether the artifact currently governs changes, whether recomputation is reliable or costly, or whether the content is correct. The note later makes those factors independent, so the production distinction alone cannot settle the stated decisions.
3. **“Each success establishes recoverability only relative to the declared source set, content unit, and consumer goal.”** — THIN — An observed success establishes that the reconstruction setup produced the content, but the setup can also contribute undeclared model knowledge, tooling, or chance. The fidelity requirement constrains the output; it does not show how the assay attributes that output specifically to the declared sources.
4. **“The assay must operate over the smallest decision-relevant closure that preserves those dependencies; otherwise, changing the chosen grain can change the result.”** — THIN — Distributed dependencies justify using a dependency-preserving closure, but they do not establish that there is a unique smallest closure or provide a way to find it. The note's own open question leaves this load-bearing assay boundary unresolved.

## For the human
Look first at the negative assay: specify what makes a failed reconstruction evidence of absent information rather than a limitation of the reconstructor, procedure, or chosen closure.
