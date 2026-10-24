"""Checks dos dicionários de interface: python tests/ui_strings_test.py"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "ui"))
import english_ui  # noqa: E402
import strings as S  # noqa: E402

TOKEN = re.compile(r"\{n\}|\{\d\}")


def check_pattern(src, dst, where):
    a, b = TOKEN.findall(src), TOKEN.findall(dst)
    assert a.count("{n}") == b.count("{n}"), (where, src, dst)
    assert set(t for t in b if t != "{n}") <= set(t for t in a if t != "{n}"), (where, src, dst)


for row in S.EXACT:
    assert len(row) == len(S.LANGS) + 1 and all(x.strip() for x in row), row[0]
for row in S.PATTERNS:
    assert len(row) == len(S.LANGS) + 1, row[0]
    for code, dst in zip(S.LANGS, row[1:]):
        # textos traduzidos sem variáveis podem omitir {0} (ex.: o nome do idioma já vem traduzido)
        assert dst.count("{n}") == row[0].count("{n}"), (code, row[0], dst)
keys = [r[0] for r in S.EXACT]
assert len(keys) == len(set(keys)), [k for k in keys if keys.count(k) > 1]
for code in S.LANGS:
    assert set(S.HEADLINE) >= {code} and set(S.INTRO) >= {code}, code

en = [r[0] for r in english_ui.EXACT]
assert len(en) == len(set(en)), [k for k in en if en.count(k) > 1]
for src, dst in english_ui.PATTERNS:
    check_pattern(src, dst, "en")

# os textos fonte do app comum existem de fato no código (evita chave morta por renomeação)
code = "".join((ROOT / p).read_text(encoding="utf-8") for p in ("practice/template.html", "practice/practice.js", "skills/skills.js", "public/assets/cloud-sync.js"))
dead = [k for k in keys[:40] if k not in code and k not in ("Correto!", "Olá,")]
assert not dead, dead
print(f"ui ok: {len(keys)} textos × {len(S.LANGS)} idiomas, {len(S.PATTERNS)} padrões; inglês {len(en)} textos")


# ---------------------------------------------------------------- enunciados no idioma estudado
def compile_pattern(src):
    out = ""
    for part in re.split(r"(\{n\}|\{\d\})", src):
        if part == "{n}":
            out += r"(\d+(?:[.,]\d+)?)"
        elif re.fullmatch(r"\{\d\}", part):
            out += "(.+?)"
        else:
            out += re.escape(part)
    return re.compile("^" + out + "$", re.S)


def covered(text, table):
    if text in table["exact"]:
        return True
    return any(compile_pattern(src).match(text) for src, _ in table["patterns"])


sys.path.insert(0, str(ROOT / "ui"))
import build_ui  # noqa: E402
import json  # noqa: E402

for code, folder in (("ko", "korean"),):
    table = build_ui.language(code)
    html = (ROOT / "public" / f"{folder}.html").read_text(encoding="utf-8")
    start = html.index("window.ROUTINE_DATA = ") + len("window.ROUTINE_DATA = ")
    data, _ = json.JSONDecoder().raw_decode(html[start:])
    prompts = {q["prompt"] for q in data["questions"]}
    labels = {s["label"] for q in data["questions"] for s in q.get("slots", [])}
    missing = sorted(p for p in prompts | labels if not covered(p, table))
    assert not missing, (code, missing[:10])
    for src, dst in S.PROMPTS[code]["patterns"]:
        assert "{" not in re.sub(r"\{n\}|\{\d\}", "", dst), dst
    print(f"enunciados {code} ok: {len(prompts)} enunciados e {len(labels)} rótulos cobertos")
