---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/fast-properties-in-v8.md"
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: Fast properties in V8

**Source:** [Fast properties in V8](../../../sources/fast-properties-in-v8.md)

## Discovery Trace

**Description listing scan:**

- Generated fresh complete title listings with `rg -N --no-heading -m1 '^# '` over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` (354, 134, 172, 12, and 497 headings respectively).
- Scanned scoped descriptions with `rg -n -i '^description:.*(deopt|hidden class|object shape|shape mutation|inline cache|megamorphic|monomorphic|polymorphic|runtime charge|compiled|specializ)'` over all five authorised destination collections. The two retained theory notes were the only note-level matches whose claims directly consume V8's runtime behavior.

**Topic indexes:**

- Read `kb/notes/tags-README.md`; the computational-model and failure-modes routes frame the two retained note candidates.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. No reference, agent-memory, or agentic-system entry needs V8 object-layout evidence to support its own claim.

**Body search:**

- `rg -n -i 'deoptimi|hiddenclass|hidden class|object shape|shape mutation|inline cache|megamorphic|monomorphic|type pollution|slow propert|dictionary propert|compiled code.*special|specialized.*shape|runtime charge'` over all authorised destinations found direct matches in [Domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) and [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md).
- The same search found no matches in `kb/agent-memory-systems/` or `kb/agentic-systems/`. Reference hits were an implementation proposal repeating the note's pricing example and an ADR with unrelated uses of “specialized.”
- Source-ingest hits were false positives about an agent runtime's process shape. Focused source follow-up instead retained the user-requested [Maps (Hidden Classes) in V8](../../../sources/maps-hidden-classes-in-v8.md) companion and the earlier [Metaobject Protocols ingest](../../../../sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md), which attest different pricing signatures for the same local idealization argument.

**Link following:**

- Followed both direct theory notes through their current idealization and class/instance arguments. The V8 source contributes only runtime-pricing evidence: Map/HiddenClass changes alter the specialization key; repeated property churn can force dictionary properties where ICs do not work; and the companion demonstrates dependent optimized code being marked for deoptimization.
- Followed the source's inline-cache and type-pollution references only to identify its evidential boundary. The captured V8 pages mention IC dependence and type pollution but do not themselves describe monomorphic-to-megamorphic state transitions, so no megamorphic claim is retained as directly evidenced.

## Connections Found

- [Domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) -- **is-evidence-for**: V8 imposes concrete optimization costs when object layout stops matching the stable shape on which ICs and compiled property access depend, providing primary runtime-charge evidence that predates the local pricing claim.
- [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) -- **is-evidence-for**: V8's Maps make the “compiled code specialized on the old shape” mechanism concrete, while dictionary-mode properties and the companion deoptimization trace show the runtime consequences of violating that specialization.
- [Maps (Hidden Classes) in V8](../../../sources/maps-hidden-classes-in-v8.md) -- **see-also**: the companion expands the main article's Map-transition account and prints the direct `field-const` deoptimization trace needed for the strongest runtime-charge claim.
- [Metaobject Protocols ingest](../../../../sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md) -- **compares-with**: the MOP paper attests a marked-interface price, whereas the V8 sources attest an independent optimizer/runtime price for shape instability.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) → source -- **evidenced-by**: cite the official V8 implementation account for the runtime-charge signature, with the companion supplying direct deoptimization output.
- [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) → source -- **evidenced-by**: cite the Map/HiddenClass, IC, slow-property, and type-pollution mechanisms behind its statement that runtimes charge for changing shapes on which compiled code specializes.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- `kb/reference/proposals/repair-dispositions-for-defeated-claims.md` -- rejected because the implementation proposal should inherit this source through the canonical theory note instead of acquiring a redundant `see-also` edge.
- `kb/reference/adr/023-quote-anchored-citations-for-code-grounded-reviews.md` -- rejected as a lexical match on specialization with no object-layout or runtime-charge connection.
- `kb/sources/spacedriveapp-spacebot-ai-agent.ingest.md` -- rejected because its “runtime shape” means a process-role topology, not object shape or compiler specialization.
- Agent-memory and agentic-system collections -- no candidates; their reflective or self-modifying systems do not rely on V8 layout behavior for their current claims.

## Index Membership

None

## Synthesis Opportunities

None. The two direct theory notes already name the tooling/runtime-charge signature and apply it to the class/instance idealization.

## Maintenance Observations

None

## Flags

- The two captured V8 pages directly support HiddenClass transitions, IC dependence, dictionary-mode slow paths, type pollution, and deoptimization. They do not directly document megamorphic IC states or thresholds; any such claim needs another source.
