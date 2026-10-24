"""Gera public/german.html (German Routine) a partir de content.py + practice/ + skills/.

Rode: python german/build_german.py
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
    "code": "de", "html_lang": "de", "brand": "German Routine", "brand_word": "german", "name": "alemão",
    "alphabet_tab": "Pronúncia", "eyebrow": "Alemão todos os dias · A1–A2", "headline": "Hallo! Vamos treinar.",
    "intro": "questões de vocabulário, falsos amigos, verbos, gramática, frases para completar, números, frases e escuta — pensadas para quem fala português.",
    "level_prefix": "A", "level1": "A1", "level2": "A2", "typing_label": "Digitar em alemão",
    "typing_hint": "Digite com ä, ö, ü e ß e com os substantivos em maiúscula. No celular, segure a letra para escolher o umlaut (a → ä, s → ß).",
    "lang_js": ROOT / "lang.js", "alphabet_html": ROOT / "alphabet.html",
}
ENDS = ["e", "st", "t", "en", "t", "en"]
NO_GE = ("be", "ver", "er", "ent", "emp", "zer", "ge")
ACC = {"m": "den", "f": "die", "n": "das", "pl": "die"}
KEIN = {"m": "keinen", "f": "keine", "n": "kein", "pl": "keine"}
LOC = {"m": "im", "n": "im", "f": "in der"}
MOV = {"m": "in den", "n": "ins", "f": "in die"}
DRILL_SUBJECTS = ["ich", "du", "er", "wir", "ihr", "die Kinder"]
LOWER = {"Ich", "Du", "Er", "Wir", "Ihr", "Mein", "Meine", "Der", "Die", "Dein", "Unsere"}


def stem_of(verb):
    return verb[:-2]


def needs_e(stem):
    """arbeit-e-st, find-e-t, öffn-e-t: radical em t/d ou consoante + m/n."""
    return stem.endswith(("t", "d")) or (stem[-1:] in "mn" and stem[-2:-1] not in "aeiouäöülrhmn")


def present(verb, p):
    if verb in C.PRESENT:
        return C.PRESENT[verb][p]
    stem = stem_of(verb)
    end = ENDS[p]
    if end in ("st", "t") and needs_e(stem):
        end = "e" + end
    elif end == "st" and stem.endswith(("s", "ß", "z", "x")):
        end = "t"  # du tanzt, du reist
    return stem + end


def regular_participle(verb):
    stem = stem_of(verb)
    tail = "et" if needs_e(stem) else "t"
    if verb.endswith("ieren") or verb.startswith(NO_GE):
        return stem + tail
    return "ge" + stem + tail


def participle(verb):
    return C.PARTICIPLE.get(verb) or regular_participle(verb)


def aux(verb, p):
    return present("sein" if verb in C.SEIN_VERBS else "haben", p)


def wrong_aux(verb, p):
    return present("haben" if verb in C.SEIN_VERBS else "sein", p)


def low(s):
    first, _, rest = s.partition(" ")
    return (first.lower() + (" " + rest if rest else "")) if first in LOWER else s


def cap(s):
    return s[0].upper() + s[1:]


def gap(word):
    return "___ " + word


def pick(rng, pool, exclude, n=3):
    pool = [p for p in dict.fromkeys(pool) if p not in exclude]
    rng.shuffle(pool)
    return pool[:n]


def bare(word):
    for a in ("der ", "die ", "das "):
        if word.startswith(a):
            return word[len(a):]
    return word


def build():
    rng = random.Random(20261027)
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

    def inf_slot(verb, label="infinitivo"):
        return slot(verb, [present(verb, 0), present(verb, 1), present(verb, 2), participle(verb)], label)

    def part_slot(verb):
        return slot(participle(verb), [verb, present(verb, 2), regular_participle(verb), "ge" + verb], "particípio")

    def aux_slot(verb, p):
        return slot(aux(verb, p), others(lambda q: aux(verb, q), p) + [wrong_aux(verb, p)], "haben / sein")

    # ---------------------------------------------------------- vocabulário e escuta
    by_theme = {}
    for de, pt, theme, level in C.VOCAB:
        by_theme.setdefault(theme, []).append((de, pt))
    for de, pt, theme, level in C.VOCAB:
        same = by_theme[theme]
        add("dv", "vocabulario", level, theme, "O que significa?", de, [pt], pick(rng, [p for _, p in same], [pt]), f"{de} = {pt}.", audio=de)
        add("dv", "vocabulario", level, theme, "Como se diz em alemão?", pt, [de, bare(de)], pick(rng, [f for f, p in same if p != pt], [de, bare(de)]),
            f"“{pt}” = {de}.", audio=de, typeable=True)
    for de, pt, theme, level in C.VOCAB[:150]:
        same = [f for f, p in by_theme[theme] if p != pt]
        add("dl", "escuta", level, theme, "Ouça e escolha a palavra que você ouviu.", "🔊", [de], pick(rng, same, [de]), f"Você ouviu {de} ({pt}).", audio=de)

    # ---------------------------------------------------------- falsos amigos
    meanings = [m for _, m, _ in C.FALSE_FRIENDS]
    for de, real, trap in C.FALSE_FRIENDS:
        add("df", "falsos", 1, "falsos amigos", "Cuidado com o falso amigo: o que significa?", de, [real], [trap] + pick(rng, meanings, [real], 2),
            f"{de} = {real} (não “{trap}”).", audio=de)

    # ---------------------------------------------------------- verbos (todas as pessoas)
    for verb, pt, comp, level in C.VERBS:
        for p in persons:
            s = DRILL_SUBJECTS[p]
            conj = present(verb, p)
            text = f"{cap(s)} ___ {comp}."
            add("dg", "verbos", level, "presente", f"Presente de {verb} ({pt}).", text, [conj],
                pick(rng, others(lambda q: present(verb, q), p) + [verb, participle(verb)], [conj]), "Präsens.",
                audio=text.replace("___", conj), typeable=True)
            if verb != "sein":
                a, part = aux(verb, p), participle(verb)
                why = f"{verb} usa sein no Perfekt (movimento/mudança)." if verb in C.SEIN_VERBS else f"Perfekt: haben + particípio ({part})."
                add("dg", "verbos", 2, "Perfekt", f"Perfekt de {verb} ({pt}).", f"Letzte Woche ___ {s} {comp} ___.", [f"{a} · {part}"], ["-"], why,
                    audio=f"Letzte Woche {a} {s} {comp} {part}.", slots=[aux_slot(verb, p), part_slot(verb)], typeable=True)
            w = present("werden", p)
            add("dg", "verbos", 2, "futuro", f"Futur de {verb} ({pt}).", f"Nächstes Jahr ___ {s} {comp} ___.", [f"{w} · {verb}"], ["-"],
                f"Futur: werden ({w}) + infinitivo no final.", audio=f"Nächstes Jahr {w} {s} {comp} {verb}.",
                slots=[slot(w, others(lambda q: present("werden", q), p), "werden"), inf_slot(verb)], typeable=True)

    # ---------------------------------------------------------- gramática
    for text, right, wrong, why, level, theme in C.GRAMMAR:
        add("dq", "gramatica", level, theme, "Complete a frase.", text, [right], wrong, why, audio=text.replace("___", right), typeable=True)

    # ---------------------------------------------------------- completar (2–3 lacunas)
    for verb, obj, og, place, pg in C.ACTIVITIES:
        art = ACC[og]
        art_obj = f"{art} {obj}"
        locp = f"{LOC[pg]} {place}"
        kein = KEIN[og]
        part = participle(verb)
        art_wrong = {"den": ["der", "dem", "das"], "das": ["der", "den", "dem"]}.get(art, ["der", "den", "dem"] if og == "f" else ["der", "den", "das"])
        kein_wrong = [k for k in ("kein", "keinen", "keine", "keinem") if k != kein]
        loc_wrong = [x for x in ("im", "in der", MOV[pg], "ins", "in den", "in die") if x != LOC[pg]][:3]
        mov_wrong = [LOC[pg]] + [x for x in ("in den", "ins", "in die") if x != MOV[pg]]

        def art_slot():
            return slot(art, art_wrong, "artigo (acusativo)")

        for subj, p in C.SUBJECTS:
            s = low(subj)
            conj = present(verb, p)
            other = others(lambda q: present(verb, q), p)
            a = aux(verb, p)
            # A presente: verbo + artigo no acusativo
            add("dc", "completar", 1, "presente", f"Complete as duas lacunas (verbo {verb} e artigo).", f"{subj} ___ {gap(obj)} {locp}.",
                [f"{conj} · {art}"], ["-"], f"{subj} → {conj}; objeto direto → {art} {obj}.", audio=f"{subj} {conj} {art_obj} {locp}.",
                slots=[slot(conj, other, f"{verb} no presente"), art_slot()], typeable=True)
            # B Perfekt: auxiliar na 2ª posição, particípio no final
            add("dc", "completar", 2, "Perfekt", f"Complete o Perfekt de {verb} (auxiliar e particípio).", f"Gestern ___ {s} {art_obj} {locp} ___.",
                [f"{a} · {part}"], ["-"], f"Auxiliar na 2ª posição ({a}), particípio no final ({part}).", audio=f"Gestern {a} {s} {art_obj} {locp} {part}.",
                slots=[aux_slot(verb, p), part_slot(verb)], typeable=True)
            # C gehen + movimento (acusativo)
            go = present("gehen", p)
            add("dc", "completar", 1, "movimento", "Complete: gehen + para onde? (acusativo).", f"Heute Abend ___ {s} {gap(place)}.",
                [f"{go} · {MOV[pg]}"], ["-"], f"Para onde? → acusativo: {MOV[pg]} {place}.", audio=f"Heute Abend {go} {s} {MOV[pg]} {place}.",
                slots=[slot(go, others(lambda q: present("gehen", q), p), "gehen"), slot(MOV[pg], mov_wrong, "preposição + artigo")], typeable=True)
            # D Futur
            w = present("werden", p)
            add("dc", "completar", 2, "futuro", f"Complete o futuro (werden + {verb}).", f"Morgen ___ {s} {art_obj} {locp} ___.", [f"{w} · {verb}"], ["-"],
                f"werden ({w}) na 2ª posição + infinitivo no final.", audio=f"Morgen {w} {s} {art_obj} {locp} {verb}.",
                slots=[slot(w, others(lambda q: present("werden", q), p), "werden"), inf_slot(verb)], typeable=True)
            # E negação com kein
            add("dc", "completar", 1, "negação", f"Complete a negação com kein ({verb}).", f"{subj} ___ heute {gap(obj)}.", [f"{conj} · {kein}"], ["-"],
                f"kein nega o substantivo e segue o gênero no acusativo: {kein} {obj}.", audio=f"{subj} {conj} heute {kein} {obj}.",
                slots=[slot(conj, other, f"{verb} no presente"), slot(kein, kein_wrong, "kein")], typeable=True)
            # F möchten + infinitivo
            m = present("möchten", p)
            add("dc", "completar", 1, "möchten", f"Complete: möchten + {verb}.", f"{subj} ___ {art_obj} ___.", [f"{m} · {verb}"], ["-"],
                f"möchten ({m}) + infinitivo no final.", audio=f"{subj} {m} {art_obj} {verb}.",
                slots=[slot(m, others(lambda q: present("möchten", q), p), "möchten"), inf_slot(verb)], typeable=True)
            # G können (negativo)
            k = present("können", p)
            add("dc", "completar", 1, "können", f"Complete: können + {verb} (negativo).", f"Heute ___ {s} {art_obj} nicht ___.", [f"{k} · {verb}"], ["-"],
                f"können ({k}) na 2ª posição; nicht e infinitivo no final.", audio=f"Heute {k} {s} {art_obj} nicht {verb}.",
                slots=[slot(k, others(lambda q: present("können", q), p), "können"), inf_slot(verb)], typeable=True)
            # H wollen + lugar
            wl = present("wollen", p)
            add("dc", "completar", 1, "wollen", f"Complete: wollen + {verb}.", f"Am Wochenende ___ {s} {art_obj} {locp} ___.", [f"{wl} · {verb}"], ["-"],
                f"wollen ({wl}) + infinitivo no final.", audio=f"Am Wochenende {wl} {s} {art_obj} {locp} {verb}.",
                slots=[slot(wl, others(lambda q: present("wollen", q), p), "wollen"), inf_slot(verb)], typeable=True)
            # I Perfekt negativo
            add("dc", "completar", 2, "Perfekt", f"Complete o Perfekt negativo de {verb}.", f"Gestern ___ {s} {art_obj} nicht ___.", [f"{a} · {part}"], ["-"],
                f"Auxiliar ({a}) + nicht + particípio no final ({part}).", audio=f"Gestern {a} {s} {art_obj} nicht {part}.",
                slots=[aux_slot(verb, p), part_slot(verb)], typeable=True)
            # J onde? (dativo)
            add("dc", "completar", 1, "lugar", f"Complete: verbo {verb} + onde? (dativo).", f"{subj} ___ {art_obj} {gap(place)}.",
                [f"{conj} · {LOC[pg]}"], ["-"], f"Onde? → dativo: {LOC[pg]} {place}.", audio=f"{subj} {conj} {art_obj} {locp}.",
                slots=[slot(conj, other, f"{verb} no presente"), slot(LOC[pg], loc_wrong, "preposição + artigo")], typeable=True)

    # ---------------------------------------------------------- números e frases
    for de, pt, wrong in C.NUMBERS:
        add("dn", "numeros", 1, "números", f"Como se diz “{pt}”?", pt, [de], wrong, f"{pt} = {de}.", audio=de, typeable=True)
    for de, pt, ctx in C.PHRASES:
        note = f" ({ctx})" if ctx else ""
        add("dp", "frases", 1, "frases", "O que significa?", de, [pt], pick(rng, [p for _, p, _ in C.PHRASES if p != pt], [pt]), f"{de} = {pt}{note}.", audio=de)
        add("dp", "frases", 1, "frases", "Como se diz em alemão?", pt, [de], pick(rng, [f for f, p, _ in C.PHRASES if p != pt], [de]), f"{pt} = {de}{note}.",
            audio=de, typeable=True)
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
    "vocabulario": "Vocabulário", "falsos": "Falsos amigos", "escuta": "Escuta", "verbos": "Verbos (presente, Perfekt, futuro)",
    "gramatica": "Gramática", "completar": "Completar frases (2 lacunas)", "numeros": "Números e horas", "frases": "Frases do dia a dia",
}


def main():
    questions = build()
    validate(questions)
    data = {"questions": questions, "modules": MODULES, "guide": C.GUIDE, "sounds": C.SOUNDS, "roman": {}}
    data["skills"], _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, listen_choice(questions))
    build_app(PAGE, data, PUBLIC / "german.html")
    counts = {}
    for q in questions:
        counts[q["module"]] = counts.get(q["module"], 0) + 1
    print(f"german.html: {len(questions)} questões", counts)


if __name__ == "__main__":
    main()
