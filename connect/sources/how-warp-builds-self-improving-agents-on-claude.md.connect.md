---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/how-warp-builds-self-improving-agents-on-claude.md"
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: How Warp builds self-improving agents on Claude

**Source:** [How Warp builds self-improving agents on Claude](../../../../sources/.snapshots/how-warp-builds-self-improving-agents-on-claude.md)

The snapshot is immutable. Every outbound candidate below is for the matching authored surface, normally `kb/sources/how-warp-builds-self-improving-agents-on-claude.ingest.md`, once that ingest exists.

## Discovery Trace

**Routing and curated heads:**

- Read `kb/sources/COLLECTION.md`. It authorises prospecting in `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`; excludes `work` and `instructions`; and permits an already-known `external` target without open-web prospecting.
- Read the curated heads `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The target has no `tags:` field, so no matching tag-README pass or completeness-mark skip applied.
- Generated each complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: 385 headings in notes, 157 in reference, 174 in agent-memory-systems, 12 in agentic-systems, and 334 in sources.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over every destination: 383 description lines in notes, 156 in reference, 172 in agent-memory-systems, 10 in agentic-systems, and 334 in sources. These were lexical scans; no semantic-search scores were available.

### Notes

**Body search:**

- `rg -n 'human feedback|feedback quality|diagnostic richness|outer[- ]loop' kb/notes/ --glob '*.md'`
- `rg -n 'retained instruction|behavio(u)?r-changing|behavior-shaping|deployment-time adaptation' kb/notes/ --glob '*.md'`
- `rg -n 'principles,? not rules|explain(s|ing)? the why|rationale.*generaliz|small,? focused' kb/notes/ --glob '*.md'`
- Follow-up filename scans included `rg -l -i 'proposal-selection improvement loop|proposal-selection loop|search, evaluation, and (operative )?retention' kb/notes --glob '*.md'` and `rg -l -i 'compounding|human-gated|acceptance.*operative|accepted.*operative' kb/notes --glob '*.md'`.

**Candidate evaluation:** The full feedback-to-patch-to-merge path kept the proposal-selection, persistent deployment-time adaptation, readable-artifact, and diagnostic-richness notes. The article's human approval and “compounds” wording also make the accepted-edit and accumulation/compounding boundaries useful contrasts. Broader continual-learning governance was rejected as redundant with those more discriminating targets; the retained-instruction note was rejected because the article reports no candidate comparison or test isolating a selected instruction; the two-gate note was rejected because Warp does not separate validity from learning value.

**Link following:** From the proposal-selection note, followed its operative-retention and false-positive-acceptance neighborhood; from persistent deployment-time adaptation, followed the readable-artifact loop; from diagnostic richness, followed the trace-learning survey; and from the compounding boundary, followed the later-episode measurement note. These hops tightened the candidates around promotion authority, diagnostic evidence, and downstream-effect claims rather than generic self-improvement vocabulary.

### Reference

**Body search:**

- `rg -n -i 'human|evaluation|retention|feedback|merge|approve' kb/reference/tag-readme-trace-as-self-improving-loop.md kb/reference/proposals/gate-learning-from-accepted-edits.md kb/reference/where-change-candidates-come-from-in-commonplace.md`
- `rg -n -i 'accepted edit|candidate mining|skill|instruction'` over the same three files.
- `rg -n -i 'self-improv|improvement loop'` over the same three files.

**Candidate evaluation:** The implemented tag-README trace matches Warp on joint candidate drafting, human judgment, merge, and later computational use. The gate-learning proposal matches the feedback-to-generalised-instruction design and its promotion problem. Both pass the articulation test, but their natural labels (`compares-with` and `is-evidence-for`) are not authorised for sources→reference. They are therefore off-authorisation rather than weakened to `see-also`. `where-change-candidates-come-from-in-commonplace.md` was rejected because it surveys noticing channels, not the feedback-to-skill-update mechanism.

**Link following:** The tag-README trace led back to the proposal-selection loop and the human-gate/oracle boundary. The gate-learning proposal led to the accepted-edit-versus-rule note, confirming that the useful comparison concerns generalisation and promotion rather than mere topical overlap.

### Agent memory systems

**Body search:**

- `rg -n -i 'feedback.*skill|skill.*feedback' kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md`
- `rg -n -i 'human.*(review|feedback)|review.*human' kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md`
- `rg -n -i 'skill.*(update|edit|evolv)|improv.*skill|outer[- ]loop' kb/agent-memory-systems/ --glob '*.md'`
- `rg -n -i 'feedback|skill|approv|curat|trace|human' kb/agent-memory-systems/reviews/hermes-agent.md`

**Candidate evaluation:** Kept the trace-learning survey because Warp adds a practitioner case of explicit human-feedback-to-readable-skill promotion. Kept Hermes because its background fork converts corrections and traces into progressively disclosed skills, but makes approval optional and off by default. Kept ARIS because it separates log-driven skill-patch proposals from a human-invoked, separately reviewed landing path. The Agent Skills for Context Engineering review was rejected: file-based skills and progressive disclosure overlap, but its reviewed mechanism does not supply the same recurring explicit-feedback and approval path.

**Link following:** The diagnostic-richness note led into the survey's readable-artifact-learning and skill-text-promotion sections. From there, followed the Hermes and ARIS reviews to compare trigger cadence, evidence source, landing authority, lifecycle controls, and whether human approval is mandatory.

### Agentic systems

**Body search:**

- `rg -n 'self-improv|feedback|skill|review|human' kb/agentic-systems/ --glob '*.md'`
- `rg -n -i 'skill|feedback|self-mod|optimi|human|schedul|gate|approv' kb/agentic-systems/gbrain.md`

**Candidate evaluation:** Kept GBrain because its scheduled dream cycle invokes a skill optimizer and reserves bundled-skill mutation for human review, giving a whole-system comparison for Warp's scheduled improver and final human merge gate. Compound Engineering was evaluated but rejected in favour of GBrain: its installed plugin skill corpus is normally frozen outside the runtime update loop, so the comparison is useful mainly as a boundary contrast already captured by GBrain and the proposal-selection notes. Exo was rejected because broad rewritable-executor self-modification would make the link a system-level analogy rather than a direct skill-feedback comparison.

**Link following:** GBrain's self-modification section led to its machine-score validation and bundled-skill `proposed.md` boundary; this made the reader payoff precise: compare explicit human feedback plus mandatory approval with scheduled benchmark/judge optimisation plus a narrower human checkpoint.

### Sources

**Body search:**

- `rg -n 'human feedback|review-derived|feedback.*skill|skill.*feedback|accepted edit' kb/sources/ --glob '*.md'`
- `rg -n 'improver|base skill|outer[- ]loop|self-improving.*skill' kb/sources/ --glob '*.md'`
- `rg -n 'reviewed.*merged|review.*merge|small,? focused' kb/sources/ --glob '*.md'`
- Follow-up filename scans included `rg -l -i 'accumulat.*rules|review.*rules|human.*feedback' kb/sources --glob '*.ingest.md'` and `rg -l -i 'harness.*(improv|updat)|self-improv' kb/sources --glob '*.ingest.md'`.

**Candidate evaluation:** Kept the accumulated-rules ingest as the nearest human-review-feedback-to-versioned-instruction case; SkillOpt as the nearest separate-optimizer-to-compact-skill case under a hard validation oracle; and Harness Updating Is Not Harness Benefit as the strongest measurement counterpoint to unmeasured update and compounding claims. The AutoResearch/evals field report was rejected because its contribution is evaluator construction after manual error analysis, already reached more directly through diagnostic richness. Fluent was rejected as a broader software-factory loop, and Agno's recursive-improvement report was rejected because its trace/probe/code-edit loop is less specific to human feedback and skill files than the retained peers.

**Link following:** The accumulated-rules ingest led to the accepted-edit-versus-rule boundary; SkillOpt led to the readable-artifact and diagnostic-richness cluster; Harness Updating led to loading, procedural match, task benefit, and later-improvement measurement as separate stages.

### External

The source URL was already present in the snapshot metadata and body, so it was evaluated as the authorised `derived-from` target. Open-web prospecting was skipped, as required; no browser or external search service was used.

## Connections Found

- [Original Claude article](https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude) -- **derived-from**: the future ingest analysis is worked out from this captured practitioner article.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: Warp's base output and feedback drive a proposed edit, human review can reject it, and merge makes the accepted skill change operative in later runs.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **is-evidence-for**: versioned skill files change later agent behaviour without a model-weight update and can be reviewed, merged, and rolled into the next execution.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: Warp explicitly distinguishes low-information thumbs from detailed reasons that tell the improver what mechanism or convention failed.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: the reported loop mutates inspectable natural-language skills, can bundle scripts, uses normal diffs and review, and relies on progressive disclosure rather than weight changes.
- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) -- **compares-with**: Warp's final human approval governs whether a generalised skill edit lands, but the article reports no later behavioural test establishing that the extracted rule transfers beyond the feedback instance.
- [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md) -- **compares-with**: Warp reports retained updates and calls the feedback “compounding,” while the article supplies neither a displaced later-improvement measure nor a causal trace that an earlier benefit made later improvement more productive.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **is-evidence-for**: Warp adds an explicit-human-feedback, scheduled, readable-skill-promotion case to the survey's trace-to-instruction family.
- [Hermes Agent](../../../../agent-memory-systems/reviews/hermes-agent.md) -- **compares-with**: both separate foreground work from a periodic reviewer that can patch progressively disclosed skills; Hermes learns from recent trace snapshots and makes approval optional, whereas Warp accumulates explicit human feedback and requires final review before merge.
- [Auto-claude-code-research-in-sleep](../../../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md) -- **compares-with**: both use an outer process to propose small skill-file changes and keep landing authority separate; ARIS mines event/reviewer logs and uses a human-invoked cross-model gate, while Warp's stated primary signal is direct human feedback.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) -- **compares-with**: both schedule a separate skill optimiser and protect stronger instruction changes with review, but GBrain's local-skill path is score-gated while Warp's account centres explicit human feedback and mandatory PR approval.
- [Self-Improving AI Coding Agents Through Accumulated Behavioral Rules](../../../../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) -- **compares-with**: both turn code-review feedback into versioned instructions for later sessions; the paper uses an engineer's immediate class-of-mistake judgment and always-loaded rules, while Warp inserts a scheduled improver proposal and PR gate.
- [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) -- **compares-with**: both isolate a reusable optimiser from the base skill and make bounded text edits, but SkillOpt selects on scored rollouts and held-out validation while Warp selects through accumulated human feedback and review.
- [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) -- **compares-with**: the paper's update-production, loading, procedural-match, and task-benefit stages name measurements absent from Warp's architectural account and prevent merged skill edits from being counted as demonstrated downstream improvement.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

- [Gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md) -- Warp's human-feedback-to-skill-patch loop bears on this proposal's candidate-mining and human-promotion design, but `is-evidence-for` is not authorised for sources→reference and `see-also` would erase the evidential intent. Extend the collection authorisation only if source-side evidence links into reference proposals are intended; otherwise author the inverse reference→ingest edge after the ingest exists.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) -- the two cases compare directly on joint search, human evaluation, merge, and later computational retention, but `compares-with` is not authorised for sources→reference. Extend or reject rather than downgrading this to `see-also`.

## Raw Text Candidates

None

## Rejected Candidates

- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- genuine but redundant: the proposal-selection and persistent-deployment-time-adaptation candidates already expose Warp's selection, approval, authority, and later-use mechanism more precisely.
- [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) -- Warp reports feedback and approval, not a comparison or test that selected one candidate instruction under a stated criterion.
- [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -- “feedback quality > volume” does not establish separate validity and learning-value gates.
- [Agent Skills for Context Engineering](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) -- file-based skills and progressive disclosure match, but the reviewed system does not supply the same recurring explicit-feedback, scheduled-improver, and human-landing chain.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- useful as a frozen-versus-mutable skill-corpus contrast, but GBrain gives a closer whole-system scheduled skill-optimisation comparison without requiring a topology edge case.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- a rewritable executor and protected substrate are too broad a comparison for this source's bounded skill update loop.
- [Improving AI Skills with AutoResearch & evals-skills](../../../../sources/improving-ai-skills-with-autoresearch-evals-skills-203525743436.ingest.md) -- shares the claim that feedback/evaluation quality matters, but its distinctive mechanism is manual failure-taxonomy and judge construction rather than explicit feedback becoming a reviewed skill patch.
- [How I built a self-improving software factory](../../../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md) -- tested, reviewed, merged retention is real, but the factory-wide loop is less discriminating than the skill-specific accumulated-rules and SkillOpt comparisons.
- [How to Recursively Improve Your Agents](../../../../sources/how-to-recursively-improve-your-agents-2084301728363462919.ingest.md) -- trace-derived probes and code edits form a neighboring outer loop, but it is less specific to human feedback and skill files than the retained source comparisons.

## Index Membership

None

## Synthesis Opportunities

- The source plus [diagnostic richness](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), [accepted edit versus rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md), and [harness updating versus benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) imply a three-stage distinction not stated in one artifact: human feedback can improve candidate search, human approval can govern promotion, and downstream behavioural uptake still needs separate evaluation. “Human in the loop” should name which of these roles the human fills rather than treating them as one gate.

## Maintenance Observations

- The sources collection authorises only `see-also` into reference. The two off-authorisation cases show a recurring gap for source analyses that materially evidence or compare with a shipped-system trace or design proposal; deciding whether the preferred direction is always reference→source would resolve the ambiguity without broadening source-side labels.

## Flags

- The matching authored ingest does not yet exist. Do not apply any candidate to the immutable snapshot, and do not author reverse or bidirectional links to `.snapshots/`; create the ingest first, then evaluate any inbound edges against that real path.
- The article is a first-party practitioner account with architectural detail but no controlled outcome evaluation. Treat it as mechanism evidence, not proof of effectiveness or scale.
- The article's use of “compounds” is in unresolved tension with the KB's causal definition of compounding; the reported facts establish durable accumulation and reuse, not a measured contribution to later improvement productivity.
