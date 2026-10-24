"""Reading, Writing, Listening e Speaking do Spanish Routine (A1–A2).

Esquema comum de skills/ (docs/PADRAO-IDIOMAS.md). Perguntas em português.
Textos originais; pessoas e lugares são fictícios ou genéricos.
"""

L1, L2 = "A1", "A2"


def q(question, options, answer, why):
    return {"question": question, "options": options, "answer": answer, "why": why}


TEXTS = [
    {"id": "er001", "level": L1, "topic": "apresentação", "title": "Me llamo Lucía",
     "text": "¡Hola! Me llamo Lucía y tengo veinticinco años. Soy de Sevilla, pero vivo en Madrid. Soy enfermera y trabajo en un hospital.\n\n"
             "Me gusta mucho bailar y leer. Los fines de semana salgo con mis amigos y vamos al cine. ¡Mucho gusto!",
     "translation": "Olá! Meu nome é Lucía e tenho vinte e cinco anos. Sou de Sevilha, mas moro em Madri. Sou enfermeira e trabalho num hospital.\n\n"
                    "Gosto muito de dançar e ler. Nos fins de semana saio com meus amigos e vamos ao cinema. Muito prazer!",
     "questions": [q("Onde Lucía mora?", ["Madri", "Sevilha", "Barcelona", "Valência"], 0, "Vivo en Madrid."),
                   q("Qual é a profissão dela?", ["Enfermeira", "Médica", "Professora", "Garçonete"], 0, "Soy enfermera."),
                   q("O que ela faz nos fins de semana?", ["Vai ao cinema com amigos", "Trabalha", "Viaja", "Estuda"], 0, "Vamos al cine.")]},
    {"id": "er002", "level": L1, "topic": "rotina", "title": "Un día normal",
     "text": "Me levanto a las siete. Me ducho y desayuno café con tostadas. A las ocho tomo el metro para ir a la oficina.\n\n"
             "Trabajo de nueve a cinco. Por la tarde voy al gimnasio. Ceno a las nueve y me acuesto a las once.",
     "translation": "Levanto-me às sete. Tomo banho e tomo café da manhã: café com torradas. Às oito pego o metrô para ir ao escritório.\n\n"
                    "Trabalho das nove às cinco. À tarde vou à academia. Janto às nove e me deito às onze.",
     "questions": [q("A que horas a pessoa se levanta?", ["Às 7h", "Às 8h", "Às 9h", "Às 6h"], 0, "Me levanto a las siete."),
                   q("O que ela faz à tarde?", ["Vai à academia", "Vai ao cinema", "Estuda", "Cozinha"], 0, "Por la tarde voy al gimnasio."),
                   q("Atenção ao falso amigo: “oficina” significa…", ["Escritório", "Oficina mecânica", "Loja", "Escola"], 0, "Oficina = escritório.")]},
    {"id": "er003", "level": L1, "topic": "família", "title": "Mi familia",
     "text": "Mi familia es pequeña. Somos cuatro: mi padre, mi madre, mi hermano y yo. Mi padre es profesor y mi madre es médica.\n\n"
             "Mi hermano se llama Pablo y tiene diez años. Es muy simpático y le gusta jugar al fútbol. Los domingos comemos todos juntos en casa de mi abuela.",
     "translation": "Minha família é pequena. Somos quatro: meu pai, minha mãe, meu irmão e eu. Meu pai é professor e minha mãe é médica.\n\n"
                    "Meu irmão se chama Pablo e tem dez anos. É muito simpático e gosta de jogar futebol. Aos domingos comemos todos juntos na casa da minha avó.",
     "questions": [q("Quantas pessoas há na família?", ["Quatro", "Três", "Cinco", "Seis"], 0, "Somos cuatro."),
                   q("Quantos anos tem Pablo?", ["Dez", "Doze", "Quinze", "Oito"], 0, "Tiene diez años."),
                   q("Onde comem aos domingos?", ["Na casa da avó", "Num restaurante", "Em casa", "No parque"], 0, "En casa de mi abuela.")]},
    {"id": "er004", "level": L1, "topic": "café", "title": "En la cafetería",
     "text": "Camarero: Buenos días, ¿qué le pongo?\n\nCliente: Un café con leche y una tostada con tomate, por favor.\n\n"
             "Camarero: ¿Algo más?\n\nCliente: No, gracias. ¿Cuánto es?\n\nCamarero: Son tres euros con cincuenta.\n\nCliente: Aquí tiene. ¡Gracias!",
     "translation": "Garçom: Bom dia, o que vai ser?\n\nCliente: Um café com leite e uma torrada com tomate, por favor.\n\n"
                    "Garçom: Mais alguma coisa?\n\nCliente: Não, obrigado. Quanto é?\n\nGarçom: São três euros e cinquenta.\n\nCliente: Aqui está. Obrigado!",
     "questions": [q("O que o cliente pede para beber?", ["Café com leite", "Suco", "Chá", "Água"], 0, "Un café con leche."),
                   q("O que ele pede para comer?", ["Torrada com tomate", "Bolo", "Sanduíche de presunto", "Nada"], 0, "Una tostada con tomate."),
                   q("Quanto custa?", ["3,50 euros", "5 euros", "13,50 euros", "2,50 euros"], 0, "Tres euros con cincuenta.")]},
    {"id": "er005", "level": L1, "topic": "viagem", "title": "Vacaciones en la playa",
     "text": "Este verano voy a ir a Málaga con mi familia. Vamos a viajar en tren porque es rápido y cómodo.\n\n"
             "En Málaga vamos a ir a la playa todos los días y vamos a comer pescado frito. También quiero visitar el museo Picasso.",
     "translation": "Neste verão vou para Málaga com minha família. Vamos viajar de trem porque é rápido e confortável.\n\n"
                    "Em Málaga vamos à praia todos os dias e vamos comer peixe frito. Também quero visitar o museu Picasso.",
     "questions": [q("Como a família vai viajar?", ["De trem", "De avião", "De carro", "De ônibus"], 0, "Vamos a viajar en tren."),
                   q("O que vão comer?", ["Peixe frito", "Paella", "Presunto", "Pizza"], 0, "Vamos a comer pescado frito."),
                   q("O que a pessoa quer visitar?", ["O museu Picasso", "Um estádio", "Uma montanha", "Um mercado"], 0, "Quiero visitar el museo Picasso.")]},
    {"id": "er006", "level": L1, "topic": "clima", "title": "¿Qué tiempo hace?",
     "text": "Hoy hace sol y mucho calor. Voy a la piscina con mi hermana. Llevo gafas de sol y una gorra.\n\n"
             "Pero mañana va a llover y va a hacer frío. Tengo que llevar un paraguas y un abrigo.",
     "translation": "Hoje faz sol e muito calor. Vou à piscina com minha irmã. Uso óculos de sol e um boné.\n\n"
                    "Mas amanhã vai chover e vai fazer frio. Tenho que levar um guarda-chuva e um casaco.",
     "questions": [q("Como está o tempo hoje?", ["Sol e calor", "Chuva", "Frio", "Neve"], 0, "Hace sol y mucho calor."),
                   q("Aonde a pessoa vai hoje?", ["À piscina", "À praia", "Ao cinema", "À escola"], 0, "Voy a la piscina."),
                   q("O que precisa levar amanhã?", ["Guarda-chuva e casaco", "Óculos de sol", "Boné", "Nada"], 0, "Un paraguas y un abrigo.")]},
    {"id": "er007", "level": L1, "topic": "música", "title": "Mi cantante favorito",
     "text": "Mi cantante favorito se llama Leo Marín. Canta pop latino y baila muy bien. Sus canciones son alegres.\n\n"
             "El mes pasado fui a su concierto en Buenos Aires. La entrada fue cara, pero el concierto fue increíble. ¡Canté todas las canciones!",
     "translation": "Meu cantor favorito se chama Leo Marín (fictício). Canta pop latino e dança muito bem. Suas canções são alegres.\n\n"
                    "No mês passado fui ao show dele em Buenos Aires. O ingresso foi caro, mas o show foi incrível. Cantei todas as músicas!",
     "questions": [q("Que tipo de música ele canta?", ["Pop latino", "Rock", "Tango", "Flamenco"], 0, "Canta pop latino."),
                   q("Onde foi o show?", ["Buenos Aires", "Madri", "México", "Lima"], 0, "Su concierto en Buenos Aires."),
                   q("Como foi o ingresso?", ["Caro", "Barato", "Grátis", "Esgotado"], 0, "La entrada fue cara.")]},
    {"id": "er008", "level": L1, "topic": "comida", "title": "En el restaurante",
     "text": "Ayer cené en un restaurante mexicano con mi novio. Yo pedí tacos de pollo y él pidió enchiladas. Las enchiladas estaban un poco picantes.\n\n"
             "De postre comimos flan. La comida estaba exquisita y el camarero fue muy simpático. Dejamos una buena propina.",
     "translation": "Ontem jantei num restaurante mexicano com meu namorado. Eu pedi tacos de frango e ele pediu enchiladas. As enchiladas estavam um pouco apimentadas.\n\n"
                    "De sobremesa comemos pudim. A comida estava deliciosa e o garçom foi muito simpático. Deixamos uma boa gorjeta.",
     "questions": [q("O que a pessoa pediu?", ["Tacos de frango", "Enchiladas", "Paella", "Pizza"], 0, "Yo pedí tacos de pollo."),
                   q("“Exquisita” significa…", ["Deliciosa", "Esquisita", "Cara", "Fria"], 0, "Falso amigo: exquisito = delicioso."),
                   q("“Propina” significa…", ["Gorjeta", "Suborno", "Conta", "Sobremesa"], 0, "Falso amigo: propina = gorjeta.")]},
    {"id": "er009", "level": L1, "topic": "compras", "title": "Un regalo para mi madre",
     "text": "El domingo es el cumpleaños de mi madre. Ayer fui al centro comercial para comprar un regalo. Vi un bolso rojo muy bonito, pero era muy caro.\n\n"
             "Al final compré unas flores y un libro de cocina. Mi madre cocina muy bien y le encantan los libros.",
     "translation": "Domingo é o aniversário da minha mãe. Ontem fui ao shopping comprar um presente. Vi uma bolsa vermelha muito bonita, mas era muito cara.\n\n"
                    "No fim comprei flores e um livro de culinária. Minha mãe cozinha muito bem e adora livros.",
     "questions": [q("De quem é o aniversário?", ["Da mãe", "Do pai", "Da irmã", "Da avó"], 0, "El cumpleaños de mi madre."),
                   q("De que cor era a bolsa?", ["Vermelha", "Roxa", "Preta", "Azul"], 0, "Rojo = vermelho (não roxo)."),
                   q("O que a pessoa comprou?", ["Flores e um livro de culinária", "A bolsa", "Uma roupa", "Um perfume"], 0, "Compré unas flores y un libro de cocina.")]},
    {"id": "er010", "level": L1, "topic": "estudos", "title": "Aprendo español",
     "text": "Soy brasileño y estudio español desde el año pasado. Me gusta porque es parecido al portugués, pero no es igual.\n\n"
             "La pronunciación es fácil, pero los falsos amigos son difíciles. Por ejemplo, “embarazada” no significa “embaraçada”. Estudio veinte minutos todos los días.",
     "translation": "Sou brasileiro e estudo espanhol desde o ano passado. Gosto porque é parecido com o português, mas não é igual.\n\n"
                    "A pronúncia é fácil, mas os falsos amigos são difíceis. Por exemplo, “embarazada” não significa “embaraçada”. Estudo vinte minutos todos os dias.",
     "questions": [q("Desde quando a pessoa estuda espanhol?", ["Desde o ano passado", "Desde criança", "Há uma semana", "Desde este mês"], 0, "Desde el año pasado."),
                   q("O que é difícil para ela?", ["Os falsos amigos", "A pronúncia", "Os números", "Os verbos"], 0, "Los falsos amigos son difíciles."),
                   q("“Embarazada” significa…", ["Grávida", "Embaraçada", "Cansada", "Casada"], 0, "Embarazada = grávida.")]},
    {"id": "er011", "level": L2, "topic": "moradia", "title": "Mi nuevo piso",
     "text": "El mes pasado me mudé a un piso nuevo. Antes vivía lejos del trabajo y tardaba una hora en llegar. Ahora vivo en el centro y voy andando en quince minutos.\n\n"
             "El piso es pequeño, pero tiene mucha luz y un balcón con plantas. Cerca hay un mercado y una panadería. Este sábado voy a invitar a mis amigos a cenar.",
     "translation": "No mês passado me mudei para um apartamento novo. Antes eu morava longe do trabalho e levava uma hora para chegar. Agora moro no centro e vou a pé em quinze minutos.\n\n"
                    "O apartamento é pequeno, mas tem muita luz e uma sacada com plantas. Perto há um mercado e uma padaria. Neste sábado vou convidar meus amigos para jantar.",
     "questions": [q("Por que a pessoa se mudou?", ["Morava longe do trabalho", "O apartamento era caro", "Queria uma sacada", "Mudou de emprego"], 0, "Antes vivía lejos del trabajo."),
                   q("Quanto tempo leva a pé agora?", ["Quinze minutos", "Uma hora", "Cinco minutos", "Meia hora"], 0, "Voy andando en quince minutos."),
                   q("O que vai fazer no sábado?", ["Convidar amigos para jantar", "Mudar de novo", "Comprar plantas", "Viajar"], 0, "Voy a invitar a mis amigos a cenar.")]},
    {"id": "er012", "level": L2, "topic": "saúde", "title": "En el médico",
     "text": "Desde ayer me duele la cabeza y tengo fiebre. Esta mañana no fui a trabajar y fui al médico. El médico me dijo que tengo gripe.\n\n"
             "Me recetó unas pastillas y me dijo que tengo que descansar y beber mucha agua. Creo que en tres o cuatro días voy a estar bien.",
     "translation": "Desde ontem estou com dor de cabeça e febre. Hoje de manhã não fui trabalhar e fui ao médico. O médico me disse que estou gripado.\n\n"
                    "Ele me receitou uns comprimidos e disse que preciso descansar e beber muita água. Acho que em três ou quatro dias vou estar bem.",
     "questions": [q("Quais são os sintomas?", ["Dor de cabeça e febre", "Dor de barriga", "Tosse", "Dor nas costas"], 0, "Me duele la cabeza y tengo fiebre."),
                   q("“Pastillas” são…", ["Comprimidos", "Pastilhas de menta", "Vitaminas", "Injeções"], 0, "Falso amigo: pastilla = comprimido."),
                   q("Qual foi o conselho?", ["Descansar e beber muita água", "Fazer exercício", "Ir trabalhar", "Comer muito"], 0, "Tengo que descansar y beber mucha agua.")]},
    {"id": "er013", "level": L2, "topic": "trabalho", "title": "Mi trabajo de fin de semana",
     "text": "Los sábados y domingos trabajo en una tienda de ropa. Empiezo a las diez de la mañana y termino a las seis de la tarde. Atiendo a los clientes y ordeno la ropa.\n\n"
             "A veces es cansado, pero mis compañeros son muy amables. Estoy ahorrando dinero porque en agosto quiero viajar a México.",
     "translation": "Aos sábados e domingos trabalho numa loja de roupas. Começo às dez da manhã e termino às seis da tarde. Atendo os clientes e arrumo as roupas.\n\n"
                    "Às vezes é cansativo, mas meus colegas são muito gentis. Estou economizando dinheiro porque em agosto quero viajar para o México.",
     "questions": [q("Onde a pessoa trabalha?", ["Numa loja de roupas", "Num café", "Num hospital", "Numa escola"], 0, "Una tienda de ropa."),
                   q("Qual é o horário?", ["Das 10h às 18h", "Das 9h às 17h", "Das 8h às 14h", "Das 14h às 22h"], 0, "A las diez … a las seis de la tarde."),
                   q("Para que economiza dinheiro?", ["Viajar ao México", "Comprar roupa", "Pagar a faculdade", "Mudar de casa"], 0, "Quiero viajar a México.")]},
    {"id": "er014", "level": L2, "topic": "séries", "title": "Una serie que recomiendo",
     "text": "Estos días estoy viendo una serie española que se llama “El patio de las flores”. La historia pasa en un pueblo pequeño de Andalucía.\n\n"
             "Los protagonistas son una profesora y un cocinero. Al principio discuten mucho, pero poco a poco se enamoran. Los actores son muy buenos. ¡Te la recomiendo!",
     "translation": "Esses dias estou vendo uma série espanhola chamada “O pátio das flores” (fictícia). A história se passa num povoado pequeno da Andaluzia.\n\n"
                    "Os protagonistas são uma professora e um cozinheiro. No começo discutem muito, mas pouco a pouco se apaixonam. Os atores são muito bons. Recomendo!",
     "questions": [q("Onde se passa a história?", ["Num povoado da Andaluzia", "Em Madri", "No México", "Numa escola"], 0, "Un pueblo pequeño de Andalucía."),
                   q("Quem são os protagonistas?", ["Uma professora e um cozinheiro", "Dois estudantes", "Um médico e uma cantora", "Duas irmãs"], 0, "Una profesora y un cocinero."),
                   q("O que acontece com eles?", ["Discutem e depois se apaixonam", "Ficam amigos para sempre", "Mudam de cidade", "Abrem um restaurante"], 0, "Discuten … se enamoran.")]},
    {"id": "er015", "level": L2, "topic": "viagem", "title": "Preguntar el camino",
     "text": "Turista: Perdone, ¿cómo llego al Museo del Prado?\n\nSeñora: Puede ir en metro. Tome la línea uno y baje en Atocha.\n\n"
             "Turista: ¿Está lejos la estación?\n\nSeñora: No, siga recto y gire a la derecha. Está a cinco minutos andando.\n\nTurista: ¡Muchas gracias!\n\nSeñora: De nada. ¡Que disfrute!",
     "translation": "Turista: Com licença, como chego ao Museu do Prado?\n\nSenhora: Pode ir de metrô. Pegue a linha um e desça em Atocha.\n\n"
                    "Turista: A estação é longe?\n\nSenhora: Não, siga reto e vire à direita. Fica a cinco minutos a pé.\n\nTurista: Muito obrigado!\n\nSenhora: De nada. Aproveite!",
     "questions": [q("Aonde o turista quer ir?", ["Museu do Prado", "Estação de trem", "Aeroporto", "Hotel"], 0, "¿Cómo llego al Museo del Prado?"),
                   q("Em qual estação deve descer?", ["Atocha", "Sol", "Prado", "Retiro"], 0, "Baje en Atocha."),
                   q("Quanto tempo leva até a estação?", ["Cinco minutos a pé", "Meia hora", "Uma hora", "Dez minutos de táxi"], 0, "A cinco minutos andando.")]},
    {"id": "er016", "level": L2, "topic": "hobby", "title": "Mi afición: la fotografía",
     "text": "Mi afición es la fotografía. Cuando tenía quince años, mi abuelo me regaló una cámara antigua. Desde entonces me encanta hacer fotos.\n\n"
             "Los fines de semana paseo por la ciudad con mi cámara. Me gusta fotografiar a la gente cuando sonríe. Algún día quiero hacer una exposición con mis fotos.",
     "translation": "Meu hobby é a fotografia. Quando eu tinha quinze anos, meu avô me deu uma câmera antiga. Desde então adoro tirar fotos.\n\n"
                    "Nos fins de semana passeio pela cidade com minha câmera. Gosto de fotografar as pessoas quando sorriem. Algum dia quero fazer uma exposição com minhas fotos.",
     "questions": [q("Qual é o hobby da pessoa?", ["Fotografia", "Pintura", "Dança", "Cozinhar"], 0, "Mi afición es la fotografía."),
                   q("Quem deu a câmera?", ["O avô", "O pai", "A mãe", "Um amigo"], 0, "Mi abuelo me regaló una cámara."),
                   q("Qual é o sonho dela?", ["Fazer uma exposição", "Comprar outra câmera", "Ser modelo", "Viajar"], 0, "Quiero hacer una exposición.")]},
    {"id": "er017", "level": L2, "topic": "estações", "title": "Las estaciones en Argentina",
     "text": "En Argentina las estaciones son al revés que en Europa: en diciembre es verano y en julio es invierno. En verano hace mucho calor y la gente va a la playa.\n\n"
             "En otoño hace fresco y los árboles cambian de color. En invierno nieva en la Patagonia y mucha gente va a esquiar. Mi estación favorita es la primavera.",
     "translation": "Na Argentina as estações são ao contrário da Europa: em dezembro é verão e em julho é inverno. No verão faz muito calor e as pessoas vão à praia.\n\n"
                    "No outono faz fresco e as árvores mudam de cor. No inverno neva na Patagônia e muita gente vai esquiar. Minha estação favorita é a primavera.",
     "questions": [q("Em julho, na Argentina, é…", ["Inverno", "Verão", "Primavera", "Outono"], 0, "En julio es invierno."),
                   q("O que muita gente faz no inverno?", ["Esquiar na Patagônia", "Ir à praia", "Ver as flores", "Nadar"], 0, "Mucha gente va a esquiar."),
                   q("Qual é a estação favorita da pessoa?", ["Primavera", "Verão", "Outono", "Inverno"], 0, "Mi estación favorita es la primavera.")]},
    {"id": "er018", "level": L2, "topic": "mensagens", "title": "Cambio de planes",
     "text": "Hola, Marta: perdona, pero no puedo ir mañana a las siete. Tengo una reunión muy importante en el trabajo y voy a salir tarde.\n\n"
             "¿Podemos quedar a las ocho y media? Si no, ¿qué tal el sábado a mediodía? Podemos comer en el restaurante italiano que te gusta. ¡Escríbeme!",
     "translation": "Oi, Marta: desculpe, mas não posso ir amanhã às sete. Tenho uma reunião muito importante no trabalho e vou sair tarde.\n\n"
                    "Podemos nos encontrar às oito e meia? Se não, que tal sábado ao meio-dia? Podemos comer no restaurante italiano de que você gosta. Me escreve!",
     "questions": [q("Por que a pessoa não pode ir às sete?", ["Tem uma reunião no trabalho", "Está doente", "Perdeu o ônibus", "Esqueceu"], 0, "Tengo una reunión muy importante."),
                   q("Que horário ela sugere amanhã?", ["20h30", "19h", "12h", "21h30"], 0, "A las ocho y media."),
                   q("Qual é a alternativa?", ["Almoço no sábado", "Café no domingo", "Jantar na sexta", "Cancelar"], 0, "El sábado a mediodía.")]},
    {"id": "er019", "level": L2, "topic": "consumo", "title": "Comprar por internet",
     "text": "Hoy en día mucha gente compra por internet. Es cómodo, porque puedes comprar desde casa, y el pedido normalmente llega al día siguiente. Además, muchas veces es más barato.\n\n"
             "Pero también tiene desventajas: no puedes probarte la ropa y a veces la talla no es la correcta. Por eso yo compro la ropa en la tienda y los libros por internet.",
     "translation": "Hoje em dia muita gente compra pela internet. É prático, porque dá para comprar de casa, e o pedido normalmente chega no dia seguinte. Além disso, muitas vezes é mais barato.\n\n"
                    "Mas também tem desvantagens: não dá para provar a roupa e às vezes o tamanho não é o certo. Por isso compro roupa na loja e livros pela internet.",
     "questions": [q("Qual é uma vantagem?", ["O pedido chega no dia seguinte", "Dá para provar a roupa", "É sempre mais caro", "Precisa ir à loja"], 0, "Llega al día siguiente."),
                   q("Qual é a desvantagem?", ["Não dá para provar a roupa", "Demora um mês", "Só aceita dinheiro", "Não há livros"], 0, "No puedes probarte la ropa."),
                   q("O que a pessoa compra pela internet?", ["Livros", "Roupa", "Sapatos", "Comida"], 0, "Los libros por internet.")]},
    {"id": "er020", "level": L2, "topic": "dança", "title": "Clases de salsa",
     "text": "Este año empecé a ir a clases de salsa. Las clases son los martes y los jueves por la noche, en una escuela cerca de mi casa.\n\n"
             "Al principio bailaba muy mal y estaba nervioso, pero la profesora tiene mucha paciencia y ahora bailo mejor. El mes que viene vamos a bailar en una fiesta del barrio. ¡Qué emoción!",
     "translation": "Este ano comecei a fazer aulas de salsa. As aulas são às terças e quintas à noite, numa escola perto de casa.\n\n"
                    "No começo eu dançava muito mal e ficava nervoso, mas a professora tem muita paciência e agora danço melhor. No mês que vem vamos dançar numa festa do bairro. Que emoção!",
     "questions": [q("Quando são as aulas?", ["Terças e quintas à noite", "Todo dia", "Só no sábado", "Segundas de manhã"], 0, "Los martes y los jueves por la noche."),
                   q("Como era no começo?", ["Dançava mal e ficava nervoso", "Já dançava bem", "Não gostava", "Faltava muito"], 0, "Bailaba muy mal y estaba nervioso."),
                   q("O que vai acontecer no mês que vem?", ["Vão dançar numa festa do bairro", "Uma prova", "Uma viagem", "O fim das aulas"], 0, "Vamos a bailar en una fiesta del barrio.")]},
]

PROMPTS = [
    {"id": "ew01", "level": L1, "topic": "apresentação", "prompt": "Preséntate.", "prompt_pt": "Apresente-se: nome, idade, cidade, trabalho ou estudos e gostos.", "units": 50, "lines": 4},
    {"id": "ew02", "level": L1, "topic": "rotina", "prompt": "Describe un día normal.", "prompt_pt": "Descreva sua rotina (use verbos reflexivos: me levanto, me ducho…).", "units": 50, "lines": 4},
    {"id": "ew03", "level": L1, "topic": "família", "prompt": "Habla de tu familia.", "prompt_pt": "Apresente sua família: quem são, profissões e gostos.", "units": 50, "lines": 4},
    {"id": "ew04", "level": L1, "topic": "comida", "prompt": "¿Qué te gusta comer?", "prompt_pt": "O que você gosta (e não gosta) de comer? Use me gusta / me gustan.", "units": 50, "lines": 4},
    {"id": "ew05", "level": L1, "topic": "passado", "prompt": "¿Qué hiciste el fin de semana pasado?", "prompt_pt": "Conte seu último fim de semana (pretérito indefinido).", "units": 50, "lines": 4},
    {"id": "ew06", "level": L1, "topic": "música", "prompt": "Tu cantante o serie favorita.", "prompt_pt": "Fale do seu cantor ou série favorita e por quê.", "units": 50, "lines": 4},
    {"id": "ew07", "level": L1, "topic": "cidade", "prompt": "Describe tu barrio.", "prompt_pt": "Descreva seu bairro: hay / está, o que tem perto.", "units": 50, "lines": 4},
    {"id": "ew08", "level": L1, "topic": "futuro", "prompt": "¿Qué vas a hacer en las próximas vacaciones?", "prompt_pt": "Planos para as férias (ir a + infinitivo).", "units": 50, "lines": 4},
    {"id": "ew09", "level": L2, "topic": "estudos", "prompt": "¿Por qué estudias español?", "prompt_pt": "Por que você estuda espanhol? O que é fácil e difícil para um brasileiro?", "units": 100, "lines": 6},
    {"id": "ew10", "level": L2, "topic": "viagem", "prompt": "Cuenta un viaje inolvidable.", "prompt_pt": "Conte uma viagem inesquecível: onde, com quem, o que aconteceu.", "units": 100, "lines": 6},
    {"id": "ew11", "level": L2, "topic": "estações", "prompt": "¿Cuál es tu estación favorita y por qué?", "prompt_pt": "Sua estação favorita e por quê; compare com outra.", "units": 100, "lines": 6},
    {"id": "ew12", "level": L2, "topic": "saúde", "prompt": "¿Qué haces para cuidar tu salud?", "prompt_pt": "O que você faz pela saúde? Dê exemplos.", "units": 100, "lines": 6},
    {"id": "ew13", "level": L2, "topic": "consumo", "prompt": "Ventajas y desventajas de comprar por internet.", "prompt_pt": "Vantagens e desvantagens de comprar online (además, pero, por eso).", "units": 100, "lines": 6},
    {"id": "ew14", "level": L2, "topic": "mensagens", "prompt": "Escribe a un amigo para cambiar una cita.", "prompt_pt": "Mensagem a um amigo mudando um encontro: desculpe-se, explique e proponha outro horário.", "units": 100, "lines": 6},
    {"id": "ew15", "level": L2, "topic": "hobby", "prompt": "Habla de tu afición.", "prompt_pt": "Apresente seu hobby: como começou, quando pratica, o que sente.", "units": 100, "lines": 6},
    {"id": "ew16", "level": L2, "topic": "futuro", "prompt": "¿Cómo te imaginas dentro de diez años?", "prompt_pt": "Como você se imagina daqui a dez anos?", "units": 100, "lines": 6},
]

ROLEPLAY = "1. ¿Cuál es tu idea principal? 2. ¿Puedes dar un ejemplo? 3. ¿Por qué piensas eso?"
