"""Conteúdo do Chinese Routine (mandarim, HSK 1–2).

Pinyin com tons de citação (como nos dicionários). Mudanças de tom (sandhi) são
explicadas no guia. Classificadores e partículas são escolhidos por tabela revisada.
Revisão por professor ou falante nativo recomendada antes da venda.
"""

# ------------------------------------------------------------------ tons e pinyin
TONES = [
    ("mā", "妈", "mãe", 1), ("má", "麻", "cânhamo / dormência", 2), ("mǎ", "马", "cavalo", 3), ("mà", "骂", "xingar", 4), ("ma", "吗", "partícula de pergunta", 0),
]
INITIALS = [
    ("b", "爸", "bà"), ("p", "跑", "pǎo"), ("m", "猫", "māo"), ("f", "饭", "fàn"), ("d", "大", "dà"), ("t", "他", "tā"), ("n", "你", "nǐ"),
    ("l", "老", "lǎo"), ("g", "哥", "gē"), ("k", "看", "kàn"), ("h", "好", "hǎo"), ("j", "家", "jiā"), ("q", "去", "qù"), ("x", "小", "xiǎo"),
    ("zh", "中", "zhōng"), ("ch", "吃", "chī"), ("sh", "是", "shì"), ("r", "人", "rén"), ("z", "在", "zài"), ("c", "菜", "cài"), ("s", "四", "sì"),
    ("y", "一", "yī"), ("w", "我", "wǒ"),
]
FINALS = [
    ("a", "八", "bā"), ("o", "我", "wǒ"), ("e", "喝", "hē"), ("i", "你", "nǐ"), ("u", "五", "wǔ"), ("ü", "女", "nǚ"), ("ai", "爱", "ài"),
    ("ei", "黑", "hēi"), ("ao", "好", "hǎo"), ("ou", "狗", "gǒu"), ("an", "饭", "fàn"), ("en", "人", "rén"), ("ang", "忙", "máng"),
    ("eng", "冷", "lěng"), ("ong", "中", "zhōng"), ("er", "二", "èr"), ("ia", "家", "jiā"), ("ie", "谢", "xiè"), ("iao", "小", "xiǎo"),
    ("iu", "六", "liù"), ("ian", "天", "tiān"), ("in", "今", "jīn"), ("iang", "两", "liǎng"), ("ing", "听", "tīng"), ("ua", "花", "huā"),
    ("uo", "多", "duō"), ("uai", "快", "kuài"), ("ui", "对", "duì"), ("uan", "饭馆", "fànguǎn"), ("un", "春", "chūn"), ("ün", "云", "yún"),
    ("üe", "学", "xué"),
]

# ------------------------------------------------------------------ vocabulário
# (hanzi, pinyin, português, tema, nível HSK)
VOCAB = [
    # pessoas
    ("我", "wǒ", "eu", "pessoas", 1), ("你", "nǐ", "você", "pessoas", 1), ("他", "tā", "ele", "pessoas", 1), ("她", "tā", "ela", "pessoas", 1),
    ("我们", "wǒmen", "nós", "pessoas", 1), ("他们", "tāmen", "eles", "pessoas", 1), ("人", "rén", "pessoa", "pessoas", 1),
    ("朋友", "péngyou", "amigo(a)", "pessoas", 1), ("老师", "lǎoshī", "professor(a)", "pessoas", 1), ("学生", "xuésheng", "estudante", "pessoas", 1),
    ("同学", "tóngxué", "colega de classe", "pessoas", 1), ("医生", "yīshēng", "médico(a)", "pessoas", 1), ("妈妈", "māma", "mãe", "pessoas", 1),
    ("爸爸", "bàba", "pai", "pessoas", 1), ("儿子", "érzi", "filho", "pessoas", 1), ("女儿", "nǚ'ér", "filha", "pessoas", 1),
    ("先生", "xiānsheng", "senhor / marido", "pessoas", 1), ("小姐", "xiǎojiě", "senhorita", "pessoas", 1), ("哥哥", "gēge", "irmão mais velho", "pessoas", 2),
    ("姐姐", "jiějie", "irmã mais velha", "pessoas", 2), ("弟弟", "dìdi", "irmão mais novo", "pessoas", 2), ("妹妹", "mèimei", "irmã mais nova", "pessoas", 2),
    ("孩子", "háizi", "criança", "pessoas", 2), ("丈夫", "zhàngfu", "marido", "pessoas", 2), ("妻子", "qīzi", "esposa", "pessoas", 2),
    ("男人", "nánrén", "homem", "pessoas", 2), ("女人", "nǚrén", "mulher", "pessoas", 2), ("服务员", "fúwùyuán", "garçom / atendente", "pessoas", 2),
    ("中国人", "Zhōngguó rén", "chinês (pessoa)", "pessoas", 1), ("歌手", "gēshǒu", "cantor(a)", "pessoas", 2), ("演员", "yǎnyuán", "ator / atriz", "pessoas", 2),
    # comida
    ("米饭", "mǐfàn", "arroz", "comida", 1), ("菜", "cài", "prato / verdura", "comida", 1), ("茶", "chá", "chá", "comida", 1), ("水", "shuǐ", "água", "comida", 1),
    ("苹果", "píngguǒ", "maçã", "comida", 1), ("水果", "shuǐguǒ", "fruta", "comida", 1), ("面条", "miàntiáo", "macarrão", "comida", 2),
    ("咖啡", "kāfēi", "café", "comida", 2), ("牛奶", "niúnǎi", "leite", "comida", 2), ("鸡蛋", "jīdàn", "ovo", "comida", 2), ("西瓜", "xīguā", "melancia", "comida", 2),
    ("面包", "miànbāo", "pão", "comida", 2), ("鱼", "yú", "peixe", "comida", 2), ("羊肉", "yángròu", "carne de carneiro", "comida", 2),
    ("饺子", "jiǎozi", "dumpling (jiaozi)", "comida", 2), ("早饭", "zǎofàn", "café da manhã", "comida", 2), ("午饭", "wǔfàn", "almoço", "comida", 2),
    ("晚饭", "wǎnfàn", "jantar", "comida", 2), ("饭", "fàn", "refeição / arroz", "comida", 1),
    # lugares
    ("中国", "Zhōngguó", "China", "lugares", 1), ("北京", "Běijīng", "Pequim", "lugares", 1), ("上海", "Shànghǎi", "Xangai", "lugares", 2),
    ("学校", "xuéxiào", "escola", "lugares", 1), ("家", "jiā", "casa / família", "lugares", 1), ("医院", "yīyuàn", "hospital", "lugares", 1),
    ("饭馆", "fànguǎn", "restaurante", "lugares", 1), ("商店", "shāngdiàn", "loja", "lugares", 1), ("火车站", "huǒchēzhàn", "estação de trem", "lugares", 1),
    ("机场", "jīchǎng", "aeroporto", "lugares", 2), ("公司", "gōngsī", "empresa", "lugares", 2), ("宾馆", "bīnguǎn", "hotel", "lugares", 2),
    ("教室", "jiàoshì", "sala de aula", "lugares", 2), ("房间", "fángjiān", "quarto", "lugares", 2), ("超市", "chāoshì", "supermercado", "lugares", 2),
    ("书店", "shūdiàn", "livraria", "lugares", 2), ("咖啡馆", "kāfēiguǎn", "cafeteria", "lugares", 2), ("公园", "gōngyuán", "parque", "lugares", 2),
    ("电影院", "diànyǐngyuàn", "cinema", "lugares", 2), ("图书馆", "túshūguǎn", "biblioteca", "lugares", 2), ("银行", "yínháng", "banco", "lugares", 2),
    ("路", "lù", "rua / caminho", "lugares", 2),
    # tempo
    ("今天", "jīntiān", "hoje", "tempo", 1), ("明天", "míngtiān", "amanhã", "tempo", 1), ("昨天", "zuótiān", "ontem", "tempo", 1),
    ("年", "nián", "ano", "tempo", 1), ("月", "yuè", "mês", "tempo", 1), ("星期", "xīngqī", "semana", "tempo", 1), ("点", "diǎn", "hora (no relógio)", "tempo", 1),
    ("分钟", "fēnzhōng", "minuto", "tempo", 1), ("现在", "xiànzài", "agora", "tempo", 1), ("时候", "shíhou", "momento / quando", "tempo", 1),
    ("上午", "shàngwǔ", "manhã", "tempo", 1), ("中午", "zhōngwǔ", "meio-dia", "tempo", 1), ("下午", "xiàwǔ", "tarde", "tempo", 1),
    ("早上", "zǎoshang", "de manhã cedo", "tempo", 2), ("晚上", "wǎnshang", "noite", "tempo", 2), ("去年", "qùnián", "ano passado", "tempo", 2),
    ("小时", "xiǎoshí", "hora (duração)", "tempo", 2), ("生日", "shēngrì", "aniversário", "tempo", 2), ("时间", "shíjiān", "tempo", "tempo", 2),
    ("周末", "zhōumò", "fim de semana", "tempo", 2),
    # objetos
    ("书", "shū", "livro", "objetos", 1), ("桌子", "zhuōzi", "mesa", "objetos", 1), ("椅子", "yǐzi", "cadeira", "objetos", 1), ("杯子", "bēizi", "copo", "objetos", 1),
    ("电脑", "diànnǎo", "computador", "objetos", 1), ("电视", "diànshì", "televisão", "objetos", 1), ("电影", "diànyǐng", "filme", "objetos", 1),
    ("衣服", "yīfu", "roupa", "objetos", 1), ("钱", "qián", "dinheiro", "objetos", 1), ("手机", "shǒujī", "celular", "objetos", 2),
    ("手表", "shǒubiǎo", "relógio de pulso", "objetos", 2), ("票", "piào", "ingresso / passagem", "objetos", 2), ("报纸", "bàozhǐ", "jornal", "objetos", 2),
    ("鞋", "xié", "sapato", "objetos", 2), ("帽子", "màozi", "chapéu / boné", "objetos", 2), ("裤子", "kùzi", "calça", "objetos", 2),
    ("照片", "zhàopiàn", "foto", "objetos", 2), ("地图", "dìtú", "mapa", "objetos", 2), ("信", "xìn", "carta", "objetos", 2), ("汉字", "hànzì", "caractere chinês", "objetos", 1),
    ("汉语", "Hànyǔ", "língua chinesa", "objetos", 1), ("字", "zì", "caractere / letra", "objetos", 1), ("东西", "dōngxi", "coisa", "objetos", 1),
    ("歌", "gē", "canção", "objetos", 2), ("音乐", "yīnyuè", "música", "objetos", 2),
    # natureza e animais
    ("猫", "māo", "gato", "natureza", 1), ("狗", "gǒu", "cachorro", "natureza", 1), ("天气", "tiānqì", "tempo (clima)", "natureza", 1),
    ("雨", "yǔ", "chuva", "natureza", 2), ("雪", "xuě", "neve", "natureza", 2), ("花", "huā", "flor", "natureza", 2), ("太阳", "tàiyáng", "sol", "natureza", 2),
    ("山", "shān", "montanha", "natureza", 2), ("河", "hé", "rio", "natureza", 2),
    # transporte
    ("飞机", "fēijī", "avião", "transporte", 1), ("出租车", "chūzūchē", "táxi", "transporte", 1), ("火车", "huǒchē", "trem", "transporte", 2),
    ("公共汽车", "gōnggòng qìchē", "ônibus", "transporte", 2), ("自行车", "zìxíngchē", "bicicleta", "transporte", 2), ("地铁", "dìtiě", "metrô", "transporte", 2),
    # verbos
    ("是", "shì", "ser", "verbos", 1), ("有", "yǒu", "ter / haver", "verbos", 1), ("在", "zài", "estar em", "verbos", 1), ("去", "qù", "ir", "verbos", 1),
    ("来", "lái", "vir", "verbos", 1), ("回", "huí", "voltar", "verbos", 1), ("吃", "chī", "comer", "verbos", 1), ("喝", "hē", "beber", "verbos", 1),
    ("看", "kàn", "ver / ler / assistir", "verbos", 1), ("听", "tīng", "ouvir", "verbos", 1), ("说", "shuō", "falar", "verbos", 1), ("读", "dú", "ler em voz alta", "verbos", 1),
    ("写", "xiě", "escrever", "verbos", 1), ("买", "mǎi", "comprar", "verbos", 1), ("开", "kāi", "abrir / dirigir", "verbos", 1), ("坐", "zuò", "sentar / ir de (transporte)", "verbos", 1),
    ("住", "zhù", "morar", "verbos", 1), ("学习", "xuéxí", "estudar", "verbos", 1), ("工作", "gōngzuò", "trabalhar", "verbos", 1), ("睡觉", "shuìjiào", "dormir", "verbos", 1),
    ("打电话", "dǎ diànhuà", "telefonar", "verbos", 1), ("做", "zuò", "fazer", "verbos", 1), ("爱", "ài", "amar", "verbos", 1), ("喜欢", "xǐhuan", "gostar", "verbos", 1),
    ("想", "xiǎng", "querer / pensar", "verbos", 1), ("认识", "rènshi", "conhecer", "verbos", 1), ("叫", "jiào", "chamar-se", "verbos", 1), ("会", "huì", "saber (fazer)", "verbos", 1),
    ("能", "néng", "poder (capacidade)", "verbos", 1), ("请", "qǐng", "por favor / convidar", "verbos", 1), ("走", "zǒu", "andar / ir embora", "verbos", 2),
    ("跑步", "pǎobù", "correr", "verbos", 2), ("唱歌", "chànggē", "cantar", "verbos", 2), ("跳舞", "tiàowǔ", "dançar", "verbos", 2), ("游泳", "yóuyǒng", "nadar", "verbos", 2),
    ("旅游", "lǚyóu", "viajar (turismo)", "verbos", 2), ("运动", "yùndòng", "fazer exercício", "verbos", 2), ("准备", "zhǔnbèi", "preparar", "verbos", 2),
    ("知道", "zhīdào", "saber", "verbos", 2), ("觉得", "juéde", "achar / sentir", "verbos", 2), ("希望", "xīwàng", "esperar / desejar", "verbos", 2),
    ("可以", "kěyǐ", "poder (permissão)", "verbos", 2), ("要", "yào", "querer / ir (futuro)", "verbos", 2), ("给", "gěi", "dar", "verbos", 2),
    ("等", "děng", "esperar", "verbos", 2), ("找", "zhǎo", "procurar", "verbos", 2), ("告诉", "gàosu", "contar / dizer", "verbos", 2),
    ("帮助", "bāngzhù", "ajudar", "verbos", 2), ("介绍", "jièshào", "apresentar", "verbos", 2), ("懂", "dǒng", "entender", "verbos", 2),
    ("笑", "xiào", "rir / sorrir", "verbos", 2), ("穿", "chuān", "vestir", "verbos", 2), ("洗", "xǐ", "lavar", "verbos", 2), ("问", "wèn", "perguntar", "verbos", 2),
    ("玩", "wán", "brincar / divertir-se", "verbos", 2), ("卖", "mài", "vender", "verbos", 2), ("上班", "shàngbān", "ir trabalhar", "verbos", 2),
    ("拍", "pāi", "tirar (foto)", "verbos", 2), ("借", "jiè", "pegar emprestado", "verbos", 2), ("学", "xué", "aprender", "verbos", 1),
    # adjetivos
    ("好", "hǎo", "bom", "adjetivos", 1), ("大", "dà", "grande", "adjetivos", 1), ("小", "xiǎo", "pequeno", "adjetivos", 1), ("多", "duō", "muito / muitos", "adjetivos", 1),
    ("少", "shǎo", "pouco", "adjetivos", 1), ("热", "rè", "quente", "adjetivos", 1), ("冷", "lěng", "frio", "adjetivos", 1), ("高兴", "gāoxìng", "contente", "adjetivos", 1),
    ("漂亮", "piàoliang", "bonito(a)", "adjetivos", 1), ("贵", "guì", "caro", "adjetivos", 2), ("便宜", "piányi", "barato", "adjetivos", 2), ("忙", "máng", "ocupado", "adjetivos", 2),
    ("累", "lèi", "cansado", "adjetivos", 2), ("快", "kuài", "rápido", "adjetivos", 2), ("慢", "màn", "devagar", "adjetivos", 2), ("远", "yuǎn", "longe", "adjetivos", 2),
    ("近", "jìn", "perto", "adjetivos", 2), ("新", "xīn", "novo", "adjetivos", 2), ("长", "cháng", "comprido", "adjetivos", 2), ("白", "bái", "branco", "adjetivos", 2),
    ("黑", "hēi", "preto", "adjetivos", 2), ("红", "hóng", "vermelho", "adjetivos", 2), ("好吃", "hǎochī", "gostoso", "adjetivos", 2), ("快乐", "kuàilè", "feliz", "adjetivos", 2),
    ("容易", "róngyì", "fácil", "adjetivos", 2), ("难", "nán", "difícil", "adjetivos", 2), ("晴", "qíng", "ensolarado", "adjetivos", 2), ("阴", "yīn", "nublado", "adjetivos", 2),
    # k-pop / c-drama e cultura
    ("电视剧", "diànshìjù", "série / drama de TV", "cultura", 2), ("演唱会", "yǎnchànghuì", "show", "cultura", 2), ("春节", "Chūnjié", "Ano-Novo Chinês", "cultura", 2),
    ("熊猫", "xióngmāo", "panda", "cultura", 2), ("长城", "Chángchéng", "Grande Muralha", "cultura", 2), ("筷子", "kuàizi", "hashi (pauzinhos)", "cultura", 2),
]

# Classificadores: (substantivo, classificador, pinyin do classificador, explicação)
MEASURES = [
    ("书", "本", "běn", "livros e cadernos"), ("杂志", "本", "běn", "livros e revistas"), ("咖啡", "杯", "bēi", "bebidas em copo/xícara"),
    ("茶", "杯", "bēi", "bebidas em copo/xícara"), ("水", "杯", "bēi", "bebidas em copo"), ("衣服", "件", "jiàn", "roupas da parte de cima e assuntos"),
    ("照片", "张", "zhāng", "objetos planos: fotos, mapas, mesas"), ("地图", "张", "zhāng", "objetos planos"), ("票", "张", "zhāng", "ingressos e passagens"),
    ("桌子", "张", "zhāng", "mesas (superfície plana)"), ("鞋", "双", "shuāng", "pares"), ("筷子", "双", "shuāng", "pares"),
    ("裤子", "条", "tiáo", "coisas longas e finas: calças, ruas, rios, peixes"), ("鱼", "条", "tiáo", "peixes (longos)"), ("路", "条", "tiáo", "ruas"),
    ("河", "条", "tiáo", "rios"), ("猫", "只", "zhī", "animais pequenos"), ("狗", "只", "zhī", "animais (cães podem usar 条 também)"),
    ("牛奶", "瓶", "píng", "garrafas"), ("面条", "碗", "wǎn", "tigelas"), ("米饭", "碗", "wǎn", "tigelas"), ("信", "封", "fēng", "cartas"),
    ("电影", "部", "bù", "filmes e obras"), ("电视剧", "部", "bù", "séries"), ("帽子", "顶", "dǐng", "chapéus"), ("手机", "部", "bù", "aparelhos (celular; 个 também é comum)"),
    ("车", "辆", "liàng", "veículos"), ("自行车", "辆", "liàng", "veículos"), ("电脑", "台", "tái", "máquinas e aparelhos"), ("电视", "台", "tái", "aparelhos"),
    ("人", "个", "gè", "classificador geral, pessoas"), ("苹果", "个", "gè", "classificador geral"), ("朋友", "个", "gè", "pessoas"), ("学生", "个", "gè", "pessoas"),
    ("老师", "位", "wèi", "pessoas, de forma respeitosa"), ("医生", "位", "wèi", "pessoas, respeitoso"), ("花", "朵", "duǒ", "flores"),
    ("歌", "首", "shǒu", "canções e poemas"), ("西瓜", "个", "gè", "classificador geral"), ("房间", "个", "gè", "classificador geral"),
]
# Classificadores que nunca servem para o substantivo (distratores seguros).
MEASURE_SET = ["本", "杯", "件", "张", "双", "条", "只", "瓶", "碗", "封", "部", "顶", "辆", "台", "位", "朵", "首"]
# Alguns substantivos aceitam mais de um classificador: não usar estes como distratores.
MEASURE_ALSO = {"狗": {"条"}, "手机": {"台"}, "电脑": {"部"}, "电视": {"部"}, "老师": {"个"}, "医生": {"个"}, "车": {"台"}, "桌子": {"个"}}
NUMBERS_CL = [("两", "liǎng"), ("三", "sān"), ("四", "sì"), ("五", "wǔ")]

# Frases para completar (2–3 lacunas)
COMBO_SUBJECTS = [("我", "wǒ"), ("你", "nǐ"), ("他", "tā"), ("她", "tā"), ("我们", "wǒmen"), ("他们", "tāmen"), ("老师", "lǎoshī"),
                  ("朋友", "péngyou"), ("妈妈", "māma"), ("爸爸", "bàba"), ("哥哥", "gēge"), ("姐姐", "jiějie")]
# (lugar, verbo, objeto, classificador)
COMBO_ACTIVITIES = [
    ("咖啡馆", "喝", "咖啡", "杯"), ("书店", "买", "书", "本"), ("商店", "买", "衣服", "件"), ("饭馆", "吃", "面条", "碗"),
    ("超市", "买", "苹果", "个"), ("电影院", "看", "电影", "部"), ("公园", "拍", "照片", "张"), ("家", "写", "信", "封"),
    ("学校", "学", "汉字", "个"), ("图书馆", "借", "书", "本"), ("超市", "买", "西瓜", "个"), ("茶馆", "喝", "茶", "杯"),
    ("商店", "买", "鞋", "双"), ("商店", "买", "裤子", "条"), ("宠物店", "买", "猫", "只"), ("书店", "买", "地图", "张"),
    ("家", "做", "菜", "个"), ("面包店", "买", "面包", "个"), ("超市", "买", "牛奶", "瓶"), ("商店", "买", "帽子", "顶"),
]

# Gramática: (frase com ___, resposta, distratores, explicação, nível, tema)
GRAMMAR = [
    # 不 × 没
    ("我每天都___喝咖啡。", "不", ["没", "吗", "了"], "Hábito (每天 = todo dia) → 不 (“não bebo café”).", 1, "不 × 没"),
    ("昨天我___去学校。", "没", ["不", "吗", "的"], "Passado (昨天) → 没 (“não fui”).", 1, "不 × 没"),
    ("他___是老师，他是医生。", "不", ["没", "很", "在"], "是 é negado sempre com 不.", 1, "不 × 没"),
    ("我___有钱。", "没", ["不", "很", "是"], "有 é negado sempre com 没 (没有).", 1, "不 × 没"),
    ("明天我___去上班。", "不", ["没", "了", "过"], "Futuro/intenção → 不.", 1, "不 × 没"),
    ("我还___吃饭。", "没", ["很", "了", "是"], "“Ainda não comi” → 还没.", 2, "不 × 没"),
    ("她___喜欢下雨。", "不", ["没", "了", "的"], "Gosto/estado → 不.", 1, "不 × 没"),
    ("上个星期他___来。", "没", ["不", "吗", "很"], "Passado → 没.", 2, "不 × 没"),
    # 吗 / 呢 / 吧
    ("你是中国人___？", "吗", ["呢", "的", "了"], "Pergunta de sim/não → 吗 no fim.", 1, "perguntas"),
    ("我很好，你___？", "呢", ["吗", "的", "了"], "“E você?” (pergunta de volta) → 呢.", 1, "perguntas"),
    ("你喜欢喝茶___？", "吗", ["呢", "的", "得"], "Sim/não → 吗.", 1, "perguntas"),
    ("我是学生，你___？", "呢", ["吗", "了", "得"], "“E você?” → 呢.", 1, "perguntas"),
    ("你有___个孩子？", "几", ["谁", "什么", "哪"], "Quantidade pequena esperada → 几 + classificador.", 1, "perguntas"),
    ("这是___？", "什么", ["几", "哪", "吗"], "“O que é isto?” → 什么.", 1, "perguntas"),
    ("你___哪儿？", "去", ["是", "的", "吗"], "“Aonde você vai?” → 去哪儿.", 1, "perguntas"),
    ("他是___？", "谁", ["几", "多少", "哪"], "“Quem é ele?” → 谁.", 1, "perguntas"),
    ("这个苹果___钱？", "多少", ["几", "什么", "谁"], "Preço → 多少钱.", 1, "perguntas"),
    # 的 / 得
    ("这是我___书。", "的", ["得", "了", "在"], "Posse → 的.", 1, "的 × 得"),
    ("他说汉语说___很好。", "得", ["的", "了", "地"], "Complemento de grau depois do verbo → 得.", 2, "的 × 得"),
    ("她是我___朋友。", "的", ["得", "是", "了"], "Posse/relação → 的.", 1, "的 × 得"),
    ("你跑___很快。", "得", ["的", "了", "吗"], "Como a ação é feita → verbo + 得.", 2, "的 × 得"),
    ("这是谁___手机？", "的", ["得", "吗", "了"], "De quem → 谁的.", 1, "的 × 得"),
    ("她唱歌唱___很好听。", "得", ["的", "了", "地"], "Verbo + 得 + avaliação.", 2, "的 × 得"),
    # 在 progressivo / lugar
    ("我___家看电视。", "在", ["是", "有", "和"], "Lugar da ação → 在 + lugar + verbo.", 1, "在"),
    ("他___看书呢。", "在", ["是", "了", "过"], "Ação em andamento → 在 + verbo (+ 呢).", 2, "在"),
    ("妈妈___做饭呢。", "在", ["了", "过", "是"], "Progressivo → 在.", 2, "在"),
    ("我的手机___桌子上。", "在", ["是", "有", "去"], "Onde algo está → 在.", 1, "在"),
    # 了 / 过
    ("我刚才买___一本书。", "了", ["着", "的", "得"], "Ação concluída (刚才 = agora há pouco) → 了.", 2, "了 × 过"),
    ("你以前去___中国吗？", "过", ["着", "在", "得"], "Experiência (“já foi alguma vez?”) → 过.", 2, "了 × 过"),
    ("我吃___北京烤鸭，很好吃。", "过", ["着", "在", "得"], "Experiência na vida → 过.", 2, "了 × 过"),
    ("昨天我看___一个电影。", "了", ["着", "在", "得"], "Ação concluída ontem → 了.", 2, "了 × 过"),
    # 会 / 能 / 可以
    ("我___说汉语。", "会", ["是", "在", "有"], "Habilidade aprendida → 会.", 1, "会/能/可以"),
    ("这里___拍照吗？", "可以", ["会", "是", "在"], "Permissão → 可以.", 2, "会/能/可以"),
    ("明天你___来吗？", "能", ["是", "在", "有"], "Possibilidade/condição de vir → 能.", 1, "会/能/可以"),
    ("他___游泳。", "会", ["是", "有", "在"], "Saber nadar (habilidade aprendida) → 会.", 1, "会/能/可以"),
    # 想 / 要
    ("我___去中国旅游。", "想", ["是", "在", "有"], "Desejo → 想.", 1, "想 × 要"),
    ("你___喝什么？", "要", ["是", "在", "有"], "Pedido / querer → 要.", 2, "想 × 要"),
    # 太…了 / 很
    ("这个___贵了！", "太", ["是", "在", "的"], "Excesso: 太 … 了.", 1, "graus"),
    ("今天天气___好。", "很", ["了", "得", "的"], "Adjetivo como predicado costuma levar 很.", 1, "graus"),
    ("这个菜太好吃___！", "了", ["的", "得", "吗"], "太 … 了.", 1, "graus"),
    # 比
    ("哥哥___我高。", "比", ["和", "跟", "很"], "Comparação: A 比 B + adjetivo.", 2, "comparação"),
    ("今天___昨天冷。", "比", ["跟", "很", "也"], "A 比 B + adjetivo.", 2, "comparação"),
    ("我___他一样高。", "跟", ["比", "很", "是"], "Igualdade: A 跟 B 一样 + adjetivo.", 2, "comparação"),
    # 也 / 都 / 和
    ("我是学生，他___是学生。", "也", ["都", "和", "很"], "“Também” → 也 antes do verbo.", 1, "advérbios"),
    ("我们___是中国人。", "都", ["很", "和", "的"], "“Todos” → 都 antes do verbo.", 1, "advérbios"),
    ("我___妈妈去商店。", "和", ["也", "都", "很"], "“Eu e a mamãe” → 和 liga substantivos.", 1, "advérbios"),
    # 是…的 / 因为…所以
    ("我是坐飞机来___。", "的", ["了", "得", "吗"], "Destaque de como algo aconteceu: 是 … 的.", 2, "estruturas"),
    ("因为下雨，___我不去公园。", "所以", ["但是", "因为", "和"], "因为 … 所以 … (porque … então …).", 2, "estruturas"),
    ("我喜欢咖啡，___他喜欢茶。", "但是", ["所以", "因为", "也"], "Contraste → 但是.", 2, "estruturas"),
    ("你去北京___去上海？", "还是", ["或者", "和", "也"], "Escolha em pergunta: A 还是 B? (或者 é para afirmações).", 2, "estruturas"),
]

# Números, datas e dinheiro: (resposta, português, distratores)
NUMBERS = [
    ("三点", "3 horas", ["三个点", "三小时", "第三点"]), ("两点", "2 horas", ["二点", "两个点", "二小时"]),
    ("十二点", "12 horas", ["十二小时", "二十点", "十两点"]), ("三点半", "3h30", ["三点三十", "半三点", "三半点"]),
    ("两个小时", "duas horas (duração)", ["两点", "二个小时", "两小时点"]), ("十分钟", "10 minutos", ["十分", "十点钟", "一十分钟"]),
    ("五块钱", "5 yuan (falado)", ["五钱块", "五个钱", "五点钱"]), ("一百块", "100 yuan", ["十百块", "一千块", "百一块"]),
    ("一千块", "1.000 yuan", ["十百块", "一万块", "千一块"]), ("一万", "10.000", ["十千", "一千", "万一"]),
    ("两个人", "duas pessoas", ["二个人", "两人个", "二人"]), ("二十", "20", ["两十", "十二", "二十个"]),
    ("十一", "11", ["一十一", "一十", "两十一"]), ("一月一号", "1º de janeiro", ["一号一月", "一月第一", "一个月一号"]),
    ("星期一", "segunda-feira", ["星期日", "一星期", "第一星期"]), ("星期天", "domingo", ["星期七", "星期一", "天星期"]),
    ("二〇二六年", "o ano de 2026 (dígito a dígito)", ["两千二十六年", "二六年", "二十二六年"]), ("三岁", "3 anos (idade)", ["三年", "三个年", "三点"]),
    ("第一", "primeiro", ["一第", "第一个第", "首一"]), ("十月", "outubro", ["十个月", "月十", "第十月份"]),
]

# Frases úteis: (hanzi, pinyin, português, contexto)
PHRASES = [
    ("你好", "nǐ hǎo", "Olá", ""), ("谢谢", "xièxie", "Obrigado(a)", ""), ("不客气", "bú kèqi", "De nada", ""), ("对不起", "duìbuqǐ", "Desculpe", ""),
    ("没关系", "méi guānxi", "Não tem problema", ""), ("再见", "zàijiàn", "Tchau", ""), ("请问", "qǐngwèn", "Com licença, posso perguntar…", ""),
    ("我叫……", "wǒ jiào", "Meu nome é…", "apresentação"), ("认识你很高兴", "rènshi nǐ hěn gāoxìng", "Prazer em conhecer", ""),
    ("多少钱？", "duōshao qián", "Quanto custa?", ""), ("我听不懂", "wǒ tīng bu dǒng", "Não entendo (o que ouço)", ""),
    ("请再说一遍", "qǐng zài shuō yí biàn", "Pode repetir, por favor?", ""), ("请慢一点儿说", "qǐng màn yìdiǎnr shuō", "Fale mais devagar, por favor", ""),
    ("洗手间在哪儿？", "xǐshǒujiān zài nǎr", "Onde fica o banheiro?", ""), ("我要这个", "wǒ yào zhège", "Quero este", ""),
    ("太好了！", "tài hǎo le", "Ótimo!", ""), ("加油！", "jiāyóu", "Força! / Vamos lá!", "incentivo"), ("我爱你", "wǒ ài nǐ", "Eu te amo", ""),
    ("生日快乐", "shēngrì kuàilè", "Feliz aniversário", ""), ("新年快乐", "xīnnián kuàilè", "Feliz Ano-Novo", ""), ("干杯！", "gānbēi", "Saúde! (brinde)", ""),
    ("好久不见", "hǎojiǔ bú jiàn", "Quanto tempo!", ""), ("你吃饭了吗？", "nǐ chīfàn le ma", "Já comeu? (cumprimento)", "cumprimento comum"),
    ("没问题", "méi wèntí", "Sem problema", ""), ("真的吗？", "zhēnde ma", "Sério?", ""), ("我不知道", "wǒ bù zhīdào", "Não sei", ""),
    ("好的", "hǎo de", "Tudo bem / Combinado", ""), ("等一下", "děng yíxià", "Espere um pouco", ""), ("祝你好运", "zhù nǐ hǎoyùn", "Boa sorte", ""),
    ("晚安", "wǎn'ān", "Boa noite (ao dormir)", ""),
]

GUIDE = [
    ("Os quatro tons", "O mandarim tem 4 tons e um neutro. 1º alto e reto (mā), 2º subindo (má), 3º desce e sobe (mǎ), 4º descendo seco (mà), neutro leve (ma). Mudar o tom muda a palavra: 妈 mā = mãe, 马 mǎ = cavalo."),
    ("Mudanças de tom (sandhi)", "3º + 3º → o primeiro vira 2º: 你好 nǐ hǎo soa ní hǎo. 不 vira bú antes de 4º tom (不是 bú shì). 一 vira yí antes de 4º tom e yì antes dos outros. O pinyin dos dicionários mostra o tom original."),
    ("Pinyin", "É a escrita do som com letras latinas. Atenção: q soa “tch” (去 qù), x soa “ch” suave (小 xiǎo), zh/ch/sh com a língua para trás, c soa “ts” (菜 cài), ü é como o “u” francês."),
    ("Ordem da frase", "Sujeito + tempo + lugar + verbo + objeto: 我 今天 在家 看 书 (Eu hoje em casa leio livro). Tempo e lugar vêm antes do verbo."),
    ("是 — ser", "Liga substantivos: 我是学生 (sou estudante). Com adjetivos não se usa 是: 我很忙 (estou ocupado), não 我是忙."),
    ("Perguntas com 吗 e 呢", "Coloque 吗 no fim para sim/não: 你好吗？ 呢 devolve a pergunta: 我很好，你呢？ (E você?). Palavras interrogativas (什么, 谁, 哪儿, 几, 多少) ficam no lugar da resposta, sem 吗."),
    ("不 × 没", "不 nega hábitos, vontades, futuro e 是: 我不喝咖啡. 没 nega o passado e o verbo 有: 我昨天没去, 我没有钱."),
    ("Classificadores", "Entre número e substantivo vai um classificador: 一本书, 两杯咖啡, 三张照片. 个 é o geral. Antes de classificador, “dois” é 两, não 二."),
    ("了 e 过", "了 depois do verbo marca ação concluída: 我买了一本书. 过 marca experiência de vida: 我去过中国 (já fui à China)."),
    ("在 — lugar e ação em andamento", "在 + lugar antes do verbo: 我在家看书. 在 + verbo indica ação em andamento: 他在看书呢."),
    ("的 × 得", "的 liga posse/descrição ao substantivo: 我的书. 得 liga o verbo à avaliação: 他说得很好."),
    ("会 × 能 × 可以", "会 = habilidade aprendida (我会说汉语). 能 = conseguir / ter condição (明天我能来). 可以 = permissão (这里可以拍照吗？)."),
    ("Comparações", "A 比 B + adjetivo: 哥哥比我高. Igualdade: A 跟 B 一样 + adjetivo."),
    ("Números e dinheiro", "Números são lógicos: 十一 (11), 二十 (20), 一百 (100). Dinheiro falado: 块 (yuan); horas: 点; duração: 小时; minutos: 分钟."),
]
