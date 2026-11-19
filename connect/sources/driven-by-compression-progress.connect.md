---
description: "Discovery candidates for the compression-progress paper, emphasizing learning value, search allocation, and observer-relative information."
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/driven-by-compression-progress.md"
source_has_frontmatter: true
date: "2026-09-18"
depth: standard
---

# Connection Report: Driven by Compression Progress

**Source:** [Driven by Compression Progress](../../../../sources/.snapshots/driven-by-compression-progress.md)

This is downstream context for the paper's ingest. The snapshot is immutable; outbound suggestions belong in its authored ingest. Reverse suggestions become eligible only after that ingest exists and supplies adequate grounding. No library edges have been authored. Discovery followed `cp-skill-connect` at standard depth using repository-local searches; no external search or semantic service was used.

## Discovery Trace

**Scope and reading.** Read the full snapshot in numbered segments, the source collection's outbound contract, the report type, the reports collection contract, and the notes collection contract for reverse edges. The source has frontmatter but no tags. Its mechanism is improvement of a bounded compressor evaluated on fixed historical data, rewarded through a controller that selects future observations. Static compressibility, raw prediction error, and task utility are distinct quantities.

**Complete title surface.** Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` once for each of `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`. Read all returned titles, paging the larger note and source listings. The listings contained 435, 162, 175, 21, and 414 nonempty lines respectively. Hidden snapshots were not a discovery surface. No scores are supplied by these lexical searches.

**Curated heads.** Read all five destination `README.md` files, plus `kb/notes/learning-theory-README.md` and its linked `kb/notes/discovery-README.md`. The latter declares `complete: true`; skipped the discovery by-tag sweep. The source has no tags requiring other matching tag scans. The heads led toward observer-relative value, search control, and memory retention rather than aesthetics or consciousness.

**Notes.** Ran `rg '^description:' kb/notes/ --glob '*.md' | rg -i 'information|epiplex|search|learn|compress|retain.*episode'`. Loaded the full observer-relative value, learning-value gates, search-allocation, search-controller evaluation, declared-objective, and episode-retention notes. Ran `rg -n -i 'observer|progress|noise|compression'` over `information-value-is-observer-relative.md`, `choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md`, and `a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md` under `kb/notes/`. Kept the four notes below because each supplies a distinct interpretation boundary. The episode-retention note makes a useful distinction, but full-history compression does not establish its selective evidence-retention claim; no direct evidence edge proposed.

**Reference.** Read its curated head and complete titles. The cross-collection description filter below surfaced mainly historical uses of “discovery”; a focused body query `rg -n -i 'compression|predict.*error|learn.*progress|curriculum' kb/reference kb/agentic-systems --glob '*.md'` found editorial compression, validation workflow, and contextual compression. These do not instantiate reward for improved historical prediction. No reference edge retained; the available `see-also` label would add a weak detour.

**Agent memory.** Read its curated head and complete titles. Ran `rg -l -i 'prediction error|intrinsic|curriculum|information gain' kb/agent-memory-systems --glob '*.md'`; results included Voyager, AgeMem, OS-Copilot, Closure-SDK, Agent-R, the comparison table, and the trace-learning overview. Read Voyager fully. Inspected matching passages in AgeMem, OS-Copilot, Closure-SDK, and Agent-R using the same pattern with `rg -n`. Voyager offers the clearest bounded comparison of active task selection and retained capability. AgeMem's mixed task/memory reward, Closure-SDK's experimental prediction-error signals, and Agent-R's future curriculum question do not establish compression-progress reward. OS-Copilot offers a second curriculum example but no additional distinction needed here.

**Agentic systems.** Read its curated head, complete titles, and `rg '^description:' kb/agentic-systems --glob '*.md'`. The focused body query shared with reference found ordinary context compression in AI Agents in Depth and trace persistence in Fractal. Broad self-improvement overlap with Exo or Prime Agent did not give a concrete compression-progress link. No candidate retained.

**Sources.** Read its head and complete titles. Ran `rg '^description:' kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' | rg -i 'compress|epiplex|intrinsic|experiment design|curriculum|discovery|search control'`. This identified epiplexity, MDA, SuperARC, the simplicity chapter, and self-revising discovery systems. Loaded the epiplexity and MDA ingests fully: the former provides the closest information-measure comparison; the latter supplies a concrete experiment-selection comparison with informative negative qualifications. Other compression hits were not promoted merely on shared terminology.

**Broad body search and noise handling.** Ran `rg -n -i 'compression progress|intrinsic reward|learning progress|curiosity' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`. Most hits were template headings. Re-ran through `rg -v 'Curiosity Pass|Curiosity Gate|curiosity gate|curiosity-gate|curiosity-prompts|curiosity experiment|broad curiosity'`, yielding a complete small result. It identified the Sutton/Javed discussion, Shannon's creative-thinking lecture, Agents Explore but Agents Ignore, and Into the Unknown. These support different senses of curiosity and were not treated as equivalent mechanisms. Truncated broad displays and combined file reads were narrowed or reread for the retained evidence; no decision relies on omitted output.

**Link following.** Followed learning-theory → discovery → observer-relative value; observer-relative value → the locally retained epiplexity ingest corresponding to its external citation; search allocation → search-controller evaluation and lightweight search control. Those full reads sharpened the distinction between inquiry routing and acceptance. Read the notes outbound rules before proposing reverse `evidenced-by` links. No reverse link to the ignored snapshot is proposed.

**External.** No external prospecting. The original arXiv URL is already in the snapshot; the ingest may use `derived-from` for that known source. Excluded `kb/work/` and `kb/instructions/` from candidate discovery as the source contract requires.

## Connections Found

- [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md) — **is-evidence-for**: sections 2.4, 2.6–2.7 and appendix A.7 make interestingness depend on the observer's current compressor and improvement capacity. This gives a formal account of one component of observer-relative value, not of goal-relative usefulness in general.
- [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — **compares-with**: both distinguish material worth learning now from mere availability or novelty. Compression progress addresses a bounded learner's remaining learnable regularity; it supplies neither source trustworthiness nor proof that retention is useful for future KB tasks.
- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md) — **compares-with**: the paper's controller chooses observations using expected future compressor improvement, while actual improvement is measured later. This is a concrete computational candidate for the note's prior allocation problem, without establishing that its intrinsic objective yields the KB's valuable downstream results.
- [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) — **is-evidence-for**: sections 1.3 and A distinguish intrinsic reward from external reward, and A.3–A.5 explicitly choose a compressor performance measure and compare old and new compressors on the same history. The paper is a formal illustration of objective-indexed improvement; it expressly assumes a helpful connection to external goals rather than establishing it universally.
- [From Entropy to Epiplexity](../../../../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md) — **compares-with**: both separate bounded-observer learnable structure from apparently random data. Compression progress measures change in the observer's coding performance and uses it to select actions; epiplexity targets structural information under computational bounds. The existing epiplexity ingest is based on a compressed summary, so this is a conceptual comparison, not an equivalence theorem or a priority claim.
- [Model Discovery Agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) — **compares-with**: both actively choose experiments to improve a model of observations. MDA uses explicit Bayesian model discrimination and tests held-out interventional forecasts; the compression-progress framework rewards improvement of a compressor. MDA's mixed acquisition ablations prevent equating information-seeking with reliable task-performance gains.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) — **compares-with**: both couple experience-responsive task selection with retained learning. Voyager conditions curriculum on completed and failed tasks and retains successful executable skills; the paper instead defines curiosity reward through compressor improvement. This comparison distinguishes adaptive curriculum and skill accumulation from an implemented compression-progress objective.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md) → the eventual tracked ingest — **evidenced-by**: add this earlier formal treatment as bounded support for pattern-learning value, while preserving the note's separate goal-relative component. Ground the precise clause in the ingest before authoring.
- [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) → the eventual tracked ingest — **evidenced-by**: the explicit separation of intrinsic and external rewards provides a compact formal case of why improvement under one objective does not imply improvement under another. This is corroboration, not invented derivation lineage.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) — retaining complete history for compression evaluation is not the same as selectively retaining the evidence needed to reopen a rule. The source does not evaluate that retention tradeoff.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — useful interpretive context reached by link following, but the paper's compression reward does not establish this note's downstream evaluation standard; the search-allocation comparison already carries the useful connection.
- [AI Agents in Depth](../../../../agentic-systems/reviews/ai-agent-book.md) — context compression and its faithfulness checks are a different mechanism from reinforcement reward for improved compression. Shared terminology is insufficient.
- [Full improvement pass closure](../../../../reference/full-improvement-pass-closure.md) — editorial compression during review does not supply the paper's objective or its before/after history-compressor comparison.

## Index Membership

None. Retain the paper as an ingest; the existing learning-theory and discovery heads already route to the theory notes it bears on.

## Synthesis Opportunities

None. Existing learning-value and search-allocation notes already own the useful distinction. A new synthesis is not needed for this ingest.

## Maintenance Observations

- The [epiplexity ingest](../../../../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md) still calls the observer-relative-value note `seedling`, although the current note carries no such status. That stale description should not affect candidate assessment.

## Flags

- Preserve the distinction between high prediction error and improvement: section 3.2 rejects raw prediction-error reward because persistent noise can attract it indefinitely.
- Appendix A.5–A.6 require old and new compressors to be evaluated on the same history. Any proposed KB analogue needs a stable comparison set; smaller prose alone does not establish the paper's kind of progress.
- The source's broad claims about aesthetics, consciousness, and human motivation are theoretical extensions with anecdotal illustrations and proposed future tests. They are not evidence that this mechanism improves a deployed KB.
- No split or note promotion proposed. The source's multiple applications remain one paper ingest; the retained connections concern its shared computational mechanism.
