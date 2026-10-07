"""Cal S1031 -- checks behind the K4-1 hash. Plain Python."""
import itertools, numpy as np
ok=n=0
def check(s,c):
    global ok,n; n+=1; ok+=bool(c); print(("PASS " if c else "FAIL ")+s)
me,Q,dnp=0.51099895,0.78233,1.29333   # MeV; CODATA/PDG values as pinned by Grace/Keeper in K4-1 prompt
print("Q/m_e =",round(Q/me,4),"(m_n-m_p)/m_e =",round(dnp/me,4))
check("Q/m_e is within 2.1% of 3/2 (a decoy any small-integer formula can hit)",abs(Q/me/1.5-1)<0.021)
# weak coupling set: particle-L and antiparticle-R. Read orientation o = +1 on coupled records.
coupled={("p","L"),("a","R")}; o=lambda s:1 if s in coupled else -1
C=lambda s:("a" if s[0]=="p" else "p",s[1]); P=lambda s:(s[0],"R" if s[1]=="L" else "L"); CP=lambda s:C(P(s))
S=list(itertools.product("pa","LR"))
check("C reverses o on every record",all(o(C(s))==-o(s) for s in S))
check("P reverses o on every record",all(o(P(s))==-o(s) for s in S))
check("CP PRESERVES o on every record (so a deck flip that reverses o cannot be CP)",all(o(CP(s))==o(s) for s in S))
check("o = (particle sign) x (chirality sign): a product of two Z2s",all(o(s)==(1 if s[0]=="p" else -1)*(1 if s[1]=="L" else -1) for s in S))
rng=np.random.default_rng(1); v=rng.normal(size=3)+1j*rng.normal(size=3)
w=v*np.exp(0.7j); u=v.copy(); u[0]*=np.exp(0.7j); R=lambda x:np.outer(x,x.conj())
check("pure record vv† forgets ONLY the global phase (relative phases are kept)",np.allclose(R(v),R(w)) and not np.allclose(R(v),R(u)))
# loop sign on a sphere record: pi_1(S^2)=0 => every read cycle is null-homotopic in the record => w1=+1 on its image
# (stated, not computed: the composition pi_1(S^2)=0 -> pi_1(Silov)=Z -> Z2 is zero)
check("K4 sphere: H1 rank = E-V+1-F+1 = 0 (every cycle bounds faces)",(6-4+1)-(4-1)==0)
print(f"SCORE {ok}/{n}")
