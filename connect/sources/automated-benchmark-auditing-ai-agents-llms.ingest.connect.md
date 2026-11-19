---
description: "ABA connection discovery: hidden acceptance conditions, grader validity, and a scientific-benchmark comparison."
type: kb/reports/types/connect-report.md
source: "kb/sources/automated-benchmark-auditing-ai-agents-llms.ingest.md"
source_has_frontmatter: true
date: "2026-09-19"
depth: standard
---

# Connection Report: Automated Benchmark Auditing for AI Agents and Large Language Models

**Source:** [ABA ingest](../../../../sources/automated-benchmark-auditing-ai-agents-llms.ingest.md)

## Discovery Trace

Discovery used repo-local reading and ripgrep. The source has domains but no tags; no source-tag sweep or completeness-mark skip applied. Source and report collection contracts and the connect-report type were read before selection. The notes contract authorizes the proposed inbound `evidenced-by` relations.

- **Shared title and description searches:** generated fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<collection>/ --glob '*.md'` for notes, reference, agent-memory-systems, agentic-systems, and sources. Large combined output was truncated; per-collection output and focused searches recovered the relevant neighborhood. Description prospecting used `rg '^description:'` on those five collections, filtered by `audit|benchmark|grader|requirement|evaluat.*(valid|oracle|objective)|false.positive`.
- **Notes:** read `kb/notes/README.md` and `kb/notes/evaluation-README.md`. The latter does not declare complete coverage. Fully read the determinability and exact-implementation notes and warranted-autonomy note. Body search `hidden (test|requirement|acceptance)|grader|benchmark audit|false.positive` surfaced evaluator validity and hidden requirements. Followed the determinability note to intent-framed delegation and instruction underspecification, searching those two artifacts for `acceptance|hidden|determin`; they explain the wider neighborhood, but the determinability note is the precise owner of the QEMU example. Followed exact implementation to oracle strength; the broader speculative spectrum adds less than the precise requirement–objective distinction.
- **Reference:** read `kb/reference/README.md`; title and description searches identified `calibrating-semantic-gates-against-labelled-fixtures.md`. Its distinction between known-case regression and deployment-population calibration agrees with the ingest's validation cautions. Rejected an additional source-to-reference edge: this is a broad evaluation-design analogue, while the report already has two more discriminating theory destinations. The shared body search also surfaced trajectory-aware evaluation; additional trace findings alone do not establish evaluator improvement, so no supporting edge is proposed.
- **Agent-memory-systems:** read its README and generated its title surface. Description and shared body searches surfaced CORAL's private grader and Autocontext/Reflexion's feedback loops. None identifies a source-specific shared audit mechanism or ABA evidence about those reviewed systems. No connection selected; the occurrence of graders or benchmarks alone is insufficient.
- **Agentic-systems:** read its README and generated its title surface. Ran `rg -n -i 'benchmark|evaluat|audit' kb/agentic-systems/reviews/ --glob '*.md' --max-count 1`. Exo's shape-versus-usefulness checks and other systems' evaluator boundaries overlap at the theory level, but ABA does not inspect these systems. Route through the theory note rather than suggest evidence for a particular implementation.
- **Sources:** read `kb/sources/README.md`; generated titles and searched descriptions and bodies using the shared queries. Fully read the SWE-bench Science full-paper ingest. Its public/private evaluation split gives a specific comparison: adding hidden checks versus auditing whether hidden checks are themselves justified. Its existing link to exact implementation confirmed this shared axis. Other benchmark hits, including long-context and compression benchmarks, were rejected as topic-only matches.
- **External:** the original paper URL is already known and the ingest already authors its `derived-from` edge. No external prospecting was performed.

## Connections Found

The first two outbound connections are already expressed in the ingest; retain them rather than duplicate them.

- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — **is-evidence-for**: the human-aligned QEMU case supplies an arbitrary socket-path acceptance condition that an executor cannot recover from the visible keyboard-control request.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) — **is-evidence-for**: narrow graders can reject valid alternatives and broad graders can accept objective failures; executable acceptance therefore needs a separate validity check.
- [SWE-bench Science full paper](../../../../sources/swe-bench-science-arxiv-2608-19799.ingest.md) — **compares-with**: SWE-bench Science uses private checks to expose scientific failures missed by public tests, whereas ABA audits the validity of acceptance checks themselves. The comparison helps readers avoid treating stricter hidden evaluation as automatically more correct.

## Bidirectional Candidates

None. Independently useful inbound theory edges are specified below rather than duplicated here.

## Reverse-edge Candidates

- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) → source — **evidenced-by**: add the QEMU case to the note's omitted acceptance condition argument. Its reader gains a bounded, reported human-aligned example distinguishing missing author information from insufficient executor skill. This does not evidence every part of the delegation account.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) → source — **evidenced-by**: use a concrete audited grader case to show that executable conformance and task success can diverge. Its reader gains direct benchmark evidence for the link distinction, without converting ABA's overall flag rate into verified defect prevalence.

Both edges independently serve the destination note's reader, rather than merely mirroring the ingest. Source support must be retained through grounding, or the authored link must declare `(snapshot required)`, before either source-dependent example is added. The current Quotes section is empty.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — the source concerns audit discovery and partial confirmation; it does not test a new unattended acceptance policy's warranted domain. The more specific requirement–objective note is a better destination.
- [Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) — a compatible sampling caution, but no direct test of the proposed Commonplace lifecycle. Omitted to keep traversal discriminating.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) — broader speculative framework; the selected exact-implementation note already states the narrower distinction the grader cases support.

## Index Membership

None. The source landing is structural rather than an itemized bibliography; the evaluation head is a selected theory navigation surface, so this ingest does not require direct membership.

## Synthesis Opportunities

None. The evaluator–objective distinction already has an owner.

## Maintenance Observations

The oracle-strength note still introduces exact implementation as a binary fixed-artifact distinction and calls hardening a gradient refinement of it. The current linked exact-implementation note instead assigns exactness and proxyhood to different links in a named path. This is a possible stale dependent description for a later maintenance pass, not a connection action.

## Flags

- The ingest currently retains no source quotes. The proposed inbound evidence uses require grounding before durable adoption; the connect report does not supply source support itself.
- Keep corpus flag rates, sampled confirmation, issue-set recall, and leaderboard sensitivity separate. None alone establishes benchmark-defect prevalence or downstream capability improvement.
