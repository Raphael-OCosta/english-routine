"""Reading, Writing, Listening e Speaking do German Routine (A1–A2). Perguntas em português."""

L1, L2 = "A1", "A2"


def q(question, options, answer, why):
    return {"question": question, "options": options, "answer": answer, "why": why}


def t(id_, level, topic, title, text, translation, questions):
    return {"id": id_, "level": level, "topic": topic, "title": title, "text": text, "translation": translation, "questions": questions}


TEXTS = [
    t("de001", L1, "apresentação", "Ich heiße Lena",
      "Hallo! Ich heiße Lena und ich bin vierundzwanzig Jahre alt. Ich komme aus Österreich, aber ich wohne in Berlin. Ich bin Grafikdesignerin.\n\n"
      "Ich mag Musik und Fahrradfahren. Am Wochenende treffe ich meine Freunde und wir gehen ins Café. Freut mich!",
      "Oi! Meu nome é Lena e tenho vinte e quatro anos. Sou da Áustria, mas moro em Berlim. Sou designer gráfica.\n\n"
      "Gosto de música e de andar de bicicleta. No fim de semana encontro meus amigos e vamos ao café. Prazer!",
      [q("De onde Lena é?", ["Áustria", "Alemanha", "Suíça", "Brasil"], 0, "Ich komme aus Österreich."),
       q("Onde ela mora?", ["Berlim", "Viena", "Munique", "Hamburgo"], 0, "Ich wohne in Berlin."),
       q("O que faz no fim de semana?", ["Vai ao café com amigos", "Trabalha", "Viaja", "Estuda"], 0, "Wir gehen ins Café.")]),
    t("de002", L1, "rotina", "Mein Tag",
      "Ich stehe um sieben Uhr auf. Ich dusche und trinke einen Kaffee. Um acht Uhr nehme ich die U-Bahn.\n\n"
      "Ich arbeite von neun bis fünf. Am Abend koche ich und sehe eine Serie. Um elf Uhr gehe ich ins Bett.",
      "Levanto às sete. Tomo banho e bebo um café. Às oito pego o metrô.\n\n"
      "Trabalho das nove às cinco. À noite cozinho e assisto a uma série. Às onze vou para a cama.",
      [q("A que horas a pessoa se levanta?", ["Às 7h", "Às 8h", "Às 9h", "Às 6h"], 0, "Um sieben Uhr."),
       q("Como vai ao trabalho?", ["De metrô", "De ônibus", "A pé", "De carro"], 0, "Ich nehme die U-Bahn."),
       q("O que faz à noite?", ["Cozinha e vê uma série", "Vai ao cinema", "Estuda", "Corre"], 0, "Ich koche und sehe eine Serie.")]),
    t("de003", L1, "família", "Meine Familie",
      "Meine Familie ist klein. Wir sind vier: mein Vater, meine Mutter, meine Schwester und ich. Mein Vater ist Arzt und meine Mutter ist Lehrerin.\n\n"
      "Meine Schwester heißt Mia. Sie ist zwölf und spielt gern Fußball. Am Sonntag essen wir bei meiner Oma.",
      "Minha família é pequena. Somos quatro: meu pai, minha mãe, minha irmã e eu. Meu pai é médico e minha mãe é professora.\n\n"
      "Minha irmã se chama Mia. Tem doze anos e gosta de jogar futebol. No domingo comemos na casa da minha avó.",
      [q("Quantas pessoas há na família?", ["Quatro", "Três", "Cinco", "Seis"], 0, "Wir sind vier."),
       q("Qual é a profissão do pai?", ["Médico", "Professor", "Engenheiro", "Garçom"], 0, "Mein Vater ist Arzt."),
       q("Onde comem no domingo?", ["Na casa da avó", "Num restaurante", "Em casa", "No parque"], 0, "Bei meiner Oma.")]),
    t("de004", L1, "café", "Im Café",
      "Kellner: Guten Tag! Was möchten Sie?\n\nKundin: Einen Cappuccino und ein Stück Apfelkuchen, bitte.\n\n"
      "Kellner: Mit Sahne?\n\nKundin: Ja, gern. Was kostet das?\n\nKellner: Sechs Euro achtzig.",
      "Garçom: Boa tarde! O que a senhora deseja?\n\nCliente: Um cappuccino e um pedaço de torta de maçã, por favor.\n\n"
      "Garçom: Com chantili?\n\nCliente: Sim, por favor. Quanto custa?\n\nGarçom: Seis euros e oitenta.",
      [q("O que a cliente pede?", ["Cappuccino e torta de maçã", "Chá e bolo", "Café e pão", "Suco e sanduíche"], 0, "Einen Cappuccino und ein Stück Apfelkuchen."),
       q("Ela quer chantili?", ["Sim", "Não", "Não diz", "Só no café"], 0, "Ja, gern."),
       q("Quanto custa?", ["€6,80", "€8,60", "€6,18", "€5,80"], 0, "Sechs Euro achtzig.")]),
    t("de005", L1, "cidade", "Meine Straße",
      "Ich wohne in einer ruhigen Straße. Neben meinem Haus gibt es eine Bäckerei und einen Supermarkt.\n\n"
      "Gegenüber ist ein kleiner Park. Am Morgen kaufe ich Brötchen in der Bäckerei. Ich wohne gern hier.",
      "Moro numa rua tranquila. Ao lado da minha casa há uma padaria e um supermercado.\n\n"
      "Em frente há um pequeno parque. De manhã compro pãezinhos na padaria. Gosto de morar aqui.",
      [q("Como é a rua?", ["Tranquila", "Barulhenta", "Perigosa", "Muito longa"], 0, "Eine ruhige Straße."),
       q("O que há em frente?", ["Um parque", "Uma escola", "Um cinema", "Um banco"], 0, "Gegenüber ist ein kleiner Park."),
       q("O que compra de manhã?", ["Pãezinhos", "Leite", "Frutas", "Jornal"], 0, "Ich kaufe Brötchen.")]),
    t("de006", L1, "tempo", "Das Wetter",
      "Heute ist es in Hamburg kalt und es regnet. Ich nehme meinen Regenschirm.\n\n"
      "Morgen scheint die Sonne. Dann gehe ich mit meinem Hund in den Park. Im Sommer ist es warm und wir fahren an die Ostsee.",
      "Hoje em Hamburgo está frio e chove. Pego meu guarda-chuva.\n\n"
      "Amanhã vai fazer sol. Então vou com meu cachorro ao parque. No verão faz calor e vamos para o mar Báltico.",
      [q("Como está o tempo hoje?", ["Frio e chuva", "Sol e calor", "Neve", "Vento"], 0, "Es ist kalt und es regnet."),
       q("O que a pessoa faz amanhã?", ["Vai ao parque com o cachorro", "Vai à praia", "Fica em casa", "Vai ao cinema"], 0, "Ich gehe mit meinem Hund in den Park."),
       q("Para onde vão no verão?", ["Mar Báltico", "Montanhas", "Itália", "Berlim"], 0, "Wir fahren an die Ostsee.")]),
    t("de007", L1, "compras", "Auf dem Markt",
      "Am Samstag gehe ich mit meiner Mutter auf den Markt. Wir kaufen Obst und Gemüse: Äpfel, Tomaten und Kartoffeln.\n\n"
      "Der Käseverkäufer ist sehr nett. Ein Kilo Äpfel kostet drei Euro. Auf dem Markt ist alles frisch!",
      "No sábado vou à feira com minha mãe. Compramos frutas e verduras: maçãs, tomates e batatas.\n\n"
      "O vendedor de queijo é muito simpático. Um quilo de maçãs custa três euros. Na feira tudo é fresco!",
      [q("Com quem a pessoa vai à feira?", ["Com a mãe", "Com o pai", "Sozinha", "Com amigos"], 0, "Mit meiner Mutter."),
       q("Quanto custa um quilo de maçãs?", ["€3", "€2", "€4", "€1"], 0, "Drei Euro."),
       q("Como é o vendedor de queijo?", ["Simpático", "Antipático", "Calado", "Jovem"], 0, "Sehr nett.")]),
    t("de008", L1, "trabalho", "Mein Job",
      "Ich bin Kellner in einem Restaurant in Köln. Ich arbeite von Dienstag bis Sonntag. Am Montag habe ich frei.\n\n"
      "Die Arbeit ist anstrengend, aber meine Kollegen sind nett. Ich spreche mit vielen Touristen und lerne so Englisch.",
      "Sou garçom num restaurante em Colônia. Trabalho de terça a domingo. Na segunda estou de folga.\n\n"
      "O trabalho é cansativo, mas meus colegas são legais. Falo com muitos turistas e assim aprendo inglês.",
      [q("Qual é a profissão?", ["Garçom", "Cozinheiro", "Guia", "Professor"], 0, "Ich bin Kellner."),
       q("Qual é o dia de folga?", ["Segunda", "Domingo", "Sábado", "Terça"], 0, "Am Montag habe ich frei."),
       q("Que língua aprende?", ["Inglês", "Francês", "Espanhol", "Italiano"], 0, "Ich lerne so Englisch.")]),
    t("de009", L1, "comida", "Das Abendessen",
      "Heute Abend koche ich für meine Freunde. Ich mache Nudeln mit Tomatensoße und einen Salat. Zum Nachtisch kaufe ich ein Eis.\n\n"
      "Jonas bringt den Wein und Sara bringt das Brot. Wir essen um acht Uhr. Guten Appetit!",
      "Hoje à noite cozinho para meus amigos. Faço macarrão com molho de tomate e uma salada. De sobremesa compro um sorvete.\n\n"
      "Jonas traz o vinho e Sara traz o pão. Comemos às oito. Bom apetite!",
      [q("O que a pessoa cozinha?", ["Macarrão e salada", "Pizza", "Peixe", "Frango"], 0, "Nudeln mit Tomatensoße und einen Salat."),
       q("O que Jonas traz?", ["Vinho", "Pão", "Sorvete", "Água"], 0, "Jonas bringt den Wein."),
       q("A que horas comem?", ["Às 20h", "Às 19h", "Às 21h", "Às 18h"], 0, "Um acht Uhr.")]),
    t("de010", L1, "hobby", "Meine Freizeit",
      "In meiner Freizeit lese ich gern und fahre Fahrrad. Am Dienstag und Donnerstag gehe ich ins Fitnessstudio.\n\n"
      "Am Sonntag sehe ich Fußball mit meinem Vater. Ich sehe nicht gern fern, ich höre lieber Podcasts.",
      "No tempo livre gosto de ler e andar de bicicleta. Às terças e quintas vou à academia.\n\n"
      "No domingo vejo futebol com meu pai. Não gosto muito de TV, prefiro ouvir podcasts.",
      [q("Quando a pessoa vai à academia?", ["Terça e quinta", "Segunda e quarta", "Sábado", "Todos os dias"], 0, "Am Dienstag und Donnerstag."),
       q("Com quem vê futebol?", ["Com o pai", "Com amigos", "Sozinha", "Com a mãe"], 0, "Mit meinem Vater."),
       q("O que prefere à TV?", ["Podcasts", "Cinema", "Livros", "Rádio"], 0, "Ich höre lieber Podcasts.")]),
    t("de011", L2, "viagem", "Urlaub in Bayern",
      "Letzten Sommer bin ich mit meiner Freundin Julia nach Bayern gefahren. Wir haben München besucht und sind in den Alpen gewandert.\n\n"
      "Wir haben Brezeln und Weißwurst gegessen. Am letzten Tag hat es geregnet, deshalb sind wir ins Museum gegangen. Es war ein toller Urlaub.",
      "No verão passado fui para a Baviera com minha amiga Julia. Visitamos Munique e fizemos trilhas nos Alpes.\n\n"
      "Comemos pretzels e salsicha branca. No último dia choveu, por isso fomos ao museu. Foram férias ótimas.",
      [q("Com quem a pessoa viajou?", ["Com a amiga Julia", "Com a família", "Sozinha", "Com o namorado"], 0, "Mit meiner Freundin Julia."),
       q("O que fizeram nos Alpes?", ["Trilhas", "Esqui", "Compras", "Natação"], 0, "Wir sind in den Alpen gewandert."),
       q("Por que foram ao museu?", ["Choveu", "Estavam cansadas", "Era de graça", "Perderam o trem"], 0, "Es hat geregnet, deshalb…")]),
    t("de012", L2, "infância", "Als ich klein war",
      "Als ich klein war, habe ich in einem Dorf gewohnt. Ich bin zu Fuß in die Schule gegangen und habe nachmittags mit meinen Cousins gespielt.\n\n"
      "Im Winter gab es immer viel Schnee. Meine Oma hat jeden Sonntag einen Apfelkuchen gebacken. Heute wohne ich in der Stadt, aber ich denke oft an diese Zeit.",
      "Quando eu era pequeno, morava numa vila. Ia a pé para a escola e à tarde brincava com meus primos.\n\n"
      "No inverno sempre tinha muita neve. Minha avó assava uma torta de maçã todo domingo. Hoje moro na cidade, mas penso muito naquela época.",
      [q("Onde a pessoa morava?", ["Numa vila", "Na cidade", "Na praia", "No exterior"], 0, "In einem Dorf."),
       q("Como ia à escola?", ["A pé", "De ônibus", "De bicicleta", "De carro"], 0, "Zu Fuß."),
       q("O que a avó fazia aos domingos?", ["Torta de maçã", "Pão", "Sopa", "Sorvete"], 0, "Einen Apfelkuchen gebacken.")]),
    t("de013", L2, "saúde", "Beim Arzt",
      "Ärztin: Guten Tag, was fehlt Ihnen?\n\nPatient: Ich habe seit zwei Tagen Kopfschmerzen und ein bisschen Fieber.\n\n"
      "Ärztin: Haben Sie auch Husten?\n\nPatient: Ja, ein bisschen.\n\nÄrztin: Das ist eine Grippe. Sie müssen sich ausruhen, viel Wasser trinken und dieses Medikament dreimal am Tag nehmen.",
      "Médica: Boa tarde, o que o senhor tem?\n\nPaciente: Estou com dor de cabeça e um pouco de febre há dois dias.\n\n"
      "Médica: Também tem tosse?\n\nPaciente: Sim, um pouco.\n\nMédica: É uma gripe. O senhor precisa descansar, beber muita água e tomar este remédio três vezes ao dia.",
      [q("Há quanto tempo o paciente está doente?", ["Dois dias", "Uma semana", "Um dia", "Três dias"], 0, "Seit zwei Tagen."),
       q("Qual é o diagnóstico?", ["Gripe", "Alergia", "Covid", "Enxaqueca"], 0, "Das ist eine Grippe."),
       q("Quantas vezes por dia deve tomar o remédio?", ["Três", "Duas", "Uma", "Quatro"], 0, "Dreimal am Tag.")]),
    t("de014", L2, "trabalho", "Ein neuer Job",
      "Letzten Monat hat Tobias einen neuen Job in einem Reisebüro angefangen. Vorher hat er in einer Bank gearbeitet, aber er war nicht glücklich.\n\n"
      "Jetzt plant er Reisen für Kunden und spricht oft Englisch und Spanisch. Er verdient weniger, aber er ist viel zufriedener. In fünf Jahren will er ein eigenes Reisebüro öffnen.",
      "No mês passado Tobias começou um novo emprego numa agência de viagens. Antes trabalhava num banco, mas não era feliz.\n\n"
      "Agora planeja viagens para clientes e fala com frequência inglês e espanhol. Ganha menos, mas está muito mais satisfeito. Em cinco anos quer abrir sua própria agência.",
      [q("Onde Tobias trabalhava antes?", ["Num banco", "Numa escola", "Num hotel", "Num restaurante"], 0, "In einer Bank."),
       q("Como ele se sente agora?", ["Mais satisfeito", "Mais cansado", "Preocupado", "Igual"], 0, "Viel zufriedener."),
       q("Qual é o plano dele?", ["Abrir a própria agência", "Voltar ao banco", "Morar fora", "Estudar"], 0, "Ein eigenes Reisebüro öffnen.")]),
    t("de015", L2, "cidade", "Berlin oder München?",
      "Berlin und München sind sehr verschieden. Berlin ist groß, jung und kreativ. Es gibt viele Museen, Clubs und Parks.\n\n"
      "München ist kleiner, ruhiger und teurer. Die Berge sind nah und im Oktober gibt es das Oktoberfest. Ich finde Berlin spannender, aber München ist sauberer.",
      "Berlim e Munique são muito diferentes. Berlim é grande, jovem e criativa. Há muitos museus, clubes e parques.\n\n"
      "Munique é menor, mais tranquila e mais cara. As montanhas ficam perto e em outubro há a Oktoberfest. Acho Berlim mais emocionante, mas Munique é mais limpa.",
      [q("Qual cidade é mais cara?", ["Munique", "Berlim", "As duas", "Nenhuma"], 0, "München ist … teurer."),
       q("O que há em Munique em outubro?", ["Oktoberfest", "Carnaval", "Um festival de cinema", "Uma maratona"], 0, "Das Oktoberfest."),
       q("O que a pessoa acha de Munique?", ["Mais limpa", "Mais emocionante", "Maior", "Mais jovem"], 0, "München ist sauberer.")]),
    t("de016", L2, "tecnologia", "Das Handy",
      "Ich benutze mein Handy den ganzen Tag: zum Arbeiten, für Nachrichten und um mit meiner Familie zu sprechen.\n\n"
      "Aber am Abend lege ich es in ein anderes Zimmer. Vor dem Schlafen lese ich ein Buch aus Papier. So schlafe ich besser und bin morgens weniger müde.",
      "Uso o celular o dia todo: para trabalhar, para notícias e para falar com minha família.\n\n"
      "Mas à noite deixo-o em outro cômodo. Antes de dormir leio um livro de papel. Assim durmo melhor e fico menos cansado de manhã.",
      [q("Onde a pessoa deixa o celular à noite?", ["Em outro cômodo", "Na cama", "No trabalho", "No carro"], 0, "In ein anderes Zimmer."),
       q("O que lê antes de dormir?", ["Um livro de papel", "Notícias", "Mensagens", "Revistas no celular"], 0, "Ein Buch aus Papier."),
       q("Qual é o resultado?", ["Dorme melhor", "Trabalha mais", "Acorda mais cedo", "Lê mais rápido"], 0, "So schlafe ich besser.")]),
    t("de017", L2, "festa", "Die Überraschungsparty",
      "Letzten Samstag haben wir eine Überraschungsparty für Jonas gemacht. Wir haben alles bei Clara vorbereitet.\n\n"
      "Als Jonas gekommen ist, haben wir „Alles Gute!“ gerufen. Er war sehr überrascht und ein bisschen gerührt. Wir haben Kuchen gegessen und bis Mitternacht getanzt.",
      "No sábado passado fizemos uma festa surpresa para o Jonas. Preparamos tudo na casa da Clara.\n\n"
      "Quando Jonas chegou, gritamos “Parabéns!”. Ele ficou muito surpreso e um pouco emocionado. Comemos bolo e dançamos até a meia-noite.",
      [q("Onde foi a festa?", ["Na casa da Clara", "Na casa do Jonas", "Num restaurante", "Num bar"], 0, "Bei Clara."),
       q("Como Jonas reagiu?", ["Surpreso e emocionado", "Bravo", "Indiferente", "Cansado"], 0, "Sehr überrascht und ein bisschen gerührt."),
       q("Até que horas dançaram?", ["Meia-noite", "Dez da noite", "Duas da manhã", "Onze"], 0, "Bis Mitternacht.")]),
    t("de018", L2, "estudos", "Warum ich Deutsch lerne",
      "Ich lerne seit einem Jahr Deutsch. Ich möchte in Deutschland studieren, weil die Universitäten sehr gut sind.\n\n"
      "Jeden Tag übe ich zwanzig Minuten und ich sehe deutsche Serien mit Untertiteln. Nächstes Jahr mache ich die B1-Prüfung.",
      "Estudo alemão há um ano. Quero fazer faculdade na Alemanha, porque as universidades são muito boas.\n\n"
      "Todo dia pratico vinte minutos e assisto a séries alemãs com legendas. No ano que vem faço a prova B1.",
      [q("Há quanto tempo a pessoa estuda?", ["Um ano", "Seis meses", "Dois anos", "Um mês"], 0, "Seit einem Jahr."),
       q("Por que quer estudar na Alemanha?", ["As universidades são boas", "A família mora lá", "É barato", "Pelo clima"], 0, "Weil die Universitäten sehr gut sind."),
       q("Quanto tempo pratica por dia?", ["Vinte minutos", "Uma hora", "Dez minutos", "Meia hora"], 0, "Zwanzig Minuten.")]),
    t("de019", L2, "transporte", "Der Zug hat Verspätung",
      "Heute hat mein Zug eine Stunde Verspätung. Ich habe meinen Chef angerufen und gesagt, dass ich später komme.\n\n"
      "In Deutschland sind Züge oft pünktlich, aber nicht immer. Ich habe auf dem Bahnsteig einen Kaffee getrunken und ein Buch gelesen.",
      "Hoje meu trem está uma hora atrasado. Liguei para meu chefe e disse que chego mais tarde.\n\n"
      "Na Alemanha os trens muitas vezes são pontuais, mas nem sempre. Na plataforma bebi um café e li um livro.",
      [q("Quanto o trem atrasou?", ["Uma hora", "Meia hora", "Dez minutos", "Duas horas"], 0, "Eine Stunde Verspätung."),
       q("O que a pessoa fez primeiro?", ["Ligou para o chefe", "Pegou um táxi", "Voltou para casa", "Foi a pé"], 0, "Ich habe meinen Chef angerufen."),
       q("O que fez na plataforma?", ["Bebeu café e leu", "Dormiu", "Trabalhou no computador", "Comeu um sanduíche"], 0, "Einen Kaffee getrunken und ein Buch gelesen.")]),
    t("de020", L2, "mensagem", "Eine Nachricht an Paula",
      "Hallo Paula! Leider kann ich heute Abend nicht ins Kino kommen: Ich muss noch eine wichtige Arbeit fertig machen. Tut mir leid!\n\n"
      "Können wir am Samstagnachmittag gehen? Dann läuft auch der neue Film mit Daniel Brühl. Sag mir Bescheid. Liebe Grüße, Nina",
      "Oi Paula! Infelizmente não posso ir ao cinema hoje à noite: ainda preciso terminar um trabalho importante. Desculpe!\n\n"
      "Podemos ir sábado à tarde? Aí também passa o novo filme com Daniel Brühl. Me avise. Um abraço, Nina",
      [q("Por que Nina não pode ir?", ["Precisa terminar um trabalho", "Está doente", "Vai viajar", "Não tem dinheiro"], 0, "Ich muss noch eine wichtige Arbeit fertig machen."),
       q("Que dia ela propõe?", ["Sábado à tarde", "Domingo de manhã", "Amanhã à noite", "Sexta"], 0, "Am Samstagnachmittag."),
       q("Qual é o objetivo da mensagem?", ["Remarcar o cinema", "Convidar para uma festa", "Pedir desculpa por um atraso", "Recomendar um livro"], 0,
         "Ela cancela hoje e propõe sábado.")]),
]

PROMPTS = [
    {"id": "dw01", "level": L1, "topic": "apresentação", "prompt": "Stell dich vor.", "prompt_pt": "Apresente-se: nome, idade, cidade, trabalho ou estudos e gostos.", "units": 50, "lines": 4},
    {"id": "dw02", "level": L1, "topic": "rotina", "prompt": "Beschreib einen normalen Tag.", "prompt_pt": "Descreva sua rotina (lembre: verbo na 2ª posição).", "units": 50, "lines": 4},
    {"id": "dw03", "level": L1, "topic": "família", "prompt": "Erzähl von deiner Familie.", "prompt_pt": "Apresente sua família (mein Vater, meine Mutter…).", "units": 50, "lines": 4},
    {"id": "dw04", "level": L1, "topic": "comida", "prompt": "Was isst du gern?", "prompt_pt": "O que você gosta de comer? Use gern / nicht gern.", "units": 50, "lines": 4},
    {"id": "dw05", "level": L1, "topic": "passado", "prompt": "Was hast du letztes Wochenende gemacht?", "prompt_pt": "Conte seu último fim de semana (Perfekt).", "units": 50, "lines": 4},
    {"id": "dw06", "level": L1, "topic": "música", "prompt": "Dein Lieblingssänger oder deine Lieblingsserie.", "prompt_pt": "Fale do seu cantor ou série favorita.", "units": 50, "lines": 4},
    {"id": "dw07", "level": L1, "topic": "cidade", "prompt": "Beschreib dein Viertel.", "prompt_pt": "Descreva seu bairro (es gibt…).", "units": 50, "lines": 4},
    {"id": "dw08", "level": L1, "topic": "futuro", "prompt": "Was machst du in den Ferien?", "prompt_pt": "Planos para as férias (ich werde…, ich möchte…).", "units": 50, "lines": 4},
    {"id": "dw09", "level": L2, "topic": "estudos", "prompt": "Warum lernst du Deutsch?", "prompt_pt": "Por que você aprende alemão? (weil…)", "units": 100, "lines": 6},
    {"id": "dw10", "level": L2, "topic": "viagem", "prompt": "Erzähl von einer unvergesslichen Reise.", "prompt_pt": "Conte uma viagem inesquecível.", "units": 100, "lines": 6},
    {"id": "dw11", "level": L2, "topic": "infância", "prompt": "Wie war deine Kindheit?", "prompt_pt": "Como foi sua infância?", "units": 100, "lines": 6},
    {"id": "dw12", "level": L2, "topic": "saúde", "prompt": "Was machst du für deine Gesundheit?", "prompt_pt": "O que você faz pela saúde?", "units": 100, "lines": 6},
    {"id": "dw13", "level": L2, "topic": "consumo", "prompt": "Vor- und Nachteile von Online-Shopping.", "prompt_pt": "Vantagens e desvantagens de comprar on-line.", "units": 100, "lines": 6},
    {"id": "dw14", "level": L2, "topic": "mensagens", "prompt": "Schreib einem Freund und verschieb einen Termin.", "prompt_pt": "Mensagem a um amigo mudando um encontro.", "units": 100, "lines": 6},
    {"id": "dw15", "level": L2, "topic": "hobby", "prompt": "Erzähl von deinem Hobby.", "prompt_pt": "Apresente seu hobby.", "units": 100, "lines": 6},
    {"id": "dw16", "level": L2, "topic": "futuro", "prompt": "Wie siehst du dich in zehn Jahren?", "prompt_pt": "Como você se imagina daqui a dez anos?", "units": 100, "lines": 6},
]

ROLEPLAY = "1. Was ist deine Hauptidee? 2. Kannst du ein Beispiel geben? 3. Warum denkst du das?"
