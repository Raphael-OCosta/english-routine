"""Conteúdo de Reading, Writing, Listening e Speaking do Korean Routine.

Segue o esquema comum de skills/ (ver docs/PADRAO-IDIOMAS.md):
- TEXTS: leitura e listening. Perguntas de compreensão em português (nível TOPIK 1–2).
- PROMPTS: propostas de escrita e de fala.
Textos originais escritos para o treino; grupos, dramas e pessoas são fictícios.
Revisão por professor ou falante nativo recomendada antes da venda.
"""

L1, L2 = "TOPIK 1", "TOPIK 2"


def q(question, options, answer, why):
    return {"question": question, "options": options, "answer": answer, "why": why}


TEXTS = [
    {
        "id": "kr001", "level": L1, "topic": "apresentação", "title": "Muito prazer, eu sou a Minji",
        "text": "안녕하세요. 제 이름은 김민지예요. 저는 스물두 살이에요. 저는 서울에 살아요. 저는 대학생이에요. 대학교에서 영어를 공부해요.\n\n"
                "저는 케이팝을 아주 좋아해요. 주말에 친구하고 같이 노래방에 가요. 노래방에서 노래를 불러요. 만나서 반갑습니다!",
        "translation": "Olá. Meu nome é Kim Minji. Tenho 22 anos. Moro em Seul. Sou universitária. Estudo inglês na universidade.\n\n"
                       "Gosto muito de K-pop. No fim de semana vou ao karaokê com um amigo. No karaokê, canto. Prazer em conhecer!",
        "questions": [
            q("Onde a Minji mora?", ["Seul", "Busan", "Jeju", "Incheon"], 0, "서울에 살아요 = mora em Seul."),
            q("O que ela estuda na universidade?", ["Inglês", "Coreano", "Música", "Matemática"], 0, "영어를 공부해요 = estuda inglês."),
            q("O que ela faz no fim de semana?", ["Vai ao karaokê com um amigo", "Trabalha", "Viaja para Busan", "Estuda na biblioteca"], 0,
              "주말에 친구하고 같이 노래방에 가요."),
        ],
    },
    {
        "id": "kr002", "level": L1, "topic": "rotina", "title": "Meu dia",
        "text": "저는 매일 아침 일곱 시에 일어나요. 일어나서 샤워를 해요. 그리고 아침을 먹어요. 저는 보통 빵하고 우유를 먹어요.\n\n"
                "여덟 시에 지하철을 타고 회사에 가요. 회사에서 아홉 시부터 여섯 시까지 일해요. 저녁에는 집에서 드라마를 봐요. 열한 시에 자요.",
        "translation": "Todo dia acordo às sete da manhã. Depois de acordar, tomo banho. Depois tomo café da manhã. Normalmente como pão e leite.\n\n"
                       "Às oito pego o metrô e vou para a empresa. Trabalho das nove às seis. À noite assisto dorama em casa. Durmo às onze.",
        "questions": [
            q("A que horas a pessoa acorda?", ["Às 7h", "Às 8h", "Às 9h", "Às 6h"], 0, "일곱 시에 일어나요 = acorda às sete."),
            q("Como ela vai para o trabalho?", ["De metrô", "De ônibus", "A pé", "De táxi"], 0, "지하철을 타고 = pega o metrô."),
            q("O que ela faz à noite?", ["Assiste dorama em casa", "Vai à academia", "Estuda coreano", "Encontra amigos"], 0,
              "저녁에는 집에서 드라마를 봐요."),
        ],
    },
    {
        "id": "kr003", "level": L1, "topic": "família", "title": "Minha família",
        "text": "우리 가족은 네 명이에요. 아버지, 어머니, 언니, 그리고 저예요. 아버지는 의사예요. 병원에서 일해요. "
                "어머니는 선생님이에요. 고등학교에서 한국어를 가르쳐요.\n\n"
                "언니는 회사원이에요. 언니는 요리를 잘해요. 주말에 우리 가족은 같이 공원에 가요. 공원에서 산책을 해요.",
        "translation": "Minha família tem quatro pessoas: pai, mãe, irmã mais velha e eu. Meu pai é médico. Trabalha no hospital. "
                       "Minha mãe é professora. Ensina coreano no ensino médio.\n\n"
                       "Minha irmã é funcionária de empresa. Ela cozinha bem. No fim de semana minha família vai junta ao parque. No parque, caminhamos.",
        "questions": [
            q("Quantas pessoas há na família?", ["Quatro", "Três", "Cinco", "Duas"], 0, "네 명 = quatro pessoas."),
            q("Qual é a profissão da mãe?", ["Professora", "Médica", "Cozinheira", "Funcionária de empresa"], 0, "어머니는 선생님이에요."),
            q("O que a família faz no fim de semana?", ["Passeia no parque", "Vai ao cinema", "Cozinha em casa", "Visita o hospital"], 0,
              "공원에서 산책을 해요 = caminha no parque."),
        ],
    },
    {
        "id": "kr004", "level": L1, "topic": "café", "title": "No café",
        "text": "점원: 어서 오세요. 뭐 드릴까요?\n\n손님: 아이스 아메리카노 한 잔 주세요.\n\n점원: 사이즈는요?\n\n"
                "손님: 큰 거 주세요. 얼마예요?\n\n점원: 오천 원이에요.\n\n손님: 여기 있어요. 감사합니다.",
        "translation": "Atendente: Seja bem-vindo. O que deseja?\n\nCliente: Um americano gelado, por favor.\n\nAtendente: E o tamanho?\n\n"
                       "Cliente: O grande, por favor. Quanto é?\n\nAtendente: São cinco mil wons.\n\nCliente: Aqui está. Obrigado.",
        "questions": [
            q("O que o cliente pede?", ["Americano gelado", "Café com leite quente", "Chá verde", "Suco de laranja"], 0, "아이스 아메리카노 한 잔."),
            q("Qual tamanho ele escolhe?", ["Grande", "Pequeno", "Médio", "Não diz"], 0, "큰 거 주세요 = me dá o grande."),
            q("Quanto custa?", ["5.000 wons", "500 wons", "50.000 wons", "1.000 wons"], 0, "오천 원 = cinco mil wons."),
        ],
    },
    {
        "id": "kr005", "level": L1, "topic": "viagem", "title": "Planos para o fim de semana",
        "text": "이번 주말에 저는 부산에 갈 거예요. 부산에 친구가 살아요. 토요일 아침에 기차를 탈 거예요.\n\n"
                "부산에서 바다를 볼 거예요. 그리고 친구하고 같이 회를 먹을 거예요. 일요일에는 시장에서 선물을 살 거예요. 정말 기대돼요!",
        "translation": "Neste fim de semana vou para Busan. Um amigo mora em Busan. Sábado de manhã vou pegar o trem.\n\n"
                       "Em Busan vou ver o mar. E vou comer peixe cru com meu amigo. No domingo vou comprar presentes no mercado. Estou ansioso!",
        "questions": [
            q("Para onde a pessoa vai?", ["Busan", "Seul", "Jeju", "Japão"], 0, "부산에 갈 거예요."),
            q("Como ela vai viajar?", ["De trem", "De avião", "De ônibus", "De carro"], 0, "기차를 탈 거예요."),
            q("O que vai fazer no domingo?", ["Comprar presentes no mercado", "Ver o mar", "Voltar para casa cedo", "Comer peixe cru"], 0,
              "일요일에는 시장에서 선물을 살 거예요."),
        ],
    },
    {
        "id": "kr006", "level": L1, "topic": "clima", "title": "O tempo hoje e amanhã",
        "text": "오늘은 날씨가 아주 좋아요. 하늘이 맑고 따뜻해요. 그래서 저는 공원에서 자전거를 타요.\n\n"
                "하지만 내일은 비가 올 거예요. 그리고 조금 추울 거예요. 내일은 우산을 가지고 가야 해요.",
        "translation": "Hoje o tempo está ótimo. O céu está limpo e está quente. Por isso ando de bicicleta no parque.\n\n"
                       "Mas amanhã vai chover. E vai fazer um pouco de frio. Amanhã preciso levar guarda-chuva.",
        "questions": [
            q("Como está o tempo hoje?", ["Bom, céu limpo e quente", "Chuvoso", "Muito frio", "Com neve"], 0, "맑고 따뜻해요."),
            q("O que a pessoa faz hoje?", ["Anda de bicicleta no parque", "Fica em casa", "Vai à praia", "Compra um guarda-chuva"], 0,
              "공원에서 자전거를 타요."),
            q("O que precisa levar amanhã?", ["Guarda-chuva", "Bicicleta", "Casaco de verão", "Óculos de sol"], 0, "우산을 가지고 가야 해요."),
        ],
    },
    {
        "id": "kr007", "level": L1, "topic": "k-pop", "title": "Meu grupo favorito",
        "text": "제가 제일 좋아하는 가수는 '별빛'이에요. '별빛'은 다섯 명의 그룹이에요. 노래도 잘하고 춤도 잘 춰요.\n\n"
                "지난달에 저는 '별빛' 콘서트에 갔어요. 콘서트 표가 비쌌어요. 하지만 정말 재미있었어요. 저는 응원봉을 흔들고 노래를 따라 불렀어요.",
        "translation": "O cantor de que mais gosto é o grupo 'Byeolbit' (fictício). É um grupo de cinco membros. Cantam bem e dançam bem.\n\n"
                       "No mês passado fui ao show do 'Byeolbit'. O ingresso era caro. Mas foi muito divertido. Balancei o lightstick e cantei junto.",
        "questions": [
            q("Quantos membros tem o grupo?", ["Cinco", "Quatro", "Sete", "Três"], 0, "다섯 명의 그룹."),
            q("Quando a pessoa foi ao show?", ["No mês passado", "Ontem", "No ano passado", "Vai no próximo mês"], 0, "지난달에 = no mês passado."),
            q("Como era o ingresso?", ["Caro", "Barato", "Grátis", "Esgotado"], 0, "표가 비쌌어요."),
        ],
    },
    {
        "id": "kr008", "level": L1, "topic": "comida", "title": "No restaurante coreano",
        "text": "저는 친구하고 한국 식당에 갔어요. 저는 비빔밥을 먹었어요. 친구는 김치찌개를 먹었어요. 김치찌개는 조금 매웠어요.\n\n"
                "식당은 깨끗하고 음식도 맛있었어요. 그리고 값이 싸서 좋았어요. 다음에 또 가고 싶어요.",
        "translation": "Fui a um restaurante coreano com um amigo. Eu comi bibimbap. Meu amigo comeu kimchi jjigae. O kimchi jjigae estava um pouco apimentado.\n\n"
                       "O restaurante era limpo e a comida também estava gostosa. E foi bom porque o preço era barato. Quero ir de novo.",
        "questions": [
            q("O que a pessoa comeu?", ["Bibimbap", "Kimchi jjigae", "Ramyeon", "Gimbap"], 0, "저는 비빔밥을 먹었어요."),
            q("Como estava o kimchi jjigae?", ["Um pouco apimentado", "Doce", "Frio", "Sem gosto"], 0, "조금 매웠어요."),
            q("O que a pessoa achou do preço?", ["Barato", "Caro", "Normal", "Não comenta"], 0, "값이 싸서 좋았어요."),
        ],
    },
    {
        "id": "kr009", "level": L1, "topic": "compras", "title": "Um presente para o irmão",
        "text": "어제 백화점에 갔어요. 동생 생일 선물을 사고 싶었어요. 동생은 모자를 좋아해요.\n\n"
                "파란색 모자가 예뻤어요. 그런데 너무 비쌌어요. 그래서 시장에 가서 까만색 모자를 샀어요. 동생이 아주 좋아했어요.",
        "translation": "Ontem fui à loja de departamentos. Queria comprar o presente de aniversário do meu irmão mais novo. Ele gosta de bonés.\n\n"
                       "O boné azul era bonito. Mas era caro demais. Então fui ao mercado e comprei um boné preto. Meu irmão gostou muito.",
        "questions": [
            q("Para quem era o presente?", ["Irmão ou irmã mais novo(a)", "Mãe", "Amigo", "Professor"], 0, "동생 생일 선물."),
            q("Por que não comprou o boné azul?", ["Era caro demais", "Era feio", "Não tinha o tamanho", "A loja estava fechada"], 0, "너무 비쌌어요."),
            q("Onde comprou o boné preto?", ["No mercado", "Na loja de departamentos", "Pela internet", "Na loja de conveniência"], 0,
              "시장에 가서 까만색 모자를 샀어요."),
        ],
    },
    {
        "id": "kr010", "level": L1, "topic": "estudos", "title": "Por que estudo coreano",
        "text": "저는 브라질 사람이에요. 작년부터 한국어를 공부해요. 한국 드라마를 좋아해서 한국어를 배우고 싶었어요.\n\n"
                "한글은 쉬웠어요. 하지만 문법은 조금 어려워요. 저는 매일 단어를 열 개 외워요. 내년에 한국에 여행을 갈 거예요.",
        "translation": "Sou brasileiro(a). Estudo coreano desde o ano passado. Quis aprender coreano porque gosto de doramas.\n\n"
                       "O hangul foi fácil. Mas a gramática é um pouco difícil. Decoro dez palavras por dia. No ano que vem vou viajar para a Coreia.",
        "questions": [
            q("Desde quando a pessoa estuda coreano?", ["Desde o ano passado", "Desde criança", "Há uma semana", "Desde este mês"], 0,
              "작년부터 = desde o ano passado."),
            q("O que é difícil para ela?", ["A gramática", "O hangul", "A pronúncia", "Os números"], 0, "문법은 조금 어려워요."),
            q("Quantas palavras decora por dia?", ["Dez", "Cinco", "Vinte", "Cem"], 0, "단어를 열 개 외워요."),
        ],
    },
    {
        "id": "kr011", "level": L2, "topic": "moradia", "title": "Casa nova",
        "text": "지난주에 새 집으로 이사했어요. 전에 살던 집은 회사에서 멀어서 매일 한 시간 넘게 지하철을 탔어요. "
                "새 집은 회사에서 가까워서 걸어서 십오 분이면 도착해요.\n\n"
                "집은 작지만 창문이 커서 아주 밝아요. 근처에 공원과 마트도 있어서 편해요. 다음 주말에 친구들을 초대해서 집들이를 하려고 해요.",
        "translation": "Na semana passada me mudei para uma casa nova. A casa onde eu morava antes era longe do trabalho, então eu pegava metrô por mais de uma hora todo dia. "
                       "A casa nova é perto do trabalho: a pé, chego em quinze minutos.\n\n"
                       "A casa é pequena, mas as janelas são grandes e ela é bem iluminada. Perto há um parque e um mercado, então é prático. "
                       "No próximo fim de semana pretendo convidar amigos para uma festa de casa nova.",
        "questions": [
            q("Por que a pessoa se mudou?", ["A casa antiga era longe do trabalho", "A casa antiga era pequena", "Queria morar perto do parque", "Mudou de emprego"], 0,
              "회사에서 멀어서 = porque era longe do trabalho."),
            q("Quanto tempo leva a pé até o trabalho agora?", ["Quinze minutos", "Uma hora", "Cinco minutos", "Meia hora"], 0, "걸어서 십오 분."),
            q("O que ela pretende fazer no próximo fim de semana?", ["Uma festa de casa nova com amigos", "Mudar de novo", "Comprar móveis", "Viajar"], 0,
              "집들이 = festa para mostrar a casa nova."),
        ],
    },
    {
        "id": "kr012", "level": L2, "topic": "saúde", "title": "No médico",
        "text": "어제부터 머리가 아프고 열이 났어요. 그래서 오늘 아침에 회사에 가지 않고 병원에 갔어요. 의사 선생님이 감기라고 하셨어요.\n\n"
                "약을 먹고 푹 쉬면 괜찮을 거라고 하셨어요. 그리고 물을 많이 마시라고 하셨어요. 오늘은 집에서 쉬고 내일 다시 출근할 거예요.",
        "translation": "Desde ontem estou com dor de cabeça e febre. Por isso hoje de manhã não fui trabalhar e fui ao hospital. O médico disse que é gripe.\n\n"
                       "Disse que, se eu tomar o remédio e descansar bem, vou ficar bem. E disse para beber bastante água. "
                       "Hoje vou descansar em casa e amanhã volto ao trabalho.",
        "questions": [
            q("Quais eram os sintomas?", ["Dor de cabeça e febre", "Dor de barriga", "Tosse e dor nas costas", "Dor de dente"], 0, "머리가 아프고 열이 났어요."),
            q("O que o médico disse?", ["Que é gripe", "Que precisa de cirurgia", "Que não é nada", "Que deve trabalhar"], 0, "감기라고 하셨어요."),
            q("Qual foi o conselho?", ["Tomar remédio, descansar e beber água", "Fazer exercício", "Ir ao trabalho", "Comer apimentado"], 0,
              "약을 먹고 푹 쉬고 물을 많이 마시라고 하셨어요."),
        ],
    },
    {
        "id": "kr013", "level": L2, "topic": "trabalho", "title": "Meu trabalho de meio período",
        "text": "저는 주말마다 편의점에서 아르바이트를 해요. 토요일과 일요일에 오후 두 시부터 열 시까지 일해요. "
                "손님에게 물건을 계산해 주고 물건을 정리해요.\n\n"
                "일이 조금 힘들지만 사장님이 친절하셔서 괜찮아요. 아르바이트로 번 돈을 모아서 여름 방학에 일본으로 여행을 가고 싶어요.",
        "translation": "Todo fim de semana trabalho meio período numa loja de conveniência. Sábado e domingo trabalho das duas da tarde às dez. "
                       "Passo as compras dos clientes e organizo os produtos.\n\n"
                       "O trabalho é um pouco cansativo, mas o dono é gentil, então tudo bem. "
                       "Quero juntar o dinheiro do trabalho e viajar para o Japão nas férias de verão.",
        "questions": [
            q("Onde a pessoa trabalha?", ["Numa loja de conveniência", "Num café", "Num restaurante", "Numa escola"], 0, "편의점에서 아르바이트를 해요."),
            q("Qual é o horário?", ["Das 14h às 22h", "Das 9h às 18h", "Das 10h às 14h", "Das 22h às 2h"], 0, "오후 두 시부터 열 시까지."),
            q("Para que ela junta dinheiro?", ["Para viajar ao Japão nas férias", "Para comprar um celular", "Para pagar a faculdade", "Para se mudar"], 0,
              "여름 방학에 일본으로 여행을 가고 싶어요."),
        ],
    },
    {
        "id": "kr014", "level": L2, "topic": "dorama", "title": "Um dorama que recomendo",
        "text": "요즘 저는 '봄날의 약속'이라는 드라마를 보고 있어요. 이 드라마는 서울의 작은 꽃집을 배경으로 해요. 주인공은 꽃집 주인과 요리사예요.\n\n"
                "처음에는 두 사람이 자주 싸웠지만 점점 서로를 이해하게 돼요. 배우들의 연기가 자연스럽고 음악도 아름다워요. 아직 안 봤으면 꼭 한번 보세요.",
        "translation": "Ultimamente estou assistindo a um dorama chamado 'Promessa de primavera' (fictício). Ele se passa numa pequena floricultura de Seul. "
                       "Os protagonistas são a dona da floricultura e um cozinheiro.\n\n"
                       "No começo os dois brigavam muito, mas aos poucos passam a se entender. A atuação é natural e a música também é bonita. "
                       "Se ainda não viu, não deixe de assistir.",
        "questions": [
            q("Onde se passa o dorama?", ["Numa floricultura de Seul", "Num hospital", "Numa escola de Busan", "Num restaurante de Jeju"], 0,
              "서울의 작은 꽃집을 배경으로 해요."),
            q("Quem são os protagonistas?", ["A dona da floricultura e um cozinheiro", "Dois estudantes", "Um médico e uma cantora", "Duas irmãs"], 0,
              "꽃집 주인과 요리사."),
            q("Como era a relação no começo?", ["Brigavam muito", "Já eram namorados", "Eram melhores amigos", "Não se conheciam e nunca se falavam"], 0,
              "처음에는 자주 싸웠지만."),
        ],
    },
    {
        "id": "kr015", "level": L2, "topic": "viagem", "title": "Pedindo informação",
        "text": "관광객: 실례합니다. 경복궁에 어떻게 가요?\n\n행인: 지하철 3호선을 타고 경복궁역에서 내리세요.\n\n"
                "관광객: 여기서 지하철역이 멀어요?\n\n행인: 아니요, 이 길로 쭉 가서 오른쪽으로 가면 바로 있어요. 걸어서 오 분쯤 걸려요.\n\n"
                "관광객: 정말 감사합니다.\n\n행인: 천만에요. 즐거운 여행 되세요.",
        "translation": "Turista: Com licença. Como chego ao Gyeongbokgung?\n\nPedestre: Pegue a linha 3 do metrô e desça na estação Gyeongbokgung.\n\n"
                       "Turista: A estação de metrô é longe daqui?\n\nPedestre: Não, siga reto por esta rua e vire à direita: fica logo ali. Leva uns cinco minutos a pé.\n\n"
                       "Turista: Muito obrigado.\n\nPedestre: De nada. Boa viagem.",
        "questions": [
            q("Para onde o turista quer ir?", ["Palácio Gyeongbokgung", "Estação de Seul", "Mercado", "Aeroporto"], 0, "경복궁에 어떻게 가요?"),
            q("Qual linha de metrô deve pegar?", ["Linha 3", "Linha 1", "Linha 2", "Linha 9"], 0, "지하철 3호선."),
            q("Quanto tempo leva até a estação?", ["Uns cinco minutos a pé", "Meia hora", "Uma hora de ônibus", "Dez minutos de táxi"], 0, "걸어서 오 분쯤."),
        ],
    },
    {
        "id": "kr016", "level": L2, "topic": "hobby", "title": "Meu hobby é fotografar",
        "text": "제 취미는 사진 찍기예요. 고등학생 때 아버지께서 오래된 카메라를 주셨어요. 그때부터 사진에 관심이 생겼어요.\n\n"
                "주말에는 카메라를 들고 시내를 걸으면서 사진을 찍어요. 특히 사람들이 웃는 모습을 찍는 것을 좋아해요. "
                "언젠가 제 사진으로 작은 전시회를 열고 싶어요.",
        "translation": "Meu hobby é tirar fotos. No ensino médio, meu pai me deu uma câmera antiga. Desde então me interessei por fotografia.\n\n"
                       "No fim de semana, pego a câmera e tiro fotos enquanto caminho pelo centro. Gosto especialmente de fotografar pessoas sorrindo. "
                       "Um dia quero fazer uma pequena exposição com minhas fotos.",
        "questions": [
            q("Qual é o hobby da pessoa?", ["Fotografia", "Pintura", "Dança", "Cozinhar"], 0, "취미는 사진 찍기예요."),
            q("Quem deu a câmera?", ["O pai", "A mãe", "Um amigo", "O professor"], 0, "아버지께서 카메라를 주셨어요."),
            q("Qual é o sonho dela?", ["Fazer uma pequena exposição", "Comprar uma câmera nova", "Ser modelo", "Viajar o mundo"], 0,
              "작은 전시회를 열고 싶어요."),
        ],
    },
    {
        "id": "kr017", "level": L2, "topic": "estações", "title": "As estações na Coreia",
        "text": "한국에는 봄, 여름, 가을, 겨울 네 계절이 있어요. 봄에는 꽃이 많이 피어서 사람들이 꽃구경을 가요. "
                "여름은 덥고 비가 많이 와요. 그래서 7월에는 장마가 있어요.\n\n"
                "가을은 시원하고 하늘이 높아요. 단풍이 아름다워서 등산하는 사람이 많아요. 겨울은 춥고 눈이 와요. 저는 시원한 가을을 제일 좋아해요.",
        "translation": "Na Coreia há quatro estações: primavera, verão, outono e inverno. Na primavera muitas flores desabrocham e as pessoas saem para vê-las. "
                       "O verão é quente e chove muito. Por isso em julho há a temporada de chuvas.\n\n"
                       "O outono é fresco e o céu fica alto. As folhas coloridas são lindas, então muita gente faz trilha. "
                       "O inverno é frio e neva. Eu gosto mais do outono fresco.",
        "questions": [
            q("Quando é a temporada de chuvas?", ["Em julho", "Em abril", "Em outubro", "Em dezembro"], 0, "7월에는 장마가 있어요."),
            q("Por que muita gente faz trilha no outono?", ["As folhas coloridas são lindas", "É quente", "Neva", "Há muitas flores"], 0,
              "단풍이 아름다워서."),
            q("Qual estação a pessoa prefere?", ["Outono", "Primavera", "Verão", "Inverno"], 0, "시원한 가을을 제일 좋아해요."),
        ],
    },
    {
        "id": "kr018", "level": L2, "topic": "mensagens", "title": "Mudança de planos",
        "text": "지수 씨, 미안해요. 내일 저녁 일곱 시에 만나기로 했는데 갑자기 회사에 일이 생겼어요. 그래서 일곱 시까지 갈 수 없을 것 같아요.\n\n"
                "혹시 여덟 시 반에 만날 수 있어요? 아니면 토요일 점심은 어때요? 토요일에는 시간이 많아서 맛있는 식당에 같이 갈 수 있어요. 연락 주세요.",
        "translation": "Jisu, desculpe. Combinamos de nos encontrar amanhã às sete da noite, mas de repente surgiu trabalho na empresa. "
                       "Então acho que não vou conseguir chegar até as sete.\n\n"
                       "Será que podemos nos encontrar às oito e meia? Ou que tal almoço no sábado? No sábado tenho bastante tempo e podemos ir juntos a um restaurante gostoso. Me avise.",
        "questions": [
            q("Por que a pessoa precisa mudar o encontro?", ["Surgiu trabalho na empresa", "Está doente", "Perdeu o metrô", "Esqueceu o compromisso"], 0,
              "갑자기 회사에 일이 생겼어요."),
            q("Que horário ela sugere para amanhã?", ["20h30", "19h", "12h", "21h30"], 0, "여덟 시 반 = oito e meia."),
            q("Qual é a outra opção?", ["Almoço no sábado", "Café no domingo", "Jantar na sexta", "Cancelar de vez"], 0, "토요일 점심은 어때요?"),
        ],
    },
    {
        "id": "kr019", "level": L2, "topic": "consumo", "title": "Compras pela internet",
        "text": "요즘은 인터넷으로 물건을 사는 사람이 많아요. 집에서 편하게 주문할 수 있고, 보통 다음 날 배송돼요. 가격도 가게보다 싼 경우가 많아요.\n\n"
                "하지만 단점도 있어요. 옷이나 신발은 직접 입어 볼 수 없어서 사이즈가 안 맞을 때가 있어요. "
                "그래서 저는 옷은 가게에서 사고, 책이나 생활용품은 인터넷으로 사요.",
        "translation": "Hoje em dia muita gente compra pela internet. Dá para pedir com conforto em casa e normalmente chega no dia seguinte. "
                       "O preço também costuma ser mais barato que na loja.\n\n"
                       "Mas também há desvantagens. Roupas e sapatos não dá para provar, então às vezes o tamanho não serve. "
                       "Por isso compro roupas na loja e livros e itens do dia a dia pela internet.",
        "questions": [
            q("Qual é uma vantagem citada?", ["Chega normalmente no dia seguinte", "Dá para provar a roupa", "Sempre é mais caro", "Precisa ir à loja"], 0,
              "보통 다음 날 배송돼요."),
            q("Qual é a desvantagem?", ["Não dá para provar roupas e sapatos", "Demora um mês", "Só aceita dinheiro", "Não há livros"], 0,
              "직접 입어 볼 수 없어서."),
            q("O que a pessoa compra pela internet?", ["Livros e itens do dia a dia", "Roupas", "Sapatos", "Nada"], 0,
              "책이나 생활용품은 인터넷으로 사요."),
        ],
    },
    {
        "id": "kr020", "level": L2, "topic": "k-pop", "title": "No clube de dança",
        "text": "저는 대학교에서 댄스 동아리에 들어갔어요. 일주일에 두 번, 화요일과 목요일 저녁에 연습해요. "
                "동아리에서 케이팝 안무를 배우고 축제 때 공연을 해요.\n\n"
                "처음에는 춤을 잘 못 춰서 걱정했어요. 하지만 선배들이 친절하게 가르쳐 줘서 지금은 많이 늘었어요. "
                "다음 달 학교 축제에서 처음으로 무대에 설 거예요. 많이 떨리지만 기대돼요.",
        "translation": "Entrei no clube de dança da universidade. Ensaiamos duas vezes por semana, terça e quinta à noite. "
                       "No clube aprendemos coreografias de K-pop e nos apresentamos no festival.\n\n"
                       "No começo eu me preocupava porque não dançava bem. Mas os veteranos ensinaram com paciência e agora melhorei muito. "
                       "No mês que vem vou subir ao palco pela primeira vez no festival da escola. Estou nervoso, mas animado.",
        "questions": [
            q("Com que frequência o clube ensaia?", ["Duas vezes por semana", "Todo dia", "Uma vez por mês", "Só no fim de semana"], 0,
              "일주일에 두 번."),
            q("O que aprendem no clube?", ["Coreografias de K-pop", "Balé", "Canto", "Teatro"], 0, "케이팝 안무를 배우고."),
            q("O que vai acontecer no mês que vem?", ["A primeira apresentação no festival", "Uma viagem do clube", "Uma prova", "O fim do clube"], 0,
              "처음으로 무대에 설 거예요."),
        ],
    },
]

# Propostas para escrever e falar. "units" = mínimo de sílabas em hangul.
PROMPTS = [
    {"id": "kw01", "level": L1, "topic": "apresentação", "prompt": "자기소개를 해 보세요.",
     "prompt_pt": "Apresente-se: nome, idade, cidade e o que você estuda ou faz.", "units": 80, "lines": 4},
    {"id": "kw02", "level": L1, "topic": "rotina", "prompt": "하루 일과를 써 보세요.",
     "prompt_pt": "Conte sua rotina: a que horas acorda, o que come, como vai ao trabalho ou à escola.", "units": 80, "lines": 4},
    {"id": "kw03", "level": L1, "topic": "família", "prompt": "가족을 소개해 보세요.",
     "prompt_pt": "Apresente sua família: quantas pessoas, profissões e do que cada um gosta.", "units": 80, "lines": 4},
    {"id": "kw04", "level": L1, "topic": "comida", "prompt": "좋아하는 음식에 대해 써 보세요.",
     "prompt_pt": "Fale da sua comida favorita: o que é, quando come e por que gosta.", "units": 80, "lines": 4},
    {"id": "kw05", "level": L1, "topic": "passado", "prompt": "지난 주말에 뭐 했어요?",
     "prompt_pt": "Conte o que você fez no fim de semana passado (use o passado -았/었어요).", "units": 80, "lines": 4},
    {"id": "kw06", "level": L1, "topic": "k-pop", "prompt": "좋아하는 가수나 드라마를 소개해 보세요.",
     "prompt_pt": "Apresente um cantor, grupo ou dorama de que você gosta e diga por quê.", "units": 80, "lines": 4},
    {"id": "kw07", "level": L1, "topic": "cidade", "prompt": "우리 동네를 소개해 보세요.",
     "prompt_pt": "Descreva seu bairro: o que há perto, onde você costuma ir.", "units": 80, "lines": 4},
    {"id": "kw08", "level": L1, "topic": "futuro", "prompt": "다음 휴가에 뭐 할 거예요?",
     "prompt_pt": "Conte seus planos para as próximas férias (use -(으)ㄹ 거예요).", "units": 80, "lines": 4},
    {"id": "kw09", "level": L2, "topic": "estudos", "prompt": "한국어를 배우는 이유는 뭐예요?",
     "prompt_pt": "Explique por que você aprende coreano, o que é fácil e o que é difícil.", "units": 150, "lines": 6},
    {"id": "kw10", "level": L2, "topic": "viagem", "prompt": "기억에 남는 여행에 대해 써 보세요.",
     "prompt_pt": "Conte uma viagem marcante: onde foi, com quem, o que aconteceu.", "units": 150, "lines": 6},
    {"id": "kw11", "level": L2, "topic": "estações", "prompt": "좋아하는 계절과 그 이유를 써 보세요.",
     "prompt_pt": "Qual estação você prefere e por quê? Compare com outra estação.", "units": 150, "lines": 6},
    {"id": "kw12", "level": L2, "topic": "saúde", "prompt": "건강을 위해서 무엇을 해요?",
     "prompt_pt": "O que você faz pela sua saúde? Dê exemplos e diga o que quer melhorar.", "units": 150, "lines": 6},
    {"id": "kw13", "level": L2, "topic": "consumo", "prompt": "인터넷 쇼핑의 장점과 단점을 써 보세요.",
     "prompt_pt": "Escreva vantagens e desvantagens de comprar pela internet (use -지만, -아서/어서).", "units": 150, "lines": 6},
    {"id": "kw14", "level": L2, "topic": "mensagens", "prompt": "친구에게 약속을 바꾸는 메시지를 써 보세요.",
     "prompt_pt": "Escreva uma mensagem a um amigo mudando um encontro: peça desculpas, explique e proponha outro horário.", "units": 150, "lines": 6},
    {"id": "kw15", "level": L2, "topic": "hobby", "prompt": "취미를 소개해 보세요.",
     "prompt_pt": "Apresente seu hobby: como começou, quando pratica e o que sente.", "units": 150, "lines": 6},
    {"id": "kw16", "level": L2, "topic": "futuro", "prompt": "10년 후의 나는 어떤 모습일까요?",
     "prompt_pt": "Imagine você daqui a 10 anos: onde mora, o que faz, que sonhos realizou.", "units": 150, "lines": 6},
]

# Perguntas da entrevista (speaking · formato entrevista)
ROLEPLAY = "1. 가장 중요한 생각은 뭐예요? 2. 예를 하나 들어 주세요. 3. 왜 그렇게 생각해요?"
