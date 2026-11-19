---
description: "Connection discovery for reference-only adversarial post-training and learned judge boundaries."
type: types/connect-report.md
source: kb/sources/.snapshots/reinforced-adversarial-learning.md
source_has_frontmatter: true
date: "2026-11-15"
depth: standard
---

# Connection Report: Reinforced Adversarial Learning

**Source:** `kb/sources/.snapshots/reinforced-adversarial-learning.md` (local immutable reading copy).

## Discovery Trace

Read the sources collection contract and connect-report type before discovery. Read curated README heads for theory, reference, agent-memory-systems, agentic-systems, tags and sources. Generated fresh complete title listings per destination with `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'`, filtering for `judg|evaluat|critic|reward|adversar|verif|learn|reason|quality|truth`.

- Theory: title hits exposed bounded judgments, verifiability gradient and the boundary of automation. Read the first two fully and inspected the boundary argument. Kept the first two for the judge interface and distinction between proxy reward and independently checked correctness. The automation-boundary note is broader and adds no separate traversal need here.
- Reference: title and description scans found review verification and trajectory-evaluation proposals, not a direct implementation of parametric adversarial training. No candidate retained.
- Agent-memory-systems and agentic-systems: title scans plus `rg -n -i 'adversarial|co.train|rubric'` exposed many review and memory loops. Their persistent-artifact mechanisms differ from this weight-training loop; no direct candidate retained.
- Tags: the title scan exposed evaluation and learning theory. These are discovery surfaces, not authorised source-to-tag edges; no index membership proposed.
- Sources: titles exposed SkillLift and the judge lifecycle paper. The scoped description scan `rg '^description:' ... | grep -Ei 'judge|adversarial|rubric|reward'` confirmed both; read both ingests. Kept SkillLift as a precise comparison of evaluator adaptation with independent execution checks; the Netflix lifecycle is a more distant production comparison and was not retained.
- Theory body search: `rg -n -i 'adversarial|judge capacity|fooling rate|rubric' kb/theory --glob '*.md'` exposed reasoning-evaluation cautions and oracle discussions. The bounded-judgment note's training/interface distinction remains the most direct fit.
- Link following: followed the verifiability gradient's oracle-strength comparison by inspecting descriptions. No additional edge was necessary. Read theory COLLECTION.md for reverse-edge authority. External prospecting was skipped; only the supplied arXiv URL is in scope as an already-known external target. Work and instructions were excluded.

### Candidate origins

- kb/theory/language-models-for-bounded-judgments-form-an-emerging-category.md — titles, body-search
- kb/theory/verifiability-gradient.md — titles, descriptions
- kb/sources/skilllift-dense-rubrics-sparse-oracles.ingest.md — titles, descriptions

## Connections Found

The authored surface for these snapshot candidates is the future name-paired ingest, not the immutable snapshot.

- [Bounded judgment models](../../../../theory/language-models-for-bounded-judgments-form-an-emerging-category.md) — **compares-with**: the paper specializes a separately scaled judge for one-token reference classification and consumes its probability as reward; this gives a training-specific contrast to reusable decision endpoints without establishing general calibration.
- [The verifiability gradient](../../../../theory/verifiability-gradient.md) — **compares-with**: withholding exact checks during training while using them for evaluation separates learned feedback from independent correctness assessment; fooling rates in open-ended writing check a different property.
- [SkillLift](../../../../sources/skilllift-dense-rubrics-sparse-oracles.ingest.md) — **compares-with**: both adapt an evaluator alongside a generator, but SkillLift calibrates textual guidance against execution outcomes whereas RAL learns a weight-based discriminator from reference membership.

## Bidirectional Candidates

- [Bounded judgment models](../../../../theory/language-models-for-bounded-judgments-form-an-emerging-category.md) → future ingest — **evidenced-by**: qualifies the category's specialization discussion with a task-specific co-trained judge whose output probability controls optimization. This is an adjacent training case, not corroboration of the category's usefulness for KB routing. Any eventual source use must satisfy theory's grounding contract.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Judge lifecycle](../../../../sources/lifecycle-llm-judge-recommendation-explanations.ingest.md) — rubric maintenance with human rationale labels is a more distant comparison than SkillLift; avoid a broad judge-related link spray.
- [Automation boundary](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) — broad contextual relation; the more specific gradient comparison preserves the exact checked-property distinction.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

Connection candidates concern evaluator design, not evidence that reference imitation yields scientifically true or useful proposals. No links were authored.
