"""Questões extras do Spanish Routine (expansão para ~10 mil).

Geradas DEPOIS das originais e com prefixos próprios (ex, ey, ez, ew2), para que os IDs
antigos — e o histórico dos alunos — não mudem.
"""

SUBJECTS_2 = [("Juan", 2), ("María", 2), ("Los niños", 5), ("Mi padre", 2), ("Mis padres", 5), ("El profesor", 2), ("La profesora", 2),
              ("Nosotras", 3), ("Ellas", 5), ("Mi novia", 2), ("Tus amigos", 5), ("Pedro y yo", 3)]
# (verbo, objeto, gênero, lugar, gênero do lugar)
ACTIVITIES_2 = [
    ("comprar", "leche", "f", "supermercado", "m"), ("beber", "zumo", "m", "bar", "m"), ("comer", "pizza", "f", "pizzería", "f"),
    ("leer", "periódico", "m", "parque", "m"), ("ver", "serie", "f", "casa", "f"), ("escribir", "correo", "m", "oficina", "f"),
    ("preparar", "comida", "f", "cocina", "f"), ("comprar", "pescado", "m", "mercado", "m"), ("pedir", "cuenta", "f", "restaurante", "m"),
    ("comprar", "billete", "m", "estación", "f"), ("buscar", "libro", "m", "biblioteca", "f"), ("visitar", "museo", "m", "ciudad", "f"),
    ("lavar", "ropa", "f", "lavandería", "f"), ("pintar", "cuadro", "m", "taller", "m"), ("tocar", "guitarra", "f", "escuela", "f"),
    ("cocinar", "arroz", "m", "cocina", "f"), ("comprar", "regalo", "m", "centro comercial", "m"), ("abrir", "ventana", "f", "clase", "f"),
    ("limpiar", "mesa", "f", "comedor", "m"), ("esperar", "autobús", "m", "parada", "f"),
]
# Verbos novos: (infinitivo, português, complemento, nível)
VERBS_2 = [
    ("alquilar", "alugar", "un coche", 2), ("caminar", "caminhar", "por la playa", 1), ("cenar", "jantar", "en casa", 1), ("correr", "correr", "en el parque", 1),
    ("desayunar", "tomar café da manhã", "a las ocho", 1), ("enseñar", "ensinar", "matemáticas", 2), ("entrar", "entrar", "en la tienda", 1),
    ("ganar", "ganhar", "el partido", 2), ("gastar", "gastar", "mucho dinero", 2), ("limpiar", "limpar", "la casa", 1), ("llevar", "levar", "una mochila", 2),
    ("mandar", "mandar", "un mensaje", 2), ("nadar", "nadar", "en el mar", 1), ("necesitar", "precisar", "ayuda", 2), ("olvidar", "esquecer", "las llaves", 2),
    ("pagar", "pagar", "la cuenta", 1), ("pasear", "passear", "con el perro", 1), ("preguntar", "perguntar", "la hora", 2), ("preparar", "preparar", "la cena", 1),
    ("regresar", "voltar", "a casa", 2), ("sacar", "tirar (foto) / tirar", "fotos", 2), ("terminar", "terminar", "el trabajo", 2), ("tocar", "tocar", "el piano", 1),
    ("usar", "usar", "el ordenador", 1), ("vender", "vender", "su coche", 2), ("visitar", "visitar", "a sus abuelos", 1), ("aprender", "aprender", "inglés", 1),
    ("comprender", "compreender", "la lección", 2), ("subir", "subir", "la montaña", 2), ("recibir", "receber", "un regalo", 2),
]
SUBJECTS = [("yo", 0), ("tú", 1), ("él", 2), ("ella", 2), ("usted", 2), ("nosotros", 3), ("ellos", 5), ("ustedes", 5)]
GERUND_IRREGULAR = {"leer": "leyendo", "pedir": "pidiendo", "dormir": "durmiendo", "decir": "diciendo", "venir": "viniendo", "poder": "pudiendo", "ir": "yendo"}
IMPERFECT_IRREGULAR = {"ser": ["era", "eras", "era", "éramos", "erais", "eran"], "ir": ["iba", "ibas", "iba", "íbamos", "ibais", "iban"],
                       "ver": ["veía", "veías", "veía", "veíamos", "veíais", "veían"]}
# gustar: (frase com pronome, pronome átono)
GUSTAR = [("A mí", "me"), ("A ti", "te"), ("A él", "le"), ("A nosotros", "nos"), ("A ellos", "les"), ("A mi madre", "le"), ("A mis amigos", "les")]
LIKES = ["el chocolate", "el café", "la música", "el fútbol", "la playa", "el verano", "la pizza", "el cine", "la paella", "el té",
         "los gatos", "los perros", "las películas de terror", "los libros", "las flores", "los deportes", "las fresas", "los conciertos", "las series", "los viajes"]
VOCAB_2 = [
    ("la cuchara", "a colher", "objetos", 1), ("el tenedor", "o garfo", "objetos", 1), ("el cuchillo", "a faca", "objetos", 1), ("el plato", "o prato", "objetos", 1),
    ("la taza", "a xícara", "objetos", 1), ("la ventana", "a janela", "objetos", 1), ("la puerta", "a porta", "objetos", 1), ("el cuadro", "o quadro", "objetos", 2),
    ("la guitarra", "o violão", "objetos", 1), ("el regalo", "o presente", "objetos", 1), ("la serie", "a série", "objetos", 1), ("el correo", "o e-mail / correio", "objetos", 1),
    ("la cuenta", "a conta", "objetos", 1), ("el paraguas", "o guarda-chuva", "objetos", 1), ("el abrigo", "o casaco", "objetos", 2), ("la gorra", "o boné", "objetos", 2),
    ("la pizza", "a pizza", "comida", 1), ("el zumo de naranja", "o suco de laranja", "comida", 1), ("la sopa", "a sopa", "comida", 1), ("el postre", "a sobremesa (doce)", "comida", 1),
    ("la tostada", "a torrada", "comida", 1), ("el helado", "o sorvete", "comida", 1), ("las fresas", "os morangos", "comida", 1), ("la naranja", "a laranja", "comida", 1),
    ("la pizzería", "a pizzaria", "lugares", 1), ("la lavandería", "a lavanderia", "lugares", 2), ("el taller", "a oficina mecânica / ateliê", "lugares", 2),
    ("el comedor", "a sala de jantar / refeitório", "lugares", 2), ("la parada", "o ponto (de ônibus)", "lugares", 1), ("el centro comercial", "o shopping", "lugares", 1),
    ("la clase", "a aula / sala de aula", "lugares", 1), ("la cocina", "a cozinha", "lugares", 1), ("el gimnasio", "a academia", "lugares", 1), ("la piscina", "a piscina", "lugares", 1),
    ("correr", "correr", "verbos", 1), ("nadar", "nadar", "verbos", 1), ("caminar", "caminhar", "verbos", 1), ("olvidar", "esquecer", "verbos", 2),
    ("necesitar", "precisar", "verbos", 2), ("terminar", "terminar", "verbos", 2), ("enseñar", "ensinar", "verbos", 2), ("vender", "vender", "verbos", 1),
    ("aprender", "aprender", "verbos", 1), ("recibir", "receber", "verbos", 2), ("alquilar", "alugar", "verbos", 2), ("limpiar", "limpar", "verbos", 1),
    ("contento", "contente", "adjetivos", 1), ("enfadado", "bravo / irritado", "adjetivos", 2), ("aburrido", "entediado / chato", "adjetivos", 2), ("ocupado", "ocupado", "adjetivos", 1),
    ("listo", "pronto / esperto", "adjetivos", 2), ("limpio", "limpo", "adjetivos", 1), ("sucio", "sujo", "adjetivos", 1), ("caliente", "quente", "adjetivos", 1),
    ("frío", "frio", "adjetivos", 1), ("cerca", "perto", "lugares", 1), ("lejos", "longe", "lugares", 1),
]


def gerund(verb):
    if verb in GERUND_IRREGULAR:
        return GERUND_IRREGULAR[verb]
    return verb[:-2] + ("ando" if verb.endswith("ar") else "iendo")


def imperfect(verb, person):
    if verb in IMPERFECT_IRREGULAR:
        return IMPERFECT_IRREGULAR[verb][person]
    if verb.endswith("ar"):
        return verb[:-2] + ["aba", "abas", "aba", "ábamos", "abais", "aban"][person]
    return verb[:-2] + ["ía", "ías", "ía", "íamos", "íais", "ían"][person]


def build_more(add, slot, pick, rng, C, present, past, article, to_place):
    def lower(s):
        return s if s in ("Ana y yo", "Pedro y yo", "Juan", "María") else s[0].lower() + s[1:]

    subjects = C.COMBO_SUBJECTS + SUBJECTS_2
    activities = C.COMBO_ACTIVITIES + ACTIVITIES_2
    old = {(s, a) for s, _ in C.COMBO_SUBJECTS for a in C.COMBO_ACTIVITIES}
    persons = (0, 1, 2, 3, 5)

    def art_slot(g, label="artigo"):
        return slot(article(g), ["el", "la", "los", "las"], label)

    # ---------------------------------------------------------- ex: completar
    for act in activities:
        verb, obj, og, place, pg = act
        for subj, person in subjects:
            s = lower(subj)
            conj, pconj = present(verb, person), past(verb, person)
            if (subj, act) not in old:
                add("ex", "completar", 1, "presente", f"Complete as duas lacunas (verbo {verb} e artigo).", f"{subj} ___ ___ {obj}.",
                    [f"{conj} · {article(og)}"], ["-"], f"{subj} → {conj}; {obj} → {article(og)}.", audio=f"{subj} {conj} {article(og)} {obj}.",
                    slots=[slot(conj, [present(verb, p) for p in persons if p != person], f"{verb} no presente"), art_slot(og)], typeable=True)
                add("ex", "completar", 2, "pretérito", f"Complete as três lacunas (verbo {verb} no passado e artigos).", f"Ayer {s} ___ ___ {obj} en ___ {place}.",
                    [f"{pconj} · {article(og)} · {article(pg)}"], ["-"], f"Ayer → pretérito: {pconj}.",
                    audio=f"Ayer {s} {pconj} {article(og)} {obj} en {article(pg)} {place}.",
                    slots=[slot(pconj, [past(verb, p) for p in persons if p != person] + [conj], f"{verb} no pretérito"), art_slot(og),
                           art_slot(pg, "artigo do lugar")], typeable=True)
                go = present("ir", person)
                add("ex", "completar", 1, "ir a", "Complete as duas lacunas (ir e a + artigo).", f"Mañana {s} ___ ___ {place}.", [f"{go} · {to_place(pg)}"], ["-"],
                    f"ir → {go}; a + {article(pg)} → {to_place(pg)}.", audio=f"Mañana {s} {go} {to_place(pg)} {place}.",
                    slots=[slot(go, [present("ir", p) for p in persons if p != person], "ir no presente"), slot(to_place(pg), ["al", "a la", "a el", "en el"], "a + artigo")],
                    typeable=True)
            est, ger = present("estar", person), gerund(verb)
            add("ex", "completar", 2, "gerúndio", f"Complete: estar + gerúndio de {verb}.", f"Ahora {s} ___ ___ {article(og)} {obj}.", [f"{est} · {ger}"], ["-"],
                f"Ação em andamento: estar ({est}) + gerúndio ({ger}).", audio=f"Ahora {s} {est} {ger} {article(og)} {obj}.",
                slots=[slot(est, [present("estar", p) for p in persons if p != person], "estar"), slot(ger, [verb, conj, verb[:-2] + "ado"], "gerúndio")],
                typeable=True)
            go = present("ir", person)
            add("ex", "completar", 1, "ir a + infinitivo", f"Complete o futuro próximo (ir a + {verb}).", f"El sábado {s} ___ a ___ {article(og)} {obj}.",
                [f"{go} · {verb}"], ["-"], f"Ir a + infinitivo: {go} a {verb}.", audio=f"El sábado {s} {go} a {verb} {article(og)} {obj}.",
                slots=[slot(go, [present("ir", p) for p in persons if p != person], "ir no presente"), slot(verb, [conj, pconj, gerund(verb)], "infinitivo")],
                typeable=True)
            add("ex", "completar", 1, "presente", f"Complete as lacunas (verbo {verb} e artigo do lugar).", f"Siempre {s} ___ {article(og)} {obj} en ___ {place}.",
                [f"{conj} · {article(pg)}"], ["-"], f"Hábito (siempre) → presente: {conj}; {place} → {article(pg)}.",
                audio=f"Siempre {s} {conj} {article(og)} {obj} en {article(pg)} {place}.",
                slots=[slot(conj, [present(verb, p) for p in persons if p != person] + [pconj], f"{verb} no presente"), art_slot(pg, "artigo do lugar")],
                typeable=True)
            im = imperfect(verb, person)
            add("ex", "completar", 2, "imperfeito", f"Complete as lacunas (hábito no passado com {verb}).", f"Antes {s} siempre ___ {article(og)} {obj} en ___ {place}.",
                [f"{im} · {article(pg)}"], ["-"], f"Hábito no passado → imperfeito: {im}; {place} → {article(pg)}.",
                audio=f"Antes {s} siempre {im} {article(og)} {obj} en {article(pg)} {place}.",
                slots=[slot(im, [imperfect(verb, p) for p in persons if p != person] + [pconj], f"{verb} no imperfeito"), art_slot(pg, "artigo do lugar")],
                typeable=True)
            add("ex", "completar", 2, "pretérito", f"Complete a negação no passado ({verb}).", f"Ayer {s} no ___ ___ {obj}.", [f"{pconj} · {article(og)}"], ["-"],
                f"Negação: no antes do verbo; ayer → {pconj}.", audio=f"Ayer {s} no {pconj} {article(og)} {obj}.",
                slots=[slot(pconj, [past(verb, p) for p in persons if p != person] + [conj], f"{verb} no pretérito"), art_slot(og)], typeable=True)

    # ---------------------------------------------------------- ey: verbos (todas as pessoas, verbos novos, imperfeito)
    no_past = {"ser", "tener", "vivir", "querer"}
    done = set()
    for verb, pt, comp, level in C.VERBS:
        for k, (subj, person) in enumerate(C.SUBJECTS):
            if (k + len(verb)) % 2 == 0:
                done.add((verb, subj))
    for verb, pt, comp, level in C.VERBS + VERBS_2:
        for subj, person in SUBJECTS:
            if (verb, subj) in done:
                continue
            right = present(verb, person)
            add("ey", "verbos", level, "presente", f"Presente de {verb} ({pt}).", f"{subj.capitalize()} ___ {comp}.", [right],
                pick(rng, [present(verb, p) for p in persons if p != person] + [verb], [right]), f"{verb} com {subj} → {right}.",
                audio=f"{subj.capitalize()} {right} {comp}.", typeable=True)
            if verb not in no_past:
                pr = past(verb, person)
                add("ey", "verbos", 2, "pretérito", f"Pretérito indefinido de {verb} ({pt}).", f"Ayer {subj} ___ {comp}.", [pr],
                    pick(rng, [past(verb, p) for p in persons if p != person] + [right], [pr]), f"Ayer → pretérito: {pr}.",
                    audio=f"Ayer {subj} {pr} {comp}.", typeable=True)
    for verb, pt, comp, level in C.VERBS + VERBS_2:
        if verb in ("poder", "saber", "conocer"):
            continue
        for subj, person in SUBJECTS[:: 2] + [("ellos", 5)]:
            im = imperfect(verb, person)
            add("ey", "verbos", 2, "imperfeito", f"Pretérito imperfeito de {verb} ({pt}): hábito no passado.", f"De niño, {subj} siempre ___ {comp}.", [im],
                pick(rng, [imperfect(verb, p) for p in persons if p != person] + [past(verb, person), present(verb, person)], [im]),
                f"Hábito no passado (de niño, siempre) → imperfeito: {im}.", audio=f"De niño, {subj} siempre {im} {comp}.", typeable=True)

    # ---------------------------------------------------------- ez: gustar
    for who, clitic in GUSTAR:
        for thing in LIKES:
            right = "gustan" if thing.split()[0] in ("los", "las") else "gusta"
            add("ez", "gramatica", 1, "gustar", "Complete com gusta ou gustan.", f"{who} {clitic} ___ {thing}.", [right],
                ["gustan" if right == "gusta" else "gusta", "gusto", "gustas"], f"Gustar concorda com o que agrada ({thing}) → {right}.",
                audio=f"{who} {clitic} {right} {thing}.", typeable=True)
            add("ez", "gramatica", 2, "gustar", "Complete com o pronome (me, te, le, nos, les).", f"{who} ___ {right} {thing}.", [clitic],
                [c for c in ("me", "te", "le", "nos", "les") if c != clitic][:3], f"{who} → {clitic} {right}.", audio=f"{who} {clitic} {right} {thing}.",
                typeable=True)

    # ---------------------------------------------------------- vocabulário extra
    by_theme = {}
    for es, pt, theme, level in C.VOCAB + VOCAB_2:
        by_theme.setdefault(theme, []).append((es, pt))
    known = {es for es, *_ in C.VOCAB}
    for es, pt, theme, level in VOCAB_2:
        if es in known:
            continue
        same = by_theme[theme]
        bare = es.split(" ", 1)[1] if es.split(" ")[0] in ("el", "la", "los", "las") else es
        add("ew2", "vocabulario", level, theme, "O que significa?", es, [pt], pick(rng, [p for _, p in same], [pt]), f"{es} = {pt}.", audio=es)
        add("ew2", "vocabulario", level, theme, "Como se diz em espanhol?", pt, [es, bare], pick(rng, [e for e, p in same if p != pt], [es, bare]),
            f"“{pt}” = {es}.", audio=es, typeable=True)
        add("ew2", "escuta", level, theme, "Ouça e escolha a palavra que você ouviu.", "🔊", [es], pick(rng, [e for e, p in same if p != pt], [es]),
            f"Você ouviu {es} ({pt}).", audio=es)
