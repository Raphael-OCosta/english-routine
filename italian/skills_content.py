"""Reading, Writing, Listening e Speaking do Italian Routine (A1–A2). Perguntas em português."""

L1, L2 = "A1", "A2"


def q(question, options, answer, why):
    return {"question": question, "options": options, "answer": answer, "why": why}


def t(id_, level, topic, title, text, translation, questions):
    return {"id": id_, "level": level, "topic": topic, "title": title, "text": text, "translation": translation, "questions": questions}


TEXTS = [
    t("it001", L1, "apresentação", "Mi chiamo Giulia",
      "Ciao! Mi chiamo Giulia e ho ventitré anni. Sono italiana, abito a Bologna. Studio medicina all'università.\n\n"
      "Mi piace la musica e mi piace cucinare. Il fine settimana esco con i miei amici e andiamo in pizzeria. Piacere!",
      "Oi! Meu nome é Giulia e tenho vinte e três anos. Sou italiana e moro em Bolonha. Estudo medicina na universidade.\n\n"
      "Gosto de música e de cozinhar. No fim de semana saio com meus amigos e vamos à pizzaria. Prazer!",
      [q("Onde Giulia mora?", ["Bolonha", "Roma", "Milão", "Nápoles"], 0, "Abito a Bologna."),
       q("O que ela estuda?", ["Medicina", "Música", "Direito", "Arquitetura"], 0, "Studio medicina."),
       q("Aonde vai no fim de semana?", ["À pizzaria", "Ao cinema", "À praia", "Ao museu"], 0, "Andiamo in pizzeria.")]),
    t("it002", L1, "rotina", "La mia giornata",
      "Mi alzo alle sette. Faccio la doccia e bevo un caffè con un cornetto. Alle otto prendo l'autobus.\n\n"
      "Lavoro dalle nove alle diciassette. La sera preparo la cena e guardo una serie. Vado a letto alle undici.",
      "Levanto-me às sete. Tomo banho e bebo um café com um croissant. Às oito pego o ônibus.\n\n"
      "Trabalho das nove às dezessete. À noite preparo o jantar e assisto a uma série. Vou dormir às onze.",
      [q("A que horas a pessoa se levanta?", ["Às 7h", "Às 8h", "Às 9h", "Às 6h"], 0, "Mi alzo alle sette."),
       q("Como vai ao trabalho?", ["De ônibus", "De metrô", "A pé", "De carro"], 0, "Prendo l'autobus."),
       q("A que horas vai dormir?", ["Às 23h", "Às 22h", "À meia-noite", "Às 21h"], 0, "Vado a letto alle undici.")]),
    t("it003", L1, "família", "La mia famiglia",
      "La mia famiglia è grande. Ho due fratelli e una sorella. Mio padre è ingegnere e mia madre è insegnante.\n\n"
      "Mia sorella si chiama Sara. Ha quindici anni e ama il calcio. La domenica pranziamo tutti insieme dai nonni.",
      "Minha família é grande. Tenho dois irmãos e uma irmã. Meu pai é engenheiro e minha mãe é professora.\n\n"
      "Minha irmã se chama Sara. Tem quinze anos e ama futebol. Aos domingos almoçamos todos juntos na casa dos avós.",
      [q("Quantos irmãos homens a pessoa tem?", ["Dois", "Um", "Três", "Nenhum"], 0, "Ho due fratelli."),
       q("Do que Sara gosta?", ["Futebol", "Música", "Tênis", "Dança"], 0, "Ama il calcio."),
       q("Onde almoçam aos domingos?", ["Na casa dos avós", "Num restaurante", "Em casa", "Na praia"], 0, "Dai nonni.")]),
    t("it004", L1, "café", "Al bar",
      "Barista: Buongiorno! Cosa prende?\n\nCliente: Un cappuccino e un cornetto, per favore.\n\n"
      "Barista: Al banco o al tavolo?\n\nCliente: Al banco. Quanto costa?\n\nBarista: Tre euro e cinquanta.",
      "Barista: Bom dia! O que vai querer?\n\nCliente: Um cappuccino e um croissant, por favor.\n\n"
      "Barista: No balcão ou na mesa?\n\nCliente: No balcão. Quanto custa?\n\nBarista: Três euros e cinquenta.",
      [q("O que o cliente pede?", ["Cappuccino e croissant", "Café e bolo", "Chá e sanduíche", "Suco e torrada"], 0, "Un cappuccino e un cornetto."),
       q("Onde ele vai consumir?", ["No balcão", "Na mesa", "Para viagem", "Em casa"], 0, "Al banco."),
       q("Quanto custa?", ["€3,50", "€3,00", "€5,30", "€2,50"], 0, "Tre euro e cinquanta.")]),
    t("it005", L1, "cidade", "Il mio quartiere",
      "Abito in un quartiere tranquillo. Vicino a casa mia c'è un parco, un supermercato e una farmacia.\n\n"
      "C'è anche una piccola piazza con un bar. La mattina compro il pane in panetteria. Mi piace molto il mio quartiere.",
      "Moro num bairro tranquilo. Perto da minha casa há um parque, um supermercado e uma farmácia.\n\n"
      "Há também uma pracinha com um bar. De manhã compro pão na padaria. Gosto muito do meu bairro.",
      [q("Como é o bairro?", ["Tranquilo", "Barulhento", "Perigoso", "Muito grande"], 0, "Un quartiere tranquillo."),
       q("O que há na praça?", ["Um bar", "Uma escola", "Um cinema", "Um banco"], 0, "Una piccola piazza con un bar."),
       q("Onde compra pão?", ["Na padaria", "No supermercado", "No bar", "Na farmácia"], 0, "In panetteria.")]),
    t("it006", L1, "tempo", "Che tempo fa?",
      "Oggi a Milano fa freddo e piove. Prendo l'ombrello e la giacca.\n\n"
      "Domani, invece, ci sarà il sole. Voglio andare al parco con il mio cane. In estate fa molto caldo e andiamo al mare.",
      "Hoje em Milão está frio e chove. Pego o guarda-chuva e a jaqueta.\n\n"
      "Amanhã, ao contrário, vai fazer sol. Quero ir ao parque com meu cachorro. No verão faz muito calor e vamos à praia.",
      [q("Como está o tempo hoje?", ["Frio e chuva", "Sol e calor", "Neve", "Vento"], 0, "Fa freddo e piove."),
       q("O que a pessoa quer fazer amanhã?", ["Ir ao parque com o cachorro", "Ir à praia", "Ficar em casa", "Ir ao cinema"], 0, "Andare al parco con il mio cane."),
       q("O que fazem no verão?", ["Vão à praia", "Vão à montanha", "Ficam em casa", "Viajam para o exterior"], 0, "Andiamo al mare.")]),
    t("it007", L1, "compras", "Al mercato",
      "Il sabato vado al mercato con mia madre. Compriamo frutta e verdura fresca: mele, pomodori e insalata.\n\n"
      "Il signore del formaggio è molto simpatico. Un chilo di mele costa due euro. Al mercato è tutto più buono!",
      "Aos sábados vou ao mercado com minha mãe. Compramos frutas e verduras frescas: maçãs, tomates e alface.\n\n"
      "O senhor do queijo é muito simpático. Um quilo de maçãs custa dois euros. No mercado tudo é mais gostoso!",
      [q("Com quem a pessoa vai ao mercado?", ["Com a mãe", "Com o pai", "Sozinha", "Com amigos"], 0, "Con mia madre."),
       q("Quanto custa um quilo de maçãs?", ["€2", "€1", "€3", "€5"], 0, "Costa due euro."),
       q("Como é o senhor do queijo?", ["Simpático", "Antipático", "Calado", "Jovem"], 0, "Molto simpatico.")]),
    t("it008", L1, "trabalho", "Il mio lavoro",
      "Sono cameriere in un ristorante a Firenze. Lavoro dal martedì alla domenica. Il lunedì è il mio giorno libero.\n\n"
      "Il lavoro è faticoso, ma i colleghi sono simpatici. Parlo con molti turisti e così pratico l'inglese.",
      "Sou garçom num restaurante em Florença. Trabalho de terça a domingo. Segunda é meu dia de folga.\n\n"
      "O trabalho é cansativo, mas os colegas são simpáticos. Falo com muitos turistas e assim pratico o inglês.",
      [q("Qual é a profissão?", ["Garçom", "Cozinheiro", "Guia", "Professor"], 0, "Sono cameriere."),
       q("Qual é o dia de folga?", ["Segunda", "Domingo", "Sábado", "Terça"], 0, "Il lunedì è il mio giorno libero."),
       q("Que língua pratica?", ["Inglês", "Francês", "Espanhol", "Alemão"], 0, "Pratico l'inglese.")]),
    t("it009", L1, "comida", "La cena",
      "Stasera preparo la cena per i miei amici. Faccio la pasta al pomodoro e un'insalata. Per dolce, compro un tiramisù.\n\n"
      "Marco porta il vino e Anna porta il pane. Mangiamo alle otto. Buon appetito!",
      "Hoje à noite preparo o jantar para meus amigos. Faço macarrão ao sugo e uma salada. De sobremesa, compro um tiramisù.\n\n"
      "Marco traz o vinho e Anna traz o pão. Comemos às oito. Bom apetite!",
      [q("O que a pessoa cozinha?", ["Macarrão ao sugo e salada", "Pizza", "Peixe", "Frango"], 0, "La pasta al pomodoro e un'insalata."),
       q("O que Marco traz?", ["Vinho", "Pão", "Sobremesa", "Água"], 0, "Marco porta il vino."),
       q("A que horas comem?", ["Às 20h", "Às 19h", "Às 21h", "Às 18h"], 0, "Mangiamo alle otto.")]),
    t("it010", L1, "hobby", "Il mio tempo libero",
      "Nel tempo libero mi piace leggere e andare in bicicletta. Il martedì e il giovedì vado in palestra.\n\n"
      "La domenica guardo la partita con mio padre. Non mi piace molto la televisione, preferisco ascoltare la radio.",
      "No tempo livre gosto de ler e andar de bicicleta. Às terças e quintas vou à academia.\n\n"
      "Aos domingos assisto ao jogo com meu pai. Não gosto muito de televisão, prefiro escutar rádio.",
      [q("Quando a pessoa vai à academia?", ["Terça e quinta", "Segunda e quarta", "Sábado", "Todos os dias"], 0, "Il martedì e il giovedì."),
       q("Com quem assiste ao jogo?", ["Com o pai", "Com amigos", "Sozinha", "Com a mãe"], 0, "Con mio padre."),
       q("O que prefere à televisão?", ["Rádio", "Cinema", "Internet", "Livros"], 0, "Preferisco ascoltare la radio.")]),
    t("it011", L2, "viagem", "Una vacanza in Sicilia",
      "L'estate scorsa sono andata in Sicilia con la mia amica Laura. Abbiamo visitato Palermo e Taormina e abbiamo fatto il bagno nel mare.\n\n"
      "Abbiamo mangiato gli arancini e i cannoli: buonissimi! L'ultimo giorno ha piovuto, ma siamo andate al museo. È stata una vacanza fantastica.",
      "No verão passado fui para a Sicília com minha amiga Laura. Visitamos Palermo e Taormina e tomamos banho de mar.\n\n"
      "Comemos arancini e cannoli: deliciosos! No último dia choveu, mas fomos ao museu. Foram férias fantásticas.",
      [q("Com quem a pessoa viajou?", ["Com a amiga Laura", "Com a família", "Sozinha", "Com o namorado"], 0, "Con la mia amica Laura."),
       q("O que fizeram no último dia?", ["Foram ao museu", "Foram à praia", "Voltaram para casa", "Ficaram no hotel"], 0, "Siamo andate al museo."),
       q("Por que mudaram o plano no último dia?", ["Choveu", "Estavam cansadas", "Perderam o trem", "Ficaram doentes"], 0, "Ha piovuto.")]),
    t("it012", L2, "infância", "Quando ero piccolo",
      "Quando ero piccolo abitavo in un paesino in montagna. Andavo a scuola a piedi e il pomeriggio giocavo a calcio con i miei cugini.\n\n"
      "D'inverno c'era sempre la neve. Mia nonna faceva una torta di mele ogni domenica. Adesso abito in città, ma ricordo quegli anni con nostalgia.",
      "Quando eu era pequeno morava numa vilazinha na montanha. Ia à escola a pé e à tarde jogava futebol com meus primos.\n\n"
      "No inverno sempre tinha neve. Minha avó fazia uma torta de maçã todo domingo. Agora moro na cidade, mas lembro desses anos com saudade.",
      [q("Onde a pessoa morava?", ["Numa vila na montanha", "Na cidade", "Na praia", "No exterior"], 0, "Un paesino in montagna."),
       q("Como ia à escola?", ["A pé", "De ônibus", "De bicicleta", "De carro"], 0, "Andavo a scuola a piedi."),
       q("O que a avó fazia aos domingos?", ["Torta de maçã", "Pizza", "Macarrão", "Sorvete"], 0, "Faceva una torta di mele.")]),
    t("it013", L2, "saúde", "Dal medico",
      "Medico: Buongiorno, cosa c'è?\n\nPaziente: Ho mal di testa e un po' di febbre da due giorni.\n\n"
      "Medico: Ha anche la tosse?\n\nPaziente: Sì, un po'.\n\nMedico: È un'influenza. Deve riposare, bere molta acqua e prendere questa medicina tre volte al giorno.",
      "Médico: Bom dia, o que houve?\n\nPaciente: Estou com dor de cabeça e um pouco de febre há dois dias.\n\n"
      "Médico: Também tem tosse?\n\nPaciente: Sim, um pouco.\n\nMédico: É uma gripe. Precisa descansar, beber muita água e tomar este remédio três vezes ao dia.",
      [q("Há quanto tempo o paciente está doente?", ["Dois dias", "Uma semana", "Um dia", "Três dias"], 0, "Da due giorni."),
       q("Qual é o diagnóstico?", ["Gripe", "Alergia", "Covid", "Enxaqueca"], 0, "È un'influenza."),
       q("Quantas vezes por dia deve tomar o remédio?", ["Três", "Duas", "Uma", "Quatro"], 0, "Tre volte al giorno.")]),
    t("it014", L2, "trabalho", "Un nuovo lavoro",
      "Il mese scorso Paolo ha cominciato un nuovo lavoro in un'agenzia di viaggi. Prima lavorava in banca, ma non era felice.\n\n"
      "Adesso organizza viaggi per i clienti e parla spesso inglese e spagnolo. Guadagna meno, ma è molto più contento. Vuole aprire la sua agenzia tra cinque anni.",
      "No mês passado Paolo começou um novo emprego numa agência de viagens. Antes trabalhava num banco, mas não era feliz.\n\n"
      "Agora organiza viagens para os clientes e fala com frequência inglês e espanhol. Ganha menos, mas está muito mais contente. Quer abrir sua agência em cinco anos.",
      [q("Onde Paolo trabalhava antes?", ["Num banco", "Numa escola", "Num hotel", "Num restaurante"], 0, "Prima lavorava in banca."),
       q("Como ele se sente agora?", ["Mais contente", "Mais cansado", "Preocupado", "Igual"], 0, "È molto più contento."),
       q("Qual é o plano dele?", ["Abrir a própria agência", "Voltar ao banco", "Morar fora", "Estudar"], 0, "Vuole aprire la sua agenzia.")]),
    t("it015", L2, "cidade", "Roma o Milano?",
      "Roma e Milano sono due città molto diverse. Roma è più antica e ha tanti monumenti: il Colosseo, la Fontana di Trevi, il Pantheon.\n\n"
      "Milano è più moderna ed è la città della moda e del lavoro. A Roma la vita è più lenta; a Milano tutti corrono. Io preferisco Roma, perché amo la storia.",
      "Roma e Milão são duas cidades muito diferentes. Roma é mais antiga e tem muitos monumentos: o Coliseu, a Fontana di Trevi, o Panteão.\n\n"
      "Milão é mais moderna e é a cidade da moda e do trabalho. Em Roma a vida é mais lenta; em Milão todos correm. Eu prefiro Roma, porque amo história.",
      [q("Qual cidade é mais moderna?", ["Milão", "Roma", "As duas", "Nenhuma"], 0, "Milano è più moderna."),
       q("Como é a vida em Roma?", ["Mais lenta", "Mais rápida", "Mais cara", "Mais barata"], 0, "La vita è più lenta."),
       q("Por que a pessoa prefere Roma?", ["Ama história", "É mais barata", "Tem mais trabalho", "Tem praia"], 0, "Perché amo la storia.")]),
    t("it016", L2, "tecnologia", "Il telefono",
      "Uso il telefono tutto il giorno: per lavorare, per leggere le notizie e per parlare con la famiglia.\n\n"
      "Però la sera lo lascio in un'altra stanza. Prima di dormire leggo un libro di carta. Così dormo meglio e la mattina sono meno stanco.",
      "Uso o telefone o dia todo: para trabalhar, ler notícias e falar com a família.\n\n"
      "Porém, à noite o deixo em outro cômodo. Antes de dormir leio um livro de papel. Assim durmo melhor e de manhã fico menos cansado.",
      [q("Onde a pessoa deixa o telefone à noite?", ["Em outro cômodo", "Na cama", "No trabalho", "Na cozinha da vizinha"], 0, "In un'altra stanza."),
       q("O que lê antes de dormir?", ["Um livro de papel", "Notícias", "Mensagens", "Revistas no celular"], 0, "Un libro di carta."),
       q("Qual é o resultado?", ["Dorme melhor", "Trabalha mais", "Acorda mais cedo", "Lê mais rápido"], 0, "Dormo meglio.")]),
    t("it017", L2, "festa", "Il compleanno di Luca",
      "Sabato scorso abbiamo fatto una festa a sorpresa per il compleanno di Luca. Abbiamo preparato tutto a casa di Chiara.\n\n"
      "Quando Luca è entrato, abbiamo gridato «Auguri!». Era molto sorpreso e un po' emozionato. Abbiamo mangiato la torta e ballato fino a mezzanotte.",
      "No sábado passado fizemos uma festa surpresa para o aniversário do Luca. Preparamos tudo na casa da Chiara.\n\n"
      "Quando Luca entrou, gritamos «Parabéns!». Ele ficou muito surpreso e um pouco emocionado. Comemos o bolo e dançamos até a meia-noite.",
      [q("Onde foi a festa?", ["Na casa da Chiara", "Na casa do Luca", "Num restaurante", "Num bar"], 0, "A casa di Chiara."),
       q("Como Luca reagiu?", ["Surpreso e emocionado", "Bravo", "Indiferente", "Cansado"], 0, "Era molto sorpreso e un po' emozionato."),
       q("Até que horas dançaram?", ["Meia-noite", "Dez da noite", "Duas da manhã", "Onze"], 0, "Fino a mezzanotte.")]),
    t("it018", L2, "estudos", "Perché studio l'italiano",
      "Studio l'italiano da un anno. Mio nonno era di Napoli e voglio conoscere meglio la sua storia.\n\n"
      "Ogni giorno faccio esercizi per venti minuti e guardo film italiani con i sottotitoli. L'anno prossimo andrò in Italia per la prima volta.",
      "Estudo italiano há um ano. Meu avô era de Nápoles e quero conhecer melhor a história dele.\n\n"
      "Todo dia faço exercícios por vinte minutos e assisto a filmes italianos com legendas. No ano que vem irei à Itália pela primeira vez.",
      [q("Há quanto tempo a pessoa estuda?", ["Um ano", "Seis meses", "Dois anos", "Um mês"], 0, "Da un anno."),
       q("De onde era o avô?", ["Nápoles", "Roma", "Milão", "Veneza"], 0, "Era di Napoli."),
       q("Quanto tempo estuda por dia?", ["Vinte minutos", "Uma hora", "Dez minutos", "Meia hora"], 0, "Per venti minuti.")]),
    t("it019", L2, "transporte", "Lo sciopero",
      "Oggi c'è lo sciopero dei treni e non posso andare in ufficio. Ho chiamato il mio capo e lavoro da casa.\n\n"
      "In Italia gli scioperi sono abbastanza frequenti, ma di solito sono annunciati prima. Domani, per fortuna, i treni funzioneranno normalmente.",
      "Hoje há greve dos trens e não posso ir ao escritório. Liguei para meu chefe e trabalho de casa.\n\n"
      "Na Itália as greves são bastante frequentes, mas normalmente são anunciadas antes. Amanhã, por sorte, os trens funcionarão normalmente.",
      [q("Por que a pessoa não vai ao escritório?", ["Greve dos trens", "Está doente", "É feriado", "Choveu muito"], 0, "C'è lo sciopero dei treni."),
       q("O que ela fez?", ["Trabalha de casa", "Pegou um táxi", "Faltou", "Foi a pé"], 0, "Lavoro da casa."),
       q("Como serão os trens amanhã?", ["Normais", "Em greve", "Atrasados", "Mais caros"], 0, "Funzioneranno normalmente.")]),
    t("it020", L2, "mensagem", "Un messaggio a Marta",
      "Ciao Marta! Purtroppo stasera non posso venire al cinema: devo finire un lavoro urgente. Mi dispiace tanto!\n\n"
      "Possiamo andare sabato pomeriggio? C'è anche il nuovo film di Sorrentino. Fammi sapere. Un abbraccio, Elena.",
      "Oi Marta! Infelizmente hoje à noite não posso ir ao cinema: preciso terminar um trabalho urgente. Sinto muito!\n\n"
      "Podemos ir sábado à tarde? Tem também o novo filme do Sorrentino. Me avise. Um abraço, Elena.",
      [q("Por que Elena não pode ir?", ["Precisa terminar um trabalho", "Está doente", "Vai viajar", "Não tem dinheiro"], 0, "Devo finire un lavoro urgente."),
       q("Que dia ela propõe?", ["Sábado à tarde", "Domingo de manhã", "Amanhã à noite", "Sexta"], 0, "Sabato pomeriggio."),
       q("Qual é o objetivo da mensagem?", ["Remarcar o cinema", "Convidar para uma festa", "Pedir desculpa por um atraso", "Recomendar um livro"], 0,
         "Ela cancela hoje e propõe sábado.")]),
]

PROMPTS = [
    {"id": "iw01", "level": L1, "topic": "apresentação", "prompt": "Presentati.", "prompt_pt": "Apresente-se: nome, idade, cidade, trabalho ou estudos e gostos.", "units": 50, "lines": 4},
    {"id": "iw02", "level": L1, "topic": "rotina", "prompt": "Descrivi una giornata normale.", "prompt_pt": "Descreva sua rotina (mi alzo, faccio colazione…).", "units": 50, "lines": 4},
    {"id": "iw03", "level": L1, "topic": "família", "prompt": "Parla della tua famiglia.", "prompt_pt": "Apresente sua família (mia madre, mio padre…).", "units": 50, "lines": 4},
    {"id": "iw04", "level": L1, "topic": "comida", "prompt": "Cosa ti piace mangiare?", "prompt_pt": "O que você gosta de comer? Use mi piace / mi piacciono.", "units": 50, "lines": 4},
    {"id": "iw05", "level": L1, "topic": "passado", "prompt": "Cosa hai fatto lo scorso fine settimana?", "prompt_pt": "Conte seu último fim de semana (passato prossimo).", "units": 50, "lines": 4},
    {"id": "iw06", "level": L1, "topic": "música", "prompt": "Il tuo cantante o la tua serie preferita.", "prompt_pt": "Fale do seu cantor ou série favorita.", "units": 50, "lines": 4},
    {"id": "iw07", "level": L1, "topic": "cidade", "prompt": "Descrivi il tuo quartiere.", "prompt_pt": "Descreva seu bairro (c'è / ci sono…).", "units": 50, "lines": 4},
    {"id": "iw08", "level": L1, "topic": "futuro", "prompt": "Cosa farai durante le vacanze?", "prompt_pt": "Planos para as férias (futuro: andrò, farò…).", "units": 50, "lines": 4},
    {"id": "iw09", "level": L2, "topic": "estudos", "prompt": "Perché studi l'italiano?", "prompt_pt": "Por que você estuda italiano?", "units": 100, "lines": 6},
    {"id": "iw10", "level": L2, "topic": "viagem", "prompt": "Racconta un viaggio indimenticabile.", "prompt_pt": "Conte uma viagem inesquecível.", "units": 100, "lines": 6},
    {"id": "iw11", "level": L2, "topic": "infância", "prompt": "Com'era la tua vita da bambino?", "prompt_pt": "Como era sua vida de criança (imperfetto).", "units": 100, "lines": 6},
    {"id": "iw12", "level": L2, "topic": "saúde", "prompt": "Cosa fai per la tua salute?", "prompt_pt": "O que você faz pela saúde?", "units": 100, "lines": 6},
    {"id": "iw13", "level": L2, "topic": "consumo", "prompt": "Vantaggi e svantaggi degli acquisti online.", "prompt_pt": "Vantagens e desvantagens de comprar on-line.", "units": 100, "lines": 6},
    {"id": "iw14", "level": L2, "topic": "mensagens", "prompt": "Scrivi a un amico per spostare un appuntamento.", "prompt_pt": "Mensagem a um amigo mudando um encontro.", "units": 100, "lines": 6},
    {"id": "iw15", "level": L2, "topic": "hobby", "prompt": "Parla della tua passione.", "prompt_pt": "Apresente seu hobby.", "units": 100, "lines": 6},
    {"id": "iw16", "level": L2, "topic": "futuro", "prompt": "Come ti immagini tra dieci anni?", "prompt_pt": "Como você se imagina daqui a dez anos?", "units": 100, "lines": 6},
]

ROLEPLAY = "1. Qual è la tua idea principale? 2. Puoi fare un esempio? 3. Perché pensi questo?"
