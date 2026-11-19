---
type: types/edit-result.md
outcome: changed
changes:
- 'Description: replaced ''non-regression prevents this only when'' with ''such a
  successor fails a non-regression requirement only when''.'
- 'Opening paragraph: conditioned ''Checking the current gain does not check that
  the revision mechanism survives'' on current production not exercising the revision
  mechanism.'
- Heading 'A gain can consume the mechanism that produced it' became 'A change can
  improve production while disabling the revision mechanism'.
- Heading 'When non-regression protects the revision path' became 'When closing the
  revision path fails non-regression'.
- Replaced 'the ability to revise the system's improvement machinery' with 'the ability
  to carry another revision through to use'.
- Replaced 'Preserving the path is therefore a consequence of non-regression only
  under an additional condition' with 'A successor that closes the path therefore
  fails non-regression only under an additional condition'.
removed-links: []
description: Retained changed result of kb/instructions/simplification-passes/narrow-overclaims.md
  on kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
format: 1
operation: kb/instructions/simplification-passes/narrow-overclaims.md
operation-sha256: fff83f2074936afa498432ab20d6f522624d8af329308aa5cdb1bd7f5cd99feb
note: kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
input-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/artifact/edits/bd8584ee244886a232bdf8b9/results/1f4f4de2659c460e900c977d4b1499c3/candidate.md
candidate-sha256: 878b49de3d0f2ce10f0209bb97747eac614ecf625094e4730639df90d3a7e148
observation: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/artifact/edits/bd8584ee244886a232bdf8b9/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1
launch: 1f4f4de2659c460e900c977d4b1499c3
completed-at: '2026-11-17T07:29:20Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/calls/launches/1f4f4de2659c460e900c977d4b1499c3/outputs/result.md
raw-output-sha256: a156baf367a453170e203ae5581ba90c69680cef9ed8b5230b9a32c4775387ea
---

# Report

Five scoped narrowings, six edits. No link, quoted span, must-keep claim, title or H1 changed. The kb-role relies only on the headline claim, and it is untouched.

- Description. Before: "non-regression prevents this only when the revision capability is included in the checked scope". After: "such a successor fails a non-regression requirement only when the revision capability is included in the checked scope". Bound: the body shows only that a path-closing successor fails a correctly scoped requirement. Whether that failure prevents adoption depends on enforcement, and the note does not state that.
- Opening. Before: "Checking the current gain does not check that the revision mechanism survives." After: "When current production does not exercise the revision mechanism, checking the current gain does not check that the mechanism survives." Bound: the claim holds only when the production check leaves the mechanism unexercised, as in the example. A production run that uses the mechanism would check it in part.
- First heading. Before: "A gain can consume the mechanism that produced it". After: "A change can improve production while disabling the revision mechanism". Bound: the example shows a gain and a disabled mechanism arriving in the same change. It does not show that the gain used up the mechanism or caused its loss.
- Second heading. Before: "When non-regression protects the revision path". After: "When closing the revision path fails non-regression". Bound: same as the description.
- Checked capability. Before: "the ability to revise the system's improvement machinery". After: "the ability to carry another revision through to use". Bound: the example loses the first-order revision route. It does not show second-order revision of the machinery. The new wording matches the replacement-workflow sentence later in the section.
- Consequence sentence. Before: "Preserving the path is therefore a consequence of non-regression only under an additional condition". After: "A successor that closes the path therefore fails non-regression only under an additional condition". Bound: same as the description. The must-keep sentences on each side ("A non-regression requirement protects only the capabilities included in its checked scope"; "Merely declaring non-regression on ordinary production tasks does not include it") are unchanged.

Noticed but not applied: "a successor that destroys the only applicable revision path" could read "closes" so it matches the note's other wording. It is outside the supplied scope, and the claim stays the same either way.
