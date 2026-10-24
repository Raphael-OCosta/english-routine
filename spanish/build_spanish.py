"""Gera public/spanish.html (Spanish Routine) a partir de content.py + practice/ + skills/.

Rode: python spanish/build_spanish.py
IDs são estáveis (prefixo por módulo + ordem fixa) para preservar o histórico.
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

import content as C
import extend
import skills_content as SK

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT.parent / "public"
sys.path.insert(0, str(ROOT.parent))
from practice.build import build_app  # noqa: E402
from skills.build import skills_bundle  # noqa: E402

PAGE = {
    "code": "es", "html_lang": "es", "brand": "Spanish Routine", "brand_word": "spanish", "name": "espanhol",
    "alphabet_tab": "Pronúncia", "eyebrow": "Espanhol todos os dias · A1–A2", "headline": "¡Hola! Vamos treinar.",
    "intro": "questões de vocabulário, falsos amigos, verbos, gramática, frases para completar, números, frases e escuta — pensadas para quem fala português.",
    "level_prefix": "A", "level1": "A1", "level2": "A2", "typing_label": "Digitar em espanhol",
    "typing_hint": "Digite com os acentos (á, é, í, ó, ú, ñ): no espanhol eles mudam o sentido (hablo × habló). No celular, segure a letra para escolher o acento.",
    "lang_js": ROOT / "lang.js", "alphabet_html": ROOT / "alphabet.html",
}
# Frases com “ayer” que não fazem sentido no passado (ayer tuve dos hermanos…).
NO_PAST = {"ser", "tener", "vivir", "querer"}
PERSONS = ["yo", "tú", "él", "nosotros", "vosotros", "ellos"]
ENDINGS_PRESENT = {"ar": ["o", "as", "a", "amos", "áis", "an"], "er": ["o", "es", "e", "emos", "éis", "en"], "ir": ["o", "es", "e", "imos", "ís", "en"]}
ENDINGS_PAST = {"ar": ["é", "aste", "ó", "amos", "asteis", "aron"], "er": ["í", "iste", "ió", "imos", "isteis", "ieron"], "ir": ["í", "iste", "ió", "imos", "isteis", "ieron"]}


def present(verb: str, person: int) -> str:
    if verb in C.IRREGULAR_PRESENT:
        return C.IRREGULAR_PRESENT[verb][person]
    return verb[:-2] + ENDINGS_PRESENT[verb[-2:]][person]


def past(verb: str, person: int) -> str:
    if verb in C.IRREGULAR_PAST:
        return C.IRREGULAR_PAST[verb][person]
    if person == 0 and verb[-3:] in ("car", "gar", "zar"):  # sacar → saqué, pagar → pagué, cruzar → crucé
        return verb[:-3] + {"car": "qué", "gar": "gué", "zar": "cé"}[verb[-3:]]
    return verb[:-2] + ENDINGS_PAST[verb[-2:]][person]


def article(gender: str) -> str:
    return "el" if gender == "m" else "la"


def to_place(gender: str) -> str:
    return "al" if gender == "m" else "a la"


def pick(rng, pool, exclude, n=3):
    pool = [p for p in dict.fromkeys(pool) if p not in exclude]
    rng.shuffle(pool)
    return pool[:n]


def build():
    rng = random.Random(20261024)
    questions = []

    def add(prefix, module, level, theme, prompt, text, answers, distractors, explanation, audio=None, slots=None, typeable=False):
        answers = list(dict.fromkeys(answers))
        distractors = [d for d in dict.fromkeys(distractors) if d not in answers]
        assert len(distractors) >= 1, (prefix, text)
        serial = sum(1 for q in questions if q["id"].startswith(prefix)) + 1
        q = {"id": f"{prefix}{serial:04d}", "module": module, "level": level, "theme": theme, "prompt": prompt, "text": text,
             "answers": answers, "distractors": distractors, "explanation": explanation, "audio": audio, "roman": None, "typeable": typeable}
        if slots:
            q["slots"] = slots
        questions.append(q)

    def slot(right, wrong, label):
        return {"answers": [right], "distractors": [w for w in dict.fromkeys(wrong) if w != right], "label": label}

    # ---------------------------------------------------------- vocabulário
    by_theme = {}
    for es, pt, theme, level in C.VOCAB:
        by_theme.setdefault(theme, []).append((es, pt))
    for es, pt, theme, level in C.VOCAB:
        same = by_theme[theme]
        add("ev", "vocabulario", level, theme, "O que significa?", es, [pt], pick(rng, [p for _, p in same], [pt]), f"{es} = {pt}.", audio=es)
        bare = es.split(" ", 1)[1] if es.split(" ")[0] in ("el", "la", "los", "las") else es  # digitar sem artigo também vale
        add("ev", "vocabulario", level, theme, "Como se diz em espanhol?", pt, [es, bare], pick(rng, [e for e, p in same if p != pt], [es, bare]),
            f"“{pt}” = {es}.", audio=es, typeable=True)

    # ---------------------------------------------------------- escuta
    for es, pt, theme, level in C.VOCAB[:120]:
        same = [e for e, p in by_theme[theme] if p != pt]
        add("el", "escuta", level, theme, "Ouça e escolha a palavra que você ouviu.", "🔊", [es], pick(rng, same, [es]), f"Você ouviu {es} ({pt}).", audio=es)

    # ---------------------------------------------------------- falsos amigos
    meanings = [m for _, m, _ in C.FALSE_FRIENDS]
    for es, real, trap in C.FALSE_FRIENDS:
        others = pick(rng, meanings, [real], 2)
        add("ef", "falsos", 1, "falsos amigos", "Cuidado com o falso amigo: o que significa?", es, [real], [trap] + others,
            f"{es} = {real} (não “{trap}”).", audio=es)

    # ---------------------------------------------------------- verbos
    for verb, pt, comp, level in C.VERBS:
        for k, (subj, person) in enumerate(C.SUBJECTS):
            if (k + len(verb)) % 2:  # metade das pessoas por verbo, para variar sem repetir demais
                continue
            right = present(verb, person)
            wrong = [present(verb, p) for p in (0, 1, 2, 3, 5) if p != person] + [verb]
            add("eg", "verbos", level, "presente", f"Presente de {verb} ({pt}).", f"{subj.capitalize()} ___ {comp}.", [right], pick(rng, wrong, [right]),
                f"{verb} com {subj} no presente → {right}.", audio=f"{subj.capitalize()} {right} {comp}.", typeable=True)
            if verb in NO_PAST:
                continue
            pright = past(verb, person)
            pwrong = [past(verb, p) for p in (0, 1, 2, 3, 5) if p != person] + [present(verb, person)]
            add("eg", "verbos", 2, "pretérito", f"Pretérito indefinido de {verb} ({pt}).", f"Ayer {subj} ___ {comp}.", [pright], pick(rng, pwrong, [pright]),
                f"Ayer pede pretérito indefinido: {subj} → {pright}.", audio=f"Ayer {subj} {pright} {comp}.", typeable=True)

    # ---------------------------------------------------------- gramática
    for text, right, wrong, why, level, theme in C.GRAMMAR:
        add("eq", "gramatica", level, theme, "Complete a frase.", text, [right], wrong, why, audio=text.replace("___", right), typeable=True)

    # ---------------------------------------------------------- completar (2–3 lacunas)
    for verb, obj, og, place, pg in C.COMBO_ACTIVITIES:
        for subj, person in C.COMBO_SUBJECTS:
            conj = present(verb, person)
            s1 = slot(conj, [present(verb, p) for p in (0, 1, 2, 3, 5) if p != person], f"{verb} no presente")
            s2 = slot(article(og), ["el", "la", "los", "las"], "artigo")
            full = f"{subj} {conj} {article(og)} {obj}."
            add("ec", "completar", 1, "presente", f"Complete as duas lacunas (verbo {verb} e artigo).", f"{subj} ___ ___ {obj}.",
                [f"{conj} · {article(og)}"], ["-"], f"{subj} → {conj}; {obj} é {'masculino' if og == 'm' else 'feminino'} → {article(og)}.",
                audio=full, slots=[s1, s2], typeable=True)
            pconj = past(verb, person)
            s1 = slot(pconj, [past(verb, p) for p in (0, 1, 2, 3, 5) if p != person] + [conj], f"{verb} no pretérito")
            s3 = slot(article(pg), ["el", "la", "los", "las"], "artigo do lugar")
            full = f"Ayer {subj.lower() if subj not in ('Ana y yo',) else subj} {pconj} {article(og)} {obj} en {article(pg)} {place}."
            add("ec", "completar", 2, "pretérito", f"Complete as três lacunas (verbo {verb} no passado e artigos).",
                f"Ayer {subj.lower() if subj != 'Ana y yo' else subj} ___ ___ {obj} en ___ {place}.",
                [f"{pconj} · {article(og)} · {article(pg)}"], ["-"],
                f"Ayer → pretérito: {pconj}. {obj} → {article(og)}; {place} → {article(pg)}.", audio=full,
                slots=[s1, dict(s2), s3], typeable=True)
            go = present("ir", person)
            s1 = slot(go, [present("ir", p) for p in (0, 1, 2, 3, 5) if p != person], "ir no presente")
            s4 = slot(to_place(pg), ["al", "a la", "a el", "en el"], "a + artigo")
            full = f"Mañana {subj.lower() if subj != 'Ana y yo' else subj} {go} {to_place(pg)} {place}."
            add("ec", "completar", 1, "ir a", "Complete as duas lacunas (ir e a + artigo).",
                f"Mañana {subj.lower() if subj != 'Ana y yo' else subj} ___ ___ {place}.", [f"{go} · {to_place(pg)}"], ["-"],
                f"ir com {subj.lower()} → {go}; a + {article(pg)} → {to_place(pg)}.", audio=full, slots=[s1, s4], typeable=True)

    # ---------------------------------------------------------- números e frases
    for es, pt, wrong in C.NUMBERS:
        add("en", "numeros", 1, "números", f"Como se diz “{pt}”?", pt, [es], wrong, f"{pt} = {es}.", audio=es, typeable=True)
    for es, pt, ctx in C.PHRASES:
        if es.lower() == pt.lower():
            continue  # iguais nos dois idiomas (de nada, por favor): nada a treinar
        note = f" ({ctx})" if ctx else ""
        add("ep", "frases", 1, "frases", "O que significa?", es, [pt], pick(rng, [p for _, p, _ in C.PHRASES if p != pt], [pt]), f"{es} = {pt}{note}.", audio=es)
        add("ep", "frases", 1, "frases", "Como se diz em espanhol?", pt, [es], pick(rng, [e for e, p, _ in C.PHRASES if p != pt], [es]),
            f"{pt} = {es}{note}.", audio=es, typeable=True)
    # Expansão (~10 mil): sempre depois das originais, com prefixos novos.
    extend.build_more(add, slot, pick, rng, C, present, past, article, to_place)
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
        if q["module"] not in ("verbos", "gramatica") or q.get("slots") or q["text"].count("___") != 1:
            continue
        answer = q["text"].replace("___", q["answers"][0])
        options = list(dict.fromkeys([answer] + [q["text"].replace("___", d) for d in q["distractors"][:3]]))
        if len(options) >= 3:
            items.append({"answer": answer, "options": options, "explanation": q["explanation"]})
    return items


MODULES = {
    "vocabulario": "Vocabulário", "falsos": "Falsos amigos", "escuta": "Escuta", "verbos": "Verbos (presente e passado)",
    "gramatica": "Gramática", "completar": "Completar frases (2–3 lacunas)", "numeros": "Números e horas", "frases": "Frases do dia a dia",
}


def main():
    questions = build()
    validate(questions)
    data = {"questions": questions, "modules": MODULES, "guide": C.GUIDE, "sounds": C.SOUNDS, "roman": {}}
    data["skills"], _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, listen_choice(questions))
    build_app(PAGE, data, PUBLIC / "spanish.html")
    counts = {}
    for q in questions:
        counts[q["module"]] = counts.get(q["module"], 0) + 1
    print(f"spanish.html: {len(questions)} questões", counts)


if __name__ == "__main__":
    main()
