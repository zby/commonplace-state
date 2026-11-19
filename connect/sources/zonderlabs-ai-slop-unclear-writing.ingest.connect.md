---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/zonderlabs-ai-slop-unclear-writing.ingest.md"
source_has_frontmatter: true
date: "2026-11-11"
depth: standard
---

# Connection Report: Ingest: Why is AI Slop so Frustrating to Read?

**Source:** [Ingest: Why is AI Slop so Frustrating to Read?](../../../../sources/zonderlabs-ai-slop-unclear-writing.ingest.md)

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` outbound section. Prospected destinations: theory (`is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`), theory/definitions (`defined-in`), reference (`see-also` only), sources (`compares-with`, `see-also`), agent-memory-systems and agentic-systems (`compares-with`, `see-also`), external (`derived-from`, `see-also`). Excluded: `kb/work/`, `kb/instructions/`. External prospecting skipped (no open-web search); Williams's *Style* is named in the source but no URL is in hand.

**Already linked from the source (`known`, confirmed sound, not re-proposed):** the Clark et al. ingest (`compares-with`), the HN AI-blind thread ingest (`compares-with`), reverse compression (`compares-with`), measurable widespread model failures (`is-evidence-for`).

**Topic indexes:**
- `kb/tags/prose-readability-README.md` (the source's tag; `complete: true`, so the by-tag rg over theory was skipped). Members read as candidates: figurative wording, position-and-proportion, dependency locality, structured output, human-writing-structures transfer, design-for-first-time-human, the two rewrite evidence notes, reverse compression. Its Procedures section pointed to `kb/instructions/simplify-prose-with-established-style-advice.md` (excluded destination, read only to check how Williams is used).

**Titles listing:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md' | rg -i 'prose|writ|read|clar|slop|style|nominal|vague|compress|llm output|wording|sentence|measur|upstream|detect|annotat|human judg|review'` -- 46 titles; flagged: warranted reader update, position-and-proportion, human-writing-structures transfer, dependency locality, writing styles, reverse compression, LLM generation relaxes goals, measurable failures, two rewrites, three simplification passes, figurative wording, vocabulary collisions, semantic review.

**Description listing scan:**
- Per-path `rg -N '^description:'` on the 12 flagged theory titles (resolved with `rg -l -F -m1 "# <title>"`). Kept three-simplification-passes (description: established-style pass "clarified actors") and position-and-proportion; rejected the rest (see Rejected).
- Per-path description read on source ingests surfaced by body search: `im-becoming-ai-blind`, `hacker-news-im-becoming-ai-blind`, `hacker-news-llm-voice`, `i-like-em-thick`, `borretti-human-routers-of-machine-words`, `hacker-news-ai-dr-ai-didnt-read`, `researchers-asked-llms-strategic-advice-trendslop`, `why-is-ai-generated-language-so-hard-to-understand`, `temperley-gildea-2018-minimizing-dependency-lengths`.

**Body search:**
- `rg -l -i 'slop|nominali[sz]|williams|stacked noun|noun stack|vague word|em dash|delve|ai-blind|clarity' kb/sources kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags` -- 46 files; source-side hits evaluated above; theory hits (text-testing, automated tests, maintenance capacity, oracle notes) use "clarity" incidentally; agent-memory-systems hits (gnosis, skillnote, Closure-SDK) use "clarity" in an unrelated sense.
- `rg -n -i 'williams|nominali[sz]|character.{0,20}subject|noun stack|stacked noun|noun compound' kb/theory kb/reference kb/tags kb/agentic-systems kb/sources` -- only the Clark ingest and the target; no theory or reference artifact states the character/action principle.
- `rg -l -i 'zonder|zonderlabs' kb` -- target only; no inbound links yet.
- `rg -n -i 'reader burden|reader cost|reading cost' kb/theory -l` -- dependency locality only.
- `rg -n -i 'emphasis|stress position|empty statement|vague|AI detector|provenance' kb/theory` -- no theory note on emphasis placement besides position-and-proportion; provenance hits are citation provenance, unrelated.
- `rg -n -i 'compound|clark|why-is-ai-generated' kb/theory` and `rg -n -i 'hacker-news-im-becoming|im-becoming-ai-blind|why-is-ai-generated|ai-dr-ai|llm-voice' kb/theory kb/tags kb/reference` -- no theory note cites the Clark ingest or the HN AI-blind ingest; AI;DR is cited by maintenance capacity.
- `rg -n -i 'mannered|clause.packing|prose gate|prose lens' kb/reference` -- no reference description of the prose gates.
- `rg -l -i 'prose quality|writing quality|readab' kb/agentic-systems kb/reference` -- hits are system reviews and proposals unrelated to prose clarity.
- Snapshot check `rg -n -i 'emphasis|empty|point|detector|ideal|agree' kb/sources/.snapshots/zonderlabs-ai-slop-unclear-writing.md` and read of the "Empty statements and misplaced emphasis" section, to judge whether the emphasis fault concerns where the point sits (it does: the repair moves the point to the front of a two-sentence reply).

**Link following:**
- Three simplification passes -> established-style instruction: its guidance names "Williams's focus on clear actors and actions" and "Gopen and Swan's attention to reader expectations and emphasis", which align with Zonder's faults 1 and 3.
- Position-and-proportion -> Kieras and Freebody/Anderson ingests: human evidence for opening position as a theme cue; confirms the note's scope is document theme, while Zonder's example is sentence-scale.
- Reverse compression body: confirms its measure is reader-accessible structure, consistent with the already-authored compares-with.
- Measurable failures: no `kb/sources/` links in its body, so a reverse edge from it would be its first external case.

### Candidate origins

- kb/sources/hacker-news-ai-dr-ai-didnt-read.ingest.md — body-search, descriptions
- kb/sources/hacker-news-llm-voice.ingest.md — body-search, descriptions
- kb/theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md — curated-head, titles, descriptions
- kb/theory/position-and-proportion-set-what-a-reader-retains.md — curated-head, titles, descriptions
- kb/sources/why-is-ai-generated-language-so-hard-to-understand.ingest.md — known, body-search
- kb/theory/measurable-widespread-model-failures-and-upstream-fixes.md — known, titles

## Connections Found

- [HN — AI;DR (ingest)](../../../../sources/hacker-news-ai-dr-ai-didnt-read.ingest.md) -- **compares-with**: on the axis of style-based detection versus fault-based review. That thread records the cost of provenance heuristics (writers avoiding em dashes and "load-bearing" to escape false accusation); Zonder argues those same signatures are not what makes text unclear and claims a measured divergence from an AI detector. Read together, they give both the cost of detecting by style and the proposed alternative.
- [HN — LLM voice (ingest)](../../../../sources/hacker-news-llm-voice.ingest.md) -- **compares-with**: on the axis of causal accounts for unclear AI prose. The thread lists post-training, concentrated default voices, prompt residue and weak audience modeling without adjudicating them; Zonder adds "hard to reward and less economically appealing". A writer comparing causal stories (with the Clark length-penalty account) needs the full set.
- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) -- **compares-with**: on the axis of clarity repairs judged by readers. The best-ranked pass there "clarified actors, causal sequences, and comparisons" — the repair for Zonder's hidden-characters fault — and a blind judge ranked it first while it added words. That is KB-local, judged evidence that fixing this fault need not shorten text, which Zonder's examples (all shorter rewrites) do not show.
- [Opening position can signal a human reader's theme; proportion remains conjectural](../../../../theory/position-and-proportion-set-what-a-reader-retains.md) -- **compares-with**: on the axis of where the point sits. Zonder's misplaced-emphasis repair moves the point to the front of a short reply; the note separates the human evidence for an opening cue from the untested proportion conjecture and warns that the repair should target placement, not brevity. Scope differs (sentence pair versus document theme), so the comparison should say so.

## Bidirectional Candidates

- [Why is AI-generated language so hard to understand? (ingest)](../../../../sources/why-is-ai-generated-language-so-hard-to-understand.ingest.md) <-> source -- **compares-with**: the Clark ingest's limitations say the paper never measures reader comprehension; a return link names Zonder as a source that claims a human clarity judgment of overlapping constructions (stacked nouns, hidden actors), marked as uninspected because its rates were not captured.

## Reverse-edge Candidates

- [Measurable, widespread model failures are candidates for upstream fixes](../../../../theory/measurable-widespread-model-failures-and-upstream-fixes.md) → source -- **evidenced-by** (under `kb/theory/COLLECTION.md`): a dated practitioner case that explains a failure's persistence with the note's measurability and incentive conditions and then publishes a measurement scheme. The context phrase must say it qualifies or illustrates rather than corroborates: the case was not a test the note could have failed, and its rates are uncaptured. It also names a concrete instance for the note's persistence experiment (Claude Code vague-wording rate across releases).

## Off-authorisation Candidates

- [Simplify prose with established style advice](../../../../instructions/simplify-prose-with-established-style-advice.md) -- the instruction already invokes Williams's actors-and-actions lens and Gopen and Swan's emphasis lens, which match Zonder's faults 1 and 3. `kb/instructions/` is an excluded destination for sources ("executing readers don't follow source links"), so reject as off-scope; any use belongs in a theory note that the instruction could rest on.

## Raw Text Candidates

None

## Rejected Candidates

- [I'm becoming AI-blind (Cymerys ingest)](../../../../sources/im-becoming-ai-blind.ingest.md) -- its axis is repeated-exposure suppression of AI-marked prose; the HN thread on the same essay is already linked and covers the style-versus-substance contrast, so a second link adds little.
- [Dependency locality supports ordering heuristics, not a reading-cost rule](../../../../theory/dependency-locality-supports-ordering-heuristics-not-a-reading-cost.md) -- concerns word order and dependency length; Zonder's faults are actor encoding, word choice and point placement, and it does not measure dependency length (the Clark ingest does).
- [Figurative wording can suggest relations that the target claim does not justify](../../../../theory/figurative-wording-imports-source-domain-entailments-unless-mapped.md) -- Zonder's odd word combinations ("user-session entry boundary") are vague compounds, not figures importing source-domain entailments.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- about LLMs as readers of human structures; Zonder is about humans reading LLM output.
- [Warranted reader update is the objective of substantive writing](../../../../theory/warranted-reader-update-is-the-objective-of-substantive-writing.md) -- contribution selection at document scale; Zonder's empty statements have a point that is present but hard to find, so the overlap is keyword-level.
- [Load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../../../../theory/vocabulary-collisions-prevented-at-write-time-not-read-time.md) -- double senses of registered terms, not vague coinages.
- [LLM generation can hide a relaxed goal where human writing exposes a stall](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) -- content-level goal relaxation, not sentence clarity.
- [Borretti — human routers of machine words (ingest)](../../../../sources/borretti-human-routers-of-machine-words.ingest.md) -- reader burden from content-free input laundered into fluent text; closer to reverse compression than to Zonder's encoding faults.
- [Trendslop (ingest)](../../../../sources/researchers-asked-llms-strategic-advice-trendslop.ingest.md) -- "slop" keyword match only; about advice content following discourse priors.
- [I like 'em thick (ingest)](../../../../sources/i-like-em-thick.ingest.md) -- "slop" keyword match; artistic thickness, not clarity.

## Index Membership

None. Sources do not participate in tag-head membership (`kb/tags/COLLECTION.md`); the source already carries `tags: [prose-readability]`, which fits the head's inclusion condition (what makes a passage hard to follow).

## Synthesis Opportunities

The Clark ingest (producer-side construction counts), this source (claimed human clarity judgment), [reverse compression](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) (selection failure) and [three simplification passes](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) (actor-clarifying repair ranked best while adding words) together imply a claim not yet in the KB: unclear encoding is a cause of reader cost separate from length or selection, and its repair can lengthen text. This matches the source's Recommended Next Action; the three-simplification evidence is a third leg that recommendation does not name.

## Maintenance Observations

- Williams's character/action principle and Gopen and Swan's emphasis principle are invoked by `kb/instructions/simplify-prose-with-established-style-advice.md` but stated in no theory or reference artifact, so procedures cite style lenses with no durable home for their content or evidence (also noted in the source's Extractable Value item 5).
- No theory note cites the Clark ingest or the HN AI-blind ingest; the prose-readability evidence base for AI-drafted prose sits only in `kb/sources/`.
- Two ingests cover the same AI-blind essay at different levels (`im-becoming-ai-blind.ingest.md` for the essay, `hacker-news-im-becoming-ai-blind.ingest.md` for the thread); not duplicates, but a writer can confuse them.

## Flags

- All quantitative claims in the source are uncaptured; every connection above should carry "claimed, not inspected" wording where it relies on Zonder's rates or detector comparison.
- Tension to keep visible, not resolve: Zonder's "hard to reward" cause versus Clark's length-penalty cause; both may hold.
