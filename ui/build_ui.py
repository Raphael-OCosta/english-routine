"""Gera public/assets/ui/<código>.js (idioma da interface) a partir de ui/strings.py e do PAGE de cada idioma.

Rode: python ui/build_ui.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import strings as S

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "assets" / "ui"
FOLDERS = {"ko": "korean", "zh": "chinese", "ja": "japanese", "es": "spanish", "fr": "french", "it": "italian", "de": "german"}


def page_field(folder: str, key: str) -> str | None:
    src = (ROOT / folder / f"build_{folder}.py").read_text(encoding="utf-8")
    m = re.search(rf'"{key}": "([^"]*)"', src)
    return m.group(1) if m else None


def language(code: str) -> dict:
    i = S.LANGS.index(code) + 1
    exact = {row[0]: row[i] for row in S.EXACT}
    exact.update(S.EXTRA.get(code, {}))
    folder = FOLDERS[code]
    for key, value in (("headline", S.HEADLINE[code]), ("intro", S.INTRO[code])):
        exact[page_field(folder, key)] = value
    patterns = [[row[0], row[i]] for row in S.PATTERNS]
    # Enunciados das questões (quando o idioma já tem a tradução deles): os padrões específicos vêm antes.
    prompts = S.PROMPTS.get(code, {})
    exact.update(prompts.get("exact", {}))
    patterns = [list(p) for p in prompts.get("patterns", [])] + patterns
    return {"exact": exact, "patterns": patterns}


def write(code: str, table: dict) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{code}.js"
    body = json.dumps(table, ensure_ascii=False, separators=(",", ":"))
    path.write_text(f"(window.ROUTINE_UI=window.ROUTINE_UI||{{}}).{code}={body};\n", encoding="utf-8", newline="\n")
    return path


def main():
    for row in S.EXACT + S.PATTERNS:
        assert len(row) == len(S.LANGS) + 1, row[0]
    for code in S.LANGS:
        table = language(code)
        print(write(code, table).name, len(table["exact"]), "textos,", len(table["patterns"]), "padrões")
    try:
        import english_ui  # noqa: E402  (inglês: textos do app próprio)
        print(write("en", english_ui.table()).name, "inglês")
    except ModuleNotFoundError:
        pass


if __name__ == "__main__":
    main()
