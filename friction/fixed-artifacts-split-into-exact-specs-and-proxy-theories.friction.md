# Friction check: Exact implementation does not validate a requirement against its objective

**Note:** kb/notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md
**Central claim (one sentence):** On a named artifact–requirement–objective path, exact conformance of an artifact to its immediate requirement neither warrants that requirement as a proxy for the objective nor disappears when the proxy link fails.

## Filter
**Verdict:** SURVIVES

Local exactness, upstream conjectural status, and preservation of local correctness after upstream failure can coexist because they apply to different links on the same declared path; the note does not require one relation to be both exact and conjectural.

## Signal — thinnest joints
1. **“A deterministic checker establishes conformance to its target.”** — UNSUPPORTED — Determinism establishes repeatability, not the checker’s soundness, coverage, or correspondence to the immediate requirement; even an accepting result establishes conformance only after those properties and the tested scope are specified.
2. **“A conjectured decomposition instead posits that satisfying one requirement contributes to a capability nobody defined.”** — UNSUPPORTED — A decomposition can be conjectural even when the objective is precisely defined: what remains uncertain is whether the requirement contributes to it. Replacing an unwarranted link with an undefined capability collapses two distinct sources of uncertainty that the path analysis needs to keep separate.
3. **“Three questions inform confidence; none determines the classification alone” followed by “If satisfying the requirement is what the bounded analysis means by success, there is no additional proxy link inside that boundary. If the requirement only stands in for a larger capability, the link remains conjectural.”** — UNSUPPORTED — The first question, as subsequently formulated, does determine the note’s constitutive-versus-proxy classification; oracle evidence and failure location can change confidence in a conjectured link, but the note does not show how they can change whether that link exists inside the declared boundary.
4. **“Vision features such as SIFT, Haar cascades, and Canny edge detection likewise had precise mathematical specifications and useful invariants. They implemented those specifications exactly.”** — THIN — A precise algorithm or specification does not by itself establish that an implementation conforms exactly, and the named items blur the requirement with the artifact; the example needs a particular implementation and conformance evidence to witness the exact artifact–requirement link it is meant to illustrate.
5. **“[Oracle strength] is therefore one confidence factor in hardening a conjectured link, alongside coverage, failure cost, reversibility, volatility, and external dependencies.”** — THIN — The preceding argument supports separating local-oracle evidence from upstream warrant, but it does not derive this list or explain why failure cost and reversibility are confidence factors rather than decision costs that govern whether hardening is prudent at a given confidence level.

## For the human
Look first at the checker claim: concretize what an accepting oracle result warrants only after separating determinism from soundness, coverage, and correspondence to the named requirement.
