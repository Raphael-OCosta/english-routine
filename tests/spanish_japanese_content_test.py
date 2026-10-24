"""Checks do conteúdo de espanhol e japonês: python tests/spanish_japanese_content_test.py"""
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from skills.build import skills_bundle  # noqa: E402


def load(folder, names):
    """Importa os módulos de uma pasta de idioma isolando nomes repetidos (content, skills_content…)."""
    for name in ("content", "skills_content", "kana", "readings", *names):
        sys.modules.pop(name, None)
    sys.path.insert(0, str(ROOT / folder))
    try:
        return [importlib.import_module(n) for n in names]
    finally:
        sys.path.pop(0)


# ---------------------------------------------------------------- espanhol
b, C, SK = load("spanish", ["build_spanish", "content", "skills_content"])
qs = b.build()
b.validate(qs)
assert len(qs) >= 1500, len(qs)
assert {q["module"] for q in qs} == set(b.MODULES)
# conjugação: regulares e irregulares
assert b.present("hablar", 0) == "hablo" and b.present("comer", 3) == "comemos" and b.present("vivir", 5) == "viven"
assert b.present("tener", 0) == "tengo" and b.present("poder", 2) == "puede" and b.present("ir", 3) == "vamos"
assert b.past("hablar", 2) == "habló" and b.past("comer", 0) == "comí" and b.past("ir", 0) == "fui" and b.past("hacer", 2) == "hizo"
assert b.past("llegar", 0) == "llegué" and b.past("leer", 2) == "leyó"
# contrações e artigos nas frases com lacunas
for q in qs:
    if q["module"] == "completar" and q["theme"] == "ir a":
        assert q["slots"][1]["answers"][0] in ("al", "a la"), q["id"]
assert all(q["typeable"] is False for q in qs if q["module"] == "falsos")
skills, _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, b.listen_choice(qs))
assert len(skills["texts"]) >= 20 and len(skills["prompts"]) >= 16
print(f"espanhol ok: {len(qs)} questões")

# ---------------------------------------------------------------- japonês
b, C, SK, K = load("japanese", ["build_japanese", "content", "skills_content", "kana"])
b.load_readings()
qs = b.build()
b.validate(qs)
assert len(qs) >= 1800, len(qs)
assert {q["module"] for q in qs} == set(b.MODULES)
cases = {
    "きって": "kitte", "コーヒー": "koohii", "がっこう": "gakkou", "しんぶん": "shinbun", "まっちゃ": "matcha", "きんえん": "kin'en",
}
for kana, rom in cases.items():
    assert K._romaji_kana(kana) == rom, (kana, K._romaji_kana(kana))
sentences = {
    "私は学生です。": "watashi wa gakusei desu.", "毎日すしを食べます。": "mainichi sushi o tabemasu.",
    "部屋に猫がいます。": "heya ni neko ga imasu.", "東京へ行きます。": "toukyou e ikimasu.", "こんにちは": "konnichiwa",
    "このかばんは高くないです。": "kono kaban wa takakunai desu.", "分かりません": "wakarimasen",
}
for ja, rom in sentences.items():
    assert K.romaji(ja) == rom, (ja, K.romaji(ja))
for w, kana, *_ in C.VOCAB:
    assert K.reading(w) == kana, (w, K.reading(w), kana)
skills, _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, b.listen_choice(qs), K.romaji)
assert len(skills["texts"]) >= 20 and len(skills["prompts"]) >= 16
for page in ("spanish.html", "japanese.html"):
    html = (ROOT / "public" / page).read_text(encoding="utf-8")
    assert "{{" not in html and "ROUTINE_APP" in html, page
print(f"japonês ok: {len(qs)} questões")
