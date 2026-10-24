"""Gera public/japanese.html (Japanese Routine) a partir de content.py + practice/ + skills/.

Rode: python japanese/build_japanese.py
IDs são estáveis (prefixo por módulo + ordem fixa) para preservar o histórico.
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

import content as C
import extend
import kana as K
import readings as R
import skills_content as SK

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT.parent / "public"
sys.path.insert(0, str(ROOT.parent))
from practice.build import build_app  # noqa: E402
from skills.build import skills_bundle  # noqa: E402

PAGE = {
    "code": "ja", "html_lang": "ja", "brand": "Japanese Routine", "brand_word": "japanese", "name": "japonês",
    "alphabet_tab": "Hiragana e katakana", "eyebrow": "Japonês todos os dias · JLPT N5–N4", "headline": "こんにちは！Vamos treinar.",
    "intro": "questões de hiragana, katakana, leitura de kanji, vocabulário, partículas, verbos, adjetivos, frases para completar, números e escuta. Responda escolhendo ou digitando em kana ou romaji.",
    "level_prefix": "N", "level1": "N5", "level2": "N4", "typing_label": "Digitar (kana ou romaji)",
    "typing_hint": "Digite em kana com o teclado japonês ou direto em romaji: “wa” vale para は. No Windows: Configurações › Hora e idioma › Idioma › Adicionar “Japonês”; alterne com Win + Espaço.",
    "lang_js": ROOT / "lang.js", "alphabet_html": ROOT / "alphabet.html",
}


def load_readings():
    entries = [(w, k) for w, k, *_ in C.VOCAB]
    for dic, stem, stem_kana, te, *_ in C.VERBS:
        entries.append((stem, stem_kana))
        entries.append((te, R.TE[te]))
    for adj, kind, *_ in C.ADJECTIVES:
        reading = next((k for w, k, *_ in C.VOCAB if w == adj), adj)
        if kind == "i" and adj != reading:
            entries.append((adj[:-1], reading[:-1]))
    # frases só em kana: leitura = texto (sem a pontuação final)
    entries += [(p.rstrip("！？"), p.rstrip("！？")) for p, *_ in C.PHRASES if not any(K.is_kanji(c) for c in p)]
    entries += list(R.EXTRA.items())
    K.add_readings([(w, k) for w, k in entries if k])


def accept(answer: str) -> list[str]:
    """Respostas aceitas ao digitar: original, kana e romaji (com e sem espaços)."""
    if not any(K.is_kana(c) or K.is_kanji(c) for c in answer):
        return [answer]
    rom = K.romaji(answer).rstrip(".!?")
    return list(dict.fromkeys([answer, K.reading(answer), rom, rom.replace(" ", "")]))


def pick(rng, pool, exclude, n=3):
    pool = [p for p in dict.fromkeys(pool) if p not in exclude]
    rng.shuffle(pool)
    return pool[:n]


def build():
    rng = random.Random(20261024)
    questions = []

    def add(prefix, module, level, theme, prompt, text, answers, distractors, explanation, audio=None, slots=None):
        answers = list(dict.fromkeys(answers))
        distractors = [d for d in dict.fromkeys(distractors) if d not in answers]
        assert len(distractors) >= 1, (prefix, text)
        serial = sum(1 for q in questions if q["id"].startswith(prefix)) + 1
        q = {"id": f"{prefix}{serial:04d}", "module": module, "level": level, "theme": theme, "prompt": prompt, "text": text,
             "answers": answers, "distractors": distractors, "explanation": explanation, "audio": audio, "roman": None}
        if slots:
            q["slots"] = slots
        questions.append(q)

    def slot(right, wrong, label):
        return {"answers": accept(right), "distractors": [w for w in dict.fromkeys(wrong) if w != right], "label": label}

    # ---------------------------------------------------------- hiragana e katakana
    basic = K.HIRAGANA + K.DAKUTEN + K.YOON
    sounds = [r for _, r in basic]
    for module, convert, label in (("hiragana", lambda x: x, "hiragana"), ("katakana", K.kata, "katakana")):
        chars = [convert(k) for k, _ in basic]
        for k, r in basic:
            if k in ("ぢ", "づ", "を"):
                continue  # mesmo som de じ/ず/お: ambíguo como pergunta
            ch = convert(k)
            add("jk" if module == "hiragana" else "jt", module, 1, label, f"Como se lê este {label}?", ch, [r], pick(rng, sounds, [r]),
                f"{ch} = {r}.", audio=ch)
            add("jk" if module == "hiragana" else "jt", module, 1, label, f"Qual {label} tem o som “{r}”?", r, [ch], pick(rng, chars, [ch]),
                f"“{r}” em {label}: {ch}.", audio=ch)

    # ---------------------------------------------------------- leitura de kanji
    kanji_words = [(w, k, pt, th, lv) for w, k, pt, th, lv in C.VOCAB if any(K.is_kanji(c) for c in w)]
    for w, k, pt, theme, level in kanji_words:
        others = [kk for ww, kk, *_ in kanji_words if kk != k]
        add("jr", "leitura", level, theme, "Como se lê?", w, [k], pick(rng, others, [k]), f"{w} lê-se {k} ({K.romaji(w)}) = {pt}.", audio=w)

    # ---------------------------------------------------------- vocabulário
    by_theme = {}
    for w, k, pt, theme, level in C.VOCAB:
        by_theme.setdefault(theme, []).append((w, pt))
    for w, k, pt, theme, level in C.VOCAB:
        same = by_theme[theme]
        add("jv", "vocabulario", level, theme, "O que significa?", w, [pt], pick(rng, [p for _, p in same], [pt]), f"{w} ({k}) = {pt}.", audio=w)
        add("jv", "vocabulario", level, theme, "Como se diz em japonês?", pt, accept(w), pick(rng, [x for x, p in same if p != pt], [w]),
            f"“{pt}” = {w} ({k}).", audio=w)

    # ---------------------------------------------------------- escuta
    for w, k, pt, theme, level in C.VOCAB[:120]:
        same = [x for x, p in by_theme[theme] if p != pt]
        add("jl", "escuta", level, theme, "Ouça e escolha a palavra que você ouviu.", "🔊", accept(w), pick(rng, same, [w]), f"Você ouviu {w} ({k}) = {pt}.", audio=w)

    # ---------------------------------------------------------- partículas
    for text, right, wrong, why, level in C.PARTICLES:
        add("jp", "particulas", level, "partículas", "Complete com a partícula.", text, accept(right), wrong, why, audio=text.replace("___", right))

    # ---------------------------------------------------------- verbos
    for dic, stem, stem_kana, te, pt, comp, level in C.VERBS:
        forms = {"ます": stem + "ます", "ません": stem + "ません", "ました": stem + "ました", "ませんでした": stem + "ませんでした", "たい": stem + "たいです"}
        all_forms = list(forms.values())
        cases = [("毎日", forms["ます"], f"Presente educado de {dic} ({pt}).", "Hábito (毎日) → radical + ます."),
                 ("昨日", forms["ました"], f"Passado de {dic} ({pt}).", "Ontem (昨日) → radical + ました."),
                 ("明日は", forms["ません"], f"Negativo de {dic} ({pt}): “não vou …”.", "Negativo educado → radical + ません."),
                 ("昨日は", forms["ませんでした"], f"Passado negativo de {dic} ({pt}).", "Passado negativo → radical + ませんでした."),
                 ("今度", forms["たい"], f"Diga “quero {pt}” ({dic}).", "Querer → radical + たいです.")]
        for time, right, prompt, why in cases:
            text = f"{time}{comp}___。"
            add("jg", "verbos", level if time in ("毎日", "昨日") else 2, "verbos", prompt, text, accept(right), [f for f in all_forms if f != right] + [dic],
                why, audio=f"{time}{comp}{right}。")
        te_wrong = [stem + "て", stem + "って", stem + "んで", dic + "て"]
        add("jg", "verbos", 2, "forma -te", f"Forma -te de {dic} ({pt}): “por favor, …”.", f"{comp}___ください。", accept(te), te_wrong,
            f"{dic} → {te}. A forma -te + ください faz um pedido educado.", audio=f"{comp}{te}ください。")

    # ---------------------------------------------------------- adjetivos
    for adj, kind, subj, pt in C.ADJECTIVES:
        if kind == "i":
            base, neg, past = adj, adj[:-1] + "くないです", adj[:-1] + "かったです"
            wrong_neg, wrong_past = [adj + "じゃないです", adj + "くないです", adj[:-1] + "でした"], [adj + "でした", adj + "かったです", adj[:-1] + "だった"]
        else:
            base, neg, past = adj, adj + "じゃないです", adj + "でした"
            wrong_neg, wrong_past = [adj + "くないです", adj + "ないです", adj + "じゃなかったです"], [adj + "かったです", adj + "だったです", adj + "くでした"]
        add("ja", "adjetivos", 1, "adjetivos", f"Negativo de {adj} ({pt}).", f"{subj}___。", accept(neg), wrong_neg,
            f"Adjetivo {'い: troca い por くない' if kind == 'i' else 'な: + じゃない'} → {neg}.", audio=f"{subj}{neg}")
        past_subj = "昨日は" if subj == "今日は" else subj
        add("ja", "adjetivos", 2, "adjetivos", f"Passado de {adj} ({pt}).", f"{past_subj}___。",
            accept(past), wrong_past, f"Adjetivo {'い: troca い por かった' if kind == 'i' else 'な: + でした'} → {past}.", audio=f"{past_subj}{past}")

    # ---------------------------------------------------------- completar (2–3 lacunas)
    def wa():
        return slot("は", ["を", "で", "に"], "tópico")
    for place, obj, stem in C.COMBO_ACTIVITIES:
        for subj in C.COMBO_SUBJECTS:
            full = f"{subj}は{place}で{obj}を{stem}ます。"
            add("jc", "completar", 1, "partículas", "Complete as três partículas (tópico, lugar da ação e objeto).", f"{subj}___{place}___{obj}___{stem}ます。",
                ["は · で · を"], ["-"], f"は marca o tópico; で, o lugar onde a ação acontece; を, o objeto. {full}", audio=full,
                slots=[wa(), slot("で", ["に", "を", "へ"], "lugar da ação"), slot("を", ["で", "に", "へ"], "objeto")])
            full = f"{subj}は{place}に行きます。"
            add("jc", "completar", 1, "destino", "Complete as duas partículas (tópico e destino).", f"{subj}___{place}___行きます。",
                ["は · に"], ["-"], f"は = tópico; に (ou へ) = destino com verbos de movimento. {full}", audio=full,
                slots=[wa(), slot("に", ["で", "を", "の"], "destino")])
            past = f"{stem}ました"
            full = f"昨日、{subj}は{place}で{obj}を{past}。"
            add("jc", "completar", 2, "passado", "Complete as três lacunas (lugar, objeto e verbo no passado).", f"昨日、{subj}は{place}___{obj}______。",
                [f"で · を · {past}"], ["-"], f"で = lugar da ação; を = objeto; 昨日 pede passado: {past}. {full}", audio=full,
                slots=[slot("で", ["に", "を", "へ"], "lugar da ação"), slot("を", ["で", "に", "へ"], "objeto"),
                       slot(past, [f"{stem}ます", f"{stem}ません", f"{stem}たいです"], "verbo no passado")])

    # ---------------------------------------------------------- números
    for word, kana_r, wrong in C.NUMBERS:
        add("jn", "numeros", 1, "números", "Como se lê?", word, accept(kana_r), wrong, f"{word} = {kana_r} ({K._romaji_kana(kana_r)}).", audio=word)

    # ---------------------------------------------------------- frases
    for ja, pt, ctx in C.PHRASES:
        note = f" ({ctx})" if ctx else ""
        add("jf", "frases", 1, "frases", "O que significa?", ja, [pt], pick(rng, [p for _, p, _ in C.PHRASES if p != pt], [pt]), f"{ja} = {pt}{note}.", audio=ja)
        add("jf", "frases", 1, "frases", "Como se diz em japonês?", pt, accept(ja), pick(rng, [j for j, p, _ in C.PHRASES if p != pt], [ja]), f"{pt} = {ja}{note}.", audio=ja)

    # Expansão (~10 mil): sempre depois das originais, com prefixos novos.
    extend.build_more(add, slot, accept, pick, rng, C, K)
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
                assert s["distractors"] and not set(s["answers"]) & set(s["distractors"]), q["id"]
        elif "___" in q["text"]:
            assert q["text"].count("___") == 1, q["id"]


def listen_choice(questions):
    items = []
    for q in questions:
        if q["module"] not in ("particulas", "verbos", "adjetivos") or q.get("slots") or q["text"].count("___") != 1:
            continue
        answer = q["text"].replace("___", q["answers"][0])
        options = list(dict.fromkeys([answer] + [q["text"].replace("___", d) for d in q["distractors"][:3]]))
        if len(options) >= 3:
            items.append({"answer": answer, "options": options, "explanation": q["explanation"]})
    return items


def roman_map(questions, extra=()):
    out = {}
    for q in questions:
        if q["module"] in ("hiragana", "katakana", "leitura", "numeros"):
            continue  # ali o som/leitura é a própria resposta
        options = [q["answers"][0]] + q["distractors"]
        for s in q.get("slots", []):
            options += [s["answers"][0]] + s["distractors"]
        for o in options:
            if any(K.is_kana(c) or K.is_kanji(c) for c in o) and o not in out:
                out[o] = K.romaji(o)
    for o in extra:
        out.setdefault(o, K.romaji(o))
    return out


MODULES = {
    "hiragana": "Hiragana", "katakana": "Katakana", "leitura": "Leitura de kanji", "vocabulario": "Vocabulário", "escuta": "Escuta",
    "particulas": "Partículas", "verbos": "Verbos (-masu e -te)", "adjetivos": "Adjetivos い e な", "completar": "Completar frases (2–3 lacunas)",
    "numeros": "Números e contadores", "frases": "Frases do dia a dia",
}


def main():
    load_readings()
    questions = build()
    validate(questions)
    choice = listen_choice(questions)
    data = {"questions": questions, "modules": MODULES, "guide": C.GUIDE,
            "hiragana": K.HIRAGANA + K.DAKUTEN, "roman": roman_map(questions, [o for i in choice for o in i["options"]])}
    data["skills"], _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, choice, K.romaji)
    build_app(PAGE, data, PUBLIC / "japanese.html")
    counts = {}
    for q in questions:
        counts[q["module"]] = counts.get(q["module"], 0) + 1
    print(f"japanese.html: {len(questions)} questões", counts)


if __name__ == "__main__":
    main()
