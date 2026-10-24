"""Conteúdo do Spanish Routine (espanhol, A1–A2), pensado para quem fala português.

Conjugações: regulares por regra + tabela de irregulares revisada. Variante peninsular
e latino-americana são aceitas; vosotros aparece só nas tabelas, não nos exercícios.
Revisão por professor ou falante nativo recomendada antes da venda.
"""

# ------------------------------------------------------------------ pronúncia
SOUNDS = [
    ("ñ", "nh", "niño", "como “nh” em “ninho”"), ("ll", "lh / j", "llamar", "na maior parte da América soa como “j” suave (ou “lh”)"),
    ("y", "i / j", "yo", "antes de vogal soa parecido com “j” suave"), ("j", "rr aspirado", "jamón", "som forte da garganta, como o “rr” carioca"),
    ("ge / gi", "rr aspirado", "gente", "g antes de e/i soa como j"), ("h", "muda", "hola", "nunca se pronuncia"),
    ("rr", "r vibrante", "perro", "a língua vibra várias vezes"), ("r", "r fraco", "pero", "como em “caro”; no começo da palavra vibra"),
    ("z", "s / th", "zapato", "“s” na América; “th” inglês na Espanha"), ("ce / ci", "s / th", "cena", "igual ao z"),
    ("v", "b", "vino", "v e b soam igual (b suave)"), ("ch", "tch", "chico", "como “tch” em “tchau”"),
    ("qu", "k", "queso", "o u não soa: “keso”"), ("gue / gui", "gue", "guitarra", "o u não soa"), ("güe / güi", "güe", "pingüino", "com trema o u soa"),
    ("d final", "d leve", "ciudad", "d entre vogais e no fim é bem suave"), ("o / e finais", "o / e", "como", "não viram u/i como no português: “como”, não “comu”"),
]

# ------------------------------------------------------------------ vocabulário
# (espanhol, português, tema, nível)
VOCAB = [
    # pessoas
    ("la madre", "a mãe", "pessoas", 1), ("el padre", "o pai", "pessoas", 1), ("el hermano", "o irmão", "pessoas", 1), ("la hermana", "a irmã", "pessoas", 1),
    ("el hijo", "o filho", "pessoas", 1), ("la hija", "a filha", "pessoas", 1), ("el abuelo", "o avô", "pessoas", 1), ("la abuela", "a avó", "pessoas", 1),
    ("el amigo", "o amigo", "pessoas", 1), ("la novia", "a namorada", "pessoas", 1), ("el niño", "o menino", "pessoas", 1), ("la mujer", "a mulher", "pessoas", 1),
    ("el hombre", "o homem", "pessoas", 1), ("el profesor", "o professor", "pessoas", 1), ("el médico", "o médico", "pessoas", 1), ("el camarero", "o garçom", "pessoas", 2),
    ("el primo", "o primo", "pessoas", 2), ("el tío", "o tio", "pessoas", 2), ("el vecino", "o vizinho", "pessoas", 2), ("el jefe", "o chefe", "pessoas", 2),
    # comida
    ("el pan", "o pão", "comida", 1), ("el agua", "a água", "comida", 1), ("la leche", "o leite", "comida", 1), ("el café", "o café", "comida", 1),
    ("el queso", "o queijo", "comida", 1), ("la manzana", "a maçã", "comida", 1), ("el huevo", "o ovo", "comida", 1), ("el pollo", "o frango", "comida", 1),
    ("la carne", "a carne", "comida", 1), ("el pescado", "o peixe (comida)", "comida", 1), ("el arroz", "o arroz", "comida", 1), ("la fruta", "a fruta", "comida", 1),
    ("el jamón", "o presunto", "comida", 2), ("la cena", "o jantar", "comida", 1), ("el desayuno", "o café da manhã", "comida", 1), ("el almuerzo", "o almoço", "comida", 1),
    ("la cerveza", "a cerveja", "comida", 2), ("el vino", "o vinho", "comida", 2), ("la ensalada", "a salada", "comida", 2), ("el zumo", "o suco (Espanha)", "comida", 2),
    ("la mantequilla", "a manteiga", "comida", 2), ("el azúcar", "o açúcar", "comida", 2), ("la galleta", "o biscoito", "comida", 2),
    # lugares
    ("la casa", "a casa", "lugares", 1), ("la escuela", "a escola", "lugares", 1), ("el mercado", "o mercado", "lugares", 1), ("el restaurante", "o restaurante", "lugares", 1),
    ("el hospital", "o hospital", "lugares", 1), ("la playa", "a praia", "lugares", 1), ("la ciudad", "a cidade", "lugares", 1), ("la calle", "a rua", "lugares", 1),
    ("la tienda", "a loja", "lugares", 1), ("el parque", "o parque", "lugares", 1), ("la biblioteca", "a biblioteca", "lugares", 1), ("el cine", "o cinema", "lugares", 1),
    ("el aeropuerto", "o aeroporto", "lugares", 2), ("la estación", "a estação", "lugares", 2), ("el banco", "o banco", "lugares", 2), ("la farmacia", "a farmácia", "lugares", 2),
    ("el supermercado", "o supermercado", "lugares", 2), ("la panadería", "a padaria", "lugares", 2), ("el museo", "o museu", "lugares", 2), ("el pueblo", "a cidadezinha / o povo", "lugares", 2),
    # tempo
    ("hoy", "hoje", "tempo", 1), ("mañana", "amanhã", "tempo", 1), ("ayer", "ontem", "tempo", 1), ("ahora", "agora", "tempo", 1), ("siempre", "sempre", "tempo", 1),
    ("nunca", "nunca", "tempo", 1), ("la semana", "a semana", "tempo", 1), ("el mes", "o mês", "tempo", 1), ("el año", "o ano", "tempo", 1), ("el día", "o dia", "tempo", 1),
    ("la noche", "a noite", "tempo", 1), ("la tarde", "a tarde", "tempo", 1), ("temprano", "cedo", "tempo", 2), ("tarde", "tarde (adv.)", "tempo", 2),
    ("el fin de semana", "o fim de semana", "tempo", 1), ("todavía", "ainda", "tempo", 2), ("ya", "já", "tempo", 2), ("pronto", "logo / em breve", "tempo", 2),
    # objetos
    ("el libro", "o livro", "objetos", 1), ("la mesa", "a mesa", "objetos", 1), ("la silla", "a cadeira", "objetos", 1), ("el coche", "o carro (Espanha)", "objetos", 1),
    ("el teléfono", "o telefone", "objetos", 1), ("la llave", "a chave", "objetos", 1), ("la ropa", "a roupa", "objetos", 1), ("los zapatos", "os sapatos", "objetos", 1),
    ("la camisa", "a camisa", "objetos", 1), ("el dinero", "o dinheiro", "objetos", 1), ("el ordenador", "o computador (Espanha)", "objetos", 2), ("la mochila", "a mochila", "objetos", 2),
    ("las gafas", "os óculos", "objetos", 2), ("el reloj", "o relógio", "objetos", 2), ("la cama", "a cama", "objetos", 1), ("el periódico", "o jornal", "objetos", 2),
    ("la entrada", "o ingresso / a entrada", "objetos", 2), ("la película", "o filme", "objetos", 1), ("la canción", "a canção", "objetos", 1), ("la carta", "a carta", "objetos", 1),
    # natureza e corpo
    ("el sol", "o sol", "natureza", 1), ("la lluvia", "a chuva", "natureza", 1), ("el mar", "o mar", "natureza", 1), ("el perro", "o cachorro (cão)", "natureza", 1),
    ("el gato", "o gato", "natureza", 1), ("la montaña", "a montanha", "natureza", 2), ("el árbol", "a árvore", "natureza", 2), ("la flor", "a flor", "natureza", 1),
    ("la cabeza", "a cabeça", "corpo", 1), ("la mano", "a mão", "corpo", 1), ("el pie", "o pé", "corpo", 1), ("los ojos", "os olhos", "corpo", 1), ("la boca", "a boca", "corpo", 2),
    ("el estómago", "o estômago", "corpo", 2), ("la espalda", "as costas", "corpo", 2), ("el pelo", "o cabelo", "corpo", 2),
    # transporte
    ("el tren", "o trem", "transporte", 1), ("el autobús", "o ônibus", "transporte", 1), ("el avión", "o avião", "transporte", 1), ("el metro", "o metrô", "transporte", 1),
    ("la bicicleta", "a bicicleta", "transporte", 1), ("el billete", "a passagem (Espanha)", "transporte", 2), ("el boleto", "a passagem (América)", "transporte", 2),
    # verbos
    ("hablar", "falar", "verbos", 1), ("comer", "comer", "verbos", 1), ("vivir", "morar / viver", "verbos", 1), ("trabajar", "trabalhar", "verbos", 1),
    ("estudiar", "estudar", "verbos", 1), ("beber", "beber", "verbos", 1), ("escribir", "escrever", "verbos", 1), ("leer", "ler", "verbos", 1),
    ("comprar", "comprar", "verbos", 1), ("escuchar", "escutar", "verbos", 1), ("mirar", "olhar", "verbos", 1), ("tener", "ter", "verbos", 1),
    ("querer", "querer", "verbos", 1), ("poder", "poder", "verbos", 1), ("hacer", "fazer", "verbos", 1), ("ir", "ir", "verbos", 1), ("venir", "vir", "verbos", 1),
    ("salir", "sair", "verbos", 1), ("dormir", "dormir", "verbos", 1), ("jugar", "jogar / brincar", "verbos", 1), ("llegar", "chegar", "verbos", 2),
    ("llamar", "chamar / ligar", "verbos", 2), ("llevar", "levar / usar (roupa)", "verbos", 2), ("buscar", "procurar / buscar", "verbos", 2), ("pagar", "pagar", "verbos", 2),
    ("esperar", "esperar", "verbos", 2), ("ayudar", "ajudar", "verbos", 2), ("viajar", "viajar", "verbos", 2), ("cocinar", "cozinhar", "verbos", 2), ("bailar", "dançar", "verbos", 2),
    ("cantar", "cantar", "verbos", 1), ("conocer", "conhecer", "verbos", 2), ("saber", "saber", "verbos", 2), ("pensar", "pensar", "verbos", 2), ("empezar", "começar", "verbos", 2),
    ("volver", "voltar", "verbos", 2), ("pedir", "pedir", "verbos", 2), ("decir", "dizer", "verbos", 2), ("ducharse", "tomar banho (chuveiro)", "verbos", 2),
    ("levantarse", "levantar-se", "verbos", 2), ("acostarse", "deitar-se", "verbos", 2),
    # adjetivos
    ("grande", "grande", "adjetivos", 1), ("pequeño", "pequeno", "adjetivos", 1), ("bueno", "bom", "adjetivos", 1), ("malo", "ruim / mau", "adjetivos", 1),
    ("bonito", "bonito", "adjetivos", 1), ("feo", "feio", "adjetivos", 1), ("caro", "caro", "adjetivos", 1), ("barato", "barato", "adjetivos", 1),
    ("nuevo", "novo", "adjetivos", 1), ("viejo", "velho", "adjetivos", 1), ("feliz", "feliz", "adjetivos", 1), ("triste", "triste", "adjetivos", 1),
    ("cansado", "cansado", "adjetivos", 1), ("rico", "rico / gostoso", "adjetivos", 1), ("fácil", "fácil", "adjetivos", 2), ("difícil", "difícil", "adjetivos", 2),
    ("alto", "alto", "adjetivos", 1), ("bajo", "baixo", "adjetivos", 1), ("rojo", "vermelho", "adjetivos", 1), ("amarillo", "amarelo", "adjetivos", 1),
    ("lleno", "cheio", "adjetivos", 2), ("vacío", "vazio", "adjetivos", 2), ("guapo", "bonito (pessoa)", "adjetivos", 2), ("simpático", "simpático", "adjetivos", 1),
]

# Falsos amigos: (espanhol, significado real, armadilha em português)
FALSE_FRIENDS = [
    ("embarazada", "grávida", "embaraçada"), ("exquisito", "delicioso", "esquisito"), ("la oficina", "o escritório", "a oficina"),
    ("el polvo", "o pó", "o polvo"), ("un rato", "um momento, pouco tempo", "um rato"), ("salado", "salgado", "salada"),
    ("el apellido", "o sobrenome", "o apelido"), ("borracho", "bêbado", "de borracha"), ("largo", "comprido", "largo"),
    ("el pelo", "o cabelo", "o pelo do corpo"), ("la cena", "o jantar", "a cena"), ("el sitio", "o lugar", "o sítio (chácara)"),
    ("el taller", "a oficina mecânica", "o talher"), ("el vaso", "o copo", "o vaso de flores"), ("zurdo", "canhoto", "surdo"),
    ("brincar", "pular", "brincar"), ("el cachorro", "o filhote", "o cachorro adulto"), ("el aceite", "o azeite / óleo", "o aceite"),
    ("la copa", "a taça", "a copa (cômodo)"), ("la escoba", "a vassoura", "a escova"), ("la firma", "a assinatura", "a firma (empresa)"),
    ("la grasa", "a gordura", "a graça"), ("el presunto", "o suposto (adj.)", "o presunto"), ("rojo", "vermelho", "roxo"),
    ("la sobremesa", "a conversa à mesa após a refeição", "a sobremesa (doce)"), ("tirar", "jogar fora / atirar", "tirar"),
    ("todavía", "ainda", "todavia"), ("la pastilla", "o comprimido", "a pastilha"), ("el berro", "o agrião", "o berro"),
    ("el balcón", "a sacada / varanda", "o balcão de loja"), ("acordarse", "lembrar-se", "acordar"), ("la propina", "a gorjeta", "a propina"),
    ("contestar", "responder", "contestar"), ("la cola", "a fila", "a cola"), ("el ratón", "o camundongo / mouse", "o ratão"),
]

# Verbos para conjugar: (infinitivo, português, complemento, nível)
VERBS = [
    ("hablar", "falar", "español", 1), ("trabajar", "trabalhar", "en una oficina", 1), ("estudiar", "estudar", "por la noche", 1),
    ("comer", "comer", "en casa", 1), ("beber", "beber", "agua", 1), ("vivir", "morar", "en Madrid", 1), ("escribir", "escrever", "un correo", 1),
    ("leer", "ler", "el periódico", 1), ("comprar", "comprar", "pan", 1), ("escuchar", "escutar", "música", 1), ("cocinar", "cozinhar", "pasta", 2),
    ("viajar", "viajar", "en tren", 2), ("bailar", "dançar", "salsa", 2), ("cantar", "cantar", "en la ducha", 1), ("llegar", "chegar", "tarde", 2),
    ("tener", "ter", "dos hermanos", 1), ("ser", "ser", "de Brasil", 1), ("estar", "estar", "en casa", 1), ("ir", "ir", "al trabajo", 1),
    ("hacer", "fazer", "los deberes", 1), ("poder", "poder", "venir", 1), ("querer", "querer", "un café", 1), ("venir", "vir", "a la fiesta", 1),
    ("salir", "sair", "con amigos", 1), ("dormir", "dormir", "ocho horas", 1), ("jugar", "jogar", "al fútbol", 1), ("pensar", "pensar", "en ti", 2),
    ("volver", "voltar", "a casa", 2), ("pedir", "pedir", "la cuenta", 2), ("decir", "dizer", "la verdad", 2), ("conocer", "conhecer", "a Pedro", 2),
    ("saber", "saber", "la respuesta", 2), ("empezar", "começar", "a las nueve", 2), ("ver", "ver", "la tele", 1), ("dar", "dar", "un regalo", 2),
    ("poner", "pôr", "la mesa", 2), ("abrir", "abrir", "la ventana", 1), ("cerrar", "fechar", "la puerta", 2), ("tomar", "tomar", "un té", 1),
]
SUBJECTS = [("yo", 0), ("tú", 1), ("él", 2), ("ella", 2), ("usted", 2), ("nosotros", 3), ("ellos", 5), ("ustedes", 5)]

# Irregulares: presente e pretérito indefinido nas pessoas yo, tú, él, nosotros, vosotros, ellos.
IRREGULAR_PRESENT = {
    "ser": ["soy", "eres", "es", "somos", "sois", "son"], "estar": ["estoy", "estás", "está", "estamos", "estáis", "están"],
    "tener": ["tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen"], "ir": ["voy", "vas", "va", "vamos", "vais", "van"],
    "hacer": ["hago", "haces", "hace", "hacemos", "hacéis", "hacen"], "poder": ["puedo", "puedes", "puede", "podemos", "podéis", "pueden"],
    "querer": ["quiero", "quieres", "quiere", "queremos", "queréis", "quieren"], "venir": ["vengo", "vienes", "viene", "venimos", "venís", "vienen"],
    "salir": ["salgo", "sales", "sale", "salimos", "salís", "salen"], "dormir": ["duermo", "duermes", "duerme", "dormimos", "dormís", "duermen"],
    "jugar": ["juego", "juegas", "juega", "jugamos", "jugáis", "juegan"], "pensar": ["pienso", "piensas", "piensa", "pensamos", "pensáis", "piensan"],
    "volver": ["vuelvo", "vuelves", "vuelve", "volvemos", "volvéis", "vuelven"], "pedir": ["pido", "pides", "pide", "pedimos", "pedís", "piden"],
    "decir": ["digo", "dices", "dice", "decimos", "decís", "dicen"], "conocer": ["conozco", "conoces", "conoce", "conocemos", "conocéis", "conocen"],
    "saber": ["sé", "sabes", "sabe", "sabemos", "sabéis", "saben"], "empezar": ["empiezo", "empiezas", "empieza", "empezamos", "empezáis", "empiezan"],
    "ver": ["veo", "ves", "ve", "vemos", "veis", "ven"], "dar": ["doy", "das", "da", "damos", "dais", "dan"],
    "poner": ["pongo", "pones", "pone", "ponemos", "ponéis", "ponen"], "cerrar": ["cierro", "cierras", "cierra", "cerramos", "cerráis", "cierran"],
}
IRREGULAR_PAST = {
    "ser": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"], "ir": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
    "estar": ["estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron"], "tener": ["tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"],
    "hacer": ["hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron"], "poder": ["pude", "pudiste", "pudo", "pudimos", "pudisteis", "pudieron"],
    "querer": ["quise", "quisiste", "quiso", "quisimos", "quisisteis", "quisieron"], "venir": ["vine", "viniste", "vino", "vinimos", "vinisteis", "vinieron"],
    "decir": ["dije", "dijiste", "dijo", "dijimos", "dijisteis", "dijeron"], "saber": ["supe", "supiste", "supo", "supimos", "supisteis", "supieron"],
    "poner": ["puse", "pusiste", "puso", "pusimos", "pusisteis", "pusieron"], "dar": ["di", "diste", "dio", "dimos", "disteis", "dieron"],
    "ver": ["vi", "viste", "vio", "vimos", "visteis", "vieron"], "dormir": ["dormí", "dormiste", "durmió", "dormimos", "dormisteis", "durmieron"],
    "pedir": ["pedí", "pediste", "pidió", "pedimos", "pedisteis", "pidieron"], "leer": ["leí", "leíste", "leyó", "leímos", "leísteis", "leyeron"],
    "llegar": ["llegué", "llegaste", "llegó", "llegamos", "llegasteis", "llegaron"], "jugar": ["jugué", "jugaste", "jugó", "jugamos", "jugasteis", "jugaron"],
    "empezar": ["empecé", "empezaste", "empezó", "empezamos", "empezasteis", "empezaron"], "pagar": ["pagué", "pagaste", "pagó", "pagamos", "pagasteis", "pagaron"],
    "buscar": ["busqué", "buscaste", "buscó", "buscamos", "buscasteis", "buscaron"],
}

# Gramática: (frase com ___, resposta, distratores, explicação, nível, tema)
GRAMMAR = [
    # ser × estar
    ("Mi hermana ___ médica.", "es", ["está", "hay", "tiene"], "Profissão → ser.", 1, "ser × estar"),
    ("Hoy ___ muy cansado.", "estoy", ["soy", "hay", "tengo"], "Estado passageiro → estar.", 1, "ser × estar"),
    ("Madrid ___ en España.", "está", ["es", "hay", "son"], "Localização → estar.", 1, "ser × estar"),
    ("Nosotros ___ brasileños.", "somos", ["estamos", "hay", "tenemos"], "Nacionalidade → ser.", 1, "ser × estar"),
    ("La fiesta ___ el sábado.", "es", ["está", "hay", "tiene"], "Evento (quando/onde acontece) → ser.", 2, "ser × estar"),
    ("La sopa ___ fría.", "está", ["es", "hay", "tiene"], "Estado no momento → estar.", 2, "ser × estar"),
    ("¿Dónde ___ el baño?", "está", ["es", "hay", "son"], "Onde está algo determinado → estar.", 1, "ser × estar"),
    ("Mis padres ___ muy simpáticos.", "son", ["están", "hay", "tienen"], "Característica → ser.", 1, "ser × estar"),
    # hay × está
    ("En mi calle ___ una farmacia.", "hay", ["está", "es", "tiene"], "Existência (algo indefinido: una) → hay.", 1, "hay × está"),
    ("La farmacia ___ al lado del banco.", "está", ["hay", "es", "tiene"], "Localização de algo definido (la) → está.", 1, "hay × está"),
    ("¿___ un supermercado cerca?", "Hay", ["Está", "Es", "Son"], "Existência → hay.", 1, "hay × está"),
    # gustar
    ("A mí me ___ el chocolate.", "gusta", ["gustan", "gusto", "gustas"], "Gustar concorda com o que agrada (singular) → gusta.", 1, "gustar"),
    ("A mí me ___ los gatos.", "gustan", ["gusta", "gusto", "gustamos"], "O que agrada é plural → gustan.", 1, "gustar"),
    ("¿A ti te ___ bailar?", "gusta", ["gustas", "gustan", "gusto"], "Com verbo no infinitivo → gusta.", 1, "gustar"),
    ("A nosotros ___ gusta viajar.", "nos", ["nosotros", "me", "les"], "A nosotros → nos gusta.", 2, "gustar"),
    ("A ellos ___ gustan las películas de terror.", "les", ["los", "le", "se"], "A ellos → les gusta(n).", 2, "gustar"),
    # muy × mucho
    ("Este libro es ___ interesante.", "muy", ["mucho", "mucha", "muchos"], "Antes de adjetivo → muy.", 1, "muy × mucho"),
    ("Hoy hace ___ calor.", "mucho", ["muy", "mucha", "muchos"], "Antes de substantivo masculino → mucho.", 1, "muy × mucho"),
    ("Tengo ___ hambre.", "mucha", ["muy", "mucho", "muchas"], "Hambre é feminino → mucha.", 2, "muy × mucho"),
    ("Él trabaja ___.", "mucho", ["muy", "mucha", "muchos"], "Depois do verbo → mucho.", 1, "muy × mucho"),
    # artigos e contrações
    ("Voy ___ cine.", "al", ["a el", "del", "en el"], "a + el → al.", 1, "artigos"),
    ("Vengo ___ mercado.", "del", ["de el", "al", "en el"], "de + el → del.", 1, "artigos"),
    ("___ agua está fría.", "El", ["La", "Lo", "Las"], "Agua é feminino, mas usa el no singular (a tônico).", 2, "artigos"),
    ("___ importante es estudiar.", "Lo", ["El", "La", "Los"], "Lo + adjetivo = “o que é”.", 2, "artigos"),
    ("Me duele ___ cabeza.", "la", ["el", "lo", "las"], "Partes do corpo com doler → artigo, não possessivo.", 2, "artigos"),
    # por × para
    ("Este regalo es ___ ti.", "para", ["por", "a", "de"], "Destinatário → para.", 2, "por × para"),
    ("Gracias ___ tu ayuda.", "por", ["para", "de", "a"], "Motivo → por.", 2, "por × para"),
    ("Estudio ___ ser médico.", "para", ["de", "a", "en"], "Finalidade → para.", 2, "por × para"),
    ("Te llamo ___ teléfono.", "por", ["para", "de", "en"], "Meio (por telefone) → por.", 2, "por × para"),
    # pronomes e outros
    ("___ llamo Ana.", "Me", ["Mi", "Yo", "Se"], "Llamarse: me llamo.", 1, "pronomes"),
    ("Mi hermano ___ llama Juan.", "se", ["me", "te", "le"], "Él se llama.", 1, "pronomes"),
    ("¿Cómo ___ llamas?", "te", ["tu", "se", "me"], "Tú te llamas.", 1, "pronomes"),
    ("Esta es ___ casa.", "mi", ["me", "mí", "mío"], "Possessivo antes do substantivo → mi (sem acento).", 1, "pronomes"),
    ("Este libro es para ___.", "mí", ["mi", "me", "yo"], "Depois de preposição → mí (com acento).", 2, "pronomes"),
    ("¿___ años tienes?", "Cuántos", ["Cuánto", "Qué", "Cómo"], "Años é masculino plural → cuántos.", 1, "perguntas"),
    ("¿___ vives?", "Dónde", ["Qué", "Cuándo", "Cuál"], "Lugar → dónde.", 1, "perguntas"),
    ("Voy a ___ una pizza esta noche.", "comer", ["como", "comí", "comiendo"], "Ir a + infinitivo = futuro próximo.", 1, "futuro"),
    ("Mañana ___ a llover.", "va", ["vas", "voy", "van"], "Ir a + infinitivo; sujeito implícito (o tempo) → va.", 1, "futuro"),
    ("Ahora estoy ___ la cena.", "preparando", ["preparado", "prepara", "preparar"], "Estar + gerúndio (-ando/-iendo).", 2, "gerúndio"),
    ("Ellos están ___ la tele.", "viendo", ["vendo", "visto", "ver"], "Ver → viendo.", 2, "gerúndio"),
    ("Hace dos años que ___ en Madrid.", "vivo", ["vivir", "viví", "vive"], "Hace … que + presente: algo que continua.", 2, "tempo"),
    ("Tengo ___ estudiar para el examen.", "que", ["de", "a", "por"], "Obrigação: tener que + infinitivo.", 1, "obrigação"),
]

NUMBERS = [
    ("quince", "15", ["cinco", "cincuenta", "quinientos"]), ("veinte", "20", ["doce", "treinta", "dos"]), ("dieciséis", "16", ["dieciseis", "seis", "sesenta"]),
    ("treinta y uno", "31", ["trece", "trescientos uno", "treinta uno"]), ("cien", "100", ["ciento", "mil", "diez"]), ("ciento veinte", "120", ["cien veinte", "doce", "veinte cien"]),
    ("quinientos", "500", ["cincocientos", "cincuenta", "quince"]), ("setecientos", "700", ["sietecientos", "setenta", "diecisiete"]), ("mil", "1.000", ["un mil", "cien", "millón"]),
    ("primero", "primeiro", ["uno", "primo", "primer día"]), ("las tres y media", "3h30", ["las tres y treinta y medio", "la tres media", "tres horas media"]),
    ("la una", "1h", ["las una", "el uno", "la primera"]), ("las dos y cuarto", "2h15", ["las dos y quince cuarto", "dos cuarto", "las dos menos cuarto"]),
    ("las cinco menos cuarto", "4h45", ["las cinco y cuarto", "las cuatro menos cuarto", "las cuatro y cuarto"]), ("el lunes", "segunda-feira", ["el martes", "el domingo", "el sábado"]),
    ("el miércoles", "quarta-feira", ["el martes", "el jueves", "el viernes"]), ("enero", "janeiro", ["junio", "julio", "febrero"]),
    ("diez euros", "10 euros", ["dos euros", "doce euros", "cien euros"]), ("tengo veinte años", "tenho 20 anos", ["soy veinte años", "estoy veinte años", "tengo veinte año"]),
    ("el primero de mayo", "1º de maio", ["el uno mayo", "mayo primero", "el primer mayo de"]),
]

PHRASES = [
    ("Hola", "Olá", ""), ("Buenos días", "Bom dia", ""), ("Buenas noches", "Boa noite", ""), ("¿Qué tal?", "Tudo bem?", "informal"),
    ("Mucho gusto", "Muito prazer", ""), ("Gracias", "Obrigado(a)", ""), ("De nada", "De nada", ""), ("Perdón", "Desculpe", ""),
    ("Lo siento", "Sinto muito", ""), ("Por favor", "Por favor", ""), ("¿Cuánto cuesta?", "Quanto custa?", ""), ("¿Dónde está el baño?", "Onde fica o banheiro?", ""),
    ("No entiendo", "Não entendo", ""), ("¿Puede repetir, por favor?", "Pode repetir, por favor?", ""), ("Más despacio, por favor", "Mais devagar, por favor", ""),
    ("La cuenta, por favor", "A conta, por favor", ""), ("¡Qué rico!", "Que gostoso!", ""), ("¡Salud!", "Saúde! (brinde)", ""), ("Te quiero", "Eu te amo", "afetivo"),
    ("¡Feliz cumpleaños!", "Feliz aniversário!", ""), ("Hasta luego", "Até logo", ""), ("Hasta mañana", "Até amanhã", ""), ("¡Buen provecho!", "Bom apetite!", ""),
    ("¿Me ayuda, por favor?", "Pode me ajudar, por favor?", ""), ("No pasa nada", "Não tem problema", ""), ("¡Qué pena!", "Que pena!", ""), ("Estoy de acuerdo", "Concordo", ""),
    ("¡Vale!", "Ok! / Combinado! (Espanha)", "Espanha"), ("¿Qué hora es?", "Que horas são?", ""), ("Me llamo…", "Meu nome é…", ""),
]

# Completar (2–3 lacunas): sujeitos (texto, pessoa) e atividades
COMBO_SUBJECTS = [("Yo", 0), ("Tú", 1), ("Él", 2), ("Ella", 2), ("Usted", 2), ("Nosotros", 3), ("Ellos", 5), ("Ustedes", 5),
                  ("Mi madre", 2), ("Mis amigos", 5), ("Ana y yo", 3), ("Mi hermano", 2)]
# (verbo, objeto, gênero do objeto, lugar, gênero do lugar)
COMBO_ACTIVITIES = [
    ("comprar", "pan", "m", "panadería", "f"), ("beber", "café", "m", "cafetería", "f"), ("comer", "paella", "f", "restaurante", "m"),
    ("leer", "libro", "m", "biblioteca", "f"), ("ver", "película", "f", "cine", "m"), ("escribir", "carta", "f", "oficina", "f"),
    ("estudiar", "lección", "f", "escuela", "f"), ("comprar", "fruta", "f", "mercado", "m"), ("comprar", "camisa", "f", "tienda", "f"),
    ("preparar", "cena", "f", "cocina", "f"), ("comprar", "periódico", "m", "quiosco", "m"), ("tomar", "té", "m", "bar", "m"),
    ("lavar", "coche", "m", "garaje", "m"), ("comprar", "entrada", "f", "taquilla", "f"), ("ver", "partido", "m", "estadio", "m"),
    ("leer", "revista", "f", "tren", "m"), ("cantar", "canción", "f", "karaoke", "m"), ("escuchar", "música", "f", "coche", "m"),
    ("comer", "ensalada", "f", "parque", "m"), ("buscar", "llave", "f", "casa", "f"),
]

GUIDE = [
    ("Pronúncia para brasileiros", "O e o finais não viram “i” e “u”: como = “como”. H é muda (hola = “ola”). J e g antes de e/i soam aspirados. LL e Y soam como um “j” suave na maior parte da América. V e B soam igual."),
    ("Artigos", "el (masc.), la (fem.), los, las. Contrações: a + el = al (voy al cine), de + el = del. Lo + adjetivo = “o que é” (lo bueno). Agua, alma, águila: el no singular por começarem com a tônico."),
    ("Ser × estar", "Ser: identidade, profissão, nacionalidade, características, horas e eventos (la fiesta es en mi casa). Estar: localização, estados passageiros e resultado (estoy cansado, la sopa está fría)."),
    ("Hay × está", "Hay = existe (com um/una ou sem artigo): hay un banco aquí. Está = onde fica algo definido: el banco está aquí."),
    ("Presente regular", "-ar: hablo, hablas, habla, hablamos, habláis, hablan. -er: como, comes, come… -ir: vivo, vives, vive, vivimos, vivís, viven."),
    ("Presente irregular", "Mudança de vogal: e→ie (quiero, pienso), o→ue (puedo, duermo, vuelvo), e→i (pido). Yo irregular: tengo, hago, salgo, pongo, conozco, sé, doy, veo. Ser/estar/ir: soy, estoy, voy."),
    ("Pretérito indefinido", "Ação terminada: hablé, hablaste, habló, hablamos, hablaron; comí/viví… Irregulares: fui (ser/ir), tuve, estuve, hice/hizo, pude, quise, vine, dije, supe, puse. Atenção: llegué, jugué, empecé, busqué."),
    ("Gustar", "Funciona “ao contrário”: me gusta el café (o café me agrada); me gustan los gatos (plural). Pronomes: me, te, le, nos, os, les."),
    ("Muy × mucho", "Muy + adjetivo/advérbio (muy bueno). Mucho/a/os/as + substantivo (mucha hambre) ou depois do verbo (trabaja mucho)."),
    ("Por × para", "Para: destino, finalidade, destinatário (para ti, para aprender). Por: motivo, percurso, troca, meio (gracias por, paseo por, por teléfono)."),
    ("Futuro próximo e progressivo", "Ir a + infinitivo: voy a comer. Estar + gerúndio: estoy comiendo (-ar → -ando; -er/-ir → -iendo; leer → leyendo)."),
    ("Acentos", "O acento muda o sentido: mi (meu) × mí (mim), tu × tú, el × él, esta × está, hablo (eu falo) × habló (ele falou)."),
    ("Falsos amigos", "Embarazada = grávida; exquisito = delicioso; oficina = escritório; polvo = pó; rato = momento; apellido = sobrenome; largo = comprido; sobremesa = conversa após a refeição."),
]
