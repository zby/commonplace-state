---
description: "Pre-ingest connections for small-code-model selection limits, extraction recovery, and calibrated early stopping"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/selection-without-signal-recovery-through-expression.md"
source_has_frontmatter: true
date: "2026-09-19"
depth: standard
---

# Connection Report: Selection Without Signal, Recovery Through Expression

**Source:** [Selection Without Signal, Recovery Through Expression](../../../../sources/.snapshots/selection-without-signal-recovery-through-expression.md)

Pre-ingest discovery using `cp-skill-connect`. The matching ingest will carry any accepted outbound links; no snapshot mutation is proposed.

## Discovery Trace

- Read the full 2,295-line snapshot, including operator definitions, positive and negative results, discussion, ledger, finite-sample appendix, and references. Loaded sources and reports contracts and connect-report type. Source has no tags.
- Reused the destination README heads and fresh title listing generated in this serial discovery session: `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. The combined listing output was truncated; focused queries supplied candidate-level resolution. Learning-theory and evaluation heads supplied the search/evaluation and oracle routes. Neither declared completeness.
- Notes and sources: `rg '^description:' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md' | rg -i 'candidate.*generat|generat.*candidate|discriminat|expression|extractor|interface.*fail|falsif'` found proposal-selection, oracle amplification, interpreter failure, and Autoreason. Read the three notes and Autoreason ingest. Kept proposal-selection for its precise search-range limit; kept oracle amplification as bounded evidence about a tested selector's absent discrimination; kept Autoreason as a comparison across generation-versus-selection regimes.
- Reference and agentic-systems: `rg -n -i 'coverage|candidate pool|extractor|extraction|do.no.harm' kb/reference/proposals/ kb/agentic-systems/ --glob '*.md'` yielded codec and generic coverage matches. No source-to-system evidence relation was earned: extraction of review results and runtime coverage are different mechanisms from recovering code already in raw generation. No targets retained from these collections.
- Agent-memory-systems: `rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg -i 'reflexion|refin|repair|verif'` and the README routed to Reflexion, already read in this serial pass. It is a valid background comparator, but omitted to avoid duplicating Autoreason's more discriminating generation-selection comparison.
- Link following: interpreter-failure note led to the three-way-diagnosis note; its body makes the assembled-input boundary explicit. Oracle-amplification note led to discrimination-versus-accuracy, also read. These clarified that extraction losses need their own harness measurement and should not be silently attributed to model reasoning.
- The experimental-contrast note, read in the preceding pass, supplies a direct connection for the paper's compute and baseline corrections. No similarity scores or external searches were used. External source URL was already supplied. Instructions/workshops excluded by source contract.

## Connections Found

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **is-evidence-for**: the bounded coverage measurements instantiate the note's claim that selection cannot retrieve a correct candidate absent from the generated pool. This supports that search/evaluation separation, not a persistent self-improvement finding.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **is-evidence-for**: tested rerankers fail where public-passing candidates offer weak usable discrimination or no correct alternative; the sound-relation probe exposes why a correct but rarely firing check need not improve selection. The paper does not establish failure of all possible checks.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **is-evidence-for**: the compute-confounded apparent repair gains and ACE's distinct full-budget-consensus reference show why matched generation budgets, control identity, and chosen operating point must remain attached to each claim.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../notes/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — **compares-with**: M1 separates recovering an already correct body from generating new logic. A wrong required name can be interpreter non-conformance; prose discarded by a fragile extractor can instead be a harness loss. The supplied output contract decides attribution.
- [Autoreason: Self-Refinement That Knows When to Stop](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md) — **compares-with**: both locate refinement value between candidate availability and selection capability. Autoreason reports benefits in a different model/task regime; Selection's frozen-small-model null bounds transfer rather than refuting that method.
- [Original paper](https://arxiv.org/abs/2606.16999) — **derived-from**: the future ingest analysis derives from this paper.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) could author **evidenced-by** to the future name-paired ingest for its search-range boundary, using the observed finite-pool coverage rather than the paper's stronger no-selector rhetoric. Notes contract authorizes this relation; cite the ingest with sufficient quotes or `(snapshot required)`.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md): the small-model conditional verification results do not establish stagnation across releases or a general automation ceiling. Oracle amplification is the narrower landing.
- [LLM output deviation requires three-way diagnosis](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md): extraction can occur downstream of the sampled model output; the taxonomy alone would obscure that boundary. Use the interpreter-failure comparison with explicit harness attribution instead.
- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md): same-instance retry is relevant background but less useful here than Autoreason's explicit candidate-generation/selection comparison.

## Index Membership

None

## Synthesis Opportunities

None. The existing search/evaluation distinction owns the strongest general claim. A future evidence note could assemble coverage, selector discrimination, and extraction losses, but this single source does not establish their distribution in KB work.

## Maintenance Observations

None

## Flags

- Do not promote the twenty-six tested operators' null to a theorem about every leakage-free selector. Lemma 1 explicitly assumes majority symmetry; the first-passer baseline and majority selector are distinct. Finite-sample empty traps do not establish zero population mass.
- M1's positive is recovery of code already present, plus public-test name alignment. The large replicated gains are DeepSeek-Coder-1.3B +12/164 HumanEval+ and +33/370 MBPP+; instruction-tuned Qwen gains are small and non-significant. Do not call this new semantic reasoning.
- ACE's 19.1% saving is relative to drawing the full budget, with zero observed harm relative to full-budget consensus. Its threshold was selected on evaluation data without selection correction; a sequential first-public-passer baseline already saves much of the same compute. The paper's blanket claim that both survivors are do-no-harm by construction is too broad for ACE, whose aggressive thresholds show harm.
- The n >= 45 result is specific to zero observed Bernoulli harm at the stated 5% harm and 90% confidence parameters under i.i.d. sampling; it is not a universal minimum study size.
- Generation-call matching does not equal all-compute matching. Some operator descriptions also use hidden correctness in analysis/training diagnostics, so distinguish deployment information from offline oracle-backed diagnostics rather than repeating an unqualified all-operators leakage-free assertion.
- Known snapshot DOI-as-date validation exception is authorized. Preserve bytes.
