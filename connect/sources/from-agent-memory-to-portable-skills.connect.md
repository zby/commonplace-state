---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/from-agent-memory-to-portable-skills.md"
source_has_frontmatter: true
date: "2026-08-29"
depth: standard
---

# Connections for From Agent Memory to Portable Skills

## Discovery Trace

The target snapshot, `kb/sources/COLLECTION.md`, and the connect-report type were read in full before discovery. Discovery stayed within the source collection's authorized local destinations: notes, reference, agent-memory systems, agentic systems, and other sources. It did not search `kb/work/` or `kb/instructions/`, and it used no web, MCP, or other external lookup.

Curated heads read in full:

- `kb/notes/README.md`
- `kb/reference/README.md`
- `kb/agent-memory-systems/README.md`
- `kb/agentic-systems/README.md`
- `kb/sources/README.md`
- `kb/notes/agent-memory-README.md`
- `kb/notes/deploy-time-learning-README.md`
- `kb/notes/learning-theory-README.md`

Complete title-listing queries were executed for all five authorized destinations. They returned 386 note titles, 159 reference titles, 174 agent-memory-system titles, 12 agentic-system titles, and 338 source titles:

```text
rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'
rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'
rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'
rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'
rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'
```

Whole-description queries:

```text
rg '^description:' kb/notes/ --glob '*.md'
rg '^description:' kb/reference/ --glob '*.md'
rg '^description:' kb/agent-memory-systems/ --glob '*.md'
rg '^description:' kb/agentic-systems/ --glob '*.md'
rg '^description:' kb/sources/ --glob '*.md'
```

Focused note and tag queries:

```text
rg -n -i '^description:.*(skill|procedur|instruction|trace|trajectory|distill|memory|episode)' kb/notes/ --glob '*.md'
rg -n -i '^description:.*(ground|provenance|lineage|source|evidence|review|gate|warrant)' kb/notes/ --glob '*.md'
rg -n -i '^description:.*(addressab|locali[sz]ed|selective|repair|drift|schema|typed|ontology|graph)' kb/notes/ --glob '*.md'
rg -l -i '(distill(ed|ation)?|trace[- ](derived|extracted)|trajectory.*(skill|procedure)|skill.*(trajectory|trace)|procedur(al|e).*(memory|artifact))' kb/notes/ --glob '*.md'
rg -l -i '(node[- ]level|addressab(le|ility)|bounded repair|selective revision|one-step diff|patch version|supersed)' kb/notes/ --glob '*.md'
rg -l -i '(ontology|typed.*graph|schema[- ]validat|validity[- ]gat|grounding score|coverage.*gate|human review)' kb/notes/ --glob '*.md'
rg -l -i '(recall is not|recall.*capability|memory.*action|knowledge.*action|raw accumulation|activation)' kb/notes/ --glob '*.md'
rg -l '^tags:.*\bagent-memory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''
rg -l '^tags:.*\bdeploy-time-learning\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''
```

Focused agent-memory-system queries:

```text
rg -n -i '(Neo4j Agent Memory Service|\bNAMS\b|portable skills|Agent Instruction Protocol|AIP)' kb/agent-memory-systems/ --glob '*.md'
rg -n -i '^description:.*(skill|trace|trajectory|provenance|ground|graph|ontology|review|repair|drift)' kb/agent-memory-systems/ --glob '*.md'
rg -l -i '(distill(ed|ation)?|trajectory.*skill|trace.*skill|skill.*trace|procedure.*graph|workflow.*trace)' kb/agent-memory-systems/ --glob '*.md'
rg -l -i '(GROUNDED_IN|grounding|provenance|human review|review-gated|pending review|drift|repair)' kb/agent-memory-systems/ --glob '*.md'
rg -l -i '(Neo4j|knowledge graph|ontology|reasoning memory|tool call)' kb/agent-memory-systems/ --glob '*.md'
```

Focused source queries:

```text
rg -n -i '(Agent Instruction Protocol|AIP: A Graph Representation|2606\.04781|validity-gated action space)' kb/sources/ --glob '*.md'
rg -n -i '^description:.*(skill|distill|trajectory|trace|provenance|ground|procedure|workflow|memory)' kb/sources/ --glob '*.md'
rg -l -i '(trace.*skill|trajectory.*skill|skill.*trace|distill.*skill|skill.*distill|procedure graph|structured skill)' kb/sources/ --glob '*.md'
rg -l -i '(provenance|grounding|node[- ]level|drift|repair|human review|review-gat)' kb/sources/ --glob '*.md'
rg -l -i '(ontology|knowledge graph|reasoning memory|tool call)' kb/sources/ --glob '*.md'
```

Focused reference and agentic-system queries:

```text
rg -n -i '^description:.*(skill|instruction|review|ground|provenance|lineage|fresh|repair|source|validation)' kb/reference/ --glob '*.md'
rg -l -i '(SKILL\.md|skill package|instruction generation|generated skill|grounding|provenance|node[- ]level|drift repair|selective repair)' kb/reference/ --glob '*.md'
rg -l -i '(human review|pending review|validation gate|freshness baseline|source snapshot)' kb/reference/ --glob '*.md'
rg -n -i '(skill|memory|trace|distill|provenance|drift|repair|review|graph)' kb/agentic-systems/ --glob '*.md'
rg -n -i '^description:.*(memory|self-improv|skill|trace|version|rollback|govern)' kb/agentic-systems/ --glob '*.md'
```

No exact NAMS, article-title, AIP-title, or AIP-identifier match surfaced in the authorized agent-memory-system or source searches. The AIP paper below is an already-known external target because its URL and identifier are supplied by the snapshot itself; it was not browsed.

Candidate artifacts were opened and evaluated for claim-level fit, not accepted from lexical matches alone. One-hop local links were followed through the agent-memory and deploy-time-learning heads and through the candidate cluster around trace authority, retained episodes, derived-view alignment, localized repair, and effect-based evaluation. The accepted candidates share at least one operative axis with the source: trace-to-procedure conversion, evidence lineage, review-gated authority, drift detection, localized repair, or downstream validation. Broad graph, memory, skill, and self-improvement matches without the same operative axis were rejected.

## Connections Found

### Notes

- **is-evidence-for** → [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) — NAMS is a concrete vendor-described ingress pipeline: it turns accumulated messages, ontology facts, reasoning, tool calls, and outcomes into a scoped procedure with provenance, review state, and lifecycle handling rather than treating stored recall as capability.
- **is-evidence-for** → [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — The seven-stage distillation pipeline separates trace capture from consolidation, grounding and coverage checks, coherence and privacy checks, and human approval. That staged promotion directly supports the note's claim that authority must be earned after capture, although the article does not independently validate the adequacy of its gates.
- **is-evidence-for** → [Retaining the episode keeps a distilled rule re-derivable](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) — Each generated skill step remains linked to supporting memory nodes through `GROUNDED_IN`; drift repair re-resolves that retained evidence instead of editing a detached instruction. This is a direct implementation example of keeping a distilled rule connected to the episode from which it can be checked and re-derived.
- **is-evidence-for** → [Localized retention pays where change is sparse in a matching](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) — NAMS decomposes a skill into addressable step nodes with grounding and dependency edges, detects drift at the supporting tool-call node, and patches only the affected step when the rest of the matching survives. The claimed benefit depends on exactly the sparse-change and explicit-impact-closure conditions in the note.
- **is-evidence-for** → [Keep compiled views aligned](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) — A portable skill is a behavior-facing compiled view of the context graph. The stored source links, expected statuses, drift query, lock, re-grounding, superseding patch version, and full-redistillation fallback form a concrete source-alignment lifecycle.

### Agent-memory systems

- **compares-with** → [Agent Skills for Context Engineering](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) — Both systems include a trace-to-`SKILL.md` path. The reviewed repository presents that path mainly as an example workflow inside a broader skill corpus, while NAMS claims a service pipeline with deterministic graph construction, claim-level grounding, pending human review, and node-level drift repair.
- **compares-with** → [SkillWeaver](../../../../agent-memory-systems/reviews/SkillWeaver.md) — Both convert successful tool-use experience into a reusable executable procedure and validate the resulting artifact. SkillWeaver produces Playwright APIs with success, static, schema, version, test, and reference metadata; NAMS produces a portable skill graph with source-node provenance and selective re-grounding. The comparison isolates executable validation from retained evidence lineage.

### Other sources

- **compares-with** → [Memento-Skills let agents design agents](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) — Both treat standard skill packages as mutable behavior and localize a correction to a unit smaller than the whole agent. Memento attributes observed failure to a skill and uses generated tests to gate a rewrite or new skill; NAMS attributes source drift to a grounded step and uses provenance, structural gates, and human approval. Together they expose the difference between source-valid repair and behavior-valid repair.
- **compares-with** → [Reason wide, not deep: distilled skills](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) — Both distill trajectories into compact Markdown skills for later agents. Reason Wide contributes controlled evidence about held-out task performance and token cost but little per-rule lineage or maintenance; NAMS contributes provenance, review, versioning, and drift repair but reports its performance claims through a vendor account of the AIP paper.

### Reference and known external target

- **see-also** → [Commonplace agent-memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) — NAMS is a useful external analogue for several planned Commonplace capabilities: trace capture, promotion rather than raw retention, explicit source alignment for compiled views, human authority, and lifecycle repair. It is not evidence that Commonplace's specific plan works, so `see-also` is the authorized and semantically conservative label.
- **see-also** → [AIP: A Graph Representation for Agent Instructions](https://arxiv.org/abs/2606.04781) — The snapshot explicitly says NAMS implements this protocol and attributes the reported success-rate and latency results to it. The paper is the appropriate primary companion for the graph schema and benchmark claims; this report did not browse or independently assess it.

## Bidirectional Candidates

None. The target is an immutable snapshot and its matching authored ingest does not yet exist, so there is no verified authored source artifact on which to place a return edge.

## Reverse-edge Candidates

None for the same pre-ingest reason. After the ingest exists and its claims are grounded, the strongest notes to reconsider for an `evidenced-by` return edge are the retained-episode, localized-retention, and compiled-view-alignment notes listed above. No return edge should target the snapshot directly.

## Off-authorisation Candidates

None. `is-evidence-for`, `compares-with`, and `see-also` express the surviving relationships under the source collection's outbound vocabulary.

## Raw Text Candidates

None. The snapshot has structured frontmatter, and every local candidate retained in this report has a verified artifact path and frontmatter-backed identity.

## Rejected Candidates

- [Checked outcome licenses episode retention, not abstraction](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) — The article records tool-call status and validation gates, but it does not show that a checked outcome warrants the abstraction embodied by a skill. Treating it as supporting evidence would overread the vendor account.
- [Skills derive from methodology](../../../../notes/skills-derive-from-methodology.md) — The source is an example of generating a skill from traces rather than methodology, which fits a caveat in the note but not its central claim about methodology-derived skills.
- [Addressability grain sets a matched selective-read floor](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md) — Step nodes are addressable, but the article demonstrates selective repair rather than a selective-read cost floor. The localized-retention note is the claim-level match.
- [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) — It is another trace-to-procedure system, but its natural-language workflow files and weak provenance make it a broader, less discriminating comparison than the accepted Agent Skills and SkillWeaver reviews.
- [SkillRL](../../../../agent-memory-systems/reviews/SkillRL.md) — It learns skill-invocation policy through reinforcement learning; NAMS derives and maintains the skill artifact itself. The shared word “skill” hides a different learning target.
- [How Warp builds self-improving agents on Claude](../../../../sources/how-warp-builds-self-improving-agents-on-claude.ingest.md) — Mandatory review and skill-file updates are relevant, but the source does not expose NAMS's claim-to-node lineage or selective re-grounding. Memento is the sharper maintenance comparison.
- [Instruction generation](../../../../reference/instruction-generation.md) — Commonplace's instruction generation is deterministic build-time projection of governed source files, not experience distillation or a learned procedure lifecycle.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) — It records implementation coverage rather than a substantive mechanism. The gap plan is the better reader-facing reference connection.

Agentic-system searches produced only broad memory, graph, and self-improvement matches. None shared enough of NAMS's memory-subsystem boundary and trace-to-portable-skill lifecycle to survive claim-level review.

## Index Membership

- [Lightweight agent-memory systems](../../../../agent-memory-systems/lightweight/README.md) — NAMS merits a lightweight, document-grounded system entry if the KB wants a dedicated review. The available evidence is a product article and referenced paper rather than an inspected implementation repository.
- [Trace learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — A future refresh should consider NAMS as a distinct case: a service-owned context graph is distilled into a portable, provenance-linked skill graph and then maintained through source-drift repair.

## Synthesis Opportunities

- **Separate provenance, currency, and behavioral-effect gates.** NAMS supplies provenance and source-currency mechanisms; [Memento-Skills](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) supplies failure attribution and generated behavioral tests; [Reason Wide](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) supplies held-out outcome evidence. Read together with [Evaluate memory by effects](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md), they suggest that a repaired step can be well-grounded and current without yet being shown to improve behavior. This is a useful cross-system synthesis, but the existing effect-evaluation and localized-retention notes may already be sufficient homes for it.

## Maintenance Observations

- No exact NAMS or AIP artifact surfaced in the authorized agent-memory-system and source searches. If a dedicated lightweight review is added, the trace-learning survey and its index should be refreshed together rather than creating an unindexed review.
- The ingest should keep two evidence layers separate: the Neo4j article supports what Neo4j says NAMS does, while the AIP paper is the primary target for the typed graph protocol and reported benchmark results. The article alone does not independently establish those results.
- The snapshot describes a patch version that supersedes its predecessor and a full-redistillation fallback, but it does not establish retirement, replay, or downstream outcome-revalidation behavior. Preserve those as explicit limits rather than filling them from analogous systems.

## Flags

- **Vendor evidence:** this is a product/tool announcement, not a code-grounded review. Treat system mechanics and performance numbers as attributed claims.
- **One pipeline, two claim classes:** the source is coherent enough for one ingest, but operational-design claims about NAMS should be separated from evaluation claims inherited from AIP.
- **Discovery-output limit:** the complete high-volume title and description sweeps were executed, but some command output was truncated at the tool boundary. All accepted and rejected candidates in this report were individually opened and evaluated; the limitation affects exhaustive recall, not verification of the emitted candidates.
