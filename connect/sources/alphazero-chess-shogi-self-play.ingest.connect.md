---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/alphazero-chess-shogi-self-play.ingest.md"
source_has_frontmatter: true
date: "2026-11-22"
depth: standard
---

# Connection Report: Ingest: Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm

**Source:** [Ingest: Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](../../../../sources/alphazero-chess-shogi-self-play.ingest.md)

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `kb/work/` and `kb/instructions/` excluded. Labels per destination: theory gets `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also` (and `defined-in` for theory/definitions); sources get `compares-with`, `see-also`; agent-memory-systems get `is-evidence-for`, `compares-with`, `see-also`; agentic-systems get `compares-with`, `see-also`; reference gets `see-also`. External: `derived-from` and `see-also`. The only already-known external target is the arXiv URL already held as `source`, so no external prospecting was done.

**Known links (already in the source's Connections Found / Learning Claims):** selection-based-learning definition, proposal-selection loop note, codification-and-relaxing, unearned-reach, machinery-persists-by-warrant, warranted-autonomy-oracle-domain, reflection-buys-addressability, bootstrap-bitter-lesson, theory-builder definition, learning-inside-a-fixed-decomposition, Sutton essay ingest, AlphaDev 2026-09-08 ingest. All 12 targets resolve (`test -f` loop). They are not re-proposed below.

**Topic indexes:**
- `kb/tags/improvement-loop-README.md` (`complete: true`, so the by-tag rg was skipped). The Loop structure group exposed [an omitted improvement-loop function and a frozen one need different repairs](../../../../theory/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md), whose context phrase reads "why a direct update lacks a gate without omitting one". That is AlphaZero's exact move. The Evaluation group exposed oracle-accumulation and weakly-discriminated notes. Both are rejected below.
- `kb/tags/learning-theory-README.md` (`complete: true`, so the by-tag rg was skipped). Its Start-here group adds nothing beyond the verifiability gradient (rejected below). It routes to the self-improving-systems child area.

**Titles listing:** `rg -N --no-filename -m1 '^# (.*)' -r '$1' theory/ --glob '*.md' --glob '!*.brief.md'` filtered by `rg -i "oracle|verif|direct update|gate|gradient|bitter|self-improv|selection|parametric|weights|search|exact|evaluat|signal|reward|domain knowledge|general"`. Flagged: Oracle strength spectrum; Self-improving system; The self-improving-system definition classifies its boundary cases; The bitter lesson selects production methods, not representational forms; The Bitter Lesson defense portfolio...; The boundary of automation is the boundary of verification; Checks for the selection-based-learning definition; Error correction works with above-chance oracles; False-positive generation is filtered...; Real self-improving systems occupy combinations no single rung captures; Quality signals for KB evaluation. The paths were resolved with `rg -l -F -x '# <title>'` and their descriptions read.

**Body search:**
- `rg -l -i "alphazero|alpha ?go|self-play|monte.carlo|stockfish|mcts"` over theory, sources, agentic-systems, agent-memory-systems and articles. Theory hits: selection-based-learning, reflection-buys-addressability and bootstrap-bitter-lesson (all known), plus quality-signals-for-kb-evaluation (new). Source hits: faster-sorting-algorithms-discovered-using-deep-rl, alphadev-2026-09-08 (known), slate, sutton-javed, envharness, spade, wikipedia-bitter-lesson and model-discovery-agent. Agent-memory-systems hits: agent-r, trace-learning-techniques and systems-table. Agentic-systems: none. Articles: the lead article.
- `rg -n -i` on the same pattern, used to read the matching lines. Kept from this pass: sutton-javed line 37 ("we can do AlphaGo because the games, we know the model"), agent-r (MCTS trees distilled into weights), and quality-signals line 14 ("AlphaGo works because the game has a perfect verifier"). Slate's AlphaZero analogy (lines 48, 64), envharness and model-discovery-agent are incidental mentions.
- `rg -n -i "direct.update|gradient|self-play|go|chess|gate"` in the omitted-loop note. Line 12 says "A direct update exposes no separate candidate–adoption decision, so adding a reject-capable gate would introduce proposal selection rather than fill an omitted universal function". Its direct-update example is Continual Harness only.
- `rg -n -i "chess|game|go\b|exact|hard oracle|perfect"` in oracle-strength-spectrum. It defines the hard oracle as "exact, cheap, deterministic check". Open question at line 63: "Does oracle strength predict bitter-lessoning, or only govern it?"
- `rg -n -i "update architecture|direct update"` in the self-improving-system definition. Line 36: "A gradient step may be direct while a checkpoint-release gate around it uses proposal selection".
- `rg -n -i "alpha|exact|direct update"` in selection-based-learning-checks. Case 5 (deploy gate vs gradient steps) and case 14 (Huxley-Gödel Machine) are its level-named direct-update cases. No AlphaZero case exists.
- `rg -l -i "reinforcement learning|exact oracle|game rules|perfect verifier"` over agentic-systems, reference and tags. Only a retained-archive Reflexion run result matched, and it is not relevant.

**Link following:**
- From the omitted-loop note's footer to the self-improving-system definition and the real-self-improving-systems casebook. The casebook's "Parametric self-improvers" row is generic. AlphaZero would be a named instance, but the casebook adds nothing the definition and omitted-loop note do not already carry.
- From the oracle-strength-spectrum to error-correction and quality-signals. Quality-signals cites AlphaGo's perfect verifier with no source link.
- From the AlphaDev ingest (known) to the second AlphaDev ingest, `faster-sorting-algorithms-discovered-using-deep-rl.ingest.md`. It has the same `source` URL and a different snapshot.

### Candidate origins

- kb/theory/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md — curated-head, titles, body-search
- kb/theory/definitions/self-improving-system.md — titles, link-following, body-search
- kb/theory/oracle-strength-spectrum.md — titles, link-following
- kb/theory/definitions/selection-based-learning-checks.md — titles, body-search
- kb/sources/sutton-javed-why-ai-models-stop-learning.ingest.md — body-search
- kb/sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md — body-search
- kb/agent-memory-systems/reviews/agent-r.md — body-search
- kb/sources/alphadev-faster-sorting-2026-09-08.ingest.md — known
- kb/sources/sutton-the-bitter-lesson-original-essay.ingest.md — known
- kb/theory/quality-signals-for-kb-evaluation.md — body-search, link-following
- kb/articles/selection-based-learning-without-a-value-function.md — body-search

## Connections Found

- [An omitted improvement-loop function and a frozen one need different repairs](../../../../theory/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) -- **is-evidence-for**: AlphaZero is a documented case of a system that removed a reject-capable gate (AlphaGo Zero's 55% match) and became a network-level direct update. It therefore bears on the note's claim that a direct update's lack of a gate is architectural, not an omission. It bounds the claim rather than corroborating it, because the paper does not show whether removing the gate cost anything. The note's only direct-update example now is Continual Harness, so AlphaZero would be a clean, well-known second one.
- [Self-improving system](../../../../theory/definitions/self-improving-system.md) -- **defined-in**: the ingest uses "direct update" and names levels ("network level", "move level") without linking the definition. The definition says update architecture attaches to "a named pathway, target aspect, and granularity" and that "a gradient step may be direct while a checkpoint-release gate around it uses proposal selection". That is exactly the AlphaGo Zero vs AlphaZero contrast.
- [Oracle strength spectrum](../../../../theory/oracle-strength-spectrum.md) -- **is-evidence-for**: game rules that score every terminal position exactly are a hard oracle in the note's sense. AlphaZero is the limiting case where a pure learned method beat handcrafted proxy theories under such an oracle. This bears on the open question "Does oracle strength predict bitter-lessoning, or only govern it?" The ingest's Extractable Value item 6 (an exact oracle as the condition for gate-free learning) is a conjecture that would extend the note. The paper does not vary oracle strength, so the link records a bound, not corroboration.
- [Checks for the selection-based-learning definition](../../../../theory/definitions/selection-based-learning-checks.md) -- **is-evidence-for**: the ingest's Learning Claims section names levels for AlphaZero: the network level is a direct update, and move-level search reaches the weights only as a gradient target. That is a ready check case beside case 5 (gradient steps vs deploy gate) and case 14 (Huxley-Gödel Machine). It tests whether the definition's own lead example classifies cleanly under its checks.
- [Ingest: Sutton and Javed on why AI models stop learning](../../../../sources/sutton-javed-why-ai-models-stop-learning.ingest.md) -- **compares-with**: compare on whether the environment model is supplied. Sutton says "we can do AlphaGo because the games, we know the model", and AlphaZero is that case with the rules supplied exactly. Read together, they mark where the AlphaZero recipe stops: domains where no rules-based simulator is given, which the ingest's Limitations already flags as untested.
- [Ingest: SPADE: Self-Play in Adaptive Synthetic Executable Environments](../../../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) -- **compares-with**: compare on the source of the self-play environment and its scoring. AlphaZero's environment and oracle are fixed and exact game rules. SPADE generates and filters executable environments with validity and learning-value checks. The pair separates self-play against a supplied exact oracle from self-play whose environments must themselves be selected.
- [Agent-R](../../../../agent-memory-systems/reviews/agent-r.md) -- **compares-with**: compare on how MCTS output reaches the weights. Both distill tree-search results into a parametric learner. AlphaZero's targets are the visit distribution and an exact game outcome. Agent-R's are value-thresholded paths, scored by environment reward and an LLM verifier, then fine-tuned offline in staged checkpoints. The axis is oracle exactness and the online vs staged update.

## Bidirectional Candidates

- [Ingest: AlphaDev (2026-09-08)](../../../../sources/alphadev-faster-sorting-2026-09-08.ingest.md) <-> source -- **compares-with**: the forward link already exists. AlphaDev's ingest quotes "an extension of the AlphaZero agent" but has no tracked AlphaZero ingest to link. A return link would let a reader of AlphaDev reach the generic learner's primary description and keep it separate from AlphaDev's correctness-and-latency scoring.
- [Ingest: Sutton, The Bitter Lesson (original essay)](../../../../sources/sutton-the-bitter-lesson-original-essay.ingest.md) <-> source -- **compares-with**: the forward link already exists. The essay ingest generalizes over chess and Go, and AlphaZero is the strongest single post-essay-style chess case. A return link gives essay readers one concrete, unablated contrast within one system.

## Reverse-edge Candidates

- [Selection-based learning](../../../../theory/definitions/selection-based-learning.md) → source -- **evidenced-by** (theory contract): replace the bare arXiv URL in the AlphaZero sentence with this ingest. The context phrase should say that the source documents removing the gate and does not test its effect. Grounding needs the continual-update quote retained first, which is the ingest's own Recommended Next Action (cp-skill-ground).
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → source -- **evidenced-by**: a boundary case with named levels. The network level is a direct update after the gate was removed. At the move level, search choice reaches retention only as a gradient target.
- [Selection-based learning without a value function (lead article)](../../../../articles/selection-based-learning-without-a-value-function.md) → source -- **evidenced-by** (articles contract, `kb/sources/` row): the article cites AlphaZero with the bare arXiv URL at line 119. Under the articles contract this would be an in-prose link to the ingest, not a footer label.
- [Quality signals for KB evaluation](../../../../theory/quality-signals-for-kb-evaluation.md) → source -- **evidenced-by**: its analogy "AlphaGo works because the game has a perfect verifier" has no source. This ingest documents the perfect-verifier condition for the AlphaZero successor: exact terminal scoring by the rules, with the outcome as the only training signal. The link would bound the analogy, not corroborate the brainstorm.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [The self-improving-system definition classifies its boundary cases](../../../../theory/the-self-improving-system-definition-classifies-its-boundary-cases.md) -- its gradient-based learning row is generic. AlphaZero adds nothing there beyond what the definition and the omitted-loop note carry.
- [Real self-improving systems occupy combinations no single rung captures](../../../../theory/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) -- its "Parametric self-improvers" row would take AlphaZero as an instance, but the source supports no new placement field.
- [The bitter lesson selects production methods, not representational forms](../../../../theory/the-bitter-lesson-selects-production-methods-not-representational.md) -- AlphaZero changes both production method (learned instead of handcrafted) and form (parametric instead of linear features) at once, so it cannot separate the note's two axes. The existing bitter-lesson links already cover the case.
- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -- topically adjacent, but oracle-strength-spectrum is the sharper target for the exact-oracle point.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../theory/false-positive-generation-is-filtered-before-retention.md) -- it concerns proposal-selection acceptance errors. AlphaZero has no network-level acceptance step, and the paper reports nothing about bad updates becoming operative.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- its "distributed-parametric learning under a sufficiently strong oracle" branch fits, but it surveys deploy-time trace mining. Agent-R is the closer, system-level comparison.
- [Ingest: Slate](../../../../sources/slate-moving-beyond-react-and-rlm.ingest.md) -- it uses AlphaZero only as a strategy/tactics analogy, which that ingest itself judges does not transfer.
- [Ingest: Wikipedia, Bitter Lesson](../../../../sources/wikipedia-bitter-lesson.ingest.md) -- it duplicates the Sutton essay comparison at lower authority.
- [Ingest: Faster sorting algorithms (AlphaDev, 2026-08-29)](../../../../sources/faster-sorting-algorithms-discovered-using-deep-rl.ingest.md) -- it is the same paper as the already-linked 2026-09-08 ingest. One AlphaDev link is enough.

## Index Membership

None. Sources are outside the tag-participating collections, so the improvement-loop and learning-theory heads list no sources. The source's own `tags:` already gives source-scoped search.

## Synthesis Opportunities

Taken together, the source's Learning Claims, the omitted-loop note, the oracle strength spectrum and SPADE suggest a higher-order claim. The stronger and more exact the training signal, the less a reject-capable gate adds over a direct update. Where the signal is weaker, selection moves outward: to environment or candidate validity checks (SPADE) or to release gates (selection-based-learning-checks case 5). No artifact states this. One exact-oracle case cannot support it, so the ingest's Extractable Value item 6 is the right place to hold it for now.

## Maintenance Observations

- Two tracked ingests share `source: https://www.nature.com/articles/s41586-023-06004-9`: `faster-sorting-algorithms-discovered-using-deep-rl.ingest.md` (2026-08-29) and `alphadev-faster-sorting-2026-09-08.ingest.md`. They have different snapshot checksums and occasions, so this may be a sanctioned second observation, but inbound links divide between them. Worth a triage decision on which one a citing note should use.
- The selection-based-learning definition, the lead article and quality-signals-for-kb-evaluation all cite AlphaZero or AlphaGo with bare URLs or no source. With this ingest available, they are grounding gaps rather than missing sources.

## Flags

- Split candidate check: the source connects to more than five notes across selection-based learning, bitter lesson and oracle theory. It is an ingest report, not a claim note, and its multiple roles are intended, so no split is recommended.
- Tension, carried from the source, not resolved here: the [unearned-reach note](../../../../theory/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) classifies the chess example as extension inside alpha-beta search. AlphaZero replaced the search as well, and the paper cannot isolate search from evaluator.
