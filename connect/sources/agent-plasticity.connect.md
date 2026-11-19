---
description: "Discovery report for Agent Plasticity: inherited-artifact learning, cost-normalized held-out gains, and availability/use/effect diagnostics"
type: types/connect-report.md
source: "kb/sources/.snapshots/agent-plasticity.md"
source_has_frontmatter: true
date: "2026-10-18"
depth: standard
---

# Connection Report: Agent Plasticity: Measuring Self-Improvement Through Experience

**Source:** [Agent Plasticity: Measuring Self-Improvement Through Experience](../../../../sources/.snapshots/agent-plasticity.md)

All edges below are discovery candidates, not authored links. The snapshot is immutable. Outbound suggestions belong on a future name-paired ingest, `kb/sources/agent-plasticity.ingest.md`, which does not currently exist. Durable incoming citations must also wait for that ingest; never point them at this snapshot or this cache report. The source has frontmatter, so this is not a provisional raw-text report.

The source studies frozen-model lineages inheriting tools, skills, strategies, and memory across fresh acting contexts. Its central measurements separate checkpoint performance, held-out gain per learning dollar, and artifact availability/use/failure. Structural admission does not imply improvement. Its failure attribution is observational, and its OOD condition changes opponent difficulty rather than testing arbitrary cross-task transfer. NetHack uses native coding-agent harnesses and fresh games at each checkpoint, so its across-checkpoint curves also mix learning with game difficulty.

## Discovery Trace

### Setup and search method

- Read the complete connect skill, global connect-report type and schema, source snapshot (all 6,575 lines, recovering each truncated segment), and [sources collection contract](../../../../sources/COLLECTION.md) before discovery. Read [reports collection contract](../../../COLLECTION.md) for the output surface.
- The sources contract permits prospecting notes, reference, historical agent-memory systems, agentic systems, tags, and other sources. It excludes work and instructions as destinations. Its external authorization permits already-known targets only. No workers, semantic-search service, or web browsing were used.
- Read each destination's `README.md`: [notes](../../../../notes/README.md), [reference](../../../../reference/README.md), [agent-memory systems](../../../../agent-memory-systems/README.md), [agentic systems](../../../../agentic-systems/README.md), [tags](../../../../tags/README.md), and [sources](../../../../sources/README.md).
- Generated one complete fresh title listing per destination using `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, replacing `<destination>` with each of the six names above. Recovered truncated title output from the tool's output logs. Listings included briefs; no brief became a standalone target.
- For each destination, scanned a scoped description listing with `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'held.out|plasticity|artifact.*(use|learn)|retriev|activat|self.improv|learning cost|behavioral eval|behavioural eval|learning trajector|frozen|compounding'`.
- For each destination, ran both body queries: `rg -l -i 'held.out|plasticity|artifact reuse' kb/<destination>/ --glob '*.md'` and `rg -l -i 'absent.*unused|activation.*(fail|effect)|learning cost|acquisition efficiency' kb/<destination>/ --glob '*.md'`. These are lexical discovery passes, not scored semantic retrieval; no numerical search scores were available.
- Verified all 20 candidate/navigation paths in the evaluated shortlist with `Path.is_file()` before authoring the report. The proposed ingest was separately checked and found absent.

### Notes — broad mechanism and evaluation pass

- The notes README routed to retained deployment-time adaptation. Titles and descriptions identified storage/activation, effects-based evaluation, retrieval-path failure, end-to-end knowledge access, experimental contrasts, sample-efficiency conjectures, and compounding as distinct possibilities.
- Fully read the adaptation note, storage/activation note, effects requirement, retrieval-miss note, end-to-end synthesis, activation-before-mistake requirement, sample-efficiency conjecture, experimental-contrast note, and compounding note. Read the notes collection contract to authorize reverse `evidenced-by` candidates and distinguish bounds from corroboration.
- Kept adaptation as a bounded existence witness, activation/effects as direct diagnostic connections, and experimental contrasts as an interpretation dependency. Retained the end-to-end synthesis as a reverse candidate because the paper supplies a bounded test case, not the origin of that synthesis.
- Rejected a direct sample-efficiency claim: dollars per held-out score point do not measure target observations under controlled structured shifts or isolate retained theory from other artifacts. Rejected treating rising performance curves as evidence of compounding.
- One-hop following: effects evaluation linked Memento-Skills and memory design; storage/activation linked the Faithful Self-Evolvers ingest; the experimental-contrast note linked the effects requirement; the compounding note linked Harness Updating. Read Faithful Self-Evolvers and Harness Updating, revealing the useful distinction between observed artifact use, causal content dependence, downstream benefit, and later improvement productivity. From the historical Voyager review, followed its trace-extraction requirement and read it; it supplies context but was not kept as another generic evidence edge.

### Reference — narrow operational analogue pass

- Titles and filtered descriptions identified [Agent memory coverage](../../../../reference/agent-memory-coverage.md) and its linked [gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md); fully read both.
- Kept coverage as one sparse `see-also` connection: the paper provides a concrete measurement example for the explicitly unimplemented behavioral-evaluation surface. Followed coverage → gap plan; the latter names cue firing, behavioral uptake, and WITH/WITHOUT checks.
- Did not add a second edge to the gap plan merely to repeat the same operational destination. Schema/review ADR hits were rejected as structural-check or frozen-source keyword overlap, not evidence that Commonplace has adopted this learning protocol.

### Agent-memory systems — executable-memory comparison pass

- The historical collection README and title listing exposed Voyager, ExpeL, Dynamic Cheatsheet, and harness-evolution systems. Description scanning made Voyager the strongest distinct comparison: a retrieved executable skill library rather than just prompt memory.
- Fully read [Voyager](../../../../agent-memory-systems/reviews/voyager.md) and this collection's contract. Kept a comparison on success-gated skill promotion, retrieval, and executable reuse versus structurally admitted, subsequently evaluated inventory revisions.
- One-hop following from Voyager reached storage/activation and trace-extraction theory, read above. This confirmed that the comparison should distinguish code available at runtime from code actually invoked.
- ExpeL/Dynamic Cheatsheet were not promoted from title-level matches into extra report edges: comparison on textual experience uptake is already better represented by the fully read causal-intervention source. Historical reviews remain citable at their recorded boundaries; no update to this frozen collection is proposed.

### Agentic systems — whole-harness boundary pass

- The README, title surface, and filtered descriptions identified Compound Engineering, Exo, and archived evaluation/learning accounts. Fully read [Compound Engineering](../../../../agentic-systems/reviews/compound-engineering-plugin.md) and the collection contract.
- Kept Compound Engineering as a comparison of retained project guidance with measured learning: its reviewed boundary does not establish later-episode outcome feedback or sustained compounding. Agent Plasticity supplies a concrete held-out trajectory/cost measurement contrast, not evidence about the plugin itself.
- One-hop following through its compounding and proposal-selection links led to the fully read compounding note. The feedback edge required for improvement productivity remains absent from the paper's headline plasticity measure.
- Did not keep Exo solely because its executor is editable: recovery/protected-history architecture is not this paper's primary contribution. Archived generated reports were visible in the full collection scans but were not selected over a suitable authored account or treated as current comparison-population data.

### Tags — navigation and authorization pass

- Fully read [continual learning](../../../../tags/continual-learning-README.md), [evaluation](../../../../tags/evaluation-README.md), and [trace-learning](../../../../tags/trace-learning-README.md), plus the tags collection contract and tag-readme type.
- Source frontmatter has no `tags:`, so there were no mandatory source-tag membership searches. The continual-learning head declares `complete: true`; skipped its by-tag `rg` and followed its curated routes to adaptation theory. Evaluation routed to the experimental-contrast note; trace-learning routed to executable-memory comparisons.
- No source→tags relationship label is authorized in the sources table, despite tags being named as a prospecting surface. The heads were useful discovery routes, but no sufficiently specific outbound edge to a head survived: topical navigation alone is not a reason to invent a label.
- Sources are outside the tags contract's participating collections. Neither the snapshot nor a future ingest is a tag-member candidate. No head additions or snapshot links are recommended.

### Sources — comparison and reverse-direction pass

- Description/body searches shortlisted Harness Updating, Continual Harness, Fragility, and Faithful Self-Evolvers. Fully read all four ingests.
- Kept Harness Updating for updater/consumer role separation, Continual Harness for reset-free versus fresh-context adaptation and unused-artifact tails, and Faithful Self-Evolvers for intervention-based dependence versus observational reuse.
- Followed Fragility → Faithful Self-Evolvers and existing notes on diagnostic evidence. Fragility remains a useful caveat about repeated lineages and order sensitivity, but no additional edge is needed in this focused shortlist.
- The sources contract authorizes `compares-with` in both directions. A reciprocal comparison at Harness Updating would add a distinct learning-cost and held-out-trajectory destination for its readers, conditional on creation of the missing ingest.

### External and exclusions

- Evaluated only the already-loaded original URL, `https://arxiv.org/abs/2610.08902`, for a future ingest's `derived-from` edge. No external prospecting.
- No discovery into work or instructions. No extra destination collections were inferred from conceptual similarity. No library artifacts or navigation files were changed.

## Connections Found

These are proposed outbound edges for the future ingest, not for the snapshot.

- [Original paper](https://arxiv.org/abs/2610.08902) — **derived-from**: the future ingest's analysis is worked out from this captured paper; the URL carries source identity while the ingest will carry Commonplace's interpretation.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) — **is-evidence-for**: frozen weights and fresh actor contexts leave inherited tools, rules, and memory as the persistent adaptation channel; positive held-out trajectories provide a bounded witness that this channel can improve later performance. Negative trajectories show that retention and structural acceptance do not guarantee gains.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: Section 3.5 and Appendix G separate available-but-unused covering artifacts from used artifacts with remaining failures. This makes storage, observed use, and benefit separately inspectable; semantic judgments and execution traces do not establish causal uptake.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — **is-evidence-for**: held-out score curves and learning costs assess what inherited artifacts buy rather than how many were written; high reuse with different task scores demonstrates why invocation is not the outcome metric.
- [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) — **is-evidence-for**: the NetHack prayer-controller case and the chess opening-book bypass show that a saved guard can exist yet miss the actual action path. These are concrete path audits, not causal validation of every proposed cue method.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **rests-on**: interpreting the paper's diagnoses depends on distinguishing observational reuse from an intervention, whole-lineage gain from an individual artifact's effect, and experience value from extra artifact-development computation. The paper explicitly leaves these separations unresolved.
- [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) — **compares-with**: both separate persistent edits, use, and benefit; cross-pairing updater and consumer models in Harness Updating addresses a role confound left coupled when Agent Plasticity uses the same model for acting and reflection. Agent Plasticity adds cost-normalized held-out checkpoint trajectories.
- [Continual Harness](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) — **compares-with**: reset-free mid-episode edits contrast with fresh-context inheritance between checkpoints. Both expose capability-dependent gains and artifacts that are written but not reused, while their differing state persistence prevents direct score comparisons.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) — **compares-with**: memory perturbation tests causal dependence on experience content; Agent Plasticity's logs and semantic annotation diagnose availability, use, and residual failure without identifying that dependence. Each supplies a measurement missing from the other.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) — **compares-with**: both retain executable skills alongside textual retrieval handles. Voyager's critic-success promotion and prompt/runtime library split contrast with structurally validated inventory revisions and decision-level reuse auditing; the comparison helps design tests beyond library growth or availability.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) — **compares-with**: retained project lessons and a narrower editable instruction surface contrast with deliberately evaluated artifact lineages. The paper's protocol shows how later capability and acquisition cost could be measured without assuming that retention or advertised compounding supplies such evidence.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) — **see-also**: Commonplace explicitly lacks first-class activation and behavioral-effect metrics. This is the operational landing for evaluating whether availability/use/outcome diagnostics would address that gap; the paper does not validate Commonplace's current architecture.

## Bidirectional Candidates

- [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) ↔ future Agent Plasticity ingest — **compares-with** in both directions under the sources contract: its readers gain a held-out learning-cost trajectory protocol, while Agent Plasticity readers gain updater/consumer cross-pairings. Author neither edge until the missing ingest exists.

## Reverse-edge Candidates

The notes contract permits notes→sources **evidenced-by**. These prospective citations must target the future tracked ingest, never this local capture. Context should say “qualifies” or “bounds” rather than claim independent corroboration without checking claim/evidence provenance.

- [Knowledge-access architecture must be evaluated end to end](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) → future ingest — **evidenced-by**: the high-reuse/different-score comparison and failure-denominator distinction provide a bounded empirical case for keeping access/use and final task quality separate. They do not test the synthesis's complete architecture or upkeep costs.
- [A retrieval miss is a local reflective-path failure](../../../../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) → future ingest — **evidenced-by**: failure coverage at individual decisions supplies a task-local absent/unused/used diagnostic. The citation must not equate every unused artifact with a retrieval miss: a covering artifact may have been read and then ignored, or bypassed at execution.

## Off-authorisation Candidates

None. The tags authorization mismatch was noticed during traversal, but topical head links were rejected rather than promoted as meaningful off-authorisation edges.

## Raw Text Candidates

None.

## Rejected Candidates

- [Retained theories may improve sample efficiency under structured shifts](../../../../notes/retained-theories-may-improve-sample-efficiency.md) — a tempting efficiency match, but plasticity's dollar denominator and opponent-difficulty shift do not test the note's target-observation or retained-theory comparisons. Do not present the paper as support for those conjectures.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — useful interpretation guardrail, but the paper measures learned task capability per acquisition cost, not the earlier gain's causal contribution to later improvement productivity. No positive compounding evidence edge.
- [On the Fragility of Self-Improving Agents](../../../../sources/on-the-fragility-of-self-improving-agents.ingest.md) — repeated-run and order sensitivity are valuable evaluation cautions, but a fourth adjacent source edge would dilute the more discriminating role-separation, state-persistence, and causal-dependence comparisons. It is not evidence that this paper's specific results are invalid.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) — operationally relevant, but its measurement section is already reachable from the selected coverage page; no second same-purpose reference edge.

## Index Membership

None. Sources are outside declared tag participation, and neither the immutable snapshot nor a nonexistent ingest should be inserted into a durable head. The sources README is a collection orientation, not a per-source roster.

## Synthesis Opportunities

None. The candidate higher-order claim that artifact presence, use, and outcome require different measurements is already expressed in the storage/activation note, effects requirement, and end-to-end synthesis. The paper offers new measurement detail, not yet a distinct synthesis claim.

## Maintenance Observations

- The name-paired ingest is absent. A separately authorized ingest/grounding operation must retain source identity, provenance, checksum, analysis, and sufficient quotes before any durable source-dependent claim is added. This report does not create that authority surface.
- The sources contract names tags as a prospecting destination but supplies no sources→tags labels. Current discovery can use heads for routing, but a future need for a genuine source→head edge would require a contract decision; do not silently use `see-also`.

## Flags

- **Do not conflate measurement levels.** Decision-level reuse includes successful decisions; failure-composition shares condition on identified failures. Neither is the overall game failure rate. Failure after use does not distinguish artifact defects from application defects.
- **Protocol-relative efficiency.** Dollar-based plasticity depends on prices, score headroom, horizon, saturation-fit assumptions, and extrapolation. It is not a universal model ranking or a target-sample-efficiency measure. Learning costs include rejected reflection attempts but are not full lifecycle or evaluation costs.
- **Domain boundary.** Board-game OOD tests stronger opponents, not cross-task transfer. NetHack changes game seeds across checkpoints and uses different native agent harnesses; preserve those conditions when importing comparisons.
- **No source split recommendation.** This is a multi-assertion scientific paper, but it was not connected to five or more notes across three independent topic areas. The kept note edges form two tightly coupled areas: persistent artifact adaptation and its evaluation. Any later KB claim should still be written at its own evidence grain.
- All proposed local durable citations are blocked on the missing ingest. Discovery itself is complete; no library changes were made.
