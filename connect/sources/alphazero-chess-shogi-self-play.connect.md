---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/alphazero-chess-shogi-self-play.md"
source_has_frontmatter: true
date: "2026-11-22"
depth: standard
---

# Connection Report: Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm

**Source:** Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (snapshot `kb/sources/.snapshots/alphazero-chess-shogi-self-play.md`; not linked because snapshots are ignored and the paired ingest does not exist yet)

The source is an immutable snapshot. Under the sources `COLLECTION.md`, outbound edges belong on its authored surface, the matching ingest `kb/sources/alphazero-chess-shogi-self-play.ingest.md`, which did not exist when this report was written. Every candidate in `Connections Found` is a recommendation for that ingest.

Source claims used for judging candidates:
- One generic algorithm (policy/value network plus general MCTS, trained by self-play from random weights) reaches superhuman chess, shogi and Go within 24 hours, given no domain knowledge beyond the game rules and a rules-based board/action encoding.
- It replaces Stockfish/Elmo's handcrafted evaluation and alpha-beta heuristics; it searches about 1000x fewer positions and scales better with thinking time.
- Hyperparameters are shared across games; the only per-game adjustment is exploration noise scaled to the typical number of legal moves.
- Unlike AlphaGo Zero, it drops the 55% evaluation gate and best-player selection: a single network is updated continually.
- The terminal position is scored by the game rules (-1/0/+1), which is the only training signal.
- AlphaZero independently discovers and frequently plays the common human chess openings.

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, section "Outbound links". Authorised destinations: `kb/theory/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/tags/`, other sources. Excluded: `kb/work/`, `kb/instructions/`. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). No label row names `kb/tags/`, so tag heads are treated as tag/index suggestions only. External prospecting skipped (no web search); the arXiv URL is the snapshot's own `source` and belongs on the ingest as `derived-from`.

**Repo-wide first pass:**
- `rg -il "alphazero|alphago|alpha-?zero|self-play|selfplay" kb --glob '*.md' --glob '!kb/work/**'` -- surfaced `kb/theory/definitions/selection-based-learning.md`, `kb/articles/selection-based-learning-without-a-value-function.md`, `kb/theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md`, `kb/theory/reflection-buys-addressability.md`, `kb/theory/quality-signals-for-kb-evaluation.md`, and source ingests (wikipedia-bitter-lesson, sutton-javed, spade, slate, both AlphaDev ingests, envharness, sutskevers-list chapters).
- `rg -n -i "alphazero|alphago|self-play" kb --glob '*.md' --glob '!kb/work/**'` -- read hit lines. The definition and the article both cite `https://arxiv.org/abs/1712.01815` for "AlphaZero dropped that step and updated a single network continually". This is the paper in this snapshot, so the definition and article are the strongest reverse-edge candidates.

**theory (curated heads + titles):**
- Tag heads `kb/tags/self-improving-systems-README.md`, `learning-theory-README.md`, `improvement-loop-README.md`, `continual-learning-README.md` -- all declare `complete: true`; by-tag rg skipped for each. Read inclusion conditions only, to judge tag suggestions for the ingest.
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'` filtered with `rg -i "bitter|self-improv|oracle|verif|search|learn|selection|reinforcement|reward|generality|general|domain knowledge|handcraft|bootstrap|evaluat|scal|compute|tabula|explor|proposal|gate|continual|weights|parametric"` -- about 85 titles. Kept for reading: codification-and-relaxing, the bitter-lesson-selects-production-methods note, the unearned-reach note, the bootstrap note, the boundary-of-automation note, oracle-strength-spectrum, warranted-autonomy, the proposal-selection loop note, the search-controller note, the scaling-absorbs-scaffolding note, quality-signals, self-improvement-is-relative-to-a-declared-objective, the self-improving-system definition.
- Resolved paths and descriptions with `rg -l -F -x '# <title>' kb/theory/` plus `rg -m1 '^description:'`.

**Body search:**
- `rg -n -i "chess|stockfish|deep blue|\bgo\b game|game of go|tabula rasa|handcrafted|hand-crafted evaluation|perfect verifier|game rules|monte.carlo|MCTS|alpha-beta" kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags kb/sources --glob '*.md'` -- new theory hits: `machinery-persists-by-warrant-not-position-in-a-reflective-loop.md` (Deep Blue alpha-beta as fixed machinery) and `bitter-lesson-selects-against-unearned-reach-not-against-structure.md` (chess-engine evaluation as an extension case). The `agent-r` review and trace-learning survey hit only on MCTS.
- `rg -n -i "game|chess|go\b|self-play|alpha|deep blue|tree search"` over the codification, production-methods, boundary-of-automation, warranted-autonomy, oracle-strength, proposal-selection, self-improving-system and declared-objective notes -- no game cases. Only a FunSearch instance in the production-methods note and a "Kephart and Chess" false positive.
- Read the bodies of `codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` (exact-spec vs proxy-theory regimes), `bitter-lesson-selects-against-unearned-reach-not-against-structure.md` (agreement/extension/replacement), `machinery-persists-by-warrant-not-position-in-a-reflective-loop.md` (fixed general machinery, learned task content), `reflection-buys-addressability.md` (self-play policy as a cumulative but opaque learner), `a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md` (self-play named as an alternative), and `definitions/selection-based-learning.md`.

**sources:**
- `rg -N --no-heading '^description:' kb/sources --glob '*.ingest.md' -r '' | rg -i "muzero|bitter|self-play|reinforcement|scal.*compute|search and learn|rich sutton|tree search|game"` -- surfaced `sutton-the-bitter-lesson-original-essay.ingest.md` (not hit by the AlphaZero query), both AlphaDev ingests, wikipedia-bitter-lesson, voooooogel-multi-agent-future, self-modifying-policies, reflexion, continual-harness, agent-plasticity, the falsifybench pair, and next-generation-agentic-RL.
- `rg -n -i "chess|go\b|self-play|search"` over the Sutton essay ingest -- the essay generalizes over chess and Go. AlphaZero, published before the essay, is the sharpest single instance of its contrast.
- `rg -n -i "alphazero|game|alphago"` over both AlphaDev ingests -- both describe AlphaDev as AlphaZero-derived. `alphadev-faster-sorting-2026-09-08.ingest.md` retains the quote "an extension of the AlphaZero agent".

**reference, agentic-systems, agent-memory-systems:**
- `rg -l -i "self-play|tabula rasa|alphazero|alphago|monte.carlo tree|game outcome" kb/reference kb/agentic-systems kb/agent-memory-systems --glob '*.md'` -- no files.
- `rg -n -i "reinforcement learning|parametric learner|weight update" kb/reference --glob '*.md'` -- no hits. No candidates in these destinations; the `agent-r` MCTS hits are keyword-only.

**Link following:**
- From `definitions/selection-based-learning.md` to `a-proposal-selection-loop-requires-search-evaluation-and-retention.md`. The AlphaGo Zero to AlphaZero change (gate dropped) is a boundary case between a proposal-selection loop and a direct update at the network level. Kept.
- From the unearned-reach note to `codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` and `warranted-autonomy-is-bounded-by-oracle-domain.md`. Both kept.
- From `machinery-persists-by-warrant-...` to `the-bitter-lesson-selects-production-methods-not-representational.md`. Read; AlphaZero adds nothing to its form axis beyond what the Sutton essay already anchors. Rejected.

### Candidate origins

- kb/theory/definitions/selection-based-learning.md — body-search
- kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md — titles, link-following
- kb/theory/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md — body-search
- kb/theory/bitter-lesson-selects-against-unearned-reach-not-against-structure.md — titles, body-search
- kb/theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md — titles, link-following
- kb/theory/reflection-buys-addressability.md — body-search
- kb/theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md — body-search, titles
- kb/theory/warranted-autonomy-is-bounded-by-oracle-domain.md — titles, link-following
- kb/sources/sutton-the-bitter-lesson-original-essay.ingest.md — descriptions, body-search
- kb/sources/alphadev-faster-sorting-2026-09-08.ingest.md — body-search, descriptions
- kb/articles/selection-based-learning-without-a-value-function.md — body-search

## Connections Found

All of these are proposed for the future ingest `kb/sources/alphazero-chess-shogi-self-play.ingest.md`.

- [Selection-based learning](../../../../theory/definitions/selection-based-learning.md) -- **is-evidence-for**: the paper is the primary statement of the example the definition uses. AlphaGo Zero replaced its best player only after a 55% win margin; AlphaZero "simply maintains a single neural network that is updated continually". It also carries the game outcome as the single measure for move selection. The ingest should quote that passage, because the definition's AlphaZero sentence currently rests on an external URL.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- **is-evidence-for**: AlphaZero shows both regimes in one system. The game rules, which define the task, stay supplied ("no domain knowledge except the rules of the game"). The handcrafted evaluation and alpha-beta enhancements, which only approximate good play, are relaxed into a learned network and general MCTS. That is the note's exact-spec vs proxy-theory split in a clean case.
- [Machinery persists by warrant, not position, in a reflective loop](../../../../theory/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) -- **is-evidence-for**: the note's test asks whether fixed machinery implements a general production method or supplies task-specific competence. AlphaZero keeps fixed human-designed machinery (MCTS, network architecture, shared hyperparameters) while all chess and shogi competence is learned. The one per-game residue, exploration noise scaled to legal-move count, is a small concrete case to test the note against.
- [The bitter lesson selects against unearned reach, not against structure](../../../../theory/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- **is-evidence-for**: AlphaZero independently rediscovered the common human chess openings (Table 2), which is the note's "agreement" outcome. Its displacement of Stockfish's evaluation is a candidate "extension" case. Its replacement of alpha-beta search itself, which the paper says calls into question the belief that alpha-beta is "inherently superior", is a test case for whether the note's chess-engine example classifies correctly.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: AlphaGo Zero to AlphaZero is a documented move from reject-capable network evaluation to continual direct update. It is a boundary case where the loop's evaluation step was removed at one level while move-level selection by game outcome stayed.
- [Reflection buys addressability](../../../../theory/reflection-buys-addressability.md) -- **is-evidence-for**: the note's central non-reflective case is "a policy improved by self-play". AlphaZero is the canonical instance. Its continually updated single network makes the "retained weights are inputs to the next update" pathway literal, and nothing in it states what an update claims.
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- **compares-with**: on the axis of how much hand-supplied starting knowledge the learner needs. AlphaZero starts from random weights with only rules and encoding, the limiting case of the self-play alternative the note names in "This is not a uniqueness claim". It also shows that feature encoding "based only on the basic rules" is itself a small supplied bootstrap.
- [Warranted autonomy is bounded by oracle domain](../../../../theory/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **is-evidence-for**: AlphaZero trains without human evaluation because the rules score every terminal position exactly (-1/0/+1), so every candidate falls inside the oracle's domain. This is a bounding case at the strong-oracle end, not corroboration of the bound itself; the context phrase should say so.
- [Ingest: Sutton, The Bitter Lesson (original essay)](../../../../sources/sutton-the-bitter-lesson-original-essay.ingest.md) -- **compares-with**: on the axis of general search and learning vs hand-built domain knowledge in chess and Go. The essay argues from selected histories. AlphaZero is a controlled within-paper contrast against Stockfish and Elmo, with search-count and thinking-time scaling data.
- [Ingest: AlphaDev faster sorting (2026-09-08)](../../../../sources/alphadev-faster-sorting-2026-09-08.ingest.md) -- **compares-with**: on the axis of what the AlphaZero recipe needs from its environment. AlphaDev reuses the AlphaZero agent with a correctness-plus-latency oracle standing in for game rules. The pair separates the generic learner from the domain's scoring function.

## Bidirectional Candidates

- [Ingest: AlphaDev faster sorting (2026-09-08)](../../../../sources/alphadev-faster-sorting-2026-09-08.ingest.md) <-> source -- **compares-with**: AlphaDev quotes "an extension of the AlphaZero agent" but has no tracked ingest to point to for that ancestor. A return link lets its readers reach the base algorithm's analysis.
- [Ingest: Sutton, The Bitter Lesson (original essay)](../../../../sources/sutton-the-bitter-lesson-original-essay.ingest.md) <-> source -- **compares-with**: the essay's limitations section says its examples are selected success stories. A return link to a primary paper for one of those examples gives readers the controlled case.

## Reverse-edge Candidates

- [Selection-based learning](../../../../theory/definitions/selection-based-learning.md) → source ingest -- **evidenced-by** (theory→sources): the definition's sentence "AlphaZero dropped that step and updated a single network continually" links only the arXiv URL. Under the theory contract, source-dependent claims should link the tracked ingest so the grounding gate can check the claim against retained quotes. The AlphaGo Zero half cites a different paper (Nature 2017), which this ingest does not cover. The context phrase should say the source bounds the example rather than corroborates the definition.
- [Selection-based learning without a value function](../../../../articles/selection-based-learning-without-a-value-function.md) → source ingest -- **evidenced-by** (articles→sources, in-prose): the article repeats the same AlphaZero claim with the arXiv link. The articles contract authorizes linking the captured source analysis for an externally attributed empirical claim.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) → source ingest -- **evidenced-by**: the note's examples are vision, edge detection and FlashAttention. AlphaZero is a case where the task-defining spec (rules) was kept and the proxy decomposition (evaluation, search heuristics) was relaxed. The note could cite it if it adds a game-playing example.
- [Machinery persists by warrant, not position, in a reflective loop](../../../../theory/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) → source ingest -- **evidenced-by**: the note cites "Deep Blue's alpha-beta search" as fixed machinery. AlphaZero is the case where that machinery itself was replaced by a more general search. This qualifies the example: fixed general machinery persists only until a more general method displaces it.

## Off-authorisation Candidates

- [Selection-based learning without a value function](../../../../articles/selection-based-learning-without-a-value-function.md) -- the article uses this paper as a primary example, but `kb/articles/` is not an authorised destination for sources outbound links. Keep it as the reverse edge above; no extension recommended, since articles are reader-facing endpoints.

## Raw Text Candidates

None

## Rejected Candidates

- [The bitter lesson selects production methods, not representational forms](../../../../theory/the-bitter-lesson-selects-production-methods-not-representational.md) -- AlphaZero is learned-parametric, so it adds no evidence on the note's form axis. The Sutton essay ingest already anchors the production-method contrast.
- [Quality signals for KB evaluation](../../../../theory/quality-signals-for-kb-evaluation.md) -- mentions "AlphaGo works because the game has a perfect verifier" only as motivation; the note catalogues KB signals. Warranted-autonomy carries the oracle point better.
- [Oracle strength spectrum](../../../../theory/oracle-strength-spectrum.md) and [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -- topically adjacent (games have exact oracles), but neither discusses game play. One oracle link (warranted-autonomy) is enough.
- [Ingest: Faster sorting algorithms discovered using deep RL](../../../../sources/faster-sorting-algorithms-discovered-using-deep-rl.ingest.md) -- the same paper as the kept AlphaDev ingest, at an earlier observation. One AlphaDev link suffices; the 2026-09-08 observation retains the AlphaZero-lineage quote.
- [Ingest: Wikipedia, Bitter lesson](../../../../sources/wikipedia-bitter-lesson.ingest.md) -- a secondary summary of the essay; the original-essay ingest is the better comparison target.
- [Ingest: SPADE](../../../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) -- "self-play" names a different mechanism (adaptive environment generation for LLM agents). Keyword overlap only.
- [Ingest: Slate](../../../../sources/slate-moving-beyond-react-and-rlm.ingest.md) -- uses AlphaZero's value/policy split only as an analogy, which its own ingest judges not to transfer. Linking from AlphaZero adds nothing.
- [Ingest: Sutton and Javed, why AI models stop learning](../../../../sources/sutton-javed-why-ai-models-stop-learning.ingest.md) -- mentions AlphaGo in passing ("we can do AlphaGo because the games, we know..."); its subject is continual weight learning. Too weak.
- [Agent-R review](../../../../agent-memory-systems/reviews/agent-r.md) -- MCTS keyword match only; trace collection for fine-tuning is a different mechanism.
- [Self-improving system](../../../../theory/definitions/self-improving-system.md) and [Self-improvement is relative to a declared objective](../../../../theory/self-improvement-is-relative-to-a-declared-objective.md) -- AlphaZero would be a routine positive case; neither note's argument turns on it.

## Index Membership

- [improvement-loop tag head](../../../../tags/improvement-loop-README.md) -- suggest `tags: [improvement-loop]` on the ingest. The source substantively documents the boundary between reject-capable selection (AlphaGo Zero's gate) and continual direct update (AlphaZero), which the head's inclusion condition names. Source tags do not affect generated listings.
- [learning-theory tag head](../../../../tags/learning-theory-README.md) -- suggest `tags: [learning-theory]` if the ingest's analysis centres on what is learned vs supplied (rules vs evaluation). Skip it if the analysis centres only on the selection boundary.

## Synthesis Opportunities

The codification-and-relaxing note, the machinery-persists note and the unearned-reach note each classify one part of a superseded game engine: evaluation terms (extension), alpha-beta search (machinery) and rules (exact spec). AlphaZero replaced the first two and kept the third in one system. Read together, they suggest a claim about which layer of a hand-built system scale displaces, and in what order: proxy content first, then the general machinery around it, while the task-defining spec stays. No current note states that ordering. A future writer would need more than this one case.

## Maintenance Observations

- `kb/theory/definitions/selection-based-learning.md` and `kb/articles/selection-based-learning-without-a-value-function.md` state a source-dependent empirical claim about AlphaZero with only an external URL. Once the ingest exists with a quote for the continual-update passage, both can be grounded through it.
- Two tracked ingests cover the same AlphaDev paper (`faster-sorting-algorithms-discovered-using-deep-rl.ingest.md`, captured 2026-08-29; `alphadev-faster-sorting-2026-09-08.ingest.md`, captured 2026-09-08) with distinct checksums. This may be intended (distinct observations), but connect runs on AlphaZero-lineage sources must choose between them.

## Flags

- The ingest that should carry these edges does not yet exist. Rerun or re-check candidates against its final analysis if its focus differs from the claims listed at the top of this report.
- This snapshot is arXiv v1 (2017). From memory, not from the KB: a later peer-reviewed version (Science, 2018) re-ran the matches under revised conditions. The ingest should scope comparative-strength and scaling claims to this preprint.
- Tension to record, not resolve: the unearned-reach note calls the chess-engine evaluation's displacement an "extension" inside the same alpha-beta search. AlphaZero displaced the search too. Whether that is extension or replacement of the search-superiority belief is open.
