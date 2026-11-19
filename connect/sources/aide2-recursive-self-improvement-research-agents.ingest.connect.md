---
description: "Post-ingest discovery for the existing AIDE2 paper analysis and the Weco source set"
type: types/connect-report.md
source: kb/sources/aide2-recursive-self-improvement-research-agents.ingest.md
source_has_frontmatter: true
date: "2026-09-27"
depth: standard
---

# Connection Report: AIDE2 paper ingest

**Source:** [AIDE2 ingest](../../../../sources/aide2-recursive-self-improvement-research-agents.ingest.md)

## Discovery Trace

- Read the existing ingest fully; verified its paired v1 snapshot hash and validation without changing it. Read sources/COLLECTION.md and the connect-report type.
- Shared discovery for this source batch read the curated README of notes, reference, agent-memory-systems, agentic-systems, tags and sources and generated their title surface with `rg -N --no-heading -m1 '^# '`. Description search: `rg -n '^description:.*(theory|critic|compounding|oracle|conjectur|AIDE|research|hypothes|eval)'` over those collections except tags. Focused search: `rg -n 'AIDE|Weco|solution tree|content-directed|fixed.search'`.
- Read the direct AIDE2 system review and followed the compounding, experimental-contrast and theory-builder distinctions. The newly accepted AIDE paper ingest supplies the prior architecture. Re-ran `rg -n '^description:.*(AIDE|Weco)|AIDE|ignition'` on both ingests, the AIDE2 review, the user-named article and the later-improvement test note.
- Reference and historical memory-system candidates did not supply a more direct connection than those below. Tag heads route to theory-builder and self-improving-systems notes; sources has no authorized outbound tag edge. No external prospecting; the canonical paper is already supplied. Instructions and work are excluded.
- Read articles/COLLECTION.md and the user-named article for the inbound evidence candidate; the article's five-unquoted-source bound must be respected by a later editor.

## Connections Found

- [AIDE paper ingest](../../../../sources/aide-ai-driven-exploration-space-of-code.ingest.md) — **compares-with**: distinguishes the original fixed controller searching task code from an outer process searching agent harnesses.
- [Compounding test](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — **compares-with**: compares demonstrated task transfer with an inconclusive test of the evolved agent as the next improver.
- [Experimental contrast](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **compares-with**: the winning harness's inactive ranking penalty demonstrates why bundle outcomes cannot establish each component's effect.
- [AIDE2 review](../../../../agentic-systems/reviews-archive/aide2.md) — **see-also**: supplies the retained whole-system analysis of the same documentary source boundary.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Which Existing Self-Improving Systems Are Theory Builders](../../../../articles/which-existing-self-improving-systems-are-theory-builders.md) → ingest — **evidenced-by**: supports a prospective Weco/AIDE2 case separating code revision, selected diagnostic traces and the unsettled scope of criticism. The new source set should inform a fresh editorial judgment.
- [Compounding test](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) → ingest — **evidenced-by**: bounds the inference from transferable task gains with the failed-to-resolve ignition comparison. This is a case-specific qualification, not corroboration of a universal claim.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

Generic repository memory stores: sharing external retained state supplies no sufficiently specific comparison beyond the selected architecture and causal questions.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

The newly captured Weco blog and this paper ingest preserve different numerical observations. The later editor should attribute each figure to its source rather than merging them.

## Flags

The existing ingest is reused unchanged. Connection candidates are not authored inbound links or an editorial classification decision.
