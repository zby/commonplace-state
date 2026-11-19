---
description: "Connection discovery for Ivan Vendrov's warning that generative AI can impress beyond its quality, with candidate comparisons on fluent failure, evaluation, and preference change"
type: types/connect-report.md
source: "kb/sources/.snapshots/good-reminder-that-all-of-generative-ai-is-2115720125328634247.md"
source_has_frontmatter: true
date: "2026-10-30"
depth: standard
---

# Connection Report: Thread by @IvanVendrov

**Source:** [Thread by @IvanVendrov](../../../../sources/.snapshots/good-reminder-that-all-of-generative-ai-is-2115720125328634247.md)

Discovery only. The snapshot is immutable. Outbound candidates below belong on a future matching ingest, not on the snapshot. The matching ingest is currently absent; no candidate below authorizes creating it in this run. The source link above is report-local inspection context, not a proposed durable library citation.

The thread asserts that pretraining, RLHF, and benchmark optimization can make AI seem better than it is. It separately asks whether good models should help users revise what they want rather than satisfy immediate preferences. These are practitioner judgments and questions, not controlled evidence of training effects or of the prevalence of quality misperception. The captured text does not reproduce the linked image or expand the shortened links; their contents are not inferred here.

## Discovery Trace

### Setup and indexes

- Read the entire target, the source and report collection contracts, and the connect-report type. The source contract authorizes prospecting theory, reference, agent-memory-systems, agentic-systems, tags, and sources. Instructions and work are excluded.
- Read each of those six collections' `README.md` files. Read the evaluation and LLM-reliability tag heads through the tags index. Neither head declares `complete: true`. The snapshot has no tags, so there was no source-tag membership query or complete-head skip.
- Generated fresh title recall with `rg -N --no-heading -m1 '^# ' kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources}/ --glob '*.md'`. The initial combined display was truncated. Re-ran the title surface through `rg -i 'confiden|relax.*goal|objective|faithful|routers|weakly.discrimin|sycoph|evaluation automation|trajectory-aware|gentle.coding|quality.signals|adversarial.loop'` to inspect the relevant claim titles without treating the truncated display as a complete reading.
- Scanned descriptions with `rg '^description:' kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources}/ --glob '*.md' | rg -i 'sycoph|persua|impress|fluen|goodhart|reward hack|proxy|credence|confidence|plausib|judge|evaluation.*human|human.*evaluation'`. This surfaced the fluency, confidence, objective-revision, faithfulness, and trajectory-evaluation candidates below. No semantic scores were used.

### Theory

- Ran `rg -n -i 'sycophan|adversarially optimized|out of proportion|RLHF|persuasi|impressiveness' kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources}/ --glob '*.md'`, then the focused theory query `rg -n -i 'preference|goodhart|fluent|impress' kb/theory/ --glob '*.md'` (inspected the first 70 hits).
- Fully read [hidden goal relaxation](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md), [generation confidence](../../../../theory/generation-confidence-does-not-by-itself-certify-soundness.md), [objective revision](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md), [weakly discriminated qualities](../../../../theory/weakly-discriminated-qualities-tend-to-be-underselected.md), and [the adversarial human-agent loop](../../../../theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md).
- Kept the first and third as substantive comparisons. Kept confidence as a comparison that distinguishes token probability from reader impression, not as confirmation of the thread. Rejected weak-quality underselection as a direct connection because the thread supplies no qualifying selection episodes, discrimination estimates, or propagation observations.
- One-hop following: the hidden-relaxation note led to the Borretti ingest and confidence note; the Borretti cluster led to the adversarial-loop note. The latter supplies a useful reverse-direction qualification: a human judge can still be susceptible to impressive output. Read the theory contract before evaluating that direction.

### Reference

- Read the reference README and searched descriptions as above. Ran `rg -n -i 'preference|goodhart|fluent|impress' kb/reference/ --glob '*.md'` (first 50 hits inspected).
- Fully read [trajectory-aware evaluation](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md). Kept a sparse `see-also` candidate because it offers a concrete, explicitly unadopted comparison of final appearances against process evidence. It does not test the thread's training claim.
- Read the reference contract for reverse-edge assessment. No reverse edge from the proposal is recommended: the thread supplies neither evidence of workflow violations nor the origin of that design.

### Sources

- Read the sources README, title and description surfaces, and the cross-collection body query above. Ran `rg -n -i 'human perception|human.judg.*plaus|real quality' kb/sources/ --glob '*.ingest.md'`.
- Fully read [Human Routers of Machine Words](../../../../sources/borretti-human-routers-of-machine-words.ingest.md) and [Towards Faithfully Interpretable NLP Systems](../../../../sources/towards-faithfully-interpretable-nlp-systems.ingest.md). Kept both for different comparison axes: superficial coherence versus reader verification, and perceived explanation quality versus process faithfulness.
- The Gentle-Coding research catalog appeared in descriptions and body hits. Did not promote it: it is a secondary lead map, whereas the two fully read ingests provide more specific, inspectable comparison material. No linked external studies were fetched.
- Explicit `test -f` confirmed that `kb/sources/good-reminder-that-all-of-generative-ai-is-2115720125328634247.ingest.md` does not exist.

### Agent-memory-systems

- Read its historical-survey README and generated its title surface in the combined command. Scanned descriptions, then ran `rg -n -i 'preference|reward.hack|goodhart|judge|impress' kb/agentic-systems/reviews/ kb/agent-memory-systems/ --glob '*.md'` (first 60 hits inspected).
- Also inspected the first 45 results from `rg '^description:' kb/{agent-memory-systems,agentic-systems,tags}/ --glob '*.md' | rg -i 'evaluat|epistemic|bias|reward|preference'`.
- Preference storage, model-judged promotion, and trace-learning systems appeared. None was promoted to a full candidate: the source describes no memory mechanism, artifact admission procedure, or downstream memory outcome. Merely sharing a preference or judge keyword does not earn a link. No reverse-direction hint requires a broader system-specific pass.

### Agentic-systems

- Read its README and generated its title surface in the combined command. Applied the system description and body queries recorded above.
- AI Agents in Depth, Meta-Harness, and Autocontext appeared at title/description resolution. Did not promote them: their broad evaluation and optimization surfaces do not supply a specific comparison to the thread's human-impression claim. The source contains no runtime or harness boundary against which to compare them. Archived analysis hits were not treated as current system evidence.

### Tags and external

- Read the tags README and the two topic heads noted above. Their evaluation and reliability distinctions routed the theory search, but the source collection authorizes no outbound label to tags. No missing useful tag edge was identified: topical routing is already available through the target notes, and sources are outside tag-head participating collections.
- External prospecting was skipped. The already-captured primary URL could supply `derived-from` provenance on a future ingest: `https://x.com/IvanVendrov/status/2115720125328634247`. It is not an additional discovery. No shortened URL, quoted-post context, image, or external page was fetched.

## Connections Found

These are candidate edges from a future authored ingest, not from the snapshot.

- [LLM generation can hide a relaxed goal where human writing exposes a stall](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) — **compares-with**: the thread's perceived-quality gap connects to this note because the note identifies a narrower failure in which fluent prose conceals an unmet constraint. Following the link gives a KB author a specific defect to check rather than judging whether prose is impressive. The note's relaxation mechanism is conjectural; the thread does not corroborate it.
- [Generation confidence does not by itself certify soundness](../../../../theory/generation-confidence-does-not-by-itself-certify-soundness.md) — **compares-with**: the thread's reader-impression claim connects to this note because both distinguish an attractive signal from correctness, but the note defines its signal precisely as next-token probability. Following it prevents conflating felt confidence, probability, and actual soundness, or inferring universal anti-correlation from the thread.
- [Revising an improvement objective is licensed from outside it or is not improvement](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) — **compares-with**: the thread's proposal to help users converge on what they want to want connects to this note because the note distinguishes clarifying a wider existing aim from revising a terminal objective. It gives a designer a test for whether model-induced preference change is beneficial relative to a declared criterion, rather than self-justifying because the changed user approves. This is an application question, not evidence that either kind of transition occurred.
- [Ingest: Human Routers of Machine Words](../../../../sources/borretti-human-routers-of-machine-words.ingest.md) — **compares-with**: the thread connects to Borretti's account because both warn that pleasing output can conceal poor substance. Borretti localizes the cost to a reader who must verify inferential joints after the model renders incoherent input as coherent prose; this gives the warning a concrete knowledge-writing consequence without making either polemic a training experiment.
- [Ingest: Towards Faithfully Interpretable NLP Systems](../../../../sources/towards-faithfully-interpretable-nlp-systems.ingest.md) — **compares-with**: the thread connects to the explanation-evaluation distinction because being convincing to a person is not the same as accurately representing the process behind a prediction. Following the link gives evaluators a named separation between plausibility and faithfulness. Faithfulness is narrower than general output quality; the paper does not establish that all generative AI is adversarially optimized.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — **see-also**: the thread connects to this unadopted design because an acceptable-looking final artifact can conceal process failures. The proposal specifies blinded output-only versus trajectory-aware comparison, independent audits, and judge-bias checks. It is a concrete evaluation option to investigate, not a shipped safeguard or evidence that trajectory access solves the perceived-quality gap.

## Bidirectional Candidates

None. Comparable sources do not automatically need reciprocal links, and no return path adds enough beyond the focused reverse candidate below.

## Reverse-edge Candidates

- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) → a future tracked ingest of this source — potential **see-also**, authorized by the theory contract for sources: the note relies on active human judgment rather than rubber-stamping. The thread raises a concrete limitation of that safeguard: perceived impressiveness may bias the human's acceptance too. Use the source only as a caution motivating a discrimination test, not as corroboration that human review fails. This edge is blocked until the matching ingest exists; never author it to the snapshot.

## Off-authorisation Candidates

None. No otherwise-useful candidate required an unauthorized label. In particular, no tag edge is proposed merely to record topical relevance.

## Raw Text Candidates

None.

## Rejected Candidates

- [Weakly discriminated qualities tend to be underselected](../../../../theory/weakly-discriminated-qualities-tend-to-be-underselected.md) — an obvious optimization match, but the source does not establish the note's proposal-selection conditions or compare oracle discrimination. Treating the thread as `is-evidence-for` would overstate it; the retained fluent-failure comparison is more direct.
- [Generation confidence does not by itself certify soundness](../../../../theory/generation-confidence-does-not-by-itself-certify-soundness.md), as **is-evidence-for** — rejected in this stronger role. A claim about human impression does not measure token probabilities, calibration, or soundness. The candidate survives only as the explicit comparison above.

## Index Membership

None. The snapshot is not a durable index member. Any later source tags belong on its tracked ingest and do not make sources participants in generated tag membership.

## Synthesis Opportunities

None. The selected notes already separate fluent appearance, correctness checking, and objective revision. The thread supplies no additional tested mechanism warranting a new higher-order claim.

## Maintenance Observations

- The target has no matching tracked ingest. This blocks durable source citation and the candidate reverse edge. A separately authorized ingest operation would need to establish source identity and checksum before library authoring; this discovery run does not perform it.
- The Borretti ingest's recommended next action still names `kb/notes/`, recommends snapshot links, and treats an absent synthesis as pending even though the hidden-goal-relaxation note now exists. These are stale traversal/authoring instructions under the current source contract. They were not followed or edited here.

## Flags

- Do not upgrade the thread's broad training attribution to established evidence. It supplies no model comparison, training intervention, task population, or measurement of perceived versus actual quality.
- Keep the preference-transformation discussion separate from the perceived-quality claim when consuming these candidates. The former concerns which criterion should govern change; it does not explain the latter's training mechanism.
- No split candidate: this short thread has two themes, but the retained connections do not span three independent topic areas. No snapshot edits are appropriate regardless.
