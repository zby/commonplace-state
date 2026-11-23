---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["First, deployment evidence arrives online and is often sparse, so candidate writes must be cheap to propose and install"]
    reason: "UNSUPPORTED — Online arrival may motivate installing lessons before a retraining cycle, but sparseness does not motivate cheapness. Sparse evidence means few candidate updates and weak signal per update. That argues for sample efficiency or for spending more per candidate, not for cheap proposal and installation. The note gives no link from sparseness to cost. The cheapness requirement also conflicts with the next sentence's regression validation, which adds cost and is expensive for parametric writes. The note does not reconcile the two requirements."
  - scope: passage
    quotes: ["because continual adaptation compounds silent degradation"]
    reason: "THIN — The 'must be validated' requirement rests on the claim that continual adaptation compounds silent degradation. The note asserts that claim and does not show it. The cited note is glossed in the footer as explaining why symbolic writes are cheap to validate and parametric writes are not. That is a claim about validation cost asymmetry, not evidence that degradation compounds or stays silent. The joint shows that validation is desirable, not that every candidate write needs regression validation."
  - scope: passage
    quotes: ["The resulting problem is governance"]
    reason: "THIN — 'Resulting' presents the four-part governance list as following from the preceding paragraphs. Earlier paragraphs derive selection, regression validation and form placement. Assigning an authority path is introduced in paragraph one only as a fact about consumption paths. Validation 'against open-ended behaviour' appears here for the first time. The note does not establish that these parts must be handled together under one function called governance, rather than by separate mechanisms. 'Authorize' in the description also leaves unclear who authorizes once the system selects for itself."
  - scope: passage
    quotes: ["Continual learning, as the field uses the term and as this note uses it, asks for more: the system does the selecting itself."]
    reason: "THIN — This sentence makes self-selection the discriminator and supports it only by appeal to how 'the field' uses the term, without evidence. It also changes what the title claim depends on: release engineering already governs behaviour-changing writes and still does not count, so governance alone does not separate continual learning from maintenance. The note does not say whether the claim is that governance is necessary, or that self-performed governance is the defining property."
  - scope: passage
    quotes: ["Persistence alone therefore does not create a governed behaviour-changing write."]
    reason: "HOLDS — The premise is that behavioural authority belongs to the consumption path, not to stored bytes, so the same object can inform or instruct. That premise supports the narrow conclusion that persistence does not settle which item shapes behaviour or with what force. The joint is close to definitional, because 'governed' is defined as more than persistence. Its weak point is the unstated alternative that retrieval or activation does the selecting. The note answers that alternative only in its final sentence and its footer."
outcome: report
---

# Friction check: Continual learning requires governing behaviour-changing writes, not just storing content

**Central claim (one sentence):** A deployed system learns continually only if its own loop selects, validates, authorizes and coordinates durable behaviour-changing writes, across whichever representational forms they touch; persisting content is not enough.

## Filter
**Filter:** SURVIVES

The claim commits to one consistent thing: the system's own evidence-responsive loop must govern its behaviour-changing writes. The properties it wants together are cheap online installation, regression validation, cross-form coordination and autonomous selection. These can coexist if validation cost depends on the form, which the linked asymmetry note suggests. The note does not state that resolution. Cheap installation and mandatory regression validation are in open tension for parametric writes. The note also gives two answers to what makes a write count as continual learning: governance in the title, self-selection in the final paragraph. Neither issue splits the claim into incompatible parts. Each one shows where the claim needs to be made concrete.

## Thinnest joints

The deployment-constraint joint ranks first because its connective ("so") joins a premise, sparseness, to a conclusion, cheapness, that the premise points away from. The regression joint ranks next because its "because" rests on an unshown empirical claim, and its citation supports a different claim. The "resulting problem is governance" joint and the self-selection joint are both thin. Each introduces or re-scopes a requirement while presenting it as a consequence of earlier argument. Together they leave unclear whether governance or self-selection is the operative condition. The persistence joint holds because the behavioural-authority premise does carry its narrow conclusion. Its closeness to a definition is what keeps it among the surfaced joints. The weights-only updater conditional ("an updater restricted to weights freezes consequential choices outside its reach") was also checked. It holds under its stated condition and was not surfaced.

## For the human
Look first at paragraph two's "sparse, so … cheap" step and its unresolved tension with mandatory regression validation. Then decide whether the title's operative condition is governance or self-selection.
