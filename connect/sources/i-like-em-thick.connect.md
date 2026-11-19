---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/i-like-em-thick.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: I like 'em thick

**Source:** [I like 'em thick](../../../../sources/.snapshots/i-like-em-thick.md)

## Discovery Trace

**Description listing scan:**

- Read the curated heads for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`. The snapshot has no tags, so no tag README or by-tag `rg` pass applied.
- Generated the complete title surfaces with `rg -N --no-heading -m1 '^# '` for all authorised local destinations: notes (360), reference (139), agent-memory-systems (173), agentic-systems (12), and sources (293).
- Generated the complete `rg '^description:'` surfaces for the same destinations: notes (357), reference (138), agent-memory-systems (171), agentic-systems (10), and sources (293).
- The notes listings flagged the writing-as-thinking, reverse-compression, cheap-generation, warranted-reader-update, explanatory-reach, information-value, and semantic-work clusters. The sources listing flagged the Borretti, Grunewald, Graham, Karlsson, Karnofsky, and AI-blindness ingests. Reference hits concerned Commonplace's own quality vocabulary and ingest architecture rather than a source-level connection. The two system-review collections supplied no candidate whose subject is this essay's artistic or writing-quality mechanism.

**Topic indexes:**

- Read [Tags](../../../../tags/README.md), [Notes](../../../../notes/README.md), [Reference](../../../../reference/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), [Agentic Systems](../../../../agentic-systems/README.md), and [Sources](../../../../sources/README.md). The source has no declared tag, so the curated heads supplied orientation rather than a tag-constrained candidate set.
- The notes hub routed the essay toward foundations, discovery, evaluation, and LLM reliability. The system indexes confirmed that the essay is not an analysis of an agent-memory system or an agentic harness.

**Body search:**

- `rg -n -i -e 'slop|thinness|thickness|cheap generation|effort signal|writing[- ]is[- ]thinking|surface.*scrutiny|substance' ...` -- retained the cheap-generation, reverse-compression, and writing-is-thinking clusters; rejected unrelated uses of `substance` and generic quality-review prose.
- `rg -n -i -e 'explanatory[- ]reach|warranted reader update|quality signal|reverse compression|information value|specificity|overgeneral|longevity|sustained attention' ...` -- retained the warranted-reader-update and explanatory-reach comparisons; the observer-relative information note was judged redundant with the more specific reader-update target.
- `rg -n -i -e 'human effort|opportunity cost|writing.*thinking|generation.*constraint|review.*quality|weakly discriminated|selection pressure' ...` -- tested the essay's discarded-work, reader-participation, reasons, cost, and AI-writing claims. `semantic-work-can-be-relocated-but-not-eliminated.md` was rejected because the essay does not identify the system-placement mechanism that note asserts.
- `rg -n -i -e 'writing[- ]is[- ]thinking|cheap generation|effort signal|reverse compression|substantive writing|explanatory-reach' kb/reference --glob '*.md'` -- found vocabulary and architecture records, not a useful source-to-reference edge.
- `rg -n -i -e 'writing[- ]is[- ]thinking|cheap generation|effort signal|reverse compression|artistic thickness|AI slop' kb/agent-memory-systems kb/agentic-systems --glob '*.md'` -- returned no candidate.

**Link following:**

- Followed [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) to [Reverse compression](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md), then followed inbound links into the AI;DR and AI-blindness source cluster. That neighborhood established that effort is only a proxy for judgment and that reader-side triage is a separate claim from content thinness.
- Followed [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) to [LLM generation relaxes goals where human writing stalls](../../../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md), and then into the Borretti, Grunewald, Graham, Karlsson, and Karnofsky ingests. The new essay repeats the cluster's anti-delegation premise but adds a broader quality concept and a longevity claim.
- Followed [Warranted reader update](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) through its information-value and weak-discrimination premises. This kept the reader-response comparison while rejecting a generic `quality` association.

## Connections Found

- [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) -- **is-evidence-for**: the essay treats accumulated human cost as a defeasible signal of artistic substance, explicitly says cost is no guarantee, and contrasts that signal with cheap machine production; this corroborates and usefully bounds the note's effort-as-proxy mechanism.
- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) -- **is-evidence-for**: the essay's definition of slop as bottomless output that yields nothing under scrutiny is a qualitative instance of expansion without added extractable structure.
- [Warranted reader update is the objective of substantive writing](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) -- **compares-with**: “thickness” says a work continues to reward attention and leaves an ingredient for the reader to supply, while reader update asks what warranted change becomes available to this reader; comparing them separates durable responsiveness from novelty or style.
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- **compares-with**: both properties reward material that survives further inspection, but thickness also bundles discarded alternatives, participation, craft cost, and longevity, none of which alone establishes a causal explanation with explanatory-reach.
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) -- **compares-with**: Mastroianni says the hard work of thickening cannot be delegated to a machine, whereas the note claims a human-judged adversarial loop can relocate drafting while reconstructing the filter; the comparison exposes the loop's disputed boundary rather than a settled contradiction.
- [Human Routers of Machine Words](../../../../sources/borretti-human-routers-of-machine-words.ingest.md) -- **compares-with**: both argue that ideas are not already complete before wording, but this essay places that claim inside a broader account of why art rewards sustained attention rather than treating concretization alone as the mechanism.
- [Why You Should Almost Never Use AI to Write Anything Substantive](../../../../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) -- **compares-with**: both reject AI drafting of substantive prose, while Mastroianni supplies a four-part quality vocabulary and a short-term-appeal versus longevity distinction absent from Grunewald's error, cognition, and trust argument.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) → the eventual ingest -- **evidenced-by**: the blood-sacrifice and AI-slop sections are a bounded conceptual witness for effort functioning as a noisy judgment proxy, including the source's own “no guarantee” caveat.
- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) → the eventual ingest -- **evidenced-by**: “slop holds no secrets” and evaporates under scrutiny is an independent essayist's formulation of the note's content-side failure.
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) → the eventual ingest -- **evidenced-by**: the essay supplies a clear contrary boundary claim—machines cannot perform the thickening work—that future review of the note should confront rather than silently assimilate.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) -- the closing anti-automation claim sounds similar, but the essay does not analyze where a meaning-dependent system judgment is paid or which inputs make relocation possible.
- [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md) -- attention and reader contribution overlap, but [warranted reader update](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) carries the more specific articulation and avoids a redundant edge.
- [Design for the first-time human, except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md) -- the essay's casual-versus-careful audience problem concerns willingness to enter a difficult work, not the linear versus sublinear access-cost mechanism of this note.
- [I'm becoming AI-blind](../../../../sources/im-becoming-ai-blind.ingest.md) and its [Hacker News discussion](../../../../sources/hacker-news-im-becoming-ai-blind.ingest.md) -- they share the AI-slop topic but study cue-conditioned rejection, verification burden, and false positives rather than how substantive work rewards sustained attention.
- [Putting Ideas into Words](../../../../sources/putting-ideas-into-words.ingest.md) -- exact-word commitment is relevant background, but Borretti and Grunewald are the closer source comparisons and already route into Graham's essay.

## Index Membership

None.

## Synthesis Opportunities

- The essay plus [warranted reader update](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md), [explanatory-reach](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md), [reverse compression](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md), and [cheap generation](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) suggest that “quality under sustained inspection” is not one scalar property. It may require separate judgments about extractable structure, justified choices, reader participation, and evidential durability. A future synthesis should first test whether that decomposition changes a KB writing or review decision; the source's aesthetic examples and longevity claim do not by themselves establish the transfer.

## Maintenance Observations

- [Sources README](../../../../sources/README.md) says ordinary pages use “plain WebFetch,” while the current snapshot skill requires Trafilatura. The landing page appears stale relative to the operative procedure.

## Flags

- Split candidate: the source combines an aesthetic-quality concept, four proposed thickening agents, a writing-as-thinking claim, an anti-AI-production thesis, and longevity as a quality test. If promoted beyond an ingest, these should not become one omnibus theory note.
