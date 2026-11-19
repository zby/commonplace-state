# Final requirements-workshop trace audit

## Outcome

**F1 and F2 are closed for the current ten connection reports.** Four foundations passes and six fresh single-source adaptation passes repaired the original discovery reductions. The intervening broad adaptation attempt stopped without replacement reports; it is not counted as successful recovery.

**F3 remains open:** the exact Gunter 2000 journal paper (`10.1109/52.896248`) and Jureta 2009 journal article (`10.3233/AO-2009-0069`) were not acquired. The separately commissioned Jureta 2008 conference preprint does not fill the journal slot.

The five accepted source analyses have substantial primary-reading support from three independent review sessions. The workshop's three stale review statements were repaired. Its matched controls, clarified local-reuse comparison and temporal-change variant are present as proposals, not executed experiments. No material reason to redraft an ingest or change the workshop's recommended first pilot was found in the recovered candidates. Optional new traversal links remain unauthored.

This is a bounded trace and output audit, not proof of exhaustive literature recall or transfer effectiveness. The parent must check this report and any final integration/commit. No repairs, commits or delegation were performed here; this report is the sole authorized output of this invocation.

## Scope and evidence locators

Audit date: 2026-11-16. Root session: `01a1e648-3641-76fa-81f9-147537bfa624`, file `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-16T21-34-14-594Z_01a1e648-3641-76fa-81f9-147537bfa624.jsonl`. Requirements scope begins at root message `edceef97`; earlier terminology work remains excluded.

[Original source audit](./source-trace-audit.md) retains the ten-session, 426-call acquisition/orchestration/drafting cohort, hashes, publication order, isolation checks and original F1–F3 evidence. Those histories are not repeated here. Its authored bytes remain identical to its original write payload.

Rediscovery parsed `execution.json` parent records recursively from the root and cross-checked dispatch results, including the three launches inside root codemode. The discovered graph contains **21 distinct descendant sessions**. There are **22 completed executions**, because the workshop author ran twice. The current auditor is a further, unfinished execution of the prior-audit session; it is explicitly excluded from certification and counts. No additional descendant of the later review/recovery workers was found.

The following **12 completed executions / 667 tool calls** extend the original ten-execution / 426-call cohort. Thus the combined completed descendant cohort is **22 executions / 1,093 calls**, excluding root and the current audit. All 667 later starts have matching tool ends. All twelve executions report `openai/gpt-6.1-sol`, exit 0 and stop; these are process facts, not success criteria. Eight tool results carry error flags; command text/results also reveal failures without such flags, discussed below. Stderr contains session-identification telemetry, not additional execution faults.

| Role | Session ID | Execution directory ID | Calls |
|---|---|---|---:|
| Four Dark Corners source review | `01a1e65c-ec39-707a-8c5e-154afda86942` | `4f23ac70-7bdc-4c05-843d-44d66bcea2c6` | 9 |
| Three adaptation-source reviews | `01a1e664-7f68-74ea-8501-a09643279400` | `95a85093-fe9a-4416-9239-9180511e2d4f` | 24 |
| Jureta source review | `01a1e669-c664-709f-897e-779c195b9f48` | `9848ae62-cafd-4194-9bbe-5822c0b65d50` | 15 |
| Workshop author, initial | `01a1e669-a617-7142-a94e-fa90ca0fd055` | `5e933ac4-aae9-43f8-b761-f692c728584e` | 68 |
| Workshop author, bounded repair | same session | `ef97f8f8-e230-44c6-b01e-7438fae269a1` | 6 |
| Independent workshop review | `01a1e66f-8722-740e-a81a-7dc3f3677aac` | `8bb6f260-8f47-46f7-87fc-63199f61bef2` | 24 |
| Original source audit | `01a1e66a-0dd7-72f0-bb31-0cd24bd9da02` | `b8f91f43-edf4-493d-af0e-9ce23fd1ce66` | 29 |
| Foundations connect recovery | `01a1e671-3b1d-7152-987a-71ba5516dc29` | `260e106a-7570-4c8f-9c0f-b6d706798a92` | 102 |
| Incomplete broad adaptation recovery | `01a1e671-618c-7786-88ea-3ca451d7275b` | `5e813537-e0c0-47b7-80e0-4a932b2fafc8` | 71 |
| RELAX recovery | `01a1e678-02f9-7492-93e0-088d4f89507c` | `3a38873e-47d9-4d3c-8135-f7a496981d2f` | 110 |
| Awareness recovery | `01a1e678-0301-71d3-a497-66ff2e979d22` | `543f5478-1f7d-49cd-859a-978cd6ca5e80` | 103 |
| Horkoff recovery | `01a1e678-0330-74fc-929e-19a51201ab5a` | `899c7908-a116-4c79-b55c-2f5ab7201e96` | 106 |

Execution directories are `<sessionFile>.subagent/<execution-directory-ID>/` in the same session base. Their `execution.json`, `events.jsonl` and `stderr.log`, and the session JSONL named in metadata, are retained locators. Calls below omit the provider suffix after `|`.

Root follow-up was inspected from `2026-11-16T22:18:00Z` through message `e9e4b149` at `22:42:26.374Z`: **21 top-level calls**, including three codemode wrappers containing **15 nested calls**. These counts are separate from descendant counts; wrappers and their children are not interchangeable units. Root activity after that cutoff and the final commit remain the parent's responsibility.

Method: parsed complete later session/event records, paired calls/results and inspected tasks, read ranges, errors, truncation recovery, mutations and validations. Read all five recovery ledgers and all ten current connect reports completely; compared retained originals, current candidate sections and actual commands. Independently checked representative primary passages and newly relevant companion notes. This is not a fresh line-by-line scientific review of every paper or an independent review of every rejected search hit. Retained validation results were inspected; this audit did not run commands that generate replacement state.

## F1/F2 recovery: actual inspection, not command issuance

### Successful foundations recovery

The foundations worker completed four distinct target passes: Four Dark Corners snapshot and accepted ingest, then Jureta snapshot and accepted ingest. Each issued fresh unfiltered H1 commands for all six authorized destinations: theory, reference, historical agent-memory systems, agentic systems, tags and sources. The commands expose title text, not `wc` counts. Examples:

- Pass 1: `call_8cfca8490d0a44579604062f6045243b`, `call_8743fbdd9ecc41a2aac561e5697e7771`, `call_14c60318e9954814b2f021fd295e0b42`.
- Pass 2: `call_856e6cded90148b696fff75bb9953dc2`, `call_fa8300fe49ed4807b4b90132d5091106`.
- Pass 3: `call_3ee33b83786f40e4868e77e8d1e2c636`, `call_deeaa2fccdea4451822755e4d8ea9b65`.
- Pass 4: `call_7d1b2ba0d0504f3a982f2e78fdb01219`, `call_7b01cd9f4c11452196c1378b97549688`.

Separate scoped description/body queries followed for each pass. Pass 4's 176-line search output exceeded 50KB (`call_6a9bba61d11d49e7a931508817c258db`); the worker recovered the full retained log `/tmp/pi-bash-6aad6834bf51939a.log` with `call_ab38be32aa824bc1b6da6953f31538e4`, `call_debd69888c4846ecbb007ff0e267fec4` and `call_12147162d46d40a1b51d6b59d300bdd4`. No unresolved discovery suffix remains there.

The 1,464-line Four Dark Corners snapshot was completely covered by reads at 1/751; the 844-line Jureta snapshot by reads at 1/431. Both accepted ingests were completely read. Contracts and destination heads were loaded; same-session head/candidate reuse is disclosed, while fresh per-target search/title surfaces are genuinely new. Useful neighbors, rejected candidates and independently useful inbound reader paths were evaluated, not inferred from reciprocal outbound edges. Four replacement reports were validated, with two subsequently edited snapshot reports validated again. All final results have zero failures/warnings.

Evidence ledger: [foundations recovery](./connect-recovery-foundations.md); original report archive: `connect-recovery-foundations/` beside it.

### Failed broad adaptation attempt: historical failure, not current recovery

The broad worker issued six fresh title/search passes, then stopped without completing candidate/report/validation acceptance. Its final [incomplete ledger](./connect-recovery-adaptation.md) attributes this to unresolved truncation. **That explanation is too broad for the title evidence:** combining the original bash-visible suffixes with later prefix reads covers all six retained title logs completely. For example, `/tmp/pi-bash-bbd545c1ea1dc256.log` originally exposed 534–1668, and its recovery prefix overlaps that suffix; `/tmp/pi-bash-02c6c9271fa52f4d.log` originally exposed 99–1231, with its prefix recovered. A recovery read's own truncation does not establish a gap when the original result already exposed the suffix. This audit therefore does not affirm the ledger's claim that complete title inspection was unestablished. It also does not retroactively finish its candidate evaluation or reports.

The ledger correctly withdrew completion, supplied no settled new candidate set, and wrote **no replacement connect reports**. Its six archived incumbents matched the current reports at that attempt's end (`call_f5513451b3824b1b8500c938a0c73b8d`); later differences are the separately authorized single-source replacements, not evidence that this historical statement was false. No replacement validation occurred in that attempt. Its process exit 0 does not mean six passes succeeded.

Root read the incomplete ledger (`call_88eb814bc00849ea966306ca2b445b74`) and commissioned three fresh workers via `call_f295aa472ba2493cab4a8626a1dfda18`; it did not resume the failed investigation or count it as completion.

### Successful single-source adaptation recovery

Each new worker read its complete snapshot and accepted ingest, loaded the connect/type/source contracts, and completed two separate standard passes. For each pass, all six destination heads and newly generated complete title surfaces were inspected, followed by uncapped scoped description/body results. No keyword-filtered title pipeline, `head` cap or counts-only title substitute was found.

| Source | Snapshot lines | Fresh title-generation calls, snapshot / ingest | Retained evidence directory |
|---|---:|---|---|
| RELAX | 1,091 | `call_686b20a1845e4c8d808f74b7221a6525` / `call_3afb1daa00b740c6b6121923f85448d8` | `recovery-relax-uncertainty-self-adaptive-systems/{snapshot,ingest}/` |
| Awareness | 990 | `call_e0e0f71433ab47e7bf79642965683a5a` / `call_0256fd26b4514cae877388b566566801` | `recovery-awareness-requirements-adaptive-systems/{snapshot,ingest}/` |
| Horkoff | 1,381 | `call_4d10b8bb182442c7ad1ee0a7bfa0bb83` / `call_8a6d8aa16d304967910190c5a1780766` | `recovery-horkoff-gore-mapping-reflections-2026/{snapshot,ingest}/` |

These directories are under `kb/reports/state/requirements-workshop/`. Each pass has actual separate title files: theory 436 lines, reference 252, historical systems 175, agentic systems 156, tags 34, sources 609. Inspection was verified from successive read calls/results, not these counts. Reconstructed coverage has no missing lines in their saved title/search surfaces. Readable search files retain commands and return codes; no-match exit 1 is not a failed search operation. No target tags required a matching-tag membership scan. Work/instructions stayed outside discovery; external prospecting was skipped, not falsely claimed.

RELAX's large snapshot body-search files required extra reads: theory lines 121–153 and sources through 137–141 completed the visible prefixes. The sources read at 66 was itself truncated at 136 and then continued at 137. Awareness/Horkoff's bounded discovery reads had no unresolved truncation. The ingests (68, 68 and 64 lines respectively) were fully read for their own passes; no pre-report copy with amended metadata substituted for post discovery.

Reports distinguish `known` candidates from fresh exposure, re-exposure and useful link following. Prior candidate bodies can inform later evaluation without making their origin independent; the current reports explicitly disclose that reuse. No consequential false candidate-origin claim was found. Full reads support retained candidates; search-level rejections do not pretend to be complete reviews. Independent inbound assessment survives snapshot immutability and does not automatically mirror outbound comparisons.

All six final reports have retained zero-failure/zero-warning validations. Horkoff's initial unquoted YAML date failed schema validation (`call_d91c0c7a71364b93ac7eaa237710bfc3`); quoting it and rerunning (`call_92e1fd15cb8a490fb6d17316fe6de94b`) recovered the error. The three source-specific recovery ledgers and current reports agree about completion and non-material interpretation effects.

**Disposition:** the procedural bases of F1/F2 are repaired for current outputs. This establishes the commissioned standard search process, not that no relevant candidate exists outside it or that every title was judged perfectly.

## Candidate changes and material impact

Compared `## Connections Found` destinations in each preserved incumbent with its current counterpart. The deltas below exclude unauthored inbound/index suggestions. A newly listed edge can already be present in the ingest; it is not necessarily newly discovered substantive content.

| Pair | Principal changes | Independent impact assessment |
|---|---|---|
| Four Dark Corners | Both reports add checked-or-absent derived copies and Jureta 2008. | Recomputable repository quantities have a stronger oracle than empirical domain assumptions; Jureta supplies a contrasting ontology. Neither alters the source's conditional S/K/R argument or warrants adopting a new schema. |
| Jureta | Both add Awareness; accepted-ingest pass also adds ATMS. | Monitoring a selected metric and maintaining conditional assumption support do not establish the approximation's warrant. These sharpen an already explicit boundary, not a missing empirical result or journal-version substitute. |
| RELAX | Adds Awareness, Requirements-Aware agenda and DOI; snapshot report also adds Fixed decomposition. Requirements Reflection was already a candidate. | Separate satisfaction flexibility, monitor implementation and proposed runtime synchronization. Existing ingests already deny a complete implemented learning/adaptation loop. Shared 2010 architecture is not independent corroboration. |
| Awareness | Adds Objective revision, Requirements Reflection and SkillRL; accepted-ingest report also adds Jureta. Removes Final task success as an outbound candidate. | SkillRL's aggregate-success trigger has a separate skill-update policy; this is not an AwReq implementation. Generic success events do not identify intended/fallback paths. AR11 authority concerns and the softgoal-to-metric warrant are already explicit; no new causal diagnosis or target-change license follows. |
| Horkoff | Adds LLM-generation comparison, Requirements Reflection and DOI; snapshot adds Runtime structure; accepted-ingest report explicitly evaluates existing Theory builder link. Removes the design-model-use and adversarial-loop candidates; snapshot no longer retains Intent controls choices. | Automated model products, participatory understanding and writing's constraint discovery are distinct benefits. The new comparison is more bounded than implying artifact review restores stakeholder negotiation. Existing workshop proposals do not rely on that implication. Existing accepted-ingest links remain evaluated, not silently removed. |

For this judgment, independently read the new ATMS, Requirements Reflection, Requirements-Aware and SkillRL analyses and the checked-copy, LLM-generation and runtime-governance notes. Checked primary passages establishing the narrower claims: Zave/Jackson designations and primitive meanings; RELAX's reverse-engineered example and eventual-satisfaction caveat; Awareness's scenario verdicts versus future full loop; Horkoff's proposed agentic goal governance; Jureta's local and revisable approximation. This supports the workers' **no material redraft** conclusion without assuming it from their ledgers.

The recovered reports improve traversal and remove some overbroad comparisons. They do not supply missing journal texts, empirical transfer outcomes, legitimate goal-revision authority or experiment results. Nothing requires changing the workshop's first-pilot recommendation. Optional outbound and inbound links require separate authoring authority and grounding. The possible broad-ingest split signals and sources→tags label gap are advisory maintenance observations, not repairs performed or current publication blockers. Horkoff's optional hand-curated tag-head suggestion is not generated source membership.

## Independent source reviews: support behind acceptance

All three independent review sessions are read-only leaves, separate from source drafting. They read accepted ingests, source/type contracts, primary snapshots and relevant KB comparison context; computed hashes agree with the pinned inputs. Their conclusions are not based only on ingest summaries.

- **Four Dark Corners:** nine calls include complete snapshot coverage at 1–700 and 701–1500, the ingest and connected concepts. The review checks conditional satisfaction, informal validation, control/observability, designation/definition/assertion and manuscript identity. Its no-material-issues verdict is supported by these reads.
- **RELAX/Awareness/Horkoff:** 24 calls include all three ingests and snapshot chunks at 1/601, 1/551 and 1/501/1001 respectively. Calls `call_da9158846ae44dfba0dc687120b60f51` through `call_b50b41be5d7047d9a6315ff2da7fe0d4` cover the full papers without a missing suffix. Linked learning/authority/diagnosis concepts were read. The final verdict distinguishes specification from controller, monitor scenario success from full adaptation, and reflection from systematic mapping. Suggested clarifications about invariant flexibility and critical-requirement reinforcement were optional, not withheld material corrections.
- **Jureta:** 15 calls include the full ingest and snapshot. Initial `call_4a1c08e354dd4c29a75dd99267461f1a` stopped at line 764; `call_8cf9b9474a8343a19e897083539e737e` continued at 765 through the end. The reviewer checks belief/desire/intention, quality constraints, approximation warrant, optionality/preferences and the ingest's criticism of the monotonicity argument. It explicitly declines to establish the inaccessible journal article's contents or relationship from this snapshot. Optional refinements were not misrepresented as blockers.

These are supported semantic reviews of text captures, not PDF visual verification or empirical replications. The current five ingests remain byte-identical to the original drafting workers' candidate-write payloads, so the reviews have not been invalidated by later ingest edits.

## Workshop authoring, independent review and bounded repair

Initial author execution wrote exactly `kb/work/operationalization-goals-grounded-concepts/README.md`, `experiments.md`, and one Active Workshops entry in `kb/work/README.md`. It read the commission, workshop/source contracts, available ingests, linked KB ownership context and selected primary passages, with checksum pairing. Its selective primary reading is appropriate to a bounded framing; it is not claimed as a second complete review of every paper. No paper was substituted for a blocked source.

The independent reviewer read both workshop documents, the brief and collection contract, navigation, relevant ownership/definition notes, and targeted primary passages. Its acceptance was substantive and conditional on **three stale Jureta-review statements**, not a blanket validation certificate. It also identified ambiguity in “unchanged-fault control.” Its scoped passages and keyword searches are not an independent full-paper review; source-fidelity reviews above supply that separate coverage.

Resumed author execution performed two targeted edits, not a fresh unsupervised rewrite:

1. `call_ef6b2524975c44b9a5f95b4164a04b8b` replaced all three stale README statements: all five reviews now passed; Jureta's comparison is conceptual rather than pending review; the final decision no longer demands that completed review. The blocked 2009 journal, served-2018 date discrepancy and non-transfer caveats remain.
2. `call_f29a5b60af6d40158d799c3ad2bd0ddc` clarified fresh same-fault versus different-fault reuse, explicitly not an unrepaired baseline, and added the commissioned temporal-change variant.

Replaying the author's initial writes and repair edits reproduces both current workshop files exactly. The framing keeps six threads distinct, routes neighboring workshops without absorbing them, and offers four unrun countertests. The navigation diff is exactly the two-line insertion containing one entry plus spacing.

**Controls:** all conditions receive the same task, model, tool access, evidence and total context/tool budget, with ordinary instructions, matched attention/checklist and structured-distinction conditions. Randomized order, fresh contexts, disputed adjudications, actual costs where exact matching fails, and separate later commission are explicit. This is a proposal-level design, not a powered or executed protocol.

**Temporal-change variant:** prior support verdicts were genuinely checked; reuse was bounded by unchanged claim-bearing content. A scheduled refresh preserves links but removes support; a matched unchanged-environment control preserves support. Conditions receive identical earlier evidence, refresh notice and before/after access within each variant. Scoring asks for withdrawing stale verdicts, rechecking support, carrying a revised reuse condition into the next case, and preserving warranted unchanged verdicts. Valid links alone never establish support. This is an explicit synthetic fixture, not a claim that a cited paper ran it.

The initial author validated both documents and the landing. After repair, both documents were validated again; root independently validated all three (`call_e3f28b689c3a4449a848dfd037173986`, nested bash). All reported zero diagnostics. No fixture code, model trial, benchmark, production monitor, library/schema/governance change or experiment execution appears in these author/reviewer traces. Only the named workshop outputs and authorized navigation were changed. The repair was not followed by a second independent workshop-review worker; root inspected the changed experiment passage/status and this audit verified exact replacements. Any stronger final acceptance remains the parent's decision.

## Errors, retries and authority reconciliation

Historical acquisition errors and original reduced discovery remain documented in the original audit; they are not current publication failures. Additional consequential observations:

| Observation | Evidence and disposition |
|---|---|
| Broad adaptation stopped and attributed noncompletion to truncation | No replacement/validation false success. Its title-coverage explanation is overconservative: original suffixes plus prefix reads cover all six retained title logs. Candidate/report acceptance was still unfinished; fresh workers supplied actual replacement reports. |
| Foundations guessed a changing-requirements filename | `call_c92dc434441849dc9bc1c37d5e5a7e1b` ENOENT; not counted as a completed candidate read. No material source dependency on the failed probe. |
| RELAX guessed runtime-structure filename and absent topic path | `call_6daac5f236764210bc473dd7d67612d9` and `call_cf94d92808124330a6f569fdca713cc3`; exact-title search resolved the theory file and it was fully read. Absent optional topic path was not claimed as read. |
| Horkoff snapshot report date validation failed | Schema failure then quoted-date edit and clean rerun, before final completion. Not hidden by final process exit. |
| Workshop reviewer initial shell command ended 1 | Final filename search found no workshop type. Earlier status/listing results were usable; review proceeded under workshop collection contract. Not an acceptance-test failure. |
| Broad adaptation shell command ended 1 | Compound discovery/probe/diff command `call_e360d31b5c0e4f5db35c777e863c8969`; no successful replacement claimed. No-match or probe failure must not be conflated with the substantive output-inspection failure. |
| Prior audit tried to read published-away candidate | `call_3dba497829c84cf180e1b3c1dedc4c07` raised FileNotFoundError; `call_0fa58e19ce794e41bf708c1cd5966b96` reran reconciliation without that false expectation. Original report correctly explains handoff candidate deletion. |
| Prior audit locator scan timed out | `call_a743e0d02c0346738ddbb2babd2f40b6`; narrowed scan `call_317b45aafc9e4c93a5ed868e11636f75` completed. No unmatched report locators were reported. Large introspection outputs limit any claim that it visibly reread every historical byte; its specific acquisition/discovery findings are independently retained and unchanged. |
| Root integrity script treated no-index diff exit 1 as failure | `call_85f98c64bb4a4771acc26df8afa567fa` raised CalledProcessError, but trailing `git status` masked it with a successful shell result. Root did not leave that as assurance: `call_24d9364a534f4f459f5386c2484ce5d0` reran all five hashes/handoffs and seven new-file whitespace checks, accepting only exit 0/1 with empty diagnostic output. All passed. |

Root follow-up also read the original audit and recovery ledgers, resumed the workshop author within its ownership, updated ignored coordination state, waited for workers, inspected inbound suggestions and validated all ten current connect reports (`call_138083badb624659b8d357c8658ada84`, ten nested read/bash calls). No new source drafting fallback, experimental execution, staging or commit appears in this follow-up interval.

Later workers' writes are confined to assigned connect reports, authorized preservation/scratch/ledger paths, or the named workshop/navigation outputs. Source reviewers and the independent workshop reviewer made no writes. Recoveries did not change snapshots, accepted ingests, library notes or workshop content. No later worker delegated. Root's parallel single-source ownership was disjoint; the failed broad worker had finished before replacements began.

## Final integrity and remaining limits

- Recomputed all five current Markdown snapshot hashes: each still agrees with its ingest pin, handoff and original audit table. All five handoffs remain `outcome: published`; no new source branch was opened by connect recovery.
- Compared all five accepted ingests with the nested drafting workers' original write payloads: exact equality. No later parent redrafting or repair changed their reviewed text. Empty Quotes and snapshot-required consumption remain in force; conceptual comparisons are not retained quotations.
- Preserved original connect reports remain in the foundations/adaptation archive directories. Current ten reports are the successful replacements described above; all have inspected clean validation evidence, including root's final rerun. Validation does not prove candidate completeness or source truth.
- Git status shows five new ingests, the new workshop directory and only the authorized two-line tracked landing diff. No staged or committed source/workshop change is certified here. The parent's final diff, this audit and eventual commit are outside this verdict.
- F3 is still a bounded acquisition blocker, not evidence that the journal texts do not exist anywhere. The Zave/Jackson capture is a dated 1996 author manuscript, not verified exact journal pagination/text; Jureta's arXiv conference-preprint date anomaly remains unexplained. The workshop states these limits.
- Deleted authorized temporary PDFs still prevent independent local re-extraction and graphical comparison. Hashes certify retained Markdown bytes, not missing formula/figure fidelity or future downloaded bytes. No sessions or execution/audit records were deleted by these recovery attempts or this invocation.
- The successful search procedure cannot establish exhaustive KB/literature recall, empirical transfer, safe adaptation, legitimate terminal-goal revision, or learning across projects. Proposed inbound edges need separate authority and quote grounding or explicit snapshot-required consumption. No experiments have been commissioned or run by this phase.

**Recommended parent disposition:** accept F1/F2 recovery and the bounded workshop repair; retain F3 and capture/version limits in final reporting. Do not rerun ingestion merely for optional links. Preserve all session/execution/event/stderr records, archives, handoffs and ledgers. Review this report and final integration independently before committing; authorize any acquisition, grounding, graph authoring or experiment separately.
