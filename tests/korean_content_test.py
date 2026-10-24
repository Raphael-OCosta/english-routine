"""Checks do conteúdo do Korean Routine: python tests/korean_content_test.py"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "korean"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_korean as b  # noqa: E402

qs = b.build()
b.validate(qs)

assert len(qs) >= 9500, len(qs)
assert {q["module"] for q in qs} == set(b.MODULES)
for q in qs:
    assert q["level"] in (1, 2), q["id"]
    assert q["prompt"] and q["text"] and q["explanation"], q["id"]
    assert len(set(q["distractors"])) == len(q["distractors"]), q["id"]

# Regra do batchim nas partículas geradas
cases = {"학생": "이에요", "가수": "예요", "커피": "예요", "책": "이에요"}
for word, cop in cases.items():
    expected = "이에요" if b.has_batchim(word) else "예요"
    assert expected == cop, word
assert b.batchim_is_rieul("지하철") and not b.batchim_is_rieul("버스")
for q in qs:
    if q["module"] != "particulas":
        continue
    m = re.search(r"(\S+)___", q["text"])
    if not m or not re.fullmatch(r"[가-힣]+", m.group(1)):
        continue
    word, ans = m.group(1), q["answers"][0]
    pairs = {("은", "는"), ("이", "가"), ("을", "를"), ("과", "와"), ("이에요", "예요")}
    for withb, without in pairs:
        if ans in (withb, without):
            assert ans == (withb if b.has_batchim(word) else without), (q["id"], word, ans)

# Frases com várias lacunas: partículas pela regra do batchim
multi = [q for q in qs if q.get("slots")]
assert len(multi) >= 600, len(multi)
for q in multi:
    words = re.findall(r"(\S+?)___", q["text"])
    for word, s in zip(words, q["slots"]):
        ans = s["answers"][0]
        for withb, without in {("은", "는"), ("을", "를")}:
            if ans in (withb, without):
                assert ans == (withb if b.has_batchim(word) else without), (q["id"], word, ans)

# Romanização (pronúncia mostrada abaixo das opções) confere com a RR oficial
from romanize import romanize  # noqa: E402
import content as C  # noqa: E402
for ko, rr in C.READING_WORDS:
    assert romanize(ko) == rr.lower(), (ko, romanize(ko), rr)
for ko, rr in {"맛있어요": "masisseoyo", "같이": "gachi", "읽어요": "ilgeoyo", "없어요": "eopseoyo",
               "몰라요": "mollayo", "독립": "dongnip", "좋네요": "jonneyo", "축하해요": "chukahaeyo"}.items():
    assert romanize(ko) == rr, (ko, romanize(ko))

# Habilidades (módulo comum skills/): textos, propostas e "ouça e escolha"
import skills_content as SK  # noqa: E402
from skills.build import skills_bundle  # noqa: E402
skills, _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, b.listen_choice(qs), romanize)
assert len(skills["texts"]) >= 20 and len(skills["prompts"]) >= 16, (len(skills["texts"]), len(skills["prompts"]))
assert {t["level"] for t in skills["texts"]} == {"TOPIK 1", "TOPIK 2"}
assert all(t["roman"].count("\n\n") == t["text"].count("\n\n") for t in skills["texts"])
assert len(skills["listenChoice"]) >= 100, len(skills["listenChoice"])

html = (Path(__file__).resolve().parents[1] / "public" / "korean.html").read_text(encoding="utf-8")
assert 'window.ROUTINE_LANGUAGE="ko"' in html
assert "{{" not in html
print(f"ok: {len(qs)} questões")
