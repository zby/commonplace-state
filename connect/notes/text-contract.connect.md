---
description: "Discovery report for possible KB connections from the text-contract definition"
type: kb/cache/types/connect-report.md
source: "kb/notes/definitions/text-contract.md"
source_has_frontmatter: true
date: "2026-08-22"
depth: standard
---

# Connection Report: Text contract

**Source:** [Text contract](../../../notes/definitions/text-contract.md)

## Discovery Trace

**Description and title listing scan:**

- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`; the full title surface was too broad to discriminate candidates, so discovery narrowed through the source's `document-system` tag and the contract/profile vocabulary below.
- Ran `rg -l '^tags:.*document-system' kb/notes --glob '*.md'`; the strongest candidates were [artifact classification](../../../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md), [directory placement](../../../../notes/directory-placement-is-total-frontmatter-classification-is-partial.md), [universal taxonomies as defaults](../../../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md), and [technical constraints as objective-choice engineering](../../../../notes/technical-constraints-make-kb-objective-choice-engineering.md).

**Topic indexes:**

- Read [top-level tag navigation](../../../../tags/README.md) and [document-system](../../../../tags/document-system-README.md). The definition carries `document-system` but is not in that curated head.
- Read the collection/navigation heads for notes, reference, instructions, types, sources, agent-memory-systems, and agentic-systems to check whether another collection already owns the invariant vocabulary. The reference catalogue owns shipped profile state; each collection contract owns its binding local clauses; no other cheap library artifact cleanly owns the invariant distinction between a text contract and a profile.

**Body search:**

- Ran `rg -n -i "text contract|communicative profile|collection contract|quality goal|title conventions|link grammar" kb/notes --glob '*.md'` and the equivalent search over `kb/reference/`. These surfaced the classifier, objective-choice note, directory-placement note, universal-taxonomy note, ADR 042, the profile catalogue, and the collection/type-boundary reference note.
- Ran `rg -n -i "text contract|communicative profile|collection contract" kb/instructions kb/types kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`. Most matches used the broader ordinary phrase “collection contract”; the six direct links from live `COLLECTION.md` files were the relevant consumers of this definition.
- Ran `rg -o -n "\\]\\([^)]*text-contract\\.md(?:#[^)]*)?\\)" kb AGENTS.md --glob '*.md'`. It found 30 direct Markdown links in 22 files: six live collection contracts, seven current theory/navigation artifacts, four current reference documents, three historical ADRs, one archived proposal, and one workshop.

**Link following:**

- Followed [artifact classification](../../../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md): it uses only the profile distinction and now owns the separation from content kind, production lineage, and authority.
- Followed [ADR 042](../../../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) and [the profile catalogue](../../../../reference/collection-prototypes.md): ADR 042 explicitly assigns invariant theory to the definition and changing shipped-system state to the catalogue, but the current definition repeats the default table, current collection mapping, promotion history, maintenance discussion, and link-grammar detail.
- Followed [the collection/type split](../../../../reference/collections-never-own-frontmatter-semantics.md) and [directory placement](../../../../notes/directory-placement-is-total-frontmatter-classification-is-partial.md): together they develop the definition's terse “not type” boundary and explain how clauses distribute across path and frontmatter surfaces.
- Inspected history with `git log --follow`, `git show 1ac2171dd38d2cc0e661e348ae546cfc2d8fbd31`, and `git show 7eb616d584d86bbc3a5f6198a888a3c8aa2189d2`. The current path was added on 2026-07-09 as the intended rename/revision of the older `register` definition; that predecessor first appeared on 2026-04-12.

## Connections Found

- [A universal knowledge framework demotes content taxonomies to defaults](../../../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — **grounds**: the definition states that profiles form an open, worked-case-guarded set; this note supplies the transferable argument for retaining useful closed taxonomies as defaults while guarding shared-catalogue growth.

- [Directory placement is total, frontmatter classification is partial](../../../../notes/directory-placement-is-total-frontmatter-classification-is-partial.md) — **extends**: the definition distinguishes text contract from type and says collection placement is a design choice; this note develops the mechanism that makes path a total selector for subtree-wide contract clauses while leaving type-owned frontmatter semantics separate.

- [The collection–type split is asymmetric: collections never own frontmatter semantics](../../../../reference/collections-never-own-frontmatter-semantics.md) — **see-also**: the definition's “text contract is not type” exclusion has a concrete shipped-system consequence here: `COLLECTION.md` owns text-level features while type specs remain self-contained owners of frontmatter semantics.

## Bidirectional Candidates

None. The strongest targets already link to the definition where the return path helps their readers.

## Reverse-edge Candidates

None beyond the curated index candidate below. Six live collection contracts and the main profile/classification artifacts already link directly to the source.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Artifact classification separates profile, content kind, lineage, and authority](../../../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md) — already linked from the source and already uses the definition at its first profile occurrence; no additional edge is needed.
- [Technical constraints make KB objective choice engineering](../../../../notes/technical-constraints-make-kb-objective-choice-engineering.md) — already links to the definition three times and is already linked from the definition through the “pre-packaged objective function” passage.
- [Text contract profiles](../../../../reference/collection-prototypes.md) — already linked in both directions. Its overlap with the definition is an ownership problem, not a missing connection.
- [Links encode conditional possibilities, not obligations](../../../../notes/links-encode-conditional-possibilities-not-obligations.md) — its links still gloss the target as a closed three-register taxonomy. That is stale terminology to repair, not a new connection.

## Index Membership

- [Document system](../../../../tags/document-system-README.md) — the definition carries the `document-system` tag and supplies the collection-level writing-contract concept used across six live collection contracts; it belongs in the curated foundations or writing-conventions section if retained as a separate definition.

## Synthesis Opportunities

None. The higher-order distinction between communicative profile, content kind, lineage, and authority is already captured by the artifact-classification note.

## Maintenance Observations

- The vocabulary has real reuse, but the current artifact is not cheap or focused: the 60-line definition repeats the concise `AGENTS.md` glossary entry, the current profile catalogue, ADR 042's history and promotion rationale, and clauses whose authoritative homes are the individual `COLLECTION.md` files. This conflicts with ADR 042's explicit decision to keep invariant definition separate from system state that stales on another schedule.
- The economically justified residue is small: a canonical distinction between **text contract** (the binding local declaration) and **profile** (a reusable, non-authoritative bundle), plus its exclusions from type, content kind, lineage, and behavioral authority. The definition type contract supports a separate note when a term is cross-workflow, plausibly misused, and benefits from a cheap canonical gloss; all three tests apply, but the present note fails the “cheap and focused” part.
- Deleting the definition outright would require retargeting 30 direct links. Collection contracts and current-system documents could mostly target the profile catalogue or carry an inline gloss; historical ADRs could target ADR 042; theory notes would need the classifier or universal-taxonomy note. That migration would make the changing catalogue the likely vocabulary authority, contrary to ADR 042's intended separation.
- [The profile catalogue](../../../../reference/collection-prototypes.md) still says profile membership itself determines a theory → prescription → description maintenance direction. The current definition and classifier now say propagation follows actual lineage/dependency and consumption paths. Those surfaces contradict one another.
- [Link vocabulary](../../../../reference/link-vocabulary.md) and [links encode conditional possibilities](../../../../notes/links-encode-conditional-possibilities-not-obligations.md) still describe the target as “register,” one of three exhaustive content modes. ADR 042 says that terminology and closed-set meaning were retired.
- Two existing footer labels in the source are outside `kb/notes/COLLECTION.md`'s authorised sets: `part-of` for the reference catalogue and `co-equal mechanism` for `constraining`. These authored edges need relabelling or removal during any revision.
- Git history distinguishes the file from the concept. Commit `1ac2171dd38d2cc0e661e348ae546cfc2d8fbd31` (`Adopt open-ended text contracts: retire register, add ADR 042`, 2026-07-09) added the current path as an intended rename and conceptual revision. Commit `7eb616d584d86bbc3a5f6198a888a3c8aa2189d2` (`Phase 4: optimize skills and strip universal mechanics from COLLECTION.md`, 2026-04-12) first added its predecessor, `kb/notes/definitions/register.md`.

## Flags

- Recommended disposition: retain the separate definition only as a sharply reduced canonical gloss; move or delete current-system tables, mappings, promotion history, maintenance policy, and link-grammar exposition. The evidence supports keeping the vocabulary target, not keeping the present multi-purpose note.
