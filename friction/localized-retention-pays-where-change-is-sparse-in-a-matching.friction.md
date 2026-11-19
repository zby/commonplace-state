# Friction check: Localized retention pays when sparse changes have bounded impact in a matching decomposition

**Note:** kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md
**Central claim (one sentence):** Localized retention reduces revision and validation work when a decomposition fixed before the change aligns addressable units with a sparse change and gives the affected units an explicit, small dependency closure.

## Filter
**Verdict:** SURVIVES

The note commits to a coherent conditional rather than promising localization from addressability alone: matching boundaries keep the edit footprint sparse, explicit dependencies identify what must be checked, and bounded impact keeps that check set small. Its substrate neutrality and its qualification that the decomposition must precede the observed change are compatible with that claim.

## Signal — thinnest joints
1. **“when change is dense and diffuse — a broad distributional drift that moves everything a little — no semantic decomposition is sparse”** — UNSUPPORTED — A change that is diffuse at one behavioral or representational level can still be captured by a small number of higher-level units, such as a shared policy, transformation, or global parameter; the example does not establish density across every semantic decomposition.
2. **“One authoring rule follows: content on different change schedules should remain independently editable and checkable.”** — THIN — The localization criterion favors schedule-aligned boundaries when revision cost is the deciding objective, but the rule does not account for invariants that require the content to change together or for the routing, consistency, and coordination costs that the preceding paragraph itself says can outweigh local advantages.
3. **“When an artifact couples them, its fast-changing part forces revisits while its slow-changing part loses credibility.”** — THIN — Coupling can force the slow-changing content to be rechecked, but repeated checking does not by itself make that content less credible; the note needs a mechanism such as stale attestations, skipped validation, or reader uncertainty to connect revisit frequency to lost credibility.
4. **“Explicit dependencies — knowing what cites, loads, or tests each unit — makes the impact closure computable.”** — THIN — Citation, loading, and test relations make a declared structural closure computable, but the inference assumes those recorded relations are complete proxies for actual behavioral dependence; hidden semantic coupling would leave the computed closure smaller than the true validation scope.
5. **“A representation whose units correspond to those commitments lets the system express, inspect, and roll back the change by editing the k affected units.”** — THIN — Matching units supports a k-unit edit footprint, but inspectability and rollback also require preserved versions, suitable tooling, and independently reversible semantics; correspondence alone does not provide all three capabilities.

## For the human
Look first at the universal jump from diffuse change to the absence of any sparse semantic decomposition; either bound that claim to the chosen decomposition or show why a higher-level unit cannot absorb the drift.
