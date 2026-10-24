"""Reading, Writing, Listening e Speaking do Chinese Routine (HSK 1–2).

Esquema comum de skills/ (docs/PADRAO-IDIOMAS.md). Perguntas em português.
Textos originais; grupos, séries e pessoas são fictícios.
Revisão por professor ou falante nativo recomendada antes da venda.
"""

L1, L2 = "HSK 1", "HSK 2"


def q(question, options, answer, why):
    return {"question": question, "options": options, "answer": answer, "why": why}


TEXTS = [
    {"id": "zr001", "level": L1, "topic": "apresentação", "title": "Muito prazer, eu sou o Wang Ming",
     "text": "你好！我叫王明。我是中国人，我家在北京。我是大学生，我在大学学习英语。\n\n"
             "我喜欢听音乐，也喜欢看电影。周末我常常和朋友一起去看电影。认识你很高兴！",
     "translation": "Olá! Meu nome é Wang Ming. Sou chinês e minha família mora em Pequim. Sou universitário e estudo inglês na universidade.\n\n"
                    "Gosto de ouvir música e também de ver filmes. No fim de semana costumo ir ao cinema com amigos. Prazer em conhecer você!",
     "questions": [q("Onde fica a casa do Wang Ming?", ["Pequim", "Xangai", "Brasil", "Japão"], 0, "我家在北京."),
                   q("O que ele estuda?", ["Inglês", "Chinês", "Música", "Medicina"], 0, "我在大学学习英语."),
                   q("O que ele faz no fim de semana?", ["Vai ao cinema com amigos", "Trabalha", "Viaja", "Estuda na biblioteca"], 0, "周末我常常和朋友一起去看电影.")]},
    {"id": "zr002", "level": L1, "topic": "rotina", "title": "Meu dia",
     "text": "我每天早上七点起床。我先喝一杯咖啡，然后吃早饭。八点我坐地铁去公司。\n\n"
             "我在公司工作八个小时。晚上六点我回家做饭。吃饭以后，我看一会儿电视，十一点睡觉。",
     "translation": "Todo dia acordo às sete da manhã. Primeiro tomo um café, depois tomo o café da manhã. Às oito pego o metrô para a empresa.\n\n"
                    "Trabalho oito horas na empresa. Às seis da tarde volto para casa e cozinho. Depois de comer, vejo um pouco de TV e durmo às onze.",
     "questions": [q("A que horas a pessoa acorda?", ["Às 7h", "Às 8h", "Às 6h", "Às 11h"], 0, "早上七点起床."),
                   q("Como ela vai para a empresa?", ["De metrô", "De ônibus", "A pé", "De táxi"], 0, "坐地铁去公司."),
                   q("A que horas ela dorme?", ["Às 23h", "Às 22h", "Às 18h", "À meia-noite"], 0, "十一点睡觉.")]},
    {"id": "zr003", "level": L1, "topic": "família", "title": "Minha família",
     "text": "我家有五个人：爸爸、妈妈、哥哥、妹妹和我。爸爸是医生，他在医院工作。妈妈是老师。\n\n"
             "哥哥在上海工作，他很忙。妹妹是学生，她今年十岁。我们都喜欢吃妈妈做的饺子。",
     "translation": "Minha família tem cinco pessoas: pai, mãe, irmão mais velho, irmã mais nova e eu. Meu pai é médico e trabalha no hospital. Minha mãe é professora.\n\n"
                    "Meu irmão trabalha em Xangai e é muito ocupado. Minha irmã é estudante e tem dez anos. Todos nós gostamos dos jiaozi que a mamãe faz.",
     "questions": [q("Quantas pessoas há na família?", ["Cinco", "Quatro", "Três", "Seis"], 0, "我家有五个人."),
                   q("Qual é a profissão do pai?", ["Médico", "Professor", "Estudante", "Cozinheiro"], 0, "爸爸是医生."),
                   q("Do que todos gostam?", ["Dos jiaozi da mãe", "De viajar a Xangai", "De ver TV", "De pato laqueado"], 0, "我们都喜欢吃妈妈做的饺子.")]},
    {"id": "zr004", "level": L1, "topic": "café", "title": "Na cafeteria",
     "text": "服务员：欢迎光临！您要喝什么？\n\n顾客：我要一杯冰美式。\n\n服务员：大杯还是中杯？\n\n顾客：大杯。多少钱？\n\n服务员：二十八块。\n\n顾客：给你。谢谢！",
     "translation": "Atendente: Seja bem-vindo! O que vai beber?\n\nCliente: Quero um americano gelado.\n\nAtendente: Grande ou médio?\n\nCliente: Grande. Quanto é?\n\nAtendente: Vinte e oito yuan.\n\nCliente: Aqui está. Obrigado!",
     "questions": [q("O que o cliente pede?", ["Americano gelado", "Chá verde", "Café com leite", "Suco"], 0, "我要一杯冰美式."),
                   q("Que tamanho ele escolhe?", ["Grande", "Médio", "Pequeno", "Não diz"], 0, "大杯."),
                   q("Quanto custa?", ["28 yuan", "8 yuan", "20 yuan", "82 yuan"], 0, "二十八块.")]},
    {"id": "zr005", "level": L1, "topic": "viagem", "title": "Fim de semana em Xangai",
     "text": "这个周末我要去上海。我的朋友住在上海。星期六上午我坐高铁去，只要四个半小时。\n\n"
             "在上海，我们要去外滩看夜景，还要吃小笼包。星期天下午我去商场给妈妈买礼物。",
     "translation": "Neste fim de semana vou para Xangai. Meu amigo mora em Xangai. Sábado de manhã vou de trem-bala; leva só quatro horas e meia.\n\n"
                    "Em Xangai vamos ao Bund ver a vista noturna e também comer xiaolongbao. Domingo à tarde vou ao shopping comprar um presente para minha mãe.",
     "questions": [q("Para onde a pessoa vai?", ["Xangai", "Pequim", "Japão", "Brasil"], 0, "我要去上海."),
                   q("Como ela vai?", ["De trem-bala", "De avião", "De ônibus", "De carro"], 0, "坐高铁去."),
                   q("O que vai fazer no domingo?", ["Comprar um presente para a mãe", "Comer xiaolongbao", "Voltar cedo", "Ver o Bund"], 0, "给妈妈买礼物.")]},
    {"id": "zr006", "level": L1, "topic": "clima", "title": "O tempo hoje e amanhã",
     "text": "今天天气很好，是晴天，不冷也不热。我和朋友在公园跑步。\n\n"
             "可是明天要下雨，还会有点儿冷。明天出门的时候，一定要带雨伞。",
     "translation": "Hoje o tempo está ótimo, faz sol, nem frio nem calor. Corro no parque com um amigo.\n\n"
                    "Mas amanhã vai chover e vai fazer um pouco de frio. Amanhã, ao sair, preciso levar guarda-chuva.",
     "questions": [q("Como está o tempo hoje?", ["Ensolarado, nem frio nem calor", "Chuvoso", "Muito frio", "Com neve"], 0, "是晴天，不冷也不热."),
                   q("O que a pessoa faz hoje?", ["Corre no parque", "Fica em casa", "Vai ao cinema", "Compra um guarda-chuva"], 0, "在公园跑步."),
                   q("O que precisa levar amanhã?", ["Guarda-chuva", "Bicicleta", "Óculos de sol", "Câmera"], 0, "一定要带雨伞.")]},
    {"id": "zr007", "level": L1, "topic": "música", "title": "Minha banda favorita",
     "text": "我最喜欢的乐队叫“星光”。“星光”有五个成员，他们唱歌唱得很好，跳舞也跳得很好。\n\n"
             "上个月我去看了他们的演唱会。门票很贵，可是演唱会特别好看。我一边挥荧光棒，一边跟着唱。",
     "translation": "Minha banda favorita se chama “Xingguang” (fictícia). Tem cinco membros, que cantam muito bem e também dançam muito bem.\n\n"
                    "No mês passado fui ao show deles. O ingresso era caro, mas o show foi incrível. Eu balançava o lightstick e cantava junto.",
     "questions": [q("Quantos membros tem a banda?", ["Cinco", "Quatro", "Sete", "Três"], 0, "有五个成员."),
                   q("Quando a pessoa foi ao show?", ["No mês passado", "Ontem", "No ano passado", "Vai no mês que vem"], 0, "上个月."),
                   q("Como era o ingresso?", ["Caro", "Barato", "Grátis", "Esgotado"], 0, "门票很贵.")]},
    {"id": "zr008", "level": L1, "topic": "comida", "title": "No restaurante",
     "text": "昨天我和朋友去了一家饭馆。我点了一碗牛肉面，朋友点了一个火锅。火锅有点儿辣。\n\n"
             "饭馆很干净，菜也很好吃，而且不贵。我们下次还想来这儿吃饭。",
     "translation": "Ontem fui a um restaurante com um amigo. Pedi uma tigela de macarrão com carne; meu amigo pediu um hotpot. O hotpot estava um pouco apimentado.\n\n"
                    "O restaurante era limpo, a comida gostosa e, além disso, não era caro. Da próxima vez queremos voltar a comer aqui.",
     "questions": [q("O que a pessoa pediu?", ["Macarrão com carne", "Hotpot", "Jiaozi", "Arroz"], 0, "我点了一碗牛肉面."),
                   q("Como estava o hotpot?", ["Um pouco apimentado", "Doce", "Frio", "Sem gosto"], 0, "火锅有点儿辣."),
                   q("Por que gostaram do restaurante?", ["Limpo, gostoso e barato", "Era perto de casa", "Tinha música ao vivo", "Era novo"], 0, "很干净，菜也很好吃，而且不贵.")]},
    {"id": "zr009", "level": L1, "topic": "compras", "title": "Um presente para o irmão",
     "text": "下个星期是弟弟的生日。我想给他买一件衣服。昨天我去了商店，看到一件红色的衣服，很漂亮，可是太贵了。\n\n"
             "后来我在网上买了一件黑色的，又便宜又好看。弟弟很喜欢。",
     "translation": "Semana que vem é o aniversário do meu irmão mais novo. Quero comprar uma roupa para ele. Ontem fui à loja e vi uma roupa vermelha, muito bonita, mas cara demais.\n\n"
                    "Depois comprei uma preta pela internet, barata e bonita. Meu irmão gostou muito.",
     "questions": [q("Para quem é o presente?", ["Irmão mais novo", "Mãe", "Amigo", "Professor"], 0, "弟弟的生日."),
                   q("Por que não comprou a roupa vermelha?", ["Era cara demais", "Era feia", "Não tinha tamanho", "A loja estava fechada"], 0, "太贵了."),
                   q("Onde comprou a roupa preta?", ["Pela internet", "Na mesma loja", "No mercado", "No shopping"], 0, "在网上买了一件黑色的.")]},
    {"id": "zr010", "level": L1, "topic": "estudos", "title": "Por que estudo chinês",
     "text": "我是巴西人。我从去年开始学习汉语。我喜欢看中国电视剧，所以想学汉语。\n\n"
             "汉字很难，可是声调更难。我每天学十个新词。明年我想去中国旅游。",
     "translation": "Sou brasileiro(a). Comecei a estudar chinês no ano passado. Gosto de séries chinesas, por isso quis aprender chinês.\n\n"
                    "Os caracteres são difíceis, mas os tons são ainda mais difíceis. Aprendo dez palavras novas por dia. No ano que vem quero viajar para a China.",
     "questions": [q("Desde quando a pessoa estuda chinês?", ["Desde o ano passado", "Desde criança", "Há uma semana", "Desde este mês"], 0, "从去年开始."),
                   q("O que é mais difícil para ela?", ["Os tons", "Os caracteres", "Os números", "A gramática"], 0, "声调更难."),
                   q("Quantas palavras novas aprende por dia?", ["Dez", "Cinco", "Vinte", "Cem"], 0, "每天学十个新词.")]},
    {"id": "zr011", "level": L2, "topic": "moradia", "title": "Casa nova",
     "text": "上个星期我搬家了。以前的房子离公司很远，我每天要坐一个多小时的地铁。现在的房子离公司很近，走路十五分钟就到了。\n\n"
             "新房子不大，但是窗户很大，房间里很亮。附近有公园和超市，生活很方便。这个周末我想请朋友来我家吃饭。",
     "translation": "Semana passada me mudei. A casa de antes era longe da empresa; eu pegava metrô por mais de uma hora todo dia. A casa de agora é perto: a pé, chego em quinze minutos.\n\n"
                    "A casa nova não é grande, mas as janelas são grandes e os cômodos são claros. Perto há um parque e um supermercado; a vida é prática. Neste fim de semana quero convidar amigos para comer em casa.",
     "questions": [q("Por que a pessoa se mudou?", ["A casa antiga era longe da empresa", "A casa antiga era pequena", "Queria morar perto do parque", "Mudou de emprego"], 0, "以前的房子离公司很远."),
                   q("Quanto tempo leva a pé até a empresa agora?", ["Quinze minutos", "Uma hora", "Cinco minutos", "Meia hora"], 0, "走路十五分钟就到了."),
                   q("O que ela quer fazer no fim de semana?", ["Convidar amigos para comer em casa", "Mudar de novo", "Comprar móveis", "Viajar"], 0, "请朋友来我家吃饭.")]},
    {"id": "zr012", "level": L2, "topic": "saúde", "title": "No médico",
     "text": "我昨天开始头疼，还发烧了。今天早上我没去上班，去了医院。医生说我感冒了。\n\n"
             "医生让我吃药，多喝水，好好休息。他说休息两三天就会好。今天我在家休息，明天再去上班。",
     "translation": "Ontem comecei a ter dor de cabeça e também febre. Hoje de manhã não fui trabalhar e fui ao hospital. O médico disse que estou gripado.\n\n"
                    "O médico mandou tomar remédio, beber bastante água e descansar bem. Disse que em dois ou três dias de descanso vou melhorar. Hoje descanso em casa; amanhã volto ao trabalho.",
     "questions": [q("Quais eram os sintomas?", ["Dor de cabeça e febre", "Dor de barriga", "Tosse", "Dor nas costas"], 0, "头疼，还发烧了."),
                   q("O que o médico disse?", ["Que é gripe", "Que precisa de cirurgia", "Que não é nada", "Que deve trabalhar"], 0, "医生说我感冒了."),
                   q("Qual foi o conselho?", ["Remédio, muita água e descanso", "Fazer exercício", "Ir trabalhar", "Comer apimentado"], 0, "吃药，多喝水，好好休息.")]},
    {"id": "zr013", "level": L2, "topic": "trabalho", "title": "Meu trabalho de fim de semana",
     "text": "我每个周末在一家便利店打工。星期六和星期天，我从下午两点工作到晚上十点。我的工作是收银和整理东西。\n\n"
             "工作有点儿累，但是老板对我很好。我想把打工的钱攒起来，暑假去日本旅游。",
     "translation": "Todo fim de semana trabalho numa loja de conveniência. Sábado e domingo trabalho das duas da tarde às dez da noite. Meu trabalho é o caixa e organizar os produtos.\n\n"
                    "O trabalho é um pouco cansativo, mas o dono me trata bem. Quero juntar o dinheiro do trabalho e viajar para o Japão nas férias de verão.",
     "questions": [q("Onde a pessoa trabalha?", ["Numa loja de conveniência", "Num café", "Num restaurante", "Numa escola"], 0, "在一家便利店打工."),
                   q("Qual é o horário?", ["Das 14h às 22h", "Das 9h às 18h", "Das 10h às 14h", "Das 22h às 2h"], 0, "从下午两点工作到晚上十点."),
                   q("Para que ela junta dinheiro?", ["Viajar ao Japão nas férias", "Comprar um celular", "Pagar a faculdade", "Mudar de casa"], 0, "暑假去日本旅游.")]},
    {"id": "zr014", "level": L2, "topic": "séries", "title": "Uma série que recomendo",
     "text": "最近我在看一部电视剧，叫《春天的约定》。故事发生在北京的一家小花店。主角是花店的主人和一个厨师。\n\n"
             "一开始他们常常吵架，后来慢慢互相理解了。演员演得很自然，音乐也很好听。如果你还没看过，一定要看看！",
     "translation": "Ultimamente estou vendo uma série chamada “Promessa de primavera” (fictícia). A história se passa numa pequena floricultura de Pequim. Os protagonistas são a dona da floricultura e um cozinheiro.\n\n"
                    "No começo eles brigavam muito; depois, aos poucos, passaram a se entender. A atuação é natural e a música é bonita. Se ainda não viu, não deixe de ver!",
     "questions": [q("Onde se passa a história?", ["Numa floricultura de Pequim", "Num hospital", "Numa escola de Xangai", "Num restaurante"], 0, "北京的一家小花店."),
                   q("Quem são os protagonistas?", ["A dona da floricultura e um cozinheiro", "Dois estudantes", "Um médico e uma cantora", "Duas irmãs"], 0, "花店的主人和一个厨师."),
                   q("Como era a relação no começo?", ["Brigavam muito", "Já namoravam", "Eram melhores amigos", "Nunca se falavam"], 0, "一开始他们常常吵架.")]},
    {"id": "zr015", "level": L2, "topic": "viagem", "title": "Pedindo informação",
     "text": "游客：请问，去故宫怎么走？\n\n路人：您可以坐地铁一号线，在天安门东站下车。\n\n游客：地铁站离这儿远吗？\n\n"
             "路人：不远。您一直往前走，然后右拐，就到了。走路五分钟左右。\n\n游客：太谢谢您了！\n\n路人：不客气，祝您玩得愉快！",
     "translation": "Turista: Com licença, como chego à Cidade Proibida?\n\nPedestre: Pode pegar a linha 1 do metrô e descer na estação Tiananmen Leste.\n\nTurista: A estação é longe daqui?\n\n"
                    "Pedestre: Não. Siga sempre em frente e depois vire à direita: é ali. Uns cinco minutos a pé.\n\nTurista: Muito obrigado!\n\nPedestre: De nada, divirta-se!",
     "questions": [q("Para onde o turista quer ir?", ["Cidade Proibida", "Grande Muralha", "Aeroporto", "Estação de trem"], 0, "去故宫怎么走？"),
                   q("Qual linha de metrô deve pegar?", ["Linha 1", "Linha 2", "Linha 3", "Linha 10"], 0, "地铁一号线."),
                   q("Quanto tempo leva até a estação?", ["Uns cinco minutos a pé", "Meia hora", "Uma hora de ônibus", "Dez minutos de táxi"], 0, "走路五分钟左右.")]},
    {"id": "zr016", "level": L2, "topic": "hobby", "title": "Meu hobby é fotografar",
     "text": "我的爱好是拍照。上高中的时候，爸爸送给我一个旧相机。从那以后，我就喜欢上了拍照。\n\n"
             "周末我常常带着相机在城市里一边走一边拍。我特别喜欢拍人们的笑容。我希望以后能办一个自己的摄影展。",
     "translation": "Meu hobby é fotografar. No ensino médio, meu pai me deu uma câmera antiga. Desde então passei a gostar de fotografar.\n\n"
                    "No fim de semana costumo levar a câmera e fotografar enquanto caminho pela cidade. Gosto especialmente de fotografar sorrisos. Espero um dia fazer minha própria exposição de fotos.",
     "questions": [q("Qual é o hobby da pessoa?", ["Fotografia", "Pintura", "Dança", "Cozinhar"], 0, "我的爱好是拍照."),
                   q("Quem deu a câmera?", ["O pai", "A mãe", "Um amigo", "O professor"], 0, "爸爸送给我一个旧相机."),
                   q("Qual é o sonho dela?", ["Fazer uma exposição de fotos", "Comprar uma câmera nova", "Ser modelo", "Viajar o mundo"], 0, "办一个自己的摄影展.")]},
    {"id": "zr017", "level": L2, "topic": "estações", "title": "As estações no norte da China",
     "text": "中国北方有四个季节：春天、夏天、秋天和冬天。春天很暖和，花都开了。夏天很热，七月雨很多。\n\n"
             "秋天很凉快，天很蓝，很多人去爬山看红叶。冬天很冷，常常下雪。我最喜欢凉快的秋天。",
     "translation": "No norte da China há quatro estações: primavera, verão, outono e inverno. A primavera é amena e as flores desabrocham. O verão é quente e em julho chove muito.\n\n"
                    "O outono é fresco, o céu é bem azul e muita gente sobe as montanhas para ver as folhas vermelhas. O inverno é frio e neva com frequência. Eu gosto mais do outono fresco.",
     "questions": [q("Quando chove muito?", ["Em julho", "Em abril", "Em outubro", "Em dezembro"], 0, "七月雨很多."),
                   q("Por que muita gente sobe as montanhas no outono?", ["Para ver as folhas vermelhas", "Porque é quente", "Para ver a neve", "Para ver as flores"], 0, "爬山看红叶."),
                   q("Qual estação a pessoa prefere?", ["Outono", "Primavera", "Verão", "Inverno"], 0, "我最喜欢凉快的秋天.")]},
    {"id": "zr018", "level": L2, "topic": "mensagens", "title": "Mudança de planos",
     "text": "小美，对不起！我们约好明天晚上七点见面，可是公司突然有事，我七点可能到不了。\n\n"
             "八点半可以吗？或者星期六中午一起吃饭怎么样？星期六我有时间，我们可以去吃那家好吃的火锅。等你回复！",
     "translation": "Xiaomei, desculpe! Combinamos de nos ver amanhã às sete da noite, mas de repente surgiu algo na empresa e acho que não consigo chegar às sete.\n\n"
                    "Pode ser às oito e meia? Ou que tal almoçarmos juntos no sábado ao meio-dia? No sábado tenho tempo; podemos ir naquele hotpot gostoso. Espero sua resposta!",
     "questions": [q("Por que a pessoa precisa mudar o encontro?", ["Surgiu algo na empresa", "Está doente", "Perdeu o metrô", "Esqueceu"], 0, "公司突然有事."),
                   q("Que horário ela sugere para amanhã?", ["20h30", "19h", "12h", "21h30"], 0, "八点半可以吗？"),
                   q("Qual é a outra opção?", ["Almoço no sábado", "Café no domingo", "Jantar na sexta", "Cancelar"], 0, "星期六中午一起吃饭.")]},
    {"id": "zr019", "level": L2, "topic": "consumo", "title": "Compras pela internet",
     "text": "现在很多人喜欢在网上买东西。在网上买东西很方便，在家就可以买，快递第二天就送到了。价格也常常比商店便宜。\n\n"
             "但是网上购物也有缺点。衣服和鞋子不能先试，有时候大小不合适。所以我在商店买衣服，在网上买书和日用品。",
     "translation": "Hoje muita gente gosta de comprar pela internet. É prático: dá para comprar de casa e a entrega chega no dia seguinte. O preço também costuma ser mais barato que na loja.\n\n"
                    "Mas comprar online também tem desvantagens. Roupas e sapatos não dá para provar antes, e às vezes o tamanho não serve. Por isso compro roupas na loja e livros e itens do dia a dia pela internet.",
     "questions": [q("Qual é uma vantagem citada?", ["A entrega chega no dia seguinte", "Dá para provar roupas", "É sempre mais caro", "Precisa ir à loja"], 0, "快递第二天就送到了."),
                   q("Qual é a desvantagem?", ["Não dá para provar roupas e sapatos", "Demora um mês", "Só aceita dinheiro", "Não há livros"], 0, "衣服和鞋子不能先试."),
                   q("O que a pessoa compra pela internet?", ["Livros e itens do dia a dia", "Roupas", "Sapatos", "Nada"], 0, "在网上买书和日用品.")]},
    {"id": "zr020", "level": L2, "topic": "dança", "title": "No clube de dança",
     "text": "这个学期我参加了学校的舞蹈社团。我们每个星期练习两次，星期二和星期四晚上。我们学习K-pop的舞蹈动作，在学校的节日上表演。\n\n"
             "一开始我跳得不好，很担心。但是学长学姐很耐心地教我，现在我进步了很多。下个月学校的节日，我第一次上台表演。我有点儿紧张，也很期待。",
     "translation": "Neste semestre entrei no clube de dança da escola. Ensaiamos duas vezes por semana, terça e quinta à noite. Aprendemos coreografias de K-pop e nos apresentamos nas festas da escola.\n\n"
                    "No começo eu dançava mal e ficava preocupado. Mas os veteranos me ensinaram com paciência e agora melhorei muito. No mês que vem, na festa da escola, vou subir ao palco pela primeira vez. Estou um pouco nervoso, mas animado.",
     "questions": [q("Com que frequência o clube ensaia?", ["Duas vezes por semana", "Todo dia", "Uma vez por mês", "Só no fim de semana"], 0, "每个星期练习两次."),
                   q("O que aprendem no clube?", ["Coreografias de K-pop", "Balé", "Canto", "Teatro"], 0, "学习K-pop的舞蹈动作."),
                   q("O que vai acontecer no mês que vem?", ["A primeira apresentação no palco", "Uma viagem", "Uma prova", "O fim do clube"], 0, "我第一次上台表演.")]},
]

PROMPTS = [
    {"id": "zw01", "level": L1, "topic": "apresentação", "prompt": "介绍一下你自己。", "prompt_pt": "Apresente-se: nome, cidade, o que estuda ou faz e do que gosta.", "units": 50, "lines": 4},
    {"id": "zw02", "level": L1, "topic": "rotina", "prompt": "说说你的一天。", "prompt_pt": "Conte seu dia: a que horas acorda, come, trabalha ou estuda e dorme.", "units": 50, "lines": 4},
    {"id": "zw03", "level": L1, "topic": "família", "prompt": "介绍一下你的家人。", "prompt_pt": "Apresente sua família: quantas pessoas, profissões e gostos.", "units": 50, "lines": 4},
    {"id": "zw04", "level": L1, "topic": "comida", "prompt": "你喜欢吃什么？", "prompt_pt": "O que você gosta de comer e beber? Quando e onde?", "units": 50, "lines": 4},
    {"id": "zw05", "level": L1, "topic": "passado", "prompt": "上个周末你做了什么？", "prompt_pt": "O que você fez no último fim de semana? (use 了)", "units": 50, "lines": 4},
    {"id": "zw06", "level": L1, "topic": "música", "prompt": "你喜欢哪个歌手或者电视剧？", "prompt_pt": "Que cantor, banda ou série você gosta e por quê?", "units": 50, "lines": 4},
    {"id": "zw07", "level": L1, "topic": "cidade", "prompt": "介绍一下你住的地方。", "prompt_pt": "Descreva onde você mora: o que tem perto e aonde costuma ir.", "units": 50, "lines": 4},
    {"id": "zw08", "level": L1, "topic": "futuro", "prompt": "下次放假你想做什么？", "prompt_pt": "O que você quer fazer nas próximas férias? (use 想 / 要)", "units": 50, "lines": 4},
    {"id": "zw09", "level": L2, "topic": "estudos", "prompt": "你为什么学习汉语？", "prompt_pt": "Por que você estuda chinês? O que é fácil e o que é difícil?", "units": 100, "lines": 6},
    {"id": "zw10", "level": L2, "topic": "viagem", "prompt": "说说一次难忘的旅行。", "prompt_pt": "Conte uma viagem inesquecível: onde, com quem e o que aconteceu.", "units": 100, "lines": 6},
    {"id": "zw11", "level": L2, "topic": "estações", "prompt": "你最喜欢哪个季节？为什么？", "prompt_pt": "Qual estação você prefere e por quê? Compare com outra (use 比).", "units": 100, "lines": 6},
    {"id": "zw12", "level": L2, "topic": "saúde", "prompt": "为了身体健康，你做什么？", "prompt_pt": "O que você faz pela sua saúde? Dê exemplos.", "units": 100, "lines": 6},
    {"id": "zw13", "level": L2, "topic": "consumo", "prompt": "网上购物有什么优点和缺点？", "prompt_pt": "Vantagens e desvantagens de comprar online (use 但是, 所以).", "units": 100, "lines": 6},
    {"id": "zw14", "level": L2, "topic": "mensagens", "prompt": "给朋友写一个改时间的消息。", "prompt_pt": "Escreva a um amigo mudando o horário de um encontro: desculpe-se, explique e proponha outro.", "units": 100, "lines": 6},
    {"id": "zw15", "level": L2, "topic": "hobby", "prompt": "介绍一下你的爱好。", "prompt_pt": "Apresente seu hobby: como começou, quando pratica, o que sente.", "units": 100, "lines": 6},
    {"id": "zw16", "level": L2, "topic": "futuro", "prompt": "十年以后的你是什么样子？", "prompt_pt": "Como você se imagina daqui a dez anos?", "units": 100, "lines": 6},
]

ROLEPLAY = "1. 你最想说的是什么？ 2. 请举一个例子。 3. 你为什么这么想？"
