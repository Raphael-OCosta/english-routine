"""Conteúdo do Italian Routine (italiano, A1–A2), pensado para quem fala português.

Conjugações: regras para os regulares (-are, -ere, -ire, -isc-, -care/-gare, -iare) + tabelas de
irregulares. Revisão por professor ou falante nativo recomendada antes da venda.
"""

SOUNDS = [
    ("c + e/i", "tch", "ciao", "ce/ci soam “tche/tchi”"), ("ch", "k", "chiesa", "ch antes de e/i soa “k”"), ("g + e/i", "dj", "gelato", "ge/gi soam “dje/dji”"),
    ("gh", "g duro", "spaghetti", "gh antes de e/i soa “gue/gui”"), ("gli", "lh", "famiglia", "como “lh”"), ("gn", "nh", "bagno", "como “nh”"),
    ("sc + e/i", "x", "pesce", "sce/sci soam “xe/xi”"), ("z", "ts / dz", "pizza", "“ts” ou “dz”"), ("consoantes duplas", "mais longas", "notte", "segure a consoante: not-te"),
    ("r", "r vibrante", "Roma", "a ponta da língua vibra"), ("e / o finais", "e / o", "pane", "não viram “i” e “u”: “pane”, não “pani”"),
    ("h", "muda", "ho", "nunca se pronuncia"), ("qu", "kw", "quando", "como em “quando”"),
]

VOCAB = [
    ("la madre", "a mãe", "pessoas", 1), ("il padre", "o pai", "pessoas", 1), ("il fratello", "o irmão", "pessoas", 1), ("la sorella", "a irmã", "pessoas", 1),
    ("il figlio", "o filho", "pessoas", 1), ("la figlia", "a filha", "pessoas", 1), ("l'amico", "o amigo", "pessoas", 1), ("l'amica", "a amiga", "pessoas", 1),
    ("il bambino", "o menino / a criança", "pessoas", 1), ("la donna", "a mulher", "pessoas", 1), ("l'uomo", "o homem", "pessoas", 1), ("il professore", "o professor", "pessoas", 1),
    ("il medico", "o médico", "pessoas", 1), ("il vicino", "o vizinho", "pessoas", 2), ("il nonno", "o avô", "pessoas", 1), ("la nonna", "a avó", "pessoas", 1),
    ("il cameriere", "o garçom", "pessoas", 2), ("il capo", "o chefe", "pessoas", 2), ("lo studente", "o estudante", "pessoas", 1), ("il ragazzo", "o rapaz / namorado", "pessoas", 1),
    ("il pane", "o pão", "comida", 1), ("l'acqua", "a água", "comida", 1), ("il latte", "o leite", "comida", 1), ("il caffè", "o café", "comida", 1), ("il tè", "o chá", "comida", 1),
    ("il formaggio", "o queijo", "comida", 1), ("la mela", "a maçã", "comida", 1), ("l'uovo", "o ovo", "comida", 1), ("il pollo", "o frango", "comida", 1),
    ("la carne", "a carne", "comida", 1), ("il pesce", "o peixe", "comida", 1), ("il riso", "o arroz", "comida", 1), ("la frutta", "a fruta", "comida", 1),
    ("la torta", "o bolo", "comida", 1), ("il gelato", "o sorvete", "comida", 1), ("la colazione", "o café da manhã", "comida", 1), ("il pranzo", "o almoço", "comida", 1),
    ("la cena", "o jantar", "comida", 1), ("il vino", "o vinho", "comida", 2), ("la birra", "a cerveja", "comida", 2), ("il cornetto", "o croissant", "comida", 1),
    ("il burro", "a manteiga", "comida", 2), ("lo zucchero", "o açúcar", "comida", 2), ("il succo", "o suco", "comida", 1), ("il panino", "o sanduíche", "comida", 1),
    ("la casa", "a casa", "lugares", 1), ("la scuola", "a escola", "lugares", 1), ("il mercato", "o mercado", "lugares", 1), ("il ristorante", "o restaurante", "lugares", 1),
    ("l'ospedale", "o hospital", "lugares", 1), ("la spiaggia", "a praia", "lugares", 1), ("la città", "a cidade", "lugares", 1), ("la strada", "a rua", "lugares", 1),
    ("il negozio", "a loja", "lugares", 1), ("il parco", "o parque", "lugares", 1), ("la biblioteca", "a biblioteca", "lugares", 1), ("il cinema", "o cinema", "lugares", 1),
    ("l'aeroporto", "o aeroporto", "lugares", 2), ("la stazione", "a estação", "lugares", 1), ("la banca", "o banco", "lugares", 2), ("la farmacia", "a farmácia", "lugares", 1),
    ("il supermercato", "o supermercado", "lugares", 1), ("la panetteria", "a padaria", "lugares", 1), ("il museo", "o museu", "lugares", 1), ("l'ufficio", "o escritório", "lugares", 1),
    ("la piazza", "a praça", "lugares", 1), ("lo stadio", "o estádio", "lugares", 2), ("il teatro", "o teatro", "lugares", 2), ("la pasticceria", "a confeitaria", "lugares", 2),
    ("oggi", "hoje", "tempo", 1), ("domani", "amanhã", "tempo", 1), ("ieri", "ontem", "tempo", 1), ("adesso", "agora", "tempo", 1), ("sempre", "sempre", "tempo", 1),
    ("mai", "nunca", "tempo", 1), ("la settimana", "a semana", "tempo", 1), ("il mese", "o mês", "tempo", 1), ("l'anno", "o ano", "tempo", 1), ("il giorno", "o dia", "tempo", 1),
    ("la notte", "a noite", "tempo", 1), ("la sera", "a noite (fim do dia)", "tempo", 1), ("la mattina", "a manhã", "tempo", 1), ("il fine settimana", "o fim de semana", "tempo", 1),
    ("spesso", "frequentemente", "tempo", 2), ("già", "já", "tempo", 2), ("ancora", "ainda", "tempo", 2), ("presto", "cedo / logo", "tempo", 2),
    ("il libro", "o livro", "objetos", 1), ("il tavolo", "a mesa", "objetos", 1), ("la sedia", "a cadeira", "objetos", 1), ("la macchina", "o carro", "objetos", 1),
    ("il telefono", "o telefone", "objetos", 1), ("la chiave", "a chave", "objetos", 1), ("i vestiti", "as roupas", "objetos", 1), ("le scarpe", "os sapatos", "objetos", 1),
    ("la camicia", "a camisa", "objetos", 1), ("i soldi", "o dinheiro", "objetos", 1), ("il computer", "o computador", "objetos", 1), ("la borsa", "a bolsa", "objetos", 1),
    ("gli occhiali", "os óculos", "objetos", 2), ("l'orologio", "o relógio", "objetos", 2), ("il letto", "a cama", "objetos", 1), ("il giornale", "o jornal", "objetos", 2),
    ("il biglietto", "o bilhete / ingresso", "objetos", 2), ("il film", "o filme", "objetos", 1), ("la canzone", "a canção", "objetos", 1), ("la lettera", "a carta", "objetos", 1),
    ("il sole", "o sol", "natureza", 1), ("la pioggia", "a chuva", "natureza", 1), ("il mare", "o mar", "natureza", 1), ("il cane", "o cachorro", "natureza", 1),
    ("il gatto", "o gato", "natureza", 1), ("la montagna", "a montanha", "natureza", 2), ("l'albero", "a árvore", "natureza", 2), ("il fiore", "a flor", "natureza", 1),
    ("la testa", "a cabeça", "corpo", 1), ("la mano", "a mão", "corpo", 1), ("il piede", "o pé", "corpo", 1), ("gli occhi", "os olhos", "corpo", 1), ("la bocca", "a boca", "corpo", 2),
    ("la pancia", "a barriga", "corpo", 2), ("la schiena", "as costas", "corpo", 2), ("i capelli", "o cabelo", "corpo", 2),
    ("il treno", "o trem", "transporte", 1), ("l'autobus", "o ônibus", "transporte", 1), ("l'aereo", "o avião", "transporte", 1), ("la metropolitana", "o metrô", "transporte", 1),
    ("la bicicletta", "a bicicleta", "transporte", 1), ("il taxi", "o táxi", "transporte", 1),
    ("parlare", "falar", "verbos", 1), ("mangiare", "comer", "verbos", 1), ("abitare", "morar", "verbos", 1), ("lavorare", "trabalhar", "verbos", 1), ("studiare", "estudar", "verbos", 1),
    ("bere", "beber", "verbos", 1), ("scrivere", "escrever", "verbos", 1), ("leggere", "ler", "verbos", 1), ("comprare", "comprar", "verbos", 1), ("ascoltare", "escutar", "verbos", 1),
    ("guardare", "olhar / assistir", "verbos", 1), ("avere", "ter", "verbos", 1), ("essere", "ser / estar", "verbos", 1), ("andare", "ir", "verbos", 1), ("fare", "fazer", "verbos", 1),
    ("volere", "querer", "verbos", 1), ("potere", "poder", "verbos", 1), ("venire", "vir", "verbos", 1), ("prendere", "pegar / tomar", "verbos", 1), ("uscire", "sair", "verbos", 1),
    ("dormire", "dormir", "verbos", 1), ("amare", "amar", "verbos", 1), ("cercare", "procurar", "verbos", 2), ("aspettare", "esperar", "verbos", 2), ("viaggiare", "viajar", "verbos", 2),
    ("cantare", "cantar", "verbos", 1), ("ballare", "dançar", "verbos", 1), ("sapere", "saber", "verbos", 2), ("conoscere", "conhecer", "verbos", 2), ("vedere", "ver", "verbos", 1),
    ("grande", "grande", "adjetivos", 1), ("piccolo", "pequeno", "adjetivos", 1), ("buono", "bom", "adjetivos", 1), ("cattivo", "ruim / mau", "adjetivos", 1), ("bello", "bonito", "adjetivos", 1),
    ("caro", "caro", "adjetivos", 1), ("nuovo", "novo", "adjetivos", 1), ("vecchio", "velho", "adjetivos", 1), ("contento", "contente", "adjetivos", 1), ("triste", "triste", "adjetivos", 1),
    ("stanco", "cansado", "adjetivos", 1), ("facile", "fácil", "adjetivos", 2), ("difficile", "difícil", "adjetivos", 2), ("caldo", "quente", "adjetivos", 1), ("freddo", "frio", "adjetivos", 1),
    ("rosso", "vermelho", "adjetivos", 1), ("giallo", "amarelo", "adjetivos", 1), ("azzurro", "azul", "adjetivos", 1), ("verde", "verde", "adjetivos", 1), ("simpatico", "simpático", "adjetivos", 1),
]

FALSE_FRIENDS = [
    ("il burro", "a manteiga", "o burro"), ("salire", "subir", "sair"), ("guardare", "olhar / assistir", "guardar"), ("squisito", "delicioso", "esquisito"),
    ("la camera", "o quarto", "a câmera"), ("caldo", "quente", "caldo (sopa)"), ("la tasca", "o bolso", "a tasca (taberna)"), ("lo scherzo", "a brincadeira", "o esquerdo"),
    ("prendere", "pegar / tomar", "prender"), ("la firma", "a assinatura", "a firma (empresa)"), ("il negozio", "a loja", "o negócio"), ("la libreria", "a livraria / estante", "a biblioteca"),
    ("lo stipendio", "o salário", "o estipêndio (bolsa)"), ("la fermata", "o ponto (de ônibus)", "a fermata (música)"), ("il palazzo", "o prédio", "o palácio"),
    ("la cantina", "a adega / porão", "a cantina (restaurante)"), ("ridere", "rir", "redigir"), ("la gamba", "a perna", "a gamba (camarão)"), ("la parola", "a palavra", "a parola (fala solene)"),
    ("la sala", "a sala de estar / salão", "a sala de aula"), ("la tazza", "a xícara", "a taça"), ("l'aceto", "o vinagre", "o aceite"), ("il costume", "o maiô / traje", "o costume (hábito)"),
    ("il fermaglio", "o grampo", "o ferragem"), ("la stanza", "o quarto / cômodo", "a estância"),
]

PERSONS = ["io", "tu", "lui", "noi", "voi", "loro"]
PRESENT = {
    "essere": ["sono", "sei", "è", "siamo", "siete", "sono"], "avere": ["ho", "hai", "ha", "abbiamo", "avete", "hanno"],
    "andare": ["vado", "vai", "va", "andiamo", "andate", "vanno"], "fare": ["faccio", "fai", "fa", "facciamo", "fate", "fanno"],
    "potere": ["posso", "puoi", "può", "possiamo", "potete", "possono"], "volere": ["voglio", "vuoi", "vuole", "vogliamo", "volete", "vogliono"],
    "venire": ["vengo", "vieni", "viene", "veniamo", "venite", "vengono"], "bere": ["bevo", "bevi", "beve", "beviamo", "bevete", "bevono"],
    "dire": ["dico", "dici", "dice", "diciamo", "dite", "dicono"], "stare": ["sto", "stai", "sta", "stiamo", "state", "stanno"],
    "uscire": ["esco", "esci", "esce", "usciamo", "uscite", "escono"], "dare": ["do", "dai", "dà", "diamo", "date", "danno"],
    "sapere": ["so", "sai", "sa", "sappiamo", "sapete", "sanno"],
}
ISC = {"finire", "capire", "preferire", "spedire"}
PARTICIPLE = {"essere": "stato", "conoscere": "conosciuto", "fare": "fatto", "leggere": "letto", "scrivere": "scritto", "vedere": "visto", "prendere": "preso", "bere": "bevuto",
              "dire": "detto", "aprire": "aperto", "chiudere": "chiuso", "venire": "venuto", "mettere": "messo", "rispondere": "risposto", "chiedere": "chiesto"}
ESSERE_VERBS = {"andare", "venire", "uscire", "tornare", "partire"}
FUTURE_STEM = {"essere": "sar", "avere": "avr", "andare": "andr", "fare": "far", "potere": "potr", "volere": "vorr", "venire": "verr", "bere": "berr",
               "vedere": "vedr", "sapere": "sapr", "dare": "dar", "stare": "star"}
IMPERFECT = {"essere": ["ero", "eri", "era", "eravamo", "eravate", "erano"], "fare": ["facevo", "facevi", "faceva", "facevamo", "facevate", "facevano"],
             "bere": ["bevevo", "bevevi", "beveva", "bevevamo", "bevevate", "bevevano"], "dire": ["dicevo", "dicevi", "diceva", "dicevamo", "dicevate", "dicevano"]}
GERUND = {"fare": "facendo", "bere": "bevendo", "dire": "dicendo"}

VERBS = [
    ("parlare", "falar", "italiano", 1), ("lavorare", "trabalhar", "a Roma", 1), ("studiare", "estudar", "la sera", 1), ("mangiare", "comer", "a casa", 1),
    ("bere", "beber", "acqua", 1), ("abitare", "morar", "a Milano", 1), ("scrivere", "escrever", "un messaggio", 1), ("leggere", "ler", "il giornale", 1),
    ("comprare", "comprar", "il pane", 1), ("ascoltare", "escutar", "musica", 1), ("guardare", "assistir", "la TV", 1), ("cantare", "cantar", "sotto la doccia", 1),
    ("ballare", "dançar", "il sabato", 1), ("viaggiare", "viajar", "in treno", 2), ("cercare", "procurar", "le chiavi", 2), ("avere", "ter", "due fratelli", 1),
    ("essere", "ser", "di San Paolo", 1), ("andare", "ir", "al lavoro", 1), ("fare", "fazer", "i compiti", 1), ("volere", "querer", "un caffè", 1),
    ("potere", "poder", "venire", 1), ("venire", "vir", "alla festa", 1), ("prendere", "pegar", "l'autobus", 1), ("uscire", "sair", "con gli amici", 1),
    ("dormire", "dormir", "otto ore", 1), ("aspettare", "esperar", "il treno", 2), ("vedere", "ver", "un film", 1), ("sapere", "saber", "la risposta", 2),
    ("conoscere", "conhecer", "Roma", 2), ("finire", "terminar", "il lavoro", 2), ("capire", "entender", "la lezione", 2), ("preferire", "preferir", "il tè", 2),
    ("aprire", "abrir", "la finestra", 1), ("chiudere", "fechar", "la porta", 2), ("pagare", "pagar", "il conto", 2), ("giocare", "jogar", "a calcio", 1),
    ("tornare", "voltar", "a casa", 2), ("partire", "partir", "per le vacanze", 2), ("dire", "dizer", "la verità", 2), ("dare", "dar", "un regalo", 2),
]

GRAMMAR = [
    ("___ pane è buono.", "Il", ["Lo", "La", "L'"], "Pane: masculino, consoante comum → il.", 1, "artigos"),
    ("___ studente è bravo.", "Lo", ["Il", "La", "L'"], "Masculino com s + consoante → lo.", 1, "artigos"),
    ("___ zucchero è sul tavolo.", "Lo", ["Il", "La", "L'"], "Masculino com z → lo.", 2, "artigos"),
    ("___ amico di Marco è simpatico.", "L'", ["Il", "Lo", "La"], "Antes de vogal → l'.", 1, "artigos"),
    ("___ casa è grande.", "La", ["Il", "Lo", "L'"], "Feminino → la.", 1, "artigos"),
    ("___ libri sono nuovi.", "I", ["Gli", "Le", "Il"], "Plural masculino comum → i.", 1, "artigos"),
    ("___ studenti sono in classe.", "Gli", ["I", "Le", "Lo"], "Plural de lo/l' → gli.", 2, "artigos"),
    ("___ ragazze sono italiane.", "Le", ["I", "Gli", "La"], "Plural feminino → le.", 1, "artigos"),
    ("Vado ___ cinema.", "al", ["a il", "alla", "nel"], "a + il = al.", 1, "preposições"),
    ("Vado ___ stazione.", "alla", ["al", "all'", "in"], "a + la = alla.", 1, "preposições"),
    ("Vado ___ aeroporto.", "all'", ["al", "alla", "allo"], "a + l' = all'.", 2, "preposições"),
    ("Vado ___ stadio.", "allo", ["al", "alla", "all'"], "a + lo = allo.", 2, "preposições"),
    ("Studio ___ biblioteca.", "in", ["alla", "al", "nella"], "Com biblioteca, banca, farmacia, ufficio usa-se in sem artigo.", 2, "preposições"),
    ("Il libro è ___ tavolo.", "sul", ["su il", "sulla", "nel"], "su + il = sul.", 2, "preposições"),
    ("Io ___ brasiliano.", "sono", ["sei", "è", "ho"], "Essere com io → sono.", 1, "essere / avere"),
    ("Lei ___ vent'anni.", "ha", ["è", "hai", "hanno"], "Idade usa avere: ha vent'anni.", 1, "essere / avere"),
    ("Noi ___ fame.", "abbiamo", ["siamo", "avete", "hanno"], "Fome: avere fame.", 1, "essere / avere"),
    ("Lui ___ stanco.", "è", ["ha", "sei", "ho"], "Estado: essere stanco.", 1, "essere / avere"),
    ("Io non ___ inglese.", "parlo", ["parli", "parla", "parlare"], "Negação: non antes do verbo.", 1, "negação"),
    ("Mi ___ la pizza.", "piace", ["piacciono", "piaccio", "piaci"], "Piacere concorda com o que agrada (singular).", 1, "piacere"),
    ("Mi ___ i gatti.", "piacciono", ["piace", "piaccio", "piacete"], "O que agrada é plural → piacciono.", 1, "piacere"),
    ("A Marco ___ piace il calcio.", "gli", ["le", "lo", "si"], "A lui → gli piace.", 2, "piacere"),
    ("A Giulia ___ piace ballare.", "le", ["gli", "la", "si"], "A lei → le piace.", 2, "piacere"),
    ("Questo è ___ libro.", "il mio", ["mio", "la mia", "i miei"], "Possessivo com artigo: il mio libro.", 1, "possessivos"),
    ("Questa è ___ sorella.", "mia", ["la mia", "mio", "le mie"], "Parente no singular: sem artigo (mia sorella).", 2, "possessivos"),
    ("Ieri ___ mangiato una pizza.", "ho", ["sono", "hai", "ha"], "Passato prossimo com avere: ho mangiato.", 2, "passato prossimo"),
    ("Ieri Giulia è ___ al cinema.", "andata", ["andato", "andare", "andati"], "Andare usa essere e concorda: Giulia è andata.", 2, "passato prossimo"),
    ("Noi siamo ___ a Roma.", "andati", ["andato", "andate", "andare"], "Essere + particípio concorda: noi (masc.) andati.", 2, "passato prossimo"),
    ("Adesso ___ mangiando.", "sto", ["sono", "ho", "faccio"], "Stare + gerundio = ação em andamento.", 2, "stare + gerundio"),
    ("Domani ___ al mare.", "andrò", ["andavo", "vado andare", "sono andato"], "Futuro semplice: andrò.", 2, "futuro"),
    ("Che ___ fa oggi?", "tempo", ["clima", "ora", "giorno"], "Que tempo faz? → Che tempo fa?", 1, "tempo"),
    ("Oggi fa ___.", "caldo", ["calda", "calore", "caldi"], "Clima: fa caldo, fa freddo.", 1, "tempo"),
    ("___ anni hai?", "Quanti", ["Quanto", "Quante", "Che"], "Anni é masculino plural → quanti.", 1, "perguntas"),
    ("___ abiti?", "Dove", ["Quando", "Chi", "Cosa"], "Lugar → dove.", 1, "perguntas"),
    ("Abito ___ Italia.", "in", ["a", "nel", "all'"], "Países → in (in Italia).", 1, "preposições"),
    ("Abito ___ Roma.", "a", ["in", "al", "nella"], "Cidades → a.", 1, "preposições"),
    ("Marco è più alto ___ Luca.", "di", ["che", "come", "da"], "Comparativo com nome: più … di.", 2, "comparação"),
    ("C'___ un bar qui vicino.", "è", ["sono", "ha", "e"], "C'è = há (singular).", 1, "c'è / ci sono"),
    ("Ci ___ due farmacie in centro.", "sono", ["è", "hanno", "ha"], "Ci sono = há (plural).", 1, "c'è / ci sono"),
    ("Devo ___ i compiti.", "fare", ["faccio", "fatto", "fa"], "Dovere + infinitivo.", 1, "modais"),
]

NUMBERS = [
    ("quindici", "15", ["cinque", "cinquanta", "quattordici"]), ("venti", "20", ["dodici", "trenta", "due"]), ("sedici", "16", ["sei", "sessanta", "diciassette"]),
    ("trentuno", "31", ["trenta uno", "tredici", "trecentouno"]), ("settanta", "70", ["sessanta", "diciassette", "settecento"]), ("ottanta", "80", ["otto", "diciotto", "ottocento"]),
    ("novanta", "90", ["nove", "diciannove", "novecento"]), ("cento", "100", ["mille", "dieci", "centi"]), ("mille", "1.000", ["un mille", "cento", "milione"]),
    ("ventuno", "21", ["venti uno", "ventiuno", "dodici"]), ("le due e mezza", "2h30", ["le due e mezzo ora", "due mezza", "le mezza due"]), ("mezzogiorno", "meio-dia", ["mezzanotte", "mezzodì sera", "dodici sera"]),
    ("lunedì", "segunda-feira", ["martedì", "domenica", "sabato"]), ("mercoledì", "quarta-feira", ["martedì", "giovedì", "venerdì"]), ("gennaio", "janeiro", ["giugno", "luglio", "febbraio"]),
    ("dieci euro", "10 euros", ["due euro", "dodici euro", "cento euro"]), ("ho vent'anni", "tenho 20 anos", ["sono vent'anni", "ho venti", "io venti anni"]),
    ("il primo maggio", "1º de maio", ["il uno maggio", "maggio primo", "la prima maggio"]), ("trecento", "300", ["tre cento", "trenta", "tredicento"]), ("diciotto", "18", ["dieciotto", "otto", "ottanta"]),
]

PHRASES = [
    ("Ciao", "Oi / Tchau", "informal"), ("Buongiorno", "Bom dia", ""), ("Buonasera", "Boa noite (cumprimento)", ""), ("Come stai?", "Como vai?", ""),
    ("Piacere", "Muito prazer", ""), ("Grazie", "Obrigado(a)", ""), ("Prego", "De nada / Por favor, entre", ""), ("Scusa", "Desculpe", "informal"),
    ("Mi scusi", "Com licença (formal)", "formal"), ("Per favore", "Por favor", ""), ("Quanto costa?", "Quanto custa?", ""), ("Dov'è il bagno?", "Onde fica o banheiro?", ""),
    ("Non capisco", "Não entendo", ""), ("Può ripetere?", "Pode repetir?", ""), ("Più piano, per favore", "Mais devagar, por favor", ""), ("Il conto, per favore", "A conta, por favor", ""),
    ("È buonissimo!", "Está delicioso!", ""), ("Salute!", "Saúde! (brinde)", ""), ("Ti amo", "Eu te amo", ""), ("Buon compleanno!", "Feliz aniversário!", ""),
    ("A presto", "Até breve", ""), ("A domani", "Até amanhã", ""), ("Buon appetito!", "Bom apetite!", ""), ("Buonanotte", "Boa noite (ao dormir)", ""),
    ("Nessun problema", "Sem problema", ""), ("Che peccato!", "Que pena!", ""), ("D'accordo", "Combinado / Concordo", ""), ("Che ore sono?", "Que horas são?", ""),
    ("Mi chiamo…", "Meu nome é…", ""), ("Arrivederci", "Até logo (formal)", ""),
]

SUBJECTS = [("Io", 0), ("Tu", 1), ("Lui", 2), ("Lei", 2), ("Noi", 3), ("Voi", 4), ("Loro", 5), ("Marco", 2), ("Giulia", 2), ("Mio fratello", 2),
            ("Mia sorella", 2), ("I miei amici", 5), ("I miei genitori", 5), ("Il professore", 2), ("La vicina", 2), ("I bambini", 5), ("Luca e io", 3),
            ("Il tuo amico", 2), ("Anna e Sara", 5), ("Mio padre", 2), ("Mia madre", 2), ("Gli studenti", 5), ("La signora Rossi", 2), ("Tu e Paolo", 4)]
# (verbo, objeto, gênero m/f, plural?, lugar, preposição de lugar)
ACTIVITIES = [
    ("comprare", "pane", "m", False, "panetteria", "in"), ("bere", "caffè", "m", False, "bar", "al"), ("mangiare", "pizza", "f", False, "pizzeria", "in"),
    ("leggere", "giornale", "m", False, "biblioteca", "in"), ("guardare", "film", "m", False, "cinema", "al"), ("comprare", "frutta", "f", False, "mercato", "al"),
    ("comprare", "camicia", "f", False, "centro", "in"), ("prendere", "treno", "m", False, "stazione", "alla"), ("vedere", "quadro", "m", False, "museo", "al"),
    ("mangiare", "gelato", "m", False, "spiaggia", "in"), ("comprare", "medicine", "f", True, "farmacia", "in"), ("spedire", "pacco", "m", False, "posta", "alla"),
    ("guardare", "partita", "f", False, "stadio", "allo"), ("comprare", "biglietto", "m", False, "stazione", "alla"), ("bere", "tè", "m", False, "bar", "al"),
    ("leggere", "libro", "m", False, "parco", "al"), ("comprare", "torta", "f", False, "pasticceria", "in"), ("cantare", "canzone", "f", False, "karaoke", "al"),
    ("prendere", "aereo", "m", False, "aeroporto", "all'"), ("fare", "spesa", "f", False, "supermercato", "al"), ("mangiare", "panino", "m", False, "bar", "al"),
    ("comprare", "fiori", "m", True, "mercato", "al"), ("guardare", "spettacolo", "m", False, "teatro", "a"), ("ascoltare", "concerto", "m", False, "parco", "al"),
    ("comprare", "giornale", "m", False, "edicola", "in"), ("cercare", "libro", "m", False, "libreria", "in"), ("ordinare", "dolce", "m", False, "ristorante", "al"),
    ("aspettare", "autobus", "m", False, "fermata", "alla"), ("comprare", "latte", "m", False, "supermercato", "al"), ("bere", "succo", "m", False, "bar", "al"),
    ("vedere", "mostra", "f", False, "museo", "al"), ("noleggiare", "bicicletta", "f", False, "parco", "al"), ("mangiare", "cornetto", "m", False, "bar", "al"),
    ("comprare", "vestito", "m", False, "centro", "in"), ("leggere", "rivista", "f", False, "treno", "in"), ("fare", "foto", "f", True, "spiaggia", "in"),
    ("guardare", "serie", "f", False, "albergo", "in"), ("comprare", "formaggio", "m", False, "mercato", "al"), ("visitare", "castello", "m", False, "campagna", "in"),
    ("pagare", "conto", "m", False, "ristorante", "al"),
]

GUIDE = [
    ("Pronúncia para brasileiros", "As vogais finais não mudam (pane, não “pani”). Ce/ci = tche/tchi; che/chi = ke/ki; ge/gi = dje/dji; gli = lh; gn = nh. Consoantes duplas são mais longas (notte). H é muda."),
    ("Artigos", "il (masc.), lo (antes de s + consoante, z, gn, ps), l' (antes de vogal), la (fem.). Plural: i, gli, le. Ex.: il libro, lo studente, l'amico, la casa, i libri, gli studenti, le case."),
    ("Preposições com artigo", "a + il = al, a + lo = allo, a + la = alla, a + l' = all'. Também in → nel/nella, di → del/della, su → sul/sulla. Alguns lugares usam in sem artigo: in biblioteca, in banca, in farmacia, in ufficio."),
    ("Essere e avere", "Essere (sono, sei, è, siamo, siete, sono) e avere (ho, hai, ha, abbiamo, avete, hanno). Idade e fome usam avere: ho vent'anni, ho fame."),
    ("Presente", "-are: parlo, parli, parla, parliamo, parlate, parlano. -ere: leggo, leggi, legge… -ire: dormo / finisco (verbos em -isc-). Irregulares: vado, faccio, posso, voglio, vengo, bevo, esco."),
    ("Passato prossimo", "avere/essere + particípio: ho mangiato, ho letto, ho preso. Verbos de movimento (andare, venire, uscire, partire, tornare) usam essere e concordam: Giulia è andata, siamo partiti."),
    ("Imperfetto e futuro", "Imperfetto (hábitos no passado): parlavo, leggevo, dormivo; essere → ero. Futuro: parlerò, leggerò, dormirò; irregulares: andrò, sarò, avrò, farò."),
    ("Stare + gerundio", "Ação em andamento: sto mangiando, stai leggendo, stanno dormendo (-are → -ando; -ere/-ire → -endo)."),
    ("Piacere", "Funciona “ao contrário”: mi piace la pizza (singular), mi piacciono i gatti (plural). A lui → gli piace; a lei → le piace."),
    ("Possessivos", "Com artigo: il mio libro, la mia casa. Sem artigo com parentes no singular: mia madre, mio fratello (mas: i miei fratelli)."),
    ("C'è e ci sono", "c'è (há, singular) e ci sono (há, plural): c'è un bar, ci sono due farmacie."),
    ("Falsos amigos", "burro = manteiga; salire = subir; guardare = olhar; squisito = delicioso; camera = quarto; prendere = pegar; negozio = loja."),
]
