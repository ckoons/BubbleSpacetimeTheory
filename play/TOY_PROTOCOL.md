# Toy Numbering Protocol

**Counter file**: `play/.next_toy`

## Rules

1. **Use the skill**: Run `/toy claim` before writing any toy. The skill reads `.next_toy`, increments it, and creates a claim file. This is the law.
2. **Monotonic**: Numbers only go up. Once allocated, never reused — even if the toy is deleted, renamed, or never built.
3. **Holes are history**: A gap in the sequence means something happened (deletion, collision fix, abandoned draft). The gap itself is the record. Don't fill it.
4. **Registry is ground truth**: `notes/BST_AC_Theorem_Registry.md` maps toy numbers to theorems. The filesystem says what exists; the registry says what it means.
5. **Specs reserve numbers**: A spec at `play/specs/toy_NNN_spec_*.md` reserves that number. The toy file gets the same number when built.
6. **Block claims**: Use `/toy claim N` when you know you need a consecutive sequence. Don't over-claim.
7. **Register**: Use `/toy register NNN "Title" X/Y` after a toy passes to log it.

## Why no reuse

Toy numbers appear in:
- BST_AC_Theorems.md (theorem references)
- BST_AC_Theorem_Registry.md (master index)
- CI_BOARD.md (task tracking)
- WorkingPaper.md (proof citations)
- Memory files (session history)
- Running notes (daily logs)
- Other toys (cross-references)

Reusing a number would make every prior reference ambiguous. The counter is cheap. Clarity isn't.

## Naming

`play/toy_NNN_short_description.py`

Keep descriptions to 2-4 words, lowercase, underscores. Examples:
- `toy_476_fusion_from_five_integers.py`
- `toy_474_linearized_trace.py`
- `toy_471_ci_clock_perception.py`

## Claim files

Every allocation creates a claim file at `play/.claims/toy_NNN_<CI>.claim`. These are permanent records of who claimed what and when.

## Collision history

Numbers 466-470 had collisions when multiple CIs allocated simultaneously before the claim protocol existed. Numbers 543-548 had collisions on March 28, 2026 (Lyra/Elie concurrent session). Fixed by renaming Elie's to 551-556. The `/toy` skill prevents recurrence.
