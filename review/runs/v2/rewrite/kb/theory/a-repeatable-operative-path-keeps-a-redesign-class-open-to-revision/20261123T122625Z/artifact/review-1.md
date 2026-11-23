---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md
  against kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
note: kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md
note-sha256: b16c8a9dca7d1d7e3cab43dcf32f93202d7a623dbf83011d6eba8937ce38b003
criterion: kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
criterion-sha256: 72878e536fd897c07be2c1dec0230689269ff118d9e862eef66f6fc8b814c3b2
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision/20261123T122625Z/reviews/3a4f21b61b4f
launch: 2259242d53c147a2828cc01ffb3077c4
completed-at: '2026-11-23T12:30:49Z'
findings:
- scope: passage
  quotes:
  - Each question names a causal step a change needs before it can matter.
  reason: 'Basis: in the candidate (note.md), question 1 says representation is the
    observer''s identification of the changed part and class, and that the system
    need not inspect or describe itself. That is a reference-fixing precondition for
    the analysis, not a causal step the change passes through. The Reasoning paragraph
    still calls all six questions causal steps, and the description keeps ''a causal
    path through representation''. A reader applying the test to their own workflow
    gets two incompatible readings of what representation requires. The commission''s
    correction (''the updater need not model or expose it'') is what produced the
    observer reading. Required change: say in Reasoning that representation fixes
    what the test is about and that determination through continuity are the causal
    steps. Adjust the description''s ''causal path through representation'' to match.'
  level: warn
- scope: passage
  quotes:
  - Repeated gain changes are not evidence that the circuit can redesign itself.
  reason: 'Basis: the opening defines a redesign class to include ''adjust this gain'',
    and the verdict calls gain adjustment operative and repeatable. This sentence
    then uses ''redesign'' for the circuit''s threshold and logic only, so by the
    note''s own term the circuit does redesign itself in the gain class. CLAUDE.md
    asks for one term per concept. Required change: keep the class-relative wording,
    e.g. ''Repeated gain changes are not evidence of a path for the class "circuit
    redesign"'', or name that contrasting class without reusing bare ''redesign''.'
  level: warn
- scope: passage
  quotes:
  - People performed the diagnosis, the review, and the admission.
  reason: 'Basis: supplied-source-1 (''Revising the self-representation'') says an
    agent in Claude Code retrieved the claim that made sense of the strain and drafted
    the split. ''Detection in this episode was human.'' So the diagnosis was shared
    between people and an agent. The sentence credits the whole diagnosis to people,
    and the candidate''s previous paragraph credits the drafting to an agent. Required
    change: say that people detected the strain and reviewed and admitted the change,
    and that an agent formulated the candidate. Alternatively, drop ''the diagnosis''.'
  level: warn
contract: verdict
target-sha256: b16c8a9dca7d1d7e3cab43dcf32f93202d7a623dbf83011d6eba8937ce38b003
target-capture: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision/20261123T122625Z/reviews/3a4f21b61b4f/calls/launches/2259242d53c147a2828cc01ffb3077c4/inputs/note.md
observation: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision/20261123T122625Z/reviews/3a4f21b61b4f/artifact/reviews/7d19f85c19a2c807c46aa1ff/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision/20261123T122625Z/reviews/3a4f21b61b4f/calls/launches/2259242d53c147a2828cc01ffb3077c4/outputs/review.md
raw-output-sha256: 45277255c50eba902adc5d4a50d9429c36b9ffdd8f0940c75399d77dd237073a
---

# Review

## Judgment

The candidate makes the contribution the commission asks for. It opens with a concrete sequence. It works the overshoot circuit as the commission specifies: a read-protected gain goes 8 → 4 → 2, each later cycle uses the replacement, and the verdict holds for gain adjustment only. It adds a familiar workflow in which an installed and used change closes its own route: the review-bot rule. Both examples are labelled invented, both in the text and in Caveats. The verdict changes between the circuit's two classes and again in the review-bot case. Those are the contrasts the commission asked for.

The must-keep items are present:
- proposed versus operative change (the draft rule would fail at admission);
- the five confusions, each brought in beside an example;
- later episode versus specified mechanism, in step 6 and in Caveats;
- all six questions;
- the point that people can carry out steps, together with the patch-from-memory case showing that a wider boundary does not by itself retain a route;
- the Agno case, kept to target-side edits.

The ADR 028 → 057 claim is gone. I found no new external empirical claim. The tag-README case stays within its evidence: the caught member is presented as dependence and explicitly not as a second redesign.

## Sources

The two Agno quotations match the ingest's Quotes section. The class "instructions, tools, parameters, and code" is supported by that ingest's first and third quotes. The six-path summary matches source-3: Accumulated Behavioral Rules lacks a baseline and per-rule isolation, and HyperAgents leaves evaluation and the outer archive loop outside the editable program. "Comes closest to a continuity witness" is hedged enough for a lineage that later generations modify again. The tag-README figures (18.8 KB, 55 entries, measured by hand), the `complete` mark, the tests, the review and merge, and the block-YAML catch all match source-1. The only attribution problem is the "diagnosis" sentence in the third finding.

## Coherence

The main weakness is conceptual: see the first finding. The commission asks for representation to be the observer's identification. The candidate adopts that reading but keeps describing representation as one causal step on the path. A small edit to the Reasoning paragraph and the description resolves this. The second finding is a terminology slip of the same kind. Neither blocks publication, but each could mislead a reader applying the test.

## Affected citations

The writer's report matches the supplied inbound passages. It correctly finds the stale "represented" in the Agno AgentOS review. It correctly notes that the reflection tag gloss may suggest self-representation. It correctly notes that "executable recovery" in the program-theory footer was never clearly supplied. I checked the other five inbound uses against the candidate, and they are still supported. The removed ADR reuse cases and removed links had no inbound dependants. The report correctly treats repairing dependants as separate work.
