---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/how-to-organise-a-project-s-knowledge-for-a-2113681318852600222.ingest.md"
source_has_frontmatter: true
date: "2026-10-24"
depth: standard
---

# Connection Report: Ingest: How to organise a project's knowledge for AI coding agent and an engineer

**Source:** [Ingest: How to organise a project's knowledge for AI coding agent and an engineer](../../../../sources/how-to-organise-a-project-s-knowledge-for-a-2113681318852600222.ingest.md)

The ingest already carries a dense inline connection surface (commitment-not-derivation, lineage-at-source, link-graph staleness, criteria/process edits, insufficient summary, index recall, checked-or-absent, changing requirements, tentative theory, epistemic stance, freshness architecture, Build Systems à la Carte conference ingest, Karpathy LLM wiki, sage-wiki). All of those paths resolve. This report proposes only additional edges and reverse edges.

## Discovery Trace

**Setup:**
- Source collection `sources`; read `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, sources, external. Excluded: `kb/work/`, `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external; sparingly).
- Verified that every link already in the ingest resolves.
- External: the source URL is already in frontmatter; no other external target in context. External prospecting skipped.

**Description listing scan:**
- Theory titles: `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` filtered with `rg -i 'stale|fresh|deriv|lineage|summar|index|progressive|citation|cite|ground|verbatim|quote|chunk|raw|compil|wiki|rebuild|regenerat|propagat|supersed|spec|always-loaded|load|retriev|provenance|hallucin|gate|check|faith|distill|span'`. Flagged and read descriptions for: keep-compiled-views-aligned, artifact-classification-separates-content-kind-lineage-and-authority, definitions/lineage, a-citation-cannot-assert-more-fidelity-than-its-capture-preserved, superseded-choices-are-retained-superseded-beliefs-are-not, derivation-and-inheritance-give-starting-warrant-earns-scope, error-correction-works-above-chance-oracles-with-decorrelated-checks, design-rationale-must-preserve-unregenerable-decision-premises, evolving-understanding-needs-holistic-rewrite-not-composition, preserve-evidence-without-loading-history, pointer-design-tradeoffs-in-progressive-disclosure, a-retrieval-miss-is-a-local-reflective-path-failure, stale-self-description-conceals-its-own-staleness, git-provenance-requires-contribution-and-dependency-semantics, thresholding-monotone-transforms-does-not-add-an-independent-check, always-loaded-context-mechanisms-in-agent-harnesses, raw-accumulation-does-not-create-usable-memory, llm-recompute-cost-inverts-the-store-vs-recompute-default, localized-retention-pays-where-change-is-sparse-in-a-matching, a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.
- Agent-memory-systems / agentic-systems: `rg -l -i 'content hash|source hash|hash.*(rebuild|regenerat|stale)|recompil|re-derive|dependents|wiki' agent-memory-systems/ agentic-systems/`; read descriptions of llm-project-wiki, Kompl, memwiki, secure-llm-wiki, llm-wiki, LLM-Wiki-v3, engraph, atomic, eidetic, echowiki, kenhuangus--llm-wiki, cobusgreyling--llm-wiki, MehmetGoekce--llm-wiki, llm-context-base, llm-wiki-coordination. Then `rg -n -i 'hash|stale|re-?compil|regenerat|rebuild|cascade|dependen|source change|non-?determin|early cutoff'` over the top five.
- Sources: `rg -l -i 'llm wiki|compiled wiki|raw/|facts.*artifacts|regenerat.*on source change|staleness|rebuild' sources/ --glob '*.ingest.md'`; read descriptions of OpenWiki self-correcting memory, Karpathy LLM knowledge bases, in-toto, PROV overview, Build Systems à la Carte (extended JFP), Flywheel.

**Topic indexes:**
- `kb/tags/COLLECTION.md`: `sources` is not a participating collection, so the ingest takes no tag membership. kb-maintenance and claims-and-grounding heads are `complete: true`; by-tag rg skipped (not applicable to a sources artifact anyway).

**Body search:**
- `rg -l -i 'early cutoff' theory reference agentic-systems` -- zero hits. The KB has no theory statement of early cutoff; it appears only in the build-systems ingests.
- `rg -l -i 'same meaning|semantic equivalen'` -- hits in proposals and archived analyses only; none bear on rebuild cutoff. Rejected.
- `rg -l -i 'per-stage|each stage|stage gate'` -- scenario-decomposition, evaluation-automation-is-phase-gated; neither is about per-write gating. Rejected.
- `rg -l -i 'verbatim'` -- a-citation-cannot-assert-more-fidelity-than-its-capture-preserved (kept), a-note-is-an-atomic-step-relative-to-the-check-that-reads-it (kept).
- `rg -l -i 'statement-level|claim-level citation|every (claim|statement) cites'` -- zero hits.
- `rg -l -i 'hallucination snowball|ClashEval|Planfence'` -- zero hits; relayed papers are not ingested anywhere.
- `rg -n 'production relation selects|selects the maintenance'` -- superseded-choices note line 48 states that the production relation selects the maintenance operation (relevant to the ingest's proposed synthesis; see Flags).

**Link following:**
- OpenWiki ingest already links lineage-at-source, localized-retention, keep-compiled-views-aligned and freshness-architecture: the same cluster the target joins, with a stale-marking response rather than auto-rewrite.
- Build Systems JFP ingest links criteria/process edits, checked-or-absent, llm-recompute-cost, link-graph staleness and the Eigenius review (memo key omitting definition version). Eigenius was followed and rejected as a direct target; the JFP ingest already carries that edge.
- keep-compiled-views-aligned links always-loaded-context-mechanisms and Synapptic; Synapptic not followed further (render targets, not source-change propagation).
- Theory COLLECTION outbound: theory may link `kb/sources/` with `evidenced-by` (corroborates, qualifies or bounds; corroboration requires a risked test). Used for reverse-edge candidates.

## Connections Found

- [Build Systems à la Carte: Theory and Practice (extended JFP ingest)](../../../../sources/build-systems-a-la-carte-theory-and-practice.ingest.md) -- **compares-with**: on rebuilder correctness for impure tasks. The target ingest already maps the design to verifying traces via the conference version, but the extended version supplies the two limits its analysis leans on: §7.3 adds rule and script versions to cache keys (the exact fix for the source's prompt/slicing-change gap) and §8.3–8.4 treat non-deterministic tasks, where exact recheck fails. An LLM rewrite is non-deterministic, and the source's "means the same" cutoff is a probabilistic stand-in for set-membership equality. Stronger fit than the conference ingest already linked.
- [OpenWiki self-correcting memory ingest](../../../../sources/building-self-correcting-memory-in-openwiki-2092280107033616451.ingest.md) -- **compares-with**: on the response to an input-version change. OpenWiki marks the dependent claim stale and asks the agent to re-verify or revise; this source rewrites dependents automatically. Same lineage shape (claim-level dependency, version or hash trigger), opposite repair policy. It is the stale-marking pole the ingest's Extractable Value 2 names only through sage-wiki.
- [Keep lineage and compiled views from drifting](../../../../theory/agent-memory-requirements/keep-compiled-views-aligned.md) -- **compares-with**: on source-of-truth rules for derived surfaces. The note requires compiled views to carry source hash and regeneration rules and to "regenerate or be marked stale"; the source picks regenerate for every artifact and has no path for direct edits to flow back. Specs are the case where the note's rule that behaviour-changing views need stricter governance is violated.
- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../theory/superseded-choices-are-retained-superseded-beliefs-are-not.md) -- **compares-with**: on what survives regeneration of decision content. The ingest's spec misfiling (Extractable Value 3) is exactly a choice event overwritten by an automatic rewrite, leaving version control as the only witness. The note also already says the production relation selects the maintenance operation, which the ingest's Recommended Next Action must account for.
- [Design rationale must preserve decision premises its interpreter cannot regenerate](../../../../theory/design-rationale-must-preserve-unregenerable-decision-premises.md) -- **compares-with**: on the retention test for spec content. The note's test (keep what is not recoverable from implementation, git and general knowledge; treat the rest as cache) is the criterion that would move specs out of the rewrite walk while leaving summaries and views in it.
- [A citation cannot assert more fidelity than its capture preserved](../../../../theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) -- **compares-with**: on citation fidelity. The source's fact unit keeps the verbatim span beside the rewrite, so every artifact citation sits on a verbatim layer; the ingest's own relayed figures (Extractable Value 7) sit on the second-hand layer the note says no gate can promote. Gives the ingest a precise term for both observations.
- [A note is an atomic step relative to the check that reads it](../../../../theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) -- **compares-with**: on check granularity. Guardrail 2 is one model call checking that a page says nothing beyond its linked facts; the note bounds an artifact by what one checker pass can verify. Same per-artifact grounding check, sized differently (page plus linked facts vs. note plus unquoted sources).
- [Error correction works with above-chance oracles and decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **compares-with**: on oracle reliability. Guardrail 2 and the same-meaning classifier are single LLM oracles; the note says their value depends on TPR > FPR and decorrelation. Grounds the ingest's Limitations point that both are fallible model judgments, and frames the false-"same" failure as an oracle error that silently halts propagation.
- [LLM recompute cost shifts the store-vs-recompute balance](../../../../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) -- **compares-with**: on materialization economics. The source materializes every derived page and pays rewrite cost eagerly on source change; the early cutoff is its cost control. The note supplies the cost frame for when that eager store-and-rewrite policy pays.
- [Lineage (definition)](../../../../theory/definitions/lineage.md) -- **defined-in**: the ingest uses "lineage mechanics" and "lineage regime" without defining lineage; the definition fixes it as source dependencies needed to invalidate, regenerate, retire or review retained artifacts.
- [LLM-Wiki-v3 review](../../../../agent-memory-systems/reviews/LLM-Wiki-v3.md) -- **compares-with**: on the admission path for source-derived pages. Both content-address raw sources by hash and check span provenance, but LLM-Wiki-v3 routes extraction into `pending/` for human review, while this source admits pages after a model check and rewrites them without review.

## Bidirectional Candidates

- [OpenWiki self-correcting memory ingest](../../../../sources/building-self-correcting-memory-in-openwiki-2092280107033616451.ingest.md) <-> source -- **compares-with**: OpenWiki's ingest analyses claim-granular stale marking; a return link to this source gives it the auto-rewrite contrast on the same axis (sources -> sources `compares-with` is authorised).
- [Build Systems à la Carte: Theory and Practice (extended JFP ingest)](../../../../sources/build-systems-a-la-carte-theory-and-practice.ingest.md) <-> source -- **compares-with**: the JFP ingest classifies workflow engines into rebuilder cells; this source is a natural-language KB instance of verifying traces with probabilistic early cutoff, which that ingest has no example of.

## Reverse-edge Candidates

Theory -> sources uses `evidenced-by` under `kb/theory/COLLECTION.md`. The source reports no outcomes, and the ingest's analysis was built through these notes, so none of these is corroboration; context phrases should say "qualifies" or "bounds".

- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -> source -- **evidenced-by**: a complete practitioner design for the derivation side, plus a worked misfiling (specs under auto-rewrite) the note's boundary predicts. Qualifies the note with a concrete case; not a risked test.
- [Link graph plus timestamps enables make-like staleness detection](../../../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) -> source -- **evidenced-by**: bounds the note with a variant keyed on content hash, with rewrite rather than re-read and a same-meaning early cutoff that answers the note's false-positive section.
- [Source changes should surface downstream review targets](../../../../theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) -> source -- **evidenced-by**: practitioner instance of artifact-side links with a script-derived reverse map, which removes the human review the note recommends. Qualifies the note's worklist step.
- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../../../../theory/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) -> source -- **evidenced-by**: a deployed-style design whose rebuild key omits process edits (prompts, slicing), illustrating the failure the note names. Qualifies; no observed failure is reported.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Eigenius review](../../../../agentic-systems/reviews/eigenius.md) -- memo key omits the component-definition version, the same gap as the source's missing prompt version; rejected because the JFP build-systems ingest already carries this edge and is the better hop.
- [Secure LLM-Wiki review](../../../../agent-memory-systems/reviews/secure-llm-wiki.md) -- has source-content hashes and per-claim write gates, but the review finds no stale invalidation; it shares only the gate idea, which LLM-Wiki-v3 covers better.
- [LLM Wiki (nvk) review](../../../../agent-memory-systems/reviews/llm-wiki.md) -- derived `_index.md` caches rebuilt when stale; only index regeneration, not dependent-page rewrite. Too generic.
- [Kompl review](../../../../agent-memory-systems/reviews/Kompl.md) -- content hashes and compile status per source, but contradiction triage logs without rewriting; weaker than OpenWiki as a contrast.
- [Artifact classification separates content kind, lineage, and authority](../../../../theory/artifact-classification-separates-content-kind-lineage-and-authority.md) -- relevant to the raw/facts/artifacts split, but superseded-choices and design-rationale make the spec point more precisely; would add a third link for one observation.
- [Evolving understanding needs holistic rewrite](../../../../theory/evolving-understanding-needs-holistic-rewrite-not-composition.md) -- views are rewritten whole, but the note concerns consumer-side reconciliation of fragments, not source-triggered rebuild. Keyword overlap.
- [Always-loaded context mechanisms in agent harnesses](../../../../theory/always-loaded-context-mechanisms-in-agent-harnesses.md) -- the root index in the always-loaded file and the relayed Vercel result touch it, but only as a second-hand pointer; wait until the Vercel post is ingested.
- [Pointer design tradeoffs in progressive disclosure](../../../../theory/pointer-design-tradeoffs-in-progressive-disclosure.md) -- the source's retrieval is fixed-pointer progressive disclosure, but the ingest's retrieval claims are already carried by the insufficient-summary and index-recall links.
- [Karpathy LLM knowledge bases ingest](../../../../sources/llm-knowledge-bases-something-i-m-finding-very-useful.ingest.md) -- duplicates the already-linked Karpathy LLM wiki contrast.
- [in-toto](../../../../sources/in-toto-farm-to-table-guarantees.ingest.md), [PROV overview](../../../../sources/prov-overview.ingest.md) -- whole-chain provenance standards; no mechanism the ingest uses.

## Index Membership

None. `sources` does not participate in tags (`kb/tags/COLLECTION.md`).

## Synthesis Opportunities

The ingest's proposed note (the response to an input change is selected by the artifact's lineage regime) now has more poles in the KB: auto-rewrite with semantic cutoff (this source), stale-marking with agent reconciliation ([OpenWiki ingest](../../../../sources/building-self-correcting-memory-in-openwiki-2092280107033616451.ingest.md)), pending human review ([LLM-Wiki-v3](../../../../agent-memory-systems/reviews/LLM-Wiki-v3.md)), enforce-or-omit ([checked or absent](../../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md)), and witness-preserving supersession ([superseded choices](../../../../theory/superseded-choices-are-retained-superseded-beliefs-are-not.md)). [Commitment, not derivation](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) supplies the boundary. See Flags for overlap with the superseded-choices note.

## Maintenance Observations

- No theory note states early cutoff (`rg 'early cutoff'` over theory, reference and agentic-systems returns nothing), although two build-systems ingests and this ingest rely on it. Semantic early cutoff for natural-language rebuilds is a repeated unnamed mechanism and a candidate for the link-graph staleness note.
- Relayed papers (Planfence, Hallucination Snowball, ClashEval, He et al., Filesystem-Based Memory) have no ingests; several relayed figures bear on freshness and gating notes.

## Flags

- Tension with the ingest's claim that "no current note states this selection rule": [superseded choices](../../../../theory/superseded-choices-are-retained-superseded-beliefs-are-not.md) line 48 already says the production relation selects the maintenance operation (refresh vs. supersession). The proposed note would extend this to auto-rewrite, stale-marking, review and enforce-or-omit; a writer should check it against that note and commitment-not-derivation for duplication before writing.
- The ingest makes several independent assertions across freshness, epistemics, citation fidelity and retrieval and connects to more than five notes; as an ingest this is expected and not a split candidate.
