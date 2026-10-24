"""Enunciados das questões no idioma estudado: chinês, japonês, espanhol, francês, italiano e alemão.

Mesmo formato de strings.PROMPTS (exatos + padrões). Importado no fim de strings.py.
"""

TYPING = {
    "ko": {"Digitar em hangul": "한글로 입력"},
    "zh": {"Digitar (caracteres ou pinyin)": "输入（汉字或拼音）"},
    "ja": {"Digitar (kana ou romaji)": "入力（かな・ローマ字）"},
}

PROMPTS = {
    "zh": {
        "exact": {
            "Como se lê?": "怎么读？", "Como se diz em chinês?": "用中文怎么说？", "O que significa?": "是什么意思？",
            "Ouça e escolha a palavra que você ouviu.": "听一听，选出你听到的词。", "Complete com o classificador.": "填上量词。",
            "Complete as duas lacunas (lugar e pergunta).": "填两个空（地点和疑问）。", "Complete as duas lacunas (lugar e classificador).": "填两个空（地点和量词）。",
            "Complete as três lacunas (lugar, ação concluída e classificador).": "填三个空（地点、完成的动作和量词）。",
            "Complete as duas lacunas (negação no passado e lugar).": "填两个空（过去的否定和地点）。", "Complete as duas lacunas (querer e classificador).": "填两个空（想要和量词）。",
            "Complete as duas lacunas (lugar e experiência).": "填两个空（地点和经历）。", "Complete a pergunta (onde?).": "完成问句（哪儿？）。",
            "Complete a frase (hábito negativo).": "完成句子（否定的习惯）。",
            "ação concluída": "完成（了）", "classificador": "量词", "experiência": "经历（过）", "lugar da ação (在)": "地点（在）", "negação": "否定",
            "pergunta": "疑问", "querer": "想要",
        },
        "patterns": [
            ["Qual é o tom de {0} ({1})?", "{0} 是第几声？"], ["Qual destas sílabas tem o {n}º tom ({0})?", "哪个音节是第{n}声？"],
            ["Como se diz “{0}”?", "用中文怎么说？"], ["“{0}” antes de classificador:", "量词前面的数字怎么说？"],
        ],
    },
    "ja": {
        "exact": {
            "Como se lê este hiragana?": "このひらがなは何と読みますか？", "Como se lê este katakana?": "このカタカナは何と読みますか？", "Como se lê?": "何と読みますか？",
            "O que significa?": "どういう意味ですか？", "Como se diz em japonês?": "日本語で何と言いますか？", "Ouça e escolha a palavra que você ouviu.": "聞いた単語を選んでください。",
            "Complete com a partícula.": "助詞を入れてください。",
            "Complete as três partículas (tópico, lugar da ação e objeto).": "助詞を三つ入れてください（主題・動作の場所・目的語）。",
            "Complete as duas partículas (tópico e destino).": "助詞を二つ入れてください（主題・行き先）。",
            "Complete as três lacunas (lugar, objeto e verbo no passado).": "空欄を三つ埋めてください（場所・目的語・動詞の過去形）。",
            "Complete as lacunas (amanhã: verbo -masu).": "空欄を埋めてください（明日：動詞の「ます」形）。",
            "Complete as lacunas (あまり pede negativo).": "空欄を埋めてください（「あまり」のあとは否定形）。",
            "Complete as partículas (forma -te liga as ações).": "助詞を入れてください（て形で動作をつなぐ）。",
            "Complete as três partículas (pergunta no passado).": "助詞を三つ入れてください（過去の質問）。",
            "Complete as lacunas (先週 + não fez).": "空欄を埋めてください（「先週」＋しなかった）。",
            "Complete as partículas (com quem e destino).": "助詞を入れてください（だれと・行き先）。",
            "companhia": "だれと", "destino": "行き先", "lugar da ação": "動作の場所", "objeto": "目的語", "passado negativo": "過去の否定形",
            "tópico": "主題", "verbo": "動詞", "verbo negativo": "動詞の否定形", "verbo no passado": "動詞の過去形",
        },
        "patterns": [
            ["Qual hiragana tem o som “{0}”?", "「{0}」と読むひらがなはどれですか？"], ["Qual katakana tem o som “{0}”?", "「{0}」と読むカタカナはどれですか？"],
            ["Presente educado de {0} ({1}).", "「{0}」を「ます」形にしてください。"], ["Passado negativo de {0} ({1}).", "「{0}」を過去の否定形にしてください。"],
            ["Passado de {0} ({1}).", "「{0}」を過去形にしてください。"], ["Negativo de {0} ({1}): “{2}”.", "「{0}」を否定形にしてください。"],
            ["Negativo de {0} ({1}).", "「{0}」を否定形にしてください。"], ["Forma -te de {0} ({1}): “{2}”.", "「{0}」をて形にしてください（〜てください）。"],
            ["Diga “quero {1}” ({0}).", "「{0}」を「〜たいです」の形にしてください。"], ["Complete com {0} ({1}).", "「{0}」を正しい形にして入れてください。"],
            ["Como se diz “{0}”?", "日本語で何と言いますか？"],
        ],
    },
    "es": {
        "exact": {
            "Complete com gusta ou gustan.": "Completa con gusta o gustan.", "Complete as duas lacunas (ir e a + artigo).": "Completa los dos espacios (ir y a + artículo).",
            "artigo do lugar": "artículo del lugar", "a + artigo": "a + artículo", "estar": "estar", "gerúndio": "gerundio", "ir no presente": "ir en presente",
        },
        "patterns": [
            ["Presente de {0} ({1}).", "Presente de {0}."], ["Pretérito indefinido de {0} ({1}).", "Pretérito indefinido de {0}."],
            ["Pretérito imperfeito de {0} ({1}): hábito no passado.", "Pretérito imperfecto de {0}: costumbre en el pasado."],
            ["Complete a negação no passado ({0}).", "Completa la negación en pasado ({0})."],
            ["Complete as duas lacunas (verbo {0} e artigo).", "Completa los dos espacios (verbo {0} y artículo)."],
            ["Complete as lacunas (hábito no passado com {0}).", "Completa los espacios (costumbre en el pasado con {0})."],
            ["Complete as lacunas (verbo {0} e artigo do lugar).", "Completa los espacios (verbo {0} y artículo del lugar)."],
            ["Complete as três lacunas (verbo {0} no passado e artigos).", "Completa los tres espacios (verbo {0} en pasado y artículos)."],
            ["Complete o futuro próximo (ir a + {0}).", "Completa el futuro próximo (ir a + {0})."], ["Complete: estar + gerúndio de {0}.", "Completa: estar + gerundio de {0}."],
            ["Complete com o pronome ({0}).", "Completa con el pronombre ({0})."], ["Como se diz “{0}”?", "¿Cómo se dice en español?"],
            ["{0} no presente", "{0} en presente"], ["{0} no pretérito", "{0} en pretérito"], ["{0} no imperfeito", "{0} en imperfecto"],
        ],
    },
    "fr": {
        "exact": {
            "Complete as duas lacunas (aller e à + artigo).": "Complétez les deux blancs (aller et à + article).", "avoir": "avoir", "aller": "aller",
            "ne + avoir": "ne + avoir", "être": "être", "vouloir": "vouloir",
        },
        "patterns": [
            ["Presente de {0} ({1}).", "Présent de {0}."], ["Imparfait de {0} ({1}).", "Imparfait de {0}."], ["Futur proche de {0} ({1}).", "Futur proche de {0}."],
            ["Passé composé de {0} ({1}).", "Passé composé de {0}."], ["Complete (hábito no passado com {0}).", "Complétez (habitude passée avec {0})."],
            ["Complete a negação (ne … pas) com {0}.", "Complétez la négation (ne … pas) avec {0}."],
            ["Complete a negação no passé composé ({0}).", "Complétez la négation au passé composé ({0})."],
            ["Complete a pergunta (verbo {0} e artigo).", "Complétez la question (verbe {0} et article)."],
            ["Complete as duas lacunas (verbo {0} e artigo).", "Complétez les deux blancs (verbe {0} et article)."],
            ["Complete as três lacunas (passé composé de {0} e artigo).", "Complétez les trois blancs (passé composé de {0} et article)."],
            ["Complete o futur proche (aller + {0}).", "Complétez le futur proche (aller + {0})."], ["Complete: vouloir + {0}.", "Complétez : vouloir + {0}."],
            ["Complete: être en train de + {0}.", "Complétez : être en train de + {0}."], ["Como se diz “{0}”?", "Comment dit-on en français ?"],
            ["{0} no presente", "{0} au présent"], ["{0} no imparfait", "{0} à l'imparfait"],
        ],
    },
    "it": {
        "exact": {
            "Complete as duas lacunas (andare e preposição).": "Completa i due spazi (andare e preposizione).", "andare": "andare", "avere": "avere",
            "potere": "potere", "stare": "stare", "volere": "volere",
        },
        "patterns": [
            ["Presente de {0} ({1}).", "Presente di {0}."], ["Imperfetto de {0} ({1}).", "Imperfetto di {0}."], ["Futuro de {0} ({1}).", "Futuro di {0}."],
            ["Passato prossimo de {0} ({1}).", "Passato prossimo di {0}."], ["Complete (futuro de {0} e artigo).", "Completa (futuro di {0} e articolo)."],
            ["Complete (hábito no passado com {0}).", "Completa (abitudine passata con {0})."], ["Complete a negação (non + {0}).", "Completa la negazione (non + {0})."],
            ["Complete a negação no passato prossimo ({0}).", "Completa la negazione al passato prossimo ({0})."],
            ["Complete as duas lacunas (verbo {0} e artigo).", "Completa i due spazi (verbo {0} e articolo)."],
            ["Complete as três lacunas (passato prossimo de {0} e artigo).", "Completa i tre spazi (passato prossimo di {0} e articolo)."],
            ["Complete: non + potere + {0}.", "Completa: non + potere + {0}."], ["Complete: stare + gerundio de {0}.", "Completa: stare + gerundio di {0}."],
            ["Complete: volere + {0}.", "Completa: volere + {0}."], ["Como se diz “{0}”?", "Come si dice in italiano?"],
            ["{0} no presente", "{0} al presente"], ["{0} no imperfetto", "{0} all'imperfetto"], ["{0} no futuro", "{0} al futuro"],
        ],
    },
    "de": {
        "exact": {
            "kein": "kein", "gehen": "gehen", "können": "können", "möchten": "möchten", "werden": "werden", "wollen": "wollen",
        },
        "patterns": [
            ["Presente de {0} ({1}).", "Präsens von {0}."], ["Perfekt de {0} ({1}).", "Perfekt von {0}."], ["Futur de {0} ({1}).", "Futur von {0}."],
            ["Complete a negação com kein ({0}).", "Ergänze die Verneinung mit kein ({0})."],
            ["Complete as duas lacunas (verbo {0} e artigo).", "Ergänze die zwei Lücken (Verb {0} und Artikel)."],
            ["Complete o Perfekt de {0} (auxiliar e particípio).", "Ergänze das Perfekt von {0} (Hilfsverb und Partizip)."],
            ["Complete o Perfekt negativo de {0}.", "Ergänze das verneinte Perfekt von {0}."], ["Complete o futuro (werden + {0}).", "Ergänze das Futur (werden + {0})."],
            ["Complete: gehen + para onde? (acusativo).", "Ergänze: gehen + wohin? (Akkusativ)."], ["Complete: können + {0} (negativo).", "Ergänze: können + {0} (verneint)."],
            ["Complete: möchten + {0}.", "Ergänze: möchten + {0}."], ["Complete: verbo {0} + onde? (dativo).", "Ergänze: Verb {0} + wo? (Dativ)."],
            ["Complete: wollen + {0}.", "Ergänze: wollen + {0}."], ["Como se diz “{0}”?", "Wie sagt man das auf Deutsch?"],
            ["{0} no presente", "{0} im Präsens"],
        ],
    },
}
