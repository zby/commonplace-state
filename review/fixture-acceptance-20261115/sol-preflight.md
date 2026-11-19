# Sol preflight for bounded fixture acceptance

## Decision and authority

The source checkout is ready for the parent's bounded experiment **only after the parent verifies launch-budget enforcement**. The ordinary CLI does not enforce the authorized two-launch total. No other blocking source or dirty-content defect was found by this inspection. The new observation, fixture, trial and resume have not yet been produced or accepted.

This report supports the parent's execution and later audit. The authorization is exactly two review-model launches total: one forced ordinary `sentence/stock-phrases` assessment of the named note, then one isolated fixture trial. Resume must launch nothing. Sol is support, not the review worker; Sol made zero review-model launches, invoked no worker-launching review command, delegated nothing, and changed no source, library artifact or historical evidence. Only `sol-*` evidence files in this acceptance directory are writable by Sol. Parent owns execution, budget enforcement, consequential choices and final verification.

The completion claim sought is machinery acceptance: a newly captured ordinary assessment can seed a reconstructable fixture; one independent trial accepts output without publishing live results; continuing that same trial replays without another launch. Matching verdicts, calibrated judgment, repeatable cost and environment equivalence are not acceptance requirements or justified conclusions.

## Evidence and inspection basis

- [Preflight byte identities](./sol-baseline.json) records HEAD, all five unrelated dirty-file hashes, target/criterion/profile hashes, source and library manifest digests, current result hashes, and the two existing v2 run manifest digests. Capture time: 2026-11-15 19:43:49 UTC. These are hashes, not retained repair bytes.
- [Implementation status](../../../../work/review-operation-unification/implementation.md) explains the previous capture defect, controller repairs, corrected library policy and cutover. It was read completely.
- [Review operation reference](../../../../reference/README-REVIEW-SYSTEM.md) states fixture, freshness, replay and guard semantics.
- Exact implementation inspected: `src/commonplace/lib/review_workflows/{fixtures,observations}.py` in full; relevant sections of `gates.py`, `results.py`, `result_contract.py`, `src/commonplace/cli/review_workflows.py`, `src/commonplace/headless/{jobs,harness}.py`, `src/commonplace/lib/{tasks,library}.py`.
- Applicable instructions read: root `AGENTS.md`, `.pi/agents/commonplace-worker.md`, `kb/reports/COLLECTION.md`, `kb/reports/state/README.md`, the writing skill and text type. This is a frontmatter-free operational report, not a worker review fragment.
- Regression evidence inspected, not executed: `tests/commonplace/review_workflows/test_observations.py` and the production-selector test location in `test_controller_failures.py`. Fake-harness tests are not paid trials.

## Current target, criterion and execution identities

| Surface | Identity at preflight |
|---|---|
| HEAD | `54e82a0c676ef3f6365686d179f5d4192c13d223` — exclude ignored ambient files from review library inventories |
| Target | `kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`; 13,518 bytes; exact SHA-256 `e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8` |
| Criterion artifact | `kb/instructions/review-gates/sentence/stock-phrases.md`; 1,299 bytes; exact SHA-256 `6e2bd9a71d2685b71fc1641640e684574da24f3115f005263a75367c0dc6c29c` |
| Pair | kind `gate`, contract `verdict`, criterion id `sentence/stock-phrases`; job is `<target>::sentence/stock-phrases` |
| Freshness | Gate watches `[body]`; normalized note freshness hash `c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5`. This is not the exact target hash. Criterion freshness normalizes line endings; here it equals the exact criterion hash. |
| Profile source | `kb/instructions/review-profiles.yaml`; SHA-256 `c14a58859c199281581d3289f87fdd93b754dc2a47e375e625915dfabde08cea` |
| Default profile | `opus`: harness `claude-code`, requested launch model `opus`, effort `medium`. `sonnet` is another available Claude profile, not the default. Parent must record any deliberate non-default selection. Fixture inherits the source observation's resolved profile. |
| Default profile flags | `allowed-tools: Read,Grep,Glob,Edit(kb/reports/state/review/runs/**),Write(kb/reports/state/review/runs/**)`; `disallowed-tools: Bash,NotebookEdit` |
| Adapter defaults | Executable `claude`; print mode, verbose stream JSON; environment default `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0`. Permission flags do not isolate the advertised tool inventory. |
| Library | Expected `/home/zby/llm/commonplace/kb`; no `COMMONPLACE_LIBRARY_ROOT` override was present in Sol's environment. Policy `git-visible-or-installed-v1`; 6,887 files; library digest `c6a961182cb87bf0b892dba321f46b55f65895a01567eef1e7f1ffb0871477b2`. |
| Executable source | 112 package files under `src/commonplace`; digest of the sorted path-to-hash manifest `408ccafcac8371dbfc75c0cf410f01599116be67ec37ddb7ac112fe88133f4da` |
| Output contract | `types/review-result.md`, `types/review-result.schema.yaml`, project `reports/COLLECTION.md`; combined fingerprint `9969d7db1b8228822ac807fdc50483981fc6d62c7effbe601a7de3fac2e131a0` |
| Active namespace | `kb/reports/state/review/runs/v2/`; observation format 2 |

The current stock-phrases view is an accepted `pass` from `20261115T132933Z`, observation `3870487350f9a4b6d7cbc816`, launch `b0f93e5dc5ce4f45adf47dc34c8dccd2`, observed model `claude-opus-5-5`. Its inputs and contract still match the identities above. Therefore an ordinary unforced invocation can skip it; `--force` matters. Neither a prior pass nor the requested alias `opus` predicts the new observed model or verdict.

Bare commands exist at `/home/zby/.local/bin/commonplace-{review,validate}`. The review entry point names the editable tool interpreter `/home/zby/.local/share/uv/tools/llm-commonplace/bin/python`. `claude` currently resolves to `/home/zby/.local/share/claude/versions/2.1.325`. Sol did not run the harness or verify its version response. Source-checkout calculations above do not substitute for the new observation's actual loaded executor, Python/package versions and executable hash.

**Timeout caution:** an omitted ordinary timeout becomes 86,400 seconds in `Run`, not the 600 seconds used in the previous four-kind check. Parent chooses and records the timeout before the ordinary launch. Trial inherits it; fixture configuration overrides are rejected.

## Exact acceptance checklist

Unchecked boxes are parent execution or post-run audit work, not completed claims.

### 1. Authorization and baseline

- [ ] Parent's enforcement permits only one actual model process for the ordinary assessment and one for the isolated trial, with no correction/relaunch beyond those slots. Verify it before execution and retain its identity/evidence. `--max-workers 1` only limits concurrency; it is not a launch cap. Sol has not inspected or certified the parent's enforcement mechanism.
- [ ] Record the parent-selected profile and timeout and confirm the active CLI loads this checkout and corrected library policy. Keep pair grouping and the single named pair; no bundles, extra criteria, draft selector, supplied operational input, assessment-led revision or full pass.
- [ ] Compare HEAD, target, criterion, contract, source and the five unrelated dirty files with `sol-baseline.json`; resolve any concurrent change before treating this as one baseline. Do not clean, stash, restore or commit unrelated work.
- [ ] Retain the exact ordinary command, process status, output, run path, before/after state and budget receipt. Reporting a controller exception is not permission for a replacement launch.

### 2. Forced ordinary assessment — first authorized launch

- [ ] Execute only the named target against `--criteria sentence/stock-phrases`, `--grouping pair`, `--force`, with the selected profile/timeout and one worker. No historical resume is the source of the new observation.
- [ ] New run captures exactly one pair in `review-request.json`; publish-results is true and operational inputs are empty. Its `sweep.json` records the resolved profile and selection.
- [ ] Exactly one actual launch belongs to that assessment; the observation state is `completed`, the pair state is `reviewed`, `stopped` is null and the checkout guard has no changed paths. A fresh skip does not satisfy this step.
- [ ] Observation records format 2 and `library-policy: git-visible-or-installed-v1`; target/criterion exact hashes, output-contract fingerprint and the source/library identity agree with the selected baseline. Every captured input hash matches.
- [ ] Accepted worker content passes the completed `types/review-result.md` contract using captured schemas and project reports contract. Passage findings identify one normalized, unique captured-target span. `pass`, `warn` or `fail` can all satisfy machinery acceptance; no favorable verdict is required.
- [ ] Completed result exists in the observation manifest with its own hash, distinct from the raw worker output hash. Validate both the retained result and current view; verify target/raw evidence references. Inspect `validation-warnings`, not only exit status.
- [ ] Only this pair's live result view may be replaced. The other three current views and both historical v2 runs remain unchanged. All unrelated dirty files still have their baseline bytes.

### 3. Fixture preparation — zero model launches

- [ ] Create from the **new** ordinary observation, using explicit `--substitute-current-executor`. Record fixture path and exact `fixture.json` hash. The two older v2 runs have no library-policy field and are refused as fixture sources; never add one retroactively.
- [ ] Check the source observation and all input hashes first. Its recorded Git commit must still be available for `git archive`; all declared dirty files need exact matching bytes. If any are missing, stop or use parent-authorized exact-hash repair copies, without repairing the original files or historical records.
- [ ] Audit `fixture.json`, `kb.tar`, `library.tar`, `executor.tar`, captured inputs and `overlays/` as described below. Require supported version/policy, confined paths, complete recorded file hashes, source observation linkage, requested profile, code manifest and package versions. Identify extras rather than relying only on `fixtures.load()`.
- [ ] Record the explicit substitutions (`current executable`, `pair grouping, one worker`) and declared gaps. Freeze executable source and package versions between fixture creation, trial and resume; otherwise `load()` refuses the baseline.
- [ ] Fixture creation consumes zero launch slots and changes neither source/library files, historical evidence nor live result views.

### 4. Isolated fixture trial — second and last authorized launch

- [ ] Invoke `run gates --fixture <fixture-path>` once without resume. Do not supply note/profile/timeout/worker/force/input overrides; the fixture supplies them. A second non-resume invocation is a second independent trial and is unauthorized here.
- [ ] New outer run has `sweep.json` format 2/workflow `trial`, a confined `tree/` with its own initialized Git repository, and `trial.json` tying fixture identity to the initial tree state. No process uses the live checkout as the trial working directory.
- [ ] Nested evidence is under `<outer-run>/tree/kb/reports/state/review/runs/v2/trial/`. Exactly one actual model launch occurs there; it is independent of the ordinary launch. Evidence is not at the ordinary outer `artifact/reviews` path.
- [ ] Trial uses captured target/criterion/contracts and inherited execution settings. Captured library inventory digest matches the ordinary source baseline. Compare input bytes, not observation IDs: injected `COMMONPLACE_LIBRARY_ROOT=<trial-tree>/<library>` changes the resolved profile/request identity, as expected.
- [ ] `trial-result.json` has `stopped: null`, `changed: []`, one observation with `state: reviewed`, fixture hash matching `trial.json`, and `effective-configuration: unassessed`. Inspect and validate its nested completed result and raw evidence.
- [ ] Live result inventory/hashes after trial equal those immediately after the ordinary assessment. Trial `ask()` has no publication callback; freshness cannot skip this trial. Trial guard and the live dirty-file check both pass.
- [ ] Total actual review-model launches now equals two, allocated one ordinary/one trial. Any attempted correction, missing output, worker problem, tool failure or budget stop is reported, not concealed with an extra trial.

### 5. Resume same trial — zero new launches

- [ ] Repeat `run gates --fixture <same-fixture> --resume <same-outer-trial-run>`. Keep the exact same tree location, fixture, executable source and package versions; do not dismiss answers with `retry`, acknowledge an unknown process, or edit the trial baseline to force progress.
- [ ] Before/after nested `calls/run.json` has the same request identities and same unique launch IDs/attempt counts; launch directories and raw stdout/stderr/input/output bytes are unchanged. No new `launch` log event or harness invocation appears. Parent budget receipt independently shows no model process started.
- [ ] Replay returns the reviewed observation, same completed-result bytes/hash, same fixture hash and no changed paths. Refreshing manifests or appending replay diagnostics alone is not a model launch and is not a new independent trial.
- [ ] Recheck both historical v2 run manifests, all protected dirty files, source/library identities and live result views. Parent retains exact commands and exit statuses for all three execution stages plus fixture creation/show inspection.

## Dirty-checkout reconstruction risks

The dirty checkout is deliberate input, not a condition to repair. There are three modified tracked files and two untracked authored files, all under `kb/`. Their exact hashes are in `sol-baseline.json`:

1. `kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md`
2. `kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md`
3. `kb/work/stochastic-operation-testing/README.md`
4. `kb/work/stochastic-operation-testing/provenance-reconstruction-results.md`
5. `kb/work/stochastic-operation-testing/provenance-reconstruction-trial.md`

`observations.content_state()` records hashes/kinds, not their bytes. They enter the Git-visible library inventory even though unrelated to this assessment. A new source observation therefore depends on retaining their exact bytes until fixture creation. `fixtures.create()` reads matching current bytes or declared captured target/criterion/operational bytes, otherwise demands `--repair ORIGINAL=PATH`. These five are not the selected target or criterion, so target capture will not rescue later edits to them. Untracked authored files also affect library membership: adding or removing one between observation and fixture creation can block library reconstruction even when other bytes remain available.

`kb.tar` alone cannot reconstruct this checkout: it omits all uncommitted changes and untracked files. Fixture overlays plus the exact `library.tar` supply those bytes. Review state is excluded from content-state and library capture, so writing this report does not perturb their baselines. Source snapshots and ignored mailboxes must not be copied wholesale to make a digest match. Existing preparation receipts explain the earlier 96-file boundary error; the corrected policy intentionally excludes those ambient files.

A clean guard means no *change relative to the dirty start*, not a clean Git checkout. The guard excludes the review state tree and does not detect ignored-file changes or changes undone before the final sample. Parent's explicit protected-file hashes supplement it. Concurrent commits change HEAD and break the comparison even if the target stays unchanged. This preflight found no lexically escaping committed symlink, but archive/overlay confinement remains mandatory.

## Archive and provenance audit method

Intent: establish exact reconstructability and retained evidence integrity without extracting over the live checkout or modifying old observations. Missing evidence means acceptance is incomplete; it is not permission to synthesize historical bytes.

1. **Fixture manifest.** Recompute every `files` entry from fixture-relative bytes with the same confined-path rule; compare version, library-policy and source-observation. Hash `fixture.json` itself separately: its `files` map is built before the manifest is written and therefore does not self-hash. Audit unmanifested extras and missing expected artifacts. The loader checks listed hashes, not a complete extra-file prohibition or a cryptographic signature.
2. **Committed archive.** Inspect tar members without extraction. Require safe relative paths, ordinary files/directories or confined symlinks; reject absolute/traversing paths, external links, devices and unsupported member types. Compare `kb.tar` with `git archive --format=tar <kb-commit>` or the corresponding Git tree/blob inventory. This establishes committed tree bytes, not Git history or working-tree equivalence.
3. **Dirty overlays and selected inputs.** For every file in content-state, verify `overlays/<original-path>` against the observation's hash. Account separately for deleted files and symlink targets. Check every retained input's role/origin/hash/byte count. Operational inputs, if present in another case, stay selected copies: they do not authorize recursive dependency capture or restoration to original ambient locations. This authorized case needs none.
4. **Library archive.** Hash each relative file payload in `library.tar`; hash the sorted JSON path-to-hash map to reproduce `library-sha256`. Reject hidden paths, `reports/state`, unauthorized symlinks or ambient ignored additions. Git-visible policy includes tracked files even if ignore patterns match, plus non-ignored untracked authored files; installed non-Git libraries use visible package files. Compare inventories as well as their digest.
5. **Executor archive.** Hash `executor.tar` payloads against `fixture.json.code`. Compare current `observations.code_files()` and complete `package_versions()` output with the fixture before trial/resume. Trials do **not** unpack/run `executor.tar`; they run the current installed executor only if source and package versions still match the fixture. Source path/version equality is not dependency-artifact identity. The substituted executable baseline is explicit, not a claim that the historical executor was recovered.
6. **Reconstructed trial.** Confirm `.git` is local to `tree/`, the overlay and selected input bytes are installed as specified, the governing project reports contract is under `tree/kb/reports/COLLECTION.md`, and the reconstructed library digest matches before asking a worker. `trial.json.tree-state` is the baseline resume checks. Fixture/load hashes do not certify ambient user configuration or effective tool availability.
7. **Observation closure.** Recompute the observation ID as the first 24 hex characters of SHA-256 of `json.dumps(request, sort_keys=True)`. Check captured inputs and completed-result manifests; independently validate raw-output and target evidence hashes in the completed result. Hash the completed result separately. `show` loads observations and validates retained results with captured contracts, but is not a full reconstruction or launch-budget audit.

Parent-only, non-launching inspection routes are `commonplace-review show <ordinary-run> --json` and `commonplace-review show <outer-trial-run> --json`. The latter automatically selects the nested trial evidence root. A `show` failure must be reported; a successful `show` is necessary evidence, not proof of all checklist items.

### Historical archives

The existing runs `20261115T123635Z` and `20261115T132933Z` are immutable evidence for this task. Baseline aggregate digests include every regular file under each run, keyed by relative POSIX path; compare them again after the experiment. Their old library-policy omission is expected and must remain unchanged. The first run's missing captured validation dependency remains historical fact even though a separate recovery receipt supplied current contract bytes for offline acceptance.

For the earlier v1 cutover archive, use `kb/reports/state/review/cutover/20261115-v2/receipt.json` and the preflight `inventory.json` to resolve original-to-archived paths and compare payload hashes; do not infer integrity from directory counts. The implementation records 4,725 verified historical files, 132 old current result files and one packet. Sol hashed the cutover receipt but did not independently rehash all v1 archived payloads in this preflight. No v1 result or answer may satisfy the newly authorized assessment.

## Count launches, replay and tool failures separately

**Actual launch accounting:** inspect each request version in `calls/run.json`, enumerating its `attempts[].launch_id`, status, process/evidence fields and matching `calls/launches/<id>/` directory. Correlate fresh `launch` events in `log.jsonl` and the parent's process-start/budget receipts. Count unique launches across the ordinary and nested trial runs, not observations, accepted results, rejection events, request versions or repeated reads of `recorded_calls()`. A reserved or launch-error record needs process evidence; it does not by itself prove paid provider execution. Missing terminal stdout or missing cost is unknown expenditure, not evidence that a started worker was free.

**Paid usage/model evidence:** inspect each unique launch's stream JSON init and terminal result event. Retain reported model/modelUsage, cost, duration, usage, terminal status and permission denials. Sum reported per-launch cost once, not on each replay or for every modelUsage entry. A requested model alias and a process launch count are different from provider-reported model and billing. Record missing cost/model evidence as unknown. Historical runs' seven and four launches are not part of this new two-launch allocation.

**Replay evidence:** an answered call can be revalidated without spawning a process. `Run.checked()` may log the same retained rejection again; `observations.refresh()` separately counts distinct rejected request keys and rejection events. A larger rejection-event count on resume is not necessarily a new launch. Conversely, resuming a stopped usage-limit/process-failure request may authorize a new launch, and `retry` dismissal can change call identity; neither is allowed by this authorization. Successful completed-answer replay must leave launch/attempt inventories unchanged.

**Tool failures:** parse every stdout JSONL event, pairing assistant `tool_use` IDs/names with user `tool_result.tool_use_id` and `is_error`. Retain failed operations even if later recovered. Inspect permission denials, hook failures, stderr, abnormal terminal events, and MCP connection/authentication statuses separately. Distinguish advertised tools, invoked tools and failures. Earlier traces demonstrate that terminal success and empty stderr can coexist with failed Edit operations. `observation.launch-evidence` preserves init tools/model/MCP summaries, not a complete tool-error audit. Tool failures must remain visible; parent decides their acceptance consequence rather than Sol silently treating all terminal success as clean execution.

**Typed acceptance:** process delivery and a successful terminal model event are not typed-result acceptance. Check observation state, saved completed-result validation, diagnostics (`rejected`, `failed`, `stopped-call`, `no-progress`, `controller-error`) and pair/trial reports independently. Controller failures must stop, not ask the model to repair missing contracts or corrupt captures. The no-progress guard avoids an identical rejected prompt/input cycle; it does not guarantee a one-launch assessment.

## Blockers, limits and handoff

- **Conditional blocker before any model process:** native retry/relaunch behavior exceeds this authorization unless parent enforcement is effective. `gates.ATTEMPTS=3`; `Run.checked()` can ask correction requests, and `Run.ask()` can relaunch process/launch errors up to its own ceiling. There is no public review CLI total-launch limit. No source/profile repair is attempted or proposed as implicitly authorized here.
- **Historical-source blocker, already understood:** both prior v2 source observations lack `git-visible-or-installed-v1`; current fixture creation refuses them. The authorized fresh ordinary assessment is the way to obtain a supported source, not a historical evidence rewrite.
- **Expected pending inputs:** no `review/fixtures/` directory or new acceptance run existed during inspection. New ordinary/fixture/trial/resume paths, actual executor environment, parent budget mechanism and statuses remain to be supplied. This is pending execution, not a discovered implementation defect.
- **Known non-blocking limits:** dependency artifacts, user-level harness configuration, automatically loaded context, provider internals and effective MCP/tool availability are not pinned. The prior traces advertised 71 tools; permission allowlists are not tool-inventory isolation. Archive reconstruction and matching hashes cannot establish a hermetic environment or calibrated judgments.

Preflight verification: `commonplace-validate` reported **VALIDATION SUCCESS**, one text file, zero failures and zero warnings. The baseline JSON parsed; protected dirty-file, target, criterion and profile hashes still matched; all report links resolved; `git diff --check` passed. Git status retained exactly the five pre-existing dirty paths. These checks launched no review worker.

Sol awaits the parent's post-run handoff naming the ordinary run/observation, fixture, outer trial run, captured command/status/budget receipts and resume result. The next Sol action is read-only audit with another `sol-*` report in this directory, not another launch, repair, commit or delegation. No connection-discovery run is needed for this operational state report; any later library contribution can separately use `cp-skill-connect` under new authority.
