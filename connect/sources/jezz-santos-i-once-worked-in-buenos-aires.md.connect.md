---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/jezz-santos-i-once-worked-in-buenos-aires.md"
source_has_frontmatter: true
date: "2026-09-02"
depth: standard
---

# Connection Report: I ONCE WORKED in Buenos Aires

**Source:** [I ONCE WORKED in Buenos Aires](../../../../sources/.snapshots/jezz-santos-i-once-worked-in-buenos-aires.md)

## Discovery Trace

**Description listing scan:**

- Ran `rg '^description:' kb/notes/ --glob '*.md'` and filtered for `software factor|factory construction|production knowledge|product famil|codif|prototype|binding|brittle|domain-specific`. Kept the versioned software-factory reconstruction, factory-construction boundary, software-factory definition, and prototype-standing note. Rejected general codification notes whose claims do not depend on organizational abandonment or tool maintenance.
- Ran the same scoped description listing over `kb/sources/`, excluding snapshots, and filtered for `software factor|factory construction|product line|model-driven|Greenfield|Tool Factory|MDSoFa`. Kept Greenfield's 2003 and 2007 program accounts as the clearest before/after comparisons. Cook and Kent's Tool Factory and MDSoFa were evaluated but rejected as weaker outcome comparisons because they describe other proposed or implemented mechanisms rather than the Microsoft initiative's later fate.
- Ran scoped description listings over `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` with `software factor|factory construction|production knowledge|model-driven|Greenfield`. No reference candidate bears on the shipped Commonplace system, and no external-system review gains a concrete traversal path from this retrospective, so those destinations were skipped after the trigger check.

**Topic indexes:**

- Read `kb/notes/tags-README.md`, `foundations-README.md`, `self-improving-systems-README.md`, and `constraining-README.md`. The source bears most directly on the foundations cluster's historical software-factory ontology and on the distinction between codified machinery and human factory development. The source has no tags, so no complete tag head could replace discovery.
- Read the curated heads for `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`. Only notes and source analyses supplied plausible destinations under the sources collection's outbound rules.

**Full title surfaces:**

- Generated fresh title listings with `rg -N --no-heading -m1 '^# '` for every authorized local destination: `kb/notes/`, `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`. The candidates retained below survived later description and body checks; generic factory, modeling, tool, and codification matches did not.

**Body search:**

- `rg -n -i "software factor|software product line|domain.specific|codif|family breadth|factory development|production knowledge|model.driven|brittle|tool coupling" kb/notes/ --glob '*.md'` surfaced the ontology, construction/acquisition, breadth, and revision-cost clusters. The breadth note was rejected because Santos discusses product-market breadth, not the workshop's stronger claim about unanticipated family demands defeating codification.
- `rg -n -i "software factor|software product line|domain.specific|codif|factory development|production knowledge|model.driven|Visual Studio|Greenfield" kb/sources/ --glob '*.md' --glob '!kb/sources/.snapshots/**'` surfaced the retained Greenfield, Cook/Kent, MDSoFa, patent, and current-agentic-factory sources. The Greenfield accounts are the only direct comparisons to the program whose later organizational fate Santos recounts.
- Equivalent body searches over `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` produced only Commonplace implementation uses or present-day agentic-factory terminology, not candidates that improve interpretation of this historical retrospective.

**Link following:**

- Followed the software-factory definition to the detailed versioned ontology and from there to Greenfield's 2003 and 2007 ingests. This established the retrospective as an outcome-side companion to the retained program-side sources.
- Followed the factory-construction note to Cook and Kent's Tool Factory and MDSoFa. Santos's account adds a human-led construction and maintenance episode, but its strongest new evidence is the organizational and platform fate of the Microsoft strategy rather than a third technical construction mechanism.
- Followed the prototype-standing note's binding and reconstruction-cost mechanism. The retrospective's repeated Visual Studio breakage is a concrete single case of tool coupling raising revision cost, but it does not establish the note's general theory by itself.

## Connections Found

- [A software factory is family-scoped lifecycle production machinery](../../../../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — **is-evidence-for**: Santos supplies a participant's later account of how the Microsoft tooling strategy, factory-building toolkit, customer deployment, and human maintenance roles developed after the 2003 and 2007 program descriptions.
- [Factory construction is not evidence of production-knowledge acquisition](../../../../notes/factory-construction-does-not-establish-knowledge-acquisition.md) — **is-evidence-for**: the retrospective describes people discovering customer problems, choosing the reusable abstraction, building the meta-factory, adapting it through Aspen feedback, and carrying its maintenance after Microsoft withdrew platform support.
- [Software factory](../../../../notes/definitions/software-factory.md) — **is-evidence-for**: the account identifies a configured family-specific use—harvesting and applying an organization's software patterns—while distinguishing the generic factory-building toolkit from the deployed Aspen program.
- [A theory's prototype standing is its expected revision cost](../../../../notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md) — **is-evidence-for**: NuPattern's tight Visual Studio integration made successive host changes expensive until its small maintenance community could no longer keep it current, providing a bounded practitioner case for external binding as revision cost.
- [Greenfield and Short's 2003 software-factory account](../../../../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) — **compares-with**: the 2003 source states the industrialization program and recursive factory-building vision; Santos later reports the Visual Studio strategy's abandonment and the successor toolkit's path out of Microsoft.
- [Greenfield's mature 2007 software-factory account](../../../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) — **compares-with**: Greenfield describes the mature ontology and feedback-supported factory development, while Santos reports one later customer program that succeeded and one platform/tooling line that did not persist.

## Bidirectional Candidates

- [Greenfield and Short's 2003 software-factory account](../../../../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) ↔ source — **compares-with**: the proposal-to-retrospective path is useful in both directions because it separates the promised industrial program from the later fate of Microsoft's tooling strategy.
- [Greenfield's mature 2007 software-factory account](../../../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) ↔ source — **compares-with**: readers of either source need the contrast between the abstract feedback-and-revision model and the actual organizational split between a successful customer program and discontinued platform support.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Broad software demands create pressure for agentic factory development](../../../../notes/broad-software-demands-create-pressure-for-agentic-factory-development.md) — rejected because Santos's product-market breadth discussion does not establish that broad product families admit unanticipated demands that defeat exhaustive codification.
- [Codification](../../../../notes/definitions/codification.md) — rejected because the source exemplifies symbolic production tooling but does not clarify or test Commonplace's natural-language-to-symbolic definition.
- [The Tool Factory](../../../../sources/cook-kent-tool-factory-2003.ingest.md) and [MDSoFa](../../../../sources/langlois-exertier-mdsofa-software-factory-factory-2004.ingest.md) — rejected as direct connections because their primary reader need is already served through the factory-construction note; neither describes the fate of Microsoft's later tooling strategy.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) — rejected because sharing the `software factory` term does not supply a useful mechanism-level comparison between a current agentic workflow and a 2008–2010 modeling-tool initiative.

## Index Membership

None

## Synthesis Opportunities

- Santos's retrospective plus the Greenfield program accounts support a narrower historical claim than “software factories failed”: Microsoft abandoned the Visual Studio Software Factories strategy and its successor toolkit later became unmaintainable, while at least one human-intensive customer program, Aspen, reportedly succeeded. The platform strategy's fate and an individual factory deployment's outcome must therefore remain separate.

## Maintenance Observations

None

## Flags

- Tension: the source directly supports initiative-level abandonment and toolkit death, but it contradicts a categorical claim that every implementation failed by calling Aspen a long-lived success.
