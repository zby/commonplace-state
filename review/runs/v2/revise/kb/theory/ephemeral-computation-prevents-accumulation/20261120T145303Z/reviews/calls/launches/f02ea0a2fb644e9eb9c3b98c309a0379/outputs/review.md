---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "It prevents learning across runs only when nothing learned from the episode survives elsewhere and affects later work."
    reason: "Weaken the 'only when' claim and distinguish necessary causal survival from sufficient cross-run accumulation: surviving state that causally affects later runs can still fail to accumulate when disposal-time extraction is lossy, retained lessons go stale or overfit, or regeneration drifts across unarticulated invariants."
  - scope: passage
    quotes:
      - "Discarding a generated artifact avoids maintaining that particular reusable object: version compatibility, stale assumptions, dependencies, and retrieval need not be managed for it."
    reason: "Account for maintenance migration onto substitute carriers: moving operational knowledge into retained theories, dependency accounts, examples, or tests transfers version compatibility, staleness, dependency, and retrieval burdens to those carriers—often with weaker automated verification—rather than eliminating them."
  - scope: passage
    quotes:
      - "That motivates retaining the knowledge; it does not require every version of the code to be its sole carrier."
    reason: "Bound carrier substitutability against disposal-time epistemic asymmetry and compositional depth: specify when operational knowledge can be losslessly extracted at disposal time (explicit, separable, shallow lessons) versus when discarding the working artifact destroys unarticulated invariants or caps hierarchical tool accumulation."
  - scope: passage
    quotes:
      - "[Codification](./definitions/codification.md) assigns an operation to a symbolic consumer. Retention determines whether an artifact or its effects remain available later. A generated program is symbolic while it runs even when it is deleted afterward."
    reason: "Align with the linked definition of codification and drop the claim that retention and codification are cleanly independent for recurring operations: regenerating a temporary script from natural language on each run keeps the recurring operation under model reinterpretation rather than holding consumers to a governing reference, so code-extraction codification of a recurring operation depends on retaining the extracted artifact (or pinning the generator)."
  - scope: document
    quotes: []
    reason: "Resolve the motte-and-bailey gap between the tautological headline ('Discarding all experience-dependent state prevents cross-run accumulation', which holds by causal isolation alone) and the substantive claim in the body about when alternative retained carriers can replace retained artifacts without degrading accumulation."
outcome: report
attack-outcome: partially lands
---

# Critique: Discarding all experience-dependent state prevents cross-run accumulation

**Note:** `kb/theory/ephemeral-computation-prevents-accumulation.md`
**Central commitment:** Discarding an intermediate generated artifact only removes one reuse path (while avoiding that object's maintenance costs); cross-run accumulation fails only when no experience-dependent state survives elsewhere in the deployed system to affect later work, because other retained carriers (theories, examples, tests, dependency accounts) can preserve what was learned.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The strongest informed opposition comes from production software engineering, software-evolution theory (Peter Naur's account of programming as theory building, Hyrum's Law, and Andreas Kirsch's actual critique of ephemeral software), and cumulative tool-building architectures in continual learning.

The objection starts by exposing a **motte-and-bailey structure** at the heart of the note:

- **The motte (the title and Scope):** "Discarding all experience-dependent state prevents cross-run accumulation," scoped to assume "no experience-dependent causal path into the later run." Once every possible causal channel (code, theories, examples, tests, policies, weights, external records, persistent environment state, changed inputs) is folded into "experience-dependent state," the headline claim reduces to a vacuous tautology of causal isolation. No critic of ephemeral software disputes that two causally isolated runs cannot causally influence each other.
- **The bailey (the substantive claim doing all the architectural work):** Ephemeral computation merely drops one reuse path and avoids maintaining that object ("version compatibility, stale assumptions, dependencies, and retrieval need not be managed for it"), while cross-run learning persists via alternative retained carriers ("a theory, examples, test results, a policy... a corrected dependency account, or a test for later scripts"), turning artifact retention into a straightforward cost trade-off.

That substantive carrier-substitutability claim fails across cumulative, coupled software and agent workflows for three structural reasons—and the note's explicit "only when" formulation ("It prevents learning across runs only when nothing learned from the episode survives elsewhere and affects later work") is false even on its own terms:

1. **Disposal-time epistemic asymmetry makes extraction structurally lossy.** Retaining "the result that matters" or "a corrected dependency account" after deleting a generated program presupposes that the system knows *at disposal time* which parts of the artifact's behavior carry load-bearing operational knowledge. In non-trivial software, much of what makes an artifact work is implicit, coupled, and discovered only retroactively: undocumented dependency quirks absorbed into control flow, ordering and timing tolerances, and unspecified observable behaviors that downstream callers come to depend on (Hyrum's Law). Keeping the artifact preserves both explicitly recognized lessons and unarticulated working invariants, and lets future runs diff and debug against exact prior behavior. Discarding it strips away everything that was not already noticed and articulated in that episode. When later runs regenerate from the retained summary and tests, they sample a different point in an underconstrained solution space, turning supposed accumulation into silent behavioral drift and recurring rediscovery.
2. **The maintenance-avoidance claim commits a conservation-of-complexity fallacy.** The note asserts that discarding a generated artifact avoids managing version compatibility, stale assumptions, dependencies, and retrieval for it. Those burdens do not belong to code as such; they belong to *retained operational knowledge*. The moment a system substitutes retained dependency accounts, edge-case notes, examples, policies, and test suites rich enough to sustain accumulation, all four maintenance costs migrate onto those substitute carriers—typically on worse terms. Dependency accounts and tests still break under upstream version changes; retained prose theories and policies accumulate stale assumptions that fail silently because they cannot be type-checked or executed; and an expanding corpus of lessons and tests still requires retrieval and conflict resolution under bounded context. The architecture faces a dilemma the note never confronts: either the substitute carrier stays lightweight (and is too lossy to prevent regeneration drift), or it grows detailed enough to preserve operational continuity (and reproduces or worsens the maintenance burden of keeping the artifact, without an authoritative implementation).
3. **Discarding artifacts imposes a ceiling on compositional depth.** Cross-run accumulation in engineering and continual learning is not merely adding flat tips to a prompt for one-shot scripts; it is hierarchical ratcheting—building layer $N+1$ atop stabilized, already-verified artifacts from layers $1 \dots N$ whose internal complexity is encapsulated behind an interface. If lower-layer artifacts are discarded and regenerated from retained descriptions on every run, regeneration cost and context load grow with the entire accumulated dependency history instead of staying bounded, and small behavioral deviations per regeneration compound across composed layers.
4. **Surviving causal state does not guarantee accumulation.** Even when experience-dependent state survives and causally affects later runs, cross-run accumulation still fails whenever extracted lessons are stale, overfitted to one episode, unvalidated, or lossy enough to induce oscillation—contradicting the note's "only when" framing (and the selection requirements stated in the note's own linked sibling on deployment-time adaptation).

**Why the attack partially lands rather than completely refuting the note:** The note's narrower boundary correction survives. Discarding an exploratory or diagnostic one-shot artifact does *not* automatically erase all learning when the episode's contribution is an explicit, self-contained, shallow finding (such as exposing a bug and adding a regression test or correcting one documented fact). The critique defeats the broader claim that alternative carriers cleanly substitute for retained artifacts while dodging their maintenance costs, and defeats the "only when" characterization of accumulation failure.

## How the note engages it

**Partially engaged.**

- **Lossy extraction and regeneration drift:** Glancingly touched in `## What discarding saves and costs` (lines 47–49: *"What disposal removes is the ability to inspect or rerun those exact bytes later, unless another record preserves them. Independent regeneration need not reproduce the same program"*) and in the brief response to Kirsch (lines 56–60: *"That motivates retaining the knowledge; it does not require every version of the code to be its sole carrier"*). This treats disposal as losing byte-level reproducibility rather than confronting the epistemic impossibility of extracting unarticulated invariants before they are known to matter, or the resulting drift across regenerations.
- **Conservation of maintenance costs:** Directly contradicted rather than engaged. Lines 39–41 credit disposal with avoiding *"version compatibility, stale assumptions, dependencies, and retrieval"* without recognizing that the substitute retained carriers needed for cross-run accumulation inherit all four costs.
- **Compositional-depth ceiling:** Unengaged. Every example in the note treats a single isolated script rather than stacked, mutually dependent artifacts.
- **"Only when" overclaim vs. drift/negative transfer:** Internally inconsistent. The diagram (line 33) carefully hedges to `"artifact discarded + retained useful lesson -> learning remains possible"`, whereas the description (line 2) and opening paragraph (lines 11–13) assert the stronger `"only when"` claim that equates non-accumulation with zero surviving causal state.

## Constructive findings

- **Replace the "only when" claim with a necessary-condition statement:** State clearly that zero surviving causal state is *sufficient* to prevent cross-run accumulation (not the *only* way it fails), and acknowledge that surviving state still fails to accumulate when extraction is lossy, unvalidated, or stale.
- **Close the motte-and-bailey between title and body:** Either narrow the note honestly to the system-boundary distinction (separating one-shot artifact disposal from zero deployed-system state) or explicitly defend the conditions under which non-code carriers can preserve operational knowledge across runs.
- **Drop the asymmetric maintenance-avoidance claim:** Revise lines 39–41 to state that discarding an artifact removes maintenance of *that implementation* only by shifting compatibility, staleness, dependency, and retrieval management onto whatever substitute carriers (tests, theories, dependency notes) preserve the lesson—and note the verification trade-off when those carriers are prose rather than executable code.
- **State the boundary of carrier substitutability:** Identify the regime where discarding an artifact plus keeping a lesson works (explicit, separable, low-coupling, shallow-depth findings) versus where artifact retention is structurally load-bearing (coupled implicit invariants, Hyrum's-law interface continuity, and compositionally deep stacks).
- **Correct the codification-vs-retention claim (see Secondary objections):** Align `## Retention and codification are different choices` with `./definitions/codification.md` so it does not claim that regenerating temporary scripts from natural language codifies a recurring operation.

## Secondary objections

- **Retention and codification are not cleanly independent choices for a recurring operation (`lines 62–76`).** The note claims *"Codification assigns an operation to a symbolic consumer. Retention determines whether an artifact or its effects remain available later. A generated program is symbolic while it runs even when it is deleted afterward,"* and suggests combining retained prose theory/examples with short-lived generated implementations. Under the note's own linked definition (`./definitions/codification.md`), however, codification moves a rule or operation into symbolic form so that consumers are held to a governing semantic reference *instead of a model reinterpreting the text on each use* (and includes adopting a pinned model package as an opaque reference, not merely assigning to a symbolic consumer). If a system retains only a natural-language theory and regenerates a throwaway script on every run, the recurring operation is *not* codified: each run still routes through natural-language reinterpretation and can emit a different program. A temporary script uses symbolic execution inside a single step, but code-extraction codification across runs depends on retaining the extracted symbolic artifact.
