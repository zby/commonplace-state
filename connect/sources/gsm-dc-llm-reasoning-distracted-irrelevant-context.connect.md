---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: How Is LLM Reasoning Distracted by Irrelevant Context? (GSM-DC benchmark)

**Source:** [GSM-DC ingest](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md)

The ingest already carries a dense Connections Found section (soft degradation, process/output levers, unscoped context, Gonen, Lampinen, context contamination, ConvexBench, Paulsen, web-agents, J-space, fixed decomposition, theory builder). This report lists only candidates the ingest does not yet carry, plus the reverse and return edges that its existing edges imply.

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, sources, external. Excluded: `kb/work/`, `kb/instructions/`. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). External prospecting skipped (no open-web search); the arXiv URL is already in the `source` field.

**Tag head:** read `kb/tags/context-engineering-README.md` (not `complete: true`). Core Claims list surfaced `context-efficiency-is-the-central-design-concern-in-agent-systems.md` (rejected, see below); no other head entry engages irrelevant-context interference.

**Inbound check:**
- `rg -l 'gsm-dc-llm-reasoning' kb --glob '*.md'` -- inbound from soft-degradation, process-structure, Gonen ingest, web-agents ingest, and two `kb/work/` files. Not inbound from `llm-context-is-composed-without-scoping.md` (cites arXiv URL only), Lampinen, ConvexBench, Paulsen, or J-space ingests.
- `rg -n 'gsm|GSM|distractor|irrelevant context'` over the ingest's existing targets -- confirmed llm-context note line 36 and line 60 use `https://arxiv.org/html/2505.18761v2`; web-agents ingest line 54 links the arXiv URL under an ingest-style slug.

**Titles listing:** `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'context|scop|degrad|decompos|isolat|attention|sub-?agent|noise|relevan|filter|retriev|verif|experiment|benchmark|depth|chain|interfer|contamin|window|load'` -- flagged: an-experiment-identifies-only-the-contrast-it-actually-runs, decomposition-heuristics-for-bounded-context-scheduling, specification-level-separation-recovers-scoping, flat-memory-predicts-specific-cross-contamination-failures, session-history-should-not-be-the-default-next-context, rule-based-context-selection-needs-a-pre-existing-signal, knowledge-access-architecture-must-be-evaluated-end-to-end, topology-isolation-and-verification-form-a-causal-chain, context-efficiency-is-the-central-design-concern.

**Body search:**
- `rg -n -i 'distract|irrelevant (context|material|token)|interference|dose|power.law|process reward|PRM\b|verifier' kb/theory kb/agentic-systems kb/agent-memory-systems --glob '*.md' -l` -- ~60 files; filtered to error-correction-works-above-chance-oracles (metamorphic "irrelevant context addition" check, line 73), an-experiment-identifies-only-the-contrast (Irrelevant controls, line 38), knowledge-storage-does-not-imply-contextual-activation (mentions interference only via soft-degradation link), session-history (line 31, irrelevant history).
- `rg -n -i 'distract|irrelevant|GSM|convexbench|paulsen|webagent'` per flagged theory note -- decomposition-heuristics cites ConvexBench focused-context arm (lines 63-65, 84) but not GSM-DC; topology-isolation cites ConvexBench only.
- `rg -l -i 'distract|irrelevant context|context rot|lost in the middle|process reward|PRM' kb/sources --glob '*.ingest.md'` -- 26 hits; evaluated self-evolvers, HART, CEDAR-GRPO, VAIR (an-enigma), Gick-Holyoak, induction-bias.
- `rg -l -i 'irrelevant context|distractor' kb/agentic-systems kb/agent-memory-systems kb/reference --glob '*.md'` -- agemem lightweight review and one retained fragility-grid report; neither engages controlled distractor dose.

**Link following:**
- From Gonen ingest (lines 40, 72, 80): confirms the GSM-DC/Gonen/Lampinen triad and the shared "no scoping baseline" limitation; nothing new.
- From web-agents ingest (lines 47-90): proposes a synthesis "irrelevant-context degradation is consistent across abstraction levels"; see Flags.
- From HART ingest line 30: HART already pairs the fixed-decomposition note with an-experiment-identifies-only-the-contrast, the same pair GSM-DC's Learning Claims need.
- From VAIR ingest lines 22, 46: PRMs degrade on valid-answer-invalid-reasoning cases.
- `rg -o '\.\./sources/[^)]+\.ingest\.md'` on reverse-edge targets to check ADR 082 unquoted-source bounds: llm-context note 0 ingests; an-experiment 4; error-correction 1; decomposition-heuristics 0 (ConvexBench cited by URL).

## Connections Found

- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **rests-on**: the ingest's central limitation (every arm keeps distractors in one flat prompt, so "most effective intervention" ranks only within-decomposition remedies and says nothing about training versus exclusion) is an application of this note's missing-comparison rule. Linking it lets the Limitations and Learning Claims sections cite the rule instead of re-deriving it, as HART's ingest already does.
- [Error correction works above-chance oracles with decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **is-evidence-for**: GSM-DC is a controlled instance of the note's "metamorphic check" under irrelevant context addition: the correct answer is invariant to distractor injection by construction, and invariance violations rise with dose and depth. It shows the transformation has signal on six models; it does not measure TPR/FPR of the check as an oracle, which the context phrase should say.
- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) -- **compares-with** on clean-frame versus flat-frame evidence: the note grounds "exploit clean frames recursively" in ConvexBench's focused-context arm; GSM-DC supplies the flat-frame side only (interference compounding with dependency depth) with no clean-frame arm. The comparison tells a reader that GSM-DC motivates the heuristic's precondition (deeper tasks are more interference-sensitive) without testing the remedy.
- [VAIR: an enigma of artificial reason](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) -- **compares-with** on process-reward-model reliability: GSM-DC's PRM search gains up to 6.29% OOD step accuracy, but the ingest notes it is unreported whether the PRM discriminates distractor use. VAIR's appendix reports PRMs degrading on valid-answer-invalid-reasoning cases, which names a concrete failure the GSM-DC PRM was not tested against.
- [LLM agents are not always faithful self-evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) -- **compares-with** on what irrelevant content does to behavior: there, irrelevant condensed experience barely moves performance (it is ignored), while GSM-DC's format-matched distractors steer computation. The contrast sharpens GSM-DC's "inert, templated distractors" limitation: surface-form match with relevant content may be what makes irrelevant material operative. Moderate value; keep the axis explicit or drop.

## Bidirectional Candidates

- [Language models, like humans, show content effects on reasoning](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) <-> source -- **compares-with**: GSM-DC already compares with Lampinen on the "kind of unlicensed content" axis; Lampinen's ingest has no return edge, so a reader starting there misses the inert-noise end and the divergent training response (hard-distractor training helps here; instruction tuning leaves content effects unchanged there).
- [ConvexBench](../../../../sources/convexbench-can-llms-recognize-convex-functions.ingest.md) <-> source -- **compares-with**: return edge on depth versus distractor count; ConvexBench's reader benefits from knowing GSM-DC is the flat-only, distractor-varying counterpart that lacks the focused-context arm.
- [Paulsen's maximum effective context window](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md) <-> source -- **compares-with**: return edge on volume versus interference; low priority.

## Reverse-edge Candidates

- [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) → source -- **evidenced-by** (theory label): the note cites GSM-DC only by arXiv URL (lines 36, 60). Under the theory contract, edges to sources point to the tracked ingest. The note currently links zero ingests, so one unquoted ingest link stays within the ADR 082 bound. This file has uncommitted working-tree edits; coordinate with that work.
- [LLM web-agents long-context benchmark](../../../../sources/llm-webagents-long-context-reasoning-benchmark.ingest.md) → source -- **compares-with**: line 54 points an ingest-style slug at the arXiv URL and uses the unauthorised label `complements`; it should link this ingest with a source-to-source label.
- [Error correction works above-chance oracles with decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) → source -- **evidenced-by**: the "metamorphic checks" bullet could cite GSM-DC as a case where irrelevant-context addition breaks invariance. The phrase must say it qualifies (shows signal) rather than corroborates TPR > FPR.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) → source -- **evidenced-by** (illustration of a missing comparison): low priority. The note already links 4 ingests; a fifth unquoted one reaches the ADR 082 limit of five, so the link would need a retained quote via `cp-skill-ground` or should be skipped.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Context efficiency is the central design concern](../../../../theory/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- reaches GSM-DC's relevance only through soft-degradation, which the ingest already links; a direct edge adds a hop, not content.
- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) -- mentions irrelevant-context interference only via its soft-degradation link; GSM-DC tests interference, not activation.
- [Session history should not be the default next context](../../../../theory/session-history-should-not-be-the-default-next-context.md) -- its irrelevant-history claim is better evidenced by the web-agents benchmark (agent histories) than by templated math.
- [Topology, isolation, and verification form a causal chain](../../../../theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) -- isolation evidence there comes from ConvexBench's framework; GSM-DC has no isolation arm.
- [Rule-based context selection needs a pre-existing signal](../../../../theory/rule-based-context-selection-needs-a-pre-existing-signal.md), [specification-level separation recovers scoping](../../../../theory/specification-level-separation-recovers-scoping-before-it-recovers.md), [flat memory predicts cross-contamination failures](../../../../theory/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) -- title-level matches on scoping/contamination; none makes a claim GSM-DC's data bears on.
- [CEDAR-GRPO](../../../../sources/cedar-grpo-process-aware-rl-abductive-reasoning.ingest.md), [HART](../../../../sources/hart-high-resolution-annotation-free-reasoning-technique.ingest.md) -- process-reward and evidence-selection training, but neither shares a named axis with GSM-DC tighter than VAIR does.
- [Gick-Holyoak](../../../../sources/gick-holyoak-analogical-problem-solving.ingest.md) -- human distractor load in analogy retrieval; different construct.

## Index Membership

- [Context engineering tag head](../../../../tags/context-engineering-README.md) -- sources are outside participating collections; no head entry needed. The ingest's existing `tags: [context-engineering]` is consistent with the head's scoping/degradation scope.

## Synthesis Opportunities

The web-agents ingest recommends a note "Irrelevant-context degradation is consistent across abstraction levels" (GSM-DC, ConvexBench, web-agents), arguing for a fundamental attention-architecture property. The GSM-DC and Gonen ingests now argue the opposite caution: divergent training responses across GSM-DC, Gonen and Lampinen count against assuming one mechanism. A synthesis would have to be scoped to the shared enabling condition (flat, unscoped context) rather than a shared mechanism; [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) already carries that scoped version. No new note appears warranted until a cross-paradigm comparison exists.

## Maintenance Observations

- `kb/sources/llm-webagents-long-context-reasoning-benchmark.ingest.md` line 54 links GSM-DC through the external arXiv URL under the label `complements`, which is not in the sources label set; line 47 shows a stale display slug (`agent-context-is-constrained-by-soft-degradation-not-hard-token-limits`) for the renamed soft-degradation note.
- `kb/theory/llm-context-is-composed-without-scoping.md` cites three tracked sources (GSM-DC, Gonen, Lampinen) only by external URL although ingests exist for all three; the theory contract says source edges point to the tracked ingest.
- An earlier connect report for this source existed at this path and was overwritten by this run.

## Flags

- Tension: the web-agents ingest's synthesis claim ("fundamental attention-architecture property") conflicts with the GSM-DC and Gonen ingests' explicit refusal to infer a shared mechanism. Flagged, not resolved.
- The ingest's Recommended Next Action (check Figure 6 for the Δ direction before trusting "IC affects arithmetic execution") also bears on [process structure and output structure are independent levers](../../../../theory/process-structure-and-output-structure-are-independent-levers.md) line 22, which states "the reported SAcc/PAcc gap shows that arithmetic can fail even when path selection succeeds" without that caveat.
