---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/steve-yegge-fences-not-sandboxes.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Fences, not Sandboxes

**Source:** [Fences, not Sandboxes](../../../../sources/.snapshots/steve-yegge-fences-not-sandboxes.md)

The snapshot is immutable. Every outbound candidate below is for the future matching ingest, `kb/sources/steve-yegge-fences-not-sandboxes.ingest.md`, not for the snapshot itself.

## Discovery Trace

**Description listing scan:**

- Read the curated heads [Notes](../../../../notes/README.md), [Tags](../../../../tags/README.md), [Reference](../../../../reference/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), [Agentic Systems](../../../../agentic-systems/README.md), and [Sources](../../../../sources/README.md). The snapshot has no `tags:` field, so no tag README was selected and no completeness-mark shortcut applied.
- Generated each authorised destination's complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over each of those five destinations. At description resolution, the strongest notes candidates concerned legal drafting, enforcement, retained deployment-time adaptation, and maintenance load. The strongest system/source candidates concerned accumulated behavioral rules, Fable-era scaffolding, behavioral contracts, policy gates, and governance kernels.
- `reference` yielded only Commonplace-specific current-state documents such as `agent-memory-coverage.md`, `commonplace-agent-memory-gap-plan.md`, and `design-rationale-management.md`. None supplied a specific reader need strong enough for the source collection's only authorised `reference` label, the intentionally sparse `see-also`.

**Topic indexes:**

- [Tags](../../../../tags/README.md) routed the claim toward the `constraining`, `deploy-time-learning`, `agent-memory`, `observability`, and `kb-maintenance` areas. Because the source itself is untagged, these were orientation cues rather than tag-complete candidate sets.
- [Agent Memory Systems](../../../../agent-memory-systems/README.md) surfaced its explicit governance comparison: Decapod uses hard proof gates and SAGE uses cryptographic gates. Decapod survived full-artifact review because its constitution fragments, promotion firewall, workunit states, and proof gates match the source's natural-language-law-to-enforcement path.
- [Agentic Systems](../../../../agentic-systems/README.md) surfaced Swamp as the closest implemented whole-system comparison: agent-authored policy, runtime checks and grants, manual gates, disposable workers, and deployment-level isolation coexist in one control plane.
- [Sources](../../../../sources/README.md) is a collection landing rather than an item index. The complete title and description scans supplied the peer-source recall surface.

**Body search:**

- Notes: `rg -n -i -m 5 'fence|sandbox|guardrail|governance|governed|policy gate|authority envelope|jurisdiction|constitution|rule of law|case law|ratif|tripwire|ratchet' kb/notes/ --glob '*.md'` and `rg -n -i -m 5 'tribal knowledge|institutional knowledge|unwritten rules|implicit (knowledge|rules)|codif|mechanical enforcement|enforceable|enforcement' kb/notes/ --glob '*.md'` kept the legal-drafting and enforcement candidates; generic sandbox and governance hits were rejected.
- Notes: `rg -n -i -m 5 'replaceable|interchangeable|amnesiac|role.*outlive|office.*outlive|authority|coordination.*text' kb/notes/ --glob '*.md'`, `rg -n -i -m 5 'software factor|agent factor|factory-to-product|multi-agent|hundreds of commits|commit.*day' kb/notes/ --glob '*.md'`, and `rg -n -i -m 5 'incident|postmortem|lesson|trace.*rule|rule.*lifecycle|warning.*enforc|progressive.*enforc' kb/notes/ --glob '*.md'` kept the retained-adaptation and maintenance candidates while rejecting the formal Greenfield software-factory definition.
- Sources: `rg -l -i 'constitution|rule of law|case law|jurisdiction|authority envelope|behavioral fence|policy gate|mechanical enforcement|governance kernel|governed.*rule|rules.*govern' kb/sources/ --glob '*.ingest.md'` and `rg -l -i 'incident.*rule|rule.*incident|postmortem.*(lesson|rule)|trace.*(lesson|rule)|accumulated behavioral rules|institutional knowledge|tribal knowledge|unwritten rules|progressive.*enforc|enforc.*lifecycle' kb/sources/ --glob '*.ingest.md'` kept Accumulated Behavioral Rules and Agent Behavioral Contracts.
- Sources: `rg -l -i 'software factor|agent factor|factory-to-product|fable|wheelhouse|mismanaged geniuses|brain from (the )?hands|multi-agent.*govern|govern.*multi-agent' kb/sources/ --glob '*.ingest.md'` kept the Fable scaffolding comparison; Fluent and the software-factory surveys were evaluated but added no connection more discriminating than the retained-adaptation note.
- Agentic systems: `rg -n -i -m 8 'govern|policy gate|permission|trust boundary|constitution|rule|enforc|sandbox|isolation|authority|review gate' kb/agentic-systems/ --glob '*.md'` and `rg -n -i -m 8 'multi-agent|office|role|worker|coordination|durable|long-lived|scheduler' kb/agentic-systems/ --glob '*.md'` kept Swamp and rejected Exo and generic coordination hits.
- Agent-memory systems: `rg -n -i -m 8 'governance|governed|constitution|policy gate|proof gate|permission|authority|role|rule|enforcement|sandbox|quarantine|consensus|ratif' kb/agent-memory-systems/ --glob '*.md'` and `rg -n -i -m 8 'trace.*(rule|lesson)|incident|postmortem|behavioral rule|precedent|lifecycle|retire|prun|drift' kb/agent-memory-systems/ --glob '*.md'` kept Decapod; Context Constitution and template-only governance systems failed the implemented-mechanism comparison.
- Reference: `rg -n -i -m 6 'governance|constitution|doctrine|authority|policy|enforcement|gate|jurisdiction|ruling|precedent|role' kb/reference/ --glob '*.md'`, `rg -n -i -m 6 'incident|postmortem|rule.*lifecycle|lifecycle.*rule|retire|supersed|ratif|drift|maintenance' kb/reference/ --glob '*.md'`, and `rg -n -i -m 6 'software factor|multi-agent|agent factory|sandbox|fence|guardrail' kb/reference/ --glob '*.md'` confirmed that the hits describe Commonplace's shipped system rather than a source-facing comparison target.

**Link following:**

- Followed [Legal drafting solves the same problem as context engineering](../../../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) into the constraining, precedent, codification, and Agent Behavioral Contracts neighborhood. This distinguished the source's deployed common-law-like account from a merely decorative legal metaphor.
- Followed [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) into governed behavior-changing writes, behavioral authority, and representational-form change. The source reports the full candidate path—incidents and rulings becoming later-consumed rules and mechanical checks—but only as a first-person account.
- Followed [Self-Improving AI Coding Agents Through Accumulated Behavioral Rules](../../../../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) into activation, Figma's precedent corpus, and rule-lifecycle limits. Its monotonic always-loaded rule file makes the contrast with Wheelhouse's staged enforcement and pruning concrete.
- Followed [Swamp](../../../../agentic-systems/reviews/swamp.md) into its memory-system companion and scheduler/LLM separation. Its code-grounded mixture of grants, checks, manual gates, remote workers, and external deployment isolation exposes the threat-model distinction hidden by “fences, not sandboxes.”
- Followed [Decapod](../../../../agent-memory-systems/reviews/decapod.md) through proof gates, context capsules, procedural promotion, and lifecycle curation. It is the closest inspected analogue to the source's reported governance substrate, while remaining a coding-agent kernel rather than a 50-agent organization.

## Connections Found

- [Legal drafting solves the same problem as context engineering](../../../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — **is-evidence-for**: the reported constitution, accumulated rulings, case-law-like precedent, jurisdiction, and text coordination among replaceable agents form a practitioner case of the note's structural law/context-engineering parallel.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) — **is-evidence-for**: Wheelhouse reportedly turns deployment incidents and human verdicts into durable doctrine, rules, gates, and programs that shape later work, while ratification, review, and retirement supply an explicit lifecycle.
- [Methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md) — **compares-with**: the source's custom → advisory/warning → written law → mechanical enforcement progression and boundary refusals provide one coupled maturation path to compare against the note's separate activation and response axes.
- [Maintenance capacity must match harmful-artifact inflow](../../../../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) — **is-evidence-for**: the reported 450 legal artifacts, obsolete rulings, cruft, and dedicated pruning role are a bounded practitioner witness that behavior-shaping artifact growth creates a separate prevention, detection, and repair load.
- [Self-Improving AI Coding Agents Through Accumulated Behavioral Rules](../../../../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) — **compares-with**: both accounts promote operational feedback into persistent behavioral rules, but the paper reports immediate human-generalized, mostly monotonic instruction growth while Wheelhouse reports staged hardening, mechanical enforcement, amendment, and retirement.
- [Claude Fable 5 Made Most of My Agent Scaffolding Obsolete](../../../../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md) — **compares-with**: two practitioner accounts of the same model-capability regime reach a productive tension—one removes compliance scripts and sync scaffolding in favor of principle-level instruction, while Wheelhouse grows hundreds of governance artifacts and more than one hundred fences.
- [Agent Behavioral Contracts for Reliable Agents](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) — **compares-with**: ABC specifies hard and soft constraints, runtime enforcement, and typed recovery upfront; Wheelhouse reportedly discovers its constitution and fence set from clarification, incidents, precedents, and repeated violations before some rules become mechanical.
- [Swamp](../../../../agentic-systems/reviews/swamp.md) — **compares-with**: Swamp is an inspected control plane where policy checks, grants, and approval gates coexist with worker isolation as a deployment concern, providing a concrete comparison for the source's claim that behavioral fences should replace sandbox-style control.
- [Decapod](../../../../agent-memory-systems/reviews/decapod.md) — **compares-with**: Decapod's inspected constitution fragments, workunit and proof gates, governed procedural promotion, ledgers, and lifecycle controls provide a code-grounded analogue to Wheelhouse's reported legal/governance substrate.

## Bidirectional Candidates

- [Legal drafting solves the same problem as context engineering](../../../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) ↔ future matching ingest — **evidenced-by** on the note side: readers testing the law/context-engineering parallel gain a concrete, explicitly bounded practitioner case rather than only the analogy and ABC formalization.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) ↔ future matching ingest — **evidenced-by** on the note side: readers gain a reported deployment pathway from incident evidence through retained rules and mechanical checks, with the source's self-report limits kept adjacent.
- [Claude Fable 5 Made Most of My Agent Scaffolding Obsolete](../../../../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md) ↔ future matching ingest — **compares-with** on the existing ingest side: the apparent disagreement about whether stronger models remove or induce scaffolding is useful from either entry point.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A software factory is family-scoped lifecycle production machinery](../../../../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — rejected as a keyword collision: Yegge uses “software factory” for one product's rapidly grown production harness, while the note intentionally reserves the term for Greenfield's family-scoped lifecycle machinery; a routine link would blur the registered boundary.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — rejected as direct support: Wheelhouse reportedly hardens rules after repeated violations, not after observing a stable favored interpretation across runs. The difference is already captured more accurately by the enforcement comparison.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) — rejected despite topical fit: the source names logs, tripwires, gates, and boundaries but does not expose enough implementation detail to establish which runtime structures make those governance operations possible.
- [Commonplace agent memory coverage](../../../../reference/agent-memory-coverage.md) — rejected because it records Commonplace's shipped surfaces and gaps; the source does not clarify that system-specific state, and `see-also` would add only generic adjacency.
- [Context Constitution](../../../../agent-memory-systems/reviews/context-constitution.md) — rejected because the reviewed repository documents a doctrine without the loader, synchronization, enforcement, or lifecycle implementation needed for a useful mechanism comparison.
- [Exo](../../../../agentic-systems/reviews/exo.md) — rejected because its sandbox rewind, protected substrate, and self-modification boundary answer failure recovery and mutability questions rather than the source's policy-refusal and institutional-governance claim.

## Index Membership

None

## Synthesis Opportunities

- The source, [Claude Fable 5 Made Most of My Agent Scaffolding Obsolete](../../../../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md), and [Accumulated Behavioral Rules](../../../../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) jointly suggest a distinction not yet owned by one candidate: stronger models may remove scaffolding that compensates for weak task execution while increasing the value of institutional governance that coordinates many capable workers. “Model-management scaffolding” and “organization-management governance” should be tested as separate artifact classes before treating the two practitioner accounts as contradictory.

## Maintenance Observations

None

## Flags

- **Split candidate:** the source makes independent claims about model maturity, software-factory throughput, textual institutional governance, rule lifecycle, policy boundaries, and domain-specific non-transferability. It has nine high-signal candidates across constraining, deploy-time learning, maintenance, source comparison, agent-memory governance, and agentic control planes. The later ingest should preserve these as separately qualified claims rather than compressing them into one endorsement of “fences.”
- **Threat-model tension:** the source frames fences as an alternative to sandboxes for a cooperative superintelligence, while Swamp retains both policy gates and deployment isolation because credential reach, untrusted extension code, and worker capabilities remain structural risks. The ingest should state that the substitution claim is conditional on agent compliance and does not address capability containment.
- **Evidence boundary:** throughput, artifact counts, rule effects, model maturity, and organizational outcomes are first-person practitioner reports. The snapshot contains no implementation inspection, traces, or controlled comparison, so connections should carry them as reported cases rather than verified system behavior or forecasts.
