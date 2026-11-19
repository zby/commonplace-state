# Sol fixture acceptance audit

## Verdict

**Qualified machinery acceptance for this one case.** A new ordinary assessment produced a usable fixture under `git-visible-or-installed-v1`. The isolated trial recovered from three budget-blocked process starts, accepted one new model answer, and subsequently replayed without another launch or changed launch evidence. The trial did not publish a live current result. The initial failed trial remains evidence; this was not an uninterrupted first-attempt success.

This accepts content reconstruction, retained evidence, same-trial recovery and replay for the selected stock-phrases assessment. It does **not** establish judgment calibration, effective-environment equivalence, OS-level containment, throughput, or independent repeated-trial behavior. The ordinary result has no findings; the trial has two INFO findings. Both outcomes are `pass`, but their agreement is not an acceptance criterion.

No blocking integrity defect was found in the inspected case. Workshop closure still needs the dispositions and durable documentation work below. The parent retains implementation-wide test acceptance and closure authority.

## Authority and method

This audit made no model launches, review retries, fixture executions, product/test/doc edits, commits or delegations. New files are confined to this directory's `sol-*` names. It did not close or delete any workshop or evidence.

The independent byte checks are in [sol-checks.json](./sol-checks.json): **52 checks passed**. [sol-extra-checks.json](./sol-extra-checks.json) records four additional passing checks for the launch executables, archive payload boundary and reconstructed symlinks. The checks use stdlib hashing, tar inspection without extraction, read-only Git comparisons and complete JSONL parsing. They do not use `parent-verification.json` as proof. That receipt was read only as the parent's claim to assess.

The baseline is [parent-refreshed-baseline.json](./parent-refreshed-baseline.json), not the earlier `sol-baseline.json` or `parent-preflight.json`. Baseline, fixture KB commit and current HEAD match `490f0194bebd10dc62f63e71a614aa65700e4489`.

### Evidence roots

All paths below are repository-relative unless explicitly absolute:

- Acceptance receipts: `kb/reports/state/review/fixture-acceptance-20261115/` (this directory).
- Ordinary run: `kb/reports/state/review/runs/v2/20261115T200346Z`.
- Ordinary observation: ordinary run + `/artifact/reviews/3870487350f9a4b6d7cbc816/observation.json`.
- Fixture: `kb/reports/state/review/fixtures/3870487350f9a4b6d7cbc816-6851bc80e3f6`.
- Outer trial: `kb/reports/state/review/runs/v2/20261115T200508Z`.
- Isolated KB: outer trial + `/tree`.
- Nested execution: isolated KB + `/kb/reports/state/review/runs/v2/trial`.
- Trial observation: nested execution + `/artifact/reviews/7ac430348fa150a4cc94c51a/observation.json`.

The ordinary observation's short ID also appears in historical evidence. It is not a globally unique execution identity: use the full run-qualified path above. The fixture explicitly names the new ordinary run, not the historical observation.

## Inputs, archives and reconstruction

The target was `kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`; the criterion was `kb/instructions/review-gates/sentence/stock-phrases.md`. The ordinary and trial requests retain the same target, criterion, output-contract and canonical prompt hashes:

| Input | SHA-256 |
|---|---|
| Exact target | `e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8` |
| Criterion | `6e2bd9a71d2685b71fc1641640e684574da24f3115f005263a75367c0dc6c29c` |
| Output-contract aggregate | `9969d7db1b8228822ac807fdc50483981fc6d62c7effbe601a7de3fac2e131a0` |
| Canonical prompt | `6345fd46a45243cd77e6e4a1ac81ea36a8c1cddfc1a91546a570539b3f392d1b` |
| Library aggregate | `6e50cd8a2f9823b9018db4320dc3e0dab6816994bf4837f8c0aff7b18cc06f56` |

All six fixture inputs and each observation's retained inputs match their manifest byte counts and hashes. Workjig's stored input strings encode to the recorded call-input hashes. Completed-result hashes, raw-output references and observation identities verify independently. The supplied show records agree with their underlying observation fields; successful raw outputs match the corresponding trace Write payloads exactly. The canonical prompt hash is distinct from the launch-specific invocation file hash, which contains launch-local paths.

| Archive | Members | Independent result |
|---|---:|---|
| `kb.tar` | 8,051 | Exact byte hash matches a fresh read-only `git archive --format=tar` of the recorded KB commit. |
| `library.tar` | 6,887 | All regular-file names and byte hashes match the refreshed library inventory. |
| `executor.tar` | 112 | All names and byte hashes match fixture code, source-observation code and refreshed code inventory. |

Tar inspection found no absolute/traversing member paths, duplicate names, escaping symlinks, special-file/hardlink members, or members nested beneath symlinks. The KB archive's 35 symlinks resolve within its tree and are reproduced with identical link text. The library and executor archives contain only regular files. No archive was extracted by this audit.

The KB archive contains no shared report-state payload. Its sole entry below `kb/reports/state/` is the tracked `.commonplace-validation-ignore` marker. In particular, it does not copy the source observation, its answer, live current results or another executable run. The library inventory excludes hidden paths and report state; its aggregate was recomputed from all 6,887 member hashes. This audits the selected inventory, not an assertion that all ignored ambient inputs were retained.

All three archive hashes, the fixture manifest hash and every fixture file still match [fixture-before-trial.json](./fixture-before-trial.json). The manifest SHA-256 is `37854de058571b8ef68474dd30d76d6d44905813054d4fc250d343332d969e1a`.

The independent tree check covers committed regular files, retained library files, all five dirty overlays and restored operational captures. Every expected byte hash matches. The isolated Git checkout is clean and its HEAD is the recorded reconstructed commit `1f06b492c111de35faf77e352c6184bccb77536e`; it is not the source's historical Git graph.

A read-only package comparison using `/home/zby/.local/share/uv/tools/llm-commonplace/bin/python` found exact equality with the fixture's 23-entry Python/package map. Dependency distribution artifacts, the OS and the user's harness configuration are not archived. Source/package equality is therefore a bounded executor check, not full environment reconstruction. Creation explicitly declares `current executable` and `pair grouping, one worker` as substitutions.

## Launch budget, failure and recovery

The underlying Workjig `calls/run.json` attempts, nested `log.jsonl`, raw stdout/stderr and [budget.json](./budget.json) reconcile by PID:

| Execution | Launch ID | PID | Process result | Actual review-model launch |
|---|---|---:|---|---|
| Ordinary | `bd69886bc175419199cd16207d642e14` | 2813718 | Delivered, exit 0 | Yes |
| Initial trial | `64aaa152e713460786cf64e08a9cea6e` | 2814859 | `process_error`, exit 78 | No |
| Initial trial | `b28641c238ab40a7a7ae9605ba940aa1` | 2815200 | `process_error`, exit 78 | No |
| Initial trial | `e9fdac2456034441b81de7a4d621fd34` | 2815809 | `process_error`, exit 78 | No |
| Recovered trial | `d9d718b95b7746a5b039987907b6b9e4` | 2816402 | Delivered, exit 0 | Yes |

Thus there were **five guarded process starts, two actual top-level review-model launches and three blocked starts**. These are not counts of provider API requests or billable turns. Both successful traces report zero spawned subagents.

The [guard](./bin/claude) serializes budget updates under `flock`, persists each event and exits 78 before `os.execv` when no slot is available. All three blocked stdout files are empty; their stderr is exactly `Acceptance launch budget exhausted; no model was called.` They have no review output. Their launch records retain exit 78, and the initial [trial-result.json](./trial-result.json) retains the stop and `not-run` observation. The guard and real executable still match the hashes in the preflight receipt. The two successful trace init socket paths also identify the two allowed PIDs.

The blocked events retain phase `source`: the label had not been advanced/released, although these processes belonged to the trial. Do not classify execution from that label alone. The final budget is `limit: 2`, `used: 2`. The guard permits a non-review `--version` query without consuming a slot.

The parent's stated cause was a development-interpreter/package mismatch during pretrial verification followed by a shell that continued before the second slot was released. The preserved blocked attempts and later successful recovery are independently established. The precise failed verification command and shell continuation are a parent-reported explanation, not independently reconstructed from a complete shell transcript here. The CLI-interpreter package equality check above supports the corrected interpreter choice.

The nested log preserves all three `launch/process_error` events, the `stopped-call`, then the delivered launch and answered event under the same request key. The current observation lists all four nested process attempts, one completed result, no content rejections and no validation warnings. Recovery continued the original outer trial rather than opening an independent replacement trial.

## Full raw trace inspection

The complete successful stdout files were parsed, not just the excerpts in `show` or terminal success summaries:

- Ordinary: ordinary run + `/calls/launches/bd69886bc175419199cd16207d642e14/stdout.log`: **102,862 bytes, 26 JSONL events**.
- Trial: nested execution + `/calls/launches/d9d718b95b7746a5b039987907b6b9e4/stdout.log`: **110,731 bytes, 34 JSONL events**.

Both successful stderr files and all three blocked stdout/stderr pairs were inspected. The derived JSON retains trace hashes, full init/terminal/hook records, tool-use payloads and event counts. Every tool-use ID has a tool-result ID; neither trace has a failed `is_error` tool-result block or terminal permission denial. Each used **six Reads and one Write**, all directed at its invocation, captured inputs and own output. No Bash, Edit, MCP invocation or subagent launch appears. No additional model appears in `modelUsage`.

| Property | Ordinary | Trial |
|---|---|---|
| Requested model/effort | `opus` / `medium` | `opus` / `medium` |
| Effective reported model | `claude-opus-5-5` | `claude-opus-5-5` |
| Claude Code version | `2.1.325` | `2.1.325` |
| Permission mode | `default` | `default` |
| Advertised tools | 71 | 25 |
| MCP servers | Scry and Claude Docs connected; Calendar, Drive and Gmail need authentication | Empty list |
| SessionStart hook | Started; success, exit 0; empty hook stdout/stderr | Started; success, exit 0; empty hook stdout/stderr |
| Terminal result | Success; no API error; no safety stop | Success; no API error; no safety stop |
| Reported cost USD | **0.2997354** | **0.352242** |

**Exact reported total: $0.6519774.** This is the sum of the two terminal `total_cost_usd` values, also supported by per-model usage. It is reported list-price usage, not proof of an invoice or net subscription charge. Blocked starts have no model-usage report; replay is not counted again.

Trial stderr is **not empty**: Claude Code says it ignored four `permissions.allow` entries from `.claude/settings.json` because the isolated workspace was not trusted. This is a configuration warning, not a failed Read/Write or a terminal permission denial. No audit action changed the user's trust settings. Successful hooks do not prove that the hook configuration or side effects were identical.

Rate-limit events report status `allowed`; their separate overage fields say `rejected`/`out_of_credits`. These were not process failures, content rejections or failed tool results in these calls.

The requested allowlist is not an isolated tool inventory. The trial's 25 advertised tools remain broader than Read/Grep/Glob/scoped Edit/Write. The trial adds `COMMONPLACE_LIBRARY_ROOT` pointing to its retained KB and `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0`; the working directory also changes. Ambient automatically loaded context and provider internals remain unknown. Effective configuration is **observed different in material respects**, not equivalent merely because both result receipts say `unassessed`.

## Replay, publication and preservation

[resume-before.json](./resume-before.json) is the comparison baseline for the final replay:

- All **33 launch files** have exactly the same names and byte hashes, including the three blocked attempts and successful trial trace/output.
- The one retained completed-result file has the same hash, `6da7468a89aa3c91a70a90381f3741fa1641613051bf0b3448d878310e3b6608`.
- The full budget object, including its five-event history, is unchanged.
- [trial-recovery-result.json](./trial-recovery-result.json), [resume-result.json](./resume-result.json) and the outer run's current `trial-result.json` agree exactly.

Together with the four-attempt nested registry and six-line nested log containing no additional launch event, this supports **zero new launches on final replay**. The audit did not rerun replay to test it again. The before snapshot is locally supplied evidence; this is an integrity comparison, not an independently authenticated timing record.

Every live result matches [live-results-after-source.json](./live-results-after-source.json). Relative to the refreshed pre-source inventory, only the selected stock-phrases current result changed; its current hash is `bffb95f5b752ff2317c1e74357aca3120b913e039c3b3a5cb4f0c57d7418537f`. The other three current results retain their baseline hashes. There are no current-result Markdown files in the isolated trial's results tree. Recovery/replay receipts report empty changed lists, and independent authored-tree/Git checks agree. This establishes no trial publication in the inspected live views; the ordinary run intentionally replaced its selected view.

The historical run directories `20261115T123635Z` and `20261115T132933Z` retain their exact baseline file sets and all **160 hashes** (86 + 74). All five unrelated dirty-file hashes remain unchanged. The 112-file source inventory and 6,887-file live library inventory also remain equal to the refreshed baseline. `git status --short` still reports only those five pre-existing dirty/untracked paths. `git diff --check` passed. This audit did not repeat the much earlier 4,725-file v1 cutover audit; that separate receipt is not subsumed by these 160 historical v2 checks.

## Focused workshop completion review

The relevant closing condition is [review-operation-unification/README.md](../../../../work/review-operation-unification/README.md), Completion, with the implementation acceptance cases in [execution-contract.md](../../../../work/review-operation-unification/execution-contract.md), section 8. It is **not** the broader `review-on-workjig` workshop's live full-pass/strike-list agenda.

### What this case resolves

The current-policy source-observation/fixture prerequisite is satisfied. The paid case demonstrates ordinary execution, sealed fixture creation, independent tree construction, one actual trial answer, preserved process-error history, same-trial recovery, no live publication and zero-launch replay. The fixture's library no longer requires silently importing ignored ambient state. A previous historical observation lacking the policy field was not rewritten to make it eligible.

### Specific remaining acceptance/closure work

1. **Retain and disposition this qualified result in the implementation record.** [implementation.md](../../../../work/review-operation-unification/implementation.md) currently stops at the library-boundary repair and completed cutover; it does not yet record this current-policy paid fixture case, its interrupted start, exact budget/cost or trust/MCP difference. The parent should decide whether the bounded machinery evidence completes its intended fixture acceptance. This audit supplies that decision evidence; it does not grant closure.
2. **Finish durable decision extraction.** The implemented [review architecture](../../../../reference/review-architecture.md), review-result type, review guide and command reference already describe the main machinery. However, [ADR 127](../../../../reference/adr/127-review-runs-as-workflows-over-result-files.md), Decision, still describes freshness as two hashes and status as pure functions of current result files, without the now-required output-contract/captured-evidence checks. Before deleting the workshop, reconcile the adopted decision record, by amendment or a focused follow-on ADR as the parent judges appropriate. A new runtime is not needed.
3. **Reconcile the proposal's atom inventory where required by the closure condition.** The [improvement-procedure proposal](../../../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md), Current state, still groups conformance and critique under the old gate/method presentation and does not identify the admitted shared typed-result/observation/fixture subset. Update only the adopted first slice; do not imply compression, friction, premises, connect, edits or stops were admitted. The runtime reference is not a substitute for checking this specifically named closure surface.
4. **Preserve the declared implementation-wide verification boundary.** This audit did not rerun the full suite or independently verify every section-8 acceptance test. In particular, one paid trial plus its resume is not the two-independent-trial fake-harness case, an installed-library live trial, a dispatch-race test, or a publication-crash test. The parent's existing offline coverage remains the evidence for those cases. No additional paid experiment is implied or authorized by this limit.
5. **Only after operator disposition and durable extraction, handle workshop/list cleanup under separate authority.** Its README still describes the collection as active work. Nothing was closed, removed or relinked here. Useful evidence must remain recoverable before any future cleanup.

The recorded gaps—automatic reporting of recovered tool failures, broad advertised tool surface, omitted user configuration/dependency artifacts and unverified provider internals—limit acceptance claims. They are not newly discovered blockers requiring a general environment framework or calibration campaign before this bounded machinery case can be accepted. They must not disappear when the workshop is eventually closed. Judgment calibration and other operation-family admissions remain separately commissioned work.

## Deterministic validation

Both representative completed artifacts were explicitly checked with the bare `commonplace-validate` command: the ordinary retained result at its source root, and the trial retained result from inside the isolated KB with its retained library selected. Each returned **VALIDATION SUCCESS**, one typed file, **0 failures and 0 warnings**. These are structural/provenance checks, not independent endorsement of either judgment.

The audit report itself is frontmatter-free operational text. It is for the named fixture-acceptance operation, not a transferable library claim. Broader graph discovery through `cp-skill-connect` would require a separate handoff and is not needed for this evidence-only write.
