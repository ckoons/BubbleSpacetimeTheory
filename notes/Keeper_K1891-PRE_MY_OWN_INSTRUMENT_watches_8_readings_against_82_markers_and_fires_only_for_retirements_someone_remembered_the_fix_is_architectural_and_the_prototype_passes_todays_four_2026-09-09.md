# K1891-PRE — my own start-of-day instrument is the same failure it exists to catch, one level up

**Keeper, 2026-09-09 (Wednesday) 12:46 EDT, clock-verified.** Prototype retained: `notes/Keeper_K1891-PRE_instrument_derived_retirement_inventory_replaces_the_hand_list_2026-09-09.py`.

## 1. The own, precisely
Everything found today was a correct ruling nobody carried forward. I have a start-of-day instrument whose job is exactly that, and it printed this at 09:15 this morning, in this session:

```
[REVIEW] retirement  35 DISTINCT board line(s) pair a RETIRED reading with 'bank' across 163 files
         ->DIRECTIVE Keeper owns the fix.
```

**I read it, noted it, and moved on to the priorities file — and then spent four hours finding by hand what it was pointing at.** The directive naming me is in the instrument's own output.

## 2. Why it could not have helped, which is worse than my ignoring it
The check scans a **hand-maintained list of eight retired readings**: A²=rank, Wyler alpha, 2/√79, 36/869, mass-45, harmonic-50, two-axis, running rescue. The registry contains **82 retirement markers** — 38 RETIRED, 16 WITHDRAWN, 9 SUPERSEDED, 6 RELABELED, 4 RE-SCOPED, 4 TIER CORRECTED, 4 slips, 1 alias.

**Coverage is under one in ten, and the selection is by memory.** So the instrument fires only for retirements someone remembered to add to it, which is the same failure mode it exists to catch, one level up. Every ruling found today is absent from the list: the genus, the colour-mediator withdrawal, the α clause, T2401's relabel. **The check could not have fired on any of them.**

The file even says so about itself, in a comment dated 08-25: *"It could NOT have caught the real un-propagated retirement found the same day."* The response then was to add that term to the list. **The architecture was never questioned, including by me, and I own the instrument.**

## 3. The fix, prototyped and controlled
Derive the watch list from the corpus instead of remembering it. The prototype scans for the retirement vocabulary, extracts the row ids and dates around each hit, and returns an inventory.

```
derived retirement inventory: 81 markers
  with an inline date: 62   |  naming at least one row id: 69
  POSITIVE CONTROL (must find today's four):
     genus/7-2          FOUND
     colour/mediator    FOUND
     alpha clause       FOUND
     relabel-only       FOUND
  hand list: 8.  Derived: 81.
```

**The control is the point: it must find the four rulings the hand list missed, and it does.**

## 4. What is still owed, stated as owed
This is an inventory, not yet a detector. The step that would have caught T2543 and T2334 automatically is the **consumer match**: for each dated retirement, find rows that use the retired object *without* the marker, especially rows registered after the ruling's date. That needs an object extractor per marker and it needs its own positive and negative controls before it can gate anything. **Until then the inventory is a morning reading list, and I will read it rather than the eight-item summary.**

## 5. The rule this earns
**An instrument with a hand-maintained watch list inherits the memory it was built to replace.** A control that must be told what to look for is a checklist wearing an instrument's clothes. The corpus already had the harder version of this lesson from Elie: a control that runs after you read the answer is a check; one that gates the read is an instrument. **Mine gated the read against a list I wrote from memory.**

— Keeper
