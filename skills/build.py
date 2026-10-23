"""Monta e valida os dados de Reading/Writing/Listening/Speaking de um idioma.

Uso no build de cada idioma (ver docs/PADRAO-IDIOMAS.md):

    from skills.build import skills_bundle
    data, css, js = skills_bundle(texts, prompts, roleplay, listen_choice, romanize)

`data` vai para o JSON do app (KDATA.skills ou equivalente); css/js são injetados no HTML.
"""
from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent


def validate(texts, prompts, listen_choice):
    ids = [t["id"] for t in texts] + [p["id"] for p in prompts]
    assert len(ids) == len(set(ids)), "IDs de habilidades repetidos"
    for t in texts:
        for key in ("id", "level", "topic", "title", "text", "questions"):
            assert t.get(key), (t.get("id"), key)
        assert "\n\n\n" not in t["text"], t["id"]
        if t.get("translation"):
            assert t["translation"].count("\n\n") == t["text"].count("\n\n"), (t["id"], "tradução com parágrafos diferentes")
        for q in t["questions"]:
            assert len(q["options"]) >= 3 and len(set(q["options"])) == len(q["options"]), (t["id"], q["question"])
            assert 0 <= q["answer"] < len(q["options"]) and q.get("why"), (t["id"], q["question"])
    for p in prompts:
        for key in ("id", "level", "topic", "prompt", "units", "lines"):
            assert p.get(key), (p.get("id"), key)
    for item in listen_choice:
        assert item["answer"] in item["options"] and len(set(item["options"])) == len(item["options"]) >= 3, item


def skills_bundle(texts, prompts, roleplay="", listen_choice=(), romanize=None):
    listen_choice = list(listen_choice)
    validate(texts, prompts, listen_choice)
    out_texts = []
    for t in texts:
        t = dict(t)
        if romanize:
            t["roman"] = "\n\n".join(romanize(p) for p in t["text"].split("\n\n"))
        out_texts.append(t)
    data = {"texts": out_texts, "prompts": list(prompts), "roleplay": roleplay, "listenChoice": listen_choice}
    css = (HERE / "skills.css").read_text(encoding="utf-8")
    js = (HERE / "skills.js").read_text(encoding="utf-8")
    return data, css, js
