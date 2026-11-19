# Requirements source-ingest trace audit

## Outcome

**Five ingests were cleanly published through isolated Sol drafting workers. No hidden drafting, publication, checksum, or ownership failure was found. Connection discovery was narrower than its `standard` procedure requires; its clean structural validations do not establish comprehensive discovery.**

The source phase is not full acquisition success: the Gunter 2000 journal paper and Jureta 2009 journal article remain unavailable through the bounded routes attempted. The recovered Jureta 2008 conference preprint is correctly separate, not a silent journal substitute. These acquisition blockers were reported, not concealed.

No fixes, tracked writes, commits, delegation, or session deletion were performed by this audit. Its only authored output is this ignored report. Recommendations below require a separate authorized action.

## Scope, evidence and method

Audit date: 2026-11-16. Producing auditor: `openai/gpt-6.1-sol`, under the operator's source-trace-audit invocation. Instruction identity is the audit task in execution record `b8f91f43-edf4-493d-af0e-9ce23fd1ce66` under session `01a1e66a-0dd7-72f0-bb31-0cd24bd9da02`.

Root: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-16T21-34-14-594Z_01a1e648-3641-76fa-81f9-147537bfa624.jsonl`.

Scope begins at root user message `edceef97` (the requirements-engineering commission), including the later audit request `422b684d`. Earlier terminology editing and its commit are prior-phase work, not defects or writes of this phase. Root orchestration after the commission was inspected for assignments, worker launch results, review routing and output reconciliation. The root session is live; this is not a verdict on its eventual final completion or commit.

Descendants were discovered from parsed `execution.json` records using `parentSessionId`, then cross-checked against actual `subagent` calls/results. They were not inferred from similar filenames. The five named sessions have exactly five drafting descendants, with no further descendants. Ten sessions form the exhaustive automatic-work cohort:

| Role | Session ID | Parent | Execution directory ID | Tool calls |
|---|---|---|---|---:|
| Read-only reconnaissance | `01a1e651-3bb5-7048-9520-1f825a71924c` | root | `010a5b8e-76a7-4dac-8b60-47b1b7d90a0b` | 51 |
| Foundations orchestration | `01a1e653-fa5c-73da-8e4c-7961398be50a` | root | `24166f04-e3b0-4bb4-adb6-e413bfc7f589` | 82 |
| Adaptation orchestration | `01a1e654-3221-766f-9377-e20f40c47fb6` | root | `7d0d55c2-e59d-43a2-985d-c2a1145c89d0` | 111 |
| Acquisition recovery | `01a1e65c-9122-7258-9ae9-61149988a951` | root | `faf1c1cf-237f-4de2-b4ac-15922cef8bd0` | 46 |
| Jureta recovery orchestration | `01a1e662-704b-74ca-b52d-72fd43680e38` | root | `93adbd96-c1b0-4256-895b-6b919c3e91f9` | 58 |
| Four Dark Corners drafting | `01a1e656-7e12-7595-9300-5a52276c2734` | foundations | `98c61621-480d-4a2b-a4b1-0362ab7ba313` | 12 |
| RELAX drafting | `01a1e657-409c-7497-bfe8-ac52e4921774` | adaptation | `65642f87-2528-48e5-9aab-3b41e7694123` | 17 |
| Awareness drafting | `01a1e65c-229b-76a2-a339-4b421531e397` | adaptation | `c90f434d-a169-433b-8042-abd74ae54364` | 17 |
| Horkoff drafting | `01a1e660-aad6-717b-8020-d247ab879bf4` | adaptation | `b7418d4d-c434-401e-bc48-e97fff647721` | 16 |
| Jureta drafting | `01a1e665-7153-74e3-aa68-bb238f86b299` | Jureta orchestration | `91d51b8f-3228-4cf0-ad78-825b3ed72f4d` | 16 |

Locator convention: each execution directory is `<sessionFile>.subagent/<execution-directory-ID>/`, beside the session file reported in its `execution.json`. The base directory is `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/`. Each contains `execution.json`, `events.jsonl` and `stderr.log`. Tool-call locators below use the unique `call_...` portion before the provider's `|fc_...` suffix.

Coverage: parsed all ten complete session JSONLs and all ten complete execution/event records; enumerated all **426 actual tool calls**, their results, model records and writes. Examined command bodies, dispatches, error/exit signatures, truncation boundaries and recovery reads, validation/publication results and relevant streaming tool events. All execution records ended with exit 0 / stop; streaming events had paired tool starts/ends and no error-stop event. All ten stderr files contained only session-identification telemetry. Process exit 0 was not used as evidence that every command succeeded.

Read the four result ledgers in full, current ingest/connect instructions, source/report collection contracts, all five handoff YAML records, current ingest/capture metadata and the ten connect discovery traces. Recomputed all five current Markdown snapshot hashes and inspected original Quotes. Compared discovery claims against actual commands, not just their ledgers. The audit did not rerun ingestion, network acquisition or drafting. Retained validation results were inspected, not replaced by a new validation run.

Excluded: workshop author `01a1e669-a617-7142-a94e-fa90ca0fd055`, workshop review/final integration, and this audit's own execution. Independent source-fidelity review sessions are auxiliary parent evidence, not part of the ten-session exhaustive trace cohort; this audit does not claim to repeat their semantic reviews. In particular it is not an independent line-by-line scientific review of all five papers. No allegation below depends on an inferred scientific misinterpretation.

## Material findings and dispositions

### F1 — Unresolved: standard connect recall was reduced by filters and hit caps

The six required source destinations were not wholly omitted in the prepasses: theory, reference, historical agent-memory systems, agentic systems, tags and other sources all appear in the loops. Work/instructions were correctly excluded; external connect prospecting was correctly skipped. Title-output truncation in the initial broad scans was recovered (details below).

However, two adaptation prepasses expose only a keyword-selected subset of titles to the model, rather than the required complete claim-title surface:

- Awareness, adaptation `call_cd06e3e0c9bf4222af503592051e7a63`: H1 output is piped through `grep -Ei 'requirement|goal|observ|monitor|diagnos|feedback|crit|revis'`. Description matches are capped with `head -8`, as are body-hit filenames.
- Horkoff, adaptation `call_4a9a736f256544f3a4e7de34fbc906a3`: H1 output is piped through `grep -Ei 'intent|goal|authorit|model.*use|writing.*thinking|understand'`. Description matches are capped at six; body-hit filenames at ten.
- RELAX, adaptation `call_f18802235bb545248e508140151a41a9`: complete title recall did occur separately, but its subsequent description/body discovery discards matches after ten/six results. The report discloses the description cap, but not the body cap.

Generating a full stream inside a pipeline is not the same as reading the full title surface. `head` selects by traversal/output order, not by relevance or a collection trigger. These are real procedure reductions, not `rg` no-match errors. Awareness/Horkoff reports say they scanned a subset, which is more honest than claiming to have read every title, but still label depth `standard` without a reduced-coverage disposition. An earlier full RELAX title scan gives useful context; it does not make the later new-source-specific standard pass complete.

Consequence: keep the accepted ingests, but do not describe their graph discovery as comprehensive. There is no demonstrated missing indispensable link; this is an unresolved recall/assurance gap, not evidence that their retained comparisons are false. Structural validation cannot detect omitted candidates.

Recommendation: under new authority, rerun affected connect discovery without prefiltering the complete title surface or silently capping candidate lists; otherwise explicitly accept and report reduced discovery coverage. No redrafting is indicated solely by this finding.

### F2 — Unresolved: post-ingest discovery reused prepasses instead of completing a new standard pass

All five accepted ingests have separate nonempty post-connect files, correct `source` fields, successful validation, an actual accepted-ingest read and a read of inbound candidate sections. This is not a wholly skipped postpass. But most of the discovery trace is carried over from snapshot discovery:

- Foundations `call_da7009c0bcaa42d08cf22285e653cce4`: regenerated H1 streams are piped to `wc -l`, so the parent sees counts, not their title contents; a fresh focused body query covers all six. `call_8aff36ab6b0043ddbde46678b4100448` builds the post report by modifying the pre-report text.
- Adaptation fresh post queries (`call_003ccc8a331c40f387df29555d012a7c`, `call_fc5bc46d4009475cb69354dfd7ca2997`, `call_fca37d7a225b4e43847f1b61d38497e6`) search theory/reference/sources plus selected targets, not fresh full title/description discovery across all six. Their post-report commands copy and amend the pre-reports (`call_5f4cc758d5604c8399b7b613972fa85c`, `call_7db94009efeb4d8a8a0d5bddcdd4af3c`, `call_2a3d707318a54825bb6bd068cde70ad7`). Some fresh queries also use `head` caps.
- Jureta `call_43b3848c9e5c4413aeef8da555da60bf` makes a useful fresh six-destination body pass and checks inbound articulation. Its post-report explicitly reuses same-run heads/title/description scans; it does not regenerate the complete title surfaces for the new target.

The reports largely disclose reuse, so copying is not itself fabrication. The unsupported stronger claim is that validated, separate reports amount to the full per-target `standard` procedure. The difference matters because the accepted analysis can foreground concepts that the raw snapshot/prepass did not select. Same-run reuse limits cost but was not an authorized quick-depth substitute here.

Recommendation: report post discovery as performed but methodologically reduced; rerun only connect if full standard assurance is needed. Do not discard already clean source outputs or treat advisory inbound suggestions as authored links.

### F3 — Unresolved acquisition coverage, correctly reported

Gunter journal DOI `10.1109/52.896248` remains blocked. `fre.html` was a bibliography mention, not a paper link. Foundations tried metadata-backed publisher, historical author PDF and CiteSeer routes; recovery tried bounded public search/author routes. Neither an abstract nor the separate ICRE extended abstract was ingested as the journal article.

Jureta journal DOI `10.3233/AO-2009-0069` remains blocked (resolver/publisher/repository access failures and no usable OA PDF). Recovery acquired the separately named RE 2008 paper, arXiv `0811.4364v1`, DOI `10.1109/RE.2008.13`. Its served bytes' 2018 date is disclosed, not explained away. This restores the conference-paper branch of the commission, not the journal article.

Evidence: foundations curl calls `call_c3c07ea4c7964114a15381bca010fc65`, `call_aa17dc8628a24f44852df35e733b4f32`, `call_04dab299c7314bf9821de22cd9f1e0d3`, `call_cd4b5d60f68c4c55b40fa0210b628967`, `call_76250f0abbe0454b94ea7425d8ea5712`, `call_e17230c7c8c2446590d8999777df4c47`; recovery `call_058e6ededc444236905d7c66e43bc8fa` (TLS hostname failure, no verification bypass), `call_9fcd4abf1ba549e9bab53c55d89fca28` (versioned conference PDF). Route and scope details remain in the acquisition/foundations ledgers.

These are task coverage blockers, not silent tool failures or false success. Recommendation: retain them in final completion wording; obtain authorized exact journal copies if those branches must be completed. Do not infer that no public copy exists anywhere.

## Recovered errors and harmless telemetry

| Observation | Evidence | Disposition |
|---|---|---|
| Four Dark Corners initial HTTP 406 | foundations `call_cd08add8ebff4651b956bc0472e27d3d`; browser-UA retry `call_4652cded1448436c9238a61f4f2e4fb0` | Recovered public acquisition; subsequent PDF extraction and snapshot completed. |
| Pre-connect snapshot hyperlinks triggered one warning each | foundations `call_efcfa5e303e549ae9f8a99d1543cd4cc`; adaptation `call_5514b8d187204dd993ce0ade56ee6e89`; Jureta `call_52c7cc83953749dd88012952223abecd` | Recovered by replacing only operational snapshot link syntax with plain code paths; reruns clean before dispatch. No snapshot bytes changed. |
| Requirements-reflection guessed path ENOENT | adaptation `call_d3a2a1d37b274edca910b0410552cc79` | Recovered to `requirements-reflection-runtime-entities.ingest.md`, then fully read. |
| AGM guessed path ENOENT | Jureta `call_1cf8e87fd0004fa4b8a3f73412a82e5a` | Recovered by exact-title lookup and reading `logic-of-theory-change-partial-meet-contraction.ingest.md`. |
| Wrong snapshot-type path `.agents/types/snapshot.md` | acquisition `call_5100e567d111416c9171cdca9bbe4e2b` | Recovered after resolving skill symlink to canonical location and reading `kb/types/snapshot.md`. |
| Search-response UTF-8 decode exception | acquisition `call_8ad2654857b9497f9ec5c8a79dfe6c43` | Recovered by `call_8f8a6e4fcdf34bfda1b8f1f2ee85747a`, using replacement decoding for link discovery, not source snapshot cleanup. Source extraction bytes were copied unchanged. |
| Guessed changing-requirements filename ENOENT | foundations `call_40110c447170470c999acbc199d118e0` | Optional lead abandoned; no subsequent claim that this file was read. Not a source-ingest blocker. |
| `which commonplace-snapshot` returned no command | adaptation `call_2f372430e2de4f12a36265b53dca50f0` | Nonexistent convenience-command probe, not an attempted capture. Existing curl/Poppler path was used; no install or false snapshot success. |
| `rg status:` found no handoff YAML field | adaptation `call_745a42081e2e48458b627b11f3f53fd4` | Wrong probe field (`outcome` is the real key); later `call_ce5f13f9eb6b4677817dc824fb77ccbf` reads actual YAML tails. Current records all published. |
| Empty PDF metadata stream | capture metadata reads | No embedded metadata is not failed extraction. Title pages, pdfinfo and external metadata supplied identity evidence. |
| `rg` exit 1 | exact duplicate searches, `jApprox` search and similar queries | No matches is expected evidence, not automatically failure. Final commands sometimes determine the shell's aggregate exit status; outputs were examined separately. |

### Read completeness

All five drafting workers recovered their source-read 50KB truncations, with no source-text gap found. First read / continuation offsets: Four Dark Corners 1–932 / 933; RELAX 1–1046 / 1047; Awareness 1–912 / 913; Horkoff 1–873 / 874; Jureta 1–764 / 765. Orchestrators likewise completed their snapshot reads; Horkoff's parent used two explicit chunks at 700/701. Short initial extraction reads were identity probes, not a substitute for these full snapshot reads.

Complete initial title scans were also recovered correctly: foundations `call_0bfad2e0308047a9b56b7739bda4e896` returned lines 533–1669, followed by retained-log read 1–535; adaptation `call_204d0c27b7564f9bb3d98bba63e4633d` returned 525–1663, followed by read 1–525; Jureta `call_764a65afafc3482c92f773e1c8548cb2` returned 529–1673, followed by read 1–528. The extra-lines notices on these prefix reads do not establish an unread gap: the remaining suffix was already visible in the original command result. Foundations description-output prefix recovery similarly overlaps its visible suffix.

Jureta's noisy initial body query was truncated and replaced with narrower queries; that is a search-coverage limitation, not a missing paper read. Reconnaissance retained some partial contextual reads (including conceptual blending, commitment-support proposal, retained-theories note and workshop exploration), and broad searches were truncated/narrowed rather than fully consumed. Its output is a selective starting map, not an exhaustive literature/KB review. These partial contextual reads did not enter fresh drafting briefs as inherited conversation.

### Masked exit-status risk

Several commands use `;` rather than fail-fast chaining: metadata/extraction followed by `wc`, snapshot assembly followed by cleanup/prepare, validation followed by status/sha/listing. A later successful command can mask an earlier failure. The audit checked their retained outputs and downstream artifacts; no actual missed extraction, assembly, handoff or validation error was identified. All publication-critical checks print clean results, and four orchestrated publish chains use `&&`; Jureta uses separate check/publish calls.

Examples: foundations `call_6e4de9208f864fc9b5d5400f20ed9a03`, adaptation `call_ba4a892a44fd448bbd334cc453f02175`, Jureta `call_e6e14aa6b27e477ca680271dc51a1728` and `call_5689d90c37dd456f8a9739da3e41d61d`. These are robustness recommendations, not proof of corrupt output. Future runs should preserve per-command exit status or use fail-fast sequencing where success is consequential.

## Isolation, authority and publication checks

- Every cohort execution requests `openai/gpt-6.1-sol`; actual assistant provenance and model-change records agree. Every session has one user task message. All five drafting sessions are new single-use launches, not resumed sessions or forks. Execution records show project `commonplace-worker` with repository cwd and leaf depth/worker budgets 0/0. Orchestrators have 1/1 only where drafting was authorized. No shell-launched agent CLI or unrecorded nested worker was found.
- Each drafting task is the prescribed standalone dispatch: instruction path, snapshot, pre-connect path, output/candidate paths, pinned checksum, retained Quotes path, handoff record, no code grounding, verbatim pre-reading occasion and `validation_failures: none`. No parent reading, source-specific interpretation, acquisition ledger or commission's substantive source hypotheses were added to the fresh drafting task. Connect reports are interpretive context, but are an explicitly fixed input, not covert extra briefing.
- Drafting workers read the standalone instruction, source/type contracts and paired snapshot, checked the checksum, wrote only their candidate, and ran handoff validation. Conditional learning assessments were loaded where applicable. None invoked ingest/connect/snapshot orchestration or spawned another worker. No replacement or local drafting fallback was used.
- Source writes in orchestrators were snapshot assembly plus `commonplace-ingest-handoff publish`, not parent-authored ingest prose. Other direct writes are owned ledgers, capture headers, connect reports and handoff state. Jureta's acquisition-ledger append and deletion of the exact temporary directory were explicitly authorized in its invocation. No cohort worker staged/committed or edited navigation, skills, other library notes or the workshop.
- All five records have `incumbent_sha256: null`, three successful checks, and `outcome: published` with `ended` timestamps. Prepare precedes discovery/dispatch; worker and parent checks precede publication; post-connect follows publication. No opened handoff remains in this cohort. The blocked journal branches opened none.
- Missing `candidate.md` files after publication are expected, not lost failed drafts: `src/commonplace/lib/ingest_handoff.py` unlinks the candidate after publication (line 435 in audited checkout). Session write payloads and published ingests retain the content. Handoff directories and retained-Quotes files remain.
- All five current Quotes sections are exactly the canonical empty section and equal the retained empty quote block. Empty Quotes is permitted here, not a failed extraction. Future source-dependent claims cannot treat those empty pools as retained evidence; ground them or use the declared snapshot-required consumption path.

## Output reconciliation and capture integrity

All paths below are under `kb/sources/`; each slug has `<slug>.ingest.md` and exact paired `.snapshots/<slug>.md`. For every slug, pre/post connect files exist at `kb/reports/state/connect/sources/<slug>.connect.md` and `<slug>.ingest.connect.md`, and handoff state at `kb/reports/state/ingest/<slug>/handoff.yaml`.

| Slug | Current exact Markdown SHA-256 | Scope/version |
|---|---|---|
| `four-dark-corners-requirements-engineering` | `c099591707df1352d907aca025aff617e9464d096a3c09585f569746b68e3704` | Full 35-page author manuscript text, dated July 1996; not verified 1997 journal pagination/text. |
| `relax-uncertainty-self-adaptive-systems` | `f212c669171101192a51f02dee34747054f684a210b4c51524f7a5e8f169e1aa` | Full ten-page Aston repository manuscript extraction; canonical conference DOI retained. |
| `awareness-requirements-adaptive-systems` | `c21c3462537ab42498d65008dc43aa729199076a203e10929629ea2b26c6c349` | Full ten-page supplied PDF extraction; SEAMS 2011 DOI verified, not similarly titled runtime workshop item. |
| `horkoff-gore-mapping-reflections-2026` | `8aec99a99f1982411637d031cdfc072425a94dd0425939a8ca626bbbe6a35a79` | Full fifteen-page publisher extraction; 2026 reflection, not a new comprehensive mapping. |
| `revisiting-core-ontology-requirements-engineering-2008` | `3fd5ccf2031710b6ef8aafae9cd10dc890050d03be2207c83d2cd19c2a9895cf` | Full served 22-page arXiv v1 conference-preprint extraction; unresolved 2018 date caveat retained. |

Current hashes agree with ingest metadata, prepare records, worker checks and publication checks. No re-pinning or snapshot mutation after preparation was found. Metadata canonical-source values pair correctly. Captures are complete text extractions, not pixel-faithful copies; nontextual graphics/formulas remain a limit. Acquisition assembly calls compare the complete extraction bytes to the snapshot body, rather than relying on model transcription. Jureta additionally checks nonempty extraction from all 22 pages (`call_749e20ab71ae42f98e8fa27179cd2dac`), then the ingest parent verifies header+body equality before cleanup (`call_de94c8c00c4f41fcb68664b6d89967e9`).

Raw PDFs/downloads were confined to ignored `kb/reports/state/snapshot-web/` directories; full Markdown copies remain ignored under `.snapshots/`. Current `git check-ignore` confirms all five snapshots and this report's ignored status. Git-visible source additions are the five ingests; no tracked diff or staged change from the cohort was found. Temporary capture directories were removed after assembly. Jureta recovery's initially retained raw PDF and route bodies were subsequently removed under explicit authorization (`call_5e27a5177f454befa0f67c8f2c15466d`), with an append preserving summaries and hashes in `acquisition-recovery.md`. This is not deletion of session/audit evidence.

Reproducibility limit: current Markdown hashes can be independently checked, but deleted raw PDFs cannot now be re-extracted or visually compared locally. Retained commands, metadata/results and checksums support the capture history; this audit cannot certify graphical completeness or byte identity of a future download. This is a disclosed preservation tradeoff under the snapshot procedure, not a reason to claim immutable PDF evidence still exists.

Retained validation evidence reconciles with the ledgers: five worker `HANDOFF CLEAN` results; five parent clean checks and successful publications; five final ingest validations; ten final connect validations with zero failures/warnings. Initial snapshot-link warnings were repaired before dispatch. None of these results validates discovery recall or proves the papers' substantive claims.

Post-connect inbound suggestions remain advisory, not authored edges:

- Four Dark Corners: reverse candidate from Exact implementation; bidirectional None.
- RELAX and Awareness: bidirectional candidate from Exact implementation; reverse None.
- Horkoff: bidirectional conceptual comparison from Intent-framed delegation; reverse None.
- Jureta: bidirectional candidate from Exact implementation and reverse candidate from Proximate target.

Each suggestion requires its own reader need and grounding before authoring. No result ledger falsely reports that these library links were added.

## Recommended parent disposition

1. Accept the five published source analyses as publication/trace-clean, subject to the separately commissioned semantic reviews. Do not rerun drafting merely to repair discovery coverage.
2. Carry F1/F2 as unresolved reduced-discovery findings. Either authorize connect-only reruns or state the limitation explicitly; do not equate zero validator diagnostics with comprehensive connection search.
3. Keep the Gunter 2000 and Jureta 2009 journal gaps visible. Report the 2008 preprint separately. Do not claim every commissioned exact version was acquired.
4. Preserve these sessions, execution/event/stderr records, handoff directories and ledgers. No new source-fidelity assurance can be inferred from their process exit codes alone.
5. Audit workshop authorship/review/integration afterward, as requested. Nothing in this report approves its eventual claims, source-link grounding, navigation or commit.
