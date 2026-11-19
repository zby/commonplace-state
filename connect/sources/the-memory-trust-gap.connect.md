---
description: "Connection candidates for The Memory Trust Gap's stale-evidence experiments and capability-dependent mitigation."
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/the-memory-trust-gap.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: The Memory Trust Gap

**Source:** [The Memory Trust Gap](../../../../sources/.snapshots/the-memory-trust-gap.md)

## Discovery Trace

- Read the source snapshot, sources collection outbound rules, and connect-report contract. The snapshot is immutable; candidates concern its prospective ingest.
- Read curated collection heads: `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`; additionally read `kb/notes/agent-memory-README.md`. The snapshot has no tags; no complete-tag skip applies.
- Generated the complete title surface once with `rg -N --no-heading -m1 '^# ' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`. Large combined output was truncated; the following focused description/body passes supplied the discriminating recall surface.
- Across all five destinations, ran `rg '^description:.*(stale|freshness|authority|supersed|conflict|pre-resolv|capability)' ... --glob '*.md'`. Notes yielded effects evaluation, temporal lifecycle, calibrated trust, and scaling candidates. Reference yielded the memory gap plan and freshness architecture. The former offers a bounded evaluation destination; the latter concerns review applicability, not truth adjudication.
- Ran `rg -n 'STALE|Trust Gap|deterministic.*adjudic|Reliable Post|post-retrieval|MemSyco' ... --glob '*.md'` over all five destinations. No existing ingest of this paper or its nearest named benchmark comparators appeared; a general memory survey mentioned post-retrieval processing but did not offer a closer comparison.
- Ran `rg -n -i 'stale|supersed|conflict' kb/agentic-systems/reviews --glob '*.md'`. Beads Rust cache invalidation and inherited-context delivery were operationally adjacent, but neither measures stale/current adjudication or capability interaction; no agentic-system edge retained.
- Ran `rg -n -i 'supersed|valid_at|invalid_at|temporal' kb/agent-memory-systems/reviews/graphiti.md kb/sources/graphiti-temporal-knowledge-graph.ingest.md`. Read the Graphiti review's temporal invalidation and read-back account and the source ingest; retained the stronger review and omitted the redundant ingest edge.
- Followed effects-evaluation and lifecycle links to the remembered-knowledge requirements, activation distinction, and Graphiti. Read the calibrated-trust note and end-to-end evaluation synthesis; selected the more specific trust and effects notes. Read the scaling/scaffolding and checked-copy notes to bound those possible transfers.
- External prospecting skipped. The supplied arXiv source is already known and is the only external candidate. No links to instructions or workshops are proposed.

## Connections Found

- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — **is-evidence-for**: the paper separately measures stale-value reliance and paired accuracy loss against a no-memory baseline. Its Benefit/Safety split shows why a baseline that lacks necessary evidence cannot measure the same harm as one with current authoritative evidence.
- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) — **is-evidence-for**: removing the stale item before consumption restores accuracy more fully than merely exposing metadata, supporting operative supersession rather than lifecycle labels alone. This is a consumption-time oracle intervention, not an evaluated production lifecycle.
- [Agent memory needs discoverable, loadable, composable, trusted knowledge](../../../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) — **is-evidence-for**: correctly parsed timestamps can increase reliance on wrong evidence; metadata presence and parsing competence do not establish calibrated trust. The result supplies a concrete failure case for the note's trust requirement.
- [Scaling absorbs scaffolding at fixed task difficulty](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — **compares-with**: the paper holds templated tasks fixed while changing checkpoint size and finds feature-specific vulnerability and mitigation. This qualifies any monotone expectation that stronger models need less external conflict resolution; it does not directly test moving deployment frontiers.
- [Graphiti](../../../../agent-memory-systems/reviews/graphiti.md) — **compares-with**: Graphiti implements validity windows, contradiction invalidation, and temporal filtering; the paper measures the downstream difference between exposing conflicting metadata and supplying a resolved representation. This suggests an evaluation axis for those operations, without attributing the paper's results to Graphiti.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) — **see-also**: the plan's lifecycle and behavioral-evaluation work can use paired stale/current perturbations to distinguish successful memory uptake from harmful reliance.
- [The Memory Trust Gap](https://arxiv.org/abs/2609.01852) — **derived-from**: original external source for the prospective ingest.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Make Authority Explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md): its claim concerns permission to mutate, promote, and activate memory. The experiment's authority cue is apparent evidential credibility, so treating the paper as direct support would conflate concepts.
- [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md): the stale-copy hazard overlaps, but the paper does not establish cheap mechanical derivation or the note's stronger enforce-or-omit rule.
- [Graphiti source ingest](../../../../sources/graphiti-temporal-knowledge-graph.ingest.md): useful temporal context, but the code-grounded review above is the stronger nonredundant companion.
- [Knowledge-access architecture must be evaluated end to end](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md): the source isolates consumption rather than the whole retrieval/write/update system; the narrower effects-evaluation connection is more precise.

## Index Membership

None. The existing agent-memory curated head routes to notes and requirements; this source can support those notes without adding a source entry directly.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Keep oracle-assisted pre-resolution distinct from a tested resolver. Ground truth is supplied by construction in this benchmark.
- Effects are conditional on cue framing, model family/size, and baseline. The paper explicitly limits the position sign reversal to Qwen and says the stale-evidence failure is not memory-specific.
