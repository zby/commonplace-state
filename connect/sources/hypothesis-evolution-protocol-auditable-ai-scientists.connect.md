---
description: "Pre-ingest discovery for HEP: hypothesis lifecycles, evidence-linked revision, and the boundary between auditability and warrant"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/hypothesis-evolution-protocol-auditable-ai-scientists.md"
source_has_frontmatter: true
date: "2026-09-19"
depth: standard
---

# Connection Report: Toward Auditable AI Scientists

**Source:** [Hypothesis Evolution Protocol snapshot](../../../../sources/.snapshots/hypothesis-evolution-protocol-auditable-ai-scientists.md)

Discovery-only output of `cp-skill-connect`, produced by GPT-6. Proposed outbound edges belong to the future matching ingest, never to the immutable snapshot. No library edges were authored.

## Discovery Trace

- Read the source in full and the source collection, report collection, and connect-report contracts. HEP retains addressable hypotheses and evidence, enforces lifecycle transitions, and elicits belief updates from the agent. It tests materials-model behavior, not physical truth or persistent cross-task learning.
- Generated the fresh title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. Broad output exceeded the display budget; recovered candidate detail with scoped descriptions, body searches, and direct reads. Regenerated the two system-collection title surfaces separately. No external search or semantic service was used.
- Ran `rg '^description:.*(hypothes|falsif|refut|belief|scientific|audit|lineage)' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. This selected discovery lifecycle, failure explanations, superseded beliefs, POPPER, MDA, and Stash; generic audit tooling was not retained.
- Ran `rg -n 'hypothes|belief|refut|audit'` across the same five collections. This broad pass was noisy; evaluated its candidate neighborhoods through narrower direct reads rather than treating lexical matches as connections. No scores were available.
- **Notes:** Read `kb/notes/README.md`; inspected the learning-theory and tags heads with `rg -n 'hypothesis|scientific|lineage|falsif'`. The source has no tags, so no matching-tag completeness shortcut applies. Read discovery lifecycle, reflective theory refinement, failure explanation, superseded beliefs, and reflection buys addressability. Followed reflective theory refinement's link to reflection buys addressability and the failure-explanation note's return link to the refinement framework. Kept the lifecycle, evidence-to-search, and retention distinctions; rejected a direct claim of reflective self-improvement because the hypotheses concern materials rather than the agent's own organization.
- **Reference:** Read `kb/reference/README.md`; searched `rg -n 'hypothes|evidence|certificate' kb/reference/freshness-architecture.md kb/reference/review-architecture.md`. These documents concern applicability of review evidence and execution finalization, not hypothesis truth. Rejected a routine architecture link because the shared idea of retaining evidence is too broad to earn a useful source-side edge.
- **Agent memory systems:** Read `kb/agent-memory-systems/README.md`, its title surface and scoped descriptions, then the Stash review. Kept a comparison of hypothesis promotion, confidence, and evidence mediation; did not infer that HEP establishes general memory effectiveness.
- **Agentic systems:** Read `kb/agentic-systems/README.md`, title surface and descriptions; inspected `rg -n 'hypothes|evidence|certificate' kb/agentic-systems/reviews/eigenius.md`. Kept Eigenius as a focused comparison between recorded execution, admission rules, and warrant. Other harnesses lacked a comparably specific connection.
- **Sources:** Read `kb/sources/README.md`; title and description discovery identified POPPER and MDA. Read both ingests. POPPER separates statistical validity from semantic relevance; MDA computes posteriors over explicit models. These provide useful contrasts with HEP's elicited probabilities and revisable hypotheses. Their authored links also point back to discovery lifecycle and theory-refinement questions, corroborating this neighborhood.
- **Reverse direction:** Read `kb/notes/COLLECTION.md`; its `evidenced-by` label permits the bounded reverse candidate below. No candidate proposes durable links to the local snapshot.
- **External:** The source URL is already supplied. Retained only that provenance candidate; external prospecting was skipped. Instructions and workshops are excluded by the source contract.

## Connections Found

- [Original paper](https://arxiv.org/abs/2607.09195) — **derived-from**: the future ingest analyzes this captured paper; this is its external source identity.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) — **compares-with**: HEP supplies an executable hypothesis-state lifecycle with evidence attachment, revision, support, refutation, and dormancy. Comparing it with the six-phase KB model makes visible that terminal status and integration are separate obligations; HEP's numeric thresholds are its own workflow choices.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) — **is-evidence-for**: the paper's A2BB′O6 example reports two refuted mechanisms redirecting search toward an A-site exception. This is a concrete same-run continuation trace, though no intervention isolates the causal role of the retained explanation.
- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md) — **compares-with**: HEP retains every hypothesis event while marking current beliefs supported, refuted, or dormant. This distinguishes historical audit value from current epistemic standing and prevents reading append-only retention as continued endorsement.
- [Reflective theory refinement needs interpretation, retention, and independent read-back](../../../../notes/reflective-theory-refinement-needs-interpretation-and-retention.md) — **compares-with**: HEP provides stable hypothesis objects and attached simulation outcomes, but its agent certifies evidence itself and its theories concern an external target. It is a useful boundary case for addressability and read-back without establishing reflective membership or independent semantic validation.
- [Automated hypothesis validation with agentic sequential falsifications](../../../../sources/automated-hypothesis-validation-sequential-falsifications.ingest.md) — **compares-with**: POPPER revises tests for a supplied main hypothesis and conditionally controls statistical error; HEP revises the hypotheses themselves but uses elicited beliefs. Compare what changes and what warrants acceptance rather than treating both numerical decisions as equivalent.
- [Model Discovery Agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) — **compares-with**: MDA computes Bayesian posteriors and uses explicit forward models, while HEP asks the agent to supply belief values with rationales. The shared hypothesis–experiment loop therefore has materially different assessment machinery and failure modes.
- [Stash](../../../../agent-memory-systems/reviews/stash.md) — **compares-with**: both systems expose explicit hypothesis and evidence records with confidence and status changes. Stash promotes hypotheses into facts through its memory service; HEP preserves an event history and gates verdicts on elicited probabilities. The comparison isolates promotion authority from the mere presence of hypothesis storage.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) — **compares-with**: both distinguish durable records from admission decisions, but Eigenius checks justification certificates on named load paths whereas HEP enforces lifecycle and belief thresholds over agent-certified evidence. Neither should be read as universally certifying truth.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) → future matching ingest — **evidenced-by**: the reported A2BB′O6 refutation-and-redirection sequence can supply a bounded illustrative trace. Author only after the ingest exists and the needed source support is retained; do not claim an ablation or independent replication.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) — rejected as direct evidence for reflection: HEP makes external-domain hypotheses addressable but does not show a self-representation changing the agent's organization. The more explicit boundary comparison with reflective theory refinement is sufficient.
- [Freshness architecture](../../../../reference/freshness-architecture.md) — rejected as a source-side connection: retained applicability baselines and hypothesis beliefs answer different questions; shared event/evidence vocabulary alone adds little.
- [Review architecture](../../../../reference/review-architecture.md) — rejected as a source-side connection: transactional completion of assay jobs is too distant from HEP's epistemic lifecycle to justify a generic companion link.

## Index Membership

None. A paper ingest does not itself qualify as a new implementation-grounded system analysis.

## Synthesis Opportunities

None. The retained lifecycle and interpretation/read-back notes already distinguish the functions needed here.

## Maintenance Observations

None

## Flags

- Beliefs are elicited, not calibrated or mechanically computed posteriors. Evidence validation is the agent's certification, with independent auditing proposed as future work.
- The comparison changes the protocol and hypothesis-discipline prompt together; baseline and HEP also use different stopping criteria. The reported three-run comparisons do not isolate registry structure from prompting.
- Generality is across three questions about one fixed machine-learned interatomic potential; correspondence to established materials physics remains untested.
- No hypothesis beginning above prior 0.7 was later flipped. The authors explicitly leave open whether those priors were good or tests insufficiently severe.
- Code is promised upon publication; this discovery pass is paper-grounded, not an implementation review.
