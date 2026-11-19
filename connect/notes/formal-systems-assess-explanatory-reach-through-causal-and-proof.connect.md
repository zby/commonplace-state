---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Causal and proof obligations are two formal routes to assessing explanatory-reach

**Source:** [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md)

## Discovery Trace

**Curated heads:**

- Read [Foundations](../../../../tags/foundations-README.md), [Computational model](../../../../tags/computational-model-README.md), [Self-improving systems](../../../../tags/self-improving-systems-README.md), and [Constraining](../../../../tags/constraining-README.md). The closest unlinked routes were the cross-form coverage and pre-formal-stage notes.

**Description listing and body search:**

- `rg -n "^description:.*(correspond|formal|proof|interpret|prototype|revision cost|binding|investment|pre-formal)|^# .*([Cc]orrespond|[Ff]ormal|[Pp]roof|[Ii]nterpret|[Pp]rototype|[Rr]evision|[Bb]inding)" kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` -- found the formalization, cross-form governance, and prototype-stage neighborhoods. No ranked retrieval was used, so no scores were available.
- `rg -n "correspondence boundary|authoritative formal definition|proof validity|translation fidelity|relocat.{0,20}interpret|prototype standing|revision cost|lost investment|intrinsic reconstruction|operational binding" kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` -- confirmed the two candidates below and the already-authored codification, semantic-work, Eigenius, and DiscoverPhysics links.
- `rg -n "\\[[^]]+\\]\\([^)]+\\)" kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md` -- inventoried existing outbound edges before retaining new candidates.

**Link following:**

- Read [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md), [Improvements outside the admitted formal language need a pre-formal stage somewhere](../../../../notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md), [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md), and [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md). The first two develop direct consequences of the source's correspondence boundary; the latter two concern timing of commitment rather than what formal checks warrant.

## Connections Found

- [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) -- **extends**: the source identifies an unchecked mapping between an externally interpreted claim and its formal obligation; the target develops the governance consequence that a system moving responsibility across that mapping must cover both forms and the mapping itself.
- [Improvements outside the admitted formal language need a pre-formal stage somewhere](../../../../notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) -- **extends**: the source bounds formal assessment to obligations already expressed inside a model; the target explains what an improvement loop must add when a candidate's concepts have not entered any admitted formal language.

## Bidirectional Candidates

- [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) <-> source -- **grounds**: a return link would give readers the proof-versus-correspondence reason that covering only the symbolic endpoint cannot govern the mapping into it.

## Reverse-edge Candidates

None. The pre-formal-stage note already links to the source, and Eigenius already uses the source as its general proof-versus-correspondence account.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Codification](../../../../notes/definitions/codification.md), [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md), [Eigenius](../../../../agentic-systems/reviews/eigenius.md), and [DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) -- already linked from the source with their exact definitional, mechanism, and evidence roles.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) -- useful timing policy for durable specifications, but it does not distinguish formal entailment from correspondence.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) -- concerns when to freeze an interpretation, not what a formal obligation can warrant after freezing.
- [Prototype standing is revision cost](../../../../notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md) -- already links to the source for the narrower claim about what proof warrants; a reciprocal edge would not independently help source readers.

## Index Membership

None proposed. The current heads are selective, and the source is already reachable through its tags and the oracle-domain and Gödel-machine cluster.

## Synthesis Opportunities

None. The two connection candidates already own the downstream lifecycle and governance consequences separately.

## Maintenance Observations

None.

## Flags

None.
