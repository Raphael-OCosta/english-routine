"""Checks do conteúdo de francês, italiano e alemão: python tests/european_content_test.py"""
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from skills.build import skills_bundle  # noqa: E402


def load(folder, names):
    """Importa os módulos de uma pasta de idioma isolando nomes repetidos (content, skills_content…)."""
    for name in ("content", "skills_content", *names):
        sys.modules.pop(name, None)
    sys.path.insert(0, str(ROOT / folder))
    try:
        return [importlib.import_module(n) for n in names]
    finally:
        sys.path.pop(0)


def common(b, SK, name):
    qs = b.build()
    b.validate(qs)
    assert len(qs) >= 9500, len(qs)
    assert {q["module"] for q in qs} == set(b.MODULES)
    assert all(q["typeable"] is False for q in qs if q["module"] == "falsos")
    skills, _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, b.listen_choice(qs))
    assert len(skills["texts"]) >= 20 and len(skills["prompts"]) >= 16
    for t in SK.TEXTS:
        assert all(0 <= q["answer"] < len(q["options"]) for q in t["questions"]), t["id"]
    for q in qs:  # a frase falada é a frase com as respostas no lugar das lacunas
        if q.get("slots") and q["audio"]:
            assert "___" not in q["audio"], q["id"]
    print(f"{name} ok: {len(qs)} questões")
    return qs


# ---------------------------------------------------------------- francês
b, SK = load("french", ["build_french", "skills_content"])
qs = common(b, SK, "francês")
assert b.present("parler", 0) == "parle" and b.present("aller", 3) == "allons" and b.present("être", 5) == "sont"
assert b.imparfait("manger", 0) == "mangeais" and b.imparfait("manger", 3) == "mangions" and b.imparfait("être", 2) == "était"
assert b.participle("acheter") == "acheté" and b.participle("venir") == "venu"
assert not any("de a" in (q["audio"] or "") or "je a" in (q["audio"] or "").lower() for q in qs)
for q in qs:  # presente sem marcador de tempo não pode ter outro tempo como distrator
    if q["module"] == "verbos" and q["theme"] == "presente":
        assert not any(d.startswith(("vais ", "va ", "vas ", "allons ", "allez ", "vont ")) for d in q["distractors"]), q["id"]

# ---------------------------------------------------------------- italiano
b, SK = load("italian", ["build_italian", "skills_content"])
qs = common(b, SK, "italiano")
assert [b.present("cercare", p) for p in range(6)] == ["cerco", "cerchi", "cerca", "cerchiamo", "cercate", "cercano"]
assert b.present("studiare", 1) == "studi" and b.present("mangiare", 3) == "mangiamo" and b.present("finire", 5) == "finiscono"
assert b.future("mangiare", 0) == "mangerò" and b.future("cercare", 0) == "cercherò" and b.future("andare", 0) == "andrò"
assert b.imperfect("parlare", 0) == "parlavo" and b.imperfect("essere", 2) == "era"
assert b.participle("leggere") == "letto" and b.participle("comprare") == "comprato" and b.gerund("fare") == "facendo"
assert b.article("studente", "m") == "lo" and b.article("aereo", "m") == "l'" and b.article("studenti", "m", True) == "gli" and b.article("casa", "f") == "la"
for q in qs:  # verbos de movimento aceitam as duas concordâncias com io/tu
    if q["module"] == "verbos" and q["theme"] == "passato prossimo" and q["text"].startswith("Ieri io") and "andare" in q["prompt"]:
        assert set(q["answers"]) == {"sono andato", "sono andata"}, q["id"]
for q in qs:  # "in" nunca é distrator de preposição de lugar (in stazione, in aeroporto também existem)
    for s in q.get("slots", []):
        if s["label"] == "preposição":
            assert "in" not in s["distractors"], q["id"]

# ---------------------------------------------------------------- alemão
b, SK = load("german", ["build_german", "skills_content"])
qs = common(b, SK, "alemão")
assert [b.present("arbeiten", p) for p in range(6)] == ["arbeite", "arbeitest", "arbeitet", "arbeiten", "arbeitet", "arbeiten"]
assert b.present("tanzen", 1) == "tanzt" and b.present("fahren", 2) == "fährt" and b.present("öffnen", 2) == "öffnet"
assert b.participle("kaufen") == "gekauft" and b.participle("studieren") == "studiert" and b.participle("besuchen") == "besucht"
assert b.participle("arbeiten") == "gearbeitet" and b.participle("essen") == "gegessen"
assert b.aux("fahren", 0) == "bin" and b.aux("kaufen", 0) == "habe"
for q in qs:  # verbo na 2ª posição depois do advérbio; substantivos em maiúscula no áudio
    if q["module"] == "completar" and q["audio"].startswith("Gestern "):
        assert q["audio"].split()[1] in ("habe", "hast", "hat", "haben", "habt", "bin", "bist", "ist", "sind", "seid"), q["id"]
    if q["module"] == "completar" and q["theme"] == "movimento":
        assert q["slots"][1]["answers"][0] in ("in den", "ins", "in die"), q["id"]
print("ok")
