---
description: "Post-ingest connection assessment for Fodor and Pylyshyn, prioritizing primary-source comparison and bounded inbound citations"
type: types/connect-report.md
source: "kb/sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md"
source_has_frontmatter: true
date: "2026-09-27"
depth: standard
---

# Connection Report: Fodor–Pylyshyn accepted ingest

**Source:** [Connectionism and Cognitive Architecture: A Critical Analysis](../../../../sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md).

This is a separate post-ingest assessment of the accepted ingest, read in full. It reuses the earlier source-reading and destination-discovery context but judges the ingest's actual scope: a theoretical argument about systematicity, a bounded comparison with learned approximation, distinctions among architecture levels, and a limited hypothesis-construction proposal. All recommendations are candidates; this operation changes no library artifact. Judgments were produced by the connect worker under `cp-skill-connect/SKILL.md` and `types/connect-report.md`.

## Discovery Trace

**Contracts and inputs.** Reused the already-read sources and reports collection contracts, connect-report type, notes contract and note type. Read the ingest type and the complete accepted ingest. Sources permits prospecting notes, reference, agent-memory-systems, agentic-systems, tags, and other sources; instructions and work remain excluded. External targets are considered only when already supplied. The ingest has domains but no tags, so no by-tag search is implied.

**Reused breadth pass.** The immediately preceding source pass read each permitted destination's `README.md`, generated its title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, and used smaller listings when output truncated. The computational-model, artifact-analysis, theory-builder, and learning-theory heads were read. The latter three declare `complete: true`; by-tag sweeps were skipped. That context remains useful for this same-source post-ingest pass.

**Current searches.** Ran `rg -n 'fodor-pylyshyn-1988-connectionism-cognitive-architecture|Fodor|Pylyshyn|systematicity' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/tags/ kb/sources/ --glob '*.md'`. Apart from the accepted ingest, the direct matches remain the learned-approximation note and Lampinen ingest. Neither currently links the accepted ingest. Ran `rg '^description:.*(systematic|compositional|representation|symbolic)' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/tags/ kb/sources/ --glob '*.md'` to screen adjacent mechanisms.

**Per-destination assessment.**

- **Notes:** Reassessed the fully read learned-approximation note, representational-form definition, action-model consumption note, and theory-builder definition against what the accepted ingest actually says. These pass at their stated conceptual or comparative strength. Read the fixed-decomposition note because the accepted ingest adds that connection; its effective-update-space qualification fits the ingest's explicit rejection of a generic computational impossibility claim. Retained-theory intervention and code execution remain less direct routes.
- **Sources:** Reused the full Lampinen and Craik ingest readings. Lampinen is the direct comparison: it represents the same dispute through a later connectionist argument. Craik remains a possible historical comparison but the accepted ingest's narrower contribution does not need another source link. Modern generalization and reasoning papers found through description/title scans do not independently resolve this architectural dispute.
- **Reference:** The prior source-adoption-policy hit concerns limiting programming analogies to Commonplace's symbolic shell. The accepted ingest already makes the relevant vocabulary distinction through representational form; adding a shipped-policy link would duplicate that route. No reference candidate retained.
- **Agent-memory-systems:** Prior descriptions for Cortex, Clude, AgentFly, and trace-learning comparisons concern implementation mechanisms, not a test of the paper's architecture claim. The accepted ingest adds no system-specific bridge. No candidate retained.
- **Agentic-systems:** Prior candidates such as ModularRSI and oh-my-pi concern runtime composition and memory mechanisms. The accepted ingest does not characterize or test them. No candidate retained.
- **Tags:** The heads remain discovery routes. The source contract provides no formal source-to-tag label, and the ingest does not warrant a selective tag-head pick merely through historical overlap. No membership or off-authorisation candidate retained.
- **External:** The original PDF is already the ingest's provenance target. No external search or new external target was needed.

**Link following.** Followed the accepted ingest's actual links into the learned-approximation/Lampinen pair, representational form, action-model consumption, theory builder, and fixed decomposition. The last note distinguishes an absent primitive from an absent effective capability; that distinction is important because the paper permits neural implementation of classical operations. Reverse-edge labels below were checked against the notes and sources collection contracts.

## Connections Found

These candidates reaffirm the accepted ingest's existing useful routes; they do not call for duplicate links.

- [Lampinen ingest](../../../../sources/symbols-neural-networks-mathematical-intelligence.ingest.md) — **compares-with**: compare its learned, fallible symbolic-competence account with the primary paper's systematicity argument, preserving the distinctions between performance and competence and between implementation and architecture.
- [Natural-language meaning is coordination among learned approximations](../../../../notes/natural-language-meaning-is-coordination-among-learned-approximations.md) — **compares-with**: the ingest specifies what this conjecture's approximate compositionality must explain: linked capacities and sufficiently stable constituent contributions. It expressly leaves open whether learned coordination can supply the mechanism.
- [Representational form](../../../../notes/definitions/representational-form.md) — **compares-with**: distinguish the paper's structured cognitive representations from Commonplace's classification of retained artifacts by localization and assigned consequences. Neither vocabulary should silently stand in for the other.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) — **is-evidence-for**: the ingest's label-versus-operative-structure example clarifies the requirement that a representation actually influence processing. This is conceptual evidence, not a test of the note's present-day agent-system claims.
- [Theory builder](../../../../notes/definitions/theory-builder.md) — **compares-with**: the ingest separates the paper's proposed hypothesis evaluation from a demonstrated process satisfying localized content, consumption, criticism, and iteration. The comparison prevents a historical resemblance from being treated as evidence of improved capacity.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: compare architectural commitments with an effective update space, while preserving the note's distinction between unexpressible corrections and capacities constructible through permitted operations. The paper's neural-implementation concession makes that qualification essential.

## Bidirectional Candidates

- [Lampinen ingest](../../../../sources/symbols-neural-networks-mathematical-intelligence.ingest.md) → [Fodor–Pylyshyn ingest](../../../../sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md) — **compares-with**: a reverse connection gives readers of Lampinen's historical account the primary rival's actual commitments. Add context distinguishing explicit rules, structured representations, fallible performance, and neural implementation; do not rewrite Lampinen's retained quotations.

## Reverse-edge Candidates

- [Natural-language meaning note](../../../../notes/natural-language-meaning-is-coordination-among-learned-approximations.md) → [Fodor–Pylyshyn ingest](../../../../sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md) — **evidenced-by**: use the primary source to qualify the historical characterization in “Meaning sits on the pattern side.” This supports an accurate statement of the rival, not corroboration of the note's untested learned-coordination hypothesis. Preserve the hypothesis's tentative status.
- [Action-model consumption note](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) → [Fodor–Pylyshyn ingest](../../../../sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md) — **evidenced-by**: a bounded conceptual example can distinguish an analyst's structured labels from structures consumed by the modeled system. Its reader gains a precise failure case for inferring mediation from documentation alone. Any added wording must identify this as conceptual clarification, not empirical corroboration or evidence of learning.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Craik ingest](../../../../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md) — structure-preserving internal models remain a legitimate historical comparison, but the accepted ingest's direct task is better served by Lampinen and the existing consumption-path note. No extra outgoing link recommended.
- [Code complements the weight–prompt pair](../../../../notes/code-complements-weight-prompt-with-symbolic-operations.md) — the accepted ingest does not establish modern runtime behavior; representational form already supplies the required vocabulary boundary.
- [Theory-building precedents](../../../../notes/theory-building-has-distinct-precedents.md) — the ingest itself finds the concluding learning proposal operationally unspecified. It should not become a claimed full theory-builder precedent through a new link.

## Index Membership

None.

## Synthesis Opportunities

None. Clarifying the existing rival characterization is the supported next step; no new synthesis is needed.

## Maintenance Observations

None.

## Flags

- The ingest currently retains no source quotes. A later source-dependent note citation needs retained supporting quotes through the grounding workflow or the explicit `(snapshot required)` marker. The connect report is not source support and does not authorize a library edit.
- The ingest limits its claim to the reconstructed 1988 architectures and treats hypothesis construction as a proposal. Do not use any candidate link to assert a present-day neural impossibility result or the superiority of Commonplace's theory-building process.
- The ingest reports absent diagrams and damaged extraction text. Prose-level comparisons above do not establish diagram topology or exact damaged wording.
- Five notes pass the articulation test, but the links address one coherent architectural dispute and its learning consequence; they do not span three independent topic areas. No split candidate is warranted.
