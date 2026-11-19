---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/naur-binds-theory-to-humans-via-premise-that-machines-follow-rules.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Rule-inexpressibility does not entail human exclusivity

**Source:** [Naur's rule-inexpressibility argument does not by itself bind program theory to humans](../../../../notes/naur-equates-machine-execution-with-formulated-criteria.md)

## Discovery Trace

**Description listing scan:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/foundations-README.md`, and `kb/notes/context-engineering-README.md`. Neither tag README declares `complete: true`, so both tag scopes remained eligible for search. The strongest candidates were the two already-linked interpretation/retention notes, [Representational form](../../../../notes/definitions/representational-form.md), and [Opacity is a scale threshold, not a class property](../../../../notes/opacity-is-a-scale-threshold.md).
- Read the curated heads for `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`. The type, external-system, and instruction collections had no candidate whose contract or observed behavior directly bears on the revised missing-premise claim. The sources scan retained the existing primary-source edge and rejected two weaker comparisons below.
- Generated the complete current title surface with `rg -N --no-heading -m1 '^# ' kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` (1,072 titles).
- Ran `rg -n -i '^description:.*(Naur|program theory|theory[- ]building|formulable|rule[- ]follow|decision premise|unregenerable|computab|trained interpreter|interpretation and retention|design rationale)' ...`. It surfaced the revised source note, its source ingest, and the two already-linked retention notes, but no near-duplicate owning the missing-premise diagnosis.

**Topic indexes:**

- `foundations-README.md` supplies the better prospective index: the note separates rule-inexpressibility from human exclusivity in a foundational argument inherited by several methodology notes. `context-engineering-README.md` is topically adjacent through retention, but its curated head is about routing, loading, and maintenance; the note would not sharpen that head's current routing.

**Body search:**

- `rg -n -i '(Naur|Programming as Theory Building|program theory|theory-holder|theory holder)' ...` found the source ingest, three current inbound citers, and adjacent notes about rationale transfer and intent. The inbound citers already author the useful reverse edges, but all three still state the old stronger claim and therefore remain maintenance dependencies rather than new candidates.
- `rg -n -i '(formulable|formulat(e|ed|ion).{0,40}rule|rule.{0,40}comput|computab|finite formal specification|learned (rule|criteria)|example-based learning|decision tree)' ...` surfaced the form/opacity distinction as the closest missing comparison to the revised note's three description levels. Most other hits concerned deterministic recomputation and did not articulate a reader need for this note.
- `rg -n -i '(interpretation and retention|interpreter.{0,80}retention|retained.{0,80}interpreter|model weights.{0,80}rule|parametric.{0,80}(rule|knowledge)|symbolic.{0,80}parametric|learned.{0,80}(symbolic|rule))' ...` confirmed that [Representational form](../../../../notes/definitions/representational-form.md) supplies the local vocabulary for separating distributed-parametric model state from the symbolic runtime that executes it.

**Link following:**

- Followed the existing edges to [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md), [Design rationale must preserve decision premises its interpreter cannot regenerate](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md), [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md), and [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md). They form a coherent transfer cluster and already route the revised note's three empirical tests; another link to [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) would duplicate that route.
- Followed the form candidate to [Opacity is a scale threshold, not a class property](../../../../notes/opacity-is-a-scale-threshold.md) and [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md). The first directly prevents practical opacity or absence of hand-authored criteria from being mistaken for in-principle informulability. The second distinguishes prompt semantics from fixed operational execution, but its prompt-to-program mechanism is one layer away from the program-theory claim and was rejected as a direct edge.

## Connections Found

- [Representational form](../../../../notes/definitions/representational-form.md) — **contrasts**: separates distributed-parametric model state from the symbolic runtime that executes it, so the revised note's acquisition/form distinction does not collapse into a single “learned rather than ruled” category.
- [Opacity is a scale threshold, not a class property](../../../../notes/opacity-is-a-scale-threshold.md) — **contrasts**: distinguishes practical inscrutability from representational category and in-principle formulability, bounding what failure to extract a human-readable semantic rubric can establish.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None. The useful reverse edges are already authored by the primary source ingest, the design-rationale note, and the theory-mediated-self-improvement note.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) — its distinction between natural-language semantics and fixed operational behavior is useful background, but the source note concerns Naur's theory-holder and rule-determination claims rather than prompt interpretation; a direct edge would make the note carry an extra conceptual branch.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — relevant to the compiler-transfer case, but the existing source-ingest and design-rationale edges already route readers to that mechanism.
- [Emergent Analogical Reasoning in Transformers](../../../../sources/emergent-analogical-reasoning-transformers.ingest.md) — behavioral evidence for learned relational transfer does not establish theory possession or escape from formal determination, so it cannot ground the note's trained-interpreter witness.
- [Why LLMs can’t make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) — a contemporary application of Naur, but its Naur framing is secondary and its own limitations reject the strong inexpressibility claim; it adds no warrant beyond the primary source already linked.

## Index Membership

- [Foundations](../../../../tags/foundations-README.md) — candidate for the curated section because the note isolates the extra premise needed to turn a foundational rule-inexpressibility argument into a human-exclusivity conclusion.

## Synthesis Opportunities

None

## Maintenance Observations

- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) still treats “a trained interpreter falls outside that partition” as load-bearing. Its body and footer need semantic reconciliation with this note's conclusion that learning history does not establish escape from formal determination.
- [Design rationale must preserve decision premises its interpreter cannot regenerate](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) and the [Programming as Theory Building ingest](../../../../sources/programming-as-theory-building.ingest.md) also retain the old machines-follow-rules diagnosis in visible summaries. Their narrower transfer claims can survive, but their link text, summaries, and any premise dependence need one coordinated update after the required note relocation.

## Flags

- The revised note has no near-duplicate in the current KB. Its historical filename and three stronger inbound summaries now create a concrete relocation-and-citer-reconciliation operation; connect reports the dependency but does not perform it.
