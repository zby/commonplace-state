---
description: "Connection discovery for Anthropic's agent-memory experiments, with independently justified inbound evidence uses and bounded offline-memory comparisons."
type: types/connect-report.md
source: kb/sources/components-of-agent-memory.ingest.md
source_has_frontmatter: true
date: "2026-11-07"
depth: standard
---

# Connection Report: The components of agent memory

**Source:** [Ingest: The components of agent memory](../../../../sources/components-of-agent-memory.ingest.md)

Discovery-only output of `cp-skill-connect`, executed locally with model `gpt-6.1-sol`. Inputs are the current source ingest, collection contracts, and repository artifacts. No external search, agents, snapshot inspection, or library edits were performed. Empirical descriptions below inherit the ingest's vendor-report limitations; this pass discovers connections rather than independently checking the experiments.

## Discovery Trace

**Contracts and scope:** Read the source and reports collection contracts, the connect-report type, and the source in full before candidate discovery. The source authorizes theory, reference, historical agent-memory systems, agentic systems, tags, and other sources as discovery surfaces. Its label table provides no source-to-tags label. Work and instructions are excluded. Read the theory collection contract and note type for proposed inbound theory uses, the agentic-systems contract for account-boundary checks, and the sources contract for reciprocal ingest comparisons.

**Curated heads:** Read `README.md` in all six permitted local destinations. The theory head routes through tags; the reference head distinguishes shipped-system state from transferable claims. The historical memory-system head explicitly freezes its corpus. The agentic-systems head distinguishes authored accounts from archived analyses and current comparison inputs. The sources head supplies no topical roster. Read the agent-memory tag head in full and inspected the trace-learning and evaluation heads with scoped `rg`. The target has no `tags`, so no source-tag search or completeness-based skip applied.

**Complete title surface:** Executed `rg -N --no-heading -m1 '^# ' kb/$d/ --glob '*.md'` separately within a shell loop for `theory reference agent-memory-systems agentic-systems tags sources`. Recovered the truncated output from its tool log. This surfaced the episode-retention, access/transformation, end-to-end evaluation, trace-authority, activation, GBrain, OpenWiki, Sleep, and Karpathy neighborhoods. Brief titles were treated as part of their documents; no brief became a target.

**Description scan, all destinations:** Executed `rg '^description:' kb/$d/ --glob '*.md' | rg -i 'episode|transcript|offline|dream|wiki|memory.*(evaluat|cost|correct)|retriev.*(reason|synth)|ownership|activation'` for each of the six destinations. Evaluations:

- **Theory:** The episode-retention note is the strongest evidence-use match. The end-to-end evaluation note adds task-outcome and cost boundaries beyond the already-linked access/transformation note. Trace authority offers an independently useful inbound case comparison. Activation is relevant but already has stronger controlled interventions; do not add another weakly diagnostic case merely because it discusses memory.
- **Reference:** `agent-memory-coverage.md` and the gap plan surfaced. Read coverage in full: they describe Commonplace's shipped capabilities and limits, which Anthropic's experiments do not establish. No outbound or inbound recommendation.
- **Agent-memory systems:** GBrain's description and full review expose a concrete offline phase graph. It is a usable outbound comparison, but no return link is proposed into the frozen historical review. OpenWiki's scoped body hits concern Git-scoped documentation updates rather than transcript-based error repair; rejected as a weaker comparison.
- **Agentic systems:** Company Brain, Reflexion, WikiSkill, and archived result descriptions surfaced. Their scoped text and the collection contract preserve implementation-specific evidence boundaries. An Anthropic experiment is not evidence for those implementations. No candidate survived beyond broad mechanism overlap; no archived account or population-bound matrix should acquire an inbound citation for topical coverage.
- **Tags:** Agent-memory provides discovery routing. The ingest is not participating-collection membership, and the source contract authorizes no tag-destination label. No necessary reader path justifies an off-authorisation recommendation.
- **Sources:** Sleep and Karpathy offer the clearest comparisons: offline computation can retain different forms, and a wiki can complement rather than replace search. Other memory evaluations surfaced but would duplicate the sharper theory-boundary routes.

**Body searches:** For every destination, executed `rg -l -i 'Mt\.? Moon|dreaming|single.writer|wiki.{0,30}search|search.{0,30}wiki|transcript.{0,50}correct' kb/$d/ --glob '*.md'`. No independent Mt. Moon account surfaced. Followed with:

- `rg -n -i 'offline|nightly|dream|wiki|single.writer|ownership|transcript' kb/agentic-systems/reviews-archive/company-brain.md kb/agentic-systems/reviews-archive/reflexion.md kb/agent-memory-systems/reviews/openwiki.md` — Company Brain's `dreaming` option is not forwarded; Reflexion is online same-question reflection; OpenWiki generates repository documentation. These are not evidence that Anthropic's repair mechanism operates in those systems.
- `rg -n -i 're.examin|transformation|maintenance|testing|memory' kb/theory/agent-memory-requirements/evaluate-memory-by-effects.md kb/theory/agent-memory-requirements/promote-only-when-value-exceeds-cost.md` — effects and promotion cost are plausible, but the end-to-end note carries the more discriminating route. No promotion break-even claim is warranted by answer-time token savings.
- `rg -n -i 'dream|wiki|episode|memory' kb/tags/trace-learning-README.md kb/tags/evaluation-README.md` — confirmed trace-fed distillation and evaluation neighborhoods without treating topical relevance as index-membership authority.

**Link following:** Followed the source's episode-retention, access/transformation, and coordination links, reading each target fully. Followed the access note's end-to-end evaluation link and the agent-memory head's trace-authority and activation links, reading all three fully. Trace authority's TRACE discussion distinguishes recommendation correctness from post-edit behavior; that distinction makes the new correction case useful inbound. Fully read Sleep and Karpathy from the source-description neighborhood and GBrain from the historical-review neighborhood. No numerical search scores were produced by local `rg`.

**External:** The original Anthropic URL is already recorded in source metadata; `derived-from` is authorized but adds no new discovery. Open-web prospecting was skipped. No durable snapshot link is proposed.

## Connections Found

These are future authoring recommendations. The first three assess links already present in the ingest, not missing-edge claims.

- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) — **is-evidence-for**: retain the existing connection. The reported mistaken location note, transcript inspection, revision, and changed navigation supply a bounded case of reopening a retained claim. They do not establish transcript infallibility or a comparative advantage over rules alone.
- [Access burden and transformation burden are distinct query dimensions](../../../../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **compares-with**: retain the existing comparison on task-relative retrieval versus synthesis work. Wiki gains on cross-document judgment do not causally isolate the two burdens.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../theory/agent-orchestration-needs-coordination-guarantees-not-just.md) — **is-evidence-for**: retain the existing connection as a reported shared-write failure and bundled repair case, not proof of the isolated effect of single-writer ownership.
- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — **is-evidence-for**: add a route from the measured wiki/search outcomes to the distinction between answer-time benefit and construction/upkeep cost. The source reports task-dependent benefit and large construction budgets, but no maintenance-adjusted cost comparison or freshness test.
- [Language Models Need Sleep](../../../../sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md) — **compares-with**: compare offline computation over editable notes and wiki instructions with consolidation into slower weights. The shared sleep/dreaming vocabulary does not imply a shared update mechanism or inspection boundary.
- [LLM Wiki](../../../../sources/karpathy-llm-wiki.ingest.md) — **compares-with**: compare the manifesto's persistent compiled wiki alternative to repeated raw-document rediscovery with Anthropic's wiki-plus-search results and no-benefit cases. This bounds the replacement claim without asserting equivalent corpora or implementations.
- [GBrain](../../../../agent-memory-systems/reviews/gbrain.md) — **compares-with**: compare the operations assigned to offline maintenance. GBrain's code-grounded phase graph separates extraction, synthesis, consolidation, checking, and skill optimization; Anthropic reports selected corrections and wiki rebuilds. Readers gain a more precise decomposition of “dreaming,” not evidence that GBrain achieves Anthropic's outcomes.

## Bidirectional Candidates

Each return edge below has its own reader need; none is justified by the ingest's outbound link alone.

- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) → source — **evidenced-by**, authorized by theory → sources. The note's reader currently gets a mechanism and proposed retention comparison, but no concrete correction case. A body-level case would illustrate the narrower retained-evidence route with a reported changed next action. Say it qualifies the mechanism's scope, not that it corroborates the note's comparative cost or general reliability claims.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../theory/agent-orchestration-needs-coordination-guarantees-not-just.md) → source — **evidenced-by**, authorized by theory → sources. Its shared-mutable-memory section would gain a concrete reported loss of contract facts under shared writes. The repair changed ownership, quotation fidelity, and instructions together; the reader benefit is recognizing concurrent-loss and abstraction-loss hypotheses that require separate tests, not assigning all improvement to ownership.
- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md) → source — **evidenced-by**, authorized by theory → sources. Unlike its ARI retrieval-only example, this case reports downstream criteria coverage and answer-time tokens. It gives the reader a measured outcome comparison while making the remaining construction-cost and upkeep gaps explicit. It qualifies the evaluation boundary; it does not corroborate the entire architecture or establish net savings.
- [Language Models Need Sleep](../../../../sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md) → source — **compares-with**, authorized by sources → sources. The Sleep ingest already argues that scheduling posture does not determine retained form and compares symbolic and token-space alternatives. Anthropic adds a concrete editable-file correction and construction-instruction revision case on exactly that analytical axis. Keep this in the ingest's comparison analysis, not as a claim that the Sleep paper evaluated file memory.

## Reverse-edge Candidates

- [Trace-extracted memory earns authority per operation, not at capture](../../../../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) → source — **evidenced-by**, authorized by theory → sources. The note distinguishes capture, investigation, verification, abstraction, and consultation. Its TRACE example stops at a recommendation metric without an applied-change outcome. Anthropic's location-note repair provides a complementary reported edit-and-subsequent-action case, while Sonnet's accumulated guesses illustrate failure to reach stronger authority. This helps the note's reader distinguish witnessed stages without treating one navigation success as verified generalization or an autonomous-repair reliability estimate. Use a bounded body-level comparison, not a new origin claim for the existing theory.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Access burden and transformation burden](../../../../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) → source return edge — its reader needs evidence separating the burdens. The experiment bundles easier access and precomputed synthesis; the outbound comparison does not independently justify importing it as evidence for separability. The end-to-end note is the better inbound host.
- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) → source — some models fail to consult memory, but the prompt changes combine reading and testing and the note already has controlled exposure/uptake interventions. No additional inbound link is warranted from broad agreement alone.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) — describes shipped Commonplace state. Anthropic's results neither establish that state nor close its gaps; adding an inbound link would distract from the page's reference contract.
- [GBrain](../../../../agent-memory-systems/reviews/gbrain.md) → source — a comparison could interest a general memory survey reader, but this frozen historical account preserves its pinned implementation boundary. The outbound comparison above is sufficient; no reciprocal update is recommended.
- [OpenWiki](../../../../agent-memory-systems/reviews/openwiki.md) — shared Markdown/wiki terminology is less useful than GBrain's explicit offline operation graph. Its Git-scoped documentation updates do not supply the same correction experiment.
- [Company Brain](../../../../agentic-systems/reviews-archive/company-brain.md) and [Reflexion](../../../../agentic-systems/reviews-archive/reflexion.md) — archived, implementation-bounded accounts; unsupported dreaming options and online reflection respectively make them weak paths for interpreting the target's offline experiments. No inbound edge or matrix population change is justified.

## Index Membership

None. The sources landing is structural, not a curated experiment index. Sources are outside participating tag collections. No historical survey or commit-bound comparison should acquire this ingest as a system row.

## Synthesis Opportunities

None. The strongest apparent synthesis—offline scheduling does not determine retained form—is already explicit in the Sleep ingest. The experiment's ownership/fidelity bundle does not yet support a new causal synthesis.

## Maintenance Observations

None.

## Flags

- **Grounding prerequisite for proposed inbound uses:** the target's Quotes section is empty. Before authoring source-dependent factual claims, retain adequate exact quotes through the grounding workflow or declare full-observation checking with the exact `(snapshot required)` link-text marker. Ordinary links currently provide no retained quotes for checking the proposed experiment details. This report proposes uses, not ready-to-paste citations or completed grounding.
- **Independent-claim split signal:** the ingest connects to at least five artifacts across evidence repair, query architecture/evaluation, and coordination, and contains multiple independent experimental assertions. This meets the connect type's split-candidate signal. Preserve the single ingest as the faithful record of one external report; if new theory is authored, separate correction, task-sensitive wiki value, and ownership/fidelity claims rather than importing the whole ingest as one theoretical premise.
- The proposed inbound theory links are bounded case uses, not declarations of corroboration. The experiments did not test these Commonplace notes as independently specified refutable claims.
