---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md"
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: Codifying predictable choices leaves agents with less predictable work

**Source:** [Codifying predictable choices leaves agents with less predictable work](../../../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md)

## Discovery Trace

**Setup and authorisation:**

- Read the source in full at SHA-256 `1e989590f6dc2cce4653b4383696b000ad8216154fd8d96fbb3c530e6e35f138`, after reading the connect-report type contract and `kb/notes/COLLECTION.md`.
- The notes contract authorizes prospecting into `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; `kb/work/` is excluded. External prospecting was skipped because the user supplied no external target and no already-known external target was present in the loaded context.
- Read the destination heads `kb/notes/README.md`, `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`.
- Read the source's three tag heads: `foundations-README.md`, `computational-model-README.md`, and `self-improving-systems-README.md`. None declares `complete: true`, so each received a by-tag description sweep.

**Complete title and description surfaces:**

- Generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination> --glob '*.md'`: notes 376 files, types 10, reference 157, agent-memory-systems 174, agentic-systems 12, sources 326, and instructions 49.
- Enumerated frontmatter descriptions with `rg -l '^description:' kb/<destination> --glob '*.md'`: notes 372 files, types 7, reference 153, agent-memory-systems 171, agentic-systems 10, sources 324, and instructions 97 description-bearing files, including nested skill and gate resources.
- Ran `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`, then the same exact pipeline for `computational-model` and `self-improving-systems`. These were lexical searches, so no semantic-search score applies.

**Notes:**

- Body searches included `rg -n -i 'predictable|unpredictable|less routine|routine work' kb/notes/ --glob '*.md'`, `rg -n -i 'agent (boundary|frontier)|deterministic shell|residual (agent )?work|moves? the frontier' kb/notes/ --glob '*.md'`, `rg -n -i 'planning-time|execution-time|advance planning|defer decisions?|information (arrives|available).*execution' kb/notes/ --glob '*.md'`, and `rg -n -i 'codif(y|ied|ication).*predict|predict.*codif|stable (mapping|pattern).*codif' kb/notes/ --glob '*.md'`.
- Kept `codify-versus-llm-decision-heuristics` for its four decision criteria, `spec-mining-as-codification` for the migration mechanism, `semantic-work-can-be-relocated-but-not-eliminated` for the upstream-judgment qualification, and `increasing-computational-autonomy-relocates-human-effort` for the elastic-workload extension.
- Followed those candidates through oracle strength, progressive constraining, methodological versus computational closure, warranted autonomy, the Commonplace tag-readme trace, and automation-boundary notes. This separated the source's residual-work selection effect from adjacent claims about verification limits, representation change, and total human effort.
- `rg -n 'codifying-predictable-choices-leaves-agents-with-less-predictable-work|agent-work-is-selected-for-unpredictability' kb/notes kb/reference kb/instructions kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` found no existing inbound links to either the final or former slug. The source's already-authored links were evaluated but are not re-reported as candidates.

**Reference and types:**

- The title and description scans found no type spec that could serve as evidence for the selection effect. `kb/types/note.md` governs form, not the claim, so no type candidate survived.
- The strongest reference hit was `tag-readme-trace-as-self-improving-loop.md`, which splits stable checks from human shape judgment. It was rejected as a direct edge because the kept computational-autonomy note already gives it a specifically articulated evidence path.

**Agent-memory and agentic systems:**

- Searches included `rg -n -i 'codif|deterministic|symbolic|compiled|validator|verification' kb/agentic-systems --glob '*.md'`, `rg -n -i 'routine|unpredict|frontier|self-modif|promot|stable pattern' kb/agentic-systems --glob '*.md'`, and corresponding `routine`, `executable`, `promotion`, `success`, and `oracle` searches over `kb/agent-memory-systems/`.
- Kept the trace-learning survey because its reviewed systems repeatedly promote successful trajectories into executable artifacts under local oracles while leaving higher-order judgment open. Kept Swamp because its architecture cleanly assigns ambiguous interpretation and artifact authoring to an LLM while a symbolic runtime takes over repeatable control flow.
- Followed the survey into Voyager, OS-Copilot, SkillWeaver, and Meta-Harness. Their individual reviews were rejected as separate edges because the survey already carries the comparative pattern and its oracle limitation. Followed Swamp into its typed model, validation, scheduling, and permission boundaries; Compound Engineering was then redundant and less explicit about a repeated symbolic execution kernel.

**Sources:**

- Searches included `rg -n -i 'residue|residual|routine work|automation transforms|operator.{0,30}role|could not automate' kb/sources --glob '*.md'`, `rg -n -i 'codif|structural tests|linter|deterministic.{0,40}agent|manual.{0,40}automat' kb/sources --glob '*.md'`, and `rg -n -i 'problem selection|no ground truth|research taste|verification.{0,40}automation|automation boundary' kb/sources --glob '*.md'`.
- Kept Bainbridge's `ironies-of-automation` ingest as historically prior evidence for the residue left past what designers can automate, with its industrial and human-operator scope retained. Kept the Harness Engineering ingest as a contemporary case in which recurring manual cleanup was encoded into structural tests, linters, and background automation while people moved to missing-capability and missing-constraint decisions.
- Rejected `when-code-is-free` because it concerns oracle-bounded problem selection rather than selective codification of a workload, and its relevant verification premise is already carried by the source's existing automation-boundary link.

**Instructions and reverse direction:**

- Read `kb/instructions/COLLECTION.md` and searched with `rg -n -i 'execution-time|advance planning|defer (a )?(choice|decision)|deterministic|codif|stable (pattern|mapping)|routine work|adaptive planning|agent (boundary|frontier)' kb/instructions --glob '*.md'`.
- The hits describe deterministic validation inside procedures but do not operationalize the source's selection effect, so no instruction edge survived. In the reverse direction, the metacircular-interpreter note can usefully point to the source as the workload consequence of hardening stable paths.

**Path verification:**

- Verified every kept, bidirectional, reverse, rejected, and index candidate with `test -f`; no candidate path was missing.

## Connections Found

- [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) -- **grounds**: supplies spec completeness, oracle strength, interpretation space, and pattern stability as concrete tests for when a choice is predictable and verifiable enough to leave open-ended agent judgment.
- [Spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md) -- **mechanism**: shows how repeated behavior exposes stable regularities that can be extracted into deterministic helpers, tests, schemas, and verifiers, performing the boundary movement the source assumes.
- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) -- **contrasts**: prevents “removed from agent discretion” from being mistaken for elimination of meaning-dependent judgment; codification prepays or relocates that judgment into specification, implementation, and verification.
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) -- **extends**: adds an elastic-workload consequence in which capacity freed from routine work is spent on more volume or harder frontier work, and derives measurements per human judgment rather than total hours.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **evidenced-by**: its source-inspected cases repeatedly promote successful task traces into executable programs under strong local oracles while reporting that cross-case synthesis and other higher-order judgments remain open.
- [Swamp](../../../../agentic-systems/reviews/swamp.md) -- **evidenced-by**: separates ambiguous operational interpretation and artifact authoring at the LLM boundary from validation, scheduling, permissions, execution, and audit in a repeatable symbolic runtime.
- [Ingest: Ironies of Automation](../../../../sources/ironies-of-automation.ingest.md) -- **evidenced-by**: provides historically prior, domain-bounded evidence that automation leaves operators the unsupported residue designers could not automate, while also warning that this allocation can create monitoring and skill-maintenance problems.
- [Ingest: Harness Engineering: Leveraging Codex in an Agent-First World](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) -- **evidenced-by**: documents recurring manual cleanup being converted into standards, structural tests, linters, and background agents while human effort moves toward identifying missing capabilities and unenforced constraints.

## Bidirectional Candidates

- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) <-> source -- **grounds (candidate→source)**: the source supplies the selective-codification mechanism behind the target's first step, where routine work becomes computational and attention shifts to the harder frontier.
- [Spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md) <-> source -- **extends (candidate→source)**: the source develops a distributional consequence of spec mining—each preferentially mined stable mapping can make the remaining agent workload less predictable.

## Reverse-edge Candidates

- [LLM-executed methodologies are metacircular interpreters, not compilers](../../../../notes/llm-executed-methodologies-are-metacircular-interpreters.md) → source -- **extends**: the target already distinguishes reinterpreted natural-language methodology from stable paths hardened into validators and commands; the source adds what that hardening predicts about the work left inside the interpreter.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) -- supplies a timing rule for commitment, but its relevant stability premise is already more directly carried by the kept decision-heuristics and spec-mining notes.
- [Constraining and extraction both trade generality for reliability](../../../../notes/constraining-and-extraction-both-trade-generality-for-reliability.md) -- names the broad tradeoff but does not explain selective migration or the resulting composition of residual agent work.
- [Scaling absorbs scaffolding at fixed difficulty, not at the frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- also describes a moving frontier, but its cause is changing model capability at fixed task difficulty rather than codification of predictable choices.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) -- gives a useful allocation case, but the kept computational-autonomy note already links it as a worked instance and gives readers the more specific route.
- [Compound Engineering Plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- separates mechanical computation from subject and strategy judgment, but Swamp more cleanly exhibits the symbolic-runtime versus LLM-interpretation boundary.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) -- critic-gated executable skill promotion is a strong instance, but the kept trace-learning survey subsumes it alongside comparable systems and states the shared oracle limit.
- [Ingest: When code is free, research is all that matters](../../../../sources/when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md) -- its problem-selection argument concerns absent ground truth and research taste, not evidence that predictable choices are preferentially codified out of an existing workload.
- [Note](../../../../types/note.md) -- governs note structure and validation but supplies no evidence or mechanism for the source's substantive claim.
- [cp-skill-validate](../../../../instructions/cp-skill-validate/SKILL.md) -- deterministic validation is an instance of a symbolic control, but the procedure neither depends on nor operationalizes the residual-work selection claim.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- under “Governance and computational allocation,” the source would explain why codifying settled choices moves the actor boundary toward cases that still require interpretation.
- [Computational model](../../../../tags/computational-model-README.md) -- under “Tensions,” the source would add the workload consequence of replacing interpreted choices with symbolic structure: the remaining LLM-facing work becomes less amenable to the same treatment.

## Synthesis Opportunities

- The source, [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md), and [Ingest: Ironies of Automation](../../../../sources/ironies-of-automation.ingest.md) together imply a human-operator hazard not yet captured as theory: selective automation can make the residual interventions harder while simultaneously removing the routine practice that maintained the operator's takeover skill. This should remain scoped to human-inclusive systems; it does not follow for an agent whose capability is unaffected by disuse.

## Maintenance Observations

- `ironies-of-automation.ingest.md` retains no verbatim source quotes. Before a future writer uses it as a load-bearing tracked-source citation in this note, run `cp-skill-ground`; the ingest's current summary is sufficient for discovery but not for discharging the note collection's grounding requirement.

## Flags

None
