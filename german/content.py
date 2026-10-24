"""Conteúdo do German Routine (alemão, A1–A2), pensado para quem fala português.

Conjugações: regras para os regulares + tabelas de irregulares (Präsens, Partizip II, auxiliar).
Revisão por professor ou falante nativo recomendada antes da venda.
"""

SOUNDS = [
    ("ä", "é aberto", "Käse", "como “é”"), ("ö", "ê com lábios de “o”", "schön", "diga “ê” arredondando os lábios"), ("ü", "i com lábios de “u”", "über", "diga “i” com lábios de “u”"),
    ("ß", "ss", "Straße", "sempre “ss”"), ("ch (ich)", "chiado suave", "ich", "depois de e, i, ä, ö, ü: como um “x” soprado"), ("ch (ach)", "rr de garganta", "Buch", "depois de a, o, u: som de garganta"),
    ("sch", "x", "Schule", "como “x” em “xícara”"), ("sp / st", "xp / xt", "Sport", "no início da palavra: “xp”, “xt”"), ("w", "v", "Wasser", "w soa “v”"),
    ("v", "f", "Vater", "v costuma soar “f”"), ("z", "ts", "Zeit", "sempre “ts”"), ("ei", "ai", "mein", "ei soa “ai”"), ("ie", "i longo", "Liebe", "ie soa “i”"),
    ("eu / äu", "oi", "heute", "soam “oi”"), ("j", "i", "ja", "j soa “i”"), ("-er final", "a", "Vater", "o -er final soa quase “a”"), ("h", "aspirado", "Haus", "no início, h aspirado como em inglês"),
]

VOCAB = [
    ("die Mutter", "a mãe", "pessoas", 1), ("der Vater", "o pai", "pessoas", 1), ("der Bruder", "o irmão", "pessoas", 1), ("die Schwester", "a irmã", "pessoas", 1),
    ("der Sohn", "o filho", "pessoas", 1), ("die Tochter", "a filha", "pessoas", 1), ("der Freund", "o amigo / namorado", "pessoas", 1), ("die Freundin", "a amiga / namorada", "pessoas", 1),
    ("das Kind", "a criança", "pessoas", 1), ("die Frau", "a mulher / senhora", "pessoas", 1), ("der Mann", "o homem / marido", "pessoas", 1), ("der Lehrer", "o professor", "pessoas", 1),
    ("der Arzt", "o médico", "pessoas", 1), ("der Nachbar", "o vizinho", "pessoas", 2), ("der Großvater", "o avô", "pessoas", 1), ("die Großmutter", "a avó", "pessoas", 1),
    ("der Kellner", "o garçom", "pessoas", 2), ("der Chef", "o chefe", "pessoas", 2), ("der Student", "o estudante", "pessoas", 1), ("die Eltern", "os pais", "pessoas", 1),
    ("das Brot", "o pão", "comida", 1), ("das Wasser", "a água", "comida", 1), ("die Milch", "o leite", "comida", 1), ("der Kaffee", "o café", "comida", 1), ("der Tee", "o chá", "comida", 1),
    ("der Käse", "o queijo", "comida", 1), ("der Apfel", "a maçã", "comida", 1), ("das Ei", "o ovo", "comida", 1), ("das Hähnchen", "o frango", "comida", 1),
    ("das Fleisch", "a carne", "comida", 1), ("der Fisch", "o peixe", "comida", 1), ("der Reis", "o arroz", "comida", 1), ("das Obst", "a fruta", "comida", 1),
    ("der Kuchen", "o bolo", "comida", 1), ("das Eis", "o sorvete", "comida", 1), ("das Frühstück", "o café da manhã", "comida", 1), ("das Mittagessen", "o almoço", "comida", 1),
    ("das Abendessen", "o jantar", "comida", 1), ("der Wein", "o vinho", "comida", 2), ("das Bier", "a cerveja", "comida", 2), ("das Brötchen", "o pãozinho", "comida", 1),
    ("die Butter", "a manteiga", "comida", 2), ("der Zucker", "o açúcar", "comida", 2), ("der Saft", "o suco", "comida", 1), ("die Kartoffel", "a batata", "comida", 1),
    ("das Haus", "a casa", "lugares", 1), ("die Schule", "a escola", "lugares", 1), ("der Supermarkt", "o supermercado", "lugares", 1), ("das Restaurant", "o restaurante", "lugares", 1),
    ("das Krankenhaus", "o hospital", "lugares", 1), ("der Strand", "a praia", "lugares", 1), ("die Stadt", "a cidade", "lugares", 1), ("die Straße", "a rua", "lugares", 1),
    ("das Geschäft", "a loja", "lugares", 1), ("der Park", "o parque", "lugares", 1), ("die Bibliothek", "a biblioteca", "lugares", 1), ("das Kino", "o cinema", "lugares", 1),
    ("der Flughafen", "o aeroporto", "lugares", 2), ("der Bahnhof", "a estação de trem", "lugares", 1), ("die Bank", "o banco", "lugares", 2), ("die Apotheke", "a farmácia", "lugares", 1),
    ("die Bäckerei", "a padaria", "lugares", 1), ("das Museum", "o museu", "lugares", 1), ("das Büro", "o escritório", "lugares", 1), ("der Platz", "a praça", "lugares", 1),
    ("das Stadion", "o estádio", "lugares", 2), ("das Theater", "o teatro", "lugares", 2), ("die Kirche", "a igreja", "lugares", 2), ("das Rathaus", "a prefeitura", "lugares", 2),
    ("heute", "hoje", "tempo", 1), ("morgen", "amanhã", "tempo", 1), ("gestern", "ontem", "tempo", 1), ("jetzt", "agora", "tempo", 1), ("immer", "sempre", "tempo", 1),
    ("nie", "nunca", "tempo", 1), ("die Woche", "a semana", "tempo", 1), ("der Monat", "o mês", "tempo", 1), ("das Jahr", "o ano", "tempo", 1), ("der Tag", "o dia", "tempo", 1),
    ("die Nacht", "a noite (madrugada)", "tempo", 1), ("der Abend", "a noite (fim do dia)", "tempo", 1), ("das Wochenende", "o fim de semana", "tempo", 1),
    ("oft", "frequentemente", "tempo", 2), ("schon", "já", "tempo", 2), ("noch", "ainda", "tempo", 2), ("früh", "cedo", "tempo", 2), ("spät", "tarde (atrasado)", "tempo", 2),
    ("das Buch", "o livro", "objetos", 1), ("der Tisch", "a mesa", "objetos", 1), ("der Stuhl", "a cadeira", "objetos", 1), ("das Auto", "o carro", "objetos", 1),
    ("das Handy", "o celular", "objetos", 1), ("der Schlüssel", "a chave", "objetos", 1), ("die Kleidung", "a roupa", "objetos", 1), ("die Schuhe", "os sapatos", "objetos", 1),
    ("das Hemd", "a camisa", "objetos", 1), ("das Geld", "o dinheiro", "objetos", 1), ("der Computer", "o computador", "objetos", 1), ("die Tasche", "a bolsa", "objetos", 1),
    ("die Brille", "os óculos", "objetos", 2), ("die Uhr", "o relógio", "objetos", 2), ("das Bett", "a cama", "objetos", 1), ("die Zeitung", "o jornal", "objetos", 2),
    ("die Fahrkarte", "a passagem", "objetos", 2), ("der Film", "o filme", "objetos", 1), ("das Lied", "a canção", "objetos", 1), ("der Brief", "a carta", "objetos", 1),
    ("die Sonne", "o sol", "natureza", 1), ("der Regen", "a chuva", "natureza", 1), ("das Meer", "o mar", "natureza", 1), ("der Hund", "o cachorro", "natureza", 1),
    ("die Katze", "o gato", "natureza", 1), ("der Berg", "a montanha", "natureza", 2), ("der Baum", "a árvore", "natureza", 2), ("die Blume", "a flor", "natureza", 1), ("der Schnee", "a neve", "natureza", 1),
    ("der Kopf", "a cabeça", "corpo", 1), ("die Hand", "a mão", "corpo", 1), ("der Fuß", "o pé", "corpo", 1), ("die Augen", "os olhos", "corpo", 1), ("der Mund", "a boca", "corpo", 2),
    ("der Bauch", "a barriga", "corpo", 2), ("der Rücken", "as costas", "corpo", 2), ("die Haare", "o cabelo", "corpo", 2),
    ("der Zug", "o trem", "transporte", 1), ("der Bus", "o ônibus", "transporte", 1), ("das Flugzeug", "o avião", "transporte", 1), ("die U-Bahn", "o metrô", "transporte", 1),
    ("das Fahrrad", "a bicicleta", "transporte", 1), ("das Taxi", "o táxi", "transporte", 1),
    ("sprechen", "falar", "verbos", 1), ("essen", "comer", "verbos", 1), ("wohnen", "morar", "verbos", 1), ("arbeiten", "trabalhar", "verbos", 1), ("lernen", "aprender / estudar", "verbos", 1),
    ("trinken", "beber", "verbos", 1), ("schreiben", "escrever", "verbos", 1), ("lesen", "ler", "verbos", 1), ("kaufen", "comprar", "verbos", 1), ("hören", "ouvir", "verbos", 1),
    ("sehen", "ver", "verbos", 1), ("haben", "ter", "verbos", 1), ("sein", "ser / estar", "verbos", 1), ("gehen", "ir (a pé)", "verbos", 1), ("machen", "fazer", "verbos", 1),
    ("wollen", "querer", "verbos", 1), ("können", "poder / saber fazer", "verbos", 1), ("kommen", "vir", "verbos", 1), ("nehmen", "pegar / tomar", "verbos", 1), ("fahren", "ir (de veículo)", "verbos", 1),
    ("schlafen", "dormir", "verbos", 1), ("lieben", "amar", "verbos", 1), ("suchen", "procurar", "verbos", 2), ("warten", "esperar", "verbos", 2), ("reisen", "viajar", "verbos", 2),
    ("singen", "cantar", "verbos", 1), ("tanzen", "dançar", "verbos", 1), ("wissen", "saber", "verbos", 2), ("kennen", "conhecer", "verbos", 2), ("helfen", "ajudar", "verbos", 2),
    ("groß", "grande", "adjetivos", 1), ("klein", "pequeno", "adjetivos", 1), ("gut", "bom", "adjetivos", 1), ("schlecht", "ruim", "adjetivos", 1), ("schön", "bonito", "adjetivos", 1),
    ("teuer", "caro", "adjetivos", 1), ("neu", "novo", "adjetivos", 1), ("alt", "velho", "adjetivos", 1), ("glücklich", "feliz", "adjetivos", 1), ("traurig", "triste", "adjetivos", 1),
    ("müde", "cansado", "adjetivos", 1), ("einfach", "fácil", "adjetivos", 2), ("schwierig", "difícil", "adjetivos", 2), ("warm", "quente", "adjetivos", 1), ("kalt", "frio", "adjetivos", 1),
    ("rot", "vermelho", "adjetivos", 1), ("gelb", "amarelo", "adjetivos", 1), ("blau", "azul", "adjetivos", 1), ("grün", "verde", "adjetivos", 1), ("nett", "simpático / gentil", "adjetivos", 1),
]

FALSE_FRIENDS = [
    ("der Rat", "o conselho", "o rato"), ("die Tante", "a tia", "tanto"), ("das Gymnasium", "o colégio (ensino médio)", "o ginásio de esportes"), ("bekommen", "receber", "comer bem"),
    ("die Marmelade", "a geleia", "a marmelada"), ("das Kompliment", "o elogio", "o cumprimento"), ("der Chef", "o chefe (patrão)", "o chef de cozinha"), ("die Bombe", "a bomba (explosivo)", "a bomba-d'água"),
    ("also", "então / portanto", "também"), ("der Pass", "o passaporte", "o passe"), ("der Prospekt", "o folheto", "o prospecto (perspectiva)"), ("die Promotion", "o doutorado", "a promoção"),
    ("das Handy", "o celular", "o prático"), ("sensibel", "sensível (emotivo)", "sensato"), ("die Konkurrenz", "a concorrência", "o concurso"), ("die Novelle", "a novela literária curta", "a novela de TV"),
    ("der Tisch", "a mesa", "o tecido"), ("brav", "bem-comportado", "bravo (irritado)"), ("der Kurs", "o curso / a cotação", "o curso superior"), ("die Fabrik", "a fábrica", "o tecido (fabric)"),
    ("das Lokal", "o bar / restaurante", "o local (lugar)"), ("die Rente", "a aposentadoria", "a renda"), ("die Mappe", "a pasta (de papéis)", "o mapa"), ("der Hut", "o chapéu", "a cabana"),
    ("bald", "logo / em breve", "balde"),
]

PERSONS = ["ich", "du", "er", "wir", "ihr", "sie"]
PRESENT = {
    "sein": ["bin", "bist", "ist", "sind", "seid", "sind"], "haben": ["habe", "hast", "hat", "haben", "habt", "haben"],
    "werden": ["werde", "wirst", "wird", "werden", "werdet", "werden"], "fahren": ["fahre", "fährst", "fährt", "fahren", "fahrt", "fahren"],
    "essen": ["esse", "isst", "isst", "essen", "esst", "essen"], "lesen": ["lese", "liest", "liest", "lesen", "lest", "lesen"],
    "sehen": ["sehe", "siehst", "sieht", "sehen", "seht", "sehen"], "nehmen": ["nehme", "nimmst", "nimmt", "nehmen", "nehmt", "nehmen"],
    "sprechen": ["spreche", "sprichst", "spricht", "sprechen", "sprecht", "sprechen"], "treffen": ["treffe", "triffst", "trifft", "treffen", "trefft", "treffen"],
    "geben": ["gebe", "gibst", "gibt", "geben", "gebt", "geben"], "schlafen": ["schlafe", "schläfst", "schläft", "schlafen", "schlaft", "schlafen"],
    "laufen": ["laufe", "läufst", "läuft", "laufen", "lauft", "laufen"], "helfen": ["helfe", "hilfst", "hilft", "helfen", "helft", "helfen"],
    "wissen": ["weiß", "weißt", "weiß", "wissen", "wisst", "wissen"], "können": ["kann", "kannst", "kann", "können", "könnt", "können"],
    "wollen": ["will", "willst", "will", "wollen", "wollt", "wollen"], "möchten": ["möchte", "möchtest", "möchte", "möchten", "möchtet", "möchten"],
    "müssen": ["muss", "musst", "muss", "müssen", "müsst", "müssen"], "tragen": ["trage", "trägst", "trägt", "tragen", "tragt", "tragen"],
}
PARTICIPLE = {
    "sein": "gewesen", "haben": "gehabt", "fahren": "gefahren", "essen": "gegessen", "lesen": "gelesen", "sehen": "gesehen", "nehmen": "genommen",
    "sprechen": "gesprochen", "treffen": "getroffen", "geben": "gegeben", "schlafen": "geschlafen", "laufen": "gelaufen", "helfen": "geholfen",
    "gehen": "gegangen", "kommen": "gekommen", "fliegen": "geflogen", "bleiben": "geblieben", "trinken": "getrunken", "schreiben": "geschrieben",
    "finden": "gefunden", "singen": "gesungen", "kennen": "gekannt", "wissen": "gewusst", "tragen": "getragen",
}
SEIN_VERBS = {"sein", "fahren", "gehen", "kommen", "fliegen", "bleiben", "laufen", "reisen"}

# (infinitivo, português, complemento, nível)
VERBS = [
    ("sprechen", "falar", "Deutsch", 1), ("arbeiten", "trabalhar", "in Berlin", 1), ("wohnen", "morar", "in München", 1), ("lernen", "aprender", "Deutsch", 1),
    ("spielen", "jogar", "Fußball", 1), ("kaufen", "comprar", "Brot", 1), ("trinken", "beber", "Kaffee", 1), ("essen", "comer", "Pizza", 1),
    ("lesen", "ler", "ein Buch", 1), ("sehen", "ver", "einen Film", 1), ("schreiben", "escrever", "eine E-Mail", 1), ("hören", "ouvir", "Musik", 1),
    ("kochen", "cozinhar", "Nudeln", 1), ("machen", "fazer", "Sport", 1), ("fahren", "ir de veículo", "nach Hamburg", 1), ("gehen", "ir a pé", "nach Hause", 1),
    ("kommen", "vir", "aus Brasilien", 1), ("fliegen", "voar", "nach Wien", 2), ("schlafen", "dormir", "acht Stunden", 1), ("nehmen", "pegar", "den Bus", 1),
    ("geben", "dar", "ein Geschenk", 2), ("treffen", "encontrar", "Freunde", 2), ("finden", "achar", "den Schlüssel", 2), ("tanzen", "dançar", "Samba", 1),
    ("reisen", "viajar", "nach Italien", 2), ("studieren", "estudar (faculdade)", "Medizin", 2), ("besuchen", "visitar", "die Oma", 2), ("bezahlen", "pagar", "die Rechnung", 2),
    ("warten", "esperar", "auf den Zug", 2), ("öffnen", "abrir", "das Fenster", 2), ("laufen", "correr", "im Park", 2), ("bleiben", "ficar", "zu Hause", 2),
    ("haben", "ter", "Hunger", 1), ("helfen", "ajudar", "der Nachbarin", 2), ("singen", "cantar", "ein Lied", 1), ("tragen", "vestir / carregar", "eine Jacke", 2),
]

GRAMMAR = [
    ("___ Hund ist groß.", "Der", ["Die", "Das", "Den"], "Hund é masculino → der.", 1, "artigos"),
    ("___ Katze schläft.", "Die", ["Der", "Das", "Dem"], "Katze é feminino → die.", 1, "artigos"),
    ("___ Kind spielt.", "Das", ["Der", "Die", "Den"], "Kind é neutro → das.", 1, "artigos"),
    ("Ich sehe ___ Hund.", "den", ["der", "dem", "das"], "Objeto direto masculino (Akkusativ): der → den.", 1, "acusativo"),
    ("Ich kaufe ___ Brot.", "das", ["den", "dem", "der"], "Neutro não muda no acusativo: das.", 1, "acusativo"),
    ("Ich habe ___ Bruder.", "einen", ["ein", "eine", "einem"], "Masculino no acusativo: ein → einen.", 1, "acusativo"),
    ("Ich habe ___ Auto.", "kein", ["keinen", "keine", "nicht"], "Negar substantivo neutro: kein.", 1, "negação"),
    ("Er trinkt ___ Kaffee.", "keinen", ["kein", "keine", "nicht"], "Kaffee é masculino: keinen no acusativo.", 2, "negação"),
    ("Ich wohne ___ Berlin.", "in", ["nach", "zu", "aus"], "Morar em cidade: in.", 1, "preposições"),
    ("Ich fahre ___ Berlin.", "nach", ["in", "zu", "bei"], "Ir para cidade/país: nach.", 1, "preposições"),
    ("Ich komme ___ Brasilien.", "aus", ["von", "nach", "in"], "Origem (país): aus.", 1, "preposições"),
    ("Ich gehe ___ Kino.", "ins", ["im", "in den", "in die"], "Movimento + neutro: in das = ins.", 2, "preposições"),
    ("Ich bin ___ Kino.", "im", ["ins", "in die", "in den"], "Lugar (onde?) + neutro: in dem = im.", 2, "preposições"),
    ("Ich gehe ___ Hause.", "nach", ["zu", "in", "im"], "Ir para casa: nach Hause.", 2, "preposições"),
    ("Ich bin ___ Hause.", "zu", ["nach", "in", "im"], "Estar em casa: zu Hause.", 2, "preposições"),
    ("Ich ___ Brasilianer.", "bin", ["bist", "ist", "habe"], "sein com ich → bin.", 1, "sein / haben"),
    ("Sie ___ zwanzig Jahre alt.", "ist", ["hat", "bist", "sind"], "Idade usa sein: Sie ist zwanzig Jahre alt.", 1, "sein / haben"),
    ("Wir ___ Hunger.", "haben", ["sind", "habt", "hat"], "Fome: Hunger haben.", 1, "sein / haben"),
    ("Heute ___ ich ins Kino.", "gehe", ["ich gehe", "gehen", "geht"], "Verbo na 2ª posição: Heute gehe ich…", 1, "ordem das palavras"),
    ("Morgen ___ wir nach Berlin.", "fahren", ["wir fahren", "fahrt", "fährt"], "Verbo na 2ª posição: Morgen fahren wir…", 1, "ordem das palavras"),
    ("Ich kann gut ___.", "schwimmen", ["schwimme", "schwimmt", "geschwommen"], "Verbo modal + infinitivo no final.", 1, "modais"),
    ("Ich ___ Deutsch lernen.", "möchte", ["möchten", "möchtest", "mag"], "möchte + infinitivo no final.", 1, "modais"),
    ("Du ___ heute arbeiten.", "musst", ["muss", "müssen", "müsst"], "müssen com du → musst.", 2, "modais"),
    ("Ich ___ gestern im Kino.", "war", ["bin", "habe", "wurde"], "Passado de sein (Präteritum): war.", 2, "passado"),
    ("Wir ___ gestern keine Zeit.", "hatten", ["haben", "waren", "hattet"], "Passado de haben: hatten.", 2, "passado"),
    ("Ich habe Pizza ___.", "gegessen", ["essen", "gegesst", "isst"], "Perfekt: haben + particípio no final.", 2, "Perfekt"),
    ("Er ist nach Berlin ___.", "gefahren", ["gefahrt", "fahren", "fährt"], "Movimento → sein + gefahren.", 2, "Perfekt"),
    ("Ich ___ nach Hause gegangen.", "bin", ["habe", "hat", "ist"], "gehen usa sein no Perfekt.", 2, "Perfekt"),
    ("Ich ___ einen Film gesehen.", "habe", ["bin", "ist", "hat"], "sehen usa haben no Perfekt.", 2, "Perfekt"),
    ("Das ist ___ Mutter.", "meine", ["mein", "meinen", "meiner"], "Mutter é feminino → meine.", 1, "possessivos"),
    ("Das ist ___ Vater.", "mein", ["meine", "meinen", "meinem"], "Vater é masculino (nominativo) → mein.", 1, "possessivos"),
    ("Ich besuche ___ Bruder.", "meinen", ["mein", "meine", "meinem"], "Acusativo masculino → meinen.", 2, "possessivos"),
    ("Wie ___ es dir?", "geht", ["gehst", "ist", "hast"], "Como vai? → Wie geht es dir?", 1, "frases"),
    ("___ heißt du?", "Wie", ["Was", "Wo", "Wer"], "Como você se chama? → Wie heißt du?", 1, "perguntas"),
    ("___ wohnst du?", "Wo", ["Wie", "Wer", "Wann"], "Lugar → wo.", 1, "perguntas"),
    ("___ kommst du?", "Woher", ["Wohin", "Wo", "Wie"], "Origem → woher.", 1, "perguntas"),
    ("Anna ist ___ als Paul.", "größer", ["groß", "am größten", "mehr groß"], "Comparativo: groß → größer als.", 2, "comparação"),
    ("Es ___ ein Café hier.", "gibt", ["hat", "habt", "sind"], "Há = es gibt (+ acusativo).", 1, "es gibt"),
    ("Ich mag ___ nicht.", "ihn", ["er", "ihm", "sein"], "Pronome masculino no acusativo: ihn.", 2, "pronomes"),
    ("Ich helfe ___.", "dir", ["dich", "du", "dein"], "helfen pede dativo: dir.", 2, "pronomes"),
]

NUMBERS = [
    ("fünfzehn", "15", ["fünf", "fünfzig", "vierzehn"]), ("zwanzig", "20", ["zwölf", "dreißig", "zwei"]), ("sechzehn", "16", ["sechs", "sechzig", "siebzehn"]),
    ("einunddreißig", "31", ["dreiundzehn", "dreizehn", "dreißigeins"]), ("siebzig", "70", ["sechzig", "siebzehn", "siebenhundert"]), ("achtzig", "80", ["acht", "achtzehn", "achthundert"]),
    ("neunzig", "90", ["neun", "neunzehn", "neunhundert"]), ("hundert", "100", ["tausend", "zehn", "hundertzehn"]), ("tausend", "1.000", ["hundert", "zehntausend", "eine Million"]),
    ("einundzwanzig", "21", ["zwanzigeins", "zweiundzwanzig", "zwölf"]), ("halb drei", "2h30", ["halb zwei", "drei Uhr", "Viertel nach drei"]), ("Mittag", "meio-dia", ["Mitternacht", "Abend", "Morgen"]),
    ("Montag", "segunda-feira", ["Dienstag", "Sonntag", "Samstag"]), ("Mittwoch", "quarta-feira", ["Dienstag", "Donnerstag", "Freitag"]), ("Januar", "janeiro", ["Juni", "Juli", "Februar"]),
    ("zehn Euro", "10 euros", ["zwei Euro", "zwölf Euro", "hundert Euro"]), ("ich bin zwanzig", "tenho 20 anos", ["ich habe zwanzig", "ich zwanzig habe", "mein zwanzig"]),
    ("der erste Mai", "1º de maio", ["der eins Mai", "Mai erste", "die erste Mai"]), ("dreihundert", "300", ["dreißig", "dreizehn", "dreihundertdrei"]), ("achtzehn", "18", ["acht", "achtzig", "achtzehnte"]),
]

PHRASES = [
    ("Hallo", "Oi", "informal"), ("Guten Morgen", "Bom dia", ""), ("Guten Abend", "Boa noite (cumprimento)", ""), ("Wie geht's?", "Como vai?", ""),
    ("Freut mich", "Muito prazer", ""), ("Danke", "Obrigado(a)", ""), ("Bitte schön", "De nada", ""), ("Entschuldigung", "Com licença / Desculpe", ""),
    ("Tut mir leid", "Sinto muito", ""), ("Bitte", "Por favor", ""), ("Was kostet das?", "Quanto custa?", ""), ("Wo ist die Toilette?", "Onde fica o banheiro?", ""),
    ("Ich verstehe nicht", "Não entendo", ""), ("Können Sie das wiederholen?", "Pode repetir?", "formal"), ("Langsamer, bitte", "Mais devagar, por favor", ""), ("Die Rechnung, bitte", "A conta, por favor", ""),
    ("Lecker!", "Delicioso!", ""), ("Prost!", "Saúde! (brinde)", ""), ("Ich liebe dich", "Eu te amo", ""), ("Alles Gute zum Geburtstag!", "Feliz aniversário!", ""),
    ("Bis bald", "Até breve", ""), ("Bis morgen", "Até amanhã", ""), ("Guten Appetit!", "Bom apetite!", ""), ("Gute Nacht", "Boa noite (ao dormir)", ""),
    ("Kein Problem", "Sem problema", ""), ("Schade!", "Que pena!", ""), ("Einverstanden", "Combinado", ""), ("Wie spät ist es?", "Que horas são?", ""),
    ("Ich heiße…", "Meu nome é…", ""), ("Tschüss", "Tchau", "informal"),
]

SUBJECTS = [("Ich", 0), ("Du", 1), ("Er", 2), ("Wir", 3), ("Ihr", 4), ("Anna", 2), ("Paul", 2), ("Mein Bruder", 2), ("Meine Schwester", 2),
            ("Meine Freunde", 5), ("Meine Eltern", 5), ("Der Lehrer", 2), ("Die Nachbarin", 2), ("Die Kinder", 5), ("Lukas und ich", 3),
            ("Dein Freund", 2), ("Lena und Mia", 5), ("Mein Vater", 2), ("Meine Mutter", 2), ("Die Studenten", 5), ("Frau Müller", 2),
            ("Du und Tim", 4), ("Herr Schmidt", 2), ("Unsere Nachbarn", 5)]
# (verbo, objeto, gênero do objeto m/f/n/pl, lugar, gênero do lugar m/f/n)
ACTIVITIES = [
    ("kaufen", "Brot", "n", "Bäckerei", "f"), ("trinken", "Kaffee", "m", "Café", "n"), ("essen", "Pizza", "f", "Restaurant", "n"), ("lesen", "Zeitung", "f", "Bibliothek", "f"),
    ("sehen", "Film", "m", "Kino", "n"), ("kaufen", "Obst", "n", "Supermarkt", "m"), ("kaufen", "Hemd", "n", "Stadt", "f"), ("sehen", "Bild", "n", "Museum", "n"),
    ("essen", "Eis", "n", "Park", "m"), ("kaufen", "Medikamente", "pl", "Apotheke", "f"), ("schreiben", "E-Mail", "f", "Büro", "n"), ("sehen", "Spiel", "n", "Stadion", "n"),
    ("trinken", "Tee", "m", "Hotel", "n"), ("lesen", "Buch", "n", "Garten", "m"), ("kaufen", "Kuchen", "m", "Konditorei", "f"), ("hören", "Konzert", "n", "Park", "m"),
    ("bestellen", "Salat", "m", "Restaurant", "n"), ("trinken", "Saft", "m", "Bar", "f"), ("kaufen", "Blumen", "pl", "Blumenladen", "m"), ("sehen", "Theaterstück", "n", "Theater", "n"),
    ("suchen", "Wörterbuch", "n", "Buchhandlung", "f"), ("bezahlen", "Rechnung", "f", "Restaurant", "n"), ("kaufen", "Milch", "f", "Supermarkt", "m"), ("besuchen", "Ausstellung", "f", "Museum", "n"),
    ("essen", "Brötchen", "n", "Café", "n"), ("machen", "Foto", "n", "Zoo", "m"), ("kochen", "Suppe", "f", "Küche", "f"), ("essen", "Salat", "m", "Kantine", "f"),
    ("lernen", "Lektion", "f", "Schule", "f"), ("kaufen", "Jacke", "f", "Einkaufszentrum", "n"), ("hören", "Musik", "f", "Wohnzimmer", "n"), ("lesen", "Speisekarte", "f", "Restaurant", "n"),
    ("kaufen", "Käse", "m", "Supermarkt", "m"), ("trinken", "Bier", "n", "Bar", "f"), ("sehen", "Tiere", "pl", "Zoo", "m"), ("kaufen", "Schuhe", "pl", "Einkaufszentrum", "n"),
    ("treffen", "Lehrer", "m", "Schule", "f"), ("spielen", "Spiel", "n", "Wohnzimmer", "n"), ("suchen", "Schlüssel", "m", "Büro", "n"), ("bestellen", "Kuchen", "m", "Café", "n"),
]

GUIDE = [
    ("Pronúncia para brasileiros", "w = v, v = f, z = ts, ei = ai, ie = i, eu/äu = oi, sch = x, sp/st no início = xp/xt. Umlauts: ä (é), ö (ê com lábios de o), ü (i com lábios de u). ß = ss."),
    ("Substantivos e artigos", "Todo substantivo começa com maiúscula. Três gêneros: der (masc.), die (fem.), das (neutro); plural: die. Aprenda cada palavra com o artigo."),
    ("Acusativo", "O objeto direto muda só no masculino: der → den, ein → einen, kein → keinen. Ex.: Ich sehe den Hund. Feminino (die), neutro (das) e plural (die) não mudam."),
    ("Ordem das palavras", "O verbo conjugado fica na 2ª posição: Ich gehe heute ins Kino → Heute gehe ich ins Kino. Infinitivos e particípios vão para o final."),
    ("sein e haben", "sein: bin, bist, ist, sind, seid, sind. haben: habe, hast, hat, haben, habt, haben. Idade usa sein: Ich bin zwanzig (Jahre alt)."),
    ("Presente", "Regular: ich lerne, du lernst, er lernt, wir lernen, ihr lernt, sie lernen. Alguns mudam a vogal com du/er: fahren → fährst, essen → isst, lesen → liest, sehen → sieht."),
    ("Perfekt (passado falado)", "haben/sein + particípio no final: Ich habe Pizza gegessen. Verbos de movimento (gehen, fahren, kommen, fliegen) usam sein: Ich bin nach Berlin gefahren."),
    ("Futuro e modais", "werden + infinitivo: Ich werde reisen. Modais (können, wollen, müssen, möchten) + infinitivo no final: Ich möchte Kaffee trinken."),
    ("Movimento × lugar", "Para onde? acusativo: in den Park, ins Kino, in die Stadt. Onde? dativo: im Park, im Kino, in der Stadt. Cidades e países: nach Berlin; casa: nach Hause / zu Hause."),
    ("Negação", "kein nega substantivos (Ich habe kein Auto, keinen Hund, keine Zeit); nicht nega o resto (Ich komme nicht)."),
    ("Falsos amigos", "Rat = conselho; Tante = tia; also = então; bekommen = receber; Gymnasium = colégio; Handy = celular; brav = bem-comportado."),
]
