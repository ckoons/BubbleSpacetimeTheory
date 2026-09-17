#!/usr/bin/env python3
"""Apply the staged A9 run-1 row edit (Grace, 2026-09-17) in one move. Assertion-before-write throughout."""
import re, sys, datetime, subprocess
S="notes/grace_STAGED_A9_run1_Landing_C_register_edit_with_Lyra_held_line_apply_on_ix_2026-09-17.md"
R="notes/Elie_FALSIFIER_REGISTER_v0_2_C1_owned_and_pinned_NuFIT6_three_delta_CP_claims_discipline_adopted_2026-08-24.md"
st=open(S).read()
def piece(n):
    m=re.search(r"## Piece %d[^\n]*\n(.*?)\n\n## "%n, st, re.S); assert m, n
    return m.group(1).strip()
P=[piece(1),piece(2),piece(3)]
for i,p in enumerate(P,1):
    assert not re.search(r"\[[A-Z_]+\]",p), f"Piece {i} still has an unfilled bracket"
anchor="Neither a large amplitude alone nor an angle alone fires it. |"
s=open(R).read(); assert s.count(anchor)==1, s.count(anchor)
ts=datetime.datetime.now().strftime("%H:%M"); d=datetime.date.today().isoformat()
s=s.replace(anchor, "Neither a large amplitude alone nor an angle alone fires it. "+" ".join(P)+" |",1)
h=re.match(r"# FALSIFIER REGISTER v0\.16 \(Ext 5's owed\)[^\n]*\n\n\*\*v0\.16[^\n]*\n", s); assert h, "header v0.16 not found"
s=s.replace(h.group(0), f"# FALSIFIER REGISTER v0.17 (Ext 5's owed) — A9 RUN 1 certified: Quaia G<20.5 (+G<20.0), v1.5.2, LANDING C by §4.4 profile-alternative + per-bin residual; Lyra's second-channel line merged — Grace\n\n**v0.17 (Grace, {d} {ts}): A9 row only (run-1 certification + Lyra's two lines). No other row touched.**\n\n## superseded header: "+h.group(0).lstrip("# "),1)
open(R,'w').write(s); print("applied v0.17;", subprocess.run(["git","diff","--stat",R],capture_output=True,text=True).stdout.strip())
