"""Reading, Writing, Listening e Speaking do Japanese Routine (JLPT N5–N4).

Esquema comum de skills/ (docs/PADRAO-IDIOMAS.md). Perguntas em português.
Textos originais; pessoas e grupos são fictícios.
"""

L1, L2 = "N5", "N4"


def q(question, options, answer, why):
    return {"question": question, "options": options, "answer": answer, "why": why}


TEXTS = [
    {"id": "jr001", "level": L1, "topic": "apresentação", "title": "Prazer, eu sou a Yuki",
     "text": "はじめまして。私は山田ゆきです。二十歳です。大阪に住んでいます。大学生です。大学で英語を勉強しています。\n\n"
             "私は音楽が好きです。週末は友だちとカラオケに行きます。よろしくお願いします。",
     "translation": "Muito prazer. Eu sou Yamada Yuki. Tenho vinte anos. Moro em Osaka. Sou universitária. Estudo inglês na universidade.\n\n"
                    "Eu gosto de música. No fim de semana vou ao karaokê com amigos. Prazer em conhecer.",
     "questions": [q("Onde Yuki mora?", ["Osaka", "Tóquio", "Quioto", "Brasil"], 0, "大阪に住んでいます."),
                   q("O que ela estuda?", ["Inglês", "Japonês", "Música", "Medicina"], 0, "英語を勉強しています."),
                   q("O que faz no fim de semana?", ["Vai ao karaokê com amigos", "Trabalha", "Viaja", "Estuda"], 0, "友だちとカラオケに行きます.")]},
    {"id": "jr002", "level": L1, "topic": "rotina", "title": "Meu dia",
     "text": "私は毎朝六時に起きます。朝ご飯にパンを食べて、コーヒーを飲みます。七時半に電車で会社へ行きます。\n\n"
             "会社は九時から六時までです。夜は家で晩ご飯を作ります。十一時に寝ます。",
     "translation": "Eu acordo às seis toda manhã. No café da manhã como pão e tomo café. Às sete e meia vou de trem para a empresa.\n\n"
                    "O trabalho é das nove às seis. À noite preparo o jantar em casa. Durmo às onze.",
     "questions": [q("A que horas a pessoa acorda?", ["Às 6h", "Às 7h", "Às 9h", "Às 11h"], 0, "六時に起きます."),
                   q("Como vai para a empresa?", ["De trem", "De ônibus", "A pé", "De bicicleta"], 0, "電車で会社へ行きます."),
                   q("O que faz à noite?", ["Prepara o jantar em casa", "Vai ao cinema", "Estuda", "Encontra amigos"], 0, "家で晩ご飯を作ります.")]},
    {"id": "jr003", "level": L1, "topic": "família", "title": "Minha família",
     "text": "私の家族は四人です。父と母と弟と私です。父は会社員です。母は病院で働いています。\n\n"
             "弟は高校生です。サッカーが好きです。日曜日はみんなで晩ご飯を食べます。",
     "translation": "Minha família tem quatro pessoas: meu pai, minha mãe, meu irmão mais novo e eu. Meu pai é funcionário de empresa. Minha mãe trabalha num hospital.\n\n"
                    "Meu irmão está no ensino médio. Gosta de futebol. No domingo todos jantamos juntos.",
     "questions": [q("Quantas pessoas há na família?", ["Quatro", "Três", "Cinco", "Seis"], 0, "家族は四人です."),
                   q("Onde a mãe trabalha?", ["Num hospital", "Numa escola", "Numa empresa", "Numa loja"], 0, "母は病院で働いています."),
                   q("Do que o irmão gosta?", ["Futebol", "Música", "Tênis", "Natação"], 0, "サッカーが好きです.")]},
    {"id": "jr004", "level": L1, "topic": "café", "title": "Na cafeteria",
     "text": "店員：いらっしゃいませ。ご注文は？\n\n客：アイスコーヒーをひとつください。\n\n店員：サイズはどうしますか。\n\n"
             "客：Mサイズでお願いします。いくらですか。\n\n店員：四百五十円です。\n\n客：はい。ありがとうございます。",
     "translation": "Atendente: Bem-vindo. O que vai pedir?\n\nCliente: Um café gelado, por favor.\n\nAtendente: Qual tamanho?\n\n"
                    "Cliente: Médio, por favor. Quanto é?\n\nAtendente: São 450 ienes.\n\nCliente: Aqui está. Obrigado.",
     "questions": [q("O que o cliente pede?", ["Café gelado", "Chá", "Suco", "Leite"], 0, "アイスコーヒーをひとつ."),
                   q("Que tamanho escolhe?", ["Médio", "Grande", "Pequeno", "Não diz"], 0, "Mサイズ."),
                   q("Quanto custa?", ["450 ienes", "540 ienes", "45 ienes", "4.500 ienes"], 0, "四百五十円.")]},
    {"id": "jr005", "level": L1, "topic": "viagem", "title": "Viagem a Quioto",
     "text": "来週、京都へ行きます。京都に友だちが住んでいます。新幹線で行きます。東京から二時間ぐらいです。\n\n"
             "京都で古いお寺を見ます。そして、おいしい料理を食べます。お土産も買いたいです。",
     "translation": "Semana que vem vou a Quioto. Um amigo mora em Quioto. Vou de trem-bala. De Tóquio leva umas duas horas.\n\n"
                    "Em Quioto vou ver templos antigos. E vou comer comida gostosa. Também quero comprar lembrancinhas.",
     "questions": [q("Para onde a pessoa vai?", ["Quioto", "Osaka", "Tóquio", "Hokkaido"], 0, "京都へ行きます."),
                   q("Como vai viajar?", ["De trem-bala", "De avião", "De ônibus", "De carro"], 0, "新幹線で行きます."),
                   q("Quanto tempo leva de Tóquio?", ["Umas duas horas", "Meia hora", "Cinco horas", "Um dia"], 0, "二時間ぐらい.")]},
    {"id": "jr006", "level": L1, "topic": "clima", "title": "O tempo hoje e amanhã",
     "text": "今日はいい天気です。暑くないです。公園で友だちとテニスをします。\n\n"
             "でも、明日は雨です。寒いです。明日は傘を持って行きます。",
     "translation": "Hoje o tempo está bom. Não está quente. Jogo tênis com um amigo no parque.\n\n"
                    "Mas amanhã vai chover. Vai fazer frio. Amanhã vou levar guarda-chuva.",
     "questions": [q("Como está o tempo hoje?", ["Bom, sem calor", "Chuvoso", "Muito frio", "Com neve"], 0, "いい天気です。暑くないです."),
                   q("O que a pessoa faz hoje?", ["Joga tênis no parque", "Fica em casa", "Vai ao cinema", "Compra um guarda-chuva"], 0, "公園で友だちとテニスをします."),
                   q("O que vai levar amanhã?", ["Guarda-chuva", "Bicicleta", "Raquete", "Óculos de sol"], 0, "傘を持って行きます.")]},
    {"id": "jr007", "level": L1, "topic": "música", "title": "Meu grupo favorito",
     "text": "私の好きなグループは「ソラ」です。メンバーは五人です。歌もダンスも上手です。\n\n"
             "先月、ソラのコンサートに行きました。チケットは高かったです。でも、とても楽しかったです。",
     "translation": "Meu grupo favorito é o “Sora” (fictício). Tem cinco membros. Cantam e dançam bem.\n\n"
                    "No mês passado fui ao show do Sora. O ingresso foi caro. Mas foi muito divertido.",
     "questions": [q("Quantos membros tem o grupo?", ["Cinco", "Quatro", "Sete", "Três"], 0, "メンバーは五人です."),
                   q("Quando a pessoa foi ao show?", ["No mês passado", "Ontem", "No ano passado", "Vai no mês que vem"], 0, "先月."),
                   q("Como foi o ingresso?", ["Caro", "Barato", "Grátis", "Esgotado"], 0, "チケットは高かったです.")]},
    {"id": "jr008", "level": L1, "topic": "comida", "title": "No restaurante",
     "text": "昨日、友だちとラーメン屋に行きました。私はしょうゆラーメンを食べました。友だちはカレーを食べました。カレーは少し辛かったです。\n\n"
             "店はきれいで、ラーメンはとてもおいしかったです。また行きたいです。",
     "translation": "Ontem fui a um restaurante de lámen com um amigo. Eu comi lámen de shoyu. Meu amigo comeu curry. O curry estava um pouco apimentado.\n\n"
                    "O restaurante era limpo e o lámen estava muito gostoso. Quero ir de novo.",
     "questions": [q("O que a pessoa comeu?", ["Lámen de shoyu", "Curry", "Sushi", "Arroz"], 0, "しょうゆラーメンを食べました."),
                   q("Como estava o curry?", ["Um pouco apimentado", "Doce", "Frio", "Sem gosto"], 0, "少し辛かったです."),
                   q("O que ela quer?", ["Ir de novo", "Cozinhar em casa", "Mudar de restaurante", "Comer curry"], 0, "また行きたいです.")]},
    {"id": "jr009", "level": L1, "topic": "compras", "title": "Um presente para a mãe",
     "text": "来週は母の誕生日です。昨日デパートへプレゼントを買いに行きました。赤いかばんがありましたが、とても高かったです。\n\n"
             "それで、花とケーキを買いました。母はとても喜びました。",
     "translation": "Semana que vem é o aniversário da minha mãe. Ontem fui à loja de departamentos comprar um presente. Havia uma bolsa vermelha, mas era muito cara.\n\n"
                    "Então comprei flores e um bolo. Minha mãe ficou muito feliz.",
     "questions": [q("De quem é o aniversário?", ["Da mãe", "Do pai", "Da irmã", "Da avó"], 0, "母の誕生日."),
                   q("Por que não comprou a bolsa?", ["Era muito cara", "Era feia", "Era pequena", "A loja fechou"], 0, "とても高かったです."),
                   q("O que comprou?", ["Flores e um bolo", "A bolsa", "Uma roupa", "Um livro"], 0, "花とケーキを買いました.")]},
    {"id": "jr010", "level": L1, "topic": "estudos", "title": "Por que estudo japonês",
     "text": "私はブラジル人です。去年から日本語を勉強しています。日本のアニメが好きですから、日本語を勉強したかったです。\n\n"
             "ひらがなはやさしいです。でも、漢字は難しいです。毎日漢字を五つ覚えます。来年、日本へ行きたいです。",
     "translation": "Sou brasileiro(a). Estudo japonês desde o ano passado. Como gosto de anime japonês, queria estudar japonês.\n\n"
                    "O hiragana é fácil. Mas o kanji é difícil. Decoro cinco kanji por dia. No ano que vem quero ir ao Japão.",
     "questions": [q("Desde quando a pessoa estuda japonês?", ["Desde o ano passado", "Desde criança", "Há uma semana", "Desde este mês"], 0, "去年から."),
                   q("O que é difícil?", ["O kanji", "O hiragana", "Os números", "A pronúncia"], 0, "漢字は難しいです."),
                   q("Quantos kanji decora por dia?", ["Cinco", "Dez", "Três", "Vinte"], 0, "漢字を五つ覚えます.")]},
    {"id": "jr011", "level": L2, "topic": "moradia", "title": "Mudança",
     "text": "先月、新しいアパートに引っ越しました。前のアパートは会社から遠かったので、毎日電車で一時間かかりました。今は会社まで歩いて十五分です。\n\n"
             "部屋は狭いですが、窓が大きくて明るいです。近くに公園とスーパーがあって、とても便利です。今度の土曜日に友だちを呼んでパーティーをします。",
     "translation": "No mês passado me mudei para um apartamento novo. O anterior era longe da empresa, então levava uma hora de trem todo dia. Agora são quinze minutos a pé até a empresa.\n\n"
                    "O quarto é apertado, mas a janela é grande e é claro. Perto há um parque e um supermercado; é muito prático. Neste sábado vou chamar amigos e fazer uma festa.",
     "questions": [q("Por que a pessoa se mudou?", ["O apartamento antigo era longe da empresa", "Era caro", "Queria um parque", "Mudou de emprego"], 0, "会社から遠かったので."),
                   q("Quanto tempo leva a pé agora?", ["Quinze minutos", "Uma hora", "Cinco minutos", "Meia hora"], 0, "歩いて十五分."),
                   q("O que vai fazer no sábado?", ["Uma festa com amigos", "Mudar de novo", "Trabalhar", "Viajar"], 0, "友だちを呼んでパーティーをします.")]},
    {"id": "jr012", "level": L2, "topic": "saúde", "title": "No médico",
     "text": "昨日から頭が痛くて、熱があります。今朝は会社を休んで、病院へ行きました。医者は「かぜですね」と言いました。\n\n"
             "薬を飲んで、ゆっくり休んでくださいと言われました。水もたくさん飲みます。明日はまた会社へ行きたいです。",
     "translation": "Desde ontem estou com dor de cabeça e febre. Hoje de manhã faltei ao trabalho e fui ao hospital. O médico disse: “É um resfriado”.\n\n"
                    "Disseram para eu tomar remédio e descansar bem. Também vou beber bastante água. Amanhã quero voltar ao trabalho.",
     "questions": [q("Quais são os sintomas?", ["Dor de cabeça e febre", "Dor de barriga", "Tosse", "Dor nas costas"], 0, "頭が痛くて、熱があります."),
                   q("O que o médico disse?", ["Que é resfriado", "Que precisa de cirurgia", "Que não é nada", "Que deve trabalhar"], 0, "かぜですね."),
                   q("Qual foi o conselho?", ["Tomar remédio e descansar", "Fazer exercício", "Ir trabalhar", "Comer muito"], 0, "薬を飲んで、ゆっくり休んで.")]},
    {"id": "jr013", "level": L2, "topic": "trabalho", "title": "Meu bico de fim de semana",
     "text": "私は毎週土曜日と日曜日にコンビニでアルバイトをしています。午後二時から夜十時まで働きます。レジをしたり、商品を並べたりします。\n\n"
             "仕事は少し大変ですが、店長が優しいので楽しいです。アルバイトのお金をためて、夏休みに韓国へ旅行したいです。",
     "translation": "Todo sábado e domingo trabalho meio período numa loja de conveniência. Trabalho das duas da tarde às dez da noite. Fico no caixa, arrumo produtos etc.\n\n"
                    "O trabalho é um pouco puxado, mas o gerente é gentil, então é agradável. Quero juntar o dinheiro e viajar para a Coreia nas férias de verão.",
     "questions": [q("Onde a pessoa trabalha?", ["Numa loja de conveniência", "Num café", "Num restaurante", "Numa escola"], 0, "コンビニでアルバイト."),
                   q("Qual é o horário?", ["Das 14h às 22h", "Das 9h às 18h", "Das 10h às 14h", "Das 22h às 6h"], 0, "午後二時から夜十時まで."),
                   q("Para onde quer viajar?", ["Coreia", "China", "Brasil", "Havaí"], 0, "韓国へ旅行したいです.")]},
    {"id": "jr014", "level": L2, "topic": "séries", "title": "Uma série que recomendo",
     "text": "最近、「春の約束」というドラマを見ています。東京の小さい花屋の話です。主人公は花屋の店長とコックです。\n\n"
             "最初、二人はよくけんかをしますが、だんだん仲良くなります。俳優の演技が自然で、音楽もきれいです。まだ見ていない人は、ぜひ見てください。",
     "translation": "Ultimamente estou vendo um drama chamado “Promessa de primavera” (fictício). É a história de uma pequena floricultura de Tóquio. Os protagonistas são a gerente da floricultura e um cozinheiro.\n\n"
                    "No começo os dois brigam muito, mas aos poucos ficam amigos. A atuação é natural e a música também é bonita. Quem ainda não viu, não deixe de ver.",
     "questions": [q("Onde se passa a história?", ["Numa floricultura de Tóquio", "Num hospital", "Numa escola de Osaka", "Num restaurante"], 0, "東京の小さい花屋の話."),
                   q("Quem são os protagonistas?", ["A gerente da floricultura e um cozinheiro", "Dois estudantes", "Um médico e uma cantora", "Duas irmãs"], 0, "花屋の店長とコック."),
                   q("Como era a relação no começo?", ["Brigavam muito", "Já namoravam", "Eram melhores amigos", "Não se falavam"], 0, "最初、二人はよくけんかをします.")]},
    {"id": "jr015", "level": L2, "topic": "viagem", "title": "Pedindo informação",
     "text": "観光客：すみません。浅草寺はどうやって行きますか。\n\n駅員：銀座線に乗って、浅草駅で降りてください。\n\n"
             "観光客：駅から遠いですか。\n\n駅員：いいえ、近いです。まっすぐ行って、右に曲がってください。歩いて五分ぐらいです。\n\n観光客：ありがとうございます。\n\n駅員：どういたしまして。",
     "translation": "Turista: Com licença. Como faço para ir ao templo Senso-ji?\n\nFuncionário: Pegue a linha Ginza e desça na estação Asakusa.\n\n"
                    "Turista: É longe da estação?\n\nFuncionário: Não, é perto. Siga reto e vire à direita. Uns cinco minutos a pé.\n\nTurista: Muito obrigado.\n\nFuncionário: De nada.",
     "questions": [q("Aonde o turista quer ir?", ["Templo Senso-ji", "Estação de Tóquio", "Aeroporto", "Hotel"], 0, "浅草寺はどうやって行きますか."),
                   q("Em que estação deve descer?", ["Asakusa", "Ginza", "Shinjuku", "Ueno"], 0, "浅草駅で降りて."),
                   q("Quanto tempo leva a pé?", ["Uns cinco minutos", "Meia hora", "Uma hora", "Dez minutos"], 0, "歩いて五分ぐらい.")]},
    {"id": "jr016", "level": L2, "topic": "hobby", "title": "Meu hobby é fotografar",
     "text": "私の趣味は写真を撮ることです。高校生のとき、祖父が古いカメラをくれました。それから、写真が好きになりました。\n\n"
             "週末はカメラを持って、町を歩きながら写真を撮ります。特に人の笑顔を撮るのが好きです。いつか自分の写真展をしたいです。",
     "translation": "Meu hobby é tirar fotos. No ensino médio, meu avô me deu uma câmera antiga. Desde então passei a gostar de fotografia.\n\n"
                    "No fim de semana levo a câmera e tiro fotos enquanto caminho pela cidade. Gosto especialmente de fotografar sorrisos. Um dia quero fazer minha própria exposição.",
     "questions": [q("Qual é o hobby da pessoa?", ["Fotografia", "Pintura", "Dança", "Cozinhar"], 0, "趣味は写真を撮ることです."),
                   q("Quem deu a câmera?", ["O avô", "O pai", "A mãe", "Um amigo"], 0, "祖父が古いカメラをくれました."),
                   q("Qual é o sonho dela?", ["Fazer uma exposição de fotos", "Comprar outra câmera", "Ser modelo", "Viajar"], 0, "自分の写真展をしたいです.")]},
    {"id": "jr017", "level": L2, "topic": "estações", "title": "As estações no Japão",
     "text": "日本には春、夏、秋、冬の四つの季節があります。春は暖かくて、桜がきれいです。夏は暑くて、六月は雨がよく降ります。\n\n"
             "秋は涼しくて、紅葉を見に山へ行く人が多いです。冬は寒くて、北海道では雪がたくさん降ります。私は涼しい秋がいちばん好きです。",
     "translation": "No Japão há quatro estações: primavera, verão, outono e inverno. A primavera é amena e as cerejeiras são lindas. O verão é quente e em junho chove muito.\n\n"
                    "O outono é fresco e muita gente vai às montanhas ver as folhas coloridas. O inverno é frio e em Hokkaido neva muito. Eu gosto mais do outono fresco.",
     "questions": [q("Quando chove muito?", ["Em junho", "Em abril", "Em outubro", "Em dezembro"], 0, "六月は雨がよく降ります."),
                   q("Por que muitos vão às montanhas no outono?", ["Para ver as folhas coloridas", "Porque é quente", "Para ver a neve", "Para ver as cerejeiras"], 0, "紅葉を見に山へ行く."),
                   q("Qual estação a pessoa prefere?", ["Outono", "Primavera", "Verão", "Inverno"], 0, "涼しい秋がいちばん好きです.")]},
    {"id": "jr018", "level": L2, "topic": "mensagens", "title": "Mudança de planos",
     "text": "ゆいさん、ごめんなさい。明日の夜七時に会う約束でしたが、急に会社の仕事ができました。七時には行けないと思います。\n\n"
             "八時半はどうですか。または、土曜日のお昼はどうですか。土曜日は時間があるので、あのおいしいすし屋に行きましょう。返事を待っています。",
     "translation": "Yui, desculpe. Tínhamos combinado de nos ver amanhã às sete da noite, mas de repente surgiu trabalho na empresa. Acho que não consigo ir às sete.\n\n"
                    "Que tal às oito e meia? Ou que tal almoço no sábado? No sábado tenho tempo; vamos naquele restaurante de sushi gostoso. Aguardo sua resposta.",
     "questions": [q("Por que a pessoa precisa mudar o encontro?", ["Surgiu trabalho na empresa", "Está doente", "Perdeu o trem", "Esqueceu"], 0, "急に会社の仕事ができました."),
                   q("Que horário ela sugere amanhã?", ["20h30", "19h", "12h", "21h30"], 0, "八時半はどうですか."),
                   q("Qual é a alternativa?", ["Almoço no sábado", "Café no domingo", "Jantar na sexta", "Cancelar"], 0, "土曜日のお昼.")]},
    {"id": "jr019", "level": L2, "topic": "consumo", "title": "Compras pela internet",
     "text": "最近、インターネットで買い物をする人が多いです。家で買えるので便利です。それに、たいてい次の日に届きます。値段も店より安いことが多いです。\n\n"
             "でも、問題もあります。服や靴は着てみることができないので、サイズが合わないことがあります。だから、私は服は店で買って、本はインターネットで買います。",
     "translation": "Ultimamente muita gente faz compras pela internet. É prático porque dá para comprar de casa. Além disso, geralmente chega no dia seguinte. O preço também costuma ser mais barato que na loja.\n\n"
                    "Mas há problemas também. Roupas e sapatos não dá para experimentar, então às vezes o tamanho não serve. Por isso compro roupas na loja e livros pela internet.",
     "questions": [q("Qual é uma vantagem?", ["Geralmente chega no dia seguinte", "Dá para experimentar roupas", "É sempre mais caro", "Precisa ir à loja"], 0, "たいてい次の日に届きます."),
                   q("Qual é o problema?", ["Não dá para experimentar roupas e sapatos", "Demora um mês", "Só aceita dinheiro", "Não há livros"], 0, "着てみることができない."),
                   q("O que a pessoa compra pela internet?", ["Livros", "Roupas", "Sapatos", "Nada"], 0, "本はインターネットで買います.")]},
    {"id": "jr020", "level": L2, "topic": "dança", "title": "No clube de dança",
     "text": "今学期、学校のダンス部に入りました。練習は週に二回、火曜日と木曜日の夜です。部ではK-POPのダンスを習って、学校のお祭りで踊ります。\n\n"
             "最初はダンスが下手で、心配でした。でも、先輩が優しく教えてくれたので、今はずいぶん上手になりました。来月、初めてステージで踊ります。少し緊張しますが、楽しみです。",
     "translation": "Neste semestre entrei no clube de dança da escola. Os ensaios são duas vezes por semana, terça e quinta à noite. No clube aprendemos danças de K-pop e dançamos no festival da escola.\n\n"
                    "No começo eu dançava mal e ficava preocupado. Mas os veteranos me ensinaram com gentileza, e agora melhorei bastante. No mês que vem vou dançar no palco pela primeira vez. Estou um pouco nervoso, mas ansioso.",
     "questions": [q("Com que frequência o clube ensaia?", ["Duas vezes por semana", "Todo dia", "Uma vez por mês", "Só no fim de semana"], 0, "週に二回."),
                   q("O que aprendem no clube?", ["Danças de K-pop", "Balé", "Canto", "Teatro"], 0, "K-POP のダンスを習って."),
                   q("O que vai acontecer no mês que vem?", ["A primeira apresentação no palco", "Uma viagem", "Uma prova", "O fim do clube"], 0, "初めてステージで踊ります.")]},
]

PROMPTS = [
    {"id": "jw01", "level": L1, "topic": "apresentação", "prompt": "自己紹介をしてください。", "prompt_pt": "Apresente-se: nome, cidade, o que faz e do que gosta.", "units": 60, "lines": 4},
    {"id": "jw02", "level": L1, "topic": "rotina", "prompt": "あなたの一日を書いてください。", "prompt_pt": "Descreva seu dia (horários + verbos -masu).", "units": 60, "lines": 4},
    {"id": "jw03", "level": L1, "topic": "família", "prompt": "家族を紹介してください。", "prompt_pt": "Apresente sua família (lembre: 母/父 para a sua, お母さん para a dos outros).", "units": 60, "lines": 4},
    {"id": "jw04", "level": L1, "topic": "comida", "prompt": "好きな食べ物は何ですか。", "prompt_pt": "Qual é sua comida favorita e por quê?", "units": 60, "lines": 4},
    {"id": "jw05", "level": L1, "topic": "passado", "prompt": "先週の週末、何をしましたか。", "prompt_pt": "O que você fez no fim de semana passado? (-mashita)", "units": 60, "lines": 4},
    {"id": "jw06", "level": L1, "topic": "música", "prompt": "好きな歌手やアニメを紹介してください。", "prompt_pt": "Apresente um cantor, grupo ou anime de que você gosta.", "units": 60, "lines": 4},
    {"id": "jw07", "level": L1, "topic": "cidade", "prompt": "あなたの町を紹介してください。", "prompt_pt": "Descreva sua cidade/bairro (あります/います).", "units": 60, "lines": 4},
    {"id": "jw08", "level": L1, "topic": "futuro", "prompt": "次の休みに何をしたいですか。", "prompt_pt": "O que você quer fazer nas próximas férias? (-tai desu)", "units": 60, "lines": 4},
    {"id": "jw09", "level": L2, "topic": "estudos", "prompt": "どうして日本語を勉強していますか。", "prompt_pt": "Por que você estuda japonês? O que é fácil e difícil?", "units": 120, "lines": 6},
    {"id": "jw10", "level": L2, "topic": "viagem", "prompt": "忘れられない旅行について書いてください。", "prompt_pt": "Conte uma viagem inesquecível.", "units": 120, "lines": 6},
    {"id": "jw11", "level": L2, "topic": "estações", "prompt": "好きな季節とその理由を書いてください。", "prompt_pt": "Sua estação favorita e por quê.", "units": 120, "lines": 6},
    {"id": "jw12", "level": L2, "topic": "saúde", "prompt": "健康のために何をしていますか。", "prompt_pt": "O que você faz pela sua saúde?", "units": 120, "lines": 6},
    {"id": "jw13", "level": L2, "topic": "consumo", "prompt": "インターネットの買い物のいい点と悪い点を書いてください。", "prompt_pt": "Vantagens e desvantagens de comprar online.", "units": 120, "lines": 6},
    {"id": "jw14", "level": L2, "topic": "mensagens", "prompt": "友だちに約束の時間を変えるメッセージを書いてください。", "prompt_pt": "Mensagem a um amigo mudando o horário de um encontro.", "units": 120, "lines": 6},
    {"id": "jw15", "level": L2, "topic": "hobby", "prompt": "あなたの趣味を紹介してください。", "prompt_pt": "Apresente seu hobby.", "units": 120, "lines": 6},
    {"id": "jw16", "level": L2, "topic": "futuro", "prompt": "十年後のあなたはどうなっていると思いますか。", "prompt_pt": "Como você se imagina daqui a dez anos?", "units": 120, "lines": 6},
]

ROLEPLAY = "1. いちばん言いたいことは何ですか。 2. 例を一つ教えてください。 3. どうしてそう思いますか。"
