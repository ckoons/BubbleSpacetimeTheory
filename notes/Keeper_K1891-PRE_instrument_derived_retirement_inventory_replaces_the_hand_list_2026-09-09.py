#!/usr/bin/env python3
"""Derived retirement inventory.  Replaces the hand-maintained RETIRED_READINGS list in
play/keeper_sod_artifact_check.py, whose coverage is 8 readings against 82 markers in the
registry -- i.e. it fires only for retirements someone REMEMBERED to add, which is the
same failure mode it exists to catch, one level up.

This derives the watch list FROM the corpus.  Positive control: it must find the four
un-propagated rulings of 2026-09-09 that the hand list could not see."""
import re,sys,os
REG='BST_AC_Theorem_Registry.md'
MARK=r"(WITHDRAWN|RE-?SCOPED|RELABEL(?:ED|-ONLY)?|\bRETIRED\b|SUPERSEDE[DS]?|TIER CORRECTED|bare-End slip|\bslip\b)"
def inventory(path=REG):
    s=open(path,encoding='utf-8',errors='replace').read()
    out=[]
    for m in re.finditer(MARK,s):
        a=max(0,m.start()-300); b=min(len(s),m.end()+300)
        seg=s[a:b]
        rid=re.findall(r"\bT\d{2,4}\b",seg)
        dat=re.findall(r"20\d\d-\d\d-\d\d",seg)
        out.append({"marker":m.group(1),"rows":sorted(set(rid))[:4],
                    "date":dat[0] if dat else None,
                    "quote":re.sub(r"\s+"," ",s[m.start()-60:m.end()+90]).strip()})
    return out
if __name__=="__main__":
    inv=inventory()
    print("derived retirement inventory: %d markers"%len(inv))
    dated=[i for i in inv if i["date"]]
    print("  with an inline date: %d   |  naming at least one row id: %d"%(
        len(dated),len([i for i in inv if i["rows"]])))
    # POSITIVE CONTROL: the four rulings found on 2026-09-09 must appear
    controls={"genus/7-2":r"7/2|genus","colour/mediator":r"M₃|colour|color","alpha clause":r"α|alpha","relabel-only":r"RELABEL"}
    joined=" || ".join(i["quote"] for i in inv)
    print("\n  POSITIVE CONTROL (must find today's four):")
    for k,rx in controls.items():
        print("     %-18s %s"%(k,"FOUND" if re.search(rx,joined) else "MISSED"))
    print("\n  hand list in the SOD check: 8 readings.  Derived here: %d."%len(inv))
    print("  first 6 entries:")
    for i in inv[:6]:
        print("     %-14s %-22s %s"%(i["marker"],",".join(i["rows"]) or "-",i["quote"][:96]))
