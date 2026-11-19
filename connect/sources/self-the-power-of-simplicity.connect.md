---
description: "Discovery report for possible KB connections from the Self: The Power of Simplicity snapshot"
type: kb/cache/types/connect-report.md
source: kb/sources/self-the-power-of-simplicity.md
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: SELF: The Power of Simplicity

**Source:** [SELF: The Power of Simplicity](../../../sources/self-the-power-of-simplicity.md)

## Discovery Trace

**Description listing scan:**

- Generated complete title surfaces with `rg -N --no-heading -m1 '^# '` over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` (354, 134, 172, 12, and 499 titles respectively).
- Ran `rg -n -i '^description:.*(prototype|class|instance|delegation|clone|rival|idealiz)'` across all authorised local destinations. The domain-pricing, instantiation, and boundary-preserving-rival notes were the only direct theoretical matches; agent-memory and agentic-system descriptions had no prototype/class design claim.

**Topic indexes:**

- Read the notes, reference, agent-memory, agentic-system, and sources collection heads, plus the Foundations and Computational Model tag heads. Foundations surfaced the boundary-preserving-rival test; Computational Model confirmed that the paper's relevant role is programming-language evidence rather than general agent architecture.

**Body search:**

- `rg -n -i "prototype-based|prototype based|classes versus prototypes|class-instance|class/instance|class commitment|rival paradigm|delegation|cloning|metaclass regress|meta-regress|one-of-a-kind"` across all authorised destinations found the two user-context notes and the review-disposition proposal.
- `rg -n -i "rival|prototype|class|instance"` over the three candidate notes confirmed distinct roles: domain pricing needs author-external rival evidence; instantiation needs evidence that the class commitment is optional design content; the framework-rival note limits what a rival can establish.
- `rg -n -i "SELF: The Power of Simplicity|Ungar|prototypes.*classes|classes.*prototypes"` over sources found citations in reflection papers but no existing snapshot or ingest of this paper.

**Link following:**

- Followed the domain-pricing note to the boundary-preserving-rival note. Kept both: the paper is primary evidence that an object-oriented design can deliberately drop classes, while the companion note supplies the limit that a rival demotes or contests a commitment but does not establish the adequacy of a different idealization.
- Followed the instantiation note's pricing paragraph to the existing metaobject-protocol and Erlang source ingests. Kept the MOP ingest as a source comparison because it attests a different signature—a marked interface inside class-based OO—where Self attests a rival organized around rejecting classes.
- Reflection and linguistic-symbiosis papers that merely cite Self were rejected; their subject is cross-language reflection, not the class/prototype design choice.

## Connections Found

- [Domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) -- **is-evidence-for**: Self presents itself as a new object-oriented paradigm whose defining simplification is eliminating classes and replacing the class/instance and subclass relations with prototypes, cloning, and one parent-based inheritance relation, directly attesting the note's rival-paradigm signature.
- [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) -- **is-evidence-for**: the paper makes the class/instance split explicit design content by contrasting plan-based instantiation with cloning and by showing which capabilities and organizational cues change when the split is removed.
- [A framework rule with a boundary-preserving rival is not an inherited constraint](../../../../notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) -- **is-evidence-for**: Self retains the broad object-oriented commitments to objects, message passing, inheritance, shared behavior, and exploratory programming while dropping classes, providing a worked programming-language instance of a rival that demotes a narrower rule to a design choice.
- [Metaobject Protocols: Why We Want Them and What Else They Can Do](../../../../sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md) -- **compares-with**: the MOP paper prices class change through a marked interface inside class-based OO, whereas Self prices the class commitment by constructing a rival paradigm without classes.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) → source -- **evidenced-by**: cite the authors' explicit classless object-oriented design as the primary rival-paradigm attestation, while retaining the note's warning that a rival establishes contestability rather than adequacy.
- [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) → source -- **evidenced-by**: cite the paper's class-versus-prototype table and its discussion of what classes cost and what their removal changes.
- [A framework rule with a boundary-preserving rival is not an inherited constraint](../../../../notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) → source -- **evidenced-by**: use Self as a domain example, not as evidence about Commonplace's own boundary invariants.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Repair dispositions for defeated claims](../../../../reference/proposals/repair-dispositions-for-defeated-claims.md) -- the proposal names prototype-based OO as part of the review episode, but the durable theory notes are the intended evidence consumers.
- [Inter-language Reflection](../../../../sources/gybels-et-al-2006-inter-language-reflection.ingest.md) and related Smalltalk/SOUL papers -- they cite or use prototype languages but do not analyze the class-versus-prototype commitment.
- Agent-memory and agentic-system reviews -- no candidate gained a concrete traversal benefit from a historical language-design paper; similarity to mutable agent definitions remained analogy-only.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- The user-named `kb/notes/a-domain-priced-exception-does-not-refute-an-idealization.md` is absent; the current successor is `kb/notes/domain-pricing-routes-an-exception-to-idealization-assessment.md`.
- The supplied PDF is the 1991 journal revision, which identifies itself as a substantial revision of the OOPSLA ’87 paper. Durable citations should distinguish the captured revision from the original conference version.

## Flags

None
