---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/meta-v-jepa-2-publication.md
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: V-JEPA 2 publication abstract

**Source:** [V-JEPA 2 publication abstract](../../../../sources/.snapshots/meta-v-jepa-2-publication.md)

## Discovery Trace

**Description listing scan:**
- Generated the complete notes title surface and filtered `rg '^description:' kb/notes/ --glob '*.md'` for `world model|action-conditioned|prediction|causal|reach assessment|physical`. The action-conditioned world-model note was the only direct note target.
- Reference, agent-memory-system, and agentic-system destinations lacked a plausible trigger and were skipped after the cross-collection body search.

**Topic indexes:**
- Read `kb/notes/README.md` and `kb/sources/README.md`; no separate publication index is maintained.

**Body search:**
- `rg -n -i 'V-JEPA|action-conditioned|world model|latent predictor|physical reasoning' kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md'` found the existing combined review and the note that uses its robot-planning claim.

**Link following:**
- Followed the action-conditioned note to reach-assessment and its formal symbolic counterpoint. The blog snapshot is the fuller same-release companion.

## Connections Found

- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) — **is-evidence-for**: the abstract reports action-conditioned post-training, zero-shot deployment in two labs, image-goal planning, and the limits of the robot-data regime.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) → future ingest — **evidenced-by**: use this record for the paper-page deployment summary while the blog ingest carries the fuller mechanism.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — useful as background but the abstract does not identify formal causal variables or proof obligations.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- The capture is limited to the publication-page abstract; any paper-detail claim requires a separate full-paper observation.

## Flags

None
