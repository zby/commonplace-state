---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/programming-as-theory-building.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: Programming as Theory Building

**Source:** [Programming as Theory Building](../../../../sources/.snapshots/programming-as-theory-building.md)

## Discovery Trace

**Collection contract and authored surface:**

- Read `kb/sources/COLLECTION.md`. The snapshot is immutable; the matching ingest report is its authored outbound surface. Authorised local prospecting destinations are notes, reference, agent-memory systems, agentic systems, and sources. Links into work and instructions are excluded.
- Read `kb/cache/types/connect-report.md`, the complete snapshot, and the curated heads `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The snapshot has no tags, so no tag-README or by-tag `rg` pass applied.
- External prospecting was skipped as required. The primary PDF URL is already known from snapshot provenance and is not an additional connection candidate.

**Full title listings:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` separately for notes, reference, agent-memory-systems, agentic-systems, and sources.
- The note titles surfaced the design-rationale, recovery, specification, maintainability, and ephemerality clusters. Reference titles surfaced Commonplace's design-rationale description. The two system collections surfaced retained-project-knowledge implementations but no artifact whose claim directly tests Naur's account.

**Description listing scans:**

- `rg -n -i '^description:.*(theor|methodolog|understand|rationale|knowledge|documentation|maintain|modif|similarity|simplicity|programming)' kb/notes --glob '*.md'` — kept the recovery, rationale-transfer, specification-strategy, maintainability-oracle, and ephemerality candidates; rejected generic learning-theory matches.
- The same scoped expression over `kb/reference` — evaluated `design-rationale-management.md`; rejected it as a system-specific implementation companion weaker than the theory-note targets.
- `rg -n -i '^description:.*(theor|understand|rationale|knowledge|documentation|maintain|tacit|programming)' kb/agent-memory-systems --glob '*.md'` and the analogous scan over `kb/agentic-systems` — evaluated Thalo and Compound Engineering; rejected both as generic retained-knowledge implementations without a Naur-specific comparison.
- `rg -n -i '^description:.*(Naur|theor|software|simplicity|programming|documentation|knowledge|maintain)' kb/sources --glob '*.md'` — kept `why-llms-cant-make-your-code-simpler.ingest.md`, which explicitly adapts Naur; rejected broader software-factory and spec-driven sources as one comparison hop too far.

**Body searches:**

- `rg -n -i 'Peter Naur|Programming as Theory Building|Theory Building View' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` — the only direct local discussion was the Answer.AI ingest.
- `rg -n -i 'design (theory|intent|rationale)|program (modification|maintenance)|maintainability|tacit knowledge|situated understanding' kb/notes --glob '*.md'` — kept the rationale-transfer and maintainability candidates.
- `rg -n -i 'documentation.*(insufficient|cannot|secondary)|code.*(why|rationale)|product.*(reason|rationale)|state.*(why|intent)' kb/notes --glob '*.md'` — kept the recovery and decision-surface candidates.
- `rg -n -i 'theory.*method|method.*theory|rules.*method' kb/notes --glob '*.md'` — evaluated but rejected the two-layer theory/methodology note because its explicit, addressable generator theory is not Naur's Ryle-style theory.
- `rg -n -i 'design rationale|decision context|tacit|programming theory|theory building|maintenance' kb/reference --glob '*.md'`, with analogous searches over agent-memory-systems and agentic-systems — found no stronger target than the note and source candidates retained below.
- `rg -n -i 'maintainability|design rationale|situated understanding|specification|ephemeral software|software factor' kb/sources --glob '*.md'` — confirmed the direct Answer.AI comparison and evaluated the neighboring factory/specification ingests.

**Link following:**

- Followed [Use tests a decomposition locally](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) to the recovery note, selective-revision note, and Commonplace design-rationale description. Kept the first two rationale/recovery surfaces only where Naur's compiler handoff supplies a specific articulation; rejected the system description as too implementation-specific.
- Followed [Bottom-up structure inference needs capture at the decision surface](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) to `Create Memory Directly` and `History has one chance to become checkable`. Kept the decision-surface claim; rejected the neighbors because Naur demonstrates interpersonal theory transfer as well as documentary loss and therefore does not establish their stronger recording claims.
- Followed [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) to changing-requirements and spec-mining notes. Kept the strategy note as a named comparison; rejected the neighbors because Naur does not separate requirement change from disambiguation or test a mining path.
- Followed [Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) to the maintainability-oracle note, weak-discrimination note, and ADR contract. Kept the direct source comparison and the maintainability target; rejected the statistical underselection note because Naur supplies no proposal-selection evidence.

## Connections Found

- [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md) — **is-evidence-for**: Naur's compiler handoff and fault-diagnosis cases show program text plus extensive documentation failing to reproduce the design knowledge used by long-involved programmers; the note usefully narrows that observation to an information gap rather than treating it as proof of provenance, authority, or universal inexpressibility.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — **is-evidence-for**: group B could run and extend the compiler yet missed the structural reasons group A immediately recognized, a concrete case where a working decomposition exposes boundaries without exposing the forces that made one extension natural and another a patch.
- [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) — **is-evidence-for**: the later compiler's still-visible structure did not preserve the design insight needed for coherent modification, supporting the note's state-versus-why distinction while not testing its proposed decision-receipt format.
- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) — **is-evidence-for**: Naur makes modification quality depend on recognizing similarities between new demands, world affairs, and existing facilities, supporting the note's relational, future-change-relative target and its warning that fixed structural rules are at best partial evidence.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) — **compares-with**: both accounts locate crucial understanding in an evolving development process; Naur treats specifications as secondary and rejects a universally right method, while the note assigns different durable specification strategies to phases in which understanding becomes available.
- [Ephemerality is safe where embedded operational knowledge has low explanatory-reach](../../../../notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md) — **compares-with**: both analyze when software remains viable across future changes, but Naur locates the essential theory in a continuing programmer group while the note emphasizes durable artifacts carrying cross-context operational knowledge.
- [Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) — **compares-with**: the later article explicitly adapts Naur to LLM-generated code and project-specific simplicity; the primary essay supplies the original theory, method critique, and program-life claims against which that secondary application can be bounded.

## Bidirectional Candidates

- [Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) ↔ source — **compares-with**: readers of either ingest benefit from moving between Naur's original account and the modern Answer.AI application, especially because the latter already labels its Naur exposition secondary and disputes an absolute reading about documentary capture.

## Reverse-edge Candidates

- [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md) → source — **evidenced-by**: the compiler and fault-diagnosis cases are classic bounded observations of failed recovery from program text and documentation, while the note supplies the inference limits.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) → source — **evidenced-by**: Naur's group-A/group-B episode gives the note a software case in which the artifact's visible structure underdetermines the reasons needed to transfer it.
- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) → source — **evidenced-by**: Naur supplies the classic conceptual basis for treating maintainability as judgment about future modifications and world-facing similarity rather than a context-free code metric.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) — rejected despite the lexical match: its theory is an explicit, addressable generator layer, while Naur's theory is a programmer's situated capacity to explain, justify, recognize similarity, and act; linking without this boundary would create a vocabulary collision.
- [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) — rejected: Naur shows theory passing through close work between programmers, so the essay does not establish that production-time records or deterministic re-derivability are the only transfer routes.
- [Create Memory Directly](../../../../notes/agent-memory-requirements/create-memory-directly.md) — rejected: the essay motivates preserving live understanding but expressly denies that documentation can exhaust the theory, so it does not establish that direct artifact creation preserves enough.
- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) — rejected: Naur assumes external change and analyzes modification, but does not distinguish genuine world change from late-discovered ambiguity.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) — rejected as a direct edge: it is a useful system-specific response to the problem, but the theory-note connections give a source-ingest reader the more discriminating route.
- [Thalo](../../../../agent-memory-systems/reviews/thalo.md) and [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) — rejected: both retain inspectable project knowledge, but neither reviewed artifact makes a claim about Naur-style program theory or tests transfer of the relevant situated understanding.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) — rejected: Naur's essay helps specify maintainability but supplies no candidate distribution, operative acceptance oracle, or enrichment evidence for the statistical selection conjecture.

## Index Membership

None

## Synthesis Opportunities

- Naur's in-principle limit on documentary expression, the recovery note's narrower information-gap account, and the rationale-transfer notes together suggest a layered claim: explicit rationale can make premises and alternatives addressable without exhausting the situated similarity judgments needed for future modification. Artifact retention and apprenticeship would then be complementary transfer channels rather than competing complete solutions.

## Maintenance Observations

- The corpus uses `theory` for at least two materially different objects: Naur's Ryle-style possession of explanatory and practical capacity, and explicit retained general theories that can serve as addressable generator layers. Any future synthesis should name this boundary rather than composing the two senses silently.

## Flags

- Split candidate: the essay makes independent claims about design-knowledge transfer, modification cost, program life/death, method, professional status, and education, and it connects across recovery/rationale, specification, maintainability, and artifact-persistence areas. A single ingest can analyze it, but promotion should select one contribution at a time.
- Tension: Naur says the relevant theory cannot in principle be fully expressed, while several KB notes rely on retained rationales or artifacts to support later transfer and revision. The primary source can bound those notes without implying that partial, checkable externalization is useless.
