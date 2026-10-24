"""Monta o HTML do app de um idioma: practice/ (treino) + skills/ (habilidades) + dados.

Uso no build de cada idioma (ver docs/PADRAO-IDIOMAS.md):

    from practice.build import build_app
    build_app(page, data, out_path)

`page` traz os textos da interface (marca, títulos, rótulos) e os caminhos do lang.js
e do HTML do alfabeto; `data` é o JSON do app (questions, modules, roman, guide, skills…).
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parent / "skills"
CLOUD_SYNC_VERSION = "20261023-1"
UI_VERSION = "20261025-1"

KEYS = ("brand", "brand_word", "name", "alphabet_tab", "eyebrow", "headline", "intro", "level_prefix",
        "level1", "level2", "typing_label", "typing_hint", "html_lang")


def ui_loader(code: str) -> str:
    """Idioma da interface: carrega o dicionário já no <head> quando o aluno escolheu o idioma estudado."""
    dict_tag = f'<script src="/assets/ui/{code}.js?v={UI_VERSION}"><\\/script>'
    return (f'<script>window.ROUTINE_UI_VERSION="{UI_VERSION}";'
            f'try{{if(localStorage.getItem("routine-ui-lang-{code}")==="{code}")document.write(\'{dict_tag}\')}}catch(e){{}}</script>'
            f'<script src="/assets/ui-language.js?v={UI_VERSION}"></script>')


# Fonte com os caracteres do idioma (a Plus Jakarta Sans só cobre o alfabeto latino).
CJK_FONTS = {"ko": "Noto Sans KR", "ja": "Noto Sans JP", "zh": "Noto Sans SC"}


def fonts(code: str) -> str:
    families = "family=Plus+Jakarta+Sans:wght@400;500;600;700;800"
    cjk = CJK_FONTS.get(code)
    if not cjk:
        return f'<link href="https://fonts.googleapis.com/css2?{families}&display=swap" rel="stylesheet">'
    families += f"&family={cjk.replace(' ', '+')}:wght@400;500;700"
    return (f'<link href="https://fonts.googleapis.com/css2?{families}&display=swap" rel="stylesheet">'
            f'<style>html body,html button,html input,html select,html textarea{{font-family:"Plus Jakarta Sans","{cjk}",system-ui,sans-serif}}'
            f':lang({code}){{font-family:"{cjk}","Plus Jakarta Sans",sans-serif;letter-spacing:0!important;word-break:keep-all}}'
            f'html h1,html h2,html .qtext,html .brand{{letter-spacing:-.2px}}</style>')


def guard(code: str) -> str:
    return ('<style>html[data-cloud-auth="pending"] body{visibility:hidden}</style>'
            '<script>document.documentElement.dataset.cloudAuth="pending"</script>'
            '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>'
            f'<script src="/config.js"></script><script>window.ROUTINE_LANGUAGE="{code}"</script>'
            f'<script src="/assets/cloud-sync.js?v={CLOUD_SYNC_VERSION}"></script>' + ui_loader(code))


def build_app(page: dict, data: dict, out: Path) -> str:
    page = {"level1": f"{page.get('level_prefix', '')} 1", "level2": f"{page.get('level_prefix', '')} 2", **page}
    missing = [k for k in KEYS if not page.get(k)]
    assert not missing, f"Faltam textos da página: {missing}"
    html = (HERE / "template.html").read_text(encoding="utf-8")
    styles = (HERE / "styles.css").read_text(encoding="utf-8") + (SKILLS / "skills.css").read_text(encoding="utf-8")
    html = (html.replace("{{GUARD}}", guard(page["code"]))
            .replace("{{STYLES}}", styles)
            .replace("{{SKILLS}}", (SKILLS / "skills.js").read_text(encoding="utf-8"))
            .replace("{{DATA}}", "window.ROUTINE_DATA = " + json.dumps(data, ensure_ascii=False) + ";")
            .replace("{{LANG_JS}}", Path(page["lang_js"]).read_text(encoding="utf-8"))
            .replace("{{APP}}", (HERE / "practice.js").read_text(encoding="utf-8"))
            .replace("{{ALPHABET_SECTION}}", Path(page["alphabet_html"]).read_text(encoding="utf-8"))
            .replace("{{FONTS}}", fonts(page["code"]))
            .replace("{{COUNT}}", f"{len(data['questions']):,}".replace(",", ".")))
    for key in KEYS:
        html = html.replace("{{" + key.upper() + "}}", page[key])
    assert "{{" not in html, html[html.index("{{"):html.index("{{") + 40]
    out.write_text(html, encoding="utf-8", newline="\n")
    return html
