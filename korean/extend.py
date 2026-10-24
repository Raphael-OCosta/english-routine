"""Questões extras do Korean Routine (expansão para ~10 mil).

Geradas DEPOIS das originais e com prefixos próprios (kx, ky, kz), para que os IDs
antigos — e o histórico dos alunos — não mudem.
"""

# Novos sujeitos (tópico) e atividades: (lugar, objeto, dicionário, presente, passado, futuro)
SUBJECTS_2 = ["할머니", "할아버지", "남자친구", "여자친구", "사장님", "배우", "의사", "이웃", "손님", "민수 씨", "지은 씨", "아이들"]
ACTIVITIES_2 = [
    ("서점", "잡지", "읽다", "읽어요", "읽었어요", "읽을 거예요"), ("식당", "냉면", "먹다", "먹어요", "먹었어요", "먹을 거예요"),
    ("카페", "케이크", "먹다", "먹어요", "먹었어요", "먹을 거예요"), ("시장", "생선", "사다", "사요", "샀어요", "살 거예요"),
    ("편의점", "우유", "사다", "사요", "샀어요", "살 거예요"), ("공원", "자전거", "타다", "타요", "탔어요", "탈 거예요"),
    ("학교", "숙제", "하다", "해요", "했어요", "할 거예요"), ("도서관", "신문", "읽다", "읽어요", "읽었어요", "읽을 거예요"),
    ("방", "일기", "쓰다", "써요", "썼어요", "쓸 거예요"), ("극장", "연극", "보다", "봐요", "봤어요", "볼 거예요"),
    ("백화점", "가방", "사다", "사요", "샀어요", "살 거예요"), ("부엌", "라면", "끓이다", "끓여요", "끓였어요", "끓일 거예요"),
    ("사무실", "보고서", "쓰다", "써요", "썼어요", "쓸 거예요"), ("스튜디오", "사진", "찍다", "찍어요", "찍었어요", "찍을 거예요"),
    ("꽃집", "꽃", "사다", "사요", "샀어요", "살 거예요"), ("체육관", "농구", "하다", "해요", "했어요", "할 거예요"),
    ("한강", "치킨", "먹다", "먹어요", "먹었어요", "먹을 거예요"), ("교실", "단어", "외우다", "외워요", "외웠어요", "외울 거예요"),
    ("콘서트장", "노래", "듣다", "들어요", "들었어요", "들을 거예요"), ("거실", "청소", "하다", "해요", "했어요", "할 거예요"),
]
# Sujeitos para variar as frases de verbos (frase = sujeito + complemento + verbo).
VERB_SUBJECTS = ["친구는", "동생은", "엄마는", "우리는", "선생님은", "언니는"]

# Substantivos para partículas: (palavra, tipo) — tipo decide frases naturais.
THINGS = ["책", "가방", "우산", "시계", "휴대폰", "컴퓨터", "의자", "사진", "선물", "열쇠", "안경", "모자", "신발", "편지", "지갑",
          "공책", "연필", "볼펜", "카메라", "자동차", "자전거", "텔레비전", "냉장고", "침대", "책상", "거울", "창문", "옷", "치마", "바지"]
FOODS = ["김치", "불고기", "비빔밥", "떡볶이", "김밥", "라면", "냉면", "치킨", "피자", "빵", "케이크", "과일", "사과", "딸기", "수박",
         "커피", "우유", "녹차", "주스", "물", "밥", "국", "생선", "고기", "계란", "아이스크림", "초콜릿", "만두", "삼겹살", "잡채"]
HOBBIES = ["음악", "영화", "드라마", "케이팝", "춤", "노래", "운동", "축구", "야구", "수영", "등산", "여행", "요리", "독서", "게임", "사진"]
PLACES_GO = ["학교", "회사", "병원", "은행", "시장", "공원", "도서관", "카페", "식당", "공항", "역", "백화점", "편의점", "서점", "노래방",
             "영화관", "미술관", "박물관", "우체국", "약국", "호텔", "바다", "산", "한국", "서울", "부산", "제주도", "친구 집", "할머니 댁"]
PEOPLE = ["친구", "동생", "언니", "오빠", "형", "누나", "엄마", "아빠", "선생님", "할머니", "할아버지", "남자친구", "여자친구", "사촌", "동료"]

# Vocabulário extra: (coreano, português, tema, nível)
VOCAB_2 = [
    ("지갑", "carteira", "objetos", 1), ("공책", "caderno", "objetos", 1), ("연필", "lápis", "objetos", 1), ("볼펜", "caneta", "objetos", 1),
    ("카메라", "câmera", "objetos", 1), ("냉장고", "geladeira", "objetos", 2), ("침대", "cama", "objetos", 1), ("책상", "escrivaninha", "objetos", 1),
    ("거울", "espelho", "objetos", 2), ("치마", "saia", "objetos", 1), ("바지", "calça", "objetos", 1), ("양말", "meia", "objetos", 2),
    ("불고기", "bulgogi (carne marinada)", "comida", 1), ("수박", "melancia", "comida", 1), ("녹차", "chá verde", "comida", 1), ("주스", "suco", "comida", 1),
    ("국", "sopa", "comida", 1), ("계란", "ovo", "comida", 1), ("아이스크림", "sorvete", "comida", 1), ("초콜릿", "chocolate", "comida", 1),
    ("만두", "mandu (pastel coreano)", "comida", 1), ("삼겹살", "barriga de porco grelhada", "comida", 2), ("잡채", "japchae (macarrão de batata-doce)", "comida", 2),
    ("야구", "beisebol", "hobbies", 1), ("수영", "natação", "hobbies", 1), ("등산", "trilha / montanhismo", "hobbies", 2), ("독서", "leitura (hobby)", "hobbies", 2),
    ("게임", "jogo / videogame", "hobbies", 1), ("미술관", "museu de arte", "lugares", 2), ("박물관", "museu", "lugares", 2), ("우체국", "correio", "lugares", 2),
    ("약국", "farmácia", "lugares", 1), ("사촌", "primo / prima", "pessoas", 2), ("동료", "colega de trabalho", "pessoas", 2), ("이웃", "vizinho", "pessoas", 2),
    ("손님", "cliente / visita", "pessoas", 2), ("사장님", "dono / chefe", "pessoas", 2), ("숙제", "dever de casa", "objetos", 1), ("일기", "diário", "objetos", 2),
    ("연극", "peça de teatro", "objetos", 2), ("보고서", "relatório", "objetos", 2), ("단어", "palavra (vocabulário)", "objetos", 1), ("잡지", "revista", "objetos", 2),
    ("청소", "limpeza", "objetos", 1), ("빨래", "roupa para lavar", "objetos", 2), ("거실", "sala de estar", "lugares", 1), ("부엌", "cozinha", "lugares", 1),
    ("교실", "sala de aula", "lugares", 1), ("체육관", "ginásio", "lugares", 2), ("꽃집", "floricultura", "lugares", 1), ("서점", "livraria", "lugares", 1),
]


def build_more(add, slot, particle, has_batchim, pick, rng, C):
    def topic_slot(noun):
        right = particle(noun, "은", "는")
        return slot(right, ["는" if right == "은" else "은", particle(noun, "을", "를")], "tópico")

    def object_slot(noun):
        right = particle(noun, "을", "를")
        return slot(right, ["를" if right == "을" else "을", "에", particle(noun, "이", "가")], "objeto")

    def place_slot():
        return slot("에서", ["에", "로"], "lugar da ação")

    def goal_slot():
        return slot("에", ["에서", "을", "로"], "destino")

    subjects = C.COMBO_SUBJECTS + SUBJECTS_2
    activities = C.COMBO_ACTIVITIES + ACTIVITIES_2
    old = {(s, a[0], a[1]) for s in C.COMBO_SUBJECTS for a in C.COMBO_ACTIVITIES}

    # ---------------------------------------------------------- kx: completar (novas combinações e novos formatos)
    for place, obj, dic, pres, past, fut in activities:
        stem = dic[:-1]
        neg = stem + "지 않아요"
        for subj in subjects:
            t = topic_slot(subj)["answers"][0]
            o = particle(obj, "을", "를")
            if (subj, place, obj) not in old:
                # mesmos três formatos das originais, para as combinações novas
                full = f"{subj}{t} {place}에서 {obj}{o} {pres}."
                add("kx", "completar", 2, "partículas", "Complete as três lacunas (tópico, lugar e objeto).", f"{subj}___ {place}___ {obj}___ {pres}.",
                    [f"{t} · 에서 · {o}"], ["-"], f"{subj}{t}: tópico; {place}에서: lugar da ação; {obj}{o}: objeto.", audio=full,
                    slots=[topic_slot(subj), place_slot(), object_slot(obj)])
                full = f"어제 {subj}{t} {obj}{o} {past}."
                add("kx", "completar", 2, "passado", f"Complete as lacunas. Use {dic} no passado.", f"어제 {subj}___ {obj}___ ___.",
                    [f"{t} · {o} · {past}"], ["-"], f"어제 pede passado: {dic} → {past}.", audio=full,
                    slots=[topic_slot(subj), object_slot(obj), slot(past, [pres, fut, dic], f"{dic} no passado")])
                full = f"내일 {subj}{t} {obj}{o} {fut}."
                add("kx", "completar", 1, "futuro", "Complete as duas lacunas.", f"내일 {subj}___ {obj}___ {fut}.",
                    [f"{t} · {o}"], ["-"], f"{subj}{t}: tópico; {obj}{o}: objeto; {fut} = futuro.", audio=full,
                    slots=[topic_slot(subj), object_slot(obj)])
            # novos formatos para todas as combinações
            full = f"{subj}{t} {place}에서 {obj}{o} {neg}."
            add("kx", "completar", 2, "negação longa", f"Complete as lacunas. Negue {dic} com -지 않아요.", f"{subj}___ {place}에서 {obj}___ ___.",
                [f"{t} · {o} · {neg}"], ["-"], f"Negação longa: radical + 지 않아요 → {neg} (= 안 {pres}).", audio=full,
                slots=[topic_slot(subj), object_slot(obj), slot(neg, [pres, stem + "지 안아요", stem + "지 않았어요"], "negação")])
            full = f"내일 {subj}{t} {place}에서 {obj}{o} {fut}."
            add("kx", "completar", 2, "futuro", "Complete as três lacunas (tópico, lugar e objeto).", f"내일 {subj}___ {place}___ {obj}___ {fut}.",
                [f"{t} · 에서 · {o}"], ["-"], f"Lugar da ação → 에서; objeto → {o}; futuro {fut}.", audio=full,
                slots=[topic_slot(subj), place_slot(), object_slot(obj)])
            full = f"{subj}{t} 매일 {place}에서 {obj}{o} {pres}."
            add("kx", "completar", 1, "presente", f"Complete as lacunas. Use {dic} no presente.", f"{subj}___ 매일 {place}에서 {obj}___ ___.",
                [f"{t} · {o} · {pres}"], ["-"], f"매일 (todo dia) pede presente: {dic} → {pres}.", audio=full,
                slots=[topic_slot(subj), object_slot(obj), slot(pres, [past, fut, dic], f"{dic} no presente")])
            friend = PEOPLE[(len(subj) + len(place) * 3) % len(PEOPLE)]
            if friend != subj:
                w = particle(friend, "과", "와")
                full = f"주말에 {subj}{t} {friend}{w} 같이 {place}에 갔어요."
                add("kx", "completar", 2, "companhia", "Complete as três lacunas (tópico, companhia e destino).",
                    f"주말에 {subj}___ {friend}___ 같이 {place}___ 갔어요.", [f"{t} · {w} · 에"], ["-"],
                    f"{friend}{w}: com (batchim → 과, sem → 와); destino de 가다 → 에.", audio=full,
                    slots=[topic_slot(subj), slot(w, ["와" if w == "과" else "과", "을", "에서"], "companhia"), goal_slot()])
            full = f"어제 {subj}{t} {place}에 갔어요."
            add("kx", "completar", 1, "destino", "Complete as duas lacunas (tópico e destino).", f"어제 {subj}___ {place}___ 갔어요.",
                [f"{t} · 에"], ["-"], f"Destino de ir/vir → 에; ação no lugar → 에서.", audio=full, slots=[topic_slot(subj), goal_slot()])

    # ---------------------------------------------------------- ky: verbos com outros sujeitos
    past_time = {"살다": "작년에", "좋아하다": "예전에"}
    future_time = {"살다": "내년에"}
    for dic, pt, comp, pres, past, fut, neg in C.VERBS:
        stem = dic[:-1]
        forms = [pres, past] + ([fut] if fut else [])
        for subj in VERB_SUBJECTS:
            add("ky", "verbos", 1, "presente", f"Presente educado de {dic} ({pt}).", f"{subj} 매일 {comp} ___.", [pres],
                [f for f in forms if f != pres] + [stem + "요"], "Presente educado: -아요/-어요 (하다 → 해요).", audio=f"{subj} 매일 {comp} {pres}.")
            add("ky", "verbos", 1, "passado", f"Passado de {dic} ({pt}).", f"{past_time.get(dic, '어제')} {subj} {comp} ___.", [past],
                [f for f in forms if f != past] + [stem + "었요"], "Passado: -았어요/-었어요.", audio=f"{past_time.get(dic, '어제')} {subj} {comp} {past}.")
            if fut:
                add("ky", "verbos", 1, "futuro", f"Futuro de {dic} ({pt}).", f"{future_time.get(dic, '내일')} {subj} {comp} ___.", [fut],
                    [pres, past, dic], "Futuro: -(으)ㄹ 거예요.", audio=f"{future_time.get(dic, '내일')} {subj} {comp} {fut}.")
            add("ky", "verbos", 1, "negação", f"Negue: “não {pt}”.", f"{subj} {comp} ___.", [neg], [pres, "안 " + stem + "요", stem + "지 안아요"],
                "Negação curta com 안 (em X하다 separável: X 안 해요).", audio=f"{subj} {comp} {neg}.")

    # ---------------------------------------------------------- kz: partículas com o vocabulário
    for noun in THINGS:
        right = particle(noun, "이", "가")
        add("kz", "particulas", 1, "sujeito", "Complete com a partícula de sujeito.", f"방에 {noun}___ 있어요.", [right],
            ["가" if right == "이" else "이", particle(noun, "을", "를"), "에서"], f"O que existe (있어요) é sujeito: {'com' if has_batchim(noun) else 'sem'} batchim → {right}.")
        right = particle(noun, "이에요", "예요")
        add("kz", "particulas", 1, "ser", "Complete com a forma correta de “ser”.", f"이것은 제 {noun}___.", [right],
            ["예요" if right == "이에요" else "이에요", particle(noun, "을", "를"), "에"], f"{noun} {'tem' if has_batchim(noun) else 'não tem'} batchim → {right}.")
        right = particle(noun, "을", "를")
        add("kz", "particulas", 1, "objeto", "Complete com a partícula de objeto.", f"어제 {noun}___ 샀어요.", [right],
            ["를" if right == "을" else "을", "에", particle(noun, "이", "가")], f"Objeto direto: → {right}.")
    for noun in FOODS:
        right = particle(noun, "을", "를")
        add("kz", "particulas", 1, "objeto", "Complete com a partícula de objeto.", f"저는 {noun}___ 좋아해요.", [right],
            ["를" if right == "을" else "을", "에", "에서"], f"좋아하다 pede objeto: → {right}.")
        right = particle(noun, "이", "가")
        add("kz", "particulas", 1, "sujeito", "Complete com a partícula de sujeito.", f"이 {noun}___ 맛있어요.", [right],
            ["가" if right == "이" else "이", particle(noun, "을", "를"), "에서"], f"O que é descrito (맛있어요) é sujeito → {right}.")
        right = particle(noun, "은", "는")
        add("kz", "particulas", 2, "tópico", "Complete com a partícula de tópico (contraste).", f"{noun}___ 좋아하지만 술은 안 마셔요.", [right],
            ["는" if right == "은" else "은", particle(noun, "이", "가"), "에"], f"Contraste com 은/는 → {right}.")
    for noun in HOBBIES:
        right = particle(noun, "을", "를")
        add("kz", "particulas", 1, "objeto", "Complete com a partícula de objeto.", f"주말에 {noun}___ 좋아해요.", [right],
            ["를" if right == "을" else "을", "에", "에서"], f"Objeto de 좋아하다 → {right}.")
    for place in PLACES_GO:
        add("kz", "particulas", 1, "lugar", "Escolha 에 ou 에서.", f"내일 {place}___ 가요.", ["에"], ["에서", "을", "로"], "Destino de 가다 → 에.")
        add("kz", "particulas", 1, "lugar", "Escolha 에 ou 에서.", f"{place}___ 친구를 만나요.", ["에서"], ["에", "을", "로"], "Lugar onde a ação acontece → 에서.")
    for person in PEOPLE:
        right = particle(person, "과", "와")
        add("kz", "particulas", 1, "e/com", "Complete com 와 ou 과 (com).", f"{person}___ 같이 영화를 봤어요.", [right],
            ["와" if right == "과" else "과", "을", "에서"], f"{'Com' if has_batchim(person) else 'Sem'} batchim → {right}.")
        add("kz", "particulas", 2, "para alguém", "Complete com a partícula “para (alguém)”.", f"{person}___ 선물을 줬어요.", ["한테", "에게"],
            ["에", "에서", "를"], "Para uma pessoa → 한테 (fala) / 에게 (escrita). 에 é para lugares.")

    # ---------------------------------------------------------- vocabulário extra
    by_theme = {}
    for ko, pt, theme, level in C.VOCAB + VOCAB_2:
        by_theme.setdefault(theme, []).append((ko, pt))
    known = {ko for ko, *_ in C.VOCAB}
    for ko, pt, theme, level in VOCAB_2:
        if ko in known:
            continue
        same = by_theme[theme]
        add("kw2", "vocabulario", level, theme, "O que significa?", ko, [pt], pick(rng, [p for _, p in same], [pt]), f"{ko} = {pt}.", audio=ko)
        add("kw2", "vocabulario", level, theme, "Como se diz em coreano?", pt, [ko], pick(rng, [k for k, p in same if p != pt], [ko]), f"“{pt}” em coreano é {ko}.", audio=ko)
        add("kw2", "escuta", level, theme, "Ouça e escolha a palavra que você ouviu.", "🔊", [ko], pick(rng, [k for k, p in same if p != pt], [ko]), f"Você ouviu {ko} ({pt}).", audio=ko)
