---
note_path: kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md
model_partition: claude-opus-4.8
---

# Fix report: abstract-an-experience-only-when-you-can-state-the-boundary

Three WARN findings from the full-gate review (jobs 4862, 4865) addressed with minimal edits. No claims or structure changed; fixes touch attribution and accuracy only.

| Gate | Strategy | Fix | Status |
|---|---|---|---|
| `accessibility/unidentified-references` | source residue → unframed reference | Glossed SkillRL, Reflexion, VOYAGER by kind on first mention; SkillRL also linked to its source snapshot | fixed |
| `accessibility/undefined-terms` | grounding → definition link | Added a `./definitions/distillation.md` definition link alongside the existing sibling-note link on first formal use of "distillation" | fixed |
| `prose/orphan-references` | grounding → unsourced addition | Replaced the unquantified "the cost of uniform compression is measurable" tail with a direct SkillRL citation; the 15.3% headline figure is SkillRL-vs-baselines, not an asymmetric-vs-uniform ablation, so no number was attached to the comparison | fixed |

## Warning-to-fix detail

- **unidentified-references** — SkillRL → "[SkillRL](../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.md) — a skill-augmented RL framework that preserves successful trajectories as demonstrations while synthesizing failures into concise lessons"; Reflexion → "an agent framework that retries tasks guided by verbal self-reflection"; VOYAGER → "an LLM agent that builds a reusable skill library". Glosses grounded in the SkillRL source snapshot and the established Reflexion/VOYAGER literature; none fabricated.
- **undefined-terms** — first formal use now reads "[distillation](./definitions/distillation.md) [transforms a single trace into a rule ...](./distillation-is-transformation-not-selection.md)", giving the "go deep" definition link the gate required without dropping the existing claim link.
- **orphan-references** — softened the measurability promise the note then withheld; added SkillRL to the Sources list as the direct citation behind the success/failure asymmetry.

## Deferred

- None.

## New patterns

- None outside the existing taxonomy.
