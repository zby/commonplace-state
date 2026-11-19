---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/futrell-levy-gibson-dependency-locality.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Dependency Locality as an Explanatory Principle for Word Order

**Source:** [Dependency Locality as an Explanatory Principle for Word Order](../../../../sources/.snapshots/futrell-levy-gibson-dependency-locality.md)

The source is an immutable snapshot. Every outbound candidate below is meant for its authored surface, the future `kb/sources/futrell-levy-gibson-dependency-locality.ingest.md`, which did not exist when this report was written. None of these edges should be authored on the snapshot.

**What the source says (for the reader of this report):** Futrell, Levy and Gibson (Language 96(2), 2020) use Universal Dependencies corpora to test dependency-length minimization (DLM), the idea that words joined by a head–dependent relation sit close together in linear order. Their results: (1) observed dependency length is shorter than random-reordering baselines that impose independently motivated constraints (projectivity, consistent head direction, fixed word order). (2) A fitted probabilistic linearization model separates grammar from usage. Observed sentences are shorter than random grammatical reorderings, which shows DLM in usage, and grammatical reorderings are shorter than the baselines, which shows DLM in grammar. (3) Dependency length varies across languages and is longer in head-final languages, which the authors leave as an open explanandum. The functional motivation the paper reviews is that working-memory representations decay and suffer interference over distance (Gibson's dependency locality theory). The paper also reviews a statistical-complexity (excess-entropy) motivation and an extension called information locality: elements that predict each other are under pressure to be close. The authors bound the claim. DLM is a pressure, not a rule for every utterance. The narrowest reading is "whatever constraints exist reduce dependency length beyond these baselines", and the paper does not exclude unexplored alternative factors.

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, section *Outbound links*. Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags and sources. Excluded: `kb/work/` and `kb/instructions/`. `external` is authorised only for `derived-from` and `see-also`. Labels per destination: theory gets `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with` and `see-also`, plus `defined-in` for theory/definitions. Reference gets only `see-also`. Sources gets `compares-with` and `see-also`. Agent-memory-systems gets `is-evidence-for`, `compares-with` and `see-also`. Agentic-systems gets `compares-with` and `see-also`. Outbound links come from the ingest, never from the snapshot.

**External:** No external target was supplied, and none is in loaded context beyond the source's own URL. External prospecting was skipped as the skill requires. The ingest's `derived-from` edge to `https://socsci.uci.edu/~rfutrell/papers/futrell2020dependency.pdf` is structural and belongs to the ingest author.

**Source read:** Frontmatter, §1 Introduction, §2.2 What is dependency locality, the start of §2.3, the start of §2.4, §4 baselines with §4.1 and §4.3 discussion, §5 grammar and usage, §5.3, §6 and the start of §6.1, and §7 conclusion with §7.1–7.3. Section headings for the whole file were listed with `grep -nE '^[0-9]+(\.[0-9]+)*\. [A-Z]'`. The data-processing details in §3, the appendix tables and the references were skimmed through that heading list only.

**Curated heads:**
- `kb/tags/document-system-README.md`, read in part (description, Foundations, Writing Conventions). Writing Conventions holds only the claim-title note. Foundations points to `human-llm-differences-are-load-bearing-for-knowledge-system-design.md`, which was kept as a context candidate.
- `kb/tags/evaluation-README.md`, top sections read. These confirmed that experiment-design notes are housed there. The snapshot has no `tags:`, so no tag-based by-tag rg was run.
- `kb/sources/README.md`: no editorial groupings, only conventions.

**Full titles listing (theory):**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` returned 427 titles. It was filtered with `rg -i 'writ|prose|sentence|read|order|position|placement|near|close|distance|proximit|adjacen|lost|attention|middle|condition|caveat|scope|qualif|efficien|compress|locality|surprise|predict|linear|sequence'`. Flagged: `human-writing-structures-transfer-to-llms-because-failure-modes.md`, `writing-styles-are-strategies-for-managing-underspecification.md`, `link-strength-is-encoded-in-position-and-prose.md` and `evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md`.

**Description listing scan:**
- `rg -N --no-heading '^description:' kb/theory --glob '*.md' | rg -i 'simpl|plain|controlled language|ste100|sentence|readab|prose|parse|syntax'` surfaced `evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md` (kept), `evidence/three-simplification-passes-exposed-different-tradeoffs.md` (rejected, see below) and `generality-bought-to-avoid-counterexamples-is-paid-for-in.md` (rejected: it concerns vocabulary generality, not syntax distance).
- `rg -N --no-heading '^description:' kb/theory --glob '*.md' | rg -i 'baseline|null model|control|confound|random'` found nothing about null baselines. Control hits were about agent control loops.
- `rg -N --no-heading '^description:' kb/sources --glob '*.ingest.md' | rg -i 'language|linguist|writing|prose|readab|efficien|communicat|information theory|zipf'`. Nothing on psycholinguistics or word order. `fodor-pylyshyn-1988-...ingest.md` and `when-is-it-better-to-think-without-words.ingest.md` were checked and rejected as off-axis.

**Body search (excluding `kb/work/`, `kb/instructions/`, `kb/reports/` and snapshots):**
- `rg -l -i -e 'Futrell|Gibson|dependency locality|dependency length|Behaghel' kb` found `sources/sutskevers-list/chapters/11-appendix-design-patterns-for-engineers.md`, which has the sentence "Architectures that minimize dependency length ... win" in the neural path-length sense. It also found `sources/sutskevers-list/full.md`, which repeats that sentence, and `sources/gavel-graph-world-models.ingest.md`, a false hit on "OmniGibson".
- `rg -l -i 'surprisal|information locality|lossy-context'` matched `theory/epiplexity-by-example-what-entropy-and-complexity-miss.md` (surprisal in the information-theory sense) and several agent-memory reviews that use "surprisal" as a salience score. All were rejected.
- `rg -l -i 'center-embed|garden.path|psycholinguist|sentence processing|reading time'` found only `theory/text-testing-framework.md`, which lists reading time as a metric. Rejected.
- `rg -l -i 'working memory'` found many agent-memory and agentic-system reviews, but all use "working memory" for agent scratch state, not human retrieval decay. Rejected as keyword-only.
- `rg -n -i 'next to (its|their|the)|beside the claim|close to the claim|near the claim|adjacent|attachment' kb/theory kb/reference kb/types` found no theory note that states or grounds the AGENTS.md rule "Keep necessary conditions next to their claims". See Maintenance Observations.
- `rg -l -i 'lost in the middle|positional bias|position bias|recency bias'` found `sources/position-bias.ingest.md` and `sources/paulsen-maximum-effective-context-window-mecw.ingest.md`, both checked and rejected (see below).
- `rg -n -i 'path length|shorter path|revers(al|ed|ing) (trick|the source|input)|dependency length|short paths' kb/sources --glob '*.ingest.md'` found `sources/05-attention-is-all-you-need.ingest.md`, whose finding "Path length explains temporary hacks" was kept.
- `rg -n -i 'excess entropy|statistical complexity|Crutchfield|Shalizi'` returned no hits outside snapshots.
- `rg -l -i 'word order|dependency length|linguist' kb/agent-memory-systems kb/agentic-systems` returned only incidental "linguistic" hits in a comparison table and retained run results. Nothing on word order.

**Link following:**
- `theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md` links to `frontloading-spares-execution-context.md`, `claim-notes-should-use-toulmin-derived-sections-for-structured.md`, `short-composable-notes-maximize-combinatorial-discovery.md` and the excluded instruction `asd-ste100-inspired-rewrite.md`. None adds a distance or locality mechanism, so none was promoted.
- `theory/human-writing-structures-transfer-to-llms-because-failure-modes.md` links to the Toulmin cluster, `structured-output-is-easier-for-humans-to-review.md` and `why-notes-have-types.md`. These are not about syntax-level conventions, so none was promoted.
- `sources/05-attention-is-all-you-need.ingest.md` links to `theory/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md` and `theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`. Both concern architecture, not reader-side processing cost. Not promoted (see Flags).

**Destinations skipped:**
- agent-memory-systems and agentic-systems: the source has no claim about agent memory or harness design, and every body hit was keyword-only.
- theory/definitions: the ingest needs no registered KB term.
- tags: the ingest-report type does not take tag membership from connect. The tag heads were read for routing only.

## Connections Found

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **is-evidence-for**: the note's first rewrite failed by moving a temporal qualifier away from the definition it limited and detaching an appositive. Its inference is that sentence syntax carries attachment relations. The paper supplies large-scale human-language evidence that dependents are kept close to their heads in both grammar and usage. It also supplies a working-memory mechanism that makes long head–dependent distance costly, which explains why the guarded rewrite restated relations at each point of use. The link should say that the evidence is about human production and comprehension. The paper does not show that the same distance cost applies to LLM readers.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **see-also**: that note's method is to take each convention's specific human-side rationale and check whether LLMs share the failure. The paper gives that rationale for one sentence-level convention, keeping linked elements and qualifiers adjacent: retrieval degrades with distance through decay and interference. This lets a reader run the per-convention test on locality. `is-evidence-for` would overclaim, because the paper says nothing about whether the failure transfers to LLMs.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **is-evidence-for**: the paper is a worked external example of bounding a conclusion to the observed contrast. §4.3 states the narrowest interpretation as dependency length being shorter than the specific baselines run. It refuses to attribute the effect to DLM as the single cause and lists unrun constraints (grammar complexity bounds, noise robustness, uniform information density) as open alternatives. §5 separates grammar from usage by adding a second comparison condition rather than by reinterpreting the first. Both behaviours match the note's three limits.
- [05 Attention Is All You Need (ingest)](../../../../sources/05-attention-is-all-you-need.ingest.md) -- **compares-with**: the shared axis is the cost of linear distance between dependent elements. Human language reduces that cost by reordering the signal (DLM in grammar and usage). The sequence-model history reduced it first by reordering the input (the reversal trick) and then by changing the reader's architecture (attention), after which the hack became unnecessary. The comparison sharpens an open question for KB writing: is a locality convention scaffolding for a distance-limited reader that attention-based readers no longer need, or does it still pay off? See Flags.

## Bidirectional Candidates

- [05 Attention Is All You Need (ingest)](../../../../sources/05-attention-is-all-you-need.ingest.md) <-> source -- **compares-with**: the return link is useful from the attention ingest's "Path length explains temporary hacks" finding. The ingest would gain a non-neural case where distance between dependents is a persistent pressure on the signal itself, not only on the architecture. Under `kb/sources/COLLECTION.md`, `compares-with` is authorised for sources-to-sources.

## Reverse-edge Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → source ingest -- **evidenced-by** (theory label): this would sit in the note's Inference section, where it says subordination, apposition and shared modifiers carry relations. Under the theory contract's "Origin is not corroboration" rule, the context phrase should say the source *qualifies or bounds* the inference. The source supplies a human-side distance mechanism. It was not a test the note could have failed.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) → source ingest -- **evidenced-by** (qualifying): the source would add a second worked convention beside Toulmin. The convention is locality, and its human mechanism is known from psycholinguistics, while its LLM transfer is unchecked. This would make the note's per-convention method concrete at sentence level.

## Off-authorisation Candidates

None

## Raw Text Candidates

- [Sutskever's list, appendix: design patterns for engineers](../../../../sources/sutskevers-list/chapters/11-appendix-design-patterns-for-engineers.md) -- potential **compares-with**: its "Favor short paths and parallelism" pattern ("Architectures that minimize dependency length ... win") uses the same term in the neural path-length sense. The file has no frontmatter and is a chapter of a larger capture, so the authored target is the attention ingest listed above.

## Rejected Candidates

- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) -- its precision regressions are omissions and modality shifts, such as dropping *later* or turning "provides evidence" into "shows". They are not cases of a modifier moving away from its head. The distance mechanism does not explain them.
- [Human-LLM differences are load-bearing for knowledge-system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- it is relevant as the dual-audience premise, but the transfer-test note above already serves the reader. A second link would be a see-also spray.
- [Epiplexity by example](../../../../theory/epiplexity-by-example-what-entropy-and-complexity-miss.md) -- it shares the information-theory vocabulary (surprisal, complexity), but the paper uses excess entropy only as one motivation it mentions in passing. The epiplexity note concerns observer-relative usable structure, not distance between dependent elements.
- [Position bias (ingest)](../../../../sources/position-bias.ingest.md) and [Paulsen MECW (ingest)](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md) -- they concern LLM position and context-length effects at document or prompt scale. Neither measures distance between linked elements, so any link would rest on analogy alone.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) -- the paper's stacked random baselines are a clean design for null models. The proposal, however, ablates framework components on agent tasks. The transferable point (claim only the residual beyond the strongest independent baseline) is already covered by the contrast note, so a reference `see-also` would add no further help.
- `theory/text-testing-framework.md`, agent "working memory" reviews and "surprisal" memory scores -- keyword-only matches.

## Index Membership

None. Sources have no curated index beyond `kb/sources/README.md`, and that file has no groupings. Tag membership is not decided by connect.

## Synthesis Opportunities

The always-loaded quality bar "Keep necessary conditions next to their claims" (AGENTS.md) has no theory note behind it, as far as these searches found. Four pieces together imply a testable claim: [two rewrites](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) shows that detaching qualifiers changes meaning, [human writing structures transfer](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) supplies the per-convention transfer test, this source gives the human-side distance mechanism, and the [attention ingest](../../../../sources/05-attention-is-all-you-need.ingest.md) shows the reader architecture changing. The candidate claim: *condition–claim adjacency is a locality convention with a known human mechanism and an untested LLM mechanism; its warrant for agent readers rests on attachment-error prevention during rewriting rather than on reading cost.* This is a candidate only. No experiment in the KB separates the two warrants.

## Maintenance Observations

- The AGENTS.md quality-bar rule "Keep necessary conditions next to their claims" has no linked theory grounding. A note under `kb/theory/` could supply one, and this source would be one of its inputs.
- `kb/tags/document-system-README.md` has a *Writing Conventions* section with one entry. Sentence-level writing evidence (the two rewrite evidence notes) is filed under Testing or elsewhere, so a reader looking for sentence conventions finds little there.

## Flags

- Tension to keep visible, unresolved: the paper's mechanism (working-memory decay and interference) is specific to humans, while attention gives transformers direct access at any distance. The attention ingest frames distance-reducing hacks as scaffolding that architecture absorbs. Whether locality conventions in KB prose still help LLM readers, or help only by preventing rewrite attachment errors, is open. An ingest that cites this source for agent-facing writing should not imply transfer.
- The ingest does not exist yet (`kb/sources/futrell-levy-gibson-dependency-locality.ingest.md`). All outbound candidates are meant for it.
