"""Reading, Writing, Listening e Speaking do French Routine (A1–A2). Perguntas em português."""

L1, L2 = "A1", "A2"


def q(question, options, answer, why):
    return {"question": question, "options": options, "answer": answer, "why": why}


TEXTS = [
    {"id": "fr001", "level": L1, "topic": "apresentação", "title": "Je m'appelle Camille",
     "text": "Bonjour ! Je m'appelle Camille et j'ai vingt-deux ans. Je suis française, j'habite à Lyon. Je suis étudiante en architecture.\n\n"
             "J'aime le cinéma et la musique. Le week-end, je sors avec mes amis et nous allons au café. Enchantée !",
     "translation": "Olá! Meu nome é Camille e tenho vinte e dois anos. Sou francesa e moro em Lyon. Sou estudante de arquitetura.\n\n"
                    "Gosto de cinema e de música. No fim de semana saio com meus amigos e vamos ao café. Prazer!",
     "questions": [q("Onde Camille mora?", ["Lyon", "Paris", "Marselha", "Nice"], 0, "J'habite à Lyon."),
                   q("O que ela estuda?", ["Arquitetura", "Medicina", "Música", "Cinema"], 0, "Étudiante en architecture."),
                   q("O que faz no fim de semana?", ["Sai com amigos e vai ao café", "Trabalha", "Viaja", "Estuda"], 0, "Nous allons au café.")]},
    {"id": "fr002", "level": L1, "topic": "rotina", "title": "Ma journée",
     "text": "Je me lève à sept heures. Je prends une douche et je bois un café avec un croissant. À huit heures, je prends le métro.\n\n"
             "Je travaille de neuf heures à dix-sept heures. Le soir, je prépare le dîner et je regarde une série. Je me couche à onze heures.",
     "translation": "Levanto-me às sete. Tomo banho e bebo um café com um croissant. Às oito pego o metrô.\n\n"
                    "Trabalho das nove às dezessete. À noite preparo o jantar e assisto a uma série. Deito-me às onze.",
     "questions": [q("A que horas a pessoa se levanta?", ["Às 7h", "Às 8h", "Às 9h", "Às 6h"], 0, "Je me lève à sept heures."),
                   q("Como vai ao trabalho?", ["De metrô", "De ônibus", "A pé", "De carro"], 0, "Je prends le métro."),
                   q("O que faz à noite?", ["Prepara o jantar e vê uma série", "Vai ao cinema", "Estuda", "Corre"], 0, "Je prépare le dîner et je regarde une série.")]},
    {"id": "fr003", "level": L1, "topic": "família", "title": "Ma famille",
     "text": "Ma famille est petite. Nous sommes quatre : mon père, ma mère, mon frère et moi. Mon père est médecin et ma mère est professeure.\n\n"
             "Mon frère s'appelle Hugo. Il a dix ans et il adore le football. Le dimanche, nous déjeunons chez ma grand-mère.",
     "translation": "Minha família é pequena. Somos quatro: meu pai, minha mãe, meu irmão e eu. Meu pai é médico e minha mãe é professora.\n\n"
                    "Meu irmão se chama Hugo. Tem dez anos e adora futebol. Aos domingos almoçamos na casa da minha avó.",
     "questions": [q("Quantas pessoas há na família?", ["Quatro", "Três", "Cinco", "Seis"], 0, "Nous sommes quatre."),
                   q("Do que Hugo gosta?", ["Futebol", "Música", "Tênis", "Cinema"], 0, "Il adore le football."),
                   q("Onde almoçam aos domingos?", ["Na casa da avó", "Num restaurante", "Em casa", "No parque"], 0, "Chez ma grand-mère.")]},
    {"id": "fr004", "level": L1, "topic": "café", "title": "Au café",
     "text": "Serveur : Bonjour, vous désirez ?\n\nCliente : Un café crème et un croissant, s'il vous plaît.\n\nServeur : Autre chose ?\n\n"
             "Cliente : Non, merci. C'est combien ?\n\nServeur : Quatre euros cinquante.\n\nCliente : Voilà. Merci, au revoir !",
     "translation": "Garçom: Bom dia, o que deseja?\n\nCliente: Um café com creme e um croissant, por favor.\n\nGarçom: Mais alguma coisa?\n\n"
                    "Cliente: Não, obrigada. Quanto é?\n\nGarçom: Quatro euros e cinquenta.\n\nCliente: Aqui está. Obrigada, tchau!",
     "questions": [q("O que a cliente pede para beber?", ["Café com creme", "Chá", "Suco", "Água"], 0, "Un café crème."),
                   q("O que ela pede para comer?", ["Um croissant", "Um sanduíche", "Uma torta", "Nada"], 0, "Un croissant."),
                   q("Quanto custa?", ["4,50 euros", "5 euros", "14,50 euros", "3,50 euros"], 0, "Quatre euros cinquante.")]},
    {"id": "fr005", "level": L1, "topic": "viagem", "title": "Vacances à Nice",
     "text": "Cet été, je vais à Nice avec ma famille. Nous allons voyager en train, parce que c'est rapide et confortable.\n\n"
             "À Nice, nous allons aller à la plage tous les jours et manger des glaces. Je veux aussi visiter le vieux marché.",
     "translation": "Neste verão vou a Nice com minha família. Vamos viajar de trem, porque é rápido e confortável.\n\n"
                    "Em Nice vamos à praia todos os dias e vamos tomar sorvete. Também quero visitar o mercado antigo.",
     "questions": [q("Como a família vai viajar?", ["De trem", "De avião", "De carro", "De ônibus"], 0, "En train."),
                   q("O que vão fazer todo dia?", ["Ir à praia", "Ir ao museu", "Trabalhar", "Fazer compras"], 0, "Aller à la plage tous les jours."),
                   q("O que a pessoa quer visitar?", ["O mercado antigo", "Um museu", "Um castelo", "Uma igreja"], 0, "Le vieux marché.")]},
    {"id": "fr006", "level": L1, "topic": "clima", "title": "Quel temps fait-il ?",
     "text": "Aujourd'hui, il fait beau et chaud. Je vais à la piscine avec ma sœur. Je porte des lunettes de soleil.\n\n"
             "Mais demain, il va pleuvoir et il va faire froid. Je dois prendre un parapluie et un manteau.",
     "translation": "Hoje faz tempo bom e calor. Vou à piscina com minha irmã. Uso óculos de sol.\n\n"
                    "Mas amanhã vai chover e vai fazer frio. Preciso levar um guarda-chuva e um casaco.",
     "questions": [q("Como está o tempo hoje?", ["Bom e quente", "Chuvoso", "Frio", "Com neve"], 0, "Il fait beau et chaud."),
                   q("Aonde a pessoa vai hoje?", ["À piscina", "À praia", "Ao cinema", "À escola"], 0, "Je vais à la piscine."),
                   q("O que precisa levar amanhã?", ["Guarda-chuva e casaco", "Óculos de sol", "Boné", "Nada"], 0, "Un parapluie et un manteau.")]},
    {"id": "fr007", "level": L1, "topic": "música", "title": "Mon chanteur préféré",
     "text": "Mon chanteur préféré s'appelle Léo Martin. Il chante de la pop et il danse très bien. Ses chansons sont joyeuses.\n\n"
             "Le mois dernier, je suis allée à son concert à Paris. Le billet était cher, mais le concert était génial !",
     "translation": "Meu cantor preferido se chama Léo Martin (fictício). Ele canta pop e dança muito bem. Suas músicas são alegres.\n\n"
                    "No mês passado fui ao show dele em Paris. O ingresso foi caro, mas o show foi genial!",
     "questions": [q("Que tipo de música ele canta?", ["Pop", "Rock", "Jazz", "Rap"], 0, "Il chante de la pop."),
                   q("Onde foi o show?", ["Paris", "Lyon", "Bruxelas", "Montreal"], 0, "À son concert à Paris."),
                   q("Como era o ingresso?", ["Caro", "Barato", "Grátis", "Esgotado"], 0, "Le billet était cher.")]},
    {"id": "fr008", "level": L1, "topic": "comida", "title": "Au restaurant",
     "text": "Hier soir, j'ai dîné dans un restaurant italien avec mon copain. J'ai pris des pâtes et il a pris une pizza.\n\n"
             "Le restaurant était propre et le serveur était très sympa. C'était délicieux et pas cher. Nous voulons y retourner.",
     "translation": "Ontem à noite jantei num restaurante italiano com meu namorado. Eu pedi massa e ele pediu uma pizza.\n\n"
                    "O restaurante era limpo e o garçom muito simpático. Estava delicioso e não era caro. Queremos voltar lá.",
     "questions": [q("O que a pessoa comeu?", ["Massa", "Pizza", "Peixe", "Salada"], 0, "J'ai pris des pâtes."),
                   q("“Propre” significa…", ["Limpo", "Próprio apenas", "Apropriado", "Caro"], 0, "Falso amigo: propre = limpo."),
                   q("O que eles querem?", ["Voltar ao restaurante", "Cozinhar em casa", "Trocar de restaurante", "Reclamar"], 0, "Nous voulons y retourner.")]},
    {"id": "fr009", "level": L1, "topic": "compras", "title": "Un cadeau pour ma mère",
     "text": "Dimanche, c'est l'anniversaire de ma mère. Hier, je suis allé au centre commercial pour acheter un cadeau. J'ai vu un sac rouge, mais il était trop cher.\n\n"
             "Finalement, j'ai acheté des fleurs et un livre de cuisine. Ma mère adore cuisiner.",
     "translation": "Domingo é o aniversário da minha mãe. Ontem fui ao shopping comprar um presente. Vi uma bolsa vermelha, mas era cara demais.\n\n"
                    "No fim, comprei flores e um livro de culinária. Minha mãe adora cozinhar.",
     "questions": [q("“Cadeau” significa…", ["Presente", "Cadeado", "Caderno", "Cartão"], 0, "Falso amigo: cadeau = presente."),
                   q("Por que não comprou a bolsa?", ["Era cara demais", "Era feia", "Não tinha cor", "A loja fechou"], 0, "Il était trop cher."),
                   q("O que comprou?", ["Flores e um livro de culinária", "A bolsa", "Uma roupa", "Um perfume"], 0, "Des fleurs et un livre de cuisine.")]},
    {"id": "fr010", "level": L1, "topic": "estudos", "title": "J'apprends le français",
     "text": "Je suis brésilien et j'apprends le français depuis l'année dernière. Le français ressemble au portugais, mais la prononciation est difficile.\n\n"
             "Les faux amis sont un piège : « attendre » ne veut pas dire « atender », mais « esperar ». J'étudie vingt minutes par jour.",
     "translation": "Sou brasileiro e aprendo francês desde o ano passado. O francês se parece com o português, mas a pronúncia é difícil.\n\n"
                    "Os falsos amigos são uma armadilha: “attendre” não quer dizer “atender”, e sim “esperar”. Estudo vinte minutos por dia.",
     "questions": [q("Desde quando a pessoa estuda francês?", ["Desde o ano passado", "Desde criança", "Há uma semana", "Desde este mês"], 0, "Depuis l'année dernière."),
                   q("O que é difícil?", ["A pronúncia", "A gramática", "Os números", "A escrita"], 0, "La prononciation est difficile."),
                   q("“Attendre” significa…", ["Esperar", "Atender", "Entender", "Atirar"], 0, "Attendre = esperar.")]},
    {"id": "fr011", "level": L2, "topic": "moradia", "title": "Mon nouvel appartement",
     "text": "Le mois dernier, j'ai déménagé. Avant, j'habitais loin du travail et je passais une heure dans le métro. Maintenant, je vais au bureau à pied en quinze minutes.\n\n"
             "L'appartement est petit, mais il est très lumineux. Il y a un marché et une boulangerie tout près. Samedi, je vais inviter mes amis à dîner.",
     "translation": "No mês passado me mudei. Antes eu morava longe do trabalho e passava uma hora no metrô. Agora vou ao escritório a pé em quinze minutos.\n\n"
                    "O apartamento é pequeno, mas muito iluminado. Há um mercado e uma padaria bem perto. Sábado vou convidar meus amigos para jantar.",
     "questions": [q("Por que a pessoa se mudou?", ["Morava longe do trabalho", "Era caro", "Queria uma padaria", "Mudou de emprego"], 0, "J'habitais loin du travail."),
                   q("Quanto tempo leva a pé agora?", ["Quinze minutos", "Uma hora", "Cinco minutos", "Meia hora"], 0, "En quinze minutes."),
                   q("O que vai fazer no sábado?", ["Convidar amigos para jantar", "Mudar de novo", "Viajar", "Trabalhar"], 0, "Inviter mes amis à dîner.")]},
    {"id": "fr012", "level": L2, "topic": "saúde", "title": "Chez le médecin",
     "text": "Depuis hier, j'ai mal à la tête et j'ai de la fièvre. Ce matin, je ne suis pas allé travailler, je suis allé chez le médecin. Il m'a dit que j'avais la grippe.\n\n"
             "Il m'a donné des médicaments et m'a conseillé de me reposer et de boire beaucoup d'eau. Dans trois jours, je vais aller mieux.",
     "translation": "Desde ontem estou com dor de cabeça e febre. Hoje de manhã não fui trabalhar, fui ao médico. Ele me disse que eu estava com gripe.\n\n"
                    "Ele me deu remédios e me aconselhou a descansar e beber muita água. Em três dias vou melhorar.",
     "questions": [q("Quais são os sintomas?", ["Dor de cabeça e febre", "Dor de barriga", "Tosse", "Dor nas costas"], 0, "J'ai mal à la tête et j'ai de la fièvre."),
                   q("O que o médico disse?", ["Que é gripe", "Que precisa de cirurgia", "Que não é nada", "Que deve trabalhar"], 0, "J'avais la grippe."),
                   q("Qual foi o conselho?", ["Descansar e beber muita água", "Fazer exercício", "Ir trabalhar", "Comer muito"], 0, "Me reposer et boire beaucoup d'eau.")]},
    {"id": "fr013", "level": L2, "topic": "trabalho", "title": "Mon petit boulot",
     "text": "Le week-end, je travaille dans une librairie. Je commence à dix heures et je finis à dix-huit heures. Je conseille les clients et je range les livres.\n\n"
             "C'est parfois fatigant, mais mes collègues sont très gentils. J'économise de l'argent pour voyager au Portugal en août.",
     "translation": "No fim de semana trabalho numa livraria. Começo às dez e termino às dezoito. Atendo e aconselho os clientes e arrumo os livros.\n\n"
                    "Às vezes é cansativo, mas meus colegas são muito gentis. Estou economizando para viajar a Portugal em agosto.",
     "questions": [q("Onde a pessoa trabalha?", ["Numa livraria", "Num café", "Num hospital", "Numa escola"], 0, "Dans une librairie."),
                   q("Qual é o horário?", ["Das 10h às 18h", "Das 9h às 17h", "Das 8h às 14h", "Das 14h às 22h"], 0, "De dix heures à dix-huit heures."),
                   q("Para onde quer viajar?", ["Portugal", "Espanha", "Itália", "Brasil"], 0, "Voyager au Portugal.")]},
    {"id": "fr014", "level": L2, "topic": "séries", "title": "Une série que je recommande",
     "text": "En ce moment, je regarde une série qui s'appelle « Le Jardin d'Amélie ». L'histoire se passe dans un petit village de Provence.\n\n"
             "Les personnages principaux sont une fleuriste et un cuisinier. Au début, ils se disputent tout le temps, mais petit à petit ils tombent amoureux. Je vous la recommande !",
     "translation": "No momento estou vendo uma série chamada “O jardim de Amélie” (fictícia). A história se passa num pequeno vilarejo da Provença.\n\n"
                    "Os personagens principais são uma florista e um cozinheiro. No começo eles brigam o tempo todo, mas pouco a pouco se apaixonam. Recomendo!",
     "questions": [q("Onde se passa a história?", ["Num vilarejo da Provença", "Em Paris", "Em Lyon", "Numa escola"], 0, "Un petit village de Provence."),
                   q("Quem são os protagonistas?", ["Uma florista e um cozinheiro", "Dois estudantes", "Um médico e uma cantora", "Duas irmãs"], 0, "Une fleuriste et un cuisinier."),
                   q("O que acontece com eles?", ["Brigam e depois se apaixonam", "Ficam amigos", "Mudam de cidade", "Abrem um restaurante"], 0, "Ils tombent amoureux.")]},
    {"id": "fr015", "level": L2, "topic": "viagem", "title": "Demander son chemin",
     "text": "Touriste : Excusez-moi, pour aller au musée du Louvre, s'il vous plaît ?\n\nPassante : Prenez la ligne un du métro et descendez à Palais-Royal.\n\n"
             "Touriste : La station est loin ?\n\nPassante : Non, allez tout droit, puis tournez à droite. C'est à cinq minutes à pied.\n\nTouriste : Merci beaucoup !\n\nPassante : Je vous en prie. Bonne visite !",
     "translation": "Turista: Com licença, para ir ao museu do Louvre, por favor?\n\nPassante: Pegue a linha um do metrô e desça em Palais-Royal.\n\n"
                    "Turista: A estação é longe?\n\nPassante: Não, siga reto e depois vire à direita. Fica a cinco minutos a pé.\n\nTurista: Muito obrigado!\n\nPassante: De nada. Boa visita!",
     "questions": [q("Aonde o turista quer ir?", ["Museu do Louvre", "Torre Eiffel", "Estação de trem", "Hotel"], 0, "Au musée du Louvre."),
                   q("Em qual estação deve descer?", ["Palais-Royal", "Louvre", "Châtelet", "Bastille"], 0, "Descendez à Palais-Royal."),
                   q("Quanto tempo leva até a estação?", ["Cinco minutos a pé", "Meia hora", "Uma hora", "Dez minutos de táxi"], 0, "À cinq minutes à pied.")]},
    {"id": "fr016", "level": L2, "topic": "hobby", "title": "Ma passion : la photographie",
     "text": "Ma passion, c'est la photographie. Quand j'avais quinze ans, mon grand-père m'a offert un vieil appareil photo. Depuis, j'adore prendre des photos.\n\n"
             "Le week-end, je me promène en ville avec mon appareil. J'aime surtout photographier les sourires des gens. Un jour, je voudrais faire une exposition.",
     "translation": "Minha paixão é a fotografia. Quando eu tinha quinze anos, meu avô me deu uma câmera antiga. Desde então adoro tirar fotos.\n\n"
                    "No fim de semana passeio pela cidade com minha câmera. Gosto sobretudo de fotografar os sorrisos das pessoas. Um dia gostaria de fazer uma exposição.",
     "questions": [q("Qual é a paixão da pessoa?", ["Fotografia", "Pintura", "Dança", "Cozinhar"], 0, "Ma passion, c'est la photographie."),
                   q("Quem deu a câmera?", ["O avô", "O pai", "A mãe", "Um amigo"], 0, "Mon grand-père m'a offert…"),
                   q("Qual é o sonho dela?", ["Fazer uma exposição", "Comprar outra câmera", "Ser modelo", "Viajar"], 0, "Faire une exposition.")]},
    {"id": "fr017", "level": L2, "topic": "estações", "title": "Les saisons au Québec",
     "text": "Au Québec, l'hiver est très long et très froid. Il neige beaucoup et les gens font du ski et du patin. L'été est court, mais il fait chaud.\n\n"
             "En automne, les arbres deviennent rouges et oranges : c'est magnifique. Ma saison préférée, c'est l'automne, pour les couleurs.",
     "translation": "No Quebec, o inverno é muito longo e muito frio. Neva muito e as pessoas esquiam e patinam. O verão é curto, mas faz calor.\n\n"
                    "No outono, as árvores ficam vermelhas e laranjas: é magnífico. Minha estação preferida é o outono, pelas cores.",
     "questions": [q("Como é o inverno no Quebec?", ["Longo e muito frio", "Curto", "Quente", "Chuvoso"], 0, "L'hiver est très long et très froid."),
                   q("O que acontece no outono?", ["As árvores ficam vermelhas e laranjas", "Neva muito", "Faz muito calor", "Chove todo dia"], 0, "Les arbres deviennent rouges et oranges."),
                   q("Qual é a estação preferida da pessoa?", ["Outono", "Inverno", "Verão", "Primavera"], 0, "C'est l'automne.")]},
    {"id": "fr018", "level": L2, "topic": "mensagens", "title": "Changement de programme",
     "text": "Salut Léa ! Désolé, mais je ne peux pas venir demain à dix-neuf heures. J'ai une réunion importante au travail et je vais finir tard.\n\n"
             "On peut se voir à vingt heures trente ? Sinon, samedi midi, ça te va ? On peut déjeuner dans le restaurant italien que tu aimes. Réponds-moi !",
     "translation": "Oi, Léa! Desculpe, mas não posso ir amanhã às dezenove. Tenho uma reunião importante no trabalho e vou terminar tarde.\n\n"
                    "Podemos nos ver às vinte e trinta? Se não, sábado ao meio-dia, pode ser? Podemos almoçar no restaurante italiano de que você gosta. Me responde!",
     "questions": [q("Por que a pessoa não pode ir?", ["Tem uma reunião no trabalho", "Está doente", "Perdeu o trem", "Esqueceu"], 0, "J'ai une réunion importante."),
                   q("Que horário sugere amanhã?", ["20h30", "19h", "12h", "21h30"], 0, "Vingt heures trente."),
                   q("Qual é a alternativa?", ["Almoço no sábado", "Café no domingo", "Jantar na sexta", "Cancelar"], 0, "Samedi midi.")]},
    {"id": "fr019", "level": L2, "topic": "consumo", "title": "Acheter en ligne",
     "text": "Aujourd'hui, beaucoup de gens achètent sur Internet. C'est pratique, parce qu'on peut commander de chez soi, et la livraison arrive souvent le lendemain. C'est aussi moins cher.\n\n"
             "Mais il y a des inconvénients : on ne peut pas essayer les vêtements et parfois la taille ne va pas. Alors j'achète les vêtements en magasin et les livres en ligne.",
     "translation": "Hoje muita gente compra pela internet. É prático, porque dá para pedir de casa, e a entrega muitas vezes chega no dia seguinte. Também é mais barato.\n\n"
                    "Mas há desvantagens: não dá para provar as roupas e às vezes o tamanho não serve. Então compro roupas na loja e livros on-line.",
     "questions": [q("Qual é uma vantagem?", ["A entrega chega no dia seguinte", "Dá para provar roupa", "É sempre mais caro", "Precisa ir à loja"], 0, "La livraison arrive souvent le lendemain."),
                   q("Qual é a desvantagem?", ["Não dá para provar roupas", "Demora um mês", "Só aceita dinheiro", "Não há livros"], 0, "On ne peut pas essayer les vêtements."),
                   q("O que a pessoa compra on-line?", ["Livros", "Roupas", "Sapatos", "Comida"], 0, "Les livres en ligne.")]},
    {"id": "fr020", "level": L2, "topic": "dança", "title": "Cours de danse",
     "text": "Cette année, j'ai commencé des cours de danse. Les cours ont lieu le mardi et le jeudi soir, dans une école près de chez moi.\n\n"
             "Au début, je dansais mal et j'étais stressé, mais la prof est très patiente et maintenant je danse mieux. Le mois prochain, nous allons danser à la fête du quartier !",
     "translation": "Este ano comecei aulas de dança. As aulas são às terças e quintas à noite, numa escola perto de casa.\n\n"
                    "No começo eu dançava mal e ficava estressado, mas a professora é muito paciente e agora danço melhor. No mês que vem vamos dançar na festa do bairro!",
     "questions": [q("Quando são as aulas?", ["Terças e quintas à noite", "Todo dia", "Só no sábado", "Segundas de manhã"], 0, "Le mardi et le jeudi soir."),
                   q("Como era no começo?", ["Dançava mal e ficava estressado", "Já dançava bem", "Não gostava", "Faltava muito"], 0, "Je dansais mal et j'étais stressé."),
                   q("O que vai acontecer no mês que vem?", ["Vão dançar na festa do bairro", "Uma prova", "Uma viagem", "O fim das aulas"], 0, "Danser à la fête du quartier.")]},
]

PROMPTS = [
    {"id": "fw01", "level": L1, "topic": "apresentação", "prompt": "Présentez-vous.", "prompt_pt": "Apresente-se: nome, idade, cidade, trabalho ou estudos e gostos.", "units": 50, "lines": 4},
    {"id": "fw02", "level": L1, "topic": "rotina", "prompt": "Décrivez une journée normale.", "prompt_pt": "Descreva sua rotina (verbos pronominais: je me lève…).", "units": 50, "lines": 4},
    {"id": "fw03", "level": L1, "topic": "família", "prompt": "Parlez de votre famille.", "prompt_pt": "Apresente sua família.", "units": 50, "lines": 4},
    {"id": "fw04", "level": L1, "topic": "comida", "prompt": "Qu'est-ce que vous aimez manger ?", "prompt_pt": "O que você gosta de comer? Use j'aime / je n'aime pas.", "units": 50, "lines": 4},
    {"id": "fw05", "level": L1, "topic": "passado", "prompt": "Qu'avez-vous fait le week-end dernier ?", "prompt_pt": "Conte seu último fim de semana (passé composé).", "units": 50, "lines": 4},
    {"id": "fw06", "level": L1, "topic": "música", "prompt": "Votre chanteur ou série préféré.", "prompt_pt": "Fale do seu cantor ou série favorita.", "units": 50, "lines": 4},
    {"id": "fw07", "level": L1, "topic": "cidade", "prompt": "Décrivez votre quartier.", "prompt_pt": "Descreva seu bairro (il y a…).", "units": 50, "lines": 4},
    {"id": "fw08", "level": L1, "topic": "futuro", "prompt": "Qu'est-ce que vous allez faire pendant les vacances ?", "prompt_pt": "Planos para as férias (aller + infinitivo).", "units": 50, "lines": 4},
    {"id": "fw09", "level": L2, "topic": "estudos", "prompt": "Pourquoi apprenez-vous le français ?", "prompt_pt": "Por que você aprende francês?", "units": 100, "lines": 6},
    {"id": "fw10", "level": L2, "topic": "viagem", "prompt": "Racontez un voyage inoubliable.", "prompt_pt": "Conte uma viagem inesquecível.", "units": 100, "lines": 6},
    {"id": "fw11", "level": L2, "topic": "estações", "prompt": "Quelle est votre saison préférée ? Pourquoi ?", "prompt_pt": "Sua estação favorita e por quê.", "units": 100, "lines": 6},
    {"id": "fw12", "level": L2, "topic": "saúde", "prompt": "Que faites-vous pour votre santé ?", "prompt_pt": "O que você faz pela saúde?", "units": 100, "lines": 6},
    {"id": "fw13", "level": L2, "topic": "consumo", "prompt": "Les avantages et les inconvénients des achats en ligne.", "prompt_pt": "Vantagens e desvantagens de comprar on-line.", "units": 100, "lines": 6},
    {"id": "fw14", "level": L2, "topic": "mensagens", "prompt": "Écrivez à un ami pour changer un rendez-vous.", "prompt_pt": "Mensagem a um amigo mudando um encontro.", "units": 100, "lines": 6},
    {"id": "fw15", "level": L2, "topic": "hobby", "prompt": "Parlez de votre passion.", "prompt_pt": "Apresente seu hobby.", "units": 100, "lines": 6},
    {"id": "fw16", "level": L2, "topic": "futuro", "prompt": "Comment vous imaginez-vous dans dix ans ?", "prompt_pt": "Como você se imagina daqui a dez anos?", "units": 100, "lines": 6},
]

ROLEPLAY = "1. Quelle est votre idée principale ? 2. Pouvez-vous donner un exemple ? 3. Pourquoi pensez-vous cela ?"
