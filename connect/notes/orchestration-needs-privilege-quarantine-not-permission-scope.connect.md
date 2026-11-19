---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/orchestration-needs-privilege-quarantine-not-permission-scope.md"
source_has_frontmatter: true
date: "2026-07-07"
depth: standard
---

# Connection Report: Agent orchestration needs a privilege quarantine, not just a permission scope

**Source:** [Agent orchestration needs a privilege quarantine, not just a permission scope](../../../../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md)

Source claim: the defense against injected instructions in an orchestrated agent is a role-level privilege quarantine (a reader that never gets a high-privilege action, and an actor that only acts on the reader's vetted output), not finer per-call tool scoping. Tags: `computational-model`, `tool-loop`. Status: seedling.

Already authored (excluded from candidates below): `a-harness-for-every-task-dynamic-workflows` (sources, derived-from), `gbrain` (agentic-systems, evidence), `compiling-coordination-preserves-primitive-not-aggregate-authority` (notes, grounds), `the-four-field-record-exposes-...` (notes, extends), `agent-orchestration-needs-coordination-guarantees-not-just` (notes, see-also), `claude-code-dynamic-workflows` (agentic-systems, see-also).

## Discovery Trace

**Curated heads:**
- Read `computational-model-README.md` and `tool-loop-README.md` heads. Both are selective heads, neither declares `complete: true`, so by-tag `rg` sweeps were run (not skipped).

**Description listing scan:**
- `rg -l '^tags:.*\bcomputational-model\b' kb/notes/ | xargs rg '^description:'` — enumerated ~50 computational-model notes. Most are scheduler/context-engineering topics irrelevant to the security claim. Flagged: `llm-context-is-composed-without-scoping` (scoping must be imposed architecturally via sub-agents), `topology-isolation-and-verification-form-a-causal-chain`, `runtime-structure-determines-governance-control-surfaces`.
- `rg -l '^tags:.*\btool-loop\b'` — 14 notes; all already-linked orchestration siblings or scheduler topics, no new security-relevant candidate.

**Body search (across notes, reference, agentic-systems, agent-memory-systems, sources, instructions):**
- `rg -i "untrusted"` — hits: `agent-memory-needs-discoverable-composable-trusted-knowledge-under`, `gbrain` (linked), `the-four-field-record` (linked), `secure-llm-wiki`, `scaling-managed-agents-decoupling-brain-from-hands`, several ingests.
- `rg -i "prompt injection"` — hits: `llm-context-is-composed-without-scoping`, `llm-context-is-a-homoiconic-medium`, `secure-llm-wiki`, many agent-memory reviews, `scaling-managed-agents...`.
- `rg -i "confused deputy"` — only `adaptation-of-agentic-ai-survey...` (source, not a role-split match).
- `rg -i "privilege separation"` — zero hits (the note names the general security principle but no other artifact uses the phrase).
- `rg -i "trust boundary"` — `gbrain` (linked), `secure-llm-wiki`, plus dynamic-cheatsheet/atlas/synto memory reviews (memory-provenance, not orchestration role-split).
- `rg -i "quarantine"` — only agent-memory reviews; strongest is `secure-llm-wiki`.
- `rg -i "oracle" / "verif"` — `topology-isolation-and-verification...`, `reliability-dimensions-map-to-oracle-hardening-stages`, `an-outcome-check-licenses-replay...`, `verifiability-gradient`, `error-correction-works-above-chance-oracles...` (relevant only to the note's Scope-Limit residual-risk point).

**Link following:**
- From `topology-isolation-and-verification...` followed its body: it explicitly frames `isolation → verification` as a dependency and cites `llm-context-is-composed-without-scoping` for the isolation step and `agent-orchestration-needs-coordination-guarantees-not-just` (already linked from source) for contamination. The quarantine note's Scope-Limit is a security-domain instance of exactly its `isolation → verification` link.
- Read `secure-llm-wiki` fully: untrusted source → sanitizer → nonce-delimited extraction → trust-tier gate → independent adversarial review → write gate; untrusted claims are hard-excluded from the read-back context the downstream LLM answers from. This is the reader/actor privilege split in a memory-ingestion setting, plus an oracle (adversarial review) for the residual "well-formed but poisoned" case.
- Confirmed `scaling-managed-agents-decoupling-brain-from-hands` has an `.ingest.md` (its authored surface); the snapshot itself is immutable.

## Connections Found

Candidate outbound edges for a future edit of the source note:

- [llm context is a homoiconic medium](../../../notes/llm-context-is-a-homoiconic-medium.md) — **grounds**: the note's whole premise — that injected content can steer a privileged call — rests on there being no enforced program/data boundary. Homoiconicity ("data can contain instructions... the program/data boundary is conventional, not enforced") is the mechanism that makes injection possible, which is why the fix cannot be a per-call permission list. *Load-bearing label on a seedling target — flag for review.*
- [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md) — **grounds**: this note argues scope "can only be imposed architecturally," with sub-agents as the canonical move (code outside the LLM constructs a fresh context). Privilege quarantine is exactly that — imposing scope at the agent-role level via code rather than trying to scope inside a single flat call. It grounds why the boundary has to move off the per-call check. (Alternative label: `exemplifies`, treating quarantine as a security instance of the general architectural-scoping move.) *Load-bearing label on a seedling target — flag for review.*
- [Topology, isolation and verification form a causal chain for reliable multi-agent systems](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — **extends**: the source's Scope-Limit (quarantine gives isolation but the actor still needs an oracle to check the reader's extraction) is a security-domain case of this note's `isolation → verification` dependency — isolation alone does not imply safety. Additive/non-load-bearing, safe for a seedling.
- [Secure LLM-Wiki](../../../../agent-memory-systems/reviews/secure-llm-wiki.md) — **evidence**: a third, code-grounded instance of the read/act privilege split beyond the two the note names. Untrusted source text is barred from becoming trusted, agent-consumable memory: extraction/trust-tier/quarantine pipeline vets before promotion, and untrusted claims are hard-excluded from the read-back context the downstream LLM acts on. It also instantiates the Scope-Limit's residual-risk oracle (independent adversarial review over the extracted-but-not-yet-trusted claims). Directly strengthens the note's convergent-design argument and could retire the Open Question's "both instances are first-party accounts" caveat by half.

## Bidirectional Candidates

- [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md) <-> source — **exemplifies** (return path): that note's "architectural response / sub-agents" section could cite privilege quarantine as a concrete security instance of imposing scope via code-constructed contexts.
- [Topology, isolation and verification form a causal chain](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) <-> source — return path: that note's "KB evidence for the chain" list could add quarantine as a security-domain case where isolation manifestly does not imply safety without verification (bearing on the chain vs. the "simpler account").

## Reverse-edge Candidates

None beyond the return-path candidates above (both are notes→notes, captured under Bidirectional Candidates). No artifact in an excluded or narrow-outbound collection needs to author a link to this target under its own rules that isn't already covered.

## Off-authorisation Candidates

- [Scaling Managed Agents: Decoupling the brain from the hands](../../../sources/scaling-managed-agents-decoupling-brain-from-hands.md) — Managed Agents splits an agent into a reasoning "brain" and an executing "hands" for *interface stability*, not to quarantine untrusted content: the brain still reads the content and still steers the privileged hand actions, so the split does **not** achieve a privilege quarantine. The genuinely useful signal is this contrast — a superficially similar agent split that a reader might wrongly assume is quarantine. `contrasts` captures it, but `contrasts` is a notes-only label; for a `sources` target the only authorised labels are `evidence` / `derived-from` / `see-also`, none of which fit a "looks-alike-but-isn't" relationship. Suggestion: either author it as a plain `see-also` from the source note (accepting the loss of the contrast nuance) or, better, note the distinction inline in the source note's prose without a footer edge. A collection-contract fix would be allowing `contrasts` toward `sources` for exactly this "structurally similar external design, different driver" case. (Authored surface if a link is wanted: `scaling-managed-agents-decoupling-brain-from-hands.ingest.md`.)

## Raw Text Candidates

None. All candidates carry frontmatter.

## Rejected Candidates

- [agent memory needs discoverable composable trusted knowledge under bounded context](../../../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) — "untrusted"/"trusted" here is about memory-artifact quality under bounded context, not an orchestration role-split against injection. Keyword overlap only.
- [make authority explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md) — about who may read/write/promote memory across risk levels; adjacent vocabulary ("authority") but a memory-governance requirement, not the orchestration-injection claim.
- [reliability dimensions map to oracle hardening stages](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md), [verifiability gradient](../../../../notes/verifiability-gradient.md), [an outcome check licenses replay, a rule needs the process verified](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) — all bear on the Scope-Limit's "the actor needs an oracle" aside, but only tangentially; linking any of them would attach a general verification-theory note to a one-sentence residual-risk caveat, not to the note's main claim. `topology-isolation-and-verification...` already covers the isolation→verification point more directly.
- [runtime structure determines governance control surfaces](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) — about which governance operations a runtime's structure permits; related theme (structure enabling control) but not the injection/role-split argument.
- [interpretation errors are failures of the interpreter](../../../notes/interpretation-errors-are-failures-of-the-interpreter.md) — touches the confused-deputy framing obliquely but is about interpretation responsibility, not privilege separation.

## Index Membership

- [computational-model-README](../../../../tags/computational-model-README.md) and [tool-loop-README](../../../../tags/tool-loop-README.md) — the source already carries both tags; a future editor may add it to either selective head. Both are non-`complete` heads, so membership is recoverable by `rg` and adding it is optional curation, not required.

## Synthesis Opportunities

Three artifacts now describe the same read/act privilege split independently — the dynamic-workflows triage pattern (already linked), GBrain's operations layer (already linked), and Secure LLM-Wiki (candidate above). With Secure LLM-Wiki added, the source note itself becomes the synthesis; no separate synthesis note is warranted. Worth revisiting only if a fourth code-grounded instance appears and the residual-risk oracle question (Open Question 1) gets a concrete answer from any of them.

## Maintenance Observations

- The phrase "privilege separation" appears only in this note across the whole KB, despite it being a named, transferable security principle. If more security-flavoured notes accrue, a definition or tag-README head for the concept may become worthwhile. Not a connection candidate; recording as a durable coverage-gap signal.

## Flags

- Two proposed load-bearing `grounds` edges land on a `status: seedling` target — flagged per the connect-report standard; a future writer should confirm the premises hold before authoring them as `grounds` rather than a lighter label.
- No split candidate: the note makes one main assertion with a bounded scope-limit; it does not spread across three+ topic areas.
