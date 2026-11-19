---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/a-retained-design-theory-is-what-the-interpreter-cannot-regenerate.md"
source_has_frontmatter: true
date: "2026-08-25"
depth: standard
---

# Connections: Design rationale must preserve decision premises its interpreter cannot regenerate

**Source:** [Design rationale must preserve decision premises its interpreter cannot regenerate](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md)

## Discovery Trace

**Description listing scan:**
- Read the source collection's `COLLECTION.md`, including its outbound labels and destination rules. Prospecting was authorized over `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; `work` was excluded.
- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/document-system-README.md`, and `kb/notes/context-engineering-README.md`. Neither tag README declares `complete: true`, so their absence of this new untracked note was not treated as proof of non-membership.
- Read the destination heads `kb/types/README.md`, `kb/reference/README.md`, `kb/instructions/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
- Generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for every authorized local destination: 363 titles in notes, 10 in types, 150 in reference, 173 in agent-memory-systems, 12 in agentic-systems, 305 in sources, and 48 in instructions.
- Ran `rg '^description:' kb/notes --glob '*.md' | rg -i 'decision premise|regener|recomput|recover|ground truth|authorit|commitment|deriv|design rationale|intent'` and the same scoped description search over reference and the remaining authorized destinations. It surfaced the recovery/authority, commitment/derivation, checked-copy, intent-yield, system-definition, content-routing, and design-rationale clusters.
- Types had no candidate that added a needed definition to the source's claim; the target already uses the base `note` contract and defines its local terms in prose. Agent-memory and agentic-system results were implementation cases one hop beyond the closer theory notes, so direct prospecting there was stopped. The Naur ingest was the only exact source-side match and is already linked. No instruction added an execution path for this retention criterion beyond links already present.

**Topic indexes:**
- `document-system-README.md` surfaced the already-linked cache-economics note and the checked-derived-copy rule.
- `context-engineering-README.md` surfaced the already-linked cache-economics note and [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).
- `reference/README.md` surfaced [Content routing](../../../../reference/content-routing.md) and `design-rationale-management.md` as Commonplace's current application surfaces.

**Body search:**
- `rg -n -i 'decision premises|faithful recover|role-free|independent authority|exact-record|design rationale' kb/notes kb/reference kb/types kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` — confirmed that recovery/authority, checked-copy, and system-definition boundaries are now authored inline; rejected generic oracle and memory-policy matches.
- `rg -n 'a-retained-design-theory|residue an interpreter|cannot regenerate' kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` — found existing inbound links from the intent-yield note, the Naur ingest, content routing, and ADR 077. Their visible old-title wording and inherited equivalence are maintenance work, not missing reverse edges.
- `rg -N --no-heading -m1 '^# ' kb/notes --glob '*.md' | rg -i 'regener|recomput|recover|ground truth|authorit|commitment|deriv|design theory|design rationale|system-definition|intent'` — confirmed that the kept candidates were the closest claim-title matches rather than keyword-only body hits.

**Link following:**
- Followed the existing “Attempted recovery” edge to its recovery/provenance/authority split, then one hop to [Commitment, not derivation, creates new ground truth](../../../../notes/commitment-not-derivation-creates-new-ground-truth.md) and the LLM-recompute note. The commitment note was rejected as a direct addition because the existing recovery edge already reaches and summarizes that distinction.
- Followed the checked-copy candidate to its deterministic-verification and history-complement neighbors; the final source now authors it inline as the mechanical-cache regime.
- Followed the system-definition candidate to its authority-bearing-constraint exception; the final source now authors it inline as a limit on recovery-based deletion.
- Followed the intent-yield note and confirmed that the reciprocal source-to-extension edge is now authored in the footer, while the target note's H1 changed after the initial report.

## Connections Found

- [Content routing](../../../../reference/content-routing.md) — **evidenced-by**: shows the source criterion applied to Commonplace's shipped routing table, with consumer and force added after the regeneration-source test.

## Bidirectional Candidates

None. The strongest reciprocal targets already author inbound links to the source, though their old-title wording needs reframe propagation.

## Reverse-edge Candidates

None. The intent-yield note, Naur ingest, content-routing reference, and ADR 077 already link to the source under their own collection rules.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) — articulates the same reproduction-versus-authority boundary, but around model weights; the system-definition candidate states the source note's immediate exception more directly.
- [Commitment, not derivation, creates new ground truth](../../../../notes/commitment-not-derivation-creates-new-ground-truth.md) — strong underlying distinction, but already reached one hop through the source's authored recovery/authority edge; a new direct footer edge would worsen current connection inflation.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) — adjacent Commonplace lifecycle description, but content routing is the more direct implemented witness for the source's retention criterion.

## Index Membership

- [Document system](../../../../tags/document-system-README.md) — the source contributes the retention boundary for design rationale and carries the `document-system` tag.
- [Context engineering](../../../../tags/context-engineering-README.md) — the source classifies when retained explanation pays against read-time reconstruction and carries the `context-engineering` tag.

## Synthesis Opportunities

None. The candidate cluster already has distinct notes for recovery versus authority, commitment versus derivation, cache maintenance, and residue ranking.

## Maintenance Observations

- The final source has reconciled the earlier contradiction with [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md) by making it an inline limit on recovery-based cache classification.
- The source footer still displays “Intents are the highest-yield retained seed, and contingent fact is their limit,” but that target's current H1 is “A specific intent may out-yield local rationales, but contingent facts stay separate.” The edge remains substantively useful, but its visible link text and context phrase need review.
- Existing inbound citers—the intent-yield note, Naur ingest, content routing, and ADR 077—still display or rely on the pass-start equivalence. Reframe propagation must update visible text and reconcile claims, not merely repair paths.

## Flags

None.
