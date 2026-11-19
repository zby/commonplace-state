# Friction check: Incrementally constrained files defer centralized schema commitment until write invariants stabilize

**Note:** kb/notes/files-not-database.md
**Central claim (one sentence):** When shared file tooling makes authored documents cheap to inspect and revise, canonical files can defer unsettled enforcement and support rebuildable read views, while database authority is warranted for state whose write-time invariants or information cannot safely remain in those documents.

## Filter
**Verdict:** SURVIVES

The claim asks deferred enforcement, preservation of information needed by later enforcement, rebuildable read capabilities, and scoped database authority to coexist. They can: the note limits deferral to unsettled invariants, requires known invariants and future-required identity or provenance immediately, and assigns authority away from files when correctness or non-rebuildable state demands it.

## Signal — thinnest joints
1. **“Commonplace reaches the same boundary at a smaller scale: documents remain Markdown, while churning review freshness on `(note, criterion)` edges lives in SQLite because no single document owns that mutable relation.”** — UNSUPPORTED — The absence of a pre-existing single-document owner does not by itself establish that SQLite must be authoritative; the system could introduce a canonical edge document or another explicit owner, so the inference needs the additional concurrency, update, or consistency requirement that makes those alternatives unsafe or costlier.
2. **“The useful difference is the sequence in which commitments become binding. Files can add constraints only after repeated use exposes a stable pattern”** — THIN — Gradual constraint addition explains the proposed sequence but not a file-specific advantage, because the note later acknowledges that a database can also defer normalization; the missing joint is why the available file authoring surface makes revision materially easier in the stated setting.
3. **“A database earns authority when an invariant must hold at write time or when mutable state cannot be assigned safely to a single document.”** — THIN — These conditions establish a need for stronger coordination, but they do not alone establish database authority: locks, a serialized writer, or another transactional substrate might enforce the invariant while files remain canonical. The conclusion holds only with the implicit comparative premise that the database is the suitable or cheaper enforcement substrate.
4. **“Under these conditions, files provide a usable authoring surface immediately.”** — HOLDS — The stated conditions include already-shared file and Git tools and writes that tolerate weak enforcement, which directly support immediate authoring; the following editor, repository-browser, and ordinary-tool examples concretize the contingent saving rather than treating it as intrinsic to files.
5. **“The important question is not file count. It is whether the database can be discarded and rebuilt from the authored documents without losing information or violating correctness.”** — HOLDS — Rebuildability directly tests the distinction the preceding paragraph defines: a structure reconstructed without information loss or correctness failure is derived, whereas one whose removal loses necessary state or breaks correctness is authoritative.

## For the human
Look first at the move from an ownerless mutable edge to SQLite authority: name the write-time or coordination property that rules out assigning that edge its own canonical file.
