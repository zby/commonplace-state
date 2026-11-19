---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Ingest: Minimizing Syntactic Dependency Lengths (Temperley & Gildea 2018)

**Source:** [Ingest: Minimizing Syntactic Dependency Lengths (Temperley & Gildea 2018)](../../../../sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md)

The ingest already carries seven footer edges: `derived-from` to the DOI, `compares-with` to the Gibson DLT, Temperley 2007 and Futrell 2015 ingests and to two-rewrites, and `is-evidence-for` to human-writing-structures-transfer and the contrast note. This report does not repeat those. It lists the new candidates found and the missing inbound edges. An earlier report, `temperley-gildea-2018-minimizing-dependency-lengths.connect.md`, was written against the snapshot before this ingest existed. All of its outbound candidates are now encoded in the ingest.

## Discovery Trace

**Setup reads:**
- `kb/sources/COLLECTION.md`, the outbound-links section. Authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags and sources, plus `external` through `derived-from` and `see-also`. `kb/work/` and `kb/instructions/` are excluded. Labels for theory are `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with` and `see-also`, with `defined-in` limited to theory/definitions. Sources take `compares-with` and `see-also`. Reference takes `see-also` only.
- `kb/types/connect-report.md`.
- The prior snapshot-targeted report in the same directory, used to avoid repeating evaluated candidates.

**Sibling sources:**
- Read the `Relevant Notes:` footers of the futrell-2015, futrell-levy-gibson, gibson-1998, gibson-DLT and temperley-2007 ingests. `grep -n 'temperley-gildea'` across all six sibling ingests returned no hits. No sibling links back to this ingest yet.
- The gibson-2019 ingest has inline connections only and no footer. Its centre is information-theoretic efficiency and ambiguity.
- The gibson-1998 ingest is new since the prior report. Its description reads "supports nesting and heavy-last rules, human-only". Lines 52-53 and 157 derive the subject-versus-object relative clause contrast and center-embedding overload.
- `rg -n -i 'object relative|...|antilocal|Demberg|Levy'` over gibson-1998 and futrell-levy-gibson. The futrell-levy-gibson ingest (line 25) reviews antilocality, decay and interference, and lossy-context surprisal, and it "takes no position on which motivation is correct". This ingest's Contribution assessment names "the overlapping Futrell, Levy and Gibson review" as a comparison point but does not link it.

**Title listing scan (theory):**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'pressure|trade|optim|target|proxy|goodhart|metric|lint|review.*select|proponent|narrative|bias|predictab|surpris|frequen|expect|convention|rule|writ|prose|reader'` flagged these: borrowed-patterns-transfer-only-over-shared-mechanism, a-proximate-target-is-checked-for-achievement-not-for-warrant, retaining-episode-evidence-keeps-a-distilled-rule-open-to, a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited, writing-styles-are-strategies-for-managing-underspecification, warranted-reader-update-is-the-objective-of-substantive-writing, plus the already-linked two-rewrites and human-writing-structures.
- `rg -m1 '^description:'` over the flagged files. Borrowed-patterns, proximate-target and soft-degradation were kept for full reads. The others were rejected (see below).

**Body search:**
- `rg -l -i 'goodhart|proxy (metric|measure)|over-?optimi' kb/theory` matched oracle and quality-signal notes, none on a goal-position proxy. The proximate-target note is the specific home for that idea.
- `rg -l -i 'proponent|selective coverage|narrative review|author.s own stud' kb/theory kb/reference` found no hits. No theory note treats proponent-authored reviews.
- `rg -l -i 'extraposition|antilocality|predictability|n-gram'` over theory, reference, agentic-systems and agent-memory-systems. The hits are an unrelated sense of "predictable" (codification, oracles) and agent-memory reviews. All were rejected as keyword-only.
- `rg -l -i 'interference' kb/theory` matched ten notes. `rg -n -i 'interference|similar'` on soft-degradation-often-binds found lines 16-26: intervening irrelevant task content between dependent subtasks degrades web agents, and the benchmark "does not isolate volume from interference".
- `ls kb/sources/*.ingest.md | rg -i 'lost|middle|long-context|position|distance|syntax|reading|readab|plain|style|prose'` matched position-bias and llm-webagents-long-context among others. Their descriptions were checked.

**Reference, tags and descriptive collections:**
- `ls kb/tags/` lists no writing, prose or psycholinguistics tag. The source ingest carries no `tags:`. The tag pass was skipped.
- The reference destination was skipped. The prior report's `rg -i 'sentence|word order|prose style' kb/reference` found only incidental hits, and only `see-also` is authorised. `source-adoption-policy` was reached through borrowed-patterns. It belongs to the theory note, not to this source.
- agent-memory-systems and agentic-systems were skipped. The source has no match for their external-system reviews.
- External prospecting was skipped by rule. The DOI is already linked as `derived-from`.

**Link following:**
- From borrowed-patterns to `kb/reference/source-adoption-policy.md`. It gives the fast-pass rule for patterns that share a mechanism. This confirms that the note governs adoption of human writing conventions into agent-read prose.
- From proximate-target to its framing: an achievement check on a target property produces a "green gate" with no evidence for the linking claim. The ingest's Extractable Value 5 contemplates "a lint check or rule". This is the case that framing warns about.
- From soft-degradation line 26 to `kb/sources/llm-webagents-long-context-reasoning-benchmark.ingest.md`. That source is the agent-scale case of material inserted between dependent elements. It is reached more usefully through the soft-degradation note.

## Connections Found

- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../theory/borrowed-patterns-transfer-only-over-shared-mechanism.md) -- **rests-on**: the Limitations bullet "No evidence about LLM readers" says that every proposed mechanism is human memory (decay, storage, retrieval interference), so each convention needs an LLM-side check. That requirement depends on this note's claim that transfer is licensed only over a shared mechanism. The existing human-writing-structures edge names the per-convention test. This note supplies the general reason the test is owed. The context phrase could be: "the writer rules transfer to agent readers only if a shared distance-cost mechanism is shown".
- [A proximate target is checked for achievement, not for warrant](../../../../theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) -- **compares-with**: the shared axis is a measurable property adopted because it is held to serve an objective, while its linking claim is separately contested. Writers demonstrably achieve short dependencies (47.5 observed against 82.7 random). The review shows the link to reading ease as small in naturalistic text, reversible through antilocality, and partly confounded with expectation. A dependency-length lint, which Extractable Value 5 floats, would be an achievement check on exactly such a target. This supports the ingest's advice to state locality "as a pressure ... not as a quantity to minimize".
- [Soft degradation can bind before the hard cap even when required evidence fits](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- **compares-with**: the shared axis is cost from material placed between dependent elements, and whether distance or interference carries it. The review lists rival metrics: word count, new discourse referents, elapsed time with similarity-based interference, and intervening heads. The web-agent benchmark that the note cites likewise "does not isolate volume from interference". This axis differs from the gibson-1998 ingest's edge to the same note ("load set by structure rather than length").
- [Futrell, Levy and Gibson ingest](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) -- **compares-with**: the ingest already names this as "one comparison point" for originality but does not link it. The shared axis is two proponent-authored DLM reviews that both leave the processing motivation open. Temperley & Gildea discriminate DLM from named rivals (EIC, end-weight, predictability). Futrell, Levy and Gibson instead test against six null baselines and split grammar from usage with linearization models. Readers choosing a citation for a bounds section need to know which review supplies which.
- [Gibson 1998 SPLT ingest](../../../../sources/gibson-1998-linguistic-complexity-locality.ingest.md) -- **compares-with**: the shared axis is evidence for the relative-clause and center-embedding rule. This review calls that rule the strongest direct comprehension evidence. The 1998 ingest holds the primary derivation (subject- versus object-extracted relatives, doubly center-embedded overload). Cite 1998 for the rule's mechanism and this review for its later critique (small naturalistic effect, antilocality).

## Bidirectional Candidates

- [Futrell, Levy and Gibson ingest](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) <-> source -- **compares-with**: the return path is useful because that ingest's Recommended Next Action asks for a bounded theory note. This review's rival discriminations and its predictability frontier are the bounds that note needs.

## Reverse-edge Candidates

All targets are sources-collection ingests. They can author `compares-with` under `kb/sources/COLLECTION.md`.

- [Gibson's Dependency Locality Theory ingest](../../../../sources/gibson-dependency-locality-theory.ingest.md) → source -- **compares-with**: its Limitations section asserts the rivals and antilocality "from background knowledge". This ingest is now the tracked citation for them: Demberg & Keller, Levy & Keller, ACT-R decay with interference.
- [Futrell 2015 ingest](../../../../sources/futrell-dependency-length-minimization.ingest.md) → source -- **compares-with**: it reads locality as a pressure, not a target, without naming the competing pressure. This ingest names n-gram predictability and the tradeoff frontier.
- [Temperley 2007 ingest](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) → source -- **compares-with**: the 2007 constructions reappear here as discriminators against EIC and end-weight, with the grammar-versus-choice estimate (51.4 against 47.5).
- [Gibson 1998 SPLT ingest](../../../../sources/gibson-1998-linguistic-complexity-locality.ingest.md) → source -- **compares-with**: it has no access to the later critique of locality-based cost. This review supplies it.
- Theory-side inbound edges from two-rewrites and the contrast note were proposed in the prior report. They still apply, with the consolidation caveat under Maintenance Observations.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) -- rejected. The ingest's advice to tag each rule with its evidence class looks similar, but that note concerns retaining the episodes behind a KB-distilled rule. It does not concern labelling external evidence types, so the overlap is topical.
- [A framework rule with a boundary-preserving rival is not an inherited constraint](../../../../theory/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) -- rejected. The ingest's "rivals" are rival scientific explanations, not rival designs that preserve framework invariants. Only the word matches.
- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- rejected. It treats context-file styles (prescriptive, explanatory and so on), not word order.
- [Warranted reader update is the objective of substantive writing](../../../../theory/warranted-reader-update-is-the-objective-of-substantive-writing.md) -- rejected. It concerns contribution selection, not sentence-level form.
- [System use provides evidence of theory fit, not independent warrant](../../../../theory/system-use-provides-evidence-of-theory-fit-not-an-independent-test.md) -- rejected. The proponent-authorship concern in Limitations is about selection in a review, not about live-system use.
- [Web-agent long-context benchmark ingest](../../../../sources/llm-webagents-long-context-reasoning-benchmark.ingest.md) -- rejected as a direct edge. The soft-degradation edge reaches it with the interpretive framing, and a direct source-to-source edge would skip the scale caveat.
- [Position bias ingest](../../../../sources/position-bias.ingest.md) -- rejected. It concerns order effects in pairwise LLM judging, not distance between dependent elements.
- [Gibson et al. 2019 efficiency ingest](../../../../sources/gibson-2019-how-efficiency-shapes-language.ingest.md) -- still rejected, as in the prior report. Its axis is ambiguity and information-theoretic efficiency.
- Local-materialization, soft-bound-traditions, human-llm-differences, three-simplification-passes and the attention ingest -- still rejected for the reasons in the prior report. Siblings already carry those axes, and this review adds nothing distinct to them.

## Index Membership

None. No writing or psycholinguistics tag exists, and the source carries no `tags:`.

## Synthesis Opportunities

This repeats the prior report's finding, which is now stronger with seven captures: the six dependency-locality ingests plus gibson-2019. Together they imply one bounded theory note. For human readers, keeping dependents near their heads lowers comprehension cost. That holds as a pressure traded against predictability, and the direction depends on head direction. Direct cost evidence exists only for relative clauses and center-embedding. The distance metric is contested, and LLM transfer is untested. The new candidates add two framing points for that note. Borrowed-patterns gives the reason transfer is owed a test. Proximate-target warns against a dependency-length lint. Do not create it during connect.

## Maintenance Observations

- `kb/reports/cache/connect/sources/temperley-gildea-2018-minimizing-dependency-lengths.connect.md` targets the snapshot path and predates the ingest. It is superseded by this report and can be regenerated or discarded.
- None of the six sibling ingests links back to this ingest. The cluster has fully meshed `compares-with` edges among the older ingests but none inbound to the bounding review, which is the one that supplies their limits.
- Cluster redundancy persists. Five ingests each carry a separate edge to two-rewrites, and four carry one to human-writing-structures-transfer. The synthesis note above remains the better single inbound target for those theory notes.

## Flags

- Not a split candidate. The ingest makes one bounded assertion with organized evidence.
- Tension, unresolved: the sibling ingests treat DLT as "the human-reader mechanism", while this ingest reports DLT as a small predictor with antilocality counterexamples. Any edge from a writing-guidance note should cite this ingest for the bound.
