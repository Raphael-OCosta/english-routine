"""Questões extras do Japanese Routine (expansão para ~10 mil).

Geradas DEPOIS das originais e com prefixos próprios (jx, jy, jz, jw2), para que os IDs
antigos — e o histórico dos alunos — não mudem.
"""

SUBJECTS_2 = ["鈴木さん", "山田さん", "祖母", "祖父", "子どもたち", "店長", "医者", "会社員", "留学生", "リーさん", "ジョンさん", "妹"]
# (lugar, objeto, radical -masu)
ACTIVITIES_2 = [
    ("本屋", "雑誌", "買い"), ("公園", "お弁当", "食べ"), ("家", "宿題", "し"), ("図書館", "新聞", "読み"), ("部屋", "日記", "書き"),
    ("劇場", "芝居", "見"), ("デパート", "かばん", "買い"), ("台所", "ラーメン", "作り"), ("会社", "報告書", "書き"), ("スタジオ", "写真", "撮り"),
    ("花屋", "花", "買い"), ("体育館", "バレーボール", "し"), ("教室", "単語", "覚え"), ("コンサート", "音楽", "聞き"), ("居間", "掃除", "し"),
    ("レストラン", "ステーキ", "食べ"), ("カフェ", "ケーキ", "食べ"), ("市場", "果物", "買い"), ("駅", "友だち", "待ち"), ("海", "写真", "撮り"),
]
READINGS = {
    "鈴木さん": "すずきさん", "山田さん": "やまださん", "祖母": "そぼ", "子どもたち": "こどもたち", "留学生": "りゅうがくせい", "リーさん": "リーさん",
    "ジョンさん": "ジョンさん", "本屋": "ほんや", "雑誌": "ざっし", "お弁当": "おべんとう", "宿題": "しゅくだい", "日記": "にっき", "劇場": "げきじょう",
    "芝居": "しばい", "報告書": "ほうこくしょ", "単語": "たんご", "居間": "いま", "掃除": "そうじ", "市場": "いちば", "あまり": "あまり",
    "ふだん": "ふだん", "先週": "せんしゅう", "来週": "らいしゅう", "時々": "ときどき", "よく": "よく", "毎晩": "まいばん", "冷蔵庫": "れいぞうこ", "財布": "さいふ", "鉛筆": "えんぴつ",
    "机": "つくえ", "椅子": "いす", "鏡": "かがみ", "眼鏡": "めがね", "帽子": "ぼうし", "辞書": "じしょ", "地図": "ちず", "窓": "まど",
    "階段": "かいだん", "庭": "にわ", "池": "いけ", "鳥": "とり", "寿司": "すし", "天ぷら": "てんぷら", "味噌汁": "みそしる", "お菓子": "おかし",
    "納豆": "なっとう", "緑茶": "りょくちゃ", "紅茶": "こうちゃ", "牛肉": "ぎゅうにく", "豚肉": "ぶたにく", "鶏肉": "とりにく", "趣味": "しゅみ",
    "野球": "やきゅう", "水泳": "すいえい", "旅行": "りょこう", "料理": "りょうり", "読書": "どくしょ", "山登り": "やまのぼり", "映画館": "えいがかん",
    "美術館": "びじゅつかん", "博物館": "はくぶつかん", "郵便局": "ゆうびんきょく", "薬局": "やっきょく", "ホテル": "ホテル", "温泉": "おんせん",
    "神社": "じんじゃ", "お寺": "おてら", "大阪": "おおさか", "京都": "きょうと", "沖縄": "おきなわ", "北海道": "ほっかいどう", "友だちの家": "ともだちのいえ",
}
TIME_SUBJECTS = ["田中さん", "母", "友だち", "兄", "先生", "学生"]
THINGS = ["本", "かばん", "傘", "時計", "財布", "鉛筆", "机", "椅子", "鏡", "眼鏡", "帽子", "辞書", "地図", "パソコン", "スマホ", "冷蔵庫", "テレビ", "写真"]
FOODS = ["すし", "天ぷら", "ラーメン", "味噌汁", "お菓子", "納豆", "緑茶", "紅茶", "コーヒー", "牛肉", "豚肉", "鶏肉", "果物", "野菜", "パン", "ケーキ", "おにぎり", "卵"]
HOBBIES = ["音楽", "映画", "野球", "水泳", "旅行", "料理", "読書", "山登り", "アニメ", "ゲーム", "ダンス", "カラオケ"]
PLACES_GO = ["学校", "会社", "病院", "銀行", "駅", "公園", "図書館", "スーパー", "デパート", "映画館", "美術館", "博物館", "郵便局", "薬局", "ホテル",
             "温泉", "神社", "お寺", "海", "山", "大阪", "京都", "沖縄", "北海道", "友だちの家"]
ANIMALS = ["犬", "猫", "鳥"]
VOCAB_2 = [
    ("財布", "さいふ", "carteira", "objetos", 1), ("鉛筆", "えんぴつ", "lápis", "objetos", 1), ("机", "つくえ", "mesa (de estudo)", "objetos", 1),
    ("椅子", "いす", "cadeira", "objetos", 1), ("鏡", "かがみ", "espelho", "objetos", 2), ("眼鏡", "めがね", "óculos", "objetos", 1),
    ("帽子", "ぼうし", "chapéu / boné", "objetos", 1), ("辞書", "じしょ", "dicionário", "objetos", 1), ("地図", "ちず", "mapa", "objetos", 1),
    ("冷蔵庫", "れいぞうこ", "geladeira", "objetos", 2), ("雑誌", "ざっし", "revista", "objetos", 1), ("宿題", "しゅくだい", "dever de casa", "objetos", 1),
    ("日記", "にっき", "diário", "objetos", 2), ("単語", "たんご", "palavra (vocabulário)", "objetos", 1), ("天ぷら", "てんぷら", "tempurá", "comida", 1),
    ("味噌汁", "みそしる", "sopa de missô", "comida", 1), ("お菓子", "おかし", "doces / salgadinhos", "comida", 1), ("納豆", "なっとう", "natto (soja fermentada)", "comida", 2),
    ("緑茶", "りょくちゃ", "chá verde", "comida", 1), ("紅茶", "こうちゃ", "chá preto", "comida", 1), ("牛肉", "ぎゅうにく", "carne bovina", "comida", 2),
    ("豚肉", "ぶたにく", "carne de porco", "comida", 2), ("鶏肉", "とりにく", "frango", "comida", 2), ("お弁当", "おべんとう", "marmita (bentô)", "comida", 1),
    ("美術館", "びじゅつかん", "museu de arte", "lugares", 2), ("博物館", "はくぶつかん", "museu", "lugares", 2), ("郵便局", "ゆうびんきょく", "correio", "lugares", 2),
    ("薬局", "やっきょく", "farmácia", "lugares", 2), ("温泉", "おんせん", "fonte termal", "lugares", 1), ("神社", "じんじゃ", "santuário xintoísta", "lugares", 1),
    ("本屋", "ほんや", "livraria", "lugares", 1), ("市場", "いちば", "mercado", "lugares", 2), ("居間", "いま", "sala de estar", "lugares", 2), ("庭", "にわ", "jardim / quintal", "lugares", 2),
    ("野球", "やきゅう", "beisebol", "hobbies", 1), ("水泳", "すいえい", "natação", "hobbies", 1), ("読書", "どくしょ", "leitura (hobby)", "hobbies", 2),
    ("山登り", "やまのぼり", "montanhismo", "hobbies", 2), ("掃除", "そうじ", "limpeza", "hobbies", 1), ("鳥", "とり", "pássaro", "natureza", 1),
    ("祖母", "そぼ", "minha avó", "pessoas", 1), ("留学生", "りゅうがくせい", "intercambista", "pessoas", 2),
]


def build_more(add, slot, accept, pick, rng, C, K):
    K.add_readings(list(READINGS.items()))
    subjects = C.COMBO_SUBJECTS + SUBJECTS_2
    activities = C.COMBO_ACTIVITIES + ACTIVITIES_2
    old = {(s, a) for s in C.COMBO_SUBJECTS for a in C.COMBO_ACTIVITIES}

    def wa():
        return slot("は", ["を", "で", "に"], "tópico")

    def de():
        return slot("で", ["に", "を", "へ"], "lugar da ação")

    def wo():
        return slot("を", ["で", "に", "へ"], "objeto")

    def ni():
        return slot("に", ["で", "を", "の"], "destino")

    # ---------------------------------------------------------- jx: completar
    for act in activities:
        place, obj, stem = act
        for k, subj in enumerate(subjects):
            if (subj, act) not in old:
                add("jx", "completar", 1, "partículas", "Complete as três partículas (tópico, lugar da ação e objeto).", f"{subj}___{place}___{obj}___{stem}ます。",
                    ["は · で · を"], ["-"], f"は tópico; で lugar da ação; を objeto. {subj}は{place}で{obj}を{stem}ます。",
                    audio=f"{subj}は{place}で{obj}を{stem}ます。", slots=[wa(), de(), wo()])
                add("jx", "completar", 1, "destino", "Complete as duas partículas (tópico e destino).", f"{subj}___{place}___行きます。", ["は · に"], ["-"],
                    f"は tópico; に (ou へ) destino. {subj}は{place}に行きます。", audio=f"{subj}は{place}に行きます。", slots=[wa(), ni()])
                add("jx", "completar", 2, "passado", "Complete as três lacunas (lugar, objeto e verbo no passado).", f"昨日、{subj}は{place}___{obj}______。",
                    [f"で · を · {stem}ました"], ["-"], f"昨日 pede passado: {stem}ました.", audio=f"昨日、{subj}は{place}で{obj}を{stem}ました。",
                    slots=[de(), wo(), slot(f"{stem}ました", [f"{stem}ます", f"{stem}ません", f"{stem}たいです"], "verbo no passado")])
            add("jx", "completar", 1, "futuro", "Complete as lacunas (amanhã: verbo -masu).", f"明日、{subj}は{place}___{obj}______。",
                [f"で · を · {stem}ます"], ["-"], f"Futuro em japonês = forma -masu: {stem}ます.", audio=f"明日、{subj}は{place}で{obj}を{stem}ます。",
                slots=[de(), wo(), slot(f"{stem}ます", [f"{stem}ました", f"{stem}ませんでした", f"{stem}たかったです"], "verbo")])
            add("jx", "completar", 2, "negativo", "Complete as lacunas (あまり pede negativo).", f"{subj}はあまり{place}___{obj}______。",
                [f"で · を · {stem}ません"], ["-"], f"あまり + negativo = não … muito: {stem}ません.", audio=f"{subj}はあまり{place}で{obj}を{stem}ません。",
                slots=[de(), wo(), slot(f"{stem}ません", [f"{stem}ます", f"{stem}ました", f"{stem}たいです"], "verbo negativo")])
            add("jx", "completar", 2, "forma -te", "Complete as partículas (forma -te liga as ações).", f"{subj}は{place}___行って、{obj}___{stem}ました。",
                ["に · を"], ["-"], f"Destino → に; objeto → を; 行って liga “foi e …”.", audio=f"{subj}は{place}に行って、{obj}を{stem}ました。", slots=[ni(), wo()])
            add("jx", "completar", 2, "pergunta", "Complete as três partículas (pergunta no passado).", f"{subj}___{place}___{obj}___{stem}ましたか。",
                ["は · で · を"], ["-"], f"Pergunta: frase + か. {subj}は{place}で{obj}を{stem}ましたか。", audio=f"{subj}は{place}で{obj}を{stem}ましたか。",
                slots=[wa(), de(), wo()])
            add("jx", "completar", 2, "passado negativo", "Complete as lacunas (先週 + não fez).", f"先週、{subj}は{place}___{obj}______。",
                [f"で · を · {stem}ませんでした"], ["-"], f"Passado negativo: {stem}ませんでした.", audio=f"先週、{subj}は{place}で{obj}を{stem}ませんでした。",
                slots=[de(), wo(), slot(f"{stem}ませんでした", [f"{stem}ません", f"{stem}ました", f"{stem}ます"], "passado negativo")])
            friend = "友だち" if subj != "友だち" else "先生"
            add("jx", "completar", 1, "companhia", "Complete as partículas (com quem e destino).", f"{subj}は{friend}___{place}___行きました。", ["と · に"], ["-"],
                f"と = com (companhia); に = destino.", audio=f"{subj}は{friend}と{place}に行きました。",
                slots=[slot("と", ["を", "で", "が"], "companhia"), ni()])

    # ---------------------------------------------------------- jy: verbos com outros sujeitos
    for dic, stem, stem_kana, te, pt, comp, level in C.VERBS:
        for subj in TIME_SUBJECTS:
            forms = [stem + "ます", stem + "ました", stem + "ません", stem + "ませんでした"]
            for time, right, why in (("毎日", forms[0], "Hábito → -ます."), ("昨日", forms[1], "Ontem → -ました."),
                                     ("あまり", forms[2], "あまり pede negativo → -ません.")):
                text = f"{subj}は{time}{comp}___。"
                add("jy", "verbos", 1 if time != "あまり" else 2, "verbos", f"Complete com {dic} ({pt}).", text, accept(right), [f for f in forms if f != right],
                    why, audio=text.replace("___", right))

    # ---------------------------------------------------------- jz: partículas com o vocabulário
    for noun in THINGS:
        add("jz", "particulas", 1, "existência", "Complete com a partícula.", f"机の上に{noun}___あります。", accept("が"), ["を", "で", "へ"],
            "O que existe (あります/います) leva が.", audio=f"机の上に{noun}があります。")
        add("jz", "particulas", 1, "objeto", "Complete com a partícula.", f"昨日{noun}___買いました。", accept("を"), ["が", "で", "に"],
            "Objeto direto → を.", audio=f"昨日{noun}を買いました。")
        add("jz", "particulas", 1, "posse", "Complete com a partícula.", f"これは私___{noun}です。", accept("の"), ["は", "を", "で"], "Posse → の.",
            audio=f"これは私の{noun}です。")
    for noun in FOODS:
        add("jz", "particulas", 1, "好き", "Complete com a partícula.", f"私は{noun}___好きです。", accept("が"), ["を", "で", "に"], "好き usa が.",
            audio=f"私は{noun}が好きです。")
        add("jz", "particulas", 1, "objeto", "Complete com a partícula.", f"毎朝{noun}___食べます。" if noun not in ("緑茶", "紅茶", "コーヒー") else f"毎朝{noun}___飲みます。",
            accept("を"), ["が", "で", "に"], "Objeto direto → を.")
    for hobby in HOBBIES:
        add("jz", "particulas", 1, "好き", "Complete com a partícula.", f"{hobby}___好きです。", accept("が"),
            ["を", "で", "に"], "好き usa が.", audio=f"{hobby}が好きです。")
    for place in PLACES_GO:
        add("jz", "particulas", 1, "destino", "Complete com a partícula.", f"来週{place}___行きます。", accept("に"), ["で", "を", "が"],
            "Destino → に (ou へ).", audio=f"来週{place}に行きます。")
        add("jz", "particulas", 1, "lugar da ação", "Complete com a partícula.", f"{place}___友だちに会いました。", accept("で"), ["に", "を", "へ"],
            "Lugar onde a ação acontece → で.", audio=f"{place}で友だちに会いました。")
    for animal in ANIMALS:
        add("jz", "particulas", 1, "existência", "Complete com a partícula.", f"庭に{animal}___います。", accept("が"), ["を", "で", "へ"],
            "Seres vivos que existem → が + います.", audio=f"庭に{animal}がいます。")

    # ---------------------------------------------------------- vocabulário extra
    by_theme = {}
    for w, kana, pt, theme, level in C.VOCAB + VOCAB_2:
        by_theme.setdefault(theme, []).append((w, pt))
    known = {w for w, *_ in C.VOCAB}
    for w, kana, pt, theme, level in VOCAB_2:
        if w in known:
            continue
        same = by_theme.get(theme, [])
        add("jw2", "vocabulario", level, theme, "O que significa?", w, [pt], pick(rng, [p for _, p in same], [pt]), f"{w} ({kana}) = {pt}.", audio=w)
        add("jw2", "vocabulario", level, theme, "Como se diz em japonês?", pt, accept(w), pick(rng, [x for x, p in same if p != pt], [w]), f"“{pt}” = {w} ({kana}).", audio=w)
        add("jw2", "leitura", level, theme, "Como se lê?", w, accept(kana), pick(rng, [k for _, k, *_ in VOCAB_2 if k != kana], [kana]), f"{w} lê-se {kana}.", audio=w)
