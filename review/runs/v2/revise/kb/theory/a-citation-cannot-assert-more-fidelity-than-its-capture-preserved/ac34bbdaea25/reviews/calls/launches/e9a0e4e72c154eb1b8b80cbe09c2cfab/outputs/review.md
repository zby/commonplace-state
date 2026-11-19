---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

## Summary

The main claim, stated in the title, description and opening paragraph, is that a citation's fidelity is fixed by the capture layer holding the passage. It cannot rise downstream through notation; only re-capture raises it. Every side section either supplies a premise for this claim or bounds it. No branch needs removal, demotion or rehoming.

## Side material checked

- **Fidelity versus authority.** This paragraph separates the claim from the linked complementary note about authority earned per operation. Without it, a reader could take the note as contradicting that note. It is a trust-building contrast that bounds the claim, so it stays.
- **Forced layering.** The context-window and copyright constraints are the premise that capture of long sources must be lossy and layered. The aside on provider output filters is one clause. It marks the filters as provider-contingent rather than inherited, so it limits the premise rather than adding a new claim.
- **Why notation cannot repair it.** This section is the core argument for the non-increasing step. The follow-on paragraph on "history has one chance" is two sentences. It places the claim under a general rule without arguing a separate thesis.
- **Locator corollary.** This is the strongest candidate for a branch, because it makes a design claim about span locators. But it follows directly from the main claim and makes that claim concrete: two spans at the same offset can differ by a full layer. The Scope section relies on it to state where the bound goes vacuous. It applies the main claim without competing with it, and it is short.
- **Scope and practical consequence.** These set the boundary condition (lossless short sources) and state what the claim changes in practice (decide provenance quality at ingest). Both strengthen the claim.
- **Open Questions.** The two questions, about transcript grain and about fidelity versus usefulness, are the kind of side ideas this gate would otherwise flag. They are already demoted to open questions, which is the correct destination.
- **Evidence footer.** The ADR 046 audit figures support the claim that naive `verbatim` marking fails.
