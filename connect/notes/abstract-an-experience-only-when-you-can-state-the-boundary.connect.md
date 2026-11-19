---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md"
source_has_frontmatter: true
date: "2026-06-30"
depth: standard
---

# Connection Report: Abstract an experience into a lesson only when you can state where the lesson stops

**Source:** [Abstract an experience into a lesson only when you can state where the lesson stops](../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md)

The source already authors six footer links (first-principles reach, distillation-as-transformation, learning-is-not-only-about-generality, memory-management-policy, constraining-and-distillation, trace-derived-learning-techniques). This run hunts for *new* candidates and excludes those six.

## Discovery Trace

**Topic indexes:**
- Read `kb/notes/learning-theory-README.md` head — `covered_by: [deploy-time-learning, constraining, distillation, discovery, artifact-analysis, agent-memory, llm-interpretation-errors]`, no `complete` mark, so the by-tag `rg` for learning-theory was still run.
- Read `kb/notes/deploy-time-learning-README.md` head — no `complete`/`covered_by` mark, by-tag `rg` run.
- Confirmed source is NOT yet listed in either tag README (`rg -l 'abstract-an-experience...' kb/notes/*-README.md` → empty) → index-membership candidate below.

**Description listing scan (source's two tags):**
- `rg -l '^tags:.*\blearning-theory\b' kb/notes/ | xargs rg '^description:'` — ~90 hits. Flagged: `an-accepted-edit-verifies-the-change-not-the-rule` (confirmation verifies instance not rule — same asymmetry as source's success/existence-proof), `choosing-what-to-learn-requires-both-validity-and-learning-value-gates` (promotion gates), `diagnostic-richness-constrains-outer-loop-learning-quality` (inspectable failure evidence), `trace-derived-memory-earns-authority-per-operation-not-at-capture` (distil/verify operations), `raw-accumulation-does-not-create-usable-memory` (preserve-vs-dump).
- `rg -l '^tags:.*\bdeploy-time-learning\b' kb/notes/ | xargs rg '^description:'` — 19 hits, subset of above; same four flagged.
- `rg -l '^tags:.*\bfailure-modes\b'` — `llm-generation-confidence-tracks-typicality-not-soundness`, `knowledge-storage-does-not-imply-contextual-activation`, `elicitation-...` — none key on the over-generalization-as-dropped-boundary mechanism; not kept.

**Body/candidate evaluation (read frontmatter + opening):**
- `an-accepted-edit...` (seedling): "acceptance judged the *instance* … never judged the *rule*" — verbatim instance of source's "a success is an existence proof … imports a boundary the agent has not earned." Kept.
- `choosing-what-to-learn...` (current): "valid enough to learn from" + "worth learning" — source's boundary-statability test is a criterion for the validity gate. Kept.
- `diagnostic-richness...` (current): "diagnostic richness decides what the proposer can infer from previous attempts" — the rich failure evidence is exactly what supplies the boundary clause the source keys on (uncompressed reflection). Kept.
- `trace-derived-memory-earns-authority...` (seedling): "authority earned through verify, distill, consult with increasingly hard oracles" — abstracting an episode IS the distil operation; the boundary test is its oracle. Kept.

**Link following:**
- From `an-accepted-edit` and `trace-derived-memory` (both tagged `distillation`) — neighbourhood overlaps source's already-authored `distillation-is-transformation-not-selection`; no new targets surfaced beyond the four above.

## Connections Found

- [an accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) — **extends**: the accepted-edit case develops the source's success/existence-proof asymmetry in the edit-mining domain — a confirmation is a strong instance-oracle but silent about the rule, exactly the unearned boundary the source warns against. (Target `seedling`; `extends` is additive, no flag needed.)
- [choosing what to learn requires both validity and learning-value gates](../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — **extends**: the boundary-statability discriminator is a concrete criterion for that note's validity gate (trustworthy-enough-to-learn-from); following the link gives the broader two-gate promotion frame the discriminator slots into.
- [diagnostic richness constrains outer-loop learning quality](../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **grounds**: the source's claim that compressing reflection strips the condition clause rests on the premise that inspectable failure evidence carries the boundary — that note establishes diagnostic richness as a first-class learning bottleneck. (Target `current`; load-bearing label safe.)
- [trace-derived memory earns authority per operation, not at capture](../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md) — **extends**: abstracting an episode into a lesson is the "distil" operation in that note's per-operation authority pipeline, and the boundary-statability test is the oracle that licenses the distilled rule; the link places the source's decision inside the broader authority-earning frame. (Target `seedling`; `extends` additive, no flag.)

## Bidirectional Candidates

- [choosing what to learn requires both validity and learning-value gates](../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) <-> source — return **extends**: the gates note could point back to the source for the boundary-statability discriminator that sharpens its validity gate.

## Reverse-edge Candidates

- [an accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) → source — **exemplifies**: under notes-collection rules the accepted-edit note (instance) could author an `exemplifies` edge up to the source (general claim that a confirmation imports an unearned generalization boundary). This is the more natural primary direction; decide whether to author it from the accepted-edit side rather than the forward `extends` above, not both.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [raw accumulation does not create usable memory](../../notes/raw-accumulation-does-not-create-usable-memory.md) — surface tension with the source's "preserve the instance" advice, but no real contradiction (a preserved, retrievable instance is not a raw dump) and no load-bearing authorised label fits; the source already covers the long-tail/retrievability half via the existing `memory-management-policy` link.
- [systematic prompt variation serves verification and diagnosis, not...](../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — shares the Deutsch variation/reach vocabulary with the source's "process verification validates the why," but the association is keyword-level; no authorised notes→notes label (`see-also` targets reference/sources, not notes) carries it without forcing.

## Index Membership

- [deploy-time-learning-README](../../notes/deploy-time-learning-README.md) — source carries `deploy-time-learning` and is not yet listed; a future writer would add the entry under that tag's curated head (and, since `learning-theory-README` is `covered_by` deploy-time-learning, that child listing satisfies the learning-theory routing too).

## Synthesis Opportunities

A latent higher-order claim threads the source, [an accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md), and [trace-derived memory earns authority per operation](../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md): *a confirmation (success, human acceptance, captured trace) is an instance-level oracle and cannot, by itself, license a generalization — the boundary/condition clause requires a separate, harder oracle.* The `an-accepted-edit` note may already be the cleanest home for this; flagged for a writer to judge whether it warrants its own synthesis note rather than three parallel statements.

## Maintenance Observations

None.

## Flags

- The source is a candidate for the `failure-modes` tag (its central object is the over-generalized lesson, an explicitly named failure mode); not a connection candidate, noted for the author's tagging judgment.
