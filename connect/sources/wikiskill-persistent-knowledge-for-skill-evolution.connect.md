---
description: "Connection candidates for WikiSkill's persistent wiki, gated skill updates, and cross-model transfer experiments"
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: WikiSkill

**Source:** [WikiSkill](../../../../sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md)

Candidates below belong on the paired ingest, not on the immutable snapshot. Discovery used cp-skill-connect; this is a cache report, not a published analysis.

## Discovery Trace

- Read the full captured paper, the source collection's outbound rules, and the connect-report type. Read the notes README and the reference, agent-memory-systems, and agentic-systems navigation heads. No source tags were supplied, so no by-tag completeness rule applied.
- Generated the fresh title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`; narrowed the large listing with `rg -i 'learn|skill|experience|trace|reflect|memory|validation|rollback'`. Long outputs were truncated, so the title pass was supplemented with focused descriptions and candidate reads.
- Description search: `rg '^description:.*(trace|skill|experience|rollback|persistent)' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`. This surfaced the diagnostic-richness, skill-derivation, trace-authority, retained-adaptation, and compounding notes, plus ACE and Autocontext reviews.
- Notes: read the skill-derivation, diagnostic-richness, trace-authority, retained-adaptation, and compounding notes. Followed the retained-adaptation note's link to the proposal-selection-loop note. Kept the more specific diagnostic and authority contrasts rather than adding every broad learning connection.
- Reference: searched `rollback|validation|wiki|skill` in the gate-learning proposal and read it. Kept its promotion/rollback design as an adjacent comparison; this is a proposal, not a shipped learning capability.
- Agent memory: searched `rollback|validation|wiki|skill` in ACE and Autocontext and inspected ACE's artifact/read-back account. Kept ACE because its whole-playbook solver input directly contrasts with WikiSkill's separation of wiki and active skills. Autocontext is plausible but omitted to keep the selected comparisons focused.
- Agentic systems: read the index and inspected the Academic Research Skills matches from `rollback|validation|wiki|skill`. Rejected that candidate: a host-dependent research workflow's skills and checks do not provide the same experience-to-skill evolution mechanism. Other title-level harness candidates would require a separate detailed comparison and were not promoted here.
- Sources: read `kb/sources/README.md`; generated the complete source title listing with `rg -N --no-heading -m1 '^# ' kb/sources --glob '*.md'` and narrowed it with `rg -i 'memory|skill|state|harness|wiki|continual|compil|life|forget|retriev'`. Queried `^description:|^## |wiki|history|rollback` in SkillOpt, Karpathy LLM Wiki, and Harness Updating Is Not Harness Benefit. Read SkillOpt and Harness Updating fully and Karpathy's summary, value, and limitations. Kept all three on distinct axes: optimizer-history organization, stated wiki inspiration, and update-production versus consumer benefit. SkillOpt's links also surfaced Agent Workflow Memory and trajectory-informed tips; these are less direct than the actual benchmark baseline and were not expanded into additional edges.
- External: no web prospecting. The paper's arXiv URL is already in hand. Its Karpathy LLM Wiki citation is provenance context, not an official WikiSkill implementation repository.
- Reverse direction: checked `evidenced-by` authorization in `kb/notes/COLLECTION.md`; the diagnostic-richness note is a candidate for a source citation after the ingest exists and grounding is arranged.

## Connections Found

- [Skills derive from methodology](../../../../notes/skills-derive-from-methodology.md) — **compares-with**: WikiSkill retains wiki patterns and skill provenance separately from procedural skill text, supplying a concrete comparison for a reasoning layer feeding a fast procedural layer. Its training solver cannot consult the wiki, so it does not establish the note's live runtime fallback claim.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **is-evidence-for**: WikiSkill's proposer combines retained pattern pages, rejected proposal history, and raw-trace drill-down. Its wiki ablation changes both wiki access and the maintainer, so the reported gain supports the retained diagnostic bundle rather than isolating any one information type.
- [Trace-extracted memory earns authority per operation](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — **compares-with**: WikiSkill gates proposed skills on validation performance while retaining every wiki update. This separates procedural selection from the authority of diagnoses and generalizations in the persistent wiki; accepting a skill does not verify every contributing pattern.
- [Compounding is tested in later improvement](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — **compares-with**: WikiSkill calls the wiki compounding and reports persistent-wiki ablations, iteration statistics, and an illustrative proposal-history case. The note supplies a stricter test of later improvement productivity and causal uptake than accepted skill counts alone.
- [ACE](../../../../agent-memory-systems/reviews/ace.md) — **compares-with**: the retained review describes trace-derived playbook text supplied wholesale to the generator. WikiSkill instead keeps a persistent wiki for the improver and injects only active skills into its default solver, permitting a focused comparison of consumers and retained artifact boundaries.
- [Gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md) — **see-also**: the proposal also separates mined candidates from promoted behavior-changing artifacts and treats rollback as necessary. WikiSkill supplies an experimental skill-update counterpart, while Commonplace gate learning remains proposed.
- [SkillOpt](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) — **compares-with**: both retain rejected proposals and accept skill changes only on strict validation improvement; WikiSkill adds a separately maintained pattern wiki to the optimizer's history. This comparison should not suggest that SkillOpt discards all historical feedback.
- [LLM Wiki](../../../../sources/karpathy-llm-wiki.ingest.md) — **compares-with**: WikiSkill explicitly cites Karpathy's persistent-wiki idea, but adapts raw/wiki/schema into raw/wiki/skills and tests downstream skill evolution rather than general personal knowledge work.
- [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) — **compares-with**: both separate producing useful updates from executing them through cross-model pairings. WikiSkill injects skills directly, whereas the harness study also measures skill loading; these designs expose different uptake bottlenecks.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) → paired WikiSkill ingest — **evidenced-by**: add a bounded observation of retained wiki plus maintainer access improving skill evolution, with the bundled-ablation caveat. Ground through the future ingest before authoring this edge.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Retained artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md): useful broad background, but WikiSkill's experiment is offline benchmark skill evolution, not evidence of an installed online deployment adaptation loop. More specific candidates above provide a clearer reader benefit.
- [Academic Research Skills](../../../../agentic-systems/reviews/academic-research-skills.md): shared skill packaging and gates do not establish a sufficiently specific learning-mechanism comparison.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

The sources collection names `agent-memory` in its label destinations while the actual directory is `agent-memory-systems`. This report follows the collection's explicit instruction to scan that directory; no vocabulary change is made.

## Flags

- PDF text extraction flattens table structure and loses checkmark semantics. Numerical or ablation-table interpretations should use surrounding prose and the original PDF where necessary.
- No official WikiSkill GitHub implementation URL was identified in the captured paper; the GitHub Gist citation belongs to Karpathy's LLM Wiki.
- WikiSkill's persistent wiki is never rolled back or automatically pruned. Its skill validation gate must not be described as validating or governing every retained wiki claim.
