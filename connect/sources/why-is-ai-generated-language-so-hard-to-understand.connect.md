---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/why-is-ai-generated-language-so-hard-to-understand.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Why is AI-generated language so hard to understand?

**Source:** [Why is AI-generated language so hard to understand?](../../../../sources/.snapshots/why-is-ai-generated-language-so-hard-to-understand.md)

The source is an immutable snapshot (Clark, Martin and Mahowald, arXiv 2610.29162, 2026-10-21). Its authored connection surface is the name-paired ingest `kb/sources/why-is-ai-generated-language-so-hard-to-understand.ingest.md`, which did not exist when this report was written. Every outbound candidate below is meant for that ingest's `Connections Found`, not for the snapshot.

Source claims used for judging candidates:

- **H1 (corpus):** text from nine frontier and near-frontier models overuses constructions associated with human processing difficulty, compared with human reference corpora and with round-trip-translation paraphrases of the same content. All nine overuse inanimate subjects with animate verbs and low-frequency n-grams; most also show longer dependencies, more stacked nouns and more reduced object relatives. Model families vary, and Opus 5.5 improves on Opus 5.
- **H2 (mechanism, proof of concept):** a length penalty under GRPO fine-tuning drives a small model to a near-categorical preference for the shorter member of syntactic alternations, and the preference transfers to untrained alternations (near transfer reliably, far transfer in one of four cases). The authors tie this to an information-density pressure from verifiable-reward post-training, against the human pressures of communicative efficiency and uniform information density.
- **Background claims:** human text is well optimized against random baselines, for example in dependency length; larger LLMs fit human reading times worse than smaller ones; memory-constrained LLMs fit human reading behaviour better.
- **Limits:** English only, few seeds, the causal claim rests on small-model proxies, and the feature list correlates with difficulty rather than measuring reader comprehension of the generated text directly.

## Discovery Trace

**Setup:**

- Read `kb/sources/COLLECTION.md` outbound section. Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `external` only for `derived-from` and `see-also`. Excluded: `kb/work/`, `kb/instructions/`. Sources→theory labels: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, `see-also`. Sources→sources: `compares-with`, `see-also`.
- Read the `connect-report` type spec and the snapshot (abstract, introduction, background, length-penalty discussion, general discussion, conclusion, limitations).
- External prospecting skipped. The only external target in hand is the arXiv URL, which belongs in the ingest's `source` field and needs no `derived-from` footer link.

**Topic indexes:**

- `kb/tags/prose-readability-README.md` (untracked, `complete: true`). Its members are the main theory candidates: the dependency-locality note, structured-output, human-writing-structures-transfer, design-for-the-first-time-human, the two rewrite evidence notes and reverse compression. Because the head is complete, the by-tag `rg` for `prose-readability` was skipped. Sources are not a participating tag collection (`kb/tags/COLLECTION.md` lists theory, reference, instructions, agent-memory-systems, agentic-systems and reports), so the ingest cannot become a tag member.

**Title and description listing:**

- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'prose|writ|read|llm output|compress|human|style|densit|legib|clar|jargon|sentence|verbos|slop|length|fluen|reward|post-train|RL|monitor|token'` flagged dependency-locality, reverse-compression, human-llm-differences, human-writing-structures-transfer, design-for-the-first-time-human, structured-output, warranted-reader-update, llm-generation-relaxes-goals, writing-styles-are-strategies and the two rewrite evidence notes. Descriptions were then read for the strongest ten.
- `ls kb/sources | grep -iE 'why-is-ai|dependenc|locality|gibson|futrell|uid|information-dens|readab|...'` found the seven dependency-locality ingests from commit 86092697f. No ingest exists yet for this paper.

**Body search:**

- `rg -l -i 'dependency locality|dependency length|information density|uniform information|processing difficulty|psycholinguist|surprisal|nominali|stacked noun|noun stack'` over theory, reference, sources, agentic-systems, agent-memory-systems and tags found the dependency-locality cluster (one theory note plus seven ingests), the prose-readability and document-system tag heads, and false positives (epiplexity, skills-derive-from-methodology, Zikkaron, signetai, the sutskevers-list chapters).
- `rg -l -i 'ai-generated (text|writing|prose)|llm-generated (text|prose|writing)|writing style|hard to (read|understand)|intelligib|unreadable|verbose|terse|RLVR|verifiable reward|length penalty|monitorab'` over ingests, theory, agentic-systems and reference found the AI-writing reader-burden ingests (hacker-news-ai-dr, im-becoming-ai-blind, borretti), reading-between-the-dots (monitorability) and many keyword-only hits on RL or self-improvement, which were rejected on description.
- `rg -n -i 'compress|dens|nominal|noun|terse|stack'` over the five closest theory notes confirmed that the two-rewrites evidence note frames its result as "syntactic compression" against lexical repetition.
- `rg -l -i 'readab|psycholing|prose style|sentence-level' kb/reference kb/agentic-systems kb/agent-memory-systems` returned only incidental "readable" mentions in system reviews and `storage-architecture.md`. No candidates in those destinations.

**Link following:**

- From the dependency-locality note: followed its footer to all seven ingests and to human-writing-structures-transfer and human-llm-differences. Its `LLM readers` section and its first open question ask whether LLM readers bear locality costs, which this paper's background addresses indirectly.
- From reverse-compression: followed to vibe-noting and the SuperARC ingest. Reverse compression is the opposite failure on the length axis.
- From the hacker-news-ai-dr ingest: it treats reader burden from AI text as an effort asymmetry about content, not syntax.

## Connections Found

- [Dependency locality supports ordering heuristics, not a reading-cost rule](../../../../theory/dependency-locality-supports-ordering-heuristics-not-a-reading-cost.md) -- **is-evidence-for**: the paper measures that frontier-model text has longer dependencies than human text, so the note's heuristics apply to agent-drafted prose, not only to human drafts. Its background also cites evidence that larger LLMs fit human reading times worse, which bears on the note's untested LLM-reader question. The paper does not test any of the six heuristics or measure reader comprehension.
- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **compares-with**: axis of syntactic compression against word count. The rewrites found that undoing compressed syntax costs words. The paper shows that a length penalty produces compressed syntax, which predicts that word-count pressure on an editing pass pushes toward the constructions the passes were trying to remove.
- [Reverse compression is when LLM output expands without adding information](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) -- **compares-with**: axis of output length against reader cost. Reverse compression adds tokens without adding structure. The paper documents the opposite failure, density that saves tokens and raises processing cost. Together they show that "shorter" and "easier to read" are separate targets, which is the prose-readability head's own warning.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- **is-evidence-for**: the paper gives a measured case on the producer side. LLM writers produce constructions that are cheap for full-attention models and costly for human working memory. The dual-audience argument predicts this divergence. Caveat: the human-cost link is correlational from prior psycholinguistics, not measured on these texts.
- [Large-scale evidence of dependency length minimization in 37 languages](../../../../sources/futrell-dependency-length-minimization.ingest.md) -- **compares-with**: axis of dependency length against a baseline. Futrell, Mahowald and Gibson find human text below random reorderings. This paper, which shares an author and cites that result as its human baseline, finds that most frontier models exceed the human level.
- [How efficiency shapes human language](../../../../sources/gibson-2019-how-efficiency-shapes-language.ingest.md) -- **compares-with**: axis of which optimization pressure shapes the language. Gibson et al. 2019 is the paper's premise that human language is optimized for communication. The paper argues that verifiable-reward post-training replaces that pressure with information density.
- [AI;DR (AI; Didn't Read) — Hacker News discussion](../../../../sources/hacker-news-ai-dr-ai-didnt-read.ingest.md) -- **compares-with**: axis of where AI text burdens readers. The thread reports burden from excess and unchecked content. The paper reports burden from dense syntax and rare word sequences. An ingest that names both keeps one remedy, cutting length, from being applied to the other failure.

## Bidirectional Candidates

- [Dependency locality supports ordering heuristics, not a reading-cost rule](../../../../theory/dependency-locality-supports-ordering-heuristics-not-a-reading-cost.md) <-> source ingest -- **evidenced-by** (theory side): the note's `LLM readers` section and its first open question would gain a pointer to the paper's cited evidence that large LLMs diverge from human reading behaviour, and to its finding that LLM writers produce longer dependencies. The return edge should be scoped as producer-side and indirect evidence. It does not answer whether LLM readers make attachment errors.

## Reverse-edge Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → source ingest -- **evidenced-by** (theory label): the paper's length-penalty result offers a mechanism for why compressed syntax appears in LLM-drafted text in the first place. It bounds rather than corroborates, so author it only if the note is revised to discuss where the compressed syntax came from.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) → source ingest -- **evidenced-by**: the paper is an external measurement of a human-LLM divergence in produced prose, which the note currently argues mostly from first principles.

## Off-authorisation Candidates

- [Clause packing](../../../../instructions/review-gates/sentence/clause-packing.md), [Mannered prose](../../../../instructions/review-gates/prose/mannered-prose.md), [Jargon persistence](../../../../instructions/review-gates/accessibility/jargon-persistence.md) -- the paper's feature list (stacked nouns, denominal verbs, inanimate subjects with animate verbs, reduced object relatives, rare n-grams) maps closely onto what these gate lenses detect. `kb/sources/COLLECTION.md` excludes `kb/instructions/` because executing readers do not follow source links. The right route is not a new label. A theory note abstracted from this paper could carry the claim, and the gates could then operationalize from that note.

## Raw Text Candidates

None

## Rejected Candidates

- [I'm becoming AI-blind](../../../../sources/im-becoming-ai-blind.ingest.md) -- concerns reader rejection triggered by style cues and inferred provenance, not processing difficulty. The overlap is only that both describe AI-text surface features.
- [Borretti: human routers of machine words](../../../../sources/borretti-human-routers-of-machine-words.ingest.md) -- a writing-is-thinking polemic about content and authorship. No syntactic axis is shared.
- [Reading between the dots](../../../../sources/reading-between-the-dots-decoding-hidden-computation.ingest.md) -- the paper names monitorability only once, in its conclusion. A keyword match.
- [Structured output is easier for humans to review](../../../../theory/structured-output-is-easier-for-humans-to-review.md) -- concerns section-level separation of evidence and reasoning, not sentence-level constructions.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- concerns LLM readers benefiting from human structures. The paper studies LLM writers and human readers, so it does not supply the transfer test this note asks for.
- [Design for the first-time human, except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md) -- concerns access-path cost, not sentence construction. The match comes only from tag co-membership.
- [LLM generation can hide a relaxed goal where human writing exposes a stall](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) -- concerns goal fidelity, not linguistic form.
- The remaining dependency-locality ingests (Gibson 1998, Gibson 2000, Futrell-Levy-Gibson 2020, Temperley 2007, Temperley-Gildea 2018) -- reached through the theory note. Linking each from this ingest would be a see-also spray, and the 2015 corpus ingest and the 2019 review already carry the two specific comparison axes.

## Index Membership

None. Sources are not a participating tag collection. The source would naturally inform the [prose-readability](../../../../tags/prose-readability-README.md) area, but it can reach that area only through a theory note.

## Synthesis Opportunities

- This paper, [reverse compression](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) and [two rewrites](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) together imply a claim the KB states only as a tag-head caution: LLM prose fails readers in two opposite directions on the length axis. Expansion adds tokens without structure, and density, which a length or token pressure selects for, removes the redundancy human readers use. A length target therefore cannot serve as a readability proxy in either direction, and an editing pass needs construction-level checks. A candidate theory note would be abstracted from this paper, with the dependency-locality note as its mechanism. Its open boundary is that no source yet measures comprehension of LLM-drafted KB prose directly.

## Maintenance Observations

- `kb/tags/prose-readability-README.md` is untracked and declares `complete: true`. A complete-head skip relies on that working-tree state. If the head changes before commit, rerun the by-tag scan.
- The name-paired ingest was absent during this run (the `cp-skill-ingest` agent was active in the same session). Re-check that the ingest's own `Connections Found` does not duplicate or contradict the candidates above.

## Flags

- Evidence strength: H1 rests on corpus feature counts tied to difficulty by prior psycholinguistics. H2 is a small-model proof of concept, and its RLVR attribution is the authors' speculation. Any theory edge should keep "producer-side, correlational" next to the claim.
- Possible tension: the paper says denser LLM syntax is harder for humans, while the dependency-locality note finds the direct reading effects on ordinary text small. Both can hold, but a writer citing the paper as proof of large comprehension costs would overreach the note's caution.
