"""Checks do conteúdo do Chinese Routine: python tests/chinese_content_test.py"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "chinese"))
sys.path.insert(0, str(ROOT))
import build_chinese as b  # noqa: E402
import content as C  # noqa: E402
import skills_content as SK  # noqa: E402
from pinyin import pinyin  # noqa: E402
from skills.build import skills_bundle  # noqa: E402

qs = b.build()
b.validate(qs)
assert len(qs) >= 1800, len(qs)
assert {q["module"] for q in qs} == set(b.MODULES)

# Pinyin por dicionário: leituras ambíguas resolvidas pela palavra inteira.
cases = {
    "你好": "nǐ hǎo", "音乐": "yīnyuè", "睡觉": "shuìjiào", "银行": "yínháng", "四只猫": "sì zhī māo",
    "我觉得很好。": "wǒ juéde hěn hǎo.", "他说得很好": "tā shuō de hěn hǎo", "我七点可能到不了": "wǒ qī diǎn kěnéng dào bu liǎo",
}
for hz, py in cases.items():
    assert pinyin(hz) == py, (hz, pinyin(hz))
for hz, py, *_ in C.VOCAB:
    assert pinyin(hz) == py, (hz, pinyin(hz), py)

# Tons: a variante gerada muda só a marca do tom.
assert [b.retone("mǎ", k) for k in (1, 2, 3, 4)] == ["mā", "má", "mǎ", "mà"]
assert b.retone("guì", 1) == "guī" and b.retone("liù", 3) == "liǔ" and b.tone_of("nǚ") == 3

# Digitar: pinyin com e sem tons é aceito.
q = next(x for x in qs if x["module"] == "vocabulario" and x["answers"][0] == "朋友")
assert {"péngyou", "pengyou"} <= set(q["answers"])

# Classificador geral 个 nunca é distrator.
assert all("个" not in x["distractors"] for x in qs if x["module"] == "classificadores")

skills, _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, b.listen_choice(qs), pinyin)
assert len(skills["texts"]) >= 20 and len(skills["prompts"]) >= 16
assert {t["level"] for t in skills["texts"]} == {"HSK 1", "HSK 2"}
assert len(skills["listenChoice"]) >= 100

html = (ROOT / "public" / "chinese.html").read_text(encoding="utf-8")
assert 'window.ROUTINE_LANGUAGE="zh"' in html and "{{" not in html
print(f"ok: {len(qs)} questões")
