# Keeper Calibration #19 — v0.11+ Forecast vs Ratified-State Count

**Filed**: 2026-05-22 Friday 09:10 EDT (Keeper, FAST CADENCE, per Cal #90)

## What Cal #90(c) caught

Cal Referee Log #90 item (c) — load-bearing referee call:

> Under PCAP cadence, null-model arithmetic for v0.11+/v0.13 projections (~9.7×10⁻¹¹, ~3×10⁻¹⁵) should NOT count C15/C16/C17 candidates until each individually passes RIGOROUSLY CLOSED 4-requirement check. Honest formal count stays 10 FORMAL + 1 ASPIRATIONAL + 3 candidates (SEED/STRUCTURALLY VERIFIED). Internal forecast-language is fine; external-facing documents must match current ratified-state count.

## My error

In `Strong_Uniqueness_Theorem_v0_11_Plus_Candidate_State.md` I quoted joint null-model figures (~3×10⁻¹², ~10⁻¹⁵, ~1.4×10⁻¹⁹) that assume the four advancing criteria reach RIGOROUSLY CLOSED. These are *forecast* numbers for the v0.11+ endpoint, not *current* ratified-state numbers.

Even though I clearly labeled this as "candidate state" / "if all four advancing close" / "endpoint", the joint null-model arithmetic could leak into external-facing documents (paper #126, paper #127, Mersenne Network position doc) without the conditional language.

## Current honest ratified-state count

Per Cal #90: **10 FORMAL + 1 ASPIRATIONAL + 3 candidates**.

Where:
- 10 FORMAL = 11 RIGOROUSLY CLOSED minus 1 ASPIRATIONAL (which I miscounted)
- 1 ASPIRATIONAL = one of the C-criteria that has not yet fully closed
- 3 candidates = C15 SEED + C16 STRUCTURALLY VERIFIED 6 (now 25) Cartan types + C9 STRUCTURALLY VERIFIED at dim_C=5

Wait — let me reconcile with Lyra's broadcast 08:41 EDT:
- 11 RIGOROUSLY CLOSED (C1-C6 + C8 + C10-C11 + C13-C14)
- 4 advancing (C7 + C9 STRUCTURALLY VERIFIED dim_C=5; C15 SEED; C16 STRUCTURALLY VERIFIED 6→25 Cartan types)

Cal #90 says current honest count = 10 FORMAL + 1 ASPIRATIONAL + 3 candidates. The numbering shows:
- Cal's "10 FORMAL" = 10 of the 11 RIGOROUSLY CLOSED that are unconditional
- Cal's "1 ASPIRATIONAL" = the one RIGOROUSLY CLOSED that has open closure (likely C13 Substrate Closure Principle if Casey-name)
- Cal's "3 candidates" = the four advancing minus one that may overlap

Coordination question for Lyra + Cal: exact reconciliation of 11 vs 10+1 counts.

## What I'll fix

1. **Update `Strong_Uniqueness_Theorem_v0_11_Plus_Candidate_State.md`** to clearly mark:
   - "Current ratified-state count: 10 FORMAL + 1 ASPIRATIONAL + 3 candidates (SEED/STRUCTURALLY VERIFIED)"
   - "Joint null-model arithmetic below is FORECAST under v0.11+ endpoint, NOT current ratified-state"

2. **Verify other Friday morning docs** for the same leakage:
   - `Keeper_Mersenne_Network_Convergence_Position_v0_1.md` — uses joint null ~3×10⁻¹⁵ language
   - `Keeper_Six_Interface_Cross_Cartography_Map_v0_1.md` — uses joint null ~10⁻¹⁴ to ~10⁻¹⁵
   - `Master_Doc_v0_16_Absorption_Grace_39_Pull.md` — uses joint null arithmetic

3. **Standing rule from Cal #90**: External-facing documents must use ratified-state count; internal forecast-language is fine but should be EXPLICITLY MARKED as forecast.

## Calibration logged

**Calibration #19**: Keeper accepted Cal #90(c) load-bearing referee call. Forecast-language vs ratified-state count distinction tightened in Friday morning Keeper-lane work. v0.11+ doc + Mersenne Network + Six-Interface + Master Doc v0.16 all flagged for forecast-language marking.

Calibration #18 (v0.13 → v0.11+ methodology tier conflation) + Calibration #19 (v0.11+ forecast-vs-ratified-state arithmetic) form a pair — both correct over-projection in different dimensions.

**This is healthy audit-chain operation**: Cal external referee catches what Keeper internal audit projected too aggressively. PCAP cadence enables high productivity *only* with tier-discipline rails to keep it honest (per Cal #90 closing).

— Keeper, Calibration #19 logged Friday 09:10 EDT (FAST CADENCE, per Cal #90)
