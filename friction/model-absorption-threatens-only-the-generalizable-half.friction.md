# Friction check: Model absorption threatens only the generalizable half of a retention layer

**Note:** kb/notes/model-absorption-threatens-only-the-generalizable-half.md
**Central claim (one sentence):** Model improvement can eventually make externally retained generalizable content redundant, but cannot make externally retained current local state redundant because that state must remain current and authoritative for a particular deployment.

## Filter
**Verdict:** DISSOLVES
The note cannot hold together its operational definition of absorption (the model can supply the content unaided), its categorical claim that a stronger model can never supply local state unaided, and its concession that deployment-local continual training can put some local state into the model. Currency and authority explain why an explicit record may remain necessary after the model can supply the content, but that establishes non-redundancy of the record, not non-absorbability of the content; the note switches between those claims without choosing one.

## Signal — thinnest joints
1. **“A stronger model can supply it unaided: eventually [for generalizable content], never [for current local state]”** — UNSUPPORTED — Indexicality alone does not prevent a model from reproducing deployment-specific content that entered a deployment-local or public training stream; the later continual-training concession directly supplies such a channel.
2. **“A model trained on everything ever written still cannot regenerate which option a team picked, because nothing entails it.”** — UNSUPPORTED — A prior description of the live options does not entail the choice, but a later written record can report it; non-derivability from pre-decision evidence does not establish absence from every possible training corpus.
3. **“Successfully absorbing a commitment would destroy the properties that made it usable as one, so absorption here would be a loss rather than a saving.”** — THIN — Copying a commitment into weights does not destroy the citable, contestable source if that source remains; only replacing the explicit record with parametric recall loses those handles, so the reason supports a claim about substitution rather than absorption itself.
4. **“The training distribution samples the same facts from other sources … Its value therefore runs on a clock, and the honest accounting is amortization.”** — THIN — Availability somewhere in model capability does not by itself establish reliable unaided supply in the deployment’s bounded context, and the note’s own scope retains retrieval, placement, and framing value after absorption; an additional criterion is needed for when redundancy actually starts.
5. **“Those distinctions are real, but they cross-cut absorbability rather than refine it. … Absorption asks only the second.”** — THIN — Showing that functional categories cross-cut indexicality does not establish that indexicality exhausts absorbability; rarity, observability, update latency, and required fidelity can still divide content with the same indexical status.

## For the human
Look first at whether the thesis is about content becoming reproducible by a model or about an external record becoming dispensable; the continual-training case makes those two claims come apart.
