---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/towards-automating-scientific-review-google-paper-assistant.md"
source_has_frontmatter: true
date: "2026-07-01"
depth: standard
---

# Connection Report: Towards Automating Scientific Review with Google's Paper Assistant Tool

**Source:** [Towards Automating Scientific Review with Google's Paper Assistant Tool](../../../sources/towards-automating-scientific-review-google-paper-assistant.md)

## Discovery Trace

**Description listing scan:**
- Read source `COLLECTION.md`; snapshots are immutable and their authored connection surface is normally the matching ingest report. Authorised durable destinations for source analyses include notes, reference, agent-memory-systems, agentic-systems, and sources; `kb/work/` and `kb/instructions/` are excluded as authored link destinations.
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/agent-memory-systems/lightweight/README.md`.
- Ran `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`; flagged notes in oracle theory, automation boundaries, bounded-context orchestration, synthesis/error correction, and process-vs-output structure. Flagged source ingests for peer-review automation, reasoning-evaluation gaps, self-refinement judging, agent reliability, multi-agent scaling, and agent harnesses.
- Ran `rg -n "description:.*(verification|automation|evaluation|oracle|review|orchestration|synthesis|agent reliability|bounded|context|human|handoff|judge|process|error)" kb/notes --glob '*.md'`; kept candidates where the PAT paper adds concrete evidence, not only shared words.
- Ran `rg -n "description:.*(peer|review|scientific|novelty|agent reliability|reason|verification|synthesis|automation|evaluation)" kb/sources --glob '*.md'`; kept existing ingests that compare to PAT as scientific-review, verification, or agent-evaluation systems.
- Ran `rg -n "description:.*(orchestration|agent|harness|review|evaluation|verification|bounded)" kb/agentic-systems kb/agent-memory-systems kb/reference --glob '*.md'`; found only weak direct matches outside sources/notes.

**Topic indexes:**
- `kb/notes/README.md` routes transferable claims to notes and points to tag READMEs. The source fits `llm-interpretation-errors`, `evaluation`, and `computational-model` more than KB-methodology foundations directly.
- `kb/agentic-systems/README.md` covers whole agentic systems, but the PAT paper is a closed/internal research-agent report without inspectable implementation. It is better handled as a source ingest, not as an agentic-system analysis.
- `kb/agent-memory-systems/README.md` covers memory and context-engineering systems. The strongest nearby system is [AutoSci](../../../../agent-memory-systems/reviews/AutoSci.md), but AutoSci is a research wiki/memory subsystem, while PAT is a review/verification agent; rejected as too indirect.

**Body search:**
- `rg -n "peer review|AI-assisted peer|automated peer|scientific review|Paper Assistant|PAT|AAAI-26|SPOT|scientific verification" kb/notes kb/sources kb/reference kb/agentic-systems kb/agent-memory-systems --glob '*.md'` -- found the new source, [Beyond "Not Novel Enough"](../../../../sources/beyond-not-novel-enough-llm-assisted-scholarly-critique.ingest.md), and [An Enigma of Artificial Reason](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md); no existing AAAI-26 snapshot.
- `rg -n "inference scaling|Pass@k|thinking tokens|segmenter|adaptive budget|synthesis agent|Deep Review|deep review|parallel thinking" kb/notes kb/sources kb/reference kb/agentic-systems kb/agent-memory-systems --glob '*.md'` -- found the PAT pipeline as a concrete bounded-call orchestration case and source-side comparisons to Pass@k/inference scaling.
- `rg -n "verification|validator|validity|error detection|boundary of automation|automation boundary|human judgment|methodological scrutiny|hallucinated critiques|reviewers" kb/notes kb/sources kb/reference kb/agentic-systems kb/agent-memory-systems --glob '*.md'` -- returned broad validation/review-system noise; kept notes where the source adds a distinct scientific-review instance.
- `rg -n "AI-assisted Peer Review|AAAI-26|Paper Assistant|automated feedback|scientific verification|STOC|ICML Experimental Program|Pangram Predicts" kb/sources --glob '*.md'` -- confirmed no prior PAT or AAAI-26 source snapshot beyond this new file and references inside it.

**Link following:**
- Read [Beyond "Not Novel Enough" ingest](../../../../sources/beyond-not-novel-enough-llm-assisted-scholarly-critique.ingest.md), then followed its note cluster: [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md), [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md), and [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md).
- Read [Towards a Science of Scaling Agent Systems ingest](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md), then followed [Synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md), [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md), [Bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md), and [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md).
- Read [Agent Harness survey ingest](../../../../sources/agent-harness-large-language-model-agents-survey.ingest.md) and [Agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) to test whether PAT belongs as a harness/runtime example. Kept this as a comparison, not a primary note edge, because the source reports one closed pipeline rather than a general runtime taxonomy.

## Connections Found

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **evidence**: PAT is a concrete scientific-review case where the authors explicitly keep publication control with humans while automating verification-heavy support work; the four-role taxonomy maps directly onto the automation-boundary claim.
- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- **evidence**: PAT's Role 1/2/3/4 ladder separates author/reviewer augmentation from supporting-reviewer and total-automation roles, with hallucinated critiques, accountability, and final human responsibility as the discriminators.
- [Bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md) -- **evidence**: PAT implements an explicit scheduler over bounded LLM calls: segment manuscript, allocate compute per segment, run deep review agents, then synthesize with grounding and deduplication.
- [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) -- **evidence**: PAT's segmenter chooses logical paper regions and adaptive budgets so deep review calls spend their context on high-complexity sections rather than the whole paper.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) -- **evidence**: the paper's critique of naive Pass@k names the same gap: independent calls improve recall but degrade precision unless the aggregation layer provides grounding, deduplication, and severity checking.
- [Synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) -- **evidence**: PAT's design discussion supplies a real review-agent example where repeated generations create a precision burden and the synthesis step needs extra grounding rather than being treated as verification by itself.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- **evidence**: the source separates AI generation from scientific validation and reports a review agent optimized for detecting proof/logical errors, not for producing new results.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- **evidence**: PAT's performance claim rests on process structure (segmentation, budget allocation, deep review, global synthesis) rather than only a more structured final report format.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **evidence**: the SPOT case uses retraction/erratum-backed errors plus a logic-aware grader and human audit, showing an attempt to harden the oracle for scientific error detection before trusting the agent's review output.
- [Beyond "Not Novel Enough" ingest](../../../../sources/beyond-not-novel-enough-llm-assisted-scholarly-critique.ingest.md) -- **compares-with**: both sources automate parts of scientific peer review through structured LLM pipelines, but PAT targets full-paper error detection/pre-submission critique while the earlier source targets novelty assessment through related-work deltas.
- [Towards a Science of AI Agent Reliability ingest](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) -- **compares-with**: PAT reports a deployed-style agent pilot but does not measure consistency, robustness, predictability, or safety; the reliability source supplies the evaluation vocabulary PAT would need before moving from augmentation to automation.
- [Towards a Science of Scaling Agent Systems ingest](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) -- **compares-with**: PAT's segmentation and synthesis pipeline is a specialized multi-call architecture whose design choices should be read against measured decomposition/coordination/verification tradeoffs.
- [Agent Harness for Large Language Model Agents ingest](../../../../sources/agent-harness-large-language-model-agents-survey.ingest.md) -- **compares-with**: PAT is a domain-specific harness instance with scheduler, context allocation, execution/search substrate, synthesis, and evaluation roles, while the survey provides the general component vocabulary.
- [An Enigma of Artificial Reason ingest](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) -- **compares-with**: VAIR warns that solving and evaluating reasoning are separable; PAT's value claim depends on the review agent genuinely evaluating proofs rather than reconstructing plausible conclusions.
- [Autoreason ingest](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md) -- **compares-with**: both sources use extra inference and adjudication structure to improve critique, but Autoreason centers blind comparative judging and incumbent survival while PAT centers section-level review plus synthesis/grounding.

## Bidirectional Candidates

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) <-> source -- **evidence**: a future note update could cite PAT's Role 1-4 taxonomy as a scientific-review domain instance where verification cost and accountability determine how far automation may go.
- [Bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md) <-> source -- **evidence**: a future update could use PAT as a closed-system example of `select(K) -> call(P) -> K+r` in a scientific-review pipeline.

## Reverse-edge Candidates

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -> source -- **evidence**: PAT provides source evidence that AI review is positioned as automation only where verification and accountability can be maintained.
- [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) -> source -- **evidence**: PAT's logical segmentation and adaptive compute budgeting are a concrete heuristic example for decomposing long semantic review tasks.
- [Synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) -> source -- **evidence**: PAT's Pass@k discussion is a source-side statement that repeated independent critiques increase human verification burden unless aggregation adds grounding/deduplication.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [AutoSci](../../../../agent-memory-systems/reviews/AutoSci.md) -- rejected: both concern scientific research tooling, but AutoSci's reviewed surface is a research wiki/memory subsystem, while PAT is a closed review/verification agent. The connection is topical rather than a useful `compares-with` edge for an ingest report.
- [Commonplace REVIEW-SYSTEM](../../../reference/REVIEW-SYSTEM.md) -- rejected: both use "review", but PAT reviews scientific manuscripts and proofs, while the Commonplace review system reviews KB artifacts under local semantic gates. The source may inspire future review design, but a direct source link to current system reference would confuse domains.
- [Semantic Engine](../../../../agentic-systems/reviews/semantic-engine.md) -- rejected: both touch source ingestion/exploration, but Semantic Engine is an ingest workbench and explicitly not an agent runtime; PAT's central contribution is review-agent orchestration.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) -- rejected: both are multi-loop agent systems, but GBrain is memory/dream-cycle/self-modification infrastructure; PAT is an application-specific scientific review tool without inspectable runtime code.

## Index Membership

- `kb/sources/` peer-review automation cluster -- this source should be read beside [Beyond "Not Novel Enough"](../../../../sources/beyond-not-novel-enough-llm-assisted-scholarly-critique.ingest.md) when evaluating AI assistance in scholarly review.
- `kb/notes/llm-interpretation-errors-README.md` -- if that curated head grows a scientific-review subsection, this source would be evidence for the verification/automation boundary and reasoning-evaluation distinction.

## Synthesis Opportunities

- PAT plus [Beyond "Not Novel Enough"](../../../../sources/beyond-not-novel-enough-llm-assisted-scholarly-critique.ingest.md) imply a stronger synthesis: AI peer-review systems are most credible when they narrow the review task to a verifiable subrole (novelty deltas, proof/error detection, evidence retrieval) instead of imitating the whole reviewer role.
- PAT plus [Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) and [Autoreason](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md) suggest a reusable critique-pipeline pattern: decompose critique work into bounded units, run redundant or specialized checks, and keep the final aggregation layer as a verified/adjudicated selection step rather than an unconstrained synthesis.

## Maintenance Observations

- The source cites "AI-Assisted Peer Review at Scale: The AAAI-26 AI Review Pilot" but no durable snapshot was found for that paper. This is only a future source-acquisition signal; no action was taken during connect.
- The new source snapshot used `capture: pdf-read` while retaining the user-provided arXiv HTML URL as `source` and the PDF URL in the body. This is acceptable for the current schema, but future snapshot tooling might want a separate `fetched_from` field when HTML URLs are captured through linked PDFs.

## Flags

- Closed/internal system: PAT's implementation and Gemini variants are not inspectable from the snapshot, so pipeline architecture claims should be treated as paper-reported evidence rather than code-grounded system evidence.
- No direct agentic-system review target: the paper is a source for theory and comparison, not enough to write a `kb/agentic-systems/` analysis without more implementation detail.
