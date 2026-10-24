"""Conteúdo do Japanese Routine (JLPT N5–N4).

Leituras escritas à mão (kanji → kana). Formas -masu são regulares a partir do radical;
a forma -te vem de tabela revisada. Revisão por professor ou falante nativo recomendada
antes da venda.
"""

# ------------------------------------------------------------------ vocabulário
# (palavra, leitura em kana, português, tema, nível 1 = N5 / 2 = N4)
VOCAB = [
    # pessoas
    ("私", "わたし", "eu", "pessoas", 1), ("あなた", "あなた", "você", "pessoas", 1), ("人", "ひと", "pessoa", "pessoas", 1),
    ("友だち", "ともだち", "amigo(a)", "pessoas", 1), ("先生", "せんせい", "professor(a)", "pessoas", 1), ("学生", "がくせい", "estudante", "pessoas", 1),
    ("母", "はは", "minha mãe", "pessoas", 1), ("父", "ちち", "meu pai", "pessoas", 1), ("お母さん", "おかあさん", "mãe (de alguém)", "pessoas", 1),
    ("お父さん", "おとうさん", "pai (de alguém)", "pessoas", 1), ("兄", "あに", "meu irmão mais velho", "pessoas", 1), ("姉", "あね", "minha irmã mais velha", "pessoas", 1),
    ("弟", "おとうと", "irmão mais novo", "pessoas", 1), ("妹", "いもうと", "irmã mais nova", "pessoas", 1), ("子ども", "こども", "criança", "pessoas", 1),
    ("家族", "かぞく", "família", "pessoas", 1), ("医者", "いしゃ", "médico(a)", "pessoas", 2), ("会社員", "かいしゃいん", "funcionário de empresa", "pessoas", 2),
    ("店員", "てんいん", "atendente de loja", "pessoas", 2), ("歌手", "かしゅ", "cantor(a)", "pessoas", 2),
    # comida
    ("ご飯", "ごはん", "arroz / refeição", "comida", 1), ("水", "みず", "água", "comida", 1), ("お茶", "おちゃ", "chá", "comida", 1),
    ("コーヒー", "コーヒー", "café", "comida", 1), ("パン", "パン", "pão", "comida", 1), ("肉", "にく", "carne", "comida", 1), ("魚", "さかな", "peixe", "comida", 1),
    ("野菜", "やさい", "verdura", "comida", 1), ("果物", "くだもの", "fruta", "comida", 1), ("卵", "たまご", "ovo", "comida", 1),
    ("すし", "すし", "sushi", "comida", 1), ("ラーメン", "ラーメン", "lámen", "comida", 1), ("朝ご飯", "あさごはん", "café da manhã", "comida", 1),
    ("昼ご飯", "ひるごはん", "almoço", "comida", 1), ("晩ご飯", "ばんごはん", "jantar", "comida", 1), ("牛乳", "ぎゅうにゅう", "leite", "comida", 2),
    ("おにぎり", "おにぎり", "bolinho de arroz", "comida", 2), ("料理", "りょうり", "comida / culinária", "comida", 2), ("お弁当", "おべんとう", "marmita (bentô)", "comida", 2),
    # lugares
    ("家", "いえ", "casa", "lugares", 1), ("学校", "がっこう", "escola", "lugares", 1), ("会社", "かいしゃ", "empresa", "lugares", 1),
    ("駅", "えき", "estação", "lugares", 1), ("病院", "びょういん", "hospital", "lugares", 1), ("図書館", "としょかん", "biblioteca", "lugares", 1),
    ("銀行", "ぎんこう", "banco", "lugares", 1), ("公園", "こうえん", "parque", "lugares", 1), ("店", "みせ", "loja", "lugares", 1),
    ("レストラン", "レストラン", "restaurante", "lugares", 1), ("トイレ", "トイレ", "banheiro", "lugares", 1), ("部屋", "へや", "quarto", "lugares", 1),
    ("日本", "にほん", "Japão", "lugares", 1), ("東京", "とうきょう", "Tóquio", "lugares", 1), ("空港", "くうこう", "aeroporto", "lugares", 2),
    ("映画館", "えいがかん", "cinema", "lugares", 2), ("スーパー", "スーパー", "supermercado", "lugares", 2), ("コンビニ", "コンビニ", "loja de conveniência", "lugares", 2),
    ("デパート", "デパート", "loja de departamentos", "lugares", 2), ("海", "うみ", "mar", "lugares", 2), ("山", "やま", "montanha", "lugares", 2), ("町", "まち", "cidade (bairro)", "lugares", 2),
    # tempo
    ("今日", "きょう", "hoje", "tempo", 1), ("明日", "あした", "amanhã", "tempo", 1), ("昨日", "きのう", "ontem", "tempo", 1), ("今", "いま", "agora", "tempo", 1),
    ("朝", "あさ", "manhã", "tempo", 1), ("夜", "よる", "noite", "tempo", 1), ("毎日", "まいにち", "todos os dias", "tempo", 1), ("週末", "しゅうまつ", "fim de semana", "tempo", 1),
    ("時間", "じかん", "tempo / horas", "tempo", 1), ("今年", "ことし", "este ano", "tempo", 1), ("来年", "らいねん", "ano que vem", "tempo", 1), ("去年", "きょねん", "ano passado", "tempo", 1),
    ("毎朝", "まいあさ", "toda manhã", "tempo", 2), ("午前", "ごぜん", "antes do meio-dia", "tempo", 2), ("午後", "ごご", "à tarde", "tempo", 2), ("来週", "らいしゅう", "semana que vem", "tempo", 2),
    # objetos
    ("本", "ほん", "livro", "objetos", 1), ("車", "くるま", "carro", "objetos", 1), ("電話", "でんわ", "telefone", "objetos", 1), ("かばん", "かばん", "bolsa", "objetos", 1),
    ("傘", "かさ", "guarda-chuva", "objetos", 1), ("時計", "とけい", "relógio", "objetos", 1), ("お金", "おかね", "dinheiro", "objetos", 1), ("写真", "しゃしん", "foto", "objetos", 1),
    ("映画", "えいが", "filme", "objetos", 1), ("音楽", "おんがく", "música", "objetos", 1), ("歌", "うた", "canção", "objetos", 1), ("服", "ふく", "roupa", "objetos", 1),
    ("靴", "くつ", "sapato", "objetos", 2), ("切符", "きっぷ", "bilhete / passagem", "objetos", 2), ("手紙", "てがみ", "carta", "objetos", 2), ("新聞", "しんぶん", "jornal", "objetos", 2),
    ("パソコン", "パソコン", "computador", "objetos", 2), ("スマホ", "スマホ", "celular (smartphone)", "objetos", 2), ("漢字", "かんじ", "kanji", "objetos", 1), ("日本語", "にほんご", "língua japonesa", "objetos", 1),
    # natureza e transporte
    ("天気", "てんき", "tempo (clima)", "natureza", 1), ("雨", "あめ", "chuva", "natureza", 1), ("雪", "ゆき", "neve", "natureza", 2), ("花", "はな", "flor", "natureza", 1),
    ("犬", "いぬ", "cachorro", "natureza", 1), ("猫", "ねこ", "gato", "natureza", 1), ("桜", "さくら", "cerejeira", "natureza", 2),
    ("電車", "でんしゃ", "trem", "transporte", 1), ("バス", "バス", "ônibus", "transporte", 1), ("飛行機", "ひこうき", "avião", "transporte", 1),
    ("自転車", "じてんしゃ", "bicicleta", "transporte", 1), ("地下鉄", "ちかてつ", "metrô", "transporte", 2), ("新幹線", "しんかんせん", "trem-bala", "transporte", 2),
    # verbos (forma de dicionário)
    ("行く", "いく", "ir", "verbos", 1), ("来る", "くる", "vir", "verbos", 1), ("帰る", "かえる", "voltar para casa", "verbos", 1), ("食べる", "たべる", "comer", "verbos", 1),
    ("飲む", "のむ", "beber", "verbos", 1), ("見る", "みる", "ver", "verbos", 1), ("聞く", "きく", "ouvir / perguntar", "verbos", 1), ("読む", "よむ", "ler", "verbos", 1),
    ("書く", "かく", "escrever", "verbos", 1), ("買う", "かう", "comprar", "verbos", 1), ("話す", "はなす", "falar", "verbos", 1), ("する", "する", "fazer", "verbos", 1),
    ("寝る", "ねる", "dormir", "verbos", 1), ("起きる", "おきる", "acordar", "verbos", 1), ("会う", "あう", "encontrar (alguém)", "verbos", 1), ("待つ", "まつ", "esperar", "verbos", 1),
    ("作る", "つくる", "fazer / preparar", "verbos", 2), ("泳ぐ", "およぐ", "nadar", "verbos", 2), ("歌う", "うたう", "cantar", "verbos", 2), ("遊ぶ", "あそぶ", "brincar / sair (lazer)", "verbos", 2),
    ("働く", "はたらく", "trabalhar", "verbos", 2), ("休む", "やすむ", "descansar", "verbos", 2), ("勉強する", "べんきょうする", "estudar", "verbos", 1), ("分かる", "わかる", "entender", "verbos", 2),
    # adjetivos
    ("大きい", "おおきい", "grande", "adjetivos", 1), ("小さい", "ちいさい", "pequeno", "adjetivos", 1), ("高い", "たかい", "caro / alto", "adjetivos", 1), ("安い", "やすい", "barato", "adjetivos", 1),
    ("新しい", "あたらしい", "novo", "adjetivos", 1), ("古い", "ふるい", "velho (coisa)", "adjetivos", 1), ("おいしい", "おいしい", "gostoso", "adjetivos", 1), ("暑い", "あつい", "quente (clima)", "adjetivos", 1),
    ("寒い", "さむい", "frio (clima)", "adjetivos", 1), ("楽しい", "たのしい", "divertido", "adjetivos", 1), ("忙しい", "いそがしい", "ocupado", "adjetivos", 1), ("難しい", "むずかしい", "difícil", "adjetivos", 1),
    ("易しい", "やさしい", "fácil", "adjetivos", 2), ("静か", "しずか", "silencioso", "adjetivos", 1), ("きれい", "きれい", "bonito / limpo", "adjetivos", 1), ("元気", "げんき", "animado / bem de saúde", "adjetivos", 1),
    ("好き", "すき", "gostar (adj.)", "adjetivos", 1), ("有名", "ゆうめい", "famoso", "adjetivos", 2), ("便利", "べんり", "prático", "adjetivos", 2), ("にぎやか", "にぎやか", "animado (lugar)", "adjetivos", 2),
]

# Verbos: (dicionário, radical -masu, leitura do radical, forma -te, português, complemento, nível)
VERBS = [
    ("行く", "行き", "いき", "行って", "ir", "学校へ", 1), ("来る", "来", "き", "来て", "vir", "日本へ", 1), ("帰る", "帰り", "かえり", "帰って", "voltar", "家へ", 1),
    ("食べる", "食べ", "たべ", "食べて", "comer", "すしを", 1), ("飲む", "飲み", "のみ", "飲んで", "beber", "お茶を", 1), ("見る", "見", "み", "見て", "ver", "映画を", 1),
    ("聞く", "聞き", "きき", "聞いて", "ouvir", "音楽を", 1), ("読む", "読み", "よみ", "読んで", "ler", "本を", 1), ("書く", "書き", "かき", "書いて", "escrever", "手紙を", 1),
    ("買う", "買い", "かい", "買って", "comprar", "パンを", 1), ("話す", "話し", "はなし", "話して", "falar", "日本語を", 1), ("寝る", "寝", "ね", "寝て", "dormir", "十一時に", 1),
    ("起きる", "起き", "おき", "起きて", "acordar", "七時に", 1), ("会う", "会い", "あい", "会って", "encontrar", "友だちに", 1), ("待つ", "待ち", "まち", "待って", "esperar", "バスを", 1),
    ("作る", "作り", "つくり", "作って", "fazer", "料理を", 2), ("泳ぐ", "泳ぎ", "およぎ", "泳いで", "nadar", "海で", 2), ("歌う", "歌い", "うたい", "歌って", "cantar", "歌を", 2),
    ("遊ぶ", "遊び", "あそび", "遊んで", "sair / brincar", "公園で", 2), ("働く", "働き", "はたらき", "働いて", "trabalhar", "会社で", 2), ("休む", "休み", "やすみ", "休んで", "descansar", "家で", 2),
    ("勉強する", "勉強し", "べんきょうし", "勉強して", "estudar", "日本語を", 1), ("する", "し", "し", "して", "fazer", "テニスを", 1), ("撮る", "撮り", "とり", "撮って", "tirar (foto)", "写真を", 2),
]
SUBJECT_TIMES = {"present": "毎日", "past": "昨日", "future": "明日"}

# Adjetivos: (adjetivo, tipo i/na, frase-sujeito, português)
ADJECTIVES = [
    ("高い", "i", "このかばんは", "caro"), ("安い", "i", "このパンは", "barato"), ("大きい", "i", "あの家は", "grande"), ("小さい", "i", "私の部屋は", "pequeno"),
    ("おいしい", "i", "このラーメンは", "gostoso"), ("暑い", "i", "今日は", "quente"), ("寒い", "i", "東京の冬は", "frio"), ("楽しい", "i", "パーティーは", "divertido"),
    ("忙しい", "i", "父は", "ocupado"), ("難しい", "i", "漢字は", "difícil"), ("新しい", "i", "この車は", "novo"), ("古い", "i", "あのお寺は", "velho"),
    ("静か", "na", "図書館は", "silencioso"), ("きれい", "na", "この花は", "bonito"), ("元気", "na", "おばあさんは", "animado"), ("有名", "na", "この店は", "famoso"),
    ("便利", "na", "電車は", "prático"), ("にぎやか", "na", "この町は", "animado (lugar)"),
]

# Partículas: (frase com ___, resposta, distratores, explicação, nível)
PARTICLES = [
    ("私___学生です。", "は", ["を", "で", "に"], "は marca o tópico: “Quanto a mim, sou estudante”.", 1),
    ("毎朝コーヒー___飲みます。", "を", ["が", "で", "に"], "を marca o objeto direto.", 1),
    ("図書館___本を読みます。", "で", ["に", "を", "へ"], "で = lugar onde a ação acontece.", 1),
    ("明日、東京___行きます。", "に", ["で", "を", "が"], "に (ou へ) = destino de movimento.", 1),
    ("部屋に猫___います。", "が", ["を", "で", "へ"], "Com います/あります, o que existe leva が.", 1),
    ("これは私___本です。", "の", ["は", "を", "で"], "の = posse (o livro de mim → meu livro).", 1),
    ("友だち___映画を見ました。", "と", ["を", "で", "に"], "と = com (companhia).", 1),
    ("七時___起きます。", "に", ["で", "を", "が"], "Hora exata leva に.", 1),
    ("バス___学校へ行きます。", "で", ["に", "を", "の"], "で = meio (de ônibus).", 1),
    ("私___日本語が好きです。", "は", ["を", "で", "に"], "Tópico は; o que se gosta leva が.", 1),
    ("私は日本語___好きです。", "が", ["を", "で", "に"], "好き usa が para o que se gosta.", 1),
    ("兄は医者です。姉___医者です。", "も", ["を", "で", "に"], "も = também (substitui は).", 1),
    ("駅___学校まで歩きます。", "から", ["まで", "で", "を"], "から = de (ponto de partida); まで = até.", 2),
    ("九時___五時まで働きます。", "から", ["まで", "に", "で"], "から … まで = das … às.", 2),
    ("机の上___本があります。", "に", ["で", "を", "が"], "Lugar onde algo existe (com あります) leva に.", 1),
    ("日本語___話せますか。", "が", ["に", "で", "へ"], "Forma potencial costuma usar が para o objeto.", 2),
    ("これは何___か。", "です", ["ます", "の", "を"], "Pergunta “o que é?”: 何ですか.", 1),
    ("先生___手紙を書きました。", "に", ["で", "を", "が"], "に = para quem (destinatário).", 2),
    ("公園___散歩します。", "を", ["に", "が", "へ"], "Caminhar por um lugar: を (公園を散歩する).", 2),
    ("雨___降っています。", "が", ["を", "に", "で"], "Fenômenos naturais: 雨が降る.", 2),
]

NUMBERS = [
    ("三百", "さんびゃく", ["さんひゃく", "さんぴゃく", "みひゃく"]), ("六百", "ろっぴゃく", ["ろくひゃく", "ろくびゃく", "むひゃく"]),
    ("八百", "はっぴゃく", ["はちひゃく", "はちびゃく", "やひゃく"]), ("四時", "よじ", ["しじ", "よんじ", "よじかん"]), ("九時", "くじ", ["きゅうじ", "ここのじ", "くじかん"]),
    ("七時", "しちじ", ["ななじ", "しちじかん", "なのじ"]), ("四月", "しがつ", ["よんがつ", "よがつ", "しげつ"]), ("九月", "くがつ", ["きゅうがつ", "ここのがつ", "くげつ"]),
    ("一つ", "ひとつ", ["いちつ", "ひとり", "いっこ"]), ("二つ", "ふたつ", ["につ", "ふたり", "にこ"]), ("一人", "ひとり", ["いちにん", "いちり", "ひとつ"]),
    ("二人", "ふたり", ["ににん", "にり", "ふたつ"]), ("三人", "さんにん", ["みにん", "さんり", "みっつ"]), ("二十歳", "はたち", ["にじゅっさい", "にじゅうさい", "ふたとし"]),
    ("一日", "ついたち", ["いちにち", "ひとひ", "いっか"]), ("二日", "ふつか", ["ににち", "ふたか", "にか"]), ("十日", "とおか", ["じゅうにち", "とおにち", "じゅっか"]),
    ("千円", "せんえん", ["いっせんえん", "ちえん", "せんねん"]), ("一万円", "いちまんえん", ["まんえん", "ひとまんえん", "いちまえん"]), ("三本", "さんぼん", ["さんほん", "さんぽん", "みほん"]),
]

PHRASES = [
    ("こんにちは", "Olá / Boa tarde", ""), ("おはようございます", "Bom dia", ""), ("こんばんは", "Boa noite (cumprimento)", ""), ("ありがとうございます", "Muito obrigado(a)", ""),
    ("すみません", "Com licença / Desculpe", ""), ("ごめんなさい", "Desculpe (pedido de desculpa)", ""), ("はじめまして", "Muito prazer (1º encontro)", ""),
    ("よろしくお願いします", "Conto com você / Prazer", "apresentação"), ("いただきます", "Bom apetite (antes de comer)", ""), ("ごちそうさまでした", "Obrigado pela refeição", "depois de comer"),
    ("いくらですか", "Quanto custa?", ""), ("トイレはどこですか", "Onde fica o banheiro?", ""), ("分かりません", "Não entendo", ""),
    ("もう一度お願いします", "Mais uma vez, por favor", ""), ("ゆっくりお願いします", "Mais devagar, por favor", ""), ("おやすみなさい", "Boa noite (ao dormir)", ""),
    ("さようなら", "Adeus / Tchau", ""), ("またね", "Até mais", "informal"), ("お元気ですか", "Como vai?", ""), ("元気です", "Estou bem", ""),
    ("大丈夫です", "Tudo bem / Está ok", ""), ("お願いします", "Por favor", ""), ("これをください", "Me dá isto, por favor", ""), ("おめでとうございます", "Parabéns", ""),
    ("がんばって", "Força! / Boa sorte", "incentivo"), ("すごい！", "Incrível!", ""), ("かわいい！", "Que fofo!", ""), ("乾杯！", "Saúde! (brinde)", ""),
    ("いってきます", "Já vou (ao sair de casa)", ""), ("ただいま", "Cheguei (ao voltar para casa)", ""),
]

# Completar (2–3 lacunas)
COMBO_SUBJECTS = ["私", "田中さん", "友だち", "母", "父", "兄", "姉", "先生", "学生", "キムさん", "マリアさん", "弟"]
# (lugar, objeto, radical -masu do verbo)
COMBO_ACTIVITIES = [
    ("図書館", "本", "読み"), ("カフェ", "コーヒー", "飲み"), ("レストラン", "すし", "食べ"), ("公園", "写真", "撮り"),
    ("スーパー", "野菜", "買い"), ("家", "テレビ", "見"), ("学校", "日本語", "勉強し"), ("部屋", "音楽", "聞き"),
    ("会社", "メール", "書き"), ("デパート", "服", "買い"), ("台所", "料理", "作り"), ("駅", "切符", "買い"),
    ("映画館", "映画", "見"), ("パン屋", "パン", "買い"), ("喫茶店", "お茶", "飲み"), ("教室", "漢字", "練習し"),
    ("カラオケ", "歌", "歌い"), ("体育館", "バスケットボール", "し"), ("コンビニ", "おにぎり", "買い"), ("海", "魚", "釣り"),
]

GUIDE = [
    ("Três escritas", "Hiragana (palavras japonesas e terminações), katakana (palavras estrangeiras: コーヒー) e kanji (ideogramas com significado: 山 = montanha). Uma frase mistura as três."),
    ("Ordem da frase", "Sujeito/tópico + complementos + verbo no fim: 私は 毎朝 コーヒーを 飲みます (Eu toda manhã café bebo)."),
    ("は × が", "は marca o tópico (do que se fala): 私は学生です. が marca o sujeito que existe ou é destacado: 猫がいます, 日本語が好きです."),
    ("を, に, で, へ", "を = objeto (本を読む). に = destino, hora, onde algo está (七時に, 東京に行く). で = lugar da ação e meio (図書館で, バスで). へ = direção (≈ に com movimento)."),
    ("の, と, も, から, まで", "の = posse (私の本). と = com / e (友だちと). も = também (私も). から … まで = de … até."),
    ("Verbos -masu", "Educado: radical + ます (飲みます). Negativo ません, passado ました, passado negativo ませんでした, querer たいです (飲みたいです)."),
    ("Forma -te", "Liga frases e pede coisas: 飲んで, 書いて, 行って (irregular), 来て, して. てください = por favor faça; ています = ação em andamento."),
    ("Adjetivos い e な", "い: 高い → 高くない (negativo) → 高かった (passado). な: 静か → 静かじゃない → 静かだった; antes de substantivo: 静かな町."),
    ("Existência: います × あります", "います para seres vivos que se movem (人, 猫). あります para coisas e plantas (本, 花)."),
    ("Números e contadores", "Leituras mudam: 三百 さんびゃく, 六百 ろっぴゃく, 八百 はっぴゃく, 四時 よじ, 九時 くじ, 四月 しがつ. Pessoas: 一人 ひとり, 二人 ふたり, depois 三人 さんにん. Coisas: ひとつ, ふたつ…"),
    ("Polidez", "Formas -masu/-desu são educadas e servem em quase tudo. さん após o nome dos outros (nunca no próprio nome)."),
    ("Romaji", "Usamos Hepburn com vogais longas dobradas (コーヒー koohii, 学校 gakkou). Partículas は/へ/を se leem wa/e/o."),
]
