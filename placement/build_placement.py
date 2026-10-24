"""Gera as páginas de nivelamento (uma por idioma) a partir do motor comum.

Rode: python placement/build_placement.py
Inglês → public/nivelamento.html. Novos idiomas: criar bank_<lang>.py e uma entrada em PAGES.
"""
from __future__ import annotations

import json
from pathlib import Path

import bank_en

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT.parent / "public"

CEFR = [
    {"code": "A1", "b": -2.5, "min": -99, "title": "Iniciante",
     "description": "Você entende e usa expressões do dia a dia e frases muito simples, como se apresentar e fazer perguntas básicas.",
     "plan": ["Gramática: simple present, verbo to be, there is/are e preposições de tempo.", "Reading nível A1, um texto por dia.", "Meta diária sugerida: 20 questões."]},
    {"code": "A2", "b": -1.5, "min": -2.0, "title": "Básico",
     "description": "Você se comunica em situações simples e rotineiras: compras, trabalho, família e o passado com frases curtas.",
     "plan": ["Gramática: simple past, comparativos, going to e present perfect com since/for.", "Reading A2 e “Ouça e escolha” no Listening.", "Meta diária sugerida: 30 questões."]},
    {"code": "B1", "b": -0.5, "min": -1.0, "title": "Intermediário",
     "description": "Você entende os pontos principais de textos claros, lida com viagens e conta experiências e planos.",
     "plan": ["Gramática: condicionais 1 e 2, past perfect, voz passiva e discurso indireto.", "Reading B1 com cronômetro e Writing B1.", "Meta diária sugerida: 40 questões."]},
    {"code": "B2", "b": 0.5, "min": 0.0, "title": "Intermediário superior",
     "description": "Você discute temas variados com fluência, entende argumentos complexos e escreve textos claros e detalhados.",
     "plan": ["Gramática: terceira condicional, future perfect, wish e verbos com -ing/to.", "Reading B2, Writing B2 e Speaking em formato entrevista.", "Meta diária sugerida: 50 questões, com 2–3 lacunas."]},
    {"code": "C1", "b": 1.5, "min": 1.0, "title": "Avançado",
     "description": "Você usa o idioma com flexibilidade no trabalho e nos estudos e entende textos longos com sentidos implícitos.",
     "plan": ["Gramática: inversões, subjuntivo, passiva reportada e linking words avançadas.", "Reading C1 e Writing C1 com correção no chat.", "Meta diária sugerida: 50 questões combinadas."]},
    {"code": "C2", "b": 2.5, "min": 2.0, "title": "Proficiente",
     "description": "Você entende praticamente tudo e se expressa com precisão, nuance e naturalidade.",
     "plan": ["Desafios C2 e C2+ do Reading e Writing.", "Shadowing de textos C2 no Speaking.", "Mantenha a constância: 30–50 questões por dia para revisar e não perder fluência."]},
]

PAGES = {
    "en": {
        "out": "nivelamento.html", "bank": bank_en.BANK, "lang": "en", "tts": "en-US", "voice": "^en",
        "levels": CEFR, "quota": {"grammar": 18, "reading": 6, "listening": 6},
        "typeLabels": {"grammar": "Gramática", "vocab": "Vocabulário", "reading": "Leitura", "listening": "Escuta"},
        "title": "Teste de nível de inglês grátis · English Routine",
        "description": "Descubra seu nível de inglês (A1 a C2) em cerca de 15 minutos com um teste adaptativo gratuito.",
        "eyebrow": "Teste de nível · inglês", "headline": "Descubra seu nível de inglês.",
        "intro": "Um teste adaptativo de gramática, vocabulário, leitura e escuta. Em cerca de 15 minutos você recebe uma estimativa na escala CEFR (A1 a C2) e um plano de treino.",
        "brand": "English Routine",
    },
}


def validate(bank, levels):
    codes = {l["code"] for l in levels}
    for q in bank:
        assert q["level"] in codes, q
        assert len(q["options"]) == 4 and len(set(q["options"])) == 4, q["stem"]
        assert q["why"], q["stem"]
        if q["type"] == "listening":
            assert q["audio"], q["stem"]
        if q["type"] == "reading":
            assert q["passage"], q["stem"]


def main():
    template = (ROOT / "template.html").read_text(encoding="utf-8")
    engine = (ROOT / "placement.js").read_text(encoding="utf-8")
    for code, page in PAGES.items():
        validate(page["bank"], page["levels"])
        config = {k: page[k] for k in ("lang", "tts", "voice", "levels", "quota", "typeLabels", "bank")}
        total = sum(page["quota"].values())
        html = (template.replace("{{ENGINE}}", engine)
                .replace("{{CONFIG}}", json.dumps(config, ensure_ascii=False))
                .replace("{{TITLE}}", page["title"]).replace("{{DESCRIPTION}}", page["description"])
                .replace("{{EYEBROW}}", page["eyebrow"]).replace("{{HEADLINE}}", page["headline"])
                .replace("{{INTRO}}", page["intro"]).replace("{{BRAND}}", page["brand"])
                .replace("{{TOTAL}}", str(total)).replace("{{LEVELS}}", str(len(page["levels"])))
                .replace("{{LANG}}", page["lang"]))
        assert "{{" not in html
        (PUBLIC / page["out"]).write_text(html, encoding="utf-8", newline="\n")
        print(f"{page['out']}: {len(page['bank'])} itens no banco, {total} por teste")


if __name__ == "__main__":
    main()
