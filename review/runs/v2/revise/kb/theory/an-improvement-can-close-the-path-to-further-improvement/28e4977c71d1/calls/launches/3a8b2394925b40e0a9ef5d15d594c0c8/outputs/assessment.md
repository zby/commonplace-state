# Assessment: An improvement can close the path to further improvement

**Proposed purpose (the operator named none):** An agent or maintainer who designs or approves self-revising KB and agent workflows should notice that a check of a production gain does not show that the revision path survives. They should also know what a non-regression check must cover before it counts against losing that path.

## What reads well

The hypothetical agent makes the failure concrete in three sentences. The section "Remaining able to improve is not improving again" cleanly blocks the opposite misreading.

## Ranked changes

1. **Narrow the sufficiency language around non-regression, and fix what the checked capability is.** Cost: four to five scoped sentence edits. Pass: `narrow-overclaims`.
   - The description says non-regression "prevents this". The heading says "When non-regression protects the revision path". The body says "Preserving the path is therefore a consequence of non-regression". Together these present scope inclusion as enough to protect the path. The body supports only a smaller claim: a path-closing successor *fails* a correctly scoped requirement. Report-2 (critique) shows the gap: a check that runs after installation records the loss but does not prevent it. Report-3 (premise decomposition) shows a second gap: a scoped check can miss a latent break. Both reports call this a local dent. The critique's own repair option is to say "the successor fails the requirement", which is a narrowing.
   - "the ability to revise the system's improvement machinery" names a second-order capability. The example loses the first-order one: carrying another instruction change through to use (finding-5; report-1's THIN joint). The narrower reading is the one the example, "the only applicable revision path" and the parent's "operative path for factory development" support. Narrowing to it repairs the joint between the example and the remedy.
   - The opening's "Checking the current gain does not check that the revision mechanism survives" is stated universally. It fails when production performance itself exercises the revision mechanism (report-3). It needs the decoupling condition that the example supplies.
   - The heading "A gain can consume the mechanism that produced it" claims a causal coupling that the example does not show and the next paragraph denies (finding-4; report-1's THIN joint). "Disable" states only what is supported.
2. **Remove the local recaps and state the files-versus-capability boundary once.** Cost: one structural pass over a short note. Pass: `readability-and-flow`.
   - Finding-3 flags two passages that restate earlier text: the "no contradiction" paragraph and the Scope bullet on another applicable path. The "therefore" sentence will already have been narrowed in change 1; fold whatever is left of it into the preceding paragraph.
   - Report-4 (synthesis), opportunity 2: one boundary is spread over three places. They are the maintainer-editable-files paragraph, the replacement paragraph and two Scope bullets. Keep three distinct meanings: (a) surviving files do not show a surviving capability; (b) a replacement mechanism can preserve the capability; (c) loss is relative to the declared system boundary. Keep the handoff to the repeatable-operative-path note.
   - Report-4, opportunity 1: the opening should carry the checked-scope condition as well as the failure, in conditional form.
   - Finding-6: the opening frames the lost mechanism as needed to "select or install" later revisions. The body defines the path as running from evidence to later use. Match the body.
   - Finding-7: "can miss its failure" attaches to the nearest antecedent, the comparison. Name the referent, the revision path.

## The sentence a hostile reviewer attacks first

"If that scope includes the ability to revise the system's improvement machinery, a successor that destroys the only applicable revision path fails the requirement even if its production performance improves." It names a different capability from the one the example loses. Its section heading also turns "fails the requirement" into "protects".

## Overclaims: support or divergence

- Support, may be narrowed: the description's "non-regression prevents this"; the heading "When non-regression protects the revision path"; "Preserving the path is therefore a consequence of non-regression only under an additional condition"; "Checking the current gain does not check that the revision mechanism survives"; the heading "A gain can consume the mechanism that produced it".
- Divergence, must be kept (listed in the plan's `must-keep`): the headline possibility claim, which `kb/theory/README.md` relies on; "A non-regression requirement protects only the capabilities included in its checked scope"; "Merely declaring non-regression on ordinary production tasks does not include it"; the claim that kept files do not preserve the capability if the successor no longer permits or consumes their changes; the claim that preserving the path does not establish that another improvement will occur; the fixed-deployment scope bullet.

## Stale qualifications: questions for the operator

- The supplement line cites "the preserved-capability consequence" of the better-factory comparison. The parent note calls it "the preserved-path consequence" (its Scope, line 49) and states it in its non-regression paragraph. Should the label match the parent? Settle this before glossing the line (see finding-1 below). Apply it as its own commit.

## Claim questions the passes cannot settle

The narrowing in change 1 answers the depth 1 reports without adding a claim. The reports also propose new content, which the passes cannot add. The operator decides whether to add it in a rewrite:

- the adoption condition: a scoped check prevents closure only when it gates installation (report-2);
- the form a check can take before installation, such as a trial revision run in staging or an argument from a specified transition mechanism (report-2);
- the alternative safeguard of keeping the revision machinery outside the surface the successor can edit (report-2, secondary).

None of these proposals splits, merges or rejects the note, and none changes its central claim. The role report shows that no dependent argues from the non-regression section, so the narrowing reaches no dependent.

## Findings not acted on

- `frontmatter/claim-strength` (finding-2): it proposes sharpening the title away from the bare possibility claim. The role report says `kb/theory/README.md` paraphrases the headline claim, so a title change reaches that dependent. The possibility claim is also kept as divergence, and report-4 says the title may stay. This is the operator's decision, not a pass.
- `accessibility/undefined-terms` (finding-1): the gloss for the supplement line depends on the stale-label question above. Settle the label first, then add the gloss in the same commit.
- `marginal-value-redundancy`, info item on the maintainer Scope bullet: keep it. It carries the declared-boundary meaning (c) above. It is folded only as part of change 2.

## Passes not recommended

`abstractions`, `plain-wording` and `opening-and-title`: once changes 1 and 2 land, no remaining item has clear value against the purpose.
