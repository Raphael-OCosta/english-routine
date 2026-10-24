"""Gera public/french.html (French Routine) a partir de content.py + practice/ + skills/.

Rode: python french/build_french.py
IDs são estáveis (prefixo por módulo + ordem fixa) para preservar o histórico.
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

import content as C
import skills_content as SK

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT.parent / "public"
sys.path.insert(0, str(ROOT.parent))
from practice.build import build_app  # noqa: E402
from skills.build import skills_bundle  # noqa: E402

PAGE = {
    "code": "fr", "html_lang": "fr", "brand": "French Routine", "brand_word": "french", "name": "francês",
    "alphabet_tab": "Pronúncia", "eyebrow": "Francês todos os dias · A1–A2", "headline": "Bonjour ! Vamos treinar.",
    "intro": "questões de vocabulário, falsos amigos, verbos, gramática, frases para completar, números, frases e escuta — pensadas para quem fala português.",
    "level_prefix": "A", "level1": "A1", "level2": "A2", "typing_label": "Digitar em francês",
    "typing_hint": "Digite com os acentos (é, è, ê, à, ç…): no francês eles mudam a pronúncia e às vezes o sentido. No celular, segure a letra para escolher o acento.",
    "lang_js": ROOT / "lang.js", "alphabet_html": ROOT / "alphabet.html",
}
VOWELS = "aeiouéèêëàâîïôûùhy"
ER = ["e", "es", "e", "ons", "ez", "ent"]
IMP = ["ais", "ais", "ait", "ions", "iez", "aient"]
ETRE_VERBS = {"aller": "allé", "venir": "venu", "sortir": "sorti", "partir": "parti"}


def present(verb, p):
    if verb in C.PRESENT:
        return C.PRESENT[verb][p]
    return verb[:-2] + ER[p]


def participle(verb):
    return C.PARTICIPLE.get(verb) or ETRE_VERBS.get(verb) or verb[:-2] + "é"


def imparfait(verb, p):
    stem = "ét" if verb == "être" else present(verb, 3)[:-3]
    if stem.endswith("ge") and IMP[p].startswith("i"):
        stem = stem[:-1]
    return stem + IMP[p]


def vowel(word):
    return word[:1].lower() in VOWELS


def article(g):
    return {"m": "le", "f": "la", "pl": "les", "v": "l'"}[g]


def to_place(g):
    return {"m": "au", "f": "à la", "pl": "aux", "v": "à l'"}[g]


def join(a, b):
    """Junta palavras respeitando a elisão (l'avion, à l'aéroport)."""
    return f"{a}{b}" if a.endswith("'") else f"{a} {b}"


def gap(answer, word):
    """Lacuna seguida de palavra: sem espaço quando a resposta termina em apóstrofo."""
    return "___" + ("" if answer.endswith("'") else " ") + word


def low(s):
    return s if s in ("Marie", "Paul", "Lucas et moi", "Sophie et Julie") else s[0].lower() + s[1:]


def pick(rng, pool, exclude, n=3):
    pool = [p for p in dict.fromkeys(pool) if p not in exclude]
    rng.shuffle(pool)
    return pool[:n]


def build():
    rng = random.Random(20261025)
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

    def art_slot(g):
        return slot(article(g), ["le", "la", "les", "l'"], "artigo")

    persons = (0, 1, 2, 3, 4, 5)

    # ---------------------------------------------------------- vocabulário e escuta
    by_theme = {}
    for fr, pt, theme, level in C.VOCAB:
        by_theme.setdefault(theme, []).append((fr, pt))
    for fr, pt, theme, level in C.VOCAB:
        same = by_theme[theme]
        bare = fr.split(" ", 1)[1] if fr.split(" ")[0] in ("le", "la", "les") else (fr[2:] if fr.startswith("l'") else fr)
        add("fv", "vocabulario", level, theme, "O que significa?", fr, [pt], pick(rng, [p for _, p in same], [pt]), f"{fr} = {pt}.", audio=fr)
        add("fv", "vocabulario", level, theme, "Como se diz em francês?", pt, [fr, bare], pick(rng, [f for f, p in same if p != pt], [fr, bare]),
            f"“{pt}” = {fr}.", audio=fr, typeable=True)
    for fr, pt, theme, level in C.VOCAB[:150]:
        same = [f for f, p in by_theme[theme] if p != pt]
        add("fl", "escuta", level, theme, "Ouça e escolha a palavra que você ouviu.", "🔊", [fr], pick(rng, same, [fr]), f"Você ouviu {fr} ({pt}).", audio=fr)

    # ---------------------------------------------------------- falsos amigos
    meanings = [m for _, m, _ in C.FALSE_FRIENDS]
    for fr, real, trap in C.FALSE_FRIENDS:
        add("ff", "falsos", 1, "falsos amigos", "Cuidado com o falso amigo: o que significa?", fr, [real], [trap] + pick(rng, meanings, [real], 2),
            f"{fr} = {real} (não “{trap}”).", audio=fr)

    # ---------------------------------------------------------- verbos (todas as pessoas)
    subj_txt = ["je", "tu", "il", "nous", "vous", "ils"]
    no_past = {"avoir", "être", "connaître", "savoir", "vouloir", "habiter"}
    for verb, pt, comp, level in C.VERBS:
        for p in persons:
            for tense, answer, why, lvl in (
                ("presente", present(verb, p), "Presente.", level),
                ("imparfait", imparfait(verb, p), "Hábito no passado (avant, toujours) → imparfait.", 2),
                ("futur proche", f"{present('aller', p)} {verb}", "Futur proche: aller + infinitivo.", 1),
                ("passé composé", None, "", 2),
            ):
                if tense == "passé composé":
                    if verb in no_past or (verb in ETRE_VERBS and p == 4):
                        continue
                    if verb in ETRE_VERBS:
                        part = ETRE_VERBS[verb] + ("s" if p >= 3 else "")
                        answer = f"{present('être', p)} {part}"
                        why = f"{verb} usa être e concorda com o sujeito: {answer}."
                    else:
                        answer = f"{present('avoir', p)} {participle(verb)}"
                        why = f"Passé composé: avoir + particípio ({participle(verb)})."
                s = subj_txt[p]
                lead = {"presente": "", "imparfait": "Avant, ", "futur proche": "Demain, ", "passé composé": "Hier, "}[tense]
                subj = ("j'" if vowel(answer) else "je ") if p == 0 else s + " "
                if lead == "":
                    subj = subj[0].upper() + subj[1:]
                text = f"{lead}{subj}___ {comp}."
                # Só formas que ficam erradas com o marcador de tempo da frase (sem ambiguidade).
                others = [q for q in persons if q != p]
                fp = f"{present('aller', p)} {verb}"
                wrong = {
                    "presente": [present(verb, q) for q in others][:3] + [verb, participle(verb)],
                    "imparfait": [imparfait(verb, q) for q in others][:2] + [present(verb, p), fp, verb],
                    "futur proche": [f"{present('aller', q)} {verb}" for q in others][:2] + [imparfait(verb, p), verb],
                    "passé composé": [f"{present('avoir', q)} {participle(verb)}" for q in others][:2] + [present(verb, p), fp],
                }[tense]
                add("fg", "verbos", lvl, tense, f"{tense.capitalize()} de {verb} ({pt}).", text, [answer], pick(rng, wrong, [answer]), why,
                    audio=text.replace("___", answer).replace("___ ", answer + " "), typeable=True)

    # ---------------------------------------------------------- gramática
    for text, right, wrong, why, level, theme in C.GRAMMAR:
        full = text.replace("___", right).replace("' ", "'")
        add("fq", "gramatica", level, theme, "Complete a frase.", text, [right], wrong, why, audio=full, typeable=True)

    # ---------------------------------------------------------- completar (2–3 lacunas)
    for verb, obj, og, place, pg in C.ACTIVITIES:
        pp = join(to_place(pg), place)
        art = article(og)
        art_obj = join(art, obj)
        part = participle(verb)
        for subj, p in C.SUBJECTS:
            s = low(subj)
            conj = present(verb, p)
            other = [present(verb, q) for q in persons if q != p]
            je = p == 0 and subj == "Je"
            # A presente: verbo + artigo
            if not (je and vowel(conj)):
                add("fc", "completar", 1, "presente", f"Complete as duas lacunas (verbo {verb} e artigo).", f"{subj} ___ {gap(art, obj)} {pp}.",
                    [f"{conj} · {art}"], ["-"], f"{subj} → {conj}; {obj} → {art}.", audio=f"{subj} {conj} {art_obj} {pp}.",
                    slots=[slot(conj, other, f"{verb} no presente"), art_slot(og)], typeable=True)
            # B passé composé: auxiliar + particípio + artigo
            aux = present("avoir", p)
            if not je:
                add("fc", "completar", 2, "passé composé", f"Complete as três lacunas (passé composé de {verb} e artigo).",
                    f"Hier, {s} ___ ___ {gap(art, obj)} {pp}.", [f"{aux} · {part} · {art}"], ["-"], f"avoir ({aux}) + particípio ({part}).",
                    audio=f"Hier, {s} {aux} {part} {art_obj} {pp}.",
                    slots=[slot(aux, [present("avoir", q) for q in persons if q != p] + [present("être", p)], "avoir"),
                           slot(part, [verb, conj, imparfait(verb, p)], "particípio"), art_slot(og)], typeable=True)
            # C ir a um lugar: aller + au/à la
            go = present("aller", p)
            prep = to_place(pg)
            add("fc", "completar", 1, "aller", "Complete as duas lacunas (aller e à + artigo).", f"Demain, {s} ___ {gap(prep, place)}.",
                [f"{go} · {prep}"], ["-"], f"aller → {go}; à + {article(pg)} → {prep}.", audio=f"Demain, {s} {go} {pp}.",
                slots=[slot(go, [present("aller", q) for q in persons if q != p], "aller"), slot(prep, ["au", "à la", "à l'", "aux"], "à + artigo")],
                typeable=True)
            # D futur proche
            add("fc", "completar", 1, "futur proche", f"Complete o futur proche (aller + {verb}).", f"Ce soir, {s} ___ ___ {art_obj}.",
                [f"{go} · {verb}"], ["-"], f"aller + infinitivo: {go} {verb}.", audio=f"Ce soir, {s} {go} {verb} {art_obj}.",
                slots=[slot(go, [present("aller", q) for q in persons if q != p], "aller"), slot(verb, [conj, part, imparfait(verb, p)], "infinitivo")],
                typeable=True)
            # E negação
            ne = "n'" if vowel(conj) else "ne "
            add("fc", "completar", 1, "negação", f"Complete a negação (ne … pas) com {verb}.", f"{subj} {ne}___ pas {gap(art, obj)}.",
                [f"{conj} · {art}"], ["-"], f"ne + verbo + pas; antes de vogal ne vira n'.", audio=f"{subj} {ne}{conj} pas {art_obj}.",
                slots=[slot(conj, other, f"{verb} no presente"), art_slot(og)], typeable=True)
            # F en train de
            be = present("être", p)
            de = "d'" if vowel(verb) else "de "
            add("fc", "completar", 2, "en train de", f"Complete: être en train de + {verb}.", f"Maintenant, {s} ___ en train {de}___ {art_obj}.",
                [f"{be} · {verb}"], ["-"], f"Ação em andamento: être ({be}) en train de + infinitivo (antes de vogal: d').",
                audio=f"Maintenant, {s} {be} en train {de}{verb} {art_obj}.",
                slots=[slot(be, [present("être", q) for q in persons if q != p] + [aux], "être"), slot(verb, [conj, part, imparfait(verb, p)], "infinitivo")],
                typeable=True)
            # G imparfait
            imp = imparfait(verb, p)
            if not (je and vowel(imp)):
                add("fc", "completar", 2, "imparfait", f"Complete (hábito no passado com {verb}).", f"Avant, {s} ___ toujours {gap(art, obj)} {pp}.",
                    [f"{imp} · {art}"], ["-"], f"Hábito no passado → imparfait: {imp}.", audio=f"Avant, {s} {imp} toujours {art_obj} {pp}.",
                    slots=[slot(imp, [imparfait(verb, q) for q in persons if q != p] + [conj], f"{verb} no imparfait"), art_slot(og)], typeable=True)
            # H pergunta com est-ce que
            if not (je and vowel(conj)):
                que = "Est-ce qu'" if vowel(s) else "Est-ce que "
                add("fc", "completar", 1, "pergunta", f"Complete a pergunta (verbo {verb} e artigo).", f"{que}{s} ___ {gap(art, obj)} {pp} ?",
                    [f"{conj} · {art}"], ["-"], f"Est-ce que + frase = pergunta (antes de vogal: est-ce qu').", audio=f"{que}{s} {conj} {art_obj} {pp} ?",
                    slots=[slot(conj, other, f"{verb} no presente"), art_slot(og)], typeable=True)
            # I vouloir + infinitivo
            want = present("vouloir", p)
            add("fc", "completar", 1, "vouloir", f"Complete: vouloir + {verb}.", f"{subj} ___ ___ {art_obj}.", [f"{want} · {verb}"], ["-"],
                f"vouloir ({want}) + infinitivo.", audio=f"{subj} {want} {verb} {art_obj}.",
                slots=[slot(want, [present("vouloir", q) for q in persons if q != p], "vouloir"), slot(verb, [conj, part, imparfait(verb, p)], "infinitivo")],
                typeable=True)
            # J passé composé negativo
            if not je:
                naux = f"n'{aux}"
                add("fc", "completar", 2, "passé composé", f"Complete a negação no passé composé ({verb}).", f"Hier, {s} ___ pas ___ {art_obj}.",
                    [f"{naux} · {part}"], ["-"], f"ne + auxiliar + pas + particípio: {s} {naux} pas {part}.", audio=f"Hier, {s} {naux} pas {part} {art_obj}.",
                    slots=[slot(naux, [f"n'{present('avoir', q)}" for q in persons if q != p] + [f"ne {present('être', p)}"], "ne + avoir"),
                           slot(part, [verb, conj, imp], "particípio")], typeable=True)

    # ---------------------------------------------------------- números e frases
    for fr, pt, wrong in C.NUMBERS:
        add("fn", "numeros", 1, "números", f"Como se diz “{pt}”?", pt, [fr], wrong, f"{pt} = {fr}.", audio=fr, typeable=True)
    for fr, pt, ctx in C.PHRASES:
        note = f" ({ctx})" if ctx else ""
        add("fp", "frases", 1, "frases", "O que significa?", fr, [pt], pick(rng, [p for _, p, _ in C.PHRASES if p != pt], [pt]), f"{fr} = {pt}{note}.", audio=fr)
        add("fp", "frases", 1, "frases", "Como se diz em francês?", pt, [fr], pick(rng, [f for f, p, _ in C.PHRASES if p != pt], [fr]), f"{pt} = {fr}{note}.",
            audio=fr, typeable=True)
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
        answer = q["audio"] or q["text"].replace("___", q["answers"][0])
        options = list(dict.fromkeys([answer] + [q["text"].replace("___", d) for d in q["distractors"][:3]]))
        if len(options) >= 3:
            items.append({"answer": answer, "options": options, "explanation": q["explanation"]})
    return items


MODULES = {
    "vocabulario": "Vocabulário", "falsos": "Falsos amigos", "escuta": "Escuta", "verbos": "Verbos (presente, passado, futuro)",
    "gramatica": "Gramática", "completar": "Completar frases (2–3 lacunas)", "numeros": "Números e horas", "frases": "Frases do dia a dia",
}


def main():
    questions = build()
    validate(questions)
    data = {"questions": questions, "modules": MODULES, "guide": C.GUIDE, "sounds": C.SOUNDS, "roman": {}}
    data["skills"], _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, listen_choice(questions))
    build_app(PAGE, data, PUBLIC / "french.html")
    counts = {}
    for q in questions:
        counts[q["module"]] = counts.get(q["module"], 0) + 1
    print(f"french.html: {len(questions)} questões", counts)


if __name__ == "__main__":
    main()
