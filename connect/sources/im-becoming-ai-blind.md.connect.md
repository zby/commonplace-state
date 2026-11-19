---
description: "Discovery report for possible KB connections from Rafal Cymerys's AI-blindness essay"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/im-becoming-ai-blind.md"
source_has_frontmatter: true
date: "2026-08-22"
depth: standard
---

# Connection Report: I'm becoming AI-blind

**Source:** [I'm becoming AI-blind](../../../../sources/.snapshots/im-becoming-ai-blind.md)

## Discovery Trace

**Description listing scan:**

- Read the curated heads for all five locally authorised destinations: [Notes](../../../../notes/README.md), [Reference](../../../../reference/README.md), [Sources](../../../../sources/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), and [Agentic Systems](../../../../agentic-systems/README.md). The snapshot has no `tags:` field, so no by-tag sweep was eligible; focused reads of the failure-modes, LLM-reliability, document-system, and evaluation heads supplied conceptual routing context.
- Generated every destination's complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and complete description surface with `rg -n '^description:' kb/<destination>/ --glob '*.md'`. Notes surfaced the cheap-generation, reverse-compression, reader-update, adversarial-loop, and credibility-erosion candidates. Sources surfaced the prior AI;DR, Grunewald, and Borretti ingests. Reference, agent-memory-system, and agentic-system candidates described Commonplace machinery or named systems rather than the essay's reader-adaptation claim, so none passed articulation.

**Topic indexes:**

- [Failure modes](../../../../tags/failure-modes-README.md) and [LLM reliability](../../../../tags/llm-reliability-README.md) led to the output-quality and verification-burden cluster. [Evaluation](../../../../tags/evaluation-README.md) led to the existing credibility-erosion mechanism. [Document system](../../../../tags/document-system-README.md) supplied the dual human/agent reader boundary but no direct candidate.

**Body search:**

- `rg -n -i 'AI[- ]generated|AI writing|AI-written|AI slop|AI-generated' kb/notes/ --glob '*.md'` and `rg -n -i 'reverse compression|verbose|verbosity|wordy|full of text|empty on meaning|information density|reader update' kb/notes/ --glob '*.md'` found [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md), [Reverse compression](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md), and the broader reader-update and writing-filter cluster.
- `rg -n -i 'trust|credib|disregard|ignore|attention|blindness|banner' kb/notes/ --glob '*.md'` and `rg -n -i 'credibility erosion|erode.{0,30}trust|trust.{0,30}infrastructure|discount|disregard|ignore.{0,30}(quality|signal)|false-positive cost|surface cues' kb/notes kb/sources kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'` isolated [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) and its credibility-erosion section. The link case and Cymerys's prose case share a consumer adaptation shape: repeated low-yield items cause a broad pointer class to be discounted, including better members.
- `rg -n -i 'AI[- ]generated|AI writing|AI-written|writing.is.thinking|cheap generation|reader.{0,30}verification|verification.{0,30}reader|credibility erosion|tuning out|disregard|banner blindness' kb/sources/ --glob '*.ingest.md'` found [the AI;DR discussion ingest](../../../../sources/hacker-news-ai-dr-ai-didnt-read.ingest.md) as the closest comparator. It already records effort-signal triage and false positives from AI-associated style. Cymerys adds a compact temporal self-report: repeated exposure allegedly trained an automatic suppression policy, which then causes missed content and extra coordination work.
- Searches over `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` for `AI[- ]generated|AI writing|AI-written|reader|verification burden|trust|credib|ignore|attention|blind|verbose|slop|style` produced no source-specific system or implementation connection. External prospecting was skipped as required; the already-present Medium link is evidence cited by the source, not a separately supplied target.

**Link following:**

- Followed [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) to [Reverse compression](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md), then to [observer-relative information value](../../../../notes/information-value-is-observer-relative.md) and `vibe-noting`. This kept the first two direct candidates and rejected the broader neighbors: Cymerys describes a screening policy and low-yield expansion, not a general theory of information value or durable KB artifacts.
- Followed [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) through [Agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md) and the agentic-note-taking source. This kept credibility erosion as a cross-domain comparison, while rejecting agent-navigation as too specific to pointer metadata.
- Followed the AI;DR ingest into the Grunewald, Borretti, hidden-relaxation, and adversarial-loop cluster. Those sources already carry stronger examples of reader burden, passive assent, and omitted technical constraints. Cymerys's distinct contribution is the claimed learned suppression dynamic, not another instance of the writing-is-thinking argument.

## Connections Found

- [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) -- **is-evidence-for**: Cymerys reports treating AI-marked verbosity and overstatement as evidence that inspecting the document will cost more than its sender invested in judgment; his account also shows the triage heuristic becoming automatic after repeated exposure.
- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) -- **is-evidence-for**: the three workplace examples describe simple requirements expanded into verbose prose, reasonable strategy diluted by technical gibberish, and familiar model phrasing carrying little reader-useful structure.
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) -- **compares-with**: that note's credibility-erosion section describes agents learning to discount all links after too many noisy ones; Cymerys proposes the same channel-level adaptation for humans reading AI-marked prose, including false negatives against documents that contain relevant material.
- [AI;DR (AI; Didn't Read) — Hacker News discussion](../../../../sources/hacker-news-ai-dr-ai-didnt-read.ingest.md) -- **compares-with**: the discussion already supplies multiple reports of effort-signal triage and style-based false positives; Cymerys adds one concise first-person sequence from repeated exposure, to automatic filtering, to missed information and coordination overhead.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) → source -- **evidenced-by**: the essay is a bounded naturalistic case of a reader using suspected unreviewed expansion to ration verification effort.
- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) → source -- **evidenced-by**: the essay reports several workplace artifacts whose textual expansion allegedly added little usable structure.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) -- Cymerys calls part of one deck technical gibberish and another document uncertain, but supplies neither the documents nor a constraint-by-constraint audit; the essay cannot establish hidden relaxation rather than weak writing, weak prompting, or mistaken provenance inference.
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) -- the reported documents may reflect failed human review, but the essay does not observe their production loops or distinguish unread delegation from output that was reviewed and accepted; the AI;DR and Grunewald sources already test this boundary more directly.
- [Warranted reader update is the objective of substantive writing](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) -- the complaint that text is low in meaning fits this broad objective, but the cheap-generation and reverse-compression notes explain the specific production/inspection asymmetry more precisely.
- [Agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md) -- both cases involve probabilistic follow-or-skip choices, but this note is about metadata surrounding explicit KB pointers; treating stylistic cues in prose as the same authored pointer mechanism would blur its scope.

## Index Membership

None

## Synthesis Opportunities

- [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md), [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md), and the [AI;DR discussion ingest](../../../../sources/hacker-news-ai-dr-ai-didnt-read.ingest.md) together suggest a missing general conjecture: repeated low-yield outputs can train a consumer to reject a whole cue-marked channel, reducing inspection cost while creating false negatives for better outputs. Cymerys contributes the temporal adaptation account; it does not establish prevalence, causal learning, or whether the heuristic improves total reader utility.

## Maintenance Observations

None

## Flags

- Epistemic limit: the source offers retrospective self-report and three paraphrased examples, not the documents, their provenance, counterexamples, or a measured change in attention. Treat the training account as a plausible mechanism hypothesis, not a demonstrated causal process.
- Novelty limit: artifact-level effort triage and AI-style false positives are already captured by the AI;DR ingest and cheap-generation note. The only candidate promotion worth considering is the cross-domain, repeated-exposure credibility-erosion synthesis.
