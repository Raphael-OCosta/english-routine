"""Questões extras do Chinese Routine (expansão para ~10 mil).

Geradas DEPOIS das originais e com prefixos próprios (zx, zy, zz, zw2), para que os IDs
antigos — e o histórico dos alunos — não mudem.
"""

SUBJECTS_2 = [("同学", "tóngxué"), ("医生", "yīshēng"), ("弟弟", "dìdi"), ("妹妹", "mèimei"), ("我们老师", "wǒmen lǎoshī"), ("你朋友", "nǐ péngyou"),
              ("我爸爸", "wǒ bàba"), ("我妈妈", "wǒ māma"), ("王先生", "Wáng xiānsheng"), ("李小姐", "Lǐ xiǎojiě"), ("孩子们", "háizimen"), ("她们", "tāmen")]
# (lugar, verbo, objeto, classificador)
ACTIVITIES_2 = [
    ("书店", "买", "杂志", "本"), ("饭馆", "吃", "饺子", "个"), ("咖啡馆", "喝", "牛奶", "杯"), ("超市", "买", "鸡蛋", "个"),
    ("商店", "买", "手表", "块"), ("电影院", "看", "电视剧", "部"), ("公园", "画", "花", "朵"), ("学校", "写", "汉字", "个"),
    ("图书馆", "看", "报纸", "份"), ("商场", "买", "裙子", "条"), ("水果店", "买", "西瓜", "个"), ("家", "做", "面条", "碗"),
    ("机场", "买", "票", "张"), ("宾馆", "订", "房间", "个"), ("教室", "唱", "歌", "首"), ("医院", "拿", "药", "盒"),
    ("银行", "办", "卡", "张"), ("车站", "等", "朋友", "个"), ("茶馆", "喝", "茶", "壶"), ("商店", "买", "袜子", "双"),
]
EXTRA_READINGS = {
    "我们老师": "wǒmen lǎoshī", "你朋友": "nǐ péngyou", "我爸爸": "wǒ bàba", "我妈妈": "wǒ māma", "王先生": "Wáng xiānsheng", "李小姐": "Lǐ xiǎojiě",
    "孩子们": "háizimen", "手表": "shǒubiǎo", "画": "huà", "裙子": "qúnzi", "订": "dìng", "拿": "ná", "药": "yào", "盒": "hé", "换": "huàn",
    "卡": "kǎ", "车站": "chēzhàn", "壶": "hú", "袜子": "wàzi", "份": "fèn", "正在": "zhèngzài", "以后": "yǐhòu", "每天": "měitiān", "常常": "chángcháng",
    "上个周末": "shàng ge zhōumò", "下个月": "xià ge yuè", "已经": "yǐjīng", "从来": "cónglái", "一起": "yìqǐ", "跟": "gēn",
}
# Classificadores que também servem para estes objetos (nunca viram distrator).
ALSO_2 = {"茶": {"杯", "壶"}, "药": {"瓶", "盒"}, "牛奶": {"瓶", "杯"}, "报纸": {"份", "张"}, "手表": {"只", "块"}, "裙子": {"条", "件"},
          "袜子": {"双", "只"}, "饺子": {"个", "盘", "碗"}, "面条": {"碗"}, "卡": {"张"}, "票": {"张"}, "电视剧": {"部"}, "花": {"朵", "束"}}
TIMES_PAST = ["昨天", "上个周末", "前天", "去年"]
TIMES_FUTURE = ["明天", "下个月", "后天", "明年"]


def build_more(add, slot, pick, rng, C):
    subjects = [s for s, _ in C.COMBO_SUBJECTS] + [s for s, _ in SUBJECTS_2]
    activities = C.COMBO_ACTIVITIES + ACTIVITIES_2
    old = {(s, a) for s, _ in C.COMBO_SUBJECTS for a in C.COMBO_ACTIVITIES}
    also = {k: set(v) for k, v in C.MEASURE_ALSO.items()}
    for k, v in ALSO_2.items():
        also.setdefault(k, set()).update(v)

    def zai():
        return slot("在", ["是", "有", "和"], "lugar da ação (在)")

    def cl_slot(obj, cl):
        bad = [m for m in C.MEASURE_SET if m != cl and m not in also.get(obj, set())]
        return slot(cl, pick(rng, bad, [cl]), "classificador")

    for a in activities:
        place, verb, obj, cl = a
        for k, subj in enumerate(subjects):
            num = C.NUMBERS_CL[k % 4][0]
            if (subj, a) not in old:
                full = f"{subj}在{place}{verb}{obj}吗？"
                add("zx", "completar", 1, "pergunta", "Complete as duas lacunas (lugar e pergunta).", f"{subj}___{place}{verb}{obj}___？",
                    ["在 · 吗"], ["-"], f"在 + lugar antes do verbo; 吗 no fim → pergunta. {full}", audio=full,
                    slots=[zai(), slot("吗", ["的", "得", "很"], "pergunta")])
                full = f"昨天{subj}在{place}{verb}了{num}{cl}{obj}。"
                add("zx", "completar", 2, "classificadores", "Complete as duas lacunas (lugar e classificador).", f"昨天{subj}___{place}{verb}了{num}___{obj}。",
                    [f"在 · {cl}"], ["-"], f"在 + lugar; {cl} é o classificador de {obj}. {full}", audio=full, slots=[zai(), cl_slot(obj, cl)])
                add("zx", "completar", 2, "passado", "Complete as três lacunas (lugar, ação concluída e classificador).", f"昨天{subj}___{place}{verb}___{num}___{obj}。",
                    [f"在 · 了 · {cl}"], ["-"], f"在 + lugar; 了 marca ação concluída; {cl} para {obj}. {full}", audio=full,
                    slots=[zai(), slot("了", ["着", "的", "得"], "ação concluída"), cl_slot(obj, cl)])
            # novos formatos para todas as combinações
            past_t, fut_t = TIMES_PAST[k % 4], TIMES_FUTURE[(k + len(place)) % 4]
            full = f"{past_t}{subj}没在{place}{verb}{obj}。"
            add("zx", "completar", 1, "não (passado)", "Complete as duas lacunas (negação no passado e lugar).", f"{past_t}{subj}___{'___'}{place}{verb}{obj}。",
                ["没 · 在"], ["-"], f"Passado → 没 (não 不); 在 + lugar. {full}", audio=full,
                slots=[slot("没", ["不", "很", "了"], "negação"), zai()])
            full = f"{fut_t}{subj}要在{place}{verb}{num}{cl}{obj}。"
            add("zx", "completar", 2, "futuro", "Complete as duas lacunas (lugar e classificador).", f"{fut_t}{subj}要___{place}{verb}{num}___{obj}。",
                [f"在 · {cl}"], ["-"], f"要 + verbo = vai fazer; 在 + lugar; {cl} para {obj}. {full}", audio=full, slots=[zai(), cl_slot(obj, cl)])
            full = f"{subj}想去{place}{verb}{num}{cl}{obj}。"
            add("zx", "completar", 1, "querer", "Complete as duas lacunas (querer e classificador).", f"{subj}___去{place}{verb}{num}___{obj}。",
                [f"想 · {cl}"], ["-"], f"想 + verbo = querer; {cl} para {obj}. {full}", audio=full,
                slots=[slot("想", ["是", "在", "有"], "querer"), cl_slot(obj, cl)])
            full = f"{subj}以前在{place}{verb}过{obj}吗？"
            add("zx", "completar", 2, "experiência", "Complete as duas lacunas (lugar e experiência).", f"{subj}以前___{place}{verb}___{obj}吗？",
                ["在 · 过"], ["-"], f"在 + lugar; 过 depois do verbo = já fez alguma vez. {full}", audio=full,
                slots=[zai(), slot("过", ["着", "在", "得"], "experiência")])
            full = f"{subj}常常在哪儿{verb}{obj}？"
            add("zx", "completar", 1, "pergunta", "Complete a pergunta (onde?).", f"{subj}常常在___{verb}{obj}？", ["哪儿"], ["什么", "谁", "几"],
                f"Lugar → 哪儿, no lugar da resposta (sem 吗). {full}", audio=full)
            full = f"{subj}每天都不{verb}{obj}。"
            add("zx", "completar", 1, "não (hábito)", "Complete a frase (hábito negativo).", f"{subj}每天都___{verb}{obj}。", ["不"], ["没", "吗", "了"],
                f"Hábito (每天) → 不. {full}", audio=full)

    # ---------------------------------------------------------- zy: classificadores com todos os números
    nums = [("一", "yī"), ("两", "liǎng"), ("三", "sān"), ("四", "sì"), ("五", "wǔ"), ("六", "liù"), ("七", "qī"), ("八", "bā"), ("九", "jiǔ"), ("十", "shí")]
    for noun, cl, clpy, why in C.MEASURES:
        for num, _ in nums:
            bad = [m for m in C.MEASURE_SET if m != cl and m not in also.get(noun, set())]
            add("zy", "classificadores", 1 if cl in "个本杯张" else 2, "classificadores", "Complete com o classificador.", f"这里有{num}___{noun}。",
                [cl], pick(rng, bad, [cl]), f"{cl} ({clpy}): {why}.", audio=f"这里有{num}{cl}{noun}。")
        add("zy", "classificadores", 1, "dois", "“Dois” antes de classificador:", f"___{cl}{noun}", ["两"], ["二", "第二", "二个"],
            "Antes de classificador, “dois” é 两 (liǎng), não 二.", audio=f"两{cl}{noun}")
