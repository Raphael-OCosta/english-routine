"""Checks do conteúdo do Korean Routine: python tests/korean_content_test.py"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "korean"))
import build_korean as b  # noqa: E402

qs = b.build()
b.validate(qs)

assert len(qs) >= 1000, len(qs)
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

html = (Path(__file__).resolve().parents[1] / "public" / "korean.html").read_text(encoding="utf-8")
assert 'window.ROUTINE_LANGUAGE="ko"' in html
assert "{{" not in html
print(f"ok: {len(qs)} questões")
