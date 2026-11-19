---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/scaling-monosemanticity-claude-3-sonnet.ingest.md"
source_has_frontmatter: true
date: "2026-11-03"
depth: standard
---

# Connection Report: Ingest: Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet

**Source:** [Ingest: Scaling Monosemanticity](../../../../sources/scaling-monosemanticity-claude-3-sonnet.ingest.md)

The ingest already makes seven inline links: ROME, representational form, opacity, inspectable-artifact, knowledge-storage, verbalizable-representations and reading-between-the-dots. It has no labelled footer. This report checks those links and adds candidates. They come mainly from the ingest's occasion, which is the localization and content-versus-scope question shared with the ROME ingest. A sibling report, [scaling-monosemanticity-claude-3-sonnet.connect.md](./scaling-monosemanticity-claude-3-sonnet.connect.md), was written against the snapshot before this ingest existed. It covers the opacity and inspection cluster. This report reuses its findings where they still apply and does not overwrite it.

## Discovery Trace

**Outbound rules read:** `kb/sources/COLLECTION.md` "Outbound links". Allowed destinations: theory, reference, agent-memory-systems, agentic-systems, tags and other sources. `kb/work/` and `kb/instructions/` are excluded. Labels by destination: theory gets `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`; theory/definitions also gets `defined-in`; sources get `compares-with` and `see-also`; external gets `derived-from` and `see-also`. The `derived-from` external edge to the paper URL is carried by the ingest's `source` field. External prospecting was skipped.

**Prior context reused:** the sibling snapshot connect report (full discovery trace over theory, sources and tags; SAE, monosemantic, Golden Gate and sparse-autoencoder vocabulary had no KB footprint before this ingest). The ROME connect report `kb/reports/cache/connect/sources/rome-locating-and-editing-factual-associations-in-gpt.connect.md`, Connections Found section only. It uses pre-relocation `notes/` paths, which were resolved to current `kb/theory/` paths by title.

**Title listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'explicit retention|reflection|addressab|localiz|opac|parametric|weights|probe|inspect|blackbox|interpret|steer|retention'`. Flagged: only-explicit-retention-is-durable-writable-and-addressable, reflection-buys-addressability, reflection-makes-retained-lessons-second-order, localized-retention-pays-where-change-is-sparse-in-a-matching, addressable-theory (definition), addressability-grain-sets-a-matched-selective-read-floor, evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs, plus the opacity and inspectable-artifact notes already linked.

**Description reads:** `rg -N '^description:'` on the flagged notes and on concept-bottleneck-models-paper-v3.ingest, addressable-theory, the ROME ingest and reflective-coverage-is-graded-across-representational-forms.

**Body search** (excluding `kb/work/**`, `kb/reports/**`, `.snapshots/**`):
- `rg -n -i 'scope-addressab|content-addressab|scope addressab|content addressab' kb`. Hits: this ingest, the ROME ingest, build-systems-a-la-carte (content-addressable hashing, a different sense, rejected), retained-theories-may-improve-sample-efficiency lines 124 and 243 (cites ROME with the content-without-scope framing and pairs it with concept bottleneck models). The last is a strong reverse-edge candidate.
- `rg -l -i 'sparse autoencoder|monosemantic|golden gate|steering vector|activation patching|causal tracing|activation clamp|superposition|knowledge edit|model edit' kb`. Theory hits: reflection-makes-retained-lessons-second-order, localized-retention-pays-where-change-is-sparse-in-a-matching, definitions/theory-builder, definitions/theory-builder-checks. The agentic-system-analyses hits are "model edit" in a tooling sense, which is outside the authorised destinations anyway.
- `rg -n -i '...|interpretab' kb/theory`. Found reflection-buys-addressability lines 62 and 69, theory-builder line 208, theory-builder-checks row 29, reflection-makes-retained-lessons-second-order line 37 (names "activation steering" explicitly), and localized-retention line 22. Rejected as wrong sense: factory-learning-mechanisms line 64 and revision-guided-by-rationale (faithfulness of rationales).
- `rg -n -i 'falsif|interpretab|editing' kb/theory/only-explicit-retention-is-durable-writable-and-addressable.md`. Line 39 says a numerical representation with a tested commitment-level editing interface should be assessed by that interface.
- `rg -l 'scaling-monosemanticity' kb -g '!kb/reports/cache/**'`. Only the ingest itself, so no inbound links yet.

**Link following:**
- Representational form, sections "Opacity and inspection" (line 33, "Probe distributed-parametric artifacts behaviorally"), "Localization", "Categories and their inspection methods" and "Addressability and the localized forms". The ingest's "localized under an instrumented path" reading fits the Localization section's path-relative definition. Also, "a parameter is addressable under the runtime's path, and editing it can change behavior ... without identifying which instruction-level commitment the edit revises".
- ROME ingest, Connections Found. It routes ROME to only-explicit-retention (falsifier), reflection-buys-addressability (rescoping), opacity and reflective-coverage. The SAE ingest is the second instance of the same gap, so the same targets are candidates. Each is re-judged below, because clamping is not a durable weight write.
- retained-theories-may-improve-sample-efficiency, lines 115-135 and footer 236-250. Its "Two lines of work" paragraph compares ROME (weight write, persistent) with concept bottleneck models (per-inference correction through a supervised concept layer). The SAE clamp is a third arrangement: per-inference, like CBMs, but over an unsupervised, found dictionary.
- reflection-buys-addressability Scope and Open Questions; reflection-makes-retained-lessons-second-order lines 30-40; theory-builder lines 200-215; theory-builder-checks rows 25-31.

**Other destinations:**
- `kb/reference/`: describes Commonplace itself. No trigger. Skipped.
- `kb/agentic-systems/`, `kb/agent-memory-systems/`: no trigger, since the source is about model internals. KBLaM (`kb/agent-memory-systems/reviews/KBLaM.md`), kept by the ROME report as a fellow inject-into-internals method, was considered and rejected below.
- `kb/tags/`: the ingest already carries `tags: [observability, artifact-analysis]`. Fit was assessed in the sibling report. The artifact-analysis tag now fits, because the ingest draws a form-field consequence (Extractable Value 1).

## Connections Found

Existing inline links, checked: all seven paths exist and pass the articulation test. As a labelled footer, they would read: ROME **compares-with** (axis: weight write versus activation clamp, both content without scope); representational form **defined-in** (distributed-parametric, localization); opacity **is-evidence-for**; inspectable-artifact **is-evidence-for** (with the narrowing the ingest already states); knowledge-storage **compares-with** (presence versus activation, an analogy at a different level, as the ingest says); verbalizable-representations **compares-with**; reading-between-the-dots **compares-with**. New candidates follow.

- [Reflection makes retained lessons second-order](../../../../theory/reflection-makes-retained-lessons-second-order.md) -- **is-evidence-for**: the note says rejection needs only content-addressability, while rescoping needs scope to be a represented aspect. It names "activation steering" among parametric pathways that produce analogous effects without targeting a represented commitment (line 37). Feature clamping is a concrete instance at production scale. It reaches the concept, but by construction it applies at every position, so there is no represented boundary to narrow. That is the ingest's Extractable Value 2 in the note's own vocabulary. This is the strongest new candidate.
- [Reflection buys addressability](../../../../theory/reflection-buys-addressability.md) -- **is-evidence-for**: its Scope says "Mechanical observation or modification can therefore coexist with weak semantic addressability", and that interpretability research tries to add operations over parametric retention. SAE features are exactly mechanical observation (top activations) plus modification (clamps) with weak semantic addressability: labels are model-written, units split with dictionary size, and there is no commitment identity. The note's open question asks whether external interpretability tooling can make parametric retention addressable to the improving system itself. The paper does not answer it, because the clamp is applied by researchers, but it is the state of the art that question points at. The ingest should say that it only bounds the question.
- [Explicit retention provides direct targets for selective revision](../../../../theory/only-explicit-retention-is-durable-writable-and-addressable.md) -- **is-evidence-for**: line 39 holds that "a numerical representation with a tested commitment-level editing interface should be assessed by that interface, not excluded by its form". The SAE clamp is a tested interface, but at concept level, not commitment level, and it is not durable because nothing is written to weights. So it fails the note's falsifier on durability where ROME failed on scope. Together the two ingests show different shortfalls against the same falsifier. The ingest's Connections Found already says "Unlike ROME, nothing is written to the model".
- [Addressable theory](../../../../theory/definitions/addressable-theory.md) -- **defined-in**: the ingest uses "content-addressability" and "scope-addressability", and representational form states that "Addressability depends on the localization question alone". A reader needs the graded, parts-and-scope definition to see why a clampable unit without a scope handle is only partly addressable.
- [Concept bottleneck models](../../../../sources/concept-bottleneck-models-paper-v3.ingest.md) -- **compares-with** on the axis "per-inference intervention through a concept interface". CBMs supervise a fixed concept layer during training and correct predicted concept values at test time. The SAE finds an unsupervised dictionary after training and clamps feature values at inference. Both corrections are per-inference, not persistent. They differ in where the vocabulary comes from (supplied versus found), and that difference drives the SAE's coverage and feature-splitting limits. retained-theories-may-improve-sample-efficiency already sets CBMs beside ROME, so this edge completes a three-way comparison.
- [Representational form](../../../../theory/definitions/representational-form.md) -- second label, **is-evidence-for**, in addition to the existing defined-in use. The Localization section defines units relative to the consumer on a path, and the Addressability section notes that editing under the runtime's path can change behavior under the interpreter's path without identifying the commitment. The SAE-instrumented forward pass is a third path between those two. Its units are concept-level activation directions, more than parameters and less than instructions. This is the evidence the ingest's Recommended Next Action wants logged before that section is amended. The amendment should stay with the definition's maintainers.
- [Definitions: theory-builder](../../../../theory/definitions/theory-builder.md) -- **see-also**, weak: the "Content located in weights" exclusion case says interpretability methods move located parts "toward the localized side", and whether they meet condition 1 is empirical per model and method. This paper is such a method, but it locates activations, not weights, so it falls short of that bullet's premise. Keep it only if the ingest adds a sentence drawing that distinction. Otherwise drop it.

## Bidirectional Candidates

- [ROME](../../../../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) <-> source -- **compares-with**: the ROME ingest compares itself with verbalizable-representations and reading-between-the-dots as read-side instruments. A return link to this ingest gives it a second write-side intervention. That intervention is an activation clamp, not a weight edit, and it shows the same content-without-scope gap. This makes ROME's "highest-reach" Extractable Value 1 a pattern across mechanisms, not a single case.
- [Verbalizable Representations Form a Global Workspace](../../../../sources/verbalizable-representations-global-workspace-llms.ingest.md) <-> source -- **compares-with**: carried over from the sibling report. The return path lets the J-space ingest compare its Jacobian lens with the dictionary-learning instrument it implicitly builds on.

## Reverse-edge Candidates

- [Retained theories may improve sample efficiency under structured shifts](../../../../theory/retained-theories-may-improve-sample-efficiency.md) → source -- **evidenced-by** (theory's own authorised set; check `kb/theory/COLLECTION.md`): the "Two lines of work" paragraph sets ROME (persistent weight write, content without scope) against CBMs (per-inference correction within a supplied concept vocabulary). The SAE clamp is per-inference over a found vocabulary, and it shows the same missing scope handle. One sentence would show that scope-addressability is absent across all three update interfaces. Caveat: the paper reports selected successes with no success rate, so it supports the interface description, not a correction-benefit measurement.
- [Reflection makes retained lessons second-order](../../../../theory/reflection-makes-retained-lessons-second-order.md) → source -- **evidenced-by**: the line-37 Scope bullet names activation steering without citing a source. This ingest would be its citation.
- [Opacity depends on the inspection question and budget](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) → source -- **evidenced-by**: carried over from the sibling report. Coverage grows with dictionary size and compute, and the authors estimate that full coverage would cost more compute than training. This gives the Scale section a measured distributed-parametric case.
- [Definitions: theory-builder checks](../../../../theory/definitions/theory-builder-checks.md) → source -- row 29 covers model editing that locates a fact in weights. A sibling row could cover a found activation decomposition that is clamped at inference. That row would be classified "partly localized under an instrumented path, not durable", and it would test whether the checks distinguish activation-level from weight-level localization. Only if the definition's maintainers want the case. This is not a citation edge.
- [Conceptual blending in humans and language models](../../../../sources/conceptual-blending-humans-and-language-models.ingest.md) → source -- **compares-with**: carried over from the sibling report. It gives large-model evidence for the superposition step that ingest supports only with toy-model work.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../theory/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- line 22 lists model editing and adapters as attempts to recover localization inside learned substrates, and any method producing "scoped, checkable edits" qualifies. The SAE clamp is neither scoped nor durable, and the paper does not measure impact closure (no side-effect measurement). A link would only say the method does not qualify, which adds little. Reconsider if a conditional-clamp experiment appears.
- [Reflective coverage is graded across representational forms](../../../../theory/reflective-coverage-is-graded-across-representational-forms.md) -- the ROME report kept it, and the sibling report rejected it. Its boundary rule (control of an external dependency does not make it covered) would apply only if some system adopted the SAE harness as a control surface. The paper describes researcher tooling, not a reflective system. Still rejected.
- [Missing rationale does not exclude a theory builder; weight-only retention excludes one across runs](../../../../theory/evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs.md) -- it concerns weight-only retention across runs in specific agent systems. The SAE does not change what is retained across runs. Title-level overlap only.
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../theory/addressability-grain-sets-a-matched-selective-read-floor.md) -- "addressability" in the sense of read-volume for recoverable content, a different question.
- [KBLaM](../../../../agent-memory-systems/reviews/KBLaM.md) -- injects KB facts into internals. The SAE reads and clamps found features and injects nothing from a KB. The ROME rationale (writing content into a model) does not carry over.
- [Build systems à la carte](../../../../sources/build-systems-a-la-carte.ingest.md) -- "content-addressable" means hash-keyed storage there. Keyword collision.
- Carried-over rejections from the sibling report: evaluation-automation-is-phase-gated-by-comprehension, oracle-strength-spectrum, grunwald-mdl-tutorial, parametric-reproduction-cannot-replace-an-authoritative-record, weight-resident-methodologies-compress-behavior-in-context, tulving-pearlstone, gentle-coding-research, and the scientific-discovery "interpretable" hits. Nothing in the ingest changes those judgments. Minimum-viable-vocabulary (kept as the weakest candidate in the sibling report) is dropped here: the ingest's Extractable Value 4 routes the frequency-threshold result to opacity, not to naming.

## Index Membership

- [observability](../../../../tags/observability-README.md) and [artifact-analysis](../../../../tags/artifact-analysis-README.md) -- already present in the ingest's `tags:`. artifact-analysis now meets its inclusion condition because Extractable Value 1 draws a consequence for the form field. Sources do not join generated member listings, so no index edit follows.

## Synthesis Opportunities

ROME (weight write), concept bottleneck models (supervised per-inference correction) and this SAE ingest (found-dictionary per-inference clamp), together with reflection-makes-retained-lessons-second-order, imply a claim no note yet states. Across three distinct update interfaces into learned substrates, content can be reached, but none exposes an applicability boundary. Scope-addressability in these cases comes only from outside the substrate, through a harness or retrieval condition. The claim would be falsified by a conditional-clamp or scoped-edit experiment that measures collateral effects outside the stated condition. The ingest names that experiment as untested. Under the Quality bar this belongs in `kb/log.md` first, as the ingest's Recommended Next Action already proposes.

## Maintenance Observations

- `kb/reports/cache/connect/sources/rome-locating-and-editing-factual-associations-in-gpt.connect.md` links pre-relocation `notes/` paths (for example `../../../../notes/reflection-buys-addressability.md`). The current targets are under `kb/theory/`. The cached report is stale against the theory relocation. Regenerate it, do not hand-fix it.
- The snapshot contains NUL bytes, so `rg` treats it as binary. This was recorded in the sibling report and still applies to any quote grounding for this ingest (`rg -a`).

## Flags

- Tension to keep visible: the "Representational form is-evidence-for" candidate and the Recommended Next Action both point at amending the Addressability section. The ingest itself rests the claim on one SAE design at one layer. A writer should log the result first and not amend the definition from this source alone.
- The causal evidence is selected successes. Any theory note that adopts the reverse edges should cite the paper for the interface's existence and shape, not for how reliable steering is.
- Split candidate: no. The ingest has one occasion and one cluster.
