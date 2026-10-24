"""Banco do teste de nivelamento de inglês (CEFR A1–C2).

Itens originais. A resposta certa é sempre a primeira opção aqui; o app embaralha.
type: grammar | vocab | reading | listening. Reading usa `passage`; listening usa `audio`.
"""

G, V, R, L = "grammar", "vocab", "reading", "listening"


def item(level, kind, stem, options, why, passage=None, audio=None):
    return {"level": level, "type": kind, "stem": stem, "options": options, "why": why, "passage": passage, "audio": audio}


GRAMMAR = [
    # A1
    item("A1", G, "I ___ from Brazil.", ["am", "is", "are", "be"], "Com I usamos am."),
    item("A1", G, "She ___ two brothers.", ["has", "have", "is", "haves"], "Terceira pessoa (she) → has."),
    item("A1", G, "There ___ a book on the table.", ["is", "are", "am", "be"], "Singular (a book) → there is."),
    item("A1", G, "___ you like coffee?", ["Do", "Does", "Are", "Is"], "Pergunta no simple present com you → Do."),
    item("A1", V, "The opposite of “big” is ___.", ["small", "tall", "long", "fast"], "big × small."),
    item("A1", G, "We go to school ___ Monday.", ["on", "in", "at", "to"], "Dias da semana → on."),
    item("A1", G, "He ___ TV every evening.", ["watches", "watch", "watching", "is watch"], "Hábito, terceira pessoa → watches."),
    item("A1", V, "My mother's brother is my ___.", ["uncle", "cousin", "nephew", "grandfather"], "Irmão da mãe = tio (uncle)."),
    # A2
    item("A2", G, "I ___ to the cinema last night.", ["went", "go", "gone", "have gone"], "Last night (tempo terminado) → simple past."),
    item("A2", G, "She is ___ than her sister.", ["taller", "more tall", "tallest", "the taller"], "Adjetivo curto no comparativo → -er than."),
    item("A2", G, "Look! It ___.", ["is raining", "rains", "rain", "rained"], "Look! = agora → present continuous."),
    item("A2", G, "We ___ visit our grandparents next weekend.", ["are going to", "going to", "will to", "go to"], "Plano decidido → be going to."),
    item("A2", G, "How ___ money do you have?", ["much", "many", "lot", "few"], "Money é incontável → how much."),
    item("A2", G, "I've lived here ___ 2015.", ["since", "for", "from", "during"], "Ponto de início → since."),
    item("A2", V, "I need to ___ an appointment with the dentist.", ["make", "do", "take", "say"], "Colocação: make an appointment."),
    item("A2", G, "You ___ smoke here. It's forbidden.", ["mustn't", "don't have to", "needn't", "aren't"], "Proibição → mustn't."),
    # B1
    item("B1", G, "If it rains tomorrow, we ___ at home.", ["will stay", "stay", "would stay", "stayed"], "Primeira condicional: if + presente, will + verbo."),
    item("B1", G, "When I arrived, the film ___.", ["had already started", "already started", "has already started", "was already start"], "Ação anterior a outra no passado → past perfect."),
    item("B1", G, "The book ___ by millions of people.", ["has been read", "has read", "is reading", "have been read"], "Voz passiva no present perfect (singular)."),
    item("B1", G, "She asked me where I ___.", ["lived", "live", "do live", "am living"], "Discurso indireto: o tempo recua (live → lived)."),
    item("B1", G, "I'm not used to ___ up so early.", ["getting", "get", "got", "be getting"], "Be used to + -ing."),
    item("B1", V, "Could you ___ the music down? I'm trying to sleep.", ["turn", "put", "take", "give"], "Turn down = abaixar o volume."),
    item("B1", G, "He suggested ___ a taxi.", ["taking", "to take", "take", "that taking"], "Suggest + -ing."),
    item("B1", G, "This is the man ___ car was stolen.", ["whose", "who", "which", "that's"], "Posse em oração relativa → whose."),
    # B2
    item("B2", G, "If I had known, I ___ you.", ["would have told", "would tell", "had told", "will have told"], "Terceira condicional: would have + particípio."),
    item("B2", G, "By the time you arrive, we ___ dinner.", ["will have finished", "will finish", "finished", "have finished"], "Ação concluída antes de um ponto no futuro → future perfect."),
    item("B2", G, "She denied ___ the money.", ["taking", "to take", "take", "to have take"], "Deny + -ing."),
    item("B2", G, "You ___ have called me; I was worried!", ["should", "must", "can", "would"], "Crítica sobre o passado → should have + particípio."),
    item("B2", V, "The match was ___ off because of the storm.", ["called", "turned", "taken", "given"], "Call off = cancelar."),
    item("B2", G, "I wish I ___ more time to travel.", ["had", "have", "would have", "will have"], "Desejo sobre o presente → wish + past simple."),
    item("B2", G, "It's high time we ___ home.", ["went", "go", "will go", "are going"], "It's high time + past simple."),
    item("B2", V, "The new policy had a significant ___ on sales.", ["impact", "affect", "influent", "consequent"], "Substantivo correto: impact on."),
    # C1
    item("C1", G, "Hardly ___ the house when it started to rain.", ["had I left", "I had left", "did I leave", "I left"], "Hardly no início pede inversão: had I left."),
    item("C1", G, "Not only ___ late, but he also forgot the tickets.", ["was he", "he was", "he is", "had he"], "Not only no início pede inversão: was he."),
    item("C1", G, "Had I known about the delay, I ___ earlier.", ["would have left", "would leave", "had left", "will leave"], "Condicional invertida (Had I known) + would have."),
    item("C1", G, "The project, ___ was funded by the EU, ended last year.", ["which", "that", "what", "who"], "Oração explicativa (entre vírgulas) não aceita that → which."),
    item("C1", V, "Her argument doesn't ___ water.", ["hold", "keep", "carry", "take"], "Expressão: not hold water = não se sustentar."),
    item("C1", G, "It is essential that he ___ on time.", ["be", "is", "will be", "being"], "Subjuntivo: essential that + verbo base."),
    item("C1", G, "She is said ___ the company in 2010.", ["to have founded", "to found", "having founded", "that she founded"], "Passiva reportada sobre o passado → to have + particípio."),
    item("C1", V, "We need to ___ a balance between cost and quality.", ["strike", "hit", "make", "take"], "Colocação: strike a balance."),
    # C2
    item("C2", G, "Little ___ that the decision would change everything.", ["did they know", "they knew", "they did know", "knew they"], "Little no início pede inversão com auxiliar: did they know."),
    item("C2", G, "___ it not been for your help, we would have failed.", ["Had", "Were", "Was", "Should"], "Had it not been for = se não fosse (passado)."),
    item("C2", V, "His explanation was so ___ that nobody could follow it.", ["convoluted", "convoluting", "convolution", "convolutely"], "Adjetivo: convoluted = enrolado, complicado."),
    item("C2", V, "She has a ___ for languages; she speaks seven.", ["flair", "flare", "flavour", "flirt"], "Flair = talento natural (não confundir com flare)."),
    item("C2", G, "No sooner had we sat down ___ the lights went out.", ["than", "when", "that", "then"], "No sooner … than."),
    item("C2", V, "The new evidence ___ the theory.", ["corroborates", "collaborates", "corrodes", "corresponds"], "Corroborate = confirmar."),
    item("C2", G, "I'd rather you ___ mention it to anyone.", ["didn't", "don't", "won't", "not"], "I'd rather + outra pessoa + past simple."),
    item("C2", V, "The plan was ___ from the start; it never had a chance.", ["doomed", "deemed", "damned", "dimmed"], "Doomed from the start = fadado ao fracasso."),
]

READING = [
    item("A1", R, "Where does Tom work?", ["In a café", "In an office", "In a school", "In a hospital"], "“I work in a café.”",
         passage="Hi, I'm Tom. I'm 25 and I live in London with my cat, Max. I work in a café. I start work at 7 a.m., so I get up very early."),
    item("A1", R, "Why does Tom get up early?", ["He starts work at 7", "He has a cat", "He lives in London", "He likes mornings"], "“I start work at 7 a.m., so I get up very early.”",
         passage="Hi, I'm Tom. I'm 25 and I live in London with my cat, Max. I work in a café. I start work at 7 a.m., so I get up very early."),
    item("A1", R, "When can you visit the library on Saturday?", ["From 10:00 to 14:00", "From 9:00 to 18:00", "All day", "You can't, it's closed"], "Saturday 10:00–14:00.",
         passage="LIBRARY HOURS\nMonday to Friday: 9:00–18:00\nSaturday: 10:00–14:00\nSunday: closed"),
    item("A2", R, "What is Ana's problem?", ["She finishes work late", "She doesn't like parties", "She can't make a cake", "She is ill"], "“I have to work until 8 p.m.”",
         passage="Hi Sara,\nThanks for the invitation! I'd love to come to your party on Saturday, but I have to work until 8 p.m. Can I come a bit later, around 9? I'll bring a cake.\nAna"),
    item("A2", R, "Two adults and one 8-year-old visit on a normal Tuesday. How much do they pay?", ["£30", "£36", "£24", "Nothing"], "£12 + £12 + £6 = £30.",
         passage="The museum is free on the first Sunday of every month. On other days, tickets cost £12 for adults and £6 for children under 12. Groups of more than 10 people must book in advance."),
    item("B1", R, "What did the study find?", ["People working from home were more productive", "People working from home took more breaks", "Office workers completed more tasks", "Productivity did not change"],
         "“those who worked from home completed 13% more tasks”.",
         passage="Many people believe that working from home makes employees less productive. However, a recent study of 16,000 workers found the opposite: those who worked from home completed 13% more tasks, mainly because they took fewer breaks and sick days."),
    item("B1", R, "Why were they more productive?", ["They took fewer breaks and sick days", "They worked longer hours", "They were paid more", "They had more meetings"],
         "“mainly because they took fewer breaks and sick days”.",
         passage="Many people believe that working from home makes employees less productive. However, a recent study of 16,000 workers found the opposite: those who worked from home completed 13% more tasks, mainly because they took fewer breaks and sick days."),
    item("B1", R, "What will the company do?", ["Send the order in two parts", "Cancel the whole order", "Charge extra for delivery", "Wait and send everything together"],
         "“We will send the available items now and the remaining item as soon as it arrives”.",
         passage="Dear customer, your order #4521 has been delayed because one of the items is temporarily out of stock. We will send the available items now and the remaining item as soon as it arrives, at no extra cost. If you prefer, you can cancel the missing item for a full refund."),
    item("B2", R, "What is the main point of the text?", ["The benefit of electric cars depends on how electricity is produced", "Electric cars pollute more than petrol cars", "Coal is cleaner than people think", "Electric cars produce exhaust emissions"],
         "“their environmental benefits depend largely on how the electricity is generated”.",
         passage="Although electric cars produce no exhaust emissions, critics argue that their environmental benefits depend largely on how the electricity is generated. In countries where most power still comes from coal, the overall reduction in carbon emissions may be smaller than expected."),
    item("B2", R, "Why was the decision postponed?", ["To consult the residents first", "Because local businesses rejected it", "Because there was no money", "Because the centre was already built"],
         "“until residents have been consulted”.",
         passage="The town council has postponed the decision on the new shopping centre until residents have been consulted. While some local businesses welcome the project, others fear it will draw customers away from the high street."),
    item("B2", R, "What do some businesses fear?", ["Losing customers to the new centre", "Higher taxes", "The council closing them", "Too many new residents"],
         "“others fear it will draw customers away from the high street”.",
         passage="The town council has postponed the decision on the new shopping centre until residents have been consulted. While some local businesses welcome the project, others fear it will draw customers away from the high street."),
    item("C1", R, "According to the text, multitasking…", ["mostly means switching between tasks, which has a cost", "is an efficient way to work", "is impossible for the brain", "has no effect on attention"],
         "“rapid switching between tasks — a process that incurs a cognitive cost”.",
         passage="The notion that multitasking boosts efficiency has been steadily undermined by research. What appears to be simultaneous processing is, in most cases, rapid switching between tasks — a process that incurs a cognitive cost each time attention shifts."),
    item("C1", R, "What did the critics claim?", ["The tax cuts mainly helped the richest households", "Inequality fell", "Median incomes rose sharply", "The wealthiest paid more tax"],
         "“had disproportionately benefited the wealthiest households”.",
         passage="Critics of the policy were quick to point out that, far from reducing inequality, the tax cuts had disproportionately benefited the wealthiest households, whose savings rose markedly while median incomes stagnated."),
    item("C2", R, "The reviewer suggests that the memoir…", ["may use honesty as a way of settling old scores", "is completely objective", "avoids personal feelings", "was written by someone else"],
         "“whether its candour is a virtue or merely a more sophisticated form of score-settling”.",
         passage="Far from being a dispassionate chronicle, the memoir is shot through with the author's lingering resentments; one is left wondering whether its candour is a virtue or merely a more sophisticated form of score-settling."),
    item("C2", R, "The writer's attitude to the null results is…", ["positive, because reporting them counters publication bias", "that they prove the experiment failed", "that they should not have been published", "indifferent"],
         "“the willingness to report what did not work is itself a contribution”.",
         passage="That the experiment yielded null results is less damning than it might first appear: in a field plagued by publication bias, the willingness to report what did not work is itself a contribution."),
]

LISTENING = [
    item("A1", L, "What is Lucy's job?", ["Teacher", "Doctor", "Student", "Cook"], "“I'm a teacher.”",
         audio="Hello, my name is Lucy. I'm a teacher and I have two children."),
    item("A1", L, "When does the bus leave?", ["At 9:30", "At 9:00", "At 10:30", "At 8:30"], "“half past nine” = 9:30.",
         audio="The bus to the airport leaves at half past nine."),
    item("A2", L, "Why is the speaker driving today?", ["There is a train strike", "The car is new", "It's raining", "The train is late"], "“because there's a strike”.",
         audio="I usually take the train to work, but today I'm driving because there's a strike."),
    item("A2", L, "What does the customer NOT order?", ["A cup of tea", "A cappuccino", "A cheese sandwich", "Water"], "Pede cappuccino, sanduíche e água; não pede chá.",
         audio="Can I have a large cappuccino and a cheese sandwich, please? Oh, and a bottle of water."),
    item("B1", L, "What did the speaker decide to do?", ["Become a vet", "Study medicine", "Open an animal shelter", "Stop studying"], "“I wanted to become a vet instead”.",
         audio="I was going to study medicine, but after volunteering at an animal shelter, I realised I wanted to become a vet instead."),
    item("B1", L, "What has changed?", ["The platform", "The departure time", "The destination", "The train was cancelled"], "“platform 4 instead of platform 2”.",
         audio="Attention, passengers. The six fifteen train to Manchester will depart from platform four instead of platform two. We apologise for any inconvenience."),
    item("B2", L, "What happened?", ["The forecast was wrong and they got caught in a storm", "They didn't go because of the forecast", "They reached the top before the storm", "The storm was correctly predicted"],
         "“Had the forecast been accurate, we'd never have set off”.",
         audio="Had the forecast been accurate, we'd never have set off that morning. As it was, we got caught in the storm halfway up the mountain."),
    item("B2", L, "How does the speaker feel about the job offer?", ["The salary is too low", "The job is too easy", "They accept it happily", "They want less responsibility"],
         "“the salary falls short of what I'd expect”.",
         audio="While I appreciate the offer, I'm afraid the salary falls short of what I'd expect for a role with this level of responsibility."),
    item("C1", L, "What is the speaker's view of the proposal?", ["The idea is good, but the timing is bad", "The proposal has no value", "The budget cuts are over", "The timing is ideal"],
         "“It's not that the proposal lacks merit; it's that the timing couldn't be worse”.",
         audio="It's not that the proposal lacks merit; it's that the timing couldn't be worse, given the budget cuts we're facing this quarter."),
    item("C1", L, "Why has the population declined?", ["Housing became too expensive for young people", "There are fewer jobs", "Older residents moved away", "It hasn't, it has grown"],
         "“younger residents have been priced out of the housing market”.",
         audio="Contrary to popular belief, the city's population has actually declined slightly over the past decade, largely because younger residents have been priced out of the housing market."),
    item("C2", L, "The speaker thinks the campaign…", ["was disappointing but not a total failure", "was a complete success", "exceeded expectations", "was a total failure"],
         "“I wouldn't go so far as to call it a failure, but … fell well short”.",
         audio="I wouldn't go so far as to call it a failure, but the campaign certainly fell well short of the lofty expectations its organisers had set for it."),
    item("C2", L, "What is the speaker's criticism of the novel?", ["It has too many ideas and abandons its plot", "It lacks ambition", "The plot is too simple", "It is too short"],
         "“buckles under the weight of its own ideas; the plot is all but abandoned”.",
         audio="Her latest novel, while undeniably ambitious, buckles under the weight of its own ideas. The plot is all but abandoned halfway through."),
]

BANK = GRAMMAR + READING + LISTENING
