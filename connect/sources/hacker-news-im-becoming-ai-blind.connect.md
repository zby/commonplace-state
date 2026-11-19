---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/hacker-news-im-becoming-ai-blind.md"
source_has_frontmatter: true
date: "2026-08-22"
depth: standard
---

# Connection Report: I'm becoming AI-blind — Hacker News discussion

**Source:** [I'm becoming AI-blind — Hacker News discussion](../../../../sources/.snapshots/hacker-news-im-becoming-ai-blind.md)

## Discovery Trace

**Source and contract read:**

- Read the complete 435-comment snapshot, `kb/sources/COLLECTION.md`, and `kb/cache/types/connect-report.md`. The source is a conversation thread with many independent anecdotes and arguments, not a single-author thesis. The sources contract makes the future ingest report, rather than the immutable snapshot, the authored outbound surface.

**Curated heads and complete title surfaces:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for notes, reference, agent-memory-systems, agentic-systems, and sources. The notes and sources title surfaces exposed an existing AI-writing cluster. The agent-memory and agentic-system collections had no plausible system-review target: the thread mentions models and harness tactics incidentally but does not analyze a memory system or agent runtime as a system. Those destinations were skipped after the curated-head and title pass.

**Description listing scan:**

- Ran `rg '^description:' kb/notes --glob '*.md'`. Strong candidates were `reverse-compression-is-when-llm-output-expands-without-adding.md`, `warranted-reader-update-is-the-objective-of-substantive-writing.md`, `generation-confidence-does-not-by-itself-certify-soundness.md`, `generality-bought-to-avoid-counterexamples-is-paid-for-in.md`, and `human-llm-differences-are-load-bearing-for-knowledge-system-design.md`.
- Ran `rg -n -i '^description:.*(writing|prose|text|reader|information|slop|meaning|communication|documentation|simplif|concise|verbosity|jargon|intent|human)' kb/sources --glob '*.md'`. This found the original Cymerys essay ingest, the earlier AI;DR Hacker News ingest, Grunewald's substantive-writing critique, Borretti's writing-is-thinking critique, and the trendslop article.
- Ran `rg -n -i '^description:.*(writing|text|reader|prose|plain|specific|clarity|human|LLM|artifact)' kb/reference --glob '*.md'`. Reference hits described Commonplace's own presentation and publication surfaces rather than a claim this thread materially bears on, so no reference target passed the articulation test.

**Body search:**

- `rg -n -i 'information[- ]dens|information[- ]sparse|verbosity|verbose|plain language|simple writing|jargon|grandiose|slop|reader update|intended reader|dual-audience|human-LLM|writing styles|substantive writing' kb/notes --glob '*.md'` — kept reverse compression, warranted reader update, and the generality/precision note; rejected human–LLM differences because its claim concerns dual-audience KB design, while this source concerns humans reading generated prose.
- `rg -n -i 'AI;DR|reverse.compression|information density|AI[- ]generated (text|writing)|writing failure|trendslop|make your code simpler|putting ideas into words|learning by writing' kb/sources --glob '*.ingest.md'` — kept the original essay, AI;DR, Grunewald, Borretti, and trendslop comparisons; rejected broader writing-process sources whose only overlap was that writing can support thinking.
- `rg -n -i 'low-yield|channel-wide|cue-marked|AI-blind|AI;DR|effort signal|reader burden|pseudo-language|slippery|unmemorable|information[- ]sparse|invented jargon|grandiose|rhetorical miscalibration|draft-state leakage|domain contamination' kb/notes kb/sources --glob '*.md'` — confirmed that the exposure-dependent channel-rejection conjecture remains recommended by the original essay ingest but has not yet been promoted into a note.

**Link following:**

- Followed the original essay ingest to reverse compression, cheap-generation effort signaling, the earlier AI;DR ingest, and the credibility-erosion section of `quality-signals-for-kb-evaluation.md`.
- Followed the AI;DR ingest to maintenance-capacity, hidden-constraint relaxation, the adversarial-loop note, and Grunewald's ingest. This established that the new thread overlaps the reader-burden cluster but contributes substantially more language-level and cognition-level failure descriptions.
- Followed reverse compression to observer-relative information value and vibe-noting. Kept reverse compression because commenters repeatedly describe expanding a small payload into prose the reader must recompress; rejected information value as a separate edge because reverse compression already carries that premise.
- Followed `generality-bought-to-avoid-counterexamples-is-paid-for-in.md` to generation confidence and reverse compression. The source's invented jargon, excessive abstraction, hedging, and polished pseudo-technical prose directly instantiate the note's readability-as-content-failure mechanism.
- Followed Grunewald and Borretti to the bare-writing-prompt, hidden-relaxation, and adversarial-loop notes. Kept hidden relaxation; rejected the bare-prompt note because the thread rarely supplies the prompts that produced the complained-about documents, and rejected the adversarial-loop note because proposed fixes are anecdotal and do not show that review reconstructed the missing filter.

## Connections Found

- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) — **is-evidence-for**: many commenters independently describe tiny informational payloads expanded into long prose that readers must recompress, with closer reading sometimes revealing less rather than more structure.
- [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) — **is-evidence-for**: workplace readers report treating obvious one-shot prose, excessive length, and unchanged model voice as signals that the sender invested less judgment than verification will cost; false-positive and high-quality-output counterexamples bound the inference.
- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) — **is-evidence-for**: reports of polished pseudo-language, missing critical components, explanations that name a problem and declare it solved, inability to backtrack, and plans whose high-level context must be reconstructed all locate verification work that the fluent surface conceals.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — **is-evidence-for**: multiple technical-writing reports describe invented terminology, abstract synonyms, defensive hedging, and grandiose language that look rigorous while making mechanisms and consequences harder to recover.
- [Warranted reader update is the objective of substantive writing](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) — **is-evidence-for**: the thread supplies naturalistic cases of polished filler, arbitrary comparison dimensions, generic topical treatment, and prose made “interesting” without an interesting idea, all of which fail to produce a discriminating reader update.
- [Generation confidence does not by itself certify soundness](../../../../notes/generation-confidence-does-not-by-itself-certify-soundness.md) — **is-evidence-for**: commenters repeatedly distinguish smooth, grammatically polished, plausible presentation from truth, valid reasoning, or the presence of load-bearing details; their anecdotes illustrate the distinction but do not measure model confidence or error rates.
- [Maintenance capacity must match harmful-artifact inflow](../../../../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) — **is-evidence-for**: reports of AI-authored methodology documents, proposals, code comments, and PR descriptions becoming review queues, context pollution, and inputs that recipients reprocess through another model instantiate harmful retained-artifact inflow without establishing prevalence.
- [I'm becoming AI-blind](../../../../sources/im-becoming-ai-blind.ingest.md) — **compares-with**: the essay supplies four first-person examples and a repeated-exposure hypothesis; the discussion broadens the candidate failure inventory, adds counterexamples, and separates surface detection from reader response.
- [AI;DR (AI; Didn't Read) — Hacker News discussion](../../../../sources/hacker-news-ai-dr-ai-didnt-read.ingest.md) — **compares-with**: both threads report reader burden and effort-based triage, while this thread adds dense accounts of pseudo-language, loss of voice, invented jargon, maximalism, unmemorability, arbitrary structure, and cognition-level effects.
- [Why You Should Almost Never Use AI to Write Anything Substantive](../../../../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) — **compares-with**: Grunewald offers a domain-expert audit and explicit delegation boundary for several failures that appear here only as heterogeneous anecdotes.
- [Human Routers of Machine Words](../../../../sources/borretti-human-routers-of-machine-words.ingest.md) — **compares-with**: Borretti gives the writing-as-thinking and shifted-verification-cost mechanism behind many reports here, while the thread supplies counterexamples and practical prompting or editing mitigations absent from the polemic.
- [Researchers Asked LLMs for Strategic Advice. They Got “Trendslop” in Return](../../../../sources/researchers-asked-llms-strategic-advice-trendslop.ingest.md) — **compares-with**: its reported fashionable-discourse prior is a narrower empirical cousin of the thread's complaints about bland averages, corporate/LinkedIn/Quora voice, and context-insensitive high-valence prose.

## Bidirectional Candidates

- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) ↔ future ingest — note-side **evidenced-by**: the thread supplies a large, self-selected field corpus for the reader-side recompression burden, bounded as anecdotal rather than prevalence evidence.
- [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) ↔ future ingest — note-side **evidenced-by**: the thread independently repeats the effort-signal behavior and supplies false-positive, survivorship-bias, and high-quality-generation caveats.
- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) ↔ future ingest — note-side **evidenced-by**: several first-person technical cases describe a polished surface concealing the exact missing mechanism or context the reader must reconstruct.

## Reverse-edge Candidates

- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) → future ingest — **evidenced-by**: the source offers recurring examples of unreadable abstraction, invented nomenclature, and hedged verbosity as symptoms of missing content, while also showing that not every jargon complaint has the same cause.
- [Maintenance capacity must match harmful-artifact inflow](../../../../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) → future ingest — **evidenced-by**: workplace reports add a human-review and cognitive-debt path alongside the note's existing recursive agent-context path.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Human–LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — rejected: the thread richly describes human response to LLM prose but does not compare the needs of human and LLM readers of one KB artifact, which is the target note's claim.
- [Minimum viable vocabulary is the naming set that most reduces extraction cost for a bounded observer](../../../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) — rejected: invented jargon in the thread is the failure of naming without a useful distinction; the source does not investigate the productive naming mechanism or vocabulary-selection problem.
- [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) — rejected: arbitrary comparison dimensions and lack of synthesis resemble missing orientation, but the note's claim is specifically about curated versus generated KB indexes.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) — rejected: comments speculate about RLHF preference for impressive language and vendor incentives for verbosity, but supply no candidate-selection comparison or enrichment evidence.
- [A bare writing prompt does not determine its intended contribution](../../../../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) — rejected: one-shot and low-effort documents are discussed, but the producing prompts and commissions are generally absent, so the thread cannot distinguish prompt underspecification from generator, activation, or review failure.
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) — rejected: commenters propose style prompts, manual editing, model switching, and re-querying, but do not compare whether those loops recover the constraints and contribution lost during generation.

## Index Membership

None.

## Synthesis Opportunities

- The thread, the original essay, and the earlier AI;DR discussion together suggest a failure-mode map with at least four separable layers: content and epistemic failures (missing mechanisms, plausible error, silent constraint loss, poor relevance selection); discourse failures (reverse compression, repetition, maximalism, hedging, invented jargon, stock structure, false personalization, loss of voice); reader effects (re-derivation burden, poor skimmability, low memorability, fatigue, automatic rejection, false positives); and social/operational failures (author non-understanding, missing accountability, review debt, context pollution, and shifted coordination cost). A durable note would need to explain why the layers require different checks, not merely catalogue stylistic tells.
- The original essay's proposed `Repeated low-yield outputs can train consumers to reject a cue-marked channel` conjecture now has a second large discussion containing both matching self-reports and boundary cases. The pair can motivate a discriminating test of exposure-dependent suppression versus static effort triage, generic overload, and survivorship bias; neither thread supplies prevalence or causal evidence.
- The source repeatedly separates polished prose from a useful contribution. Combined with reverse compression, hidden constraint relaxation, and defensive abstraction, it suggests a higher-order claim: an anti-slop style guide can remove visible model tells while leaving the substantive failure untouched, so AI-writing review must test contribution, constraint satisfaction, and reader extraction cost separately from style.

## Maintenance Observations

None.

## Flags

- Split candidate: the thread makes more than one independent assertion and connects to at least seven notes across epistemic soundness, document quality, reader cognition, and maintenance. The ingest should preserve one source identity but organize its failure modes into distinct mechanisms rather than flattening them into “AI style.”
- Evidence-strength flag: 435 comments provide breadth of reported modes and counterexamples, not 435 independent observations. Participation is self-selected, identities and anecdotes are unverified, branches are dependent, and comment ranking shapes visibility. Use the source to enumerate hypotheses and boundaries, not estimate frequency or prove causes.
