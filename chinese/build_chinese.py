"""Gera public/chinese.html (Chinese Routine) a partir de content.py + practice/ + skills/.

Rode: python chinese/build_chinese.py
IDs são estáveis (prefixo por módulo + ordem fixa) para preservar o histórico.
"""
from __future__ import annotations

import random
import sys
import unicodedata
from pathlib import Path

import content as C
import skills_content as SK
from pinyin import is_hanzi, pinyin

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT.parent / "public"
sys.path.insert(0, str(ROOT.parent))
from practice.build import build_app  # noqa: E402
from skills.build import skills_bundle  # noqa: E402

PAGE = {
    "code": "zh", "html_lang": "zh-CN", "brand": "Chinese Routine", "brand_word": "chinese", "name": "chinês",
    "alphabet_tab": "Pinyin e tons", "eyebrow": "Mandarim todos os dias · HSK 1–2", "headline": "你好！Vamos treinar.",
    "intro": "questões de tons, pinyin, vocabulário, classificadores, gramática, frases para completar, números e escuta. Responda escolhendo ou digitando em caracteres ou em pinyin.",
    "level_prefix": "HSK", "typing_label": "Digitar (caracteres ou pinyin)",
    "typing_hint": "Digite em caracteres com o teclado chinês (pinyin) ou direto em pinyin, com ou sem tons: “ni hao” vale para 你好. No Windows: Configurações › Hora e idioma › Idioma › Adicionar “Chinês (simplificado)”; alterne com Win + Espaço.",
    "lang_js": ROOT / "lang.js", "alphabet_html": ROOT / "alphabet.html",
}

TONE_MARKS = {"̄": 1, "́": 2, "̌": 3, "̀": 4}
MARK_OF = {1: "̄", 2: "́", 3: "̌", 4: "̀"}
TONE_NAMES = {1: "1º tom (alto e reto)", 2: "2º tom (sobe)", 3: "3º tom (desce e sobe)", 4: "4º tom (desce)", 0: "tom neutro"}


def has_hanzi(text: str) -> bool:
    return any(is_hanzi(ch) for ch in text)


def tone_of(syllable: str) -> int:
    for ch in unicodedata.normalize("NFD", syllable):
        if ch in TONE_MARKS:
            return TONE_MARKS[ch]
    return 0


def plain(py: str) -> str:
    """Pinyin sem tons (ü vira u): para aceitar respostas digitadas sem acento."""
    out = "".join(ch for ch in unicodedata.normalize("NFD", py) if ch not in TONE_MARKS)
    return unicodedata.normalize("NFC", out).replace("ü", "u").replace("ü", "u")


def retone(syllable: str, tone: int) -> str:
    """Troca o tom de UMA sílaba: a marca vai em a/e, no o de “ou”, senão na última vogal."""
    base = unicodedata.normalize("NFC", "".join(ch for ch in unicodedata.normalize("NFD", syllable) if ch not in TONE_MARKS))
    if tone == 0:
        return base
    if "a" in base:
        pos = base.index("a")
    elif "e" in base:
        pos = base.index("e")
    elif "ou" in base:
        pos = base.index("o")
    else:
        pos = max(base.rfind(v) for v in "iouü")
    if pos < 0:
        return syllable
    return unicodedata.normalize("NFC", base[:pos + 1] + MARK_OF[tone] + base[pos + 1:])


def accept(answer: str) -> list[str]:
    """Respostas aceitas ao digitar: caracteres, pinyin com tons e sem tons."""
    if not has_hanzi(answer):
        return [answer]
    py = pinyin(answer)
    return list(dict.fromkeys([answer, py, plain(py), plain(py).replace("u", "v") if "ü" in py else plain(py)]))


def pick(rng, pool, exclude, n=3):
    pool = [p for p in dict.fromkeys(pool) if p not in exclude]
    rng.shuffle(pool)
    return pool[:n]


def build():
    rng = random.Random(20261024)
    questions = []

    def add(prefix, module, level, theme, prompt, text, answers, distractors, explanation, audio=None, roman=None, slots=None):
        answers = list(dict.fromkeys(answers))
        distractors = [d for d in dict.fromkeys(distractors) if d not in answers]
        assert len(distractors) >= 1, (prefix, text)
        serial = sum(1 for q in questions if q["id"].startswith(prefix)) + 1
        question = {"id": f"{prefix}{serial:04d}", "module": module, "level": level, "theme": theme, "prompt": prompt, "text": text,
                    "answers": answers, "distractors": distractors, "explanation": explanation, "audio": audio, "roman": roman}
        if slots:
            question["slots"] = slots
        questions.append(question)

    def slot(right, wrong, label):
        return {"answers": accept(right), "distractors": [w for w in dict.fromkeys(wrong) if w != right], "label": label}

    single = [(hz, py, pt) for hz, py, pt, _, _ in C.VOCAB if len(hz) == 1 and " " not in py]

    # ---------------------------------------------------------- tons
    names = list(TONE_NAMES.values())[:4]
    for hz, py, pt in single:
        t = tone_of(py)
        if not t:
            continue
        add("zt", "tons", 1, "tons", f"Qual é o tom de {py} ({hz} = {pt})?", py, [TONE_NAMES[t]], [n for n in names if n != TONE_NAMES[t]],
            f"{py}: {TONE_NAMES[t]}. Ouça e repita imitando a curva do tom.", audio=hz)
        variants = [retone(py, k) for k in (1, 2, 3, 4)]
        add("zt", "tons", 1, "tons", f"Qual destas sílabas tem o {TONE_NAMES[t]}?", plain(py), [py], [v for v in variants if v != py],
            f"A marca sobre a vogal indica o tom: ˉ 1º, ˊ 2º, ˇ 3º, ˋ 4º. {hz} = {py}.", audio=hz)

    # ---------------------------------------------------------- pinyin (leitura)
    for hz, py, pt, theme, level in C.VOCAB:
        others = [p for _, p, _, th, _ in C.VOCAB if th == theme and p != py]
        if len(hz) == 1 and " " not in py:
            # uma sílaba: distratores com o mesmo som em outros tons
            wrong = [v for v in (retone(py, k) for k in (1, 2, 3, 4)) if v != py][:2] + pick(rng, others, [py], 1)
        else:
            wrong = pick(rng, others, [py])
        add("zp", "pinyin", level, theme, "Como se lê?", hz, [py], wrong, f"{hz} lê-se {py} ({pt}).", audio=hz)

    # ---------------------------------------------------------- vocabulário
    by_theme = {}
    for hz, py, pt, theme, level in C.VOCAB:
        by_theme.setdefault(theme, []).append((hz, py, pt))
    for hz, py, pt, theme, level in C.VOCAB:
        same = by_theme[theme]
        add("zv", "vocabulario", level, theme, "O que significa?", hz, [pt], pick(rng, [p for _, _, p in same], [pt]), f"{hz} ({py}) = {pt}.", audio=hz)
        add("zv", "vocabulario", level, theme, "Como se diz em chinês?", pt, [hz], pick(rng, [h for h, _, p in same if p != pt], [hz]), f"“{pt}” = {hz} ({py}).", audio=hz)

    # ---------------------------------------------------------- escuta
    listen = [v for v in C.VOCAB][:120]
    for hz, py, pt, theme, level in listen:
        same = [h for h, _, p in by_theme[theme] if p != pt]
        add("zl", "escuta", level, theme, "Ouça e escolha a palavra que você ouviu.", "🔊", [hz], pick(rng, same, [hz]), f"Você ouviu {hz} ({py}) = {pt}.", audio=hz)

    # ---------------------------------------------------------- classificadores
    for i, (noun, cl, clpy, why) in enumerate(C.MEASURES):
        for num, numpy in (C.NUMBERS_CL[i % 4], C.NUMBERS_CL[(i + 2) % 4]):
            bad = [m for m in C.MEASURE_SET if m != cl and m not in C.MEASURE_ALSO.get(noun, set())]
            add("zm", "classificadores", 1 if cl in "个本杯张" else 2, "classificadores", "Complete com o classificador.", f"{num}___{noun}",
                [cl], pick(rng, bad, [cl]), f"{cl} ({clpy}) é usado para {why}: {num}{cl}{noun}.", audio=f"{num}{cl}{noun}")

    # ---------------------------------------------------------- gramática
    for text, right, wrong, why, level, theme in C.GRAMMAR:
        add("zg", "gramatica", level, theme, "Complete a frase.", text, [right], wrong, why, audio=text.replace("___", right))

    # ---------------------------------------------------------- completar (2–3 lacunas)
    zai = lambda: slot("在", ["是", "有", "和"], "lugar da ação (在)")
    for place, verb, obj, cl in C.COMBO_ACTIVITIES:
        for k, (subj, _) in enumerate(C.COMBO_SUBJECTS):
            num = C.NUMBERS_CL[k % 4][0]
            bad_cl = [m for m in C.MEASURE_SET if m != cl and m not in C.MEASURE_ALSO.get(obj, set())]
            cl_slot = slot(cl, pick(rng, bad_cl, [cl]), "classificador")
            full = f"{subj}在{place}{verb}{obj}吗？"
            add("zc", "completar", 1, "pergunta", "Complete as duas lacunas (lugar e pergunta).", f"{subj}___{place}{verb}{obj}___？",
                ["在 · 吗"], ["-"], f"在 + lugar vem antes do verbo; 吗 no fim transforma a frase em pergunta de sim/não. {full}",
                audio=full, slots=[zai(), slot("吗", ["的", "得", "很"], "pergunta")])
            full = f"昨天{subj}在{place}{verb}了{num}{cl}{obj}。"
            add("zc", "completar", 2, "classificadores", "Complete as duas lacunas (lugar e classificador).", f"昨天{subj}___{place}{verb}了{num}___{obj}。",
                [f"在 · {cl}"], ["-"], f"在 + lugar antes do verbo; {cl} é o classificador de {obj}. {full}", audio=full, slots=[zai(), cl_slot])
            full = f"昨天{subj}在{place}{verb}了{num}{cl}{obj}。"
            add("zc", "completar", 2, "passado", "Complete as três lacunas (lugar, ação concluída e classificador).", f"昨天{subj}___{place}{verb}___{num}___{obj}。",
                [f"在 · 了 · {cl}"], ["-"], f"在 + lugar; 了 depois do verbo marca a ação concluída; {cl} para {obj}. {full}",
                audio=full, slots=[zai(), slot("了", ["着", "的", "得"], "ação concluída"), dict(cl_slot)])

    # ---------------------------------------------------------- números
    for right, pt, wrong in C.NUMBERS:
        add("zn", "numeros", 1, "números", f"Como se diz “{pt}”?", pt, [right], wrong, f"{pt} = {right} ({pinyin(right)}).", audio=right)

    # ---------------------------------------------------------- frases
    for hz, py, pt, ctx in C.PHRASES:
        others_pt = [p for _, _, p, _ in C.PHRASES if p != pt]
        others_hz = [h for h, _, p, _ in C.PHRASES if h != hz]
        note = f" ({ctx})" if ctx else ""
        add("zf", "frases", 1, "frases", "O que significa?", hz, [pt], pick(rng, others_pt, [pt]), f"{hz} ({py}) = {pt}{note}.", audio=hz)
        add("zf", "frases", 1, "frases", "Como se diz em chinês?", pt, [hz], pick(rng, others_hz, [hz]), f"{pt} = {hz} ({py}){note}.", audio=hz)

    # Digitação: aceitar pinyin com e sem tons onde a resposta é em caracteres.
    for q in questions:
        if not q.get("slots") and has_hanzi(q["answers"][0]):
            q["answers"] = accept(q["answers"][0])
    return questions


def validate(questions):
    ids = [q["id"] for q in questions]
    assert len(ids) == len(set(ids)), "IDs repetidos"
    for q in questions:
        assert q["answers"] and q["distractors"], q["id"]
        assert not set(q["answers"]) & set(q["distractors"]), q["id"]
        if q.get("slots"):
            assert q["text"].count("___") == len(q["slots"]) >= 2, q["id"]
            for s in q["slots"]:
                assert not set(s["answers"]) & set(s["distractors"]), q["id"]
        elif "___" in q["text"]:
            assert q["text"].count("___") == 1, q["id"]
    # 个 nunca é distrator de classificador (é o classificador geral, aceito na fala).
    for q in questions:
        if q["module"] == "classificadores":
            assert "个" not in q["distractors"], q["id"]


def listen_choice(questions):
    items = []
    for q in questions:
        if q["module"] not in ("gramatica", "classificadores") or q["text"].count("___") != 1:
            continue
        answer = q["text"].replace("___", q["answers"][0])
        options = list(dict.fromkeys([answer] + [q["text"].replace("___", d) for d in q["distractors"][:3]]))
        if len(options) >= 3:
            items.append({"answer": answer, "options": options, "explanation": q["explanation"]})
    return items


def roman_map(questions, extra=()):
    out = {}
    for q in questions:
        options = [q["answers"][0]] + q["distractors"]
        for s in q.get("slots", []):
            options += [s["answers"][0]] + s["distractors"]
        for o in options:
            if has_hanzi(o) and o not in out and q["module"] != "pinyin":
                out[o] = pinyin(o)
    for o in extra:
        out.setdefault(o, pinyin(o))
    return out


MODULES = {
    "tons": "Tons", "pinyin": "Pinyin (leitura)", "vocabulario": "Vocabulário", "escuta": "Escuta",
    "classificadores": "Classificadores", "gramatica": "Gramática", "completar": "Completar frases (2–3 lacunas)",
    "numeros": "Números, horas e dinheiro", "frases": "Frases do dia a dia",
}


def main():
    questions = build()
    validate(questions)
    choice = listen_choice(questions)
    data = {
        "questions": questions, "modules": MODULES, "guide": C.GUIDE,
        "tones": C.TONES, "initials": C.INITIALS, "finals": C.FINALS,
        "roman": roman_map(questions, [o for item in choice for o in item["options"]]),
    }
    data["skills"], _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, choice, pinyin)
    build_app(PAGE, data, PUBLIC / "chinese.html")
    counts = {}
    for q in questions:
        counts[q["module"]] = counts.get(q["module"], 0) + 1
    print(f"chinese.html: {len(questions)} questões", counts)


if __name__ == "__main__":
    main()
