"""Construit data/*.json depuis bank/*.py.
Chaque bank/<x>.py définit MAT = {"id","nom","chapitres":[(cid,titre),...]} et Q = [(cid, question, [bonne, fausse1, ...], explication), ...]
La bonne réponse est toujours en premier (mélangée à l'affichage)."""
import json, hashlib, importlib.util, glob, os, sys, datetime
ORDER = ["mvlen", "sb", "da", "mto", "nav", "pdv", "ccm", "hp"]
os.makedirs("data", exist_ok=True)
files = []
total = 0
for name in ORDER:
    p = f"bank/{name}.py"
    if not os.path.exists(p):
        continue
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    chap_ids = {c for c, _ in m.MAT["chapitres"]}
    qs, seen = [], set()
    for cid, t, o, e in m.Q:
        assert cid in chap_ids, (name, cid, t)
        assert len(o) >= 2 and len(set(o)) == len(o), (name, t)
        qid = cid + "-" + hashlib.md5(t.encode()).hexdigest()[:6]
        assert qid not in seen, ("doublon", t)
        seen.add(qid)
        qs.append({"id": qid, "c": cid, "t": t, "o": o, "e": e})
    d = {"id": m.MAT["id"], "nom": m.MAT["nom"],
         "chapitres": [{"id": c, "titre": t} for c, t in m.MAT["chapitres"]], "questions": qs}
    json.dump(d, open(f"data/{name}.json", "w"), ensure_ascii=False)
    files.append(f"{name}.json"); total += len(qs)
    covered = len({q["c"] for q in qs})
    # Contrôle anti-indice : la bonne réponse ne doit pas se repérer à sa longueur
    longest = [q for q in qs if len(q["o"][0]) > max(len(x) for x in q["o"][1:])]
    tooLong = [q for q in qs if len(q["o"][0]) > 1.35 * max(len(x) for x in q["o"][1:])]
    pct = round(100 * len(longest) / max(1, len(qs)))
    shortest = [q for q in qs if len(q["o"][0]) < min(len(x) for x in q["o"][1:])]
    spct = round(100 * len(shortest) / max(1, len(qs)))
    print(f"{m.MAT['nom']:<22} {len(qs):>4} questions  {covered}/{len(chap_ids)} chapitres  | bonne=plus longue {pct}%  plus courte {spct}%  trop longues {len(tooLong)}")
    for q in tooLong:
        print("   ⚠", q["c"], q["t"][:70])
    if "--strict" in sys.argv:
        assert pct <= 40 and spct <= 30 and not tooLong, f"{name}: réponses déséquilibrées"
json.dump({"matieres": files, "maj": datetime.date.today().strftime("%d/%m")}, open("data/index.json", "w"))
print("TOTAL", total)
