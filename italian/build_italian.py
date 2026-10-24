"""Gera public/italian.html (Italian Routine) a partir de content.py + practice/ + skills/.

Rode: python italian/build_italian.py
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
    "code": "it", "html_lang": "it", "brand": "Italian Routine", "brand_word": "italian", "name": "italiano",
    "alphabet_tab": "Pronúncia", "eyebrow": "Italiano todos os dias · A1–A2", "headline": "Ciao! Vamos treinar.",
    "intro": "questões de vocabulário, falsos amigos, verbos, gramática, frases para completar, números, frases e escuta — pensadas para quem fala português.",
    "level_prefix": "A", "level1": "A1", "level2": "A2", "typing_label": "Digitar em italiano",
    "typing_hint": "Digite com os acentos (è, à, ò, ù, ì): em italiano eles mudam o sentido (è = é; e = e). No celular, segure a letra para escolher o acento.",
    "lang_js": ROOT / "lang.js", "alphabet_html": ROOT / "alphabet.html",
}
VOWELS = "aeiouàèéìòù"
ENDINGS = {"are": ["o", "i", "a", "iamo", "ate", "ano"], "ere": ["o", "i", "e", "iamo", "ete", "ono"], "ire": ["o", "i", "e", "iamo", "ite", "ono"],
           "isc": ["isco", "isci", "isce", "iamo", "ite", "iscono"]}
IMP = ["vo", "vi", "va", "vamo", "vate", "vano"]
FUT = ["ò", "ai", "à", "emo", "ete", "anno"]
A_ART = {"il": "al", "lo": "allo", "l'": "all'", "la": "alla", "i": "ai", "gli": "agli", "le": "alle"}
PLACE_GENDER = {
    "panetteria": "f", "bar": "m", "pizzeria": "f", "biblioteca": "f", "cinema": "m", "mercato": "m", "centro": "m", "stazione": "f",
    "museo": "m", "spiaggia": "f", "farmacia": "f", "posta": "f", "stadio": "m", "parco": "m", "pasticceria": "f", "karaoke": "m",
    "aeroporto": "m", "supermercato": "m", "teatro": "m", "edicola": "f", "libreria": "f", "ristorante": "m", "fermata": "f",
    "treno": "m", "albergo": "m", "campagna": "f",
}


def present(verb, p):
    if verb in C.PRESENT:
        return C.PRESENT[verb][p]
    stem, kind = verb[:-3], verb[-3:]
    ending = ENDINGS["isc" if verb in C.ISC else kind][p]
    if kind == "are" and stem.endswith(("c", "g")) and ending.startswith("i"):
        stem += "h"  # cerchi, paghiamo
    if stem.endswith("i") and ending.startswith("i"):
        ending = ending[1:]  # studi, mangiamo
    return stem + ending


def participle(verb):
    return C.PARTICIPLE.get(verb) or verb[:-3] + {"are": "ato", "ere": "uto", "ire": "ito"}[verb[-3:]]


def imperfect(verb, p):
    return C.IMPERFECT[verb][p] if verb in C.IMPERFECT else verb[:-2] + IMP[p]


def future(verb, p):
    if verb in C.FUTURE_STEM:
        stem = C.FUTURE_STEM[verb]
    elif verb.endswith("are"):
        base = verb[:-3]
        if base.endswith(("ci", "gi")):
            base = base[:-1]  # mangerò
        elif base.endswith(("c", "g")):
            base += "h"  # cercherò
        stem = base + "er"
    else:
        stem = verb[:-1]
    return stem + FUT[p]


def gerund(verb):
    return C.GERUND.get(verb) or verb[:-3] + ("ando" if verb.endswith("are") else "endo")


def article(noun, g, plural=False):
    first = noun[:1].lower()
    lo = first in "zxy" or noun[:2] in ("gn", "ps") or (first == "s" and noun[1:2] not in VOWELS)
    if g == "f":
        return "le" if plural else ("l'" if first in VOWELS else "la")
    if plural:
        return "gli" if first in VOWELS or lo else "i"
    return "l'" if first in VOWELS else ("lo" if lo else "il")


def art_wrong(art):
    """Distratores sem ambiguidade: mesmo número (singular) ou plurais + um singular do outro gênero."""
    if art in ("i", "gli", "le"):
        return [a for a in ("i", "gli", "le") if a != art] + ["il" if art == "le" else "la"]
    return [a for a in ("il", "lo", "la", "l'") if a != art]


def join(a, b):
    return f"{a}{b}" if a.endswith("'") else f"{a} {b}"


def gap(answer, word):
    return "___" + ("" if answer.endswith("'") else " ") + word


def low(s):
    return s if s.split(" ")[0] in ("Marco", "Giulia", "Anna", "Luca") else s[0].lower() + s[1:]


def pick(rng, pool, exclude, n=3):
    pool = [p for p in dict.fromkeys(pool) if p not in exclude]
    rng.shuffle(pool)
    return pool[:n]


def bare(word):
    for a in ("il ", "lo ", "la ", "i ", "gli ", "le "):
        if word.startswith(a):
            return word[len(a):]
    return word[2:] if word.startswith("l'") else word


def build():
    rng = random.Random(20261026)
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

    persons = (0, 1, 2, 3, 4, 5)

    def others(fn, p):
        return [fn(q) for q in persons if q != p]

    # ---------------------------------------------------------- vocabulário e escuta
    by_theme = {}
    for it, pt, theme, level in C.VOCAB:
        by_theme.setdefault(theme, []).append((it, pt))
    for it, pt, theme, level in C.VOCAB:
        same = by_theme[theme]
        add("iv", "vocabulario", level, theme, "O que significa?", it, [pt], pick(rng, [p for _, p in same], [pt]), f"{it} = {pt}.", audio=it)
        add("iv", "vocabulario", level, theme, "Como se diz em italiano?", pt, [it, bare(it)], pick(rng, [f for f, p in same if p != pt], [it, bare(it)]),
            f"“{pt}” = {it}.", audio=it, typeable=True)
    for it, pt, theme, level in C.VOCAB[:150]:
        same = [f for f, p in by_theme[theme] if p != pt]
        add("il", "escuta", level, theme, "Ouça e escolha a palavra que você ouviu.", "🔊", [it], pick(rng, same, [it]), f"Você ouviu {it} ({pt}).", audio=it)

    # ---------------------------------------------------------- falsos amigos
    meanings = [m for _, m, _ in C.FALSE_FRIENDS]
    for it, real, trap in C.FALSE_FRIENDS:
        add("if", "falsos", 1, "falsos amigos", "Cuidado com o falso amigo: o que significa?", it, [real], [trap] + pick(rng, meanings, [real], 2),
            f"{it} = {real} (não “{trap}”).", audio=it)

    # ---------------------------------------------------------- verbos (todas as pessoas)
    no_past = {"essere", "potere", "volere", "sapere"}

    def past(verb, p):
        """Passato prossimo; verbos de movimento usam essere e concordam (aceita masculino e feminino)."""
        if verb in C.ESSERE_VERBS:
            base = participle(verb)[:-1]
            ends = ["o", "a"] if p < 3 else ["i", "e"]
            if p == 2:
                ends = ["o"]
            return [f"{present('essere', p)} {base}{e}" for e in ends]
        return [f"{present('avere', p)} {participle(verb)}"]

    for verb, pt, comp, level in C.VERBS:
        for p in persons:
            s = C.PERSONS[p]
            tenses = [
                ("presente", "Oggi", [present(verb, p)], others(lambda q: present(verb, q), p)[:3] + [verb, participle(verb)], level, "Presente."),
                ("imperfetto", "Anni fa", [imperfect(verb, p)], others(lambda q: imperfect(verb, q), p)[:2] + [present(verb, p), future(verb, p), verb], 2,
                 "Hábito no passado → imperfetto."),
                ("futuro", "Domani", [future(verb, p)], others(lambda q: future(verb, q), p)[:2] + [imperfect(verb, p), verb], 2, "Futuro semplice."),
            ]
            if verb not in no_past:
                why = (f"{verb} usa essere e concorda com o sujeito." if verb in C.ESSERE_VERBS
                       else f"Passato prossimo: avere + particípio ({participle(verb)}).")
                wrong = [past(verb, q)[0] for q in persons if q != p][:2] + [present(verb, p), future(verb, p)]
                tenses.append(("passato prossimo", "Ieri", past(verb, p), wrong, 2, why))
            for tense, lead, answers, wrong, lvl, why in tenses:
                text = f"{lead} {s} ___ {comp}."
                add("ig", "verbos", lvl, tense, f"{tense.capitalize()} de {verb} ({pt}).", text, answers, pick(rng, wrong, answers), why,
                    audio=text.replace("___", answers[0]), typeable=True)

    # ---------------------------------------------------------- gramática
    for text, right, wrong, why, level, theme in C.GRAMMAR:
        full = text.replace("___", right).replace("' ", "'")
        add("iq", "gramatica", level, theme, "Complete a frase.", text, [right], wrong, why, audio=full, typeable=True)

    # ---------------------------------------------------------- completar (2–3 lacunas)
    for verb, obj, og, plural, place, prep in C.ACTIVITIES:
        pp = join(prep, place)
        art = article(obj, og, plural)
        art_obj = join(art, obj)
        part = participle(verb)
        place_art = A_ART[article(place, PLACE_GENDER[place])]
        prep_wrong = [x for x in ("al", "alla", "allo", "all'") if x not in (prep, place_art)]

        def art_slot():
            return slot(art, art_wrong(art), "artigo")

        for subj, p in C.SUBJECTS:
            s = low(subj)
            conj = present(verb, p)
            other = others(lambda q: present(verb, q), p)
            aux = present("avere", p)
            inf_wrong = [conj, part, gerund(verb)]
            # A presente: verbo + artigo
            add("ic", "completar", 1, "presente", f"Complete as duas lacunas (verbo {verb} e artigo).", f"{subj} ___ {gap(art, obj)} {pp}.",
                [f"{conj} · {art}"], ["-"], f"{subj} → {conj}; {obj} → {art}.", audio=f"{subj} {conj} {art_obj} {pp}.",
                slots=[slot(conj, other, f"{verb} no presente"), art_slot()], typeable=True)
            # B passato prossimo: avere + particípio + artigo
            add("ic", "completar", 2, "passato prossimo", f"Complete as três lacunas (passato prossimo de {verb} e artigo).",
                f"Ieri {s} ___ ___ {gap(art, obj)} {pp}.", [f"{aux} · {part} · {art}"], ["-"], f"avere ({aux}) + particípio ({part}).",
                audio=f"Ieri {s} {aux} {part} {art_obj} {pp}.",
                slots=[slot(aux, others(lambda q: present("avere", q), p) + [present("essere", p)], "avere"),
                       slot(part, [verb, conj, imperfect(verb, p)], "particípio"), art_slot()], typeable=True)
            # C andare + preposição de lugar
            if place != "treno":
                go = present("andare", p)
                add("ic", "completar", 1, "andare", "Complete as duas lacunas (andare e preposição).", f"Stasera {s} ___ {gap(prep, place)}.",
                    [f"{go} · {prep}"], ["-"], f"andare → {go}; {pp}.", audio=f"Stasera {s} {go} {pp}.",
                    slots=[slot(go, others(lambda q: present("andare", q), p), "andare"), slot(prep, prep_wrong, "preposição")], typeable=True)
            # D futuro
            fut = future(verb, p)
            add("ic", "completar", 2, "futuro", f"Complete (futuro de {verb} e artigo).", f"Domani {s} ___ {gap(art, obj)} {pp}.",
                [f"{fut} · {art}"], ["-"], f"Futuro semplice: {fut}.", audio=f"Domani {s} {fut} {art_obj} {pp}.",
                slots=[slot(fut, others(lambda q: future(verb, q), p) + [imperfect(verb, p)], f"{verb} no futuro"), art_slot()], typeable=True)
            # E negação
            add("ic", "completar", 1, "negação", f"Complete a negação (non + {verb}).", f"{subj} non ___ {gap(art, obj)}.",
                [f"{conj} · {art}"], ["-"], "Negação: non antes do verbo.", audio=f"{subj} non {conj} {art_obj}.",
                slots=[slot(conj, other, f"{verb} no presente"), art_slot()], typeable=True)
            # F stare + gerundio
            st = present("stare", p)
            ger = gerund(verb)
            add("ic", "completar", 2, "stare + gerundio", f"Complete: stare + gerundio de {verb}.", f"Adesso {s} ___ ___ {art_obj}.",
                [f"{st} · {ger}"], ["-"], f"Ação em andamento: stare ({st}) + gerundio ({ger}).", audio=f"Adesso {s} {st} {ger} {art_obj}.",
                slots=[slot(st, others(lambda q: present("stare", q), p) + [present("essere", p)], "stare"),
                       slot(ger, [verb, part, conj], "gerundio")], typeable=True)
            # G imperfetto
            imp = imperfect(verb, p)
            add("ic", "completar", 2, "imperfetto", f"Complete (hábito no passado com {verb}).", f"Anni fa {s} ___ sempre {gap(art, obj)} {pp}.",
                [f"{imp} · {art}"], ["-"], f"Hábito no passado → imperfetto: {imp}.", audio=f"Anni fa {s} {imp} sempre {art_obj} {pp}.",
                slots=[slot(imp, others(lambda q: imperfect(verb, q), p) + [conj], f"{verb} no imperfetto"), art_slot()], typeable=True)
            # H volere + infinitivo
            want = present("volere", p)
            add("ic", "completar", 1, "volere", f"Complete: volere + {verb}.", f"{subj} ___ ___ {art_obj}.", [f"{want} · {verb}"], ["-"],
                f"volere ({want}) + infinitivo.", audio=f"{subj} {want} {verb} {art_obj}.",
                slots=[slot(want, others(lambda q: present("volere", q), p), "volere"), slot(verb, inf_wrong, "infinitivo")], typeable=True)
            # I potere + infinitivo (negativo)
            can = present("potere", p)
            add("ic", "completar", 1, "potere", f"Complete: non + potere + {verb}.", f"Oggi {s} non ___ ___ {art_obj}.", [f"{can} · {verb}"], ["-"],
                f"potere ({can}) + infinitivo.", audio=f"Oggi {s} non {can} {verb} {art_obj}.",
                slots=[slot(can, others(lambda q: present("potere", q), p), "potere"), slot(verb, inf_wrong, "infinitivo")], typeable=True)
            # J passato prossimo negativo
            add("ic", "completar", 2, "passato prossimo", f"Complete a negação no passato prossimo ({verb}).", f"Ieri {s} non ___ ___ {art_obj}.",
                [f"{aux} · {part}"], ["-"], f"non + avere + particípio: non {aux} {part}.", audio=f"Ieri {s} non {aux} {part} {art_obj}.",
                slots=[slot(aux, others(lambda q: present("avere", q), p) + [present("essere", p)], "avere"),
                       slot(part, [verb, conj, imp], "particípio")], typeable=True)

    # ---------------------------------------------------------- números e frases
    for it, pt, wrong in C.NUMBERS:
        add("in", "numeros", 1, "números", f"Como se diz “{pt}”?", pt, [it], wrong, f"{pt} = {it}.", audio=it, typeable=True)
    for it, pt, ctx in C.PHRASES:
        note = f" ({ctx})" if ctx else ""
        add("ip", "frases", 1, "frases", "O que significa?", it, [pt], pick(rng, [p for _, p, _ in C.PHRASES if p != pt], [pt]), f"{it} = {pt}{note}.", audio=it)
        add("ip", "frases", 1, "frases", "Como se diz em italiano?", pt, [it], pick(rng, [f for f, p, _ in C.PHRASES if p != pt], [it]), f"{pt} = {it}{note}.",
            audio=it, typeable=True)
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
    build_app(PAGE, data, PUBLIC / "italian.html")
    counts = {}
    for q in questions:
        counts[q["module"]] = counts.get(q["module"], 0) + 1
    print(f"italian.html: {len(questions)} questões", counts)


if __name__ == "__main__":
    main()
