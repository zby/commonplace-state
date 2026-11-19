---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/from-single-to-multi-llm-hallucination-mds.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: From Single to Multi: How LLMs Hallucinate in Multi-Document Summarization

**Source:** [Ingest: From Single to Multi](../../../../sources/from-single-to-multi-llm-hallucination-mds.ingest.md)

The source already carries nine footer links: derived-from (external), four is-evidence-for links to theory (out-of-spec, soft degradation, reverse compression, decomposition heuristics), and four compares-with links to sources (Peters and Chin-Yee, Paulsen, GSM-DC, LongMemEval). This report covers only new candidates. All existing link targets resolve.

## Discovery Trace

**Authorization (kb/sources/COLLECTION.md, Outbound links):** the destinations to prospect are theory, reference, agent-memory-systems, agentic-systems, tags and sources. `kb/work/` and `kb/instructions/` are excluded. The labels for theory are is-evidence-for, abstracted-from, rests-on, compares-with, defined-in and see-also. Sources may use compares-with and see-also; agent-memory-systems may use is-evidence-for, compares-with and see-also; agentic-systems may use compares-with and see-also; reference may use only see-also. The `external` destination is used only by the existing derived-from link. External prospecting was skipped.

**Topic indexes:**
- `kb/tags/llm-reliability-README.md`, which matches the source's `tags:`. Its taxonomy section led to `llm-output-deviation-requires-three-way-diagnosis`. Its aggregation section led to `synthesis-is-not-error-correction`. The out-of-spec note is already linked.
- I listed the sections of `kb/tags/evaluation-README.md` (oracles and judges; experiment and benchmark design). That led to `an-experiment-identifies-only-the-contrast-it-actually-runs`.

**Title listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'summar|degrad|context|absent|abstain|confidence|synthesis|merge|interpreter|out-of-spec|spec|deviation|evaluation|metric|measure|benchmark|position|recency|distract|relevance|expan|compress|oracle|verification|insufficient|label|judge'` found these candidates:
  - synthesis-is-not-error-correction: kept
  - llm-output-deviation-requires-three-way-diagnosis: kept
  - an-experiment-identifies-only-the-contrast-it-actually-runs: kept
  - generation-confidence-does-not-by-itself-certify-soundness: rejected
  - automated-synthesis-is-missing-good-oracles: rejected
  - position-and-proportion-set-what-a-reader-retains: rejected
  - llm-debugging-starts-with-retry-versus-rewrite-triage: rejected because the three-way diagnosis note covers it
  - semantic-sub-goals-that-exceed-one-context-window-become-scheduling: rejected
  - an-insufficient-summary-precedes-the-source-rather-than-replacing: rejected
- `ls kb/sources | rg -i 'claim-verification|webagents|hallucin|summar|lost-in|position|recency|abstain|validity|generaliz|judge|distract|context-rot|needle|long-context'` found these candidates:
  - assessing-llm-reasoning-evidence-based-claim-verification: kept
  - llm-webagents-long-context-reasoning-benchmark: kept
  - llm-validity-plausibility-conflation-content-effects: rejected; see Synthesis Opportunities
  - position-bias: rejected
  - tombros-sanderson-query-biased-summaries: rejected
  - coding-agents-are-effective-long-context-processors: rejected
  - the-y-combinator-for-llms-solving-long-context-rot: rejected

**Body search** (over kb/theory, kb/reference, kb/agentic-systems, kb/agent-memory-systems and kb/sources, excluding work):
- `rg -l -i "abstain|abstention"` matched about 25 files. Relevant hits:
  - generation-confidence: its line 26 says confidence can trigger abstention. The MDS paper measures no confidence, so I rejected it.
  - an-insufficient-summary: its line 50 puts abstention risk out of scope, so I rejected it.
  - assessing-llm-reasoning (RECV): its response-policy and forced-verdict analysis made it a kept candidate.
  - longmemeval: already linked.
- `rg -l -i "hallucinat"` hits included:
  - out-of-spec and Paulsen: already linked.
  - llm-output-deviation-requires-three-way-diagnosis: kept.
  - traditional-software-can-bracket-executor-conformance: foundational and too indirect.
  - agent-memory reviews (deja-vu, origin, wuphf and others): these mention hallucination generically. None treats multi-document aggregation, so I rejected them.
- `rg -l -i "multi-document|summari[sz]ation"` mostly hit memory-system reviews whose "summarization" means session compaction. None tests cross-document overlap, so I rejected them.
- `rg -l -i "fabricat"` hits were system reports and unrelated sources. No theory note distinguishes fabrication from condition violation.
- `rg -l -i "instruction.follow|instruction inconsisten|condition.*enforce"` hits were:
  - a-goal-holding-interpreter-fails-soft: rejected; it concerns re-routing around blocked steps, not output conditions.
  - context-contamination-operates-below-an-agents-compliance-reasoning: adjacent but already reached through the three-way diagnosis note.
  - an-experiment-identifies-only-the-contrast-it-actually-runs: kept.
- `rg -l -i "LLM-as-judge|LLM judge|judge model"` hits were:
  - error-correction-works-above-chance-oracles: generic.
  - lifecycle-llm-judge-recommendation-explanations: a Netflix judge case. The source's gpt-4o-mini judge is a measurement detail, not its contribution, so I rejected it.
- `rg -l -i 'shared across|cross-document|multiple documents|consolidat' kb/agentic-systems/reviews kb/agent-memory-systems/reviews` returned 123 files. These are generic memory-consolidation mentions. No single review tests or designs for shared-across-sources selection, so I skipped agent-memory-systems and agentic-systems.

**Link following:**
- I read the existing source links in `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md`. It cites Paulsen, GSM-DC, llm-webagents, ConvexBench and J-space. llm-webagents is the one with objective loss under added irrelevant history, which this source does not yet compare against.
- I read the existing source links in `out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md`. Its position-bias paragraph (line 23) refuses to classify order flips as interpreter failure without a judging-contract premise. This source has that premise: an explicit "mentioned in at least two documents" condition. That makes the reverse edge below unusually clean.
- I read the opening of `synthesis-is-not-error-correction.md`, which defines synthesis as union-like merging and voting as minority-discarding selection.
- I read the opening of `llm-output-deviation-requires-three-way-diagnosis.md` (I/V/D model and remedy non-substitution).
- I read `decomposition-heuristics-for-bounded-context-scheduling.md` lines 43-57. It is already linked; I checked that the "separate selection from joint reasoning" fit holds.
- Inbound check: `rg -l 'from-single-to-multi' kb --glob '*.md'` finds no inbound links outside `kb/work/`.

## Connections Found

- [Synthesis is not error correction](../../../../theory/synthesis-is-not-error-correction.md) -- **compares-with**: the axis is union-like merging versus selection by agreement. The shared-only prompt asks for an intersection: keep only insights at least two documents support, which is structurally a support-count filter like voting. Models instead output a union, passing single-document content off as shared (58.54%-67.24% of news errors at N = 2). The paper is single-model summarization, not multi-agent aggregation, so this is a comparison, not evidence for the note's Kim/MAKER claim.
- [LLM output deviation requires three-way diagnosis](../../../../theory/llm-output-deviation-requires-three-way-diagnosis.md) -- **is-evidence-for**: the paper's single "hallucination rate" bundles three things the note keeps apart. Unshared bullets under an explicit sharedness condition are out-of-V output. Pedantic bullets from a format with no target count are arguably admissible under V. Temperature-1 single-sample generation leaves dispersion unmeasured. Weak, illustrative support: a pooled deviation rate cannot by itself choose a repair surface.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **is-evidence-for**: a worked case of contrasts that were not run. The shared-only setting tests thin overlap, never zero overlap. The absence probe removes the topic, not the overlap. The recommended per-document-then-merge pipeline is untested. Mechanism hypotheses such as recency and count mismatch go unmanipulated. A reader citing this paper for "absent shared information" needs exactly this rule.
- [Assessing LLM reasoning in evidence-based claim verification (RECV)](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md) -- **compares-with**: the axis is the response policy for unsupported answers. RECV removes the abstain option, so warranted abstention can appear as reasoning error. This paper offers an explicit "No insights found" option, and models still decline it 29%-79% of the time on absent subtopics, more often as N grows. Together they show that a missing abstention option and an offered-but-unused one are separate failure surfaces.
- [LLM web agents long-context reasoning benchmark](../../../../sources/llm-webagents-long-context-reasoning-benchmark.ingest.md) -- **compares-with**: the axis is which quantity degrades as non-target input grows. In the web-agent benchmark, injected irrelevant history causes loops and loss of the original objective. Here, added documents lower recall and abstention while output error share stays flat. This sharpens the ingest's Extractable Value item 5 (degradation splits into separately moving quantities) with an agent-level case, beside the existing Paulsen and GSM-DC comparisons.

## Bidirectional Candidates

- [Assessing LLM reasoning in evidence-based claim verification (RECV)](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md) <-> source -- **compares-with**: the RECV ingest's item 4 proposes an `INSUFFICIENT EVIDENCE` ablation. This paper is a measured case of what happens when such an option exists, which informs how to design that ablation.

## Reverse-edge Candidates

These are edges authored under `kb/theory/COLLECTION.md` rules, where `evidenced-by` may point into sources. Each context phrase must say whether the evidence corroborates, qualifies or bounds the claim. None of the theory notes was built from this source.

- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) → source -- **evidenced-by**: the strongest reverse edge. The note excludes position-bias flips because no judging contract fixes V. This paper supplies an explicit prompt condition ("only insights mentioned in at least two documents"). The measured violations, unshared content presented as shared, are therefore classifiable as out-of-V. The context phrase should say the evidence bounds the claim: author-coded, news-only, N = 2, with fabrication rare. It does not corroborate the claim in the Popperian sense.
- [Soft degradation can bind before the hard cap even when required evidence fits](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) → source -- **evidenced-by** (qualifies): recall and abstention fall from 2 to 10 short documents, well inside the window, while output error share stays near-flat. The note's interference paragraph could cite it as a case where degradation shows up as lost coverage rather than rising error.
- [Reverse compression is when LLM output expands without adding information](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) → source -- **evidenced-by** (qualifies): the human-coded "pedantic" class (subtopic paraphrases, generic openers, takeaway closers) is an instance. Classifying it as reverse compression is local analysis, as with the SuperARC footer already in that note.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Generation confidence does not by itself certify soundness](../../../../theory/generation-confidence-does-not-by-itself-certify-soundness.md) -- it discusses abstention triggered by calibrated confidence. The paper measures abstention behaviour but no confidence signal, so this is a keyword match only.
- [Automated synthesis is missing good oracles](../../../../theory/automated-synthesis-is-missing-good-oracles.md) -- the weak post-hoc filters look superficially relevant. However, the note concerns evaluating cross-note insight candidates, not summary-faithfulness filtering, and the paper's filters are LLM classifiers at N = 2 only.
- [Opening position can signal a human reader's theme](../../../../theory/position-and-proportion-set-what-a-reader-retains.md) -- the note concerns how human and LLM readers take in authored text. The paper's position effects concern the model's own output and input order, which is a different axis.
- [An insufficient summary precedes the source rather than replacing it](../../../../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) -- it explicitly puts abstention risk without a fallback out of scope.
- [Mazur position-bias benchmark](../../../../sources/position-bias.ingest.md) -- the shared word "position" covers judge order sensitivity there and output-bullet position here. These are not a shared axis.
- [LLM validity-plausibility conflation](../../../../sources/llm-validity-plausibility-conflation-content-effects.ingest.md) -- a direct compares-with would rest on an untested analogy (content salience overriding a formal condition). It is routed to Synthesis Opportunities instead.
- [Query-biased summaries (Tombros and Sanderson)](../../../../sources/tombros-sanderson-query-biased-summaries.ingest.md) -- this is a human study of search-result snippets. Query-focused summarization is shared only at the genre level.
- Agent-memory-systems and agentic-systems reviews -- the 123 consolidation-related hits are generic. No review makes a cross-source support-count or abstention design decision this paper would inform.

## Index Membership

- [LLM reliability tag head](../../../../tags/llm-reliability-README.md) -- its `## Sources` section lists Ma et al. as evidence separating deviation sources. This paper could join as measured evidence that "hallucination" rates mostly count condition violations rather than fabrication. Sources do not participate in tag membership, so this would be an editorial addition under `kb/tags/COLLECTION.md` rules, not required membership.

## Synthesis Opportunities

Three sources ingested for the same workshop occasion may imply one higher-order claim:
- this paper (unshared single-document insights presented as shared, despite an explicit condition)
- [Peters and Chin-Yee](../../../../sources/peters-chin-yee-llm-generalization-bias.ingest.md) (scope qualifiers dropped in summaries; accuracy prompts worsen it)
- [validity-plausibility conflation](../../../../sources/llm-validity-plausibility-conflation-content-effects.ingest.md) (validity verdicts track conclusion plausibility)

The candidate claim: a formal or relational condition on content (sharedness, scope, validity) is under-enforced when the content itself is plausible and salient, and naming the condition in the prompt does not reliably close the gap. Only the third source offers a mechanism, and only for syllogisms. This belongs to the epistemic-relevance workshop's synthesis, not to connect.

## Maintenance Observations

- `kb/sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md` recommends writing a note "A forced verdict can turn warranted abstention into apparent reasoning failure" in `kb/notes/`. No `kb/notes/` collection appears in the routing table in AGENTS.md; the destination would be `kb/theory/`. That note, if written, would be a natural target for this source as well (offered-but-unused abstention as the contrasting case).
- The source and its two sibling ingests (Peters and Chin-Yee; validity-plausibility) were untracked at the time of this run. Their mutual compares-with edges assume all three get committed.

## Flags

- Tension to keep visible, not resolve: this source's near-flat output error share with document count sits beside Paulsen's rising hallucination and GSM-DC's power-law error growth. Any reverse edge from the soft-degradation note should name the quantity measured, as the ingest already warns.
- No split candidate: the ingest makes one coherent measurement contribution.
