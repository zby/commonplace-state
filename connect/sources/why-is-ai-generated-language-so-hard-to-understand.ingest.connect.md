---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/why-is-ai-generated-language-so-hard-to-understand.ingest.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Ingest: Why is AI-generated language so hard to understand?

**Source:** [Ingest: Why is AI-generated language so hard to understand?](../../../../sources/why-is-ai-generated-language-so-hard-to-understand.ingest.md)

The ingest already carries nine footer links (external paper; theory: dependency-locality, human-LLM differences, reverse compression, two rewrites, fixed decomposition; sources: Futrell 37 languages, Gibson 2019, AI;DR). This report lists only candidates beyond those.

## Discovery Trace

**Linking rules:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `kb/work/` and `kb/instructions/` excluded. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). No label names `tags` as a destination. External prospecting skipped (the only external target, the arXiv URL, is already linked).

**Description listing scan:**
- `rg -m1 '^description:'` over the seven dependency-locality ingests in `kb/sources/` (futrell-*, gibson-*, temperley-*) -- flagged `gibson-dependency-locality-theory`, `gibson-1998-linguistic-complexity-locality`, `temperley-gildea-2018-minimizing-dependency-lengths` (all carry an object-relative cost rule); `temperley-2007` (writer word order, no relative-clause overlap with H1 features beyond nesting) and `futrell-levy-gibson` (corpus word order) not flagged.
- Descriptions of AI-prose ingests: `borretti-human-routers-of-machine-words`, `im-becoming-ai-blind`, `researchers-asked-llms-strategic-advice-trendslop`, `i-like-em-thick`, `adam-mastroianni-infinite-midwit`, `hacker-news-ai-dr-ai-didnt-read` (already linked).
- Theory titles: `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (428 titles) filtered with `grep -i -E "proxy|goodhart|compress|dens|terse|short|length|readab|prose|style|word|sentence|reader|optimi|objective|reward|metric"` -- flagged `exact-implementation-does-not-validate-a-requirement`, `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric`, `warranted-reader-update-is-the-objective-of-substantive-writing`, `writing-styles-are-strategies-for-managing-underspecification`; descriptions read for each.

**Topic indexes:**
- `kb/tags/prose-readability-README.md` (`complete: true`; by-tag rg skipped). Members reviewed: dependency-locality, structured output, human writing structures transfer, design for first-time human, two rewrites, three simplification passes, reverse compression. New candidate: `three-simplification-passes-exposed-different-tradeoffs`.
- `kb/tags/COLLECTION.md` -- `participating` excludes `sources`, so the ingest cannot be a tag member.
- `kb/sources/README.md` -- no curated per-source listing.

**Body search:**
- `rg -l -i "reward hacking|goodhart|length penalty|verbos|RLHF|post-training|mode collapse|sycophan|slop" kb/theory kb/sources` -- ~50 files, mostly RL/self-improvement ingests (cedar-grpo, dual-nature on-policy distillation, sutton-javed); none treats style or readability drift, rejected as keyword-only.
- `rg -l -i "AI writing|AI-generated (text|prose|writing)|machine prose|llm prose|em.dash|purple prose|mannered" kb/sources kb/theory` -- `adversarial-loop-can-reconstruct-the-writing-is-thinking-filter`, `llm-generation-relaxes-goals-where-human-writing-stalls`, `adam-mastroianni-infinite-midwit`, `i-like-em-thick`; evaluated below.
- `rg -n -i "object relative|relative clause|that.omission|optional .that|noun compound|denominal|animacy|inanimate" kb/sources kb/theory` -- hits in `gibson-dependency-locality-theory` (rule: "prefer subject-extracted to object-extracted relative clauses"), `gibson-1998` (same rule), `temperley-gildea-2018` ("Avoid object relatives with full-noun subjects ... strongest direct cost evidence in the review"; limitation: such constructions "are rare in KB prose"), `temperley-2007`, dependency-locality theory note. No KB artifact covers denominal verbs, inanimacy or noun stacks.
- `rg -n -i "gibson|temperley|futrell|grodner" kb/sources/.snapshots/why-is-ai-generated-language-so-hard-to-understand.md` -- the paper cites Gibson 1998 and 2000 and Temperley & Gildea 2018 as its object-relative difficulty premise; its "Futrell et al., 2020" is *Lossy-context surprisal*, not the `futrell-levy-gibson-dependency-locality` ingest (2020 *Language* paper).
- `rg -l "why-is-ai-generated-language" kb` -- no inbound links anywhere.
- `rg -n -i "llm|agent-drafted|model" kb/theory/dependency-locality-supports-ordering-heuristics-not-a-reading-cost.md` -- the note has an "LLM readers" section and says LLM-reader benefit is untested; it has no producer-side evidence.

**Link following:**
- `exact-implementation-does-not-validate-a-requirement` -> footer `a-proximate-target-is-checked-for-achievement-not-for-warrant`; the former is the closer fit (a locally exact check versus a conjectured proxy link).
- `three-simplification-passes` body: "The result argues against judging a simplifier by word count alone" -- directly shares the length-versus-readability axis.
- `temperley-gildea-2018` limitations: strongest cost evidence comes from object relatives "rare in KB prose" -- this paper reports LLMs overuse reduced object relatives, which tensions that rarity premise for agent-drafted prose.

## Connections Found

- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) -- **compares-with**: word count against readability of an edit. The KB run found the shortest pass drifted and the best-ranked pass added words; the paper's length-penalty result gives a mechanism for why word-count pressure pushes toward denser constructions. Complements the existing two-rewrites link, and is one of the inputs the ingest's Recommended Next Action ("A length target cannot proxy readability") would need.
- [The Dependency Locality Theory (Gibson 2000)](../../../../sources/gibson-dependency-locality-theory.ingest.md) -- **compares-with**: object-relative processing cost. The paper borrows Gibson 1998/2000 as the human-difficulty premise for one of its measured features; this ingest records that premise, its "prefer subject-extracted relatives" rule, and its human-only scope. Lets a reader check what the borrowed cost actually rests on.
- [Minimizing Syntactic Dependency Lengths (Temperley & Gildea 2018)](../../../../sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md) -- **compares-with**: object-relative cost and its naturalistic size. The paper cites this review for speakers avoiding costly constructions; the ingest records that object-relative evidence is the review's strongest but comes from constructed sentences and is small on newspaper text. That bounds the paper's inferred reader cost, while the paper's finding that LLMs overuse reduced object relatives challenges the ingest's "rare in KB prose" assumption for agent-drafted prose.
- [Exact implementation does not validate a requirement against its objective](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) -- **is-evidence-for** (optional, lower priority): in the H2 task the correctness check is exact and both variants pass, yet the requirement (correct and short) is a conjectured proxy for human-like communication, and the proxy link fails. Overlaps with the existing fixed-decomposition link; add only if the ingest's Learning Claims section is expanded to the proxy framing.

## Bidirectional Candidates

- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) <-> source -- the evidence note's "against judging a simplifier by word count alone" inference would gain an external mechanism; see reverse edges.

## Reverse-edge Candidates

Theory labels apply (`kb/theory/COLLECTION.md`); the ingest was not the origin of these notes, so `evidenced-by` context phrases must say the evidence qualifies or bounds, not corroborates, unless the note's claim risked failing against it.

- [Dependency locality supports ordering heuristics, not a reading-cost rule](../../../../theory/dependency-locality-supports-ordering-heuristics-not-a-reading-cost.md) → source -- **evidenced-by**: qualifies the "LLM readers" section from the producer side: frontier-model text has longer standardized dependencies than its round-trip paraphrases, so the heuristics target a real tendency in agent-drafted prose; LLM-reader benefit remains untested. Highest-value reverse edge; the ingest's own lead connection points here and there is currently no return path.
- [Reverse compression is when LLM output expands without adding information](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) → source -- **evidenced-by**: bounds the note's framing of the "common failure" of LLM output by documenting the opposite length failure (density that saves tokens and raises human processing cost), so length reduction is not the remedy for reverse compression in general.
- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) → source -- **evidenced-by**: qualifies the word-count inference with a sufficiency mechanism (a per-token penalty alone drove a categorical shift to the shorter alternation in one 1.5B model).
- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → source -- **evidenced-by**: same qualification as above for the syntax-versus-word-count tradeoff.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) → source -- **evidenced-by**: a measured human-LLM divergence in produced prose; human cost inferred from prior studies, so the phrase should say it bounds rather than corroborates.

## Off-authorisation Candidates

- [Prose readability tag head](../../../../tags/prose-readability-README.md) -- the ingest's subject is this tag's scope, and the head's "Readability is not brevity" caution is the claim the ingest's Extractable Value item 1 says the KB "has stated only as a tag-head caution". No label in `kb/sources/COLLECTION.md` authorises `sources -> tags` although the contract tells writers to scan `kb/tags/`. Suggest either adding a tags destination to `see-also` or rejecting; the reverse direction is also blocked because `sources` is not a participating collection.

## Raw Text Candidates

None

## Rejected Candidates

- [LLM generation relaxes goals where human writing stalls](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) -- about silent goal relaxation behind fluent prose, not syntactic density; shared topic "LLM prose is hard on readers" only.
- [Adversarial loop can reconstruct the writing-is-thinking filter](../../../../theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) -- concerns thinking delegated to drafting, not construction-level readability.
- [I'm becoming AI-blind](../../../../sources/im-becoming-ai-blind.ingest.md) -- reader rejection by repeated exposure; no construction or mechanism overlap. The existing AI;DR link already covers the reader-burden comparison.
- [Borretti: human routers of machine words](../../../../sources/borretti-human-routers-of-machine-words.ingest.md) -- writing-is-thinking polemic; no density axis.
- [Trendslop](../../../../sources/researchers-asked-llms-strategic-advice-trendslop.ingest.md) and [Infinite midwit](../../../../sources/adam-mastroianni-infinite-midwit.ingest.md) -- content homogeneity and taste, not syntax.
- [Gibson 1998](../../../../sources/gibson-1998-linguistic-complexity-locality.ingest.md) -- same object-relative rule as Gibson 2000; one link to the DLT ingest suffices.
- [Futrell, Levy and Gibson 2020](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) -- the paper's "Futrell et al., 2020" is a different work (lossy-context surprisal); word-order corpus overlap is already carried by the Futrell 37-languages link.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- about evidence for compounding across episodes, not an objective omitting a distinction.
- [Verifiability gradient](../../../../theory/verifiability-gradient.md) -- shares the word "verifiable" with "verifiable-reward training" only.
- Reference, agent-memory-systems and agentic-systems -- no artifact treats LLM prose style or post-training style drift; nothing prospected passed the articulation test.

## Index Membership

None. `kb/sources/README.md` has no curated listing, and `sources` does not participate in tags, so the ingest is reachable only through inbound links (currently none).

## Synthesis Opportunities

The ingest's Recommended Next Action already names it: reverse compression + two rewrites + three simplification passes + this paper imply "a length target cannot proxy readability of LLM-drafted prose; expansion and density fail in opposite directions". Three simplification passes is a third KB-internal input the recommendation does not list.

## Maintenance Observations

- Collection-contract gap: `kb/sources/COLLECTION.md` tells writers to scan `kb/tags/` for link targets but no label authorises a tags destination.
- The ingest has no inbound links. Because sources cannot carry tags, it stays orphaned until a theory note authors a reverse edge.
- `temperley-gildea-2018` and `gibson-dependency-locality-theory` ingests treat object relatives as rare in KB prose; this paper's overuse finding is a tension worth noting when those ingests or the dependency-locality note are next revised.

## Flags

- Tension: Temperley & Gildea ingest ("object relatives ... rare in KB prose", so reordering gains may be small) versus this paper (LLMs overuse reduced object relatives relative to their own paraphrases). Not resolved; the paper measures chat, coding and essays, not KB prose.
