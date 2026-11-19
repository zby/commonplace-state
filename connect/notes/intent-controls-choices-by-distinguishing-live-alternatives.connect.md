---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/intent-controls-choices-by-distinguishing-live-alternatives.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Intent controls a local choice only when it distinguishes its live alternatives

**Source:** [Intent controls a local choice only when it distinguishes its live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md)

## Discovery Trace

**Authorisation and curated heads:**

- Read the source note, `kb/notes/COLLECTION.md`, and the connect-report type before discovery. The notes contract authorises prospecting in notes, types, reference, agent-memory-systems, agentic-systems, sources, and instructions; it excludes `kb/work/`. It authorises external targets only when already known, so open-web prospecting was skipped.
- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, and `kb/notes/foundations-README.md`. The foundations head has no `complete: true` mark, so its by-tag scan was retained. No methodology or planning tag head exists, so both by-tag scans were also retained.
- Read the curated destination heads `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. Read the destination collection contracts where inverse-edge labels had to be checked. No search command produced a ranking score.

**Complete title and description surfaces:**

- For each authorised local destination, ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'`, with `<destination>` separately set to `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Ran the guarded by-tag description query separately for `foundations`, `methodology`, and `planning` in every destination: `rg -l '^tags:.*\bTAG\b' kb/<destination>/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`. The notes scans surfaced the direct theory cohort. The other collections had no matching methodology or planning descriptions; the only non-note foundations hits were four reference artifacts and one unrelated Ashby source.

**Notes body search:**

- `rg -n -i 'live alternatives|local alternatives|local choice|choice.*intent|intent.*choice' kb/notes/ --glob '*.md'` -- kept the executor-boundary and methodology-selection candidates; the exact source was otherwise the only literal live-alternatives hit.
- `rg -n -i "commander'?s intent|mission command|auftragstaktik|specific intent|high-level purpose" kb/notes/ --glob '*.md'` -- kept the specific-intent candidate and recovered the existing intent-framed edge; military-label hits were re-filtered through the mechanism rather than kept by keyword.
- `rg -n -i 'admissible|preferred|stopping condition|sufficient to stop|branch decision|rank branches|further search' kb/notes/ --glob '*.md'` -- kept the failure-explanation contrast; productive deferral was evaluated but rejected as an evidence-timing rule already reached through a stronger neighbor.
- `rg -n -i 'distinguish(es|ing)? .*alternatives|discriminat(e|es|ing|ion).*option|compatible with every' kb/notes/ --glob '*.md'` -- confirmed that rule-based context selection is a structural analogy about codified signals, not a direct intent connection.
- Follow-up queries `rg -n -i 'leaves? (every|the|all) .*decision.*unchanged|leave.*choice.*unchanged|leav.*search unchanged|if.*unchanged.*(choice|decision|search)' kb/notes/ --glob '*.md'`, `rg -n -i 'withholding|removing|replacing|perturbing' kb/notes/ --glob '*.md'`, and `rg -n -i 'participates? in (action|decision) selection|affects? (action|intervention|branch) selection|changes? .*ordering' kb/notes/ --glob '*.md'` exposed the cross-note counterfactual-control synthesis recorded below.

**Other-destination body search:**

- Reference: `rg -n -i 'intent|purpose|live alternatives|local choice|decision rights|delegat' kb/reference/ --glob '*.md'`, `rg -n -i 'mission command|auftragstaktik|commander.?s intent|specific intent' kb/reference/ --glob '*.md'`, and `rg -n -i 'admissible|preferred|further search|stopping condition|branch decision|discriminat' kb/reference/ --glob '*.md'`. `control-plane-goals.md`, `definitions/commonplace-doctrine.md`, and `content-routing.md` were evaluated; each either concerns retention/routing rather than the local discrimination test or already routes through the broader intent-framed note.
- Types and instructions: `rg -n -i 'intent|purpose|alternative|choice|discriminat' kb/types/ --glob '*.md'` and the same query over `kb/instructions/`. The instruction type and `write-instruction.md` encode the source claim directly. Their collections' frontloaded posture makes inverse `rests-on` edges more useful than outbound links from the source.
- Agentic systems and agent-memory systems: ran `rg -n -i 'intent|purpose|alternative|choice|discriminat|mission command|auftragstaktik'` over each collection, then the narrower `rg -n -i 'live alternatives|task intent|intent.{0,60}(choice|branch|means)|purpose.{0,60}(choice|branch|means)|mission command|auftragstaktik'`. The few hits described incidental task intent or selection bundles and failed the articulation test.
- Sources: `rg -n -i "commander'?s intent|mission command|auftragstaktik|intent.{0,80}(choice|means|action)|purpose.{0,80}(choice|means|action)" kb/sources/ --glob '*.md'`, `rg -n -i 'live alternatives|local alternatives|discriminat.{0,60}(alternative|option|choice)|further search|stopping condition' kb/sources/ --glob '*.md'`, and `rg -n -i 'intention is all you need|intelligent ai delegation' kb/sources/ --glob '*.md'`. MCDP 1, ADRP 6-0, Stahel, *Intention Is All You Need*, and *Intelligent AI Delegation* were read. They supply cases, doctrine, or adjacent frameworks but do not establish the source's universal counterfactual necessity claim.

**Link following and inbound check:**

- Followed both authored source links: the intent-framed delegation note and lightweight search-control note. From the first, followed the executor-boundary note, its MCDP 1 / ADRP 6-0 / Stahel sources, and the Commonplace-doctrine definition. From the executor-boundary note, followed productive deferral. From methodology selection, followed methodology-closure. From the specific-intent candidate, followed design-rationale retention and the bare-writing-prompt case. From the failure-explanation candidate, followed the theory-mediated path and its withholding test.
- `rg -n 'intent-controls-choices-by-distinguishing-live-alternatives' kb --glob '*.md'` returned no inbound links at discovery time.

## Connections Found

- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **extends**: applies the source's necessary discrimination test to the author-executor boundary, leaving a choice open only when task intent or authorised evidence can distinguish permitted alternatives and treating the residue as fixed, irrelevant, or a gap.
- [A capable agent needs methodology selection, not just relevant knowledge](../../../../notes/capable-agents-need-methodology-selection.md) -- **extends**: gives the control problem a concrete live-alternative set--mutually incompatible methods--and explains how an intent-and-constraints cue can make one method govern rather than merely add relevant facts.
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) -- **extends**: develops the scope consequence of the discrimination test: a sufficiently specific purpose can constrain many local judgments, while a broad purpose and facts it does not entail cannot.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- **contrasts**: applies the same null-effect test to a different proposed control input--a retained failure explanation--and to later search branches rather than task intent and local means.

## Bidirectional Candidates

- [Intent-framed delegation is a control regime; prompt length does not establish it](../../../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) <-> source -- **mechanism**: a return edge would isolate why task purpose has local force inside the larger delegation regime: directly or through a bridge, it must discriminate among the executor's live means.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) <-> source -- **grounds**: a return edge would expose the atomic premise behind its rule that task intent and live evidence can justify leaving one decision to execution.

## Reverse-edge Candidates

- [Instruction](../../../../types/instruction.md) -> source -- **rests-on**: the global instruction contract tells authors to leave a bounded choice open when purpose and authorised evidence permit selection, and to name evidence that can discriminate a coarse future choice; the source supplies the intent-specific necessity behind that contract.
- [Write an instruction](../../../../instructions/write-instruction.md) -> source -- **rests-on**: its choice-classification and verification steps depend on intent controlling an open execution choice only where authorised live or produced evidence changes or constructs the selection.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../notes/productive-deferral-requires-option-evidence-and-convergence.md) -- rejected as a direct edge because its selector is future evidence and its return rule, not intent; the useful route is already one hop through the executor-boundary and lightweight-search notes.
- [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) -- its proposed ablation changes an intent-theory-history-constraints bundle, so it does not isolate intent well enough to support a direct evidence or mechanism edge.
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../../../../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) -- criteria constraining meta-decisions have a similar shape, but the note does not make intent or the live-alternative bridge load-bearing; methodology selection is the more direct neighbor.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) -- a codified routing signal distinguishes cases for a rule-based selector, but it is not a stated intent governing a choice; similarity is structural rather than a useful artifact-to-artifact edge.
- [MCDP 1, Warfighting](../../../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md) and [ADRP 6-0, Mission Command](../../../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md) -- both give positive doctrinal cases in which purpose guides changing local means, but neither establishes the universal counterfactual necessity claim, and the existing intent-framed edge already carries their bounded source support.
- [Intention Is All You Need](../../../../sources/intention-is-all-you-need-2022428696595108152.ingest.md) -- proposes structured intention as a coordination surface but reports no implementation, comparison, or counterfactual showing which choices the intention changes.
- [Control-plane goals](../../../../reference/control-plane-goals.md) -- the shipped delegation invariant is a useful Commonplace application, but it already rests on the broader intent-framed note; a second source-to-reference `see-also` edge would add little traversal value.

## Index Membership

- [Foundations](../../../../tags/foundations-README.md) -- add under “Rationale and design method” as the atomic test for whether a stated purpose actually constrains a downstream choice.

## Synthesis Opportunities

- [This source](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md), [the failure-explanation note](../../../../notes/failure-explanation-changes-later-branch-decisions.md), and [the natural-language project-state note](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) jointly suggest a representation-independent counterfactual test: a stated or retained representation exercises decision control only where withholding or replacing it changes the live candidate set, ordering, search allocation, or stop rule. [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) already owns the participation-path half; consider extending that owner with the discrimination test before creating a separate synthesis note.

## Maintenance Observations

- [A capable agent needs methodology selection, not just relevant knowledge](../../../../notes/capable-agents-need-methodology-selection.md) has footer labels `complements` and `motivates`, neither of which is authorised by `kb/notes/COLLECTION.md`; a later maintenance pass should replace them with authorised reader-need labels or ordinary prose.

## Flags

None
