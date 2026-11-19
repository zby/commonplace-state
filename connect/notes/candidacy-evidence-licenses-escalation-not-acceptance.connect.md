---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/candidacy-evidence-licenses-escalation-not-acceptance.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Candidacy evidence licenses escalation to assessment, not acceptance

**Source:** [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md)

## Discovery Trace

**Source collection contract and report contract:**
- Read [connect-report](../../../../types/connect-report.md) and [kb/notes/COLLECTION.md](../../../../notes/COLLECTION.md). Extracted outbound rules: `notes` is the primary destination; `instructions` is rare but explicitly allows `operationalized-from`; `reference`, `types`, `sources`, `agent-memory-systems`, `agentic-systems`, and `external` are conditional; `kb/work/` is excluded.

**Topic indexes:**
- Read [Notes](../../../../notes/README.md), [Foundations](../../../../tags/foundations-README.md), and [discovery](../../../../tags/discovery-README.md).
- `discovery-README.md` declares `complete: true`, so I skipped a by-tag `rg` pass for `discovery`.
- Read [Reference](../../../../reference/README.md), [Instructions](../../../../instructions/README.md), [Types](../../../../types/README.md), [Sources](../../../../sources/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), and [Agentic Systems](../../../../agentic-systems/README.md) to check whether other destinations had source-aligned triggers.

**Description listing scan:**
- `rg '^description:' kb/notes/ --glob '*.md' | rg 'verdict|warrant|acceptance|assessment|oracle|candidate|search|evaluation|escalation'`
  - Kept [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md): same acceptance-authority boundary, but stated at loop/oracle level.
  - Kept [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): gives the broader search-versus-evaluation split the source relies on.
  - Rejected [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md): same "green check is not warrant" shape, but at the target/objective proxy layer rather than inside one assessment.
  - Rejected [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md): useful authority-transfer analogy, but it governs episode-to-rule abstraction rather than candidacy-versus-verdict evidence.

**Title scan and exact-mention pass:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' | rg 'claim modality|proposal-selection|warranted autonomy|proximate target|checked outcome|consumption channel|acceptance gate'`
  - Followed [Claim modality is the inference form of the refuter](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md), [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), and [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md).
- `rg -n 'candidacy|verdict evidence|acceptance bar|pursuit-worthiness|nominate|source suggestions may|routing evidence|oracle domain|search.*evaluation|achievement check' kb/notes/ kb/instructions/ kb/reference/ kb/types/ kb/sources/ --glob '*.md'`
  - Confirmed a direct operationalization in [Assess a claim-bearing artifact against external literature](../../../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md), especially its rule that source suggestions or topical resemblance may nominate reading but cannot supply verdict evidence.
  - Confirmed the shipped design companion in [081-Literature disposition is explicit and claim-grained](../../../../reference/adr/081-literature-disposition-is-explicit-and-claim-grained.md), but judged the instruction the stronger traversal target because it carries the operative procedure.
  - Checked [Review gate](../../../../types/review-gate.md) and rejected it: `FAIL` as escalation signal is the same family, but the type contract governs assay force rather than the source note's evidence-stage distinction.
  - No `sources`, `agent-memory-systems`, or `agentic-systems` candidate survived articulation: the hits were either already mediated through better local notes/instructions or too far from claim-assessment staging to beat the notes-level routes.

**Link following:**
- Followed the source's existing links into [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md), [Domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md), and [An independent pass tightened three of four Pirolli grounding verdicts](../../../../notes/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md).
- Their neighborhoods reinforced three missing routes: the refuter-defined modality note that already points back here, the proposal-selection loop note that separates search from reject-capable evaluation, and the literature-assessment instruction that already treats nomination as non-verdict evidence.

## Connections Found

- [Claim modality is the inference form of the refuter](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) -- **extends**: it places this note's Peircean routing stage inside the broader account where abduction belongs to discovery while verdict authority belongs to the criticism phase and its refuter form.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **mechanism**: it supplies the broader loop decomposition behind the source's claim, where nomination/search and accept-or-reject evaluation are distinct functions with distinct failure modes.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **extends**: it develops the operational consequence of the source's authority boundary, turning "candidacy evidence is not verdict evidence" into a limit on which unattended acceptances an oracle can warrant.
- [Assess a claim-bearing artifact against external literature](../../../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md) -- **operationalized-from**: it converts the note's core boundary into procedure by allowing source suggestions to nominate reading assignments while forbidding them to decide overlap or disposition.

## Bidirectional Candidates

- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) <-> source -- **extends**: the reverse path is independently useful because the autonomy note states the oracle-domain limit abstractly, while this note gives a concrete worked case where nomination-grade evidence outruns warranted acceptance.

## Reverse-edge Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → source -- **extends**: the loop note states that evaluation is scoped to what the check establishes; this source adds a sharper within-evaluation distinction between evidence that brings a candidate into consideration and evidence that can actually accept it.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) -- same broad anti-transfer pattern, but the target/objective proxy layer is one level removed from this source note's staged-assessment boundary; better synthesis material than a direct traversal aid.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -- similar authority non-transfer, but it governs episode-to-rule abstraction rather than candidacy-versus-verdict evidence inside one assessment.
- [Review gate](../../../../types/review-gate.md) -- the "FAIL is an escalation signal" force boundary is an operational analogue, not a close enough match to the note's evidence-license claim to beat the instruction route.

## Index Membership

- [Foundations](../../../../tags/foundations-README.md) -- the note is tagged `foundations` and contributes a core epistemic boundary on how support can move between routing and acceptance in staged evaluation; it fits the head's methodology remit and is not currently listed there.

## Synthesis Opportunities

- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md), [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md), and [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) suggest a broader synthesis: evidence or checks that authorize a weaker upstream action do not automatically transfer warrant to a stronger downstream claim.

## Maintenance Observations

None

## Flags

None
