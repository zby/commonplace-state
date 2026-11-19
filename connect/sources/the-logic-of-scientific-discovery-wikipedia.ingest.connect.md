---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/the-logic-of-scientific-discovery-wikipedia.ingest.md"
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: Ingest: The Logic of Scientific Discovery (Wikipedia)

**Source:** [Ingest: The Logic of Scientific Discovery (Wikipedia)](../../../../sources/the-logic-of-scientific-discovery-wikipedia.ingest.md)

The ingest already authors five footer edges (external `derived-from`; `is-evidence-for` to claim-modality and discovery-lifecycle; `compares-with` to the Conjectures and POPPER ingests). This report looks for what those five miss. The source is a thin tertiary witness for two Popper quotations: p. 19, the asymmetry of verification and falsification; p. 66, refutation needs a reproducible effect. So the candidate set is small on purpose.

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` "Outbound links". It allows prospecting in notes, reference, agent-memory-systems, agentic-systems, tags, and sources, and excludes `kb/work/` and `kb/instructions/`. Authorised labels by destination: notes — `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`, plus `defined-in` for notes/definitions; sources — `compares-with`, `see-also`; reference — `see-also` only; agent-memory-systems — `is-evidence-for`, `compares-with`, `see-also`; agentic-systems — `compares-with`, `see-also`; external — `derived-from`, `see-also`. No label row names `tags`. External prospecting was skipped because only the already-present Wikipedia URL is in scope.

**Tag heads:** the ingest carries no `tags:`, so no tag-head read was triggered. Tags is also unusable as a destination because no label authorises it.

**Body search:**
- `rg -il "popper|falsif|refut|counterexample|corroborat" kb/notes kb/sources kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags` — about 80 files. I triaged them by description. The Popper-specific hits kept for reading were `definitions/tentative-theory.md`, `definitions/theory-builder.md`, `claim-modality-is-the-inference-form-of-the-refuter.md`, `domain-pricing-routes-an-exception-to-idealization-assessment.md`, `candidacy-evidence-licenses-escalation-not-acceptance.md`, `generality-bought-to-avoid-counterexamples-is-paid-for-in.md`, `title-as-claim-exposes-commitments-enabling-popperian-maintenance.md`, `oracle-strength-spectrum.md`, the `popper-a-realist-view-...-1966` and `popper-conjectures-and-refutations` ingests, `reference/proposals/repair-dispositions-for-defeated-claims.md`, and `reference/source-adoption-policy.md`.
- `rg -n "genuine instance|one genuine|genuine counterexample|reproduc" kb/notes kb/sources` — "genuine counterexample" is left undefined in two places: `kb/notes/COLLECTION.md` line 63 and the claim-modality note. The "reproduc" hits are unrelated uses (reproducibility of evidence, parametric reproduction).
- `rg -n "Logic of Scientific Discovery|Logik der Forschung" kb` — outside the target, the only citation is `generality-bought-to-avoid-counterexamples-is-paid-for-in.md`, and it cites the levels-of-universality material that this article does not cover.
- `rg -n -i "anomal|single (counter|instance|report)|basic statement|stray|blam(e|ing) the data|asymmetr"` over the shortlisted files — `discovery-lifecycle.md` line 35 routes later counterevidence to observation / anomaly. The 1966 ingest line 52 records Popper's "strongest available means for criticism".
- `rg -n -i "counterexample|falsif|refut"` over `title-as-claim-exposes-commitments-...`, `narrowing-bought-...`, and ADR 066 — ADR 066 decision 1 codifies "one genuine counterexample refutes" for the universal mode.
- `rg -il "falsif|refut|popper" kb/agent-memory-systems kb/agentic-systems` — two hits. `reviews/agentic-harness-engineering.md` line 106 ("falsification loop"; safety from "repeated external evaluation") and `reviews/evoontology.md` line 36 (asks for "a falsifiable hypothesis"). Both are evaluated below.

**Link following:**
- The claim-modality footer led to domain-pricing, `narrowing-bought-to-survive-review-is-paid-for-in-content.md`, `candidacy-evidence-...`, and ADR 066. Candidacy-evidence and ADR 066 were kept for evaluation.
- The tentative-theory footer led to the two primary Popper ingests. Both are already covered, or evaluated below.
- The theory-builder definition body (line 43) says a criticism "can blame the test, the data, or an..." That clause is the specific hook for the p. 66 condition.

## Connections Found

- [Theory builder](../../../../notes/definitions/theory-builder.md) -- **is-evidence-for**: the p. 66 reproducible-effect condition bears on condition 3 (criticism) and on the definition's statement (line 43) that a criticism can itself be criticized by blaming the data. It is a Popperian case of a test result that does not count against a theory until it is reproduced. The ingest's Learning Claims section already argues this and links the target inline, but the footer has no edge. The evidence is weak (a tertiary source, and a gloss rather than a revision), so the context phrase should say that.
- [Tentative theory](../../../../notes/definitions/tentative-theory.md) -- **is-evidence-for**: the p. 19 asymmetry states the logical reason that no accumulation of passing reviews verifies a universal claim, which is why every retained theory stays tentative. Extractable Value 2 already names this and links the target inline without a footer edge. The target is already grounded in primary Popper texts, so this adds a quotable page reference, not new support. Consider the edge optional.
- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) -- **is-evidence-for**: the p. 66 condition is the refutation-side counterpart of that note's separation. One stray contradicting report is candidacy evidence: it earns investigation. A reproducible effect is verdict evidence: it refutes. The note's two worked witnesses and its Peircean anchor are all on the acceptance side. This would be an independent Popperian witness that the same separation holds for counterevidence. Moderate: mapping "stray basic statements" onto candidacy evidence is the ingest's interpretation, not the article's.
- [Popper, A realist view of logic, physics, and history (1966)](../../../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md) -- **compares-with**: axis is how strong a criticism must be before it refutes. That ingest records Popper favouring "the strongest available means for criticism" (Extractable Value 5). The p. 66 passage sets a minimum on what a criticism must establish, a reproducible effect, before it counts as a falsification. Read together, they separate how hard a reviewer should attack from what a single finding can decide. The 1966 source is also primary, so it gives a second primary-text alternative to this tertiary summary.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [claim modality is the inference form of the refuter](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) → source -- **evidenced-by** (notes collection label): the target says "modus tollens on one genuine instance" but does not say what "genuine" means. The p. 66 condition would bound that phrase. However, the ingest's own Recommended Next Action makes this Wikipedia ingest only a fallback grounding target, used only if a primary text cannot be captured. Author this edge only on that fallback path.
- [discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) → source -- **evidenced-by** (notes collection label): the routing of later counterevidence to observation / anomaly (line 35) is currently unsourced. The p. 66 condition is a Popperian witness for it. Low priority: the definition's lineage is Peircean, and a primary Popper text would be the better anchor.

## Off-authorisation Candidates

- [ADR 066 — Claims declare modality in text, and passes repair mode mismatch](../../../../reference/adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md) -- decision 1 codifies "one genuine counterexample refutes" for the universal mode, and the p. 66 condition bears materially on what that rule should count as a counterexample. The sources contract authorises only `see-also` for reference destinations, and `see-also` understates an evidential relation. Suggestion: reject for now. The durable edge belongs on the claim-modality note (reverse-edge above), and ADR 066 already links to that note's subject area. Extend `is-evidence-for` to reference ADRs only if source-to-ADR evidence edges recur.

## Raw Text Candidates

None

## Rejected Candidates

- [generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- cites the book, but for levels of universality and precision, which this article does not cover. The ingest already says it cannot support that citation, so an edge would mislead.
- [narrowing bought to survive review is paid for in content](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) -- concerns how a defeated claim is repaired, not what defeats it. Neither quotation bears on repair.
- [title as claim exposes commitments, enabling Popperian maintenance](../../../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) -- invokes Popper's falsifiability criterion in general terms. The two quotations add nothing specific to its argument about claim titles.
- [domain pricing routes an exception to idealization assessment](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) -- its routing concerns ideal-type exceptions (Lakatos's anomaly). The p. 66 condition concerns universal claims, so candidacy-evidence is the better-scoped target for the routing parallel.
- [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- keyword match on verification. It is not about refutation thresholds.
- [Agentic Harness Engineering review](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- "safety comes from repeated external evaluation" loosely echoes reproducibility. But the review does not frame benchmark flips as refutations that need reproduction, so a `compares-with` axis would be invented.
- [EvoOntology review](../../../../agentic-systems/reviews-archive/evoontology.md) -- asks for "a falsifiable hypothesis": a keyword match with no bearing on the two quotations.
- [Repair dispositions for defeated claims (proposal)](../../../../reference/proposals/repair-dispositions-for-defeated-claims.md) -- covers repair policy after a claim is defeated, not the refutation threshold. It would also be `see-also` only.
- [Optimal choice of hypothesis is the weakest, not the shortest](../../../../sources/optimal-choice-of-hypothesis-is-the-weakest-not-the-shortest.ingest.md) -- a Popper keyword hit about hypothesis selection, with no axis shared with this source.

## Index Membership

None. The ingest carries no tags, and the sources collection has no curated index that would list it.

## Synthesis Opportunities

None beyond the open question the ingest already flags: whether "genuine counterexample" in the universal mode should mean "reproducible". The candidacy-evidence note, the discovery-lifecycle routing, and the p. 66 condition together suggest a possible rule: a single unreproduced counterexample is candidacy evidence that routes a universal claim to assessment, not a refuter. The rule has a known difficulty, raised in the ingest: in a prose KB many counterexamples are arguments, not observations, and "reproducible" may not apply to them. This needs a deliberate decision and a primary Popper text, not a connect-driven note.

## Maintenance Observations

- "Genuine counterexample" is undefined in both `kb/notes/COLLECTION.md` (claim-modality paragraph, line 63) and ADR 066 decision 1, as well as in the claim-modality note. That wording is binding, so the gap sits in a system-definition artifact, not only in a knowledge note. Any resolution needs to touch all three consistently.

## Flags

- The source is weak and tertiary. The ingest's own Recommended Next Action is to capture a primary text of *The Logic of Scientific Discovery*. Every `is-evidence-for` candidate above would be better authored from that future primary ingest, so a writer may prefer to defer them.
