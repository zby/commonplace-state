---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md"
source_has_frontmatter: true
date: "2026-07-29"
depth: standard
---

# Connection Report: The bitter lesson selects production methods, not representational forms

**Source:** [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md)

## Discovery Trace

**Curated heads:**

- Read `kb/notes/README.md` and the three matching tag heads: `learning-theory-README.md`, `deploy-time-learning-README.md`, and `foundations-README.md`. The learning-theory head declares `covered_by: [deploy-time-learning, ...]`, so it routes this source through its child rather than listing it directly. It does not declare `complete: true`; the by-tag scan was therefore not skipped. Neither matching child head declares `complete: true`.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. `kb/types/` has no `README.md`; its complete title surface and collection contract were used instead.
- The deploy-time-learning head surfaced a missing general mechanism in `diagnostic-richness-constrains-outer-loop-learning-quality.md`. The agent-memory head's trace-learning comparison led to SkillRL and Autocontext as mixed-form implementation prospects. The other heads supplied orientation but no stronger candidate than their scoped searches.

**Full title and description scans:**

- Generated the complete fresh title surface once for every authorized local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, for `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` and filtered the resulting path-plus-description surfaces for `bitter|representational|production|search|learn|localized|symbolic|parametric|scaffolding|harness|credit assignment|selection`.
- Ran the required by-tag description listings for `deploy-time-learning` and `foundations` with `rg -l '^tags:.*\\bTAG\\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\\s*' -r ''`. Also ran the `learning-theory` listing because its head has `covered_by` but not `complete: true`.
- Notes prospects included codification/relaxing, diagnostic richness, constraining-as-learning, reflective coverage, explicit retention, and several targets already linked by the source. Codification/relaxing and diagnostic richness survived articulation. Existing targets were removed from candidate sections rather than re-proposed.
- Reference surfaced `proposals/bidirectional-codification-comparative-test.md`, whose four-arm experiment is a concrete but narrower companion to the source's requested mixed-form comparison. Types supplied no plausible trigger: global artifact contracts do not bear on the production-method/form distinction. Instructions likewise supplied no outbound candidate; the source does not need an execution procedure, and instruction links are inverse by default.
- Agent-memory systems surfaced SkillRL and Autocontext as implementations spanning readable artifacts and weights. SkillRL survived because it couples an actively used natural-language SkillBank to SFT/RL policy learning in one inspected system; Autocontext was rejected because its weight-distillation path is optional and not shown to co-evolve with its artifact loop.
- Agentic systems surfaced Exo's explicit bitter-lesson placement. It survived only as a reverse-edge candidate: Exo should use this source to distinguish learning to produce harness content from retaining a localized harness form.
- Sources surfaced SkillRL, Symbolic Learning, Co-Harness, Meta-Harness, and the update-substrate survey. Direct source pairs already linked from the target were rejected as duplicates; the code-grounded SkillRL review was preferred over its paper ingest for the new implementation candidate.

**Body search:**

- Ran `rg -n -i "bitter lesson|production method|hand-crafted|learned localized|credit assignment|chain rule" kb/notes/ --glob '*.md'`.
- Ran `rg -n -i "representational form|codif(y|ication)|search.*(evaluation|retention)|mixed-form|model weights" kb/reference/ --glob '*.md'`.
- Ran `rg -n -i "co-evol|model weights|weight promotion|skillbank|credit assignment|natural-language.*symbolic|symbolic.*parametric" kb/agent-memory-systems/ --glob '*.md'`.
- Ran `rg -n -i "bitter lesson|hand-engineered harness|self-improv|model weights|search.*harness" kb/agentic-systems/ --glob '*.md'`.
- Ran `rg -n -i "bitter lesson|production method|co-evol|credit assignment|model weights|symbolic learn|localized" kb/sources/ --glob '*.md'` and `rg -n -i "representational form|bitter lesson|credit assignment|learning loop|codif" kb/instructions/ --glob '*.md'`.
- The notes search showed that `machinery-persists-by-warrant-not-position-in-a-reflective-loop.md` and `scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md` already author inbound edges to the source. It also exposed a vocabulary tension: `constraining-during-deployment-is-continuous-learning.md` counts manually accumulated artifacts as learning under Simon's capacity-change definition, while this source reserves its learned production column for search and selection.

**Link following:**

- Followed the source's existing neighborhoods through representational-form coevolution, the readable-artifact loop, proposal-selection, machinery persistence, localized retention, oracle accumulation, and the four cited fourth-quadrant systems. These confirmed that the current note already covers general loop anatomy, frontier recurrence, and its primary published cases.
- Followed codification/relaxing into its exact-spec/proxy-theory distinction and comparative-test proposal. The note contributes per-component movement across the source's method axis; the proposal turns one readable-form subproblem into a falsifiable four-arm experiment.
- Followed diagnostic richness into Meta-Harness and the trace-learning comparison. It adds a missing distinction inside the source's credit-assignment problem: an oracle selects winners, while diagnostic evidence lets the proposer infer what to change.
- Followed SkillRL's review and ingest. The code-grounded review verifies a path from trajectory-derived natural-language skills in symbolic JSON through prompt injection into SFT/RL policy learning, while also bounding lifecycle and provenance weaknesses.
- External prospecting was skipped. `external` is authorized for already-known targets only, and no unrecorded external target was supplied.

## Connections Found

- [Codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- **extends**: develops the source's static two-axis matrix into a time-indexed per-component dynamic, explaining how a localized artifact can move between hand-crafted and learned production as codification bets are tested and relaxed.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **mechanism**: separates the source's missing localized credit-assignment machinery into selection evidence and proposal evidence; an oracle can choose a winner while traces, diffs, and component state determine whether the next proposer can infer which artifact should change.
- [Bidirectional codification as a comparative test](../../../../reference/proposals/bidirectional-codification-comparative-test.md) -- **see-also**: supplies an explicit four-arm experiment over natural-language-only, symbolic-only, one-way, and bidirectional regimes, a narrower readable-form test that could become one component of the source's broader localized-versus-parametric comparison.
- [SkillRL](../../../../agent-memory-systems/reviews/SkillRL.md) -- **evidenced-by**: code-grounded evidence of one system coupling trajectory-derived natural-language skills in symbolic JSON with prompt-time use and SFT/RL policy learning; it is a bounded mixed-form fragment, not evidence that corpus-scale localized credit assignment is solved.

## Bidirectional Candidates

- [Codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) <-> source -- reverse **grounds**: the source supplies the orthogonal production-method/form distinction needed to state precisely what codification and relaxation move between, while the target independently develops the movement dynamics.
- [SkillRL](../../../../agent-memory-systems/reviews/SkillRL.md) <-> source -- reverse **is-evidence-for**: the reviewed system materially bears on the source's mixed-form conjecture and should expose that theoretical implication to readers comparing SkillRL's artifact and policy-learning paths.

## Reverse-edge Candidates

- [Exo](../../../../agentic-systems/reviews/exo.md) -> source -- **rests-on**: Exo's bitter-lesson placement argues that an agent should learn to rewrite hand-engineered harness policy; the source clarifies that this changes the harness's production method without implying that localized harness form itself must disappear.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) -- rejected as an outbound edge because it uses the broader capacity-change meaning of learning and bundles manual with automated constraining; without an explicit context phrase about the terminological contrast, it would blur the source's hand-crafted versus search-and-selection column boundary.
- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) -- rejected because it classifies which operations a system exposes over each form, not how the contents of those forms are produced; the shared form vocabulary alone does not pass articulation.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) -- rejected because its addressability/governance comparison concerns properties after retention, while the source already carries the narrower authority and authoritative-record claims needed for its argument.
- [Autocontext](../../../../agent-memory-systems/reviews/autocontext.md) -- rejected in favor of SkillRL: Autocontext spans natural-language, symbolic, and optional parametric outputs, but its reviewed weight-distillation path is secondary and does not demonstrate coevolution or comparative advantage across forms.
- [Ingest: SkillRL](../../../../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md) -- rejected as a second candidate edge because the code-grounded system review verifies the relevant mixed-form implementation more directly; the paper ingest remains useful evidence behind that review.
- [Ingest: Symbolic Learning Enables Self-Evolving Agents](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) -- rejected as an additional edge because the source already links the paired snapshot for its whole-harness search and cross-node credit-assignment evidence.
- [The What & When of Self-Evolving Agents](../../../../sources/the-what-and-when-of-self-evolving-agents.ingest.md) -- rejected because its substrate-by-horizon taxonomy describes where updates land but does not establish that production method is independent of representational form; linking it here risks reinstating the conflation the source corrects.

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) -- the source supplies the framework with its central method/form distinction and a falsifiable account of the missing machinery for learned localized artifacts.
- [Foundations](../../../../tags/foundations-README.md) -- the source rules out two symmetric architectural positions and states a field-organizing mixed-form conjecture with explicit failure conditions.

## Synthesis Opportunities

None. The apparent synthesis between credit assignment, diagnostic richness, and proposal selection is already stated by the source plus the diagnostic-richness note; no additional higher-order claim was found.

## Maintenance Observations

- The KB now uses two legitimate meanings of “learning” in adjacent notes: permanent capacity change in [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md), and search-plus-selection production in this source's matrix. Future linking or revision should name the operative definition rather than treating the terms as interchangeable.

## Flags

- Terminology tension: the source's learned production column is narrower than the deploy-time-learning cluster's Simon-derived capacity-change usage. This is not a contradiction, but it is easy for a reader to mistake it for one.
