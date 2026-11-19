---
description: "Discovery report for possible KB connections from Pol Alvarez Vecino's practitioner argument about tacit program theory and code simplification"
type: kb/cache/types/connect-report.md
source: kb/sources/why-llms-cant-make-your-code-simpler.md
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: Why LLMs can’t make your code simpler

**Source:** [Why LLMs can’t make your code simpler](../../../sources/why-llms-cant-make-your-code-simpler.md)

## Discovery Trace

**Description listing scan:**
- `rg "^description:" kb/notes/ kb/reference/ kb/instructions/ --glob "*.md"` and equivalent scoped scans over `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` surfaced the selection-asymmetry, future-change, maintainability-oracle, rationale-retention, and external-system comparison clusters. The strongest candidates were [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md), [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md), [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md), [On the Criteria To Be Used in Decomposing Systems into Modules](../../../sources/parnas-1972-criteria-decomposing-systems-modules.md), and [Why Software Factories Fail](../../../../sources/why-software-factories-fail-2080697380379427275.ingest.md).
- Full H1/title surfaces for those collections were also scanned. No agent-memory-system or agentic-system artifact described a sufficiently close implemented system to retain as a connection.

**Topic indexes:**
- Read the curated heads at `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source is evidence for theoretical and evaluation questions, not an external-system review or an index placement.
- Read the source and notes collection contracts. Source-side candidates below use `is-evidence-for` or `compares-with`; note-side return links use the notes collection's `evidenced-by` relation.

**Body search:**
- `rg -n -i --glob '*.md' 'Peter Naur|Programming as Theory|program theory|Theory complexity' kb/notes` — found no prior note that directly adopts Naur's theory-building vocabulary.
- `rg -n -i --glob '*.md' 'tacit knowledge|tacit understanding|lives in people|where understanding lives' kb/notes` — surfaced the explicit-retention and specification-strategy cluster, but the source does not establish those notes' broader claims.
- `rg -n --pcre2 --glob '*.md' 'code complexity|cyclomatic|Halstead|maintainability|lines of code|(?<![[:alnum:]_])LoC(?![[:alnum:]_])' kb/notes` — surfaced the maintainability-oracle and weak-discrimination notes. The weak-discrimination connection was retained as a bounded mechanism-level case: the source contrasts a strongly measurable code-shape proxy with future-change-relative maintainability, while supplying no prevalence or enrichment evidence for the note's statistical conjecture.
- `rg -n -i --glob '*.md' 'weakly discriminated|underselect|selection pressure|training signal|reward model|reinforcement learning|RL training|preference optimization' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources` — confirmed that the article explicitly proposes RL complexity penalties and that the underselection note permits propagation through later training signals. Following the note's proposal-selection definition exposed a boundary: preference filtering, rejection sampling, and other reject-capable candidate stages fit directly, while a direct gradient update without candidate non-adoption does not.
- `rg -n -i --glob '*.md' 'business priorities|expected product changes|operational constraints|design rationale|future change distribution|changing requirements' kb/notes` — confirmed that the source's provider and billing examples instantiate the future-change-relative target in the maintainability-oracle note and the rationale boundary in the local-decomposition note.
- `rg -n -i --glob '*.md' 'abstraction layer|hidden complexity|external abstraction|API contract|managed service|dependency.*complex|complex.*dependency' kb/notes` — found adjacent abstraction and dependency discussions, but none with a more useful traversal path than the retained maintainability candidates.
- `rg -n -i --glob '*.md' 'maintainability|cyclomatic|Halstead|future change|design decisions likely to change|duplication.*abstraction|abstraction.*duplication' kb/sources` — surfaced Parnas and the three-part Why Software Factories Fail series. Parnas and Part I were kept because they supply distinct comparison bases: change-oriented modularization and delayed maintainability verification.
- `rg -n -i --glob '*.md' 'tacit knowledge|human expertise|design rationale|why-memory|engineering decisions' kb/agent-memory-systems` and the corresponding agentic-system scan found only weak system-level matches; none was retained.

**Link following:**
- Followed the maintainability-oracle note to its future-change target, static-proxy caveat, synthetic-futures experiment, and Why Software Factories sources. The new article supplies a concrete opposite-ranking example for code-shape metrics, but no calibrated maintainability oracle.
- Followed the weak-discrimination note to [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). The article supplies a plausible selection-asymmetry mechanism at code review and selection-shaped training stages, but its discussion of generic RL penalties does not by itself establish the reject-capable loop the registered term requires.
- Followed the local-decomposition note to Parnas and Commonplace's rationale-management description. Parnas gives the stronger comparison: two workable structures are distinguished by anticipated changes, while the Commonplace reference only describes this repository's rationale surfaces.
- Followed the Why Software Factories Part I ingest and its oracle-gap framing. That source concerns delayed feedback after unattended generation; this article adds a different obstacle, namely that the relevant objective variables may remain in team history and business priorities rather than in the code or evaluator input.
- External prospecting was skipped. The supplied URL is already the source being connected, and the local graph contained stronger, fully captured comparison targets.

## Connections Found

- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) — **is-evidence-for**: the source gives a constructed preference reversal and practitioner account consistent with candidates varying in correctness and future change cost while tests or static metrics discriminate the former and its surface proxies more reliably. At selection-shaped training stages, retaining those preferences in data or weights can propagate the asymmetry; the source illustrates the mechanism but does not supply the representative enrichment evidence needed to test the note's statistical conjecture.
- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) — **is-evidence-for**: the provider split and Answer.AI billing redesign are practitioner cases in which the preferable code shape depends on a declared future-change distribution and business objective, so lower lines of code, duplication, or cyclomatic complexity cannot determine the maintainability ranking by themselves.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — **is-evidence-for**: the reported credits-only architecture worked for Answer.AI after a product-scope trade-off, while the article's own account shows that the result depends on local priorities, Stripe behavior, and rejected alternatives; it is evidence of local sufficiency and rationale value, not of the design's transferability.
- [On the Criteria To Be Used in Decomposing Systems into Modules](../../../sources/parnas-1972-criteria-decomposing-systems-modules.md) — **compares-with**: Parnas distinguishes two runnable decompositions by the design decisions likely to change; Alvarez Vecino makes the same change-relative distinction through provider removal and billing-service examples, then extends it to LLM judgment and business context.
- [Why Software Factories Fail](../../../../sources/why-software-factories-fail-2080697380379427275.ingest.md) — **compares-with**: Horthy explains maintainability failure as a delayed-oracle problem in unattended coding, whereas this article argues that even immediate structural metrics can target the wrong thing when the expected changes and trade-off policy are absent from the evaluator's evidence.

## Bidirectional Candidates

- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) <-> source — **evidenced-by**: a bounded return link would supply a current practitioner illustration of why maintainability may receive less selection pressure than correctness, while explicitly withholding prevalence warrant and distinguishing selection-shaped training from direct gradient updates.
- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) <-> source — **evidenced-by**: a return link would give the exploratory note a compact practitioner witness for its claim that maintainability is relational to future changes and that static proxies need target-alignment tests.

## Reverse-edge Candidates

- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) → source — **evidenced-by**: the billing redesign is a current practitioner case in which the working boundary is intelligible only with the team-specific forces and rejected alternatives, while one successful launch does not test transfer.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) — the article repeats Naur's claim that code and documentation incompletely transfer human understanding; it does not independently establish the note's full durability, writability, and addressability comparison, so a load-bearing evidence edge would overstate the source.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) — the source motivates retaining constraints, alternatives, and trade-offs in general, but it says nothing about Commonplace's shipped proposal, ADR, contract, or enforcement surfaces.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) — the source supports supplying known priorities as context and acknowledges that experience exposes new constraints, but it does not compare spec-first, bidirectional, and spec-mining strategies.

## Index Membership

None.

## Synthesis Opportunities

The source and the two oracle notes suggest a sharper account of code-complexity accumulation: correctness receives strong selection pressure from tests, while future-change-relative maintainability receives weak or misaligned pressure when the evaluator sees only code-shape proxies. An ADR can expose the expected change distribution and trade-off policy as process evidence, strengthening discrimination rather than serving as an inevitably incomplete substitute for human Theory. Training can teach the general policy of seeking and conditioning on that rationale, while runtime context supplies the project-specific record. This belongs as a bounded application of the existing weak-discrimination claim and its maintainability exploration, not as a new impossibility claim about LLMs.

## Maintenance Observations

None.

## Flags

- Fixed-decomposition audit: the team had access to implementation history, Stripe operations, launch feedback, discussions, and product priorities; the reported LLM received only an unspecified subset. The considered response set was also fixed to subscriptions, a dual system, or manual Indian top-ups, while Answer.AI's preference for low theory complexity, the candidate architectures, Stripe's constraints, and the decision to accept reduced Indian auto-top-up service stayed outside evaluation. The result therefore supports this configuration in this context; it does not validate the decomposition, exclude unconsidered designs, or establish the headline's categorical claim about LLM capability.
- Training-stage boundary: the article inspects no training corpus, preference data, reward model, candidate filtering, or weight update. Its mechanism applies directly to reject-capable selection stages whose operative oracle favors correctness over maintainability. Extending the same vocabulary to direct reward-gradient learning would require broadening the registered proposal-selection claim or naming a parallel unequal-optimization mechanism.
- The article treats weak model continual learning as a primary limit. [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) creates an unresolved boundary tension: a deployed agent system can retain explicit rationale and user feedback without changing model weights, although that does not fully transfer tacit expertise.
