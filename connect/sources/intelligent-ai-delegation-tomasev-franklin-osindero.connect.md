---
description: "Discovery report for possible KB connections from Intelligent AI Delegation"
type: kb/cache/types/connect-report.md
source: "kb/sources/intelligent-ai-delegation-tomasev-franklin-osindero.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: Intelligent AI Delegation

**Source:** [Intelligent AI Delegation](../../../sources/intelligent-ai-delegation-tomasev-franklin-osindero.md)

## Discovery Trace

**Collection rules:** Read `kb/sources/COLLECTION.md`. The immutable snapshot cannot carry authored links; its matching ingest report is the active outbound surface. Authorised local destinations are notes, reference, agent-memory systems, agentic systems, and other sources. Work and instructions are excluded. External prospecting was skipped because the collection reserves it for already-known targets, and the source URL is already captured.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The notes head routed the paper to bounded-context orchestration, verification, and coordination guarantees. The agentic-systems head exposed Autogenesis as a code-grounded implementation comparison. The reference head produced no source-specific Commonplace-system target. The agent-memory head exposed Tracecraft, but its memory/coordination review is not a task-decomposition account.
- The source carries no `tags`, so no tag-README or by-tag description scan applied.

**Full title and description listings:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over notes, reference, agent-memory systems, agentic systems, and sources. The fresh title surfaces contained 355, 136, 173, 12, and 534 headings respectively.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over all five destinations. A focused second pass with `rg -i 'decompos|delegat|orchestrat|verif|oracle|coordination|privilege|authority|accountab|liabil'` retained the decomposition, verification, governance, and empirical multi-agent candidates evaluated below.

**Body search:**

- `rg -n -i 'decompos|sub-?tasks?|delegat|task allocat|task assign' kb/notes/ --glob '*.md'` -- kept the bounded-context decomposition, fixed-decomposition, and transfer-warrant notes; rejected generic uses of “decomposition” that named document or architecture partitioning without delegated task boundaries.
- `rg -n -i 'verif|oracle|contract-first|accountab|liabil|authority|permission|privilege|reversib|subjectiv' kb/notes/ --glob '*.md'` -- kept typed-target verification, privilege quarantine, aggregate authority, and the automation boundary; rejected broader oracle notes already represented by stronger direct connections in the ingest.
- `rg -n -i 'bounded context|coordination|orchestrat|integration (cost|burden)|seams?' kb/notes/ --glob '*.md'` -- kept the topology/isolation/verification tension and coordination-guarantee neighborhood.
- `rg -n -i 'decompos|delegat|verif|accountab|liabil|permission|privilege|orchestrat|coordination' kb/<destination>/ --glob '*.md'` over reference, agent-memory systems, agentic systems, and sources -- no reference target passed the articulation test; Tracecraft was rejected as a memory/coordination implementation rather than a decomposition theory; Autogenesis and four source comparisons survived.
- `rg -n 'intelligent-ai-delegation-tomasev-franklin-osindero|2602\.11865|Intelligent AI Delegation|2604\.00389' kb/ --glob '*.md'` -- found two note-level direct external citations and one source-to-source local link, but no note links to the local snapshot or ingest.
- `rg -n -i 'total (verification|assurance)|verification (cost|budget|burden)|leaf (check|verif)|integration (check|verif)|merge (cost|verif)|accountability.*decompos|decompos.*accountability' kb/notes/ --glob '*.md'` -- found the component costs but no existing note that combines them into total assurance load.

**Link following:**

- Followed [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) to the bounded-context model, verification boundary, and topology/isolation/verification note. This showed that the source's verifiability objective is already integrated, while its recursive rule remains conditional on interface and merge costs.
- Followed [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) to the orchestration design-space and privilege-boundary neighborhood. The accountability-vacuum and liability-firebreak contribution is already integrated; permission attenuation and aggregate authority remain unconnected tensions.
- Followed [Verification needs a typed target before it needs an oracle](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md) through oracle domain and automation-boundary notes. This exposed a missing prerequisite in “contract-first decomposition”: a contract must identify the output class and asserted property before a verifier can have a reusable domain.
- Followed the empirical source cluster through [MAKER](../../../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md), [Structured Test-Time Scaling](../../../../sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md), [Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md), and [DeLM](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md). Together they bracket the paper's conceptual rule with a hard-oracle success case, an isolation-prerequisite theory, task-contingent negative evidence, and a measured verifier ablation inside a fixed decomposition.

## Connections Found

- [Verification needs a typed target before it needs an oracle](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md) -- **compares-with**: “contract-first decomposition” assumes that precise verification can govern a subtask boundary; the note separates the prior task-contract question—what typed output and property are being checked—from the later oracle-strength question.
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) -- **compares-with**: the paper moves directly from recursive decomposition to verifiability, whereas the note tests whether isolation is an intervening prerequisite and whether good decomposition merely makes both possible.
- [Agent orchestration needs a privilege quarantine, not just a permission scope](../../../../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md) -- **compares-with**: the paper proposes privilege attenuation and just-in-time scoped permissions; the note explains why content-provenance attacks require separating the untrusted reader from the privileged actor, not merely shrinking the reader's tool set.
- [Compiling a coordination strategy preserves primitive authority but expands aggregate authority](../../../../notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md) -- **compares-with**: the paper scopes delegated permissions by resource and duration but does not bound the cumulative effect volume a long-running delegation chain can produce; the note identifies that aggregate-authority gap.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- **rests-on**: treating the paper's eleven task axes and contract-first rule as reusable decomposition guidance requires recording which task forces justify each boundary; the paper supplies rationale but no use evidence that establishes transfer.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- **compares-with**: the paper specifies adaptive decomposition, verifiable completion, permission handling, and accountability as one delegation framework, while current Autogenesis leaves decomposition and review prompt-guided and exposes permission modes without a hard semantic reviewer gate.
- [Solving a Million-Step LLM Task with Zero Errors](../../../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) -- **compares-with**: MAKER is the empirical hard-oracle endpoint where maximal decomposition works because every leaf has a deterministic check and negligible cross-leaf interaction; it demonstrates the favorable boundary of the paper's rule rather than its generality.
- [Structured Test-Time Scaling](../../../../sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md) -- **compares-with**: Tu supplies the missing topology → isolation → verification dependency and therefore a stricter account of when decomposition creates checkable units.
- [Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) -- **compares-with**: controlled results show that multi-agent benefit depends on task decomposability, verifier-bearing topology, and coordination overhead, directly bounding the paper's otherwise untested recursive-decomposition prescription.
- [Decentralized Multi-Agent Systems with Shared Context](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md) -- **compares-with**: DeLM measures a verification-gated decomposition in operation, including a 60.1% to 55.2% no-verification ablation, while leaving its queue, hierarchy, and task partition fixed; it supplies partial empirical support without validating the chosen decomposition.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) → [source snapshot](../../../sources/intelligent-ai-delegation-tomasev-franklin-osindero.md) -- **evidenced-by**: the note already derives its verifiability-aware boundary rule from this paper, but cites an external URL rather than the captured source.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) → [source snapshot](../../../sources/intelligent-ai-delegation-tomasev-franklin-osindero.md) -- **evidenced-by**: the note already imports the accountability-vacuum and liability-firebreak vocabulary through a direct external link; the local snapshot is the captured evidence artifact.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → [source snapshot](../../../sources/intelligent-ai-delegation-tomasev-franklin-osindero.md) -- **evidenced-by**: the paper independently applies verification cost to delegation depth, oversight, and delegatee choice, adding an agent-delegation domain to the note's convergence argument while remaining conceptual rather than empirical evidence.
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) → [source snapshot](../../../sources/intelligent-ai-delegation-tomasev-franklin-osindero.md) -- **evidenced-by**: the paper bears directly on the note's simpler rival account by asserting that finer decomposition can make verification tractable while leaving isolation unstated.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- the ingest already records the four verification mechanisms against this spectrum; another candidate edge would repeat an authored connection without adding a new reader need.
- [Review automation should target verifiable subroles before reviewer identity](../../../../notes/verifiable-subroles-before-reviewer-identity.md) -- the review-role application shares the “split toward checkable work” pattern, but the delegation paper adds no review-specific mechanism or evidence beyond the general verification-boundary connection.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- the paper's framework is consistent with explicit scheduler control surfaces, but it proposes no implementation whose structure could evidence the note; the decomposition and coordination connections carry the useful signal more directly.
- [Tracecraft](../../../../agent-memory-systems/reviews/tracecraft.md) -- its task claims, messages, and shared JSON state expose coordination-guarantee gaps, but the review does not implement or analyze contract-first task decomposition, authority transfer, or liability.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) -- “contract” and decomposition rationale overlap lexically, but the paper does not describe the shipped Commonplace rationale system and no source-to-reference `see-also` edge would improve system-documentation traversal.

## Index Membership

None. The source belongs in the sources collection, whose README does not enumerate individual ingests; it is a conceptual framework rather than a code-inspected agentic-system entry.

## Synthesis Opportunities

- **Decomposition should minimize total assurance load, not merely leaf verification cost.** The paper contributes leaf checkability and liability; the bounded-context heuristics add context fit, interface preservation, merge cost, and orchestration overhead; the empirical source cluster shows that those terms can reverse the value of further splitting. The resulting objective includes leaf checks, cross-boundary integration checks, coordination cost, and accountable ownership. “Recursively split any hard-to-verify task” is valid only when this total falls.
- **Task descriptors and orchestration axes occupy different levels of one selection model.** The paper's eleven axes describe the incoming task (complexity, criticality, uncertainty, duration, cost, resources, constraints, verifiability, reversibility, contextuality, subjectivity). The KB's orchestration design-space axes describe the strategy selected for it (scheduler placement, decomposition-policy form, persistence, coordination form and guarantee, return artifact). Treating the first vector as input to `select(K)` and the second as its strategy choice avoids conflating task properties with architecture properties.

## Maintenance Observations

- [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) cites the same author/title combination at `2604.00389`, while the snapshot, ingest, and coordination-guarantees note use `2602.11865`. The identifier should be verified before that citation is normalized to the local captured source.
- The two notes that already depend directly on the paper use external arXiv links rather than the local snapshot or ingest. Local backlink search therefore understates how far the source has already entered the theory graph.
- The ingest's existing `Connections Found` prose uses `grounds`, `exemplifies`, and `extends` for source-to-note relationships. Those labels are not in the current sources-collection authorised set; a future edit should express the commitments with `is-evidence-for`, `compares-with`, `rests-on`, or another authorised source label.

## Flags

- **Conceptual-evidence limit:** the paper contains no implementation, ablation, or observed delegation chain. Use it as design rationale and independent conceptual convergence, not as evidence that recursive decomposition improves outcomes.
- **Tension:** further decomposition does not monotonically improve verifiability. It can erase global interactions, multiply seams, increase merge checks, and diffuse accountability; irreducibly subjective residue may need high-trust or human handling rather than another split.
- **Split candidate for downstream theory extraction:** the source independently contributes at least two transferable claims across three clusters—total-assurance decomposition, and accountability/authority in delegation chains. The immutable source should not be split, but future note work should not force both claims into one note.
