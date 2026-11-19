---
description: "Post-ingest discovery for RAL's learned reward, checking-property distinction and specialised judge interface."
type: types/connect-report.md
source: kb/sources/reinforced-adversarial-learning.ingest.md
source_has_frontmatter: true
date: "2026-11-15"
depth: standard
---

# Connection Report: Reinforced Adversarial Learning ingest

**Source:** [Accepted ingest](../../../../sources/reinforced-adversarial-learning.ingest.md)

## Discovery Trace

Read the accepted ingest fully. Sources COLLECTION.md, the connect-report type, and the destination curated README heads were read during this run and remain current. This is a separate discovery pass on the published analysis, not publication of the snapshot report's suggestions.

Generated fresh complete title listings for theory, reference, agent-memory-systems, agentic-systems, tags and sources using `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'`, then filtered with `bounded judgment|verifiability gradient|fixed decomposition|SkillLift|judge|adversarial|reward`.

- Theory: the ingest already names bounded judgments, verifiability gradient and fixed decomposition. Fresh titles exposed them again. Read the first two during snapshot discovery and the fixed-decomposition note fully in this pass. They address three distinct reader needs: judge specialisation, property-specific checking, and the unchanged interface around learned weights.
- Reference: the scan exposed judged-version records, not an applicable RAL implementation or calibration experiment. No retained target.
- Agent-memory-systems: no close title match. Earlier scoped `rg -n -i 'adversarial|co.train|rubric'` found artifact-learning mechanisms rather than this training method. No additional connection.
- Agentic-systems: SkillLift is a title hit; its source ingest supplies the narrower direct comparison. No system-review edge is needed.
- Tags: no matching title under this narrow scan. The evaluation head remains a discovery surface, not an authorised outbound target.
- Sources: SkillLift and the Netflix judge lifecycle reappear. Read their analyses during snapshot discovery; retained SkillLift's independent execution calibration as the sharper comparison. The Netflix case adds no distinct immediate traversal need.
- Description scan: `rg '^description:' kb/theory kb/sources --glob '*.md' | grep -Ei 'fixed decomposition|bounded judgment|reference.answer|dense rubrics'` found the accepted ingest and broader fixed-decomposition applications; no stronger omitted target.
- Body search: `rg -n 'reference|independent|proxy'` on the gradient and bounded-judgment notes located their requirement-strength and calibration boundaries. These passages justify inbound paths independently of the ingest's existing outbound links.
- Link following: the ingest's fixed-decomposition link led to the complete note, whose unchanged-interface qualification fits judge-size comparisons without asserting a demonstrated decomposition error. No further edge was retained.
- Theory COLLECTION.md authorises source citations as `evidenced-by` when they qualify or bound an assertion. Any future citation must satisfy the source-grounding contract. External prospecting was skipped; work and instructions were excluded.

### Candidate origins

- kb/theory/language-models-for-bounded-judgments-form-an-emerging-category.md — known, titles, body-search
- kb/theory/verifiability-gradient.md — known, titles, body-search
- kb/theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md — known, titles, link-following
- kb/sources/skilllift-dense-rubrics-sparse-oracles.ingest.md — known, titles

## Connections Found

The first three connections are already discussed in the ingest; they are retained here as evaluated candidate relationships, not newly authored links.

- [Bounded judgment models](../../../../theory/language-models-for-bounded-judgments-form-an-emerging-category.md) — **compares-with**: independently scaled, one-token reference classification is a training-specific specialisation; probability-as-reward does not establish calibration as a decision service.
- [Verifiability gradient](../../../../theory/verifiability-gradient.md) — **compares-with**: exact evaluation after verifier-withheld training and abstract discrimination check different properties. This concretises the separation of feedback and requirement.
- [Fixed decomposition](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: capacity improves the learned mapping within a fixed answer-only interface; no alternative-interface comparison establishes that boundary as preferable or mistaken.
- [SkillLift](../../../../sources/skilllift-dense-rubrics-sparse-oracles.ingest.md) — **compares-with**: evaluator adaptation uses execution-calibrated textual guidance in SkillLift, versus reference-membership-trained weights in RAL. This additional comparison remains only a discovery candidate.

## Bidirectional Candidates

- [Verifiability gradient](../../../../theory/verifiability-gradient.md) → [ingest](../../../../sources/reinforced-adversarial-learning.ingest.md) — **evidenced-by**: qualifies the checking discussion with a concrete paired example: training without exact rewards can improve exact held-out correctness, while fooling abstract evaluators checks resemblance rather than truth. This serves readers selecting which property their check must establish; it is not corroboration of a universal claim. Full experimental assessment currently needs the snapshot, so a future source citation must declare that requirement or first retain suitable quotes.
- [Bounded judgment models](../../../../theory/language-models-for-bounded-judgments-form-an-emerging-category.md) → [ingest](../../../../sources/reinforced-adversarial-learning.ingest.md) — **evidenced-by**: qualifies the specialisation discussion with a co-trained one-token reward judge whose needed capacity can exceed the generator's. Readers comparing role, readout and training gain a distinct case; this does not corroborate KB efficiency or decision-probability calibration. The future author must handle source grounding, not infer support from the existing outbound edge.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Judge lifecycle](../../../../sources/lifecycle-llm-judge-recommendation-explanations.ingest.md) — production rationale and human-label maintenance is more distant than the retained execution-calibration comparison.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

No library links were authored. Inbound suggestions require separate authorisation and grounding. The accepted report's recommended next action is the gradient comparison, not deployment of an adaptive KB judge.
