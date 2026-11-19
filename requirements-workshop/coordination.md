# Requirements workshop coordination

Commission: 2026-11-16, operator requests six principal-source ingests and a bounded workshop on Operationalization, Goals, and Grounded Concepts. Work on main; parent plans/verifies and commits; Sol workers do bulk work. No large experiments, theory promotion, broad literature review, or procedure changes. Terminology change already committed in 86639599f; preserve its narrow scope.

## Plan

1. Read-only KB reconnaissance and duplicate check before mutations.
2. Ingest six principal sources through cp-skill-ingest, with fresh isolated Sol drafting workers. Verify bibliographic identity and capture scope. Reuse existing sources if appropriate; report blocked captures rather than inventing evidence.
3. Sol author creates a compact workshop and navigation entry from accepted ingests and KB evidence. Six distinct research threads and four discriminating candidate experiments; no implementation.
4. Independent Sol review; parent verifies evidence, links, validation, diff.
5. Operator addition: after automated work, inspect parent and all nested worker session/execution traces for hidden failures, recovered versus unresolved errors, omitted checks, unfinished handoffs, model/isolation and scope violations, and differences between outputs and success claims. Record bounded findings; fix material issues before commit.
6. Commit explicit deliverables after verification and trace audit.

## Assignments

- 4e07e66d-b97c-4964-9ec9-350f4eaf0055: Sol read-only KB reconnaissance; completed, no existing principal ingests found. Session 01a1e651-3bb5-7048-9520-1f825a71924c. Key neighboring workshops: operationalization-executability-automation, epistemic-relevance-and-conceptual-blending, open-ended-work-economics, chatbot-goal-state, theory-refinement-interface. Their conjectures are not findings.
- ccd6c61d-e7e6-45aa-ac61-283f757e88b1: Sol foundations source orchestration (Zave/Jackson; Gunter et al; Jureta et al), owns only corresponding source/state files and foundations-results.md; one reserved fresh drafting slot. Pending.
- af4192ea-4995-427a-a28b-7f4d42c6dc0b: Sol adaptation source orchestration (RELAX; Awareness Requirements; Horkoff), owns only corresponding source/state files and adaptation-results.md; one reserved fresh drafting slot. Pending.

Foundations first pass completed: one full manuscript ingest (Four Dark Corners, 1996 manuscript for 1997 article), two acquisition blocks. Details: foundations-results.md. No unfinished handoffs.
- 00d2b3d7-dcde-42ea-acba-a97dd0bdaa20: Sol acquisition-only bounded second look for Gunter/Jureta, owns ignored acquisition-recovery.md and capture artifacts only. No ingestion or tracked writes. Pending.
- 199a0bdb-3875-46df-9189-e0b4c32a03a0: Sol independent read-only Four Dark Corners evidence check. Pending.

Acquisition recovery completed: full distinct RE 2008 Jureta preprint captured; reference-model journal and Jureta 2009 journal remain blocked. a09a1d7d-fc6e-4710-9755-5fca42843788 completed Jureta ingest with fresh drafting; temporary recovery payloads cleaned. Adaptation worker completed all three ingests. Five accepted ingests total, ten connect reports. Parent reran all 15 validations: 0 failures/warnings.

- eb30dd15-aa97-4141-9040-b285c75cdc95: Sol workshop author executing workshop-brief.md; owns new workshop directory plus one navigation entry. Pending.
- bbbe13f4-c138-44d0-85b8-00ccdc170ea8: Sol independent Jureta source review, read-only. Pending.
- dc28951c-b423-4fa3-aa6e-1e6be5436547: Sol forensic source-phase audit including nested sessions; owns ignored source-trace-audit.md only. Pending.

All five independent source reviews completed: no material issues; optional elaborations not adopted to avoid scope growth. Workshop authored in README.md + experiments.md, navigation added. Independent workshop review 8c05fa91-daae-4cde-9dae-be86cfcc64e9 accepts subject to removing three stale Jureta-review statements. Author resumed as 9ed1db51-3021-4ebe-859f-d429bc1e5b2c for that fix, clarification of same-fault comparison, and compact temporal assumption-change variant requested by parent.

Source trace audit inspected 426 calls across ten source-phase sessions (including all five fresh drafters). No integrity/isolation/publication failure; F1/F2: reduced connect discovery due filtered/capped title or candidate lists and reused prepasses. F3: known journal acquisition gaps. Parent authorized connect-only repair, not redrafting:
- 77a3bb10-2589-4307-8487-3e3840ed325b: fresh complete pre/post connect for Four Dark Corners + Jureta, four reports; preserve prior reports in ignored foundations recovery archive, write recovery ledger only.
- 51316a24-c0bb-4e61-b3fb-8fce9e64c561: fresh complete pre/post connect for RELAX + Awareness + Horkoff, six reports; separate ignored adaptation archive/ledger.
No repair worker edited accepted ingests or workshop. Foundations repair completed four passes. Broad adaptation repair stopped without replacement reports; reassigned one source each to f7a067f0-6b5c-459d-89b0-a3b430a896ab (RELAX), ae9c1cc4-0efc-4ecd-8b47-401c430f4f73 (Awareness), 88f60acb-46a9-44d3-920b-4f0d09a6796a (Horkoff). All six replacement passes completed and validated. Candidate deltas are optional traversal improvements, no material ingest/workshop correction.

Final audit bd170075-007c-41b5-9c29-0ed085c87ce6 resumed original auditor and checked 21 descendant sessions/22 completed executions/1093 calls plus root follow-up. final-trace-audit.md closes F1/F2 on actual read/search/recovery evidence; F3 (two exact journal versions inaccessible) remains. It also corrects failed broad recovery's overconservative truncation explanation; failure was unfinished candidate/report acceptance, not proven missing title lines. Parent read final audit, execution/stderr, enumerated all 63 final-auditor calls and checked bash commands/mutations: only authorized final report writes, no tool errors or delegation; concluded no new blocker. Parent independently revalidated all ten current reports, both workshop files and navigation; verified all five snapshot pins/published handoffs and all seven new-file whitespace checks. One parent no-index diff exit-code handling error was recovered by complete rerun and is explicitly in final audit.

Acceptance: five source ingests plus compact two-file workshop and navigation accepted with disclosed access/version limits. All source reviews no material issues. Workshop repair verified directly. No experiments, library theory edits, new terminology rule, or inbound source links authored. Committed eight explicit files on main as 6d671a6ce (Establish a requirements-engineering research workshop). Final validation rerun: all eight deliverables 0 failures/warnings; ten recovered connect reports also validated. Git working tree clean after commit. Do not claim complete journal acquisition. No push performed. Keep source workers' URL/slug ownership disjoint. Ingest orchestrators may reserve one leaf slot, run connect locally, and dispatch only source-isolated drafting to a fresh Sol worker. No commits by workers.
