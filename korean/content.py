"""Conteúdo do Korean Routine (TOPIK 1–2).

Escrito à mão; partículas são geradas pela regra do batchim (consoante final),
então ficam corretas por construção. Conjugações vêm de uma tabela revisada,
incluindo irregulares (듣다→들어요, 돕다→도와요, 걷다→걸어요...).
Revisão por professor ou falante nativo recomendada antes da venda.
"""

# ------------------------------------------------------------------ hangul
CONSONANTS = [
    ("ㄱ", "g/k", "giyeok"), ("ㄴ", "n", "nieun"), ("ㄷ", "d/t", "digeut"), ("ㄹ", "r/l", "rieul"),
    ("ㅁ", "m", "mieum"), ("ㅂ", "b/p", "bieup"), ("ㅅ", "s", "siot"), ("ㅇ", "muda / ng", "ieung"),
    ("ㅈ", "j", "jieut"), ("ㅊ", "ch", "chieut"), ("ㅋ", "k", "kieuk"), ("ㅌ", "t", "tieut"),
    ("ㅍ", "p", "pieup"), ("ㅎ", "h", "hieut"),
    ("ㄲ", "kk", "ssanggiyeok"), ("ㄸ", "tt", "ssangdigeut"), ("ㅃ", "pp", "ssangbieup"),
    ("ㅆ", "ss", "ssangsiot"), ("ㅉ", "jj", "ssangjieut"),
]
VOWELS = [
    ("ㅏ", "a"), ("ㅑ", "ya"), ("ㅓ", "eo"), ("ㅕ", "yeo"), ("ㅗ", "o"), ("ㅛ", "yo"), ("ㅜ", "u"),
    ("ㅠ", "yu"), ("ㅡ", "eu"), ("ㅣ", "i"), ("ㅐ", "ae"), ("ㅒ", "yae"), ("ㅔ", "e"), ("ㅖ", "ye"),
    ("ㅘ", "wa"), ("ㅙ", "wae"), ("ㅚ", "oe"), ("ㅝ", "wo"), ("ㅞ", "we"), ("ㅟ", "wi"), ("ㅢ", "ui"),
]

# Ordem Unicode das iniciais e vogais (para compor sílabas).
INITIALS = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
MEDIALS = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
# Romanização revisada de inicial em começo de sílaba.
INITIAL_RR = {"ㄱ": "g", "ㄲ": "kk", "ㄴ": "n", "ㄷ": "d", "ㄸ": "tt", "ㄹ": "r", "ㅁ": "m", "ㅂ": "b",
              "ㅃ": "pp", "ㅅ": "s", "ㅆ": "ss", "ㅇ": "", "ㅈ": "j", "ㅉ": "jj", "ㅊ": "ch", "ㅋ": "k",
              "ㅌ": "t", "ㅍ": "p", "ㅎ": "h"}
VOWEL_RR = dict(VOWELS)
SYLLABLE_INITIALS = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ"
SYLLABLE_VOWELS = "ㅏㅓㅗㅜㅡㅣ"

# Palavras para leitura, com a romanização revisada oficial (segue a pronúncia).
READING_WORDS = [
    ("한국", "Hanguk"), ("서울", "Seoul"), ("부산", "Busan"), ("김치", "gimchi"), ("사랑", "sarang"),
    ("친구", "chingu"), ("노래", "norae"), ("학교", "hakgyo"), ("커피", "keopi"), ("우유", "uyu"),
    ("바나나", "banana"), ("사과", "sagwa"), ("아이돌", "aidol"), ("드라마", "deurama"), ("오빠", "oppa"),
    ("언니", "eonni"), ("누나", "nuna"), ("엄마", "eomma"), ("아빠", "appa"), ("물", "mul"),
    ("밥", "bap"), ("집", "jip"), ("책", "chaek"), ("나무", "namu"), ("바다", "bada"),
    ("하늘", "haneul"), ("가수", "gasu"), ("배우", "baeu"), ("팬", "paen"), ("춤", "chum"),
    ("버스", "beoseu"), ("택시", "taeksi"), ("지하철", "jihacheol"), ("병원", "byeongwon"), ("시장", "sijang"),
    ("한국어", "Hangugeo"), ("음악", "eumak"), ("감사합니다", "gamsahamnida"), ("안녕하세요", "annyeonghaseyo"),
    ("떡볶이", "tteokbokki"), ("김밥", "gimbap"), ("라면", "ramyeon"), ("대박", "daebak"), ("화이팅", "hwaiting"),
]

# ------------------------------------------------------------------ vocabulário
# (coreano, português, tema, nível TOPIK)
VOCAB = [
    # pessoas e família
    ("사람", "pessoa", "pessoas", 1), ("친구", "amigo(a)", "pessoas", 1), ("가족", "família", "pessoas", 1),
    ("엄마", "mãe", "pessoas", 1), ("아빠", "pai", "pessoas", 1), ("어머니", "mãe (formal)", "pessoas", 1),
    ("아버지", "pai (formal)", "pessoas", 1), ("형", "irmão mais velho (dito por homem)", "pessoas", 1),
    ("오빠", "irmão mais velho (dito por mulher)", "pessoas", 1), ("누나", "irmã mais velha (dita por homem)", "pessoas", 1),
    ("언니", "irmã mais velha (dita por mulher)", "pessoas", 1), ("동생", "irmão ou irmã mais novo(a)", "pessoas", 1),
    ("남자", "homem", "pessoas", 1), ("여자", "mulher", "pessoas", 1), ("아이", "criança", "pessoas", 1),
    ("학생", "estudante", "pessoas", 1), ("선생님", "professor(a)", "pessoas", 1), ("의사", "médico(a)", "pessoas", 1),
    ("남자친구", "namorado", "pessoas", 1), ("여자친구", "namorada", "pessoas", 1), ("할머니", "avó", "pessoas", 1),
    ("할아버지", "avô", "pessoas", 1), ("회사원", "funcionário(a) de empresa", "pessoas", 2),
    # comida
    ("밥", "arroz cozido / refeição", "comida", 1), ("물", "água", "comida", 1), ("김치", "kimchi", "comida", 1),
    ("고기", "carne", "comida", 1), ("빵", "pão", "comida", 1), ("우유", "leite", "comida", 1),
    ("커피", "café (bebida)", "comida", 1), ("과일", "fruta", "comida", 1), ("사과", "maçã", "comida", 1),
    ("딸기", "morango", "comida", 1), ("라면", "lámen", "comida", 1), ("떡볶이", "tteokbokki (bolinho de arroz apimentado)", "comida", 1),
    ("김밥", "gimbap", "comida", 1), ("치킨", "frango frito", "comida", 1), ("맥주", "cerveja", "comida", 1),
    ("소주", "soju", "comida", 1), ("생선", "peixe (comida)", "comida", 1), ("계란", "ovo", "comida", 1),
    ("점심", "almoço", "comida", 1), ("음식", "comida", "comida", 1), ("야채", "verdura", "comida", 2),
    # lugares
    ("집", "casa", "lugares", 1), ("학교", "escola", "lugares", 1), ("회사", "empresa", "lugares", 1),
    ("병원", "hospital", "lugares", 1), ("은행", "banco (instituição)", "lugares", 1), ("식당", "restaurante", "lugares", 1),
    ("카페", "café (lugar)", "lugares", 1), ("시장", "mercado", "lugares", 1), ("공원", "parque", "lugares", 1),
    ("도서관", "biblioteca", "lugares", 1), ("화장실", "banheiro", "lugares", 1), ("방", "quarto", "lugares", 1),
    ("가게", "loja", "lugares", 1), ("편의점", "loja de conveniência", "lugares", 1), ("백화점", "loja de departamentos", "lugares", 2),
    ("공항", "aeroporto", "lugares", 1), ("역", "estação", "lugares", 1), ("호텔", "hotel", "lugares", 1),
    ("영화관", "cinema", "lugares", 1), ("노래방", "karaokê", "lugares", 1), ("우체국", "correio", "lugares", 2),
    # tempo
    ("오늘", "hoje", "tempo", 1), ("어제", "ontem", "tempo", 1), ("내일", "amanhã", "tempo", 1),
    ("지금", "agora", "tempo", 1), ("주말", "fim de semana", "tempo", 1), ("아침", "manhã", "tempo", 1),
    ("밤", "noite", "tempo", 1), ("월요일", "segunda-feira", "tempo", 1), ("금요일", "sexta-feira", "tempo", 1),
    ("일요일", "domingo", "tempo", 1), ("생일", "aniversário", "tempo", 1), ("방학", "férias escolares", "tempo", 2),
    ("매일", "todos os dias", "tempo", 1), ("항상", "sempre", "tempo", 1), ("가끔", "às vezes", "tempo", 2),
    ("다음 주", "semana que vem", "tempo", 1), ("이번 주", "esta semana", "tempo", 1),
    # objetos
    ("책", "livro", "objetos", 1), ("가방", "bolsa / mochila", "objetos", 1), ("옷", "roupa", "objetos", 1),
    ("신발", "sapato", "objetos", 1), ("모자", "boné / chapéu", "objetos", 1), ("우산", "guarda-chuva", "objetos", 1),
    ("시계", "relógio", "objetos", 1), ("휴대폰", "celular", "objetos", 1), ("컴퓨터", "computador", "objetos", 1),
    ("의자", "cadeira", "objetos", 1), ("책상", "escrivaninha", "objetos", 1), ("문", "porta", "objetos", 1),
    ("창문", "janela", "objetos", 1), ("침대", "cama", "objetos", 1), ("돈", "dinheiro", "objetos", 1),
    ("사진", "foto", "objetos", 1), ("편지", "carta", "objetos", 1), ("선물", "presente", "objetos", 1),
    ("열쇠", "chave", "objetos", 2), ("안경", "óculos", "objetos", 1),
    # K-pop
    ("노래", "música / canção", "kpop", 1), ("가수", "cantor(a)", "kpop", 1), ("아이돌", "ídolo (idol)", "kpop", 1),
    ("팬", "fã", "kpop", 1), ("콘서트", "show / concerto", "kpop", 1), ("춤", "dança", "kpop", 1),
    ("무대", "palco", "kpop", 2), ("앨범", "álbum", "kpop", 1), ("뮤직비디오", "videoclipe", "kpop", 1),
    ("데뷔", "estreia (debut)", "kpop", 2), ("그룹", "grupo", "kpop", 1), ("멤버", "integrante", "kpop", 1),
    ("응원봉", "lightstick", "kpop", 2), ("팬미팅", "fanmeeting", "kpop", 2), ("연습생", "trainee", "kpop", 2),
    # dorama
    ("드라마", "dorama / novela", "dorama", 1), ("배우", "ator / atriz", "dorama", 1), ("주인공", "protagonista", "dorama", 2),
    ("사랑", "amor", "dorama", 1), ("첫사랑", "primeiro amor", "dorama", 2), ("결혼", "casamento", "dorama", 1),
    ("비밀", "segredo", "dorama", 2), ("이야기", "história", "dorama", 1), ("영화", "filme", "dorama", 1),
    ("장면", "cena", "dorama", 2), ("눈물", "lágrima", "dorama", 2), ("마음", "coração / sentimento", "dorama", 2),
    ("꿈", "sonho", "dorama", 1), ("약속", "promessa / compromisso", "dorama", 1), ("운명", "destino", "dorama", 2),
    # corpo
    ("머리", "cabeça", "corpo", 1), ("손", "mão", "corpo", 1), ("발", "pé", "corpo", 1), ("입", "boca", "corpo", 1),
    ("코", "nariz", "corpo", 1), ("귀", "orelha", "corpo", 1), ("얼굴", "rosto", "corpo", 1), ("약", "remédio", "corpo", 1),
    # natureza e clima
    ("날씨", "tempo (clima)", "natureza", 1), ("비", "chuva", "natureza", 1), ("바람", "vento", "natureza", 1),
    ("하늘", "céu", "natureza", 1), ("바다", "mar", "natureza", 1), ("산", "montanha", "natureza", 1),
    ("강", "rio", "natureza", 1), ("꽃", "flor", "natureza", 1), ("나무", "árvore", "natureza", 1),
    ("해", "sol", "natureza", 1), ("달", "lua", "natureza", 1), ("별", "estrela", "natureza", 1),
    ("봄", "primavera", "natureza", 1), ("여름", "verão", "natureza", 1), ("가을", "outono", "natureza", 1),
    ("겨울", "inverno", "natureza", 1),
    # transporte e compras
    ("버스", "ônibus", "transporte", 1), ("지하철", "metrô", "transporte", 1), ("택시", "táxi", "transporte", 1),
    ("비행기", "avião", "transporte", 1), ("기차", "trem", "transporte", 1), ("자전거", "bicicleta", "transporte", 1),
    ("표", "bilhete / ingresso", "transporte", 1), ("가격", "preço", "transporte", 2),
]

# Adjetivos: (dicionário, português, presente, passado)
ADJECTIVES = [
    ("좋다", "ser bom", "좋아요", "좋았어요"), ("나쁘다", "ser ruim", "나빠요", "나빴어요"),
    ("크다", "ser grande", "커요", "컸어요"), ("작다", "ser pequeno", "작아요", "작았어요"),
    ("많다", "ser muito / ter muito", "많아요", "많았어요"), ("맛있다", "ser gostoso", "맛있어요", "맛있었어요"),
    ("재미있다", "ser divertido", "재미있어요", "재미있었어요"), ("예쁘다", "ser bonito(a)", "예뻐요", "예뻤어요"),
    ("멋있다", "ser estiloso / legal", "멋있어요", "멋있었어요"), ("바쁘다", "estar ocupado", "바빠요", "바빴어요"),
    ("비싸다", "ser caro", "비싸요", "비쌌어요"), ("싸다", "ser barato", "싸요", "쌌어요"),
    ("덥다", "estar quente (clima)", "더워요", "더웠어요"), ("춥다", "estar frio (clima)", "추워요", "추웠어요"),
    ("피곤하다", "estar cansado", "피곤해요", "피곤했어요"), ("행복하다", "estar feliz", "행복해요", "행복했어요"),
    ("슬프다", "estar triste", "슬퍼요", "슬펐어요"), ("아프다", "estar doente / doer", "아파요", "아팠어요"),
    ("쉽다", "ser fácil", "쉬워요", "쉬웠어요"), ("어렵다", "ser difícil", "어려워요", "어려웠어요"),
]
# Frases para adjetivos: (sujeito com partícula, adjetivo)
ADJECTIVE_SENTENCES = {
    "좋다": "날씨가", "나쁘다": "날씨가", "크다": "가방이", "작다": "방이", "많다": "사람이",
    "맛있다": "김치가", "재미있다": "드라마가", "예쁘다": "꽃이", "멋있다": "무대가", "바쁘다": "저는",
    "비싸다": "콘서트 표가", "싸다": "라면이", "덥다": "여름에는", "춥다": "겨울에는", "피곤하다": "오늘은",
    "행복하다": "저는", "슬프다": "그 장면이", "아프다": "머리가", "쉽다": "한글이", "어렵다": "시험이",
}

# Verbos: (dicionário, português, complemento, presente, passado, futuro|None, negação no presente)
VERBS = [
    ("가다", "ir", "학교에", "가요", "갔어요", "갈 거예요", "안 가요"),
    ("오다", "vir", "집에", "와요", "왔어요", "올 거예요", "안 와요"),
    ("먹다", "comer", "김치를", "먹어요", "먹었어요", "먹을 거예요", "안 먹어요"),
    ("마시다", "beber", "커피를", "마셔요", "마셨어요", "마실 거예요", "안 마셔요"),
    ("보다", "ver / assistir", "드라마를", "봐요", "봤어요", "볼 거예요", "안 봐요"),
    ("듣다", "ouvir", "노래를", "들어요", "들었어요", "들을 거예요", "안 들어요"),
    ("읽다", "ler", "책을", "읽어요", "읽었어요", "읽을 거예요", "안 읽어요"),
    ("쓰다", "escrever", "편지를", "써요", "썼어요", "쓸 거예요", "안 써요"),
    ("만나다", "encontrar", "친구를", "만나요", "만났어요", "만날 거예요", "안 만나요"),
    ("공부하다", "estudar", "한국어를", "공부해요", "공부했어요", "공부할 거예요", "공부 안 해요"),
    ("일하다", "trabalhar", "회사에서", "일해요", "일했어요", "일할 거예요", "일 안 해요"),
    ("운동하다", "fazer exercício", "공원에서", "운동해요", "운동했어요", "운동할 거예요", "운동 안 해요"),
    ("요리하다", "cozinhar", "집에서", "요리해요", "요리했어요", "요리할 거예요", "요리 안 해요"),
    ("사다", "comprar", "옷을", "사요", "샀어요", "살 거예요", "안 사요"),
    ("배우다", "aprender", "춤을", "배워요", "배웠어요", "배울 거예요", "안 배워요"),
    ("가르치다", "ensinar", "영어를", "가르쳐요", "가르쳤어요", "가르칠 거예요", "안 가르쳐요"),
    ("자다", "dormir", "일찍", "자요", "잤어요", "잘 거예요", "안 자요"),
    ("일어나다", "acordar / levantar", "일곱 시에", "일어나요", "일어났어요", "일어날 거예요", "안 일어나요"),
    ("기다리다", "esperar", "버스를", "기다려요", "기다렸어요", "기다릴 거예요", "안 기다려요"),
    ("좋아하다", "gostar", "케이팝을", "좋아해요", "좋아했어요", None, "안 좋아해요"),
    ("타다", "pegar (transporte)", "지하철을", "타요", "탔어요", "탈 거예요", "안 타요"),
    ("노래하다", "cantar", "무대에서", "노래해요", "노래했어요", "노래할 거예요", "노래 안 해요"),
    ("춤추다", "dançar", "친구와 같이", "춤춰요", "춤췄어요", "춤출 거예요", "춤 안 춰요"),
    ("찍다", "tirar (foto)", "사진을", "찍어요", "찍었어요", "찍을 거예요", "안 찍어요"),
    ("만들다", "fazer / preparar", "김밥을", "만들어요", "만들었어요", "만들 거예요", "안 만들어요"),
    ("살다", "morar / viver", "서울에서", "살아요", "살았어요", "살 거예요", "안 살아요"),
    ("앉다", "sentar", "의자에", "앉아요", "앉았어요", "앉을 거예요", "안 앉아요"),
    ("걷다", "caminhar", "공원에서", "걸어요", "걸었어요", "걸을 거예요", "안 걸어요"),
    ("돕다", "ajudar", "친구를", "도와요", "도왔어요", "도울 거예요", "안 도와요"),
    ("쉬다", "descansar", "집에서", "쉬어요", "쉬었어요", "쉴 거예요", "안 쉬어요"),
    ("씻다", "lavar", "손을", "씻어요", "씻었어요", "씻을 거예요", "안 씻어요"),
    ("열다", "abrir", "문을", "열어요", "열었어요", "열 거예요", "안 열어요"),
    ("닫다", "fechar", "창문을", "닫아요", "닫았어요", "닫을 거예요", "안 닫아요"),
    ("보내다", "enviar", "메시지를", "보내요", "보냈어요", "보낼 거예요", "안 보내요"),
    ("전화하다", "telefonar", "엄마한테", "전화해요", "전화했어요", "전화할 거예요", "전화 안 해요"),
    ("청소하다", "limpar", "방을", "청소해요", "청소했어요", "청소할 거예요", "청소 안 해요"),
    ("여행하다", "viajar", "부산을", "여행해요", "여행했어요", "여행할 거예요", "여행 안 해요"),
    ("말하다", "falar", "한국어로", "말해요", "말했어요", "말할 거예요", "말 안 해요"),
    ("울다", "chorar", "드라마를 보고", "울어요", "울었어요", "울 거예요", "안 울어요"),
    ("웃다", "rir / sorrir", "친구와 같이", "웃어요", "웃었어요", "웃을 거예요", "안 웃어요"),
]

# 에 (destino/existência) × 에서 (lugar onde a ação acontece)
LOCATION_SENTENCES = [
    ("학교___ 가요.", "에"), ("학교___ 공부해요.", "에서"), ("집___ 있어요.", "에"), ("집___ 쉬어요.", "에서"),
    ("회사___ 가요.", "에"), ("회사___ 일해요.", "에서"), ("카페___ 가요.", "에"), ("카페___ 커피를 마셔요.", "에서"),
    ("도서관___ 책을 읽어요.", "에서"), ("공원___ 운동해요.", "에서"), ("공항___ 도착해요.", "에"),
    ("식당___ 밥을 먹어요.", "에서"), ("병원___ 가요.", "에"), ("노래방___ 노래해요.", "에서"),
    ("콘서트___ 가요.", "에"), ("방___ 있어요.", "에"), ("무대___ 춤을 춰요.", "에서"),
    ("시장___ 과일을 사요.", "에서"), ("영화관___ 영화를 봐요.", "에서"), ("역___ 가요.", "에"),
    ("한국___ 가고 싶어요.", "에"), ("공원___ 사진을 찍어요.", "에서"), ("편의점___ 라면을 사요.", "에서"),
    ("내일 서울___ 가요.", "에"),
]

# (으)로: meio/instrumento
INSTRUMENT_NOUNS = ["버스", "지하철", "택시", "비행기", "기차", "자전거", "손", "한국어", "영어", "펜", "젓가락", "숟가락"]
INSTRUMENT_VERB = {"버스": "가요", "지하철": "가요", "택시": "가요", "비행기": "가요", "기차": "가요", "자전거": "가요",
                   "손": "먹어요", "한국어": "말해요", "영어": "말해요", "펜": "써요", "젓가락": "먹어요", "숟가락": "먹어요"}

# Frases para completar com 2–3 lacunas (como as combinações do English Routine).
# Sujeitos usados como tópico (은/는).
COMBO_SUBJECTS = ["저", "친구", "동생", "언니", "오빠", "형", "누나", "엄마", "아빠", "선생님", "학생", "가수"]
# (lugar, objeto, dicionário, presente, passado, futuro)
COMBO_ACTIVITIES = [
    ("카페", "커피", "마시다", "마셔요", "마셨어요", "마실 거예요"),
    ("식당", "비빔밥", "먹다", "먹어요", "먹었어요", "먹을 거예요"),
    ("집", "드라마", "보다", "봐요", "봤어요", "볼 거예요"),
    ("도서관", "책", "읽다", "읽어요", "읽었어요", "읽을 거예요"),
    ("학교", "한국어", "공부하다", "공부해요", "공부했어요", "공부할 거예요"),
    ("공원", "사진", "찍다", "찍어요", "찍었어요", "찍을 거예요"),
    ("시장", "과일", "사다", "사요", "샀어요", "살 거예요"),
    ("편의점", "라면", "사다", "사요", "샀어요", "살 거예요"),
    ("노래방", "노래", "부르다", "불러요", "불렀어요", "부를 거예요"),
    ("영화관", "영화", "보다", "봐요", "봤어요", "볼 거예요"),
    ("부엌", "김밥", "만들다", "만들어요", "만들었어요", "만들 거예요"),
    ("방", "음악", "듣다", "들어요", "들었어요", "들을 거예요"),
    ("회사", "메일", "보내다", "보내요", "보냈어요", "보낼 거예요"),
    ("연습실", "춤", "연습하다", "연습해요", "연습했어요", "연습할 거예요"),
    ("콘서트장", "응원봉", "흔들다", "흔들어요", "흔들었어요", "흔들 거예요"),
    ("백화점", "옷", "사다", "사요", "샀어요", "살 거예요"),
    ("빵집", "빵", "사다", "사요", "샀어요", "살 거예요"),
    ("체육관", "운동", "하다", "해요", "했어요", "할 거예요"),
    ("공항", "비행기", "기다리다", "기다려요", "기다렸어요", "기다릴 거예요"),
    ("역", "지하철", "타다", "타요", "탔어요", "탈 거예요"),
]

# Números
NUMBERS = [
    ("세 시", "3 horas", ["삼 시", "셋 시", "세 분"]), ("한 시", "1 hora", ["일 시", "하나 시", "한 분"]),
    ("두 시", "2 horas", ["이 시", "둘 시", "두 분"]), ("다섯 시", "5 horas", ["오 시", "다섯 분", "오 분"]),
    ("열두 시", "12 horas", ["십이 시", "열둘 시", "열두 분"]), ("삼십 분", "30 minutos", ["서른 분", "삼십 시", "세 분"]),
    ("십 분", "10 minutos", ["열 분", "십 시", "열 시"]), ("천 원", "1.000 wons", ["백 원", "만 원", "일천 시"]),
    ("오천 원", "5.000 wons", ["다섯천 원", "오만 원", "오백 원"]), ("만 원", "10.000 wons", ["일만 시", "천 원", "십천 원"]),
    ("사과 두 개", "duas maçãs", ["사과 둘 개", "사과 이 개", "사과 두 명"]), ("친구 세 명", "três amigos", ["친구 셋 명", "친구 삼 명", "친구 세 개"]),
    ("커피 한 잔", "um copo de café", ["커피 하나 잔", "커피 일 잔", "커피 한 명"]), ("스무 살", "20 anos (idade)", ["스물 살", "이십 살", "스무 시"]),
    ("삼월", "março", ["셋월", "세월", "삼일"]), ("유월", "junho", ["육월", "여섯월", "유일"]),
    ("시월", "outubro", ["십월", "열월", "시일"]), ("일요일", "domingo", ["일월", "하나요일", "일일"]),
    ("하나, 둘, 셋", "1, 2, 3 (nativos)", ["일, 이, 삼", "한, 두, 세", "하나, 이, 셋"]),
    ("일, 이, 삼", "1, 2, 3 (sino-coreanos)", ["하나, 둘, 셋", "한, 두, 세", "일, 둘, 삼"]),
]

# Frases úteis: (coreano, português, contexto)
PHRASES = [
    ("안녕하세요", "Olá", "cumprimento educado"), ("감사합니다", "Obrigado(a)", "formal"),
    ("고마워요", "Obrigado(a)", "educado, menos formal"), ("죄송합니다", "Desculpe", "formal"),
    ("괜찮아요", "Tudo bem / Não tem problema", ""), ("네", "Sim", ""), ("아니요", "Não", ""),
    ("잘 먹겠습니다", "Bom apetite (antes de comer)", "dito antes da refeição"),
    ("잘 먹었습니다", "Estava ótimo (depois de comer)", "dito depois da refeição"),
    ("처음 뵙겠습니다", "Muito prazer (primeira vez)", "formal"), ("만나서 반갑습니다", "Prazer em conhecer", ""),
    ("안녕히 가세요", "Tchau (para quem vai embora)", ""), ("안녕히 계세요", "Tchau (para quem fica)", ""),
    ("얼마예요?", "Quanto custa?", ""), ("화장실이 어디예요?", "Onde fica o banheiro?", ""),
    ("이거 주세요", "Me dá isto, por favor", ""), ("사랑해요", "Eu te amo", ""), ("보고 싶어요", "Sinto sua falta", ""),
    ("화이팅!", "Força! / Vamos lá!", "incentivo"), ("대박!", "Incrível! / Que demais!", "gíria"),
    ("진짜요?", "Sério?", ""), ("잠깐만요", "Um momento", ""), ("몰라요", "Não sei", ""), ("알겠어요", "Entendi", ""),
    ("다시 한번 말해 주세요", "Pode repetir, por favor?", ""), ("천천히 말해 주세요", "Fale devagar, por favor", ""),
    ("축하해요", "Parabéns", ""), ("생일 축하해요", "Feliz aniversário", ""), ("잘 자요", "Durma bem", ""),
    ("수고하셨습니다", "Bom trabalho / Obrigado pelo esforço", "fim do trabalho"),
]

GUIDE = [
    ("Hangul: como as sílabas se formam", "Cada bloco é uma sílaba: consoante inicial + vogal (+ consoante final, o batchim). 가 = ㄱ + ㅏ; 한 = ㅎ + ㅏ + ㄴ. A ㅇ inicial é muda (아 = a); no final soa ng (방 = bang)."),
    ("Batchim decide a partícula", "Se a palavra termina em consoante (tem batchim), use a forma com consoante: 은, 이, 을, 과, 이에요, 으로. Sem batchim: 는, 가, 를, 와, 예요, 로. Exceção: palavra terminada em ㄹ usa 로 (지하철로)."),
    ("은/는 — tópico", "Marca o assunto da frase, muitas vezes em contraste: 저는 학생이에요 (Eu sou estudante)."),
    ("이/가 — sujeito", "Marca quem faz ou o que existe/é descrito: 김치가 맛있어요 (O kimchi é gostoso), 시간이 있어요 (Tenho tempo)."),
    ("을/를 — objeto", "Marca o objeto direto: 드라마를 봐요 (Assisto ao dorama), 김밥을 먹어요."),
    ("이에요/예요 — ser", "Liga substantivo ao sujeito: 가수예요 (é cantor), 학생이에요 (é estudante)."),
    ("에 × 에서", "에 = destino ou lugar onde algo está (학교에 가요, 집에 있어요). 에서 = lugar onde a ação acontece (학교에서 공부해요)."),
    ("Presente educado -아요/-어요", "Radical com ㅏ ou ㅗ → -아요 (가다 → 가요, 보다 → 봐요); outros → -어요 (먹다 → 먹어요); 하다 → 해요. Irregulares comuns: 듣다 → 들어요, 돕다 → 도와요, 걷다 → 걸어요, 쓰다 → 써요."),
    ("Passado -았/었어요", "Mesma regra com -았어요/-었어요/했어요: 갔어요, 먹었어요, 공부했어요."),
    ("Futuro -(으)ㄹ 거예요", "Radical sem batchim → -ㄹ 거예요 (갈 거예요); com batchim → -을 거예요 (먹을 거예요); terminado em ㄹ → mantém (만들 거예요)."),
    ("Querer -고 싶어요", "Radical + 고 싶어요: 가고 싶어요 (quero ir), 먹고 싶어요 (quero comer)."),
    ("Negação com 안", "안 antes do verbo: 안 가요. Em verbos com 하다 separáveis, 안 vai antes de 해요: 공부 안 해요."),
    ("Números nativos × sino-coreanos", "Nativos (하나, 둘, 셋...) para horas, idade e contadores: 세 시, 스무 살, 두 개. Sino-coreanos (일, 이, 삼...) para minutos, dinheiro e datas: 삼십 분, 오천 원, 삼월. Atenção: 유월 (junho) e 시월 (outubro)."),
    ("Honoríficos e família", "Oppa/hyeong/eonni/nuna dependem de quem fala: mulher chama o irmão mais velho de 오빠 e a irmã de 언니; homem diz 형 e 누나. Nos doramas, 오빠 também é usado com namorados e amigos mais velhos."),
]
