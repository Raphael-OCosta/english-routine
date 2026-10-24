"""Conteúdo do French Routine (francês, A1–A2), pensado para quem fala português.

Conjugações por tabela revisada (presente, passé composé com avoir, imparfait regular a
partir do radical de “nous”). Revisão por professor ou falante nativo recomendada antes da venda.
"""

SOUNDS = [
    ("ou", "u", "rouge", "como o “u” português: “ruj”"), ("u", "ü", "tu", "lábios de “u”, língua de “i”"), ("eu / œu", "ê fechado", "deux", "como “ê” com lábios arredondados"),
    ("on / om", "õ nasal", "bon", "nasal sem fechar com “m”"), ("an / en", "ã nasal", "enfant", "nasal aberta"), ("in / ain", "ẽ nasal", "pain", "nasal parecida com “é”"),
    ("r", "r de garganta", "Paris", "vibra no fundo da garganta"), ("ch", "x", "chat", "como “x” em “xícara”"), ("j / ge", "j", "je", "como em português"),
    ("gn", "nh", "montagne", "como “nh”"), ("oi", "uá", "moi", "“muá”"), ("é", "ê fechado", "café", "“caFÊ”"), ("è / ê", "é aberto", "mère", "“mér”"),
    ("h", "muda", "hôtel", "não se pronuncia"), ("final mudo", "—", "petit", "consoantes finais quase nunca soam"), ("liaison", "liga", "les amis", "“lezami”: o s final liga com a vogal"),
]

# (francês, português, tema, nível)
VOCAB = [
    ("la mère", "a mãe", "pessoas", 1), ("le père", "o pai", "pessoas", 1), ("le frère", "o irmão", "pessoas", 1), ("la sœur", "a irmã", "pessoas", 1),
    ("le fils", "o filho", "pessoas", 1), ("la fille", "a filha / a menina", "pessoas", 1), ("l'ami", "o amigo", "pessoas", 1), ("l'amie", "a amiga", "pessoas", 1),
    ("l'enfant", "a criança", "pessoas", 1), ("la femme", "a mulher", "pessoas", 1), ("l'homme", "o homem", "pessoas", 1), ("le professeur", "o professor", "pessoas", 1),
    ("le médecin", "o médico", "pessoas", 1), ("le voisin", "o vizinho", "pessoas", 2), ("le grand-père", "o avô", "pessoas", 1), ("la grand-mère", "a avó", "pessoas", 1),
    ("le serveur", "o garçom", "pessoas", 2), ("le patron", "o chefe", "pessoas", 2), ("l'étudiant", "o estudante", "pessoas", 1), ("le copain", "o colega / namorado", "pessoas", 2),
    ("le pain", "o pão", "comida", 1), ("l'eau", "a água", "comida", 1), ("le lait", "o leite", "comida", 1), ("le café", "o café", "comida", 1), ("le thé", "o chá", "comida", 1),
    ("le fromage", "o queijo", "comida", 1), ("la pomme", "a maçã", "comida", 1), ("l'œuf", "o ovo", "comida", 1), ("le poulet", "o frango", "comida", 1),
    ("la viande", "a carne", "comida", 1), ("le poisson", "o peixe", "comida", 1), ("le riz", "o arroz", "comida", 1), ("les fruits", "as frutas", "comida", 1),
    ("le gâteau", "o bolo", "comida", 1), ("la glace", "o sorvete", "comida", 1), ("le petit-déjeuner", "o café da manhã", "comida", 1), ("le déjeuner", "o almoço", "comida", 1),
    ("le dîner", "o jantar", "comida", 1), ("le vin", "o vinho", "comida", 2), ("la bière", "a cerveja", "comida", 2), ("le croissant", "o croissant", "comida", 1),
    ("la baguette", "a baguete", "comida", 1), ("le beurre", "a manteiga", "comida", 2), ("le sucre", "o açúcar", "comida", 2), ("le jus", "o suco", "comida", 1),
    ("la maison", "a casa", "lugares", 1), ("l'école", "a escola", "lugares", 1), ("le marché", "o mercado", "lugares", 1), ("le restaurant", "o restaurante", "lugares", 1),
    ("l'hôpital", "o hospital", "lugares", 1), ("la plage", "a praia", "lugares", 1), ("la ville", "a cidade", "lugares", 1), ("la rue", "a rua", "lugares", 1),
    ("le magasin", "a loja", "lugares", 1), ("le parc", "o parque", "lugares", 1), ("la bibliothèque", "a biblioteca", "lugares", 1), ("le cinéma", "o cinema", "lugares", 1),
    ("l'aéroport", "o aeroporto", "lugares", 2), ("la gare", "a estação de trem", "lugares", 1), ("la banque", "o banco", "lugares", 2), ("la pharmacie", "a farmácia", "lugares", 1),
    ("le supermarché", "o supermercado", "lugares", 1), ("la boulangerie", "a padaria", "lugares", 1), ("le musée", "o museu", "lugares", 1), ("le bureau", "o escritório / a mesa", "lugares", 1),
    ("la poste", "o correio", "lugares", 2), ("le stade", "o estádio", "lugares", 2), ("le théâtre", "o teatro", "lugares", 2), ("la pâtisserie", "a confeitaria", "lugares", 2),
    ("aujourd'hui", "hoje", "tempo", 1), ("demain", "amanhã", "tempo", 1), ("hier", "ontem", "tempo", 1), ("maintenant", "agora", "tempo", 1), ("toujours", "sempre", "tempo", 1),
    ("jamais", "nunca", "tempo", 1), ("la semaine", "a semana", "tempo", 1), ("le mois", "o mês", "tempo", 1), ("l'année", "o ano", "tempo", 1), ("le jour", "o dia", "tempo", 1),
    ("la nuit", "a noite", "tempo", 1), ("le soir", "a noite (fim do dia)", "tempo", 1), ("le matin", "a manhã", "tempo", 1), ("le week-end", "o fim de semana", "tempo", 1),
    ("souvent", "frequentemente", "tempo", 2), ("déjà", "já", "tempo", 2), ("encore", "ainda / de novo", "tempo", 2), ("bientôt", "logo / em breve", "tempo", 2),
    ("le livre", "o livro", "objetos", 1), ("la table", "a mesa", "objetos", 1), ("la chaise", "a cadeira", "objetos", 1), ("la voiture", "o carro", "objetos", 1),
    ("le téléphone", "o telefone", "objetos", 1), ("la clé", "a chave", "objetos", 1), ("les vêtements", "as roupas", "objetos", 1), ("les chaussures", "os sapatos", "objetos", 1),
    ("la chemise", "a camisa", "objetos", 1), ("l'argent", "o dinheiro", "objetos", 1), ("l'ordinateur", "o computador", "objetos", 1), ("le sac", "a bolsa", "objetos", 1),
    ("les lunettes", "os óculos", "objetos", 2), ("la montre", "o relógio (de pulso)", "objetos", 2), ("le lit", "a cama", "objetos", 1), ("le journal", "o jornal", "objetos", 2),
    ("le billet", "o bilhete / ingresso", "objetos", 2), ("le film", "o filme", "objetos", 1), ("la chanson", "a canção", "objetos", 1), ("la lettre", "a carta", "objetos", 1),
    ("le soleil", "o sol", "natureza", 1), ("la pluie", "a chuva", "natureza", 1), ("la mer", "o mar", "natureza", 1), ("le chien", "o cachorro", "natureza", 1),
    ("le chat", "o gato", "natureza", 1), ("la montagne", "a montanha", "natureza", 2), ("l'arbre", "a árvore", "natureza", 2), ("la fleur", "a flor", "natureza", 1),
    ("la tête", "a cabeça", "corpo", 1), ("la main", "a mão", "corpo", 1), ("le pied", "o pé", "corpo", 1), ("les yeux", "os olhos", "corpo", 1), ("la bouche", "a boca", "corpo", 2),
    ("le ventre", "a barriga", "corpo", 2), ("le dos", "as costas", "corpo", 2), ("les cheveux", "o cabelo", "corpo", 2),
    ("le train", "o trem", "transporte", 1), ("le bus", "o ônibus", "transporte", 1), ("l'avion", "o avião", "transporte", 1), ("le métro", "o metrô", "transporte", 1),
    ("le vélo", "a bicicleta", "transporte", 1), ("le taxi", "o táxi", "transporte", 1),
    ("parler", "falar", "verbos", 1), ("manger", "comer", "verbos", 1), ("habiter", "morar", "verbos", 1), ("travailler", "trabalhar", "verbos", 1), ("étudier", "estudar", "verbos", 1),
    ("boire", "beber", "verbos", 1), ("écrire", "escrever", "verbos", 1), ("lire", "ler", "verbos", 1), ("acheter", "comprar", "verbos", 1), ("écouter", "escutar", "verbos", 1),
    ("regarder", "olhar / assistir", "verbos", 1), ("avoir", "ter", "verbos", 1), ("être", "ser / estar", "verbos", 1), ("aller", "ir", "verbos", 1), ("faire", "fazer", "verbos", 1),
    ("vouloir", "querer", "verbos", 1), ("pouvoir", "poder", "verbos", 1), ("venir", "vir", "verbos", 1), ("prendre", "pegar / tomar", "verbos", 1), ("sortir", "sair", "verbos", 1),
    ("dormir", "dormir", "verbos", 1), ("aimer", "amar / gostar", "verbos", 1), ("chercher", "procurar", "verbos", 2), ("attendre", "esperar", "verbos", 2), ("voyager", "viajar", "verbos", 2),
    ("chanter", "cantar", "verbos", 1), ("danser", "dançar", "verbos", 1), ("savoir", "saber", "verbos", 2), ("connaître", "conhecer", "verbos", 2), ("voir", "ver", "verbos", 1),
    ("grand", "grande", "adjetivos", 1), ("petit", "pequeno", "adjetivos", 1), ("bon", "bom", "adjetivos", 1), ("mauvais", "ruim", "adjetivos", 1), ("beau", "bonito", "adjetivos", 1),
    ("cher", "caro", "adjetivos", 1), ("nouveau", "novo", "adjetivos", 1), ("vieux", "velho", "adjetivos", 1), ("content", "contente", "adjetivos", 1), ("triste", "triste", "adjetivos", 1),
    ("fatigué", "cansado", "adjetivos", 1), ("facile", "fácil", "adjetivos", 2), ("difficile", "difícil", "adjetivos", 2), ("chaud", "quente", "adjetivos", 1), ("froid", "frio", "adjetivos", 1),
    ("rouge", "vermelho", "adjetivos", 1), ("jaune", "amarelo", "adjetivos", 1), ("bleu", "azul", "adjetivos", 1), ("vert", "verde", "adjetivos", 1), ("sympa", "simpático", "adjetivos", 1),
]

# Falsos amigos: (francês, significado real, armadilha)
FALSE_FRIENDS = [
    ("attendre", "esperar", "atender"), ("rester", "ficar", "restar"), ("rendre", "devolver", "render"), ("la tasse", "a xícara", "a taça"),
    ("sale", "sujo", "sala"), ("la salle", "a sala", "sal"), ("le crayon", "o lápis", "o crayon / giz de cera"), ("la boîte", "a caixa", "a boate"),
    ("le cadeau", "o presente", "o cadeado"), ("la cave", "o porão / a adega", "a cava"), ("la blague", "a piada", "a blague (bobagem)"),
    ("propre", "limpo / próprio", "apropriado"), ("la cour", "o pátio", "o couro"), ("la fois", "a vez", "a foice"), ("le coup", "o golpe", "o copo"),
    ("le collège", "a escola (fundamental II)", "a faculdade"), ("la journée", "o dia (duração)", "a jornada de trabalho"), ("le bureau", "o escritório / a mesa", "o bureau / guarda-roupa"),
    ("la ceinture", "o cinto", "a cintura"), ("les lunettes", "os óculos", "as lunetas"), ("la ville", "a cidade", "a vila"), ("le pôle", "o polo", "o pó"),
    ("débile", "idiota", "débil (fraco)"), ("exquis", "requintado / delicioso", "esquisito"), ("la place", "a praça / o lugar", "a placa"),
]

PERSONS = ["je", "tu", "il", "nous", "vous", "ils"]
PRESENT = {
    "être": ["suis", "es", "est", "sommes", "êtes", "sont"], "avoir": ["ai", "as", "a", "avons", "avez", "ont"],
    "aller": ["vais", "vas", "va", "allons", "allez", "vont"], "faire": ["fais", "fais", "fait", "faisons", "faites", "font"],
    "prendre": ["prends", "prends", "prend", "prenons", "prenez", "prennent"], "boire": ["bois", "bois", "boit", "buvons", "buvez", "boivent"],
    "lire": ["lis", "lis", "lit", "lisons", "lisez", "lisent"], "écrire": ["écris", "écris", "écrit", "écrivons", "écrivez", "écrivent"],
    "voir": ["vois", "vois", "voit", "voyons", "voyez", "voient"], "vouloir": ["veux", "veux", "veut", "voulons", "voulez", "veulent"],
    "pouvoir": ["peux", "peux", "peut", "pouvons", "pouvez", "peuvent"], "venir": ["viens", "viens", "vient", "venons", "venez", "viennent"],
    "sortir": ["sors", "sors", "sort", "sortons", "sortez", "sortent"], "dormir": ["dors", "dors", "dort", "dormons", "dormez", "dorment"],
    "attendre": ["attends", "attends", "attend", "attendons", "attendez", "attendent"], "acheter": ["achète", "achètes", "achète", "achetons", "achetez", "achètent"],
    "manger": ["mange", "manges", "mange", "mangeons", "mangez", "mangent"], "voyager": ["voyage", "voyages", "voyage", "voyageons", "voyagez", "voyagent"],
    "envoyer": ["envoie", "envoies", "envoie", "envoyons", "envoyez", "envoient"], "payer": ["paie", "paies", "paie", "payons", "payez", "paient"],
    "savoir": ["sais", "sais", "sait", "savons", "savez", "savent"], "connaître": ["connais", "connais", "connaît", "connaissons", "connaissez", "connaissent"],
    "finir": ["finis", "finis", "finit", "finissons", "finissez", "finissent"], "choisir": ["choisis", "choisis", "choisit", "choisissons", "choisissez", "choisissent"],
    "mettre": ["mets", "mets", "met", "mettons", "mettez", "mettent"], "partir": ["pars", "pars", "part", "partons", "partez", "partent"],
}
PARTICIPLE = {"être": "été", "avoir": "eu", "faire": "fait", "prendre": "pris", "boire": "bu", "lire": "lu", "écrire": "écrit", "voir": "vu",
              "vouloir": "voulu", "pouvoir": "pu", "attendre": "attendu", "dormir": "dormi", "savoir": "su", "connaître": "connu", "finir": "fini",
              "choisir": "choisi", "mettre": "mis", "envoyer": "envoyé", "payer": "payé"}
# Verbos para frases: (infinitivo, português, complemento, nível)
VERBS = [
    ("parler", "falar", "français", 1), ("travailler", "trabalhar", "à Paris", 1), ("étudier", "estudar", "le soir", 1), ("manger", "comer", "à la maison", 1),
    ("boire", "beber", "de l'eau", 1), ("habiter", "morar", "à Lyon", 1), ("écrire", "escrever", "un message", 1), ("lire", "ler", "le journal", 1),
    ("acheter", "comprar", "du pain", 1), ("écouter", "escutar", "de la musique", 1), ("regarder", "assistir", "la télé", 1), ("chanter", "cantar", "sous la douche", 1),
    ("danser", "dançar", "le samedi", 1), ("voyager", "viajar", "en train", 2), ("aimer", "gostar de", "le chocolat", 1), ("chercher", "procurar", "les clés", 2),
    ("avoir", "ter", "deux frères", 1), ("être", "ser", "brésilien", 1), ("aller", "ir", "au travail", 1), ("faire", "fazer", "les devoirs", 1),
    ("vouloir", "querer", "un café", 1), ("pouvoir", "poder", "venir", 1), ("venir", "vir", "à la fête", 1), ("prendre", "pegar", "le bus", 1),
    ("sortir", "sair", "avec des amis", 1), ("dormir", "dormir", "huit heures", 1), ("attendre", "esperar", "le train", 2), ("voir", "ver", "un film", 1),
    ("savoir", "saber", "la réponse", 2), ("connaître", "conhecer", "Paris", 2), ("finir", "terminar", "le travail", 2), ("choisir", "escolher", "un dessert", 2),
    ("mettre", "pôr", "la table", 2), ("partir", "partir / sair", "en vacances", 2), ("envoyer", "enviar", "un e-mail", 2), ("payer", "pagar", "l'addition", 2),
]

GRAMMAR = [
    ("___ pain est délicieux.", "Le", ["La", "Les", "L'"], "Pain é masculino → le.", 1, "artigos"),
    ("___ maison est grande.", "La", ["Le", "Les", "L'"], "Maison é feminino → la.", 1, "artigos"),
    ("___ école est fermée.", "L'", ["Le", "La", "Les"], "Antes de vogal, le/la viram l'.", 1, "artigos"),
    ("Je vais ___ cinéma.", "au", ["à le", "à la", "du"], "à + le = au.", 1, "contrações"),
    ("Je vais ___ plage.", "à la", ["au", "à l'", "aux"], "Plage é feminino → à la.", 1, "contrações"),
    ("Je viens ___ marché.", "du", ["de le", "au", "de la"], "de + le = du.", 1, "contrações"),
    ("Je bois ___ café.", "du", ["de la", "des", "au"], "Quantidade indefinida de algo masculino → partitivo du.", 2, "partitivo"),
    ("Je mange ___ salade.", "de la", ["du", "des", "au"], "Partitivo feminino → de la.", 2, "partitivo"),
    ("Je ne bois pas ___ café.", "de", ["du", "le", "des"], "Na negação, o partitivo vira de.", 2, "partitivo"),
    ("Je ___ brésilien.", "suis", ["es", "est", "ai"], "Être com je → suis.", 1, "être / avoir"),
    ("Elle ___ vingt ans.", "a", ["est", "as", "ont"], "Idade em francês usa avoir: elle a vingt ans.", 1, "être / avoir"),
    ("Nous ___ faim.", "avons", ["sommes", "avez", "ont"], "Fome: avoir faim.", 1, "être / avoir"),
    ("Il ___ fatigué.", "est", ["a", "es", "ai"], "Estado: être fatigué.", 1, "être / avoir"),
    ("Je ne ___ pas le français.", "parle", ["parles", "parlons", "parler"], "Negação: ne + verbo + pas.", 1, "negação"),
    ("Il n'___ pas de voiture.", "a", ["est", "ai", "as"], "Avoir na negação: il n'a pas de…", 1, "negação"),
    ("C'___ mon frère.", "est", ["a", "et", "es"], "C'est + pessoa/coisa.", 1, "c'est"),
    ("___ est médecin.", "Il", ["C'", "Ce", "Le"], "Profissão sem artigo: il est médecin (não c'est médecin).", 2, "c'est"),
    ("___ livre est intéressant.", "Ce", ["Cet", "Cette", "Ces"], "Demonstrativo masculino → ce.", 1, "demonstrativos"),
    ("___ ami est sympa.", "Cet", ["Ce", "Cette", "Ces"], "Masculino com vogal → cet.", 2, "demonstrativos"),
    ("___ maison est belle.", "Cette", ["Ce", "Cet", "Ces"], "Feminino → cette.", 1, "demonstrativos"),
    ("C'est ___ livre.", "mon", ["ma", "mes", "me"], "Livre é masculino → mon.", 1, "possessivos"),
    ("C'est ___ sœur.", "ma", ["mon", "mes", "me"], "Sœur é feminino → ma.", 1, "possessivos"),
    ("C'est ___ amie Julie.", "mon", ["ma", "mes", "m'"], "Antes de vogal usa-se mon, mesmo no feminino.", 2, "possessivos"),
    ("Ce sont ___ parents.", "mes", ["mon", "ma", "me"], "Plural → mes.", 1, "possessivos"),
    ("___ habites où ?", "Tu", ["Te", "Toi", "Ton"], "Sujeito → tu.", 1, "pronomes"),
    ("Il ___ appelle Paul.", "s'", ["se", "si", "c'"], "S'appeler: il s'appelle.", 1, "pronomes"),
    ("Je ___ appelle Marie.", "m'", ["me", "ma", "mon"], "Je m'appelle (elisão antes de vogal).", 1, "pronomes"),
    ("Demain, je vais ___ un gâteau.", "faire", ["fais", "fait", "faisons"], "Futur proche: aller + infinitivo.", 1, "futur proche"),
    ("Hier, j'___ mangé une pizza.", "ai", ["suis", "as", "a"], "Passé composé com avoir: j'ai mangé.", 2, "passé composé"),
    ("Hier, elle est ___ au cinéma.", "allée", ["allé", "aller", "allés"], "Aller usa être; concorda com o sujeito feminino: allée.", 2, "passé composé"),
    ("Nous sommes ___ à Paris.", "allés", ["allé", "allées", "aller"], "Être + participe concorda: nous (masc.) allés.", 2, "passé composé"),
    ("Il fait ___ aujourd'hui.", "beau", ["belle", "bon", "bien"], "Tempo bom: il fait beau.", 1, "tempo"),
    ("Il ___ froid.", "fait", ["est", "a", "va"], "Clima: il fait froid.", 1, "tempo"),
    ("Tu ___ quel âge ?", "as", ["es", "a", "est"], "Idade com avoir: tu as quel âge ?", 1, "perguntas"),
    ("___ est-ce que tu habites ?", "Où", ["Quand", "Qui", "Quoi"], "Lugar → où.", 1, "perguntas"),
    ("Je suis ___ France depuis un an.", "en", ["à", "au", "dans"], "Países femininos → en (en France).", 2, "preposições"),
    ("J'habite ___ Brésil.", "au", ["en", "à", "aux"], "Países masculinos → au (au Brésil).", 2, "preposições"),
    ("J'habite ___ Paris.", "à", ["en", "au", "dans"], "Cidades → à.", 1, "preposições"),
    ("Elle est plus grande ___ moi.", "que", ["de", "comme", "qui"], "Comparativo: plus … que.", 2, "comparação"),
    ("C'est le livre ___ je lis.", "que", ["qui", "où", "dont"], "Objeto do verbo na relativa → que.", 2, "relativos"),
    ("C'est l'homme ___ habite ici.", "qui", ["que", "où", "dont"], "Sujeito na relativa → qui.", 2, "relativos"),
]

NUMBERS = [
    ("quinze", "15", ["cinq", "cinquante", "quatorze"]), ("vingt", "20", ["douze", "trente", "deux"]), ("seize", "16", ["six", "soixante", "dix-six"]),
    ("trente et un", "31", ["trente-un", "treize", "trois cent un"]), ("soixante-dix", "70", ["septante (Bélgica)", "soixante", "dix-sept"]),
    ("quatre-vingts", "80", ["huitante", "quatre-vingt-dix", "quarante"]), ("quatre-vingt-dix", "90", ["neuf-vingts", "quatre-vingts", "dix-neuf"]),
    ("cent", "100", ["mille", "dix", "cents"]), ("mille", "1.000", ["un mille", "cent", "million"]), ("soixante-quinze", "75", ["septante-cinq", "soixante-cinq", "quinze"]),
    ("deux heures et demie", "2h30", ["deux heures et demi", "deux et demie heures", "demi deux"]), ("midi", "meio-dia", ["minuit", "midi et demie", "douze"]),
    ("lundi", "segunda-feira", ["mardi", "dimanche", "samedi"]), ("mercredi", "quarta-feira", ["mardi", "jeudi", "vendredi"]), ("janvier", "janeiro", ["juin", "juillet", "février"]),
    ("dix euros", "10 euros", ["deux euros", "douze euros", "cent euros"]), ("j'ai vingt ans", "tenho 20 anos", ["je suis vingt ans", "j'ai vingt", "je vingt ans"]),
    ("le premier mai", "1º de maio", ["le un mai", "mai premier", "le première mai"]), ("vingt-et-un", "21", ["vingt-un", "vingt et une", "douze"]),
    ("trois cents", "300", ["trois cent", "trente", "treize cents"]),
]

PHRASES = [
    ("Bonjour", "Bom dia / Olá", ""), ("Bonsoir", "Boa noite (cumprimento)", ""), ("Salut", "Oi / Tchau", "informal"), ("Ça va ?", "Tudo bem?", ""),
    ("Enchanté", "Muito prazer", ""), ("Merci", "Obrigado(a)", ""), ("De rien", "De nada", ""), ("Pardon", "Desculpe", ""), ("Excusez-moi", "Com licença", ""),
    ("S'il vous plaît", "Por favor", "formal"), ("Combien ça coûte ?", "Quanto custa?", ""), ("Où sont les toilettes ?", "Onde fica o banheiro?", ""),
    ("Je ne comprends pas", "Não entendo", ""), ("Vous pouvez répéter ?", "Pode repetir?", ""), ("Plus lentement, s'il vous plaît", "Mais devagar, por favor", ""),
    ("L'addition, s'il vous plaît", "A conta, por favor", ""), ("C'est délicieux !", "Está delicioso!", ""), ("Santé !", "Saúde! (brinde)", ""), ("Je t'aime", "Eu te amo", ""),
    ("Bon anniversaire !", "Feliz aniversário!", ""), ("À bientôt", "Até logo", ""), ("À demain", "Até amanhã", ""), ("Bon appétit !", "Bom apetite!", ""),
    ("Bonne nuit", "Boa noite (ao dormir)", ""), ("Pas de problème", "Sem problema", ""), ("Dommage !", "Que pena!", ""), ("D'accord", "Combinado / Concordo", ""),
    ("Quelle heure est-il ?", "Que horas são?", ""), ("Je m'appelle…", "Meu nome é…", ""), ("Au revoir", "Tchau / Até logo", ""),
]

# Frases com lacunas: sujeitos (texto, pessoa) e atividades
SUBJECTS = [("Je", 0), ("Tu", 1), ("Il", 2), ("Elle", 2), ("On", 2), ("Nous", 3), ("Vous", 4), ("Ils", 5), ("Elles", 5), ("Marie", 2), ("Paul", 2),
            ("Mon frère", 2), ("Ma sœur", 2), ("Mes amis", 5), ("Mes parents", 5), ("Le professeur", 2), ("La voisine", 2), ("Les enfants", 5),
            ("Lucas et moi", 3), ("Ton ami", 2), ("Sophie et Julie", 5), ("Mon père", 2), ("Ma mère", 2), ("Les étudiants", 5)]
# (verbo, objeto, gênero m/f/pl/v=vogal, lugar, gênero do lugar)
ACTIVITIES = [
    ("acheter", "pain", "m", "boulangerie", "f"), ("boire", "café", "m", "bar", "m"), ("manger", "pizza", "f", "restaurant", "m"),
    ("lire", "journal", "m", "bibliothèque", "f"), ("regarder", "film", "m", "cinéma", "m"), ("acheter", "fruits", "pl", "marché", "m"),
    ("acheter", "chemise", "f", "magasin", "m"), ("prendre", "train", "m", "gare", "f"), ("voir", "tableau", "m", "musée", "m"),
    ("manger", "glace", "f", "plage", "f"), ("acheter", "médicaments", "pl", "pharmacie", "f"), ("envoyer", "colis", "m", "poste", "f"),
    ("regarder", "match", "m", "stade", "m"), ("acheter", "billet", "m", "gare", "f"), ("boire", "thé", "m", "café", "m"),
    ("lire", "livre", "m", "parc", "m"), ("acheter", "gâteau", "m", "pâtisserie", "f"), ("chanter", "chanson", "f", "karaoké", "m"),
    ("prendre", "avion", "v", "aéroport", "v"), ("faire", "courses", "pl", "supermarché", "m"), ("manger", "sandwich", "m", "café", "m"),
    ("acheter", "fleurs", "pl", "marché", "m"), ("regarder", "spectacle", "m", "théâtre", "m"), ("écouter", "concert", "m", "parc", "m"),
    ("acheter", "journal", "m", "kiosque", "m"), ("chercher", "livre", "m", "librairie", "f"), ("commander", "dessert", "m", "restaurant", "m"),
    ("attendre", "bus", "m", "arrêt de bus", "v"), ("acheter", "baguette", "f", "boulangerie", "f"), ("boire", "jus", "m", "bar", "m"),
    ("voir", "exposition", "v", "musée", "m"), ("louer", "vélo", "m", "parc", "m"), ("manger", "croissant", "m", "café", "m"),
    ("acheter", "robe", "f", "magasin", "m"), ("lire", "magazine", "m", "café", "m"), ("prendre", "photo", "f", "plage", "f"),
    ("regarder", "série", "f", "hôtel", "v"), ("acheter", "fromage", "m", "marché", "m"), ("visiter", "château", "m", "village", "m"),
    ("payer", "addition", "v", "restaurant", "m"),
]

GUIDE = [
    ("Pronúncia para brasileiros", "Consoantes finais quase nunca soam (petit = “petí”). U é um “i” com bico; OU é o nosso “u”. Há vogais nasais (on, an, in). O R é de garganta. H é mudo."),
    ("Artigos", "le (masc.), la (fem.), l' (antes de vogal ou h mudo), les (plural). Indefinidos: un, une, des. Contrações: à + le = au, à + les = aux, de + le = du, de + les = des."),
    ("Partitivo", "Para quantidade indefinida: du pain, de la salade, de l'eau, des fruits. Na negação vira de: je ne mange pas de pain."),
    ("Être e avoir", "Être (suis, es, est, sommes, êtes, sont) e avoir (ai, as, a, avons, avez, ont). Idade, fome, sede e frio usam avoir: j'ai 20 ans, j'ai faim."),
    ("Presente", "-er: parle, parles, parle, parlons, parlez, parlent (a maioria soa igual!). Irregulares importantes: aller (vais…), faire (fais…), prendre (prends…), vouloir (veux…), pouvoir (peux…)."),
    ("Negação", "ne + verbo + pas: je ne parle pas. Antes de vogal: n' (je n'aime pas). Na fala informal o ne costuma cair."),
    ("Passé composé", "avoir/être + particípio: j'ai mangé, j'ai lu, j'ai pris. Verbos de movimento (aller, venir, partir, arriver…) usam être e concordam: elle est allée, nous sommes partis."),
    ("Futur proche", "aller + infinitivo: je vais manger, nous allons partir."),
    ("Imparfait", "Hábitos e descrições no passado: radical de nous + ais, ais, ait, ions, iez, aient (nous parlons → je parlais). Être: j'étais."),
    ("Preposições de lugar", "Cidades: à (à Paris). Países femininos: en (en France). Masculinos: au (au Brésil). Plural: aux (aux États-Unis)."),
    ("C'est × il est", "C'est + artigo/nome: c'est mon frère, c'est un médecin. Il est + adjetivo ou profissão sem artigo: il est médecin, il est sympa."),
    ("Possessivos e demonstrativos", "mon/ma/mes, ton/ta/tes, son/sa/ses (antes de vogal: mon amie). Ce/cet/cette/ces: ce livre, cet ami, cette maison."),
    ("Falsos amigos", "attendre = esperar; rester = ficar; rendre = devolver; la tasse = xícara; sale = sujo; le cadeau = presente; la boîte = caixa."),
]
