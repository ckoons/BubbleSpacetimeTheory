exec(open('resonance2.py').read().split('print("R = 6')[0])
mp.dps=80
for par in (False,True):
    sp=spec(5,420,par); c=fit(sp,5,[mpf(x) for x in np.linspace(0.0015,0.004,14)],8)
    print(('p=q mod 2' if par else 'all (p,q) [corpus]')+': '+'  '.join(f'a{k}/a0={float(c[k]/c[0]):.4f}' for k in range(1,6)))
