"""Gera public/korean.html (Korean Routine) a partir de content.py + src/.

Rode: python korean/build_korean.py
IDs são estáveis (prefixo por módulo + ordem fixa) para preservar o histórico.
"""
from __future__ import annotations

import random
from pathlib import Path

import sys

import content as C
import extend
import skills_content as SK
from romanize import has_syllable, romanize

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from practice.build import build_app  # noqa: E402
from skills.build import skills_bundle  # noqa: E402
PUBLIC = ROOT.parent / "public"
PAGE = {
    "code": "ko", "html_lang": "ko", "brand": "Korean Routine", "brand_word": "korean", "name": "coreano",
    "alphabet_tab": "Hangul", "eyebrow": "Coreano todos os dias · TOPIK 1–2", "headline": "안녕하세요! Vamos treinar.",
    "intro": "questões de hangul, vocabulário, partículas, verbos, frases para completar, números e escuta — com temas de K-pop e dorama. Responda escolhendo ou digitando em hangul.",
    "level_prefix": "TOPIK", "typing_label": "Digitar em hangul",
    "typing_hint": "Para digitar em hangul, ative o teclado coreano: no Windows, Configurações › Hora e idioma › Idioma › Adicionar “Coreano” (alterne com Win + Espaço e use a tecla 한/영 ou Alt direito); no celular, adicione o teclado coreano.",
    "lang_js": ROOT / "lang.js", "alphabet_html": ROOT / "alphabet.html",
}


def has_batchim(word: str) -> bool:
    last = word.strip()[-1]
    code = ord(last) - 0xAC00
    return 0 <= code < 11172 and code % 28 != 0


def batchim_is_rieul(word: str) -> bool:
    code = ord(word.strip()[-1]) - 0xAC00
    return 0 <= code < 11172 and code % 28 == 8


def pick(rng, pool, exclude, n=3):
    pool = [p for p in dict.fromkeys(pool) if p not in exclude]
    rng.shuffle(pool)
    return pool[:n]


def build():
    rng = random.Random(20261023)
    questions = []

    def add(prefix, module, level, theme, prompt, text, answers, distractors, explanation, audio=None, roman=None, slots=None):
        answers = list(dict.fromkeys(answers))
        distractors = [d for d in dict.fromkeys(distractors) if d not in answers]
        assert len(distractors) >= 1, (prefix, text)
        serial = sum(1 for q in questions if q["id"].startswith(prefix)) + 1
        question = {
            "id": f"{prefix}{serial:04d}", "module": module, "level": level, "theme": theme,
            "prompt": prompt, "text": text, "answers": answers, "distractors": distractors,
            "explanation": explanation, "audio": audio, "roman": roman,
        }
        if slots:
            question["slots"] = slots
        questions.append(question)

    def slot(right, wrong, label):
        return {"answers": [right], "distractors": [w for w in dict.fromkeys(wrong) if w != right], "label": label}

    # ---------------------------------------------------------- hangul: letras
    cons_rr = [rr for _, rr, _ in C.CONSONANTS]
    for letter, rr, name in C.CONSONANTS:
        add("kh", "hangul", 1, "consoantes", "Qual é o som desta consoante?", letter, [rr],
            pick(rng, cons_rr, [rr]), f"{letter} ({name}) soa como “{rr}”.", audio=None)
        add("kh", "hangul", 1, "consoantes", f"Qual letra tem o som “{rr}”?", rr, [letter],
            pick(rng, [c for c, _, _ in C.CONSONANTS], [letter]), f"O som “{rr}” é escrito {letter} ({name}).")
    vow_rr = [rr for _, rr in C.VOWELS]
    for letter, rr in C.VOWELS:
        add("kh", "hangul", 1, "vogais", "Qual é o som desta vogal?", letter, [rr],
            pick(rng, vow_rr, [rr]), f"{letter} soa como “{rr}”.")
        add("kh", "hangul", 1, "vogais", f"Qual vogal tem o som “{rr}”?", rr, [letter],
            pick(rng, [v for v, _ in C.VOWELS], [letter]), f"O som “{rr}” é escrito {letter}.")

    # ---------------------------------------------------------- hangul: sílabas
    def syllable(initial, vowel):
        return chr(0xAC00 + (C.INITIALS.index(initial) * 21 + C.MEDIALS.index(vowel)) * 28)

    for initial in C.SYLLABLE_INITIALS:
        for vowel in C.SYLLABLE_VOWELS:
            if (C.SYLLABLE_INITIALS.index(initial) + C.SYLLABLE_VOWELS.index(vowel)) % 2:
                continue  # metade das combinações basta para treinar sem repetir demais
            syl = syllable(initial, vowel)
            rr = C.INITIAL_RR[initial] + C.VOWEL_RR[vowel]
            wrong = []
            for other in C.SYLLABLE_VOWELS:
                if other != vowel:
                    wrong.append(C.INITIAL_RR[initial] + C.VOWEL_RR[other])
            for other in C.SYLLABLE_INITIALS:
                if C.INITIAL_RR[other] != C.INITIAL_RR[initial]:
                    wrong.append(C.INITIAL_RR[other] + C.VOWEL_RR[vowel])
            add("ks", "leitura", 1, "sílabas", "Como se lê esta sílaba?", syl, [rr], pick(rng, wrong, [rr]),
                f"{syl} = {initial} + {vowel} → “{rr}”.", audio=syl)

    # ---------------------------------------------------------- leitura de palavras
    word_rr = [rr for _, rr in C.READING_WORDS]
    for word, rr in C.READING_WORDS:
        add("kw", "leitura", 1, "palavras", "Como se lê esta palavra?", word, [rr], pick(rng, word_rr, [rr]),
            f"{word} lê-se “{rr}” (romanização revisada, que segue a pronúncia).", audio=word)

    # ---------------------------------------------------------- vocabulário
    by_theme = {}
    for ko, pt, theme, level in C.VOCAB:
        by_theme.setdefault(theme, []).append((ko, pt))
    for ko, pt, theme, level in C.VOCAB:
        same = by_theme[theme]
        add("kv", "vocabulario", level, theme, "O que significa?", ko, [pt],
            pick(rng, [p for _, p in same], [pt]), f"{ko} = {pt}.", audio=ko)
        add("kv", "vocabulario", level, theme, "Como se diz em coreano?", pt, [ko],
            pick(rng, [k for k, _ in same], [ko]), f"“{pt}” em coreano é {ko}.", audio=ko)
    verb_pt = [(v[0], v[1]) for v in C.VERBS] + [(a[0], a[1]) for a in C.ADJECTIVES]
    for ko, pt in verb_pt:
        add("kv", "vocabulario", 1, "verbos", "O que significa?", ko, [pt],
            pick(rng, [p for _, p in verb_pt], [pt]), f"{ko} = {pt} (forma de dicionário).", audio=ko)

    # ---------------------------------------------------------- escuta
    listening = [v for v in C.VOCAB if v[3] == 1]
    rng_l = random.Random(7)
    rng_l.shuffle(listening)
    for ko, pt, theme, level in listening[:120]:
        same = [k for k, _ in by_theme[theme]]
        add("kl", "escuta", level, theme, "Ouça e escolha a palavra que você ouviu.", "🔊", [ko],
            pick(rng, same, [ko]), f"Você ouviu {ko} ({pt}).", audio=ko)

    # ---------------------------------------------------------- partículas
    def particle(word, with_b, without_b):
        return with_b if has_batchim(word) else without_b

    people = ["학생", "가수", "배우", "의사", "선생님", "팬", "연습생", "회사원"]
    for noun in people:
        right = particle(noun, "이에요", "예요")
        wrong = "예요" if right == "이에요" else "이에요"
        add("kp", "particulas", 1, "ser", "Complete com a forma correta de “ser”.", f"저는 {noun}___.",
            [right], [wrong, "을", "에서"], f"{noun} {'termina' if has_batchim(noun) else 'não termina'} em consoante → {right}.")
    things = ["책", "가방", "우산", "시계", "휴대폰", "컴퓨터", "의자", "사진", "선물", "열쇠", "안경", "모자", "신발", "편지"]
    for noun in things:
        right = particle(noun, "이에요", "예요")
        wrong = "예요" if right == "이에요" else "이에요"
        add("kp", "particulas", 1, "ser", "Complete com a forma correta de “ser”.", f"이것은 {noun}___.",
            [right], [wrong, "를", "에"], f"{noun} {'tem' if has_batchim(noun) else 'não tem'} batchim → {right}.")
    places = ["집", "학교", "회사", "병원", "은행", "식당", "카페", "시장", "공원", "도서관", "화장실", "공항", "호텔", "노래방"]
    for noun in places:
        right = particle(noun, "이에요", "예요")
        wrong = "예요" if right == "이에요" else "이에요"
        add("kp", "particulas", 1, "ser", "Complete com a forma correta de “ser”.", f"여기는 {noun}___.",
            [right], [wrong, "을", "에서"], f"{noun} → {right}.")

    topic_people = ["저", "친구", "동생", "선생님", "언니", "형", "엄마", "아빠", "학생", "가수"]
    predicate = {"저": "한국 사람이 아니에요", "친구": "대학생이에요", "동생": "학생이에요", "선생님": "한국 사람이에요",
                 "언니": "회사원이에요", "형": "의사예요", "엄마": "요리사예요", "아빠": "선생님이에요",
                 "학생": "열 명이에요", "가수": "아주 유명해요"}
    for noun in topic_people:
        right = particle(noun, "은", "는")
        wrong = "는" if right == "은" else "은"
        add("kp", "particulas", 1, "tópico", "Complete com a partícula de tópico.", f"{noun}___ {predicate[noun]}.",
            [right], [wrong, "을", "에"], f"Tópico: {'com' if has_batchim(noun) else 'sem'} batchim → {right}.")

    subject_pairs = [("김치", "맛있어요"), ("떡볶이", "매워요"), ("커피", "뜨거워요"), ("라면", "싸요"), ("빵", "맛있어요"),
                     ("날씨", "좋아요"), ("가방", "커요"), ("방", "작아요"), ("시험", "어려워요"), ("드라마", "재미있어요"),
                     ("콘서트 표", "비싸요"), ("머리", "아파요"), ("사람", "많아요"), ("시간", "있어요"), ("돈", "없어요"),
                     ("동생", "있어요"), ("꽃", "예뻐요"), ("무대", "멋있어요"), ("바다", "아름다워요"), ("우산", "없어요")]
    for noun, pred in subject_pairs:
        right = particle(noun, "이", "가")
        wrong = "가" if right == "이" else "이"
        add("kp", "particulas", 1, "sujeito", "Complete com a partícula de sujeito.", f"{noun}___ {pred}.",
            [right], [wrong, "를" if right == "가" else "을", "에서"], f"Sujeito: {'com' if has_batchim(noun) else 'sem'} batchim → {right}.")

    object_pairs = [("김치", "먹어요"), ("커피", "마셔요"), ("드라마", "봐요"), ("노래", "들어요"), ("책", "읽어요"),
                    ("편지", "써요"), ("친구", "만나요"), ("한국어", "공부해요"), ("옷", "사요"), ("춤", "배워요"),
                    ("사진", "찍어요"), ("김밥", "만들어요"), ("문", "열어요"), ("창문", "닫아요"), ("메시지", "보내요"),
                    ("방", "청소해요"), ("버스", "기다려요"), ("물", "마셔요"), ("영화", "봐요"), ("빵", "먹어요"),
                    ("케이팝", "좋아해요"), ("손", "씻어요"), ("우유", "마셔요"), ("앨범", "사요"), ("뮤직비디오", "봐요")]
    for noun, verb in object_pairs:
        right = particle(noun, "을", "를")
        wrong = "를" if right == "을" else "을"
        add("kp", "particulas", 1, "objeto", "Complete com a partícula de objeto.", f"{noun}___ {verb}.",
            [right], [wrong, "에", "에서"], f"Objeto direto: {'com' if has_batchim(noun) else 'sem'} batchim → {right}.")

    for sentence, right in C.LOCATION_SENTENCES:
        wrong = "에서" if right == "에" else "에"
        add("kp", "particulas", 1, "lugar", "Escolha 에 ou 에서.", sentence, [right], [wrong],
            "에 indica destino ou onde algo está; 에서, o lugar onde a ação acontece.")

    with_pairs = [("빵", "우유를 사요"), ("엄마", "아빠는 집에 있어요"), ("김치", "밥을 먹어요"), ("커피", "케이크를 주문해요"),
                  ("친구", "같이 가요"), ("책", "펜이 있어요"), ("사과", "딸기를 좋아해요"), ("형", "누나가 있어요"),
                  ("라면", "김밥을 먹어요"), ("가방", "우산을 샀어요")]
    for noun, rest in with_pairs:
        right = particle(noun, "과", "와")
        wrong = "와" if right == "과" else "과"
        add("kp", "particulas", 1, "e/com", "Complete com 와 ou 과 (e / com).", f"{noun}___ {rest}.",
            [right], [wrong, "을" if right == "과" else "를"], f"{'Com' if has_batchim(noun) else 'Sem'} batchim → {right}. Na fala, 하고 também é usado.")

    for noun in C.INSTRUMENT_NOUNS:
        right = "로" if (not has_batchim(noun) or batchim_is_rieul(noun)) else "으로"
        wrong = "으로" if right == "로" else "로"
        add("kp", "particulas", 1, "meio", "Complete com 로 ou 으로 (por meio de).", f"{noun}___ {C.INSTRUMENT_VERB[noun]}.",
            [right], [wrong, "에서"], "Sem batchim ou terminado em ㄹ → 로; outros → 으로.")

    # ---------------------------------------------------------- verbos e adjetivos
    past_time = {"살다": "작년에", "좋아하다": "예전에"}
    future_time = {"살다": "내년에"}
    no_want = {"좋아하다", "울다"}
    for dic, pt, comp, pres, past, fut, neg in C.VERBS:
        forms = [pres, past] + ([fut] if fut else [])
        stem = dic[:-1]
        bad = stem + "요"
        add("kg", "verbos", 1, "presente", f"Presente educado de {dic} ({pt}).", f"저는 매일 {comp} ___.",
            [pres], [f for f in forms if f != pres] + [bad], "Presente educado: -아요/-어요 (하다 → 해요).", audio=f"저는 매일 {comp} {pres}.")
        add("kg", "verbos", 1, "passado", f"Passado de {dic} ({pt}).", f"{past_time.get(dic, '어제')} {comp} ___.",
            [past], [f for f in forms if f != past] + [stem + "었요"], "Passado: -았어요/-었어요 (하다 → 했어요).", audio=f"{past_time.get(dic, '어제')} {comp} {past}.")
        if fut:
            add("kg", "verbos", 1, "futuro", f"Futuro de {dic} ({pt}).", f"{future_time.get(dic, '내일')} {comp} ___.",
                [fut], [pres, past, stem + "을 거예요" if not has_batchim(stem) else stem + "ㄹ 거예요"],
                "Futuro: -(으)ㄹ 거예요.", audio=f"{future_time.get(dic, '내일')} {comp} {fut}.")
        if dic not in no_want:
            want = stem + "고 싶어요"
            add("kg", "verbos", 1, "querer", f"Diga “quero {pt}”.", f"{comp} ___.",
                [want], [stem + "고 있어요", pres, stem + "싶어요"], "Querer: radical + 고 싶어요.", audio=f"{comp} {want}.")
        add("kg", "verbos", 1, "negação", f"Negue: “não {pt}”.", f"저는 {comp} ___.",
            [neg], [pres, "안 " + bad, neg.replace("안 ", "") + " 안"], "Negação curta: 안 antes do verbo (em X하다 separável: X 안 해요).",
            audio=f"저는 {comp} {neg}.")
    for dic, pt, pres, past in C.ADJECTIVES:
        subj = C.ADJECTIVE_SENTENCES[dic]
        stem = dic[:-1]
        add("kg", "verbos", 1, "adjetivos", f"Presente de {dic} ({pt}).", f"{subj} ___.",
            [pres], [past, stem + "요", dic], "Adjetivos coreanos se conjugam como verbos.", audio=f"{subj} {pres}.")
        add("kg", "verbos", 2, "adjetivos", f"Passado de {dic} ({pt}).", f"어제 {subj} ___.",
            [past], [pres, dic, stem + "었요"], "Passado de adjetivo: -았어요/-었어요.", audio=f"어제 {subj} {past}.")

    # ---------------------------------------------------------- completar (2–3 lacunas)
    # Mesma ideia das combinações do inglês: várias lacunas na mesma frase.
    def topic_slot(noun):
        right = particle(noun, "은", "는")
        return slot(right, ["는" if right == "은" else "은", particle(noun, "을", "를")], "tópico")

    def object_slot(noun):
        right = particle(noun, "을", "를")
        return slot(right, ["를" if right == "을" else "을", "에", particle(noun, "이", "가")], "objeto")

    place_slot = slot("에서", ["에", "로"], "lugar da ação")
    for place, obj, dic, pres, past, fut in C.COMBO_ACTIVITIES:
        for subj in C.COMBO_SUBJECTS:
            slots = [topic_slot(subj), place_slot, object_slot(obj)]
            joined = [s["answers"][0] for s in slots]
            full = f"{subj}{joined[0]} {place}{joined[1]} {obj}{joined[2]} {pres}."
            add("kc", "completar", 2, "partículas", "Complete as três lacunas (tópico, lugar e objeto).",
                f"{subj}___ {place}___ {obj}___ {pres}.", [" · ".join(joined)], ["-"],
                f"{subj}{joined[0]}: tópico ({'com' if has_batchim(subj) else 'sem'} batchim). {place}에서: lugar onde a ação acontece. "
                f"{obj}{joined[2]}: objeto ({'com' if has_batchim(obj) else 'sem'} batchim).", audio=full, slots=slots)
        for subj in C.COMBO_SUBJECTS:
            slots = [topic_slot(subj), object_slot(obj), slot(past, [pres, fut, dic], f"{dic} no passado")]
            joined = [s["answers"][0] for s in slots]
            full = f"어제 {subj}{joined[0]} {obj}{joined[1]} {past}."
            add("kc", "completar", 2, "passado", f"Complete as lacunas. Use {dic} no passado.",
                f"어제 {subj}___ {obj}___ ___.", [" · ".join(joined)], ["-"],
                f"어제 (ontem) pede passado: {dic} → {past}. Partículas: {subj}{joined[0]}, {obj}{joined[1]}.", audio=full, slots=slots)
        for subj in C.COMBO_SUBJECTS:
            slots = [topic_slot(subj), object_slot(obj)]
            joined = [s["answers"][0] for s in slots]
            full = f"내일 {subj}{joined[0]} {obj}{joined[1]} {fut}."
            add("kc", "completar", 1, "futuro", "Complete as duas lacunas.",
                f"내일 {subj}___ {obj}___ {fut}.", [" · ".join(joined)], ["-"],
                f"{subj}{joined[0]}: tópico. {obj}{joined[1]}: objeto. {fut} = futuro de {dic}.", audio=full, slots=slots)

    # ---------------------------------------------------------- números
    for ko, pt, wrong in C.NUMBERS:
        add("kn", "numeros", 1, "números", f"Como se diz “{pt}”?", pt, [ko], wrong,
            "Nativos para horas, idade e contadores; sino-coreanos para minutos, dinheiro e datas.", audio=ko)

    # ---------------------------------------------------------- frases
    for ko, pt, ctx in C.PHRASES:
        others_pt = [p for _, p, _ in C.PHRASES if p != pt]
        others_ko = [k for k, _, _ in C.PHRASES if k != ko]
        note = f" ({ctx})" if ctx else ""
        add("kf", "frases", 1, "frases", "O que significa?", ko, [pt], pick(rng, others_pt, [pt]), f"{ko} = {pt}{note}.", audio=ko)
        add("kf", "frases", 1, "frases", "Como se diz em coreano?", pt, [ko], pick(rng, others_ko, [ko]), f"{pt} = {ko}{note}.", audio=ko)

    # Expansão (~10 mil): sempre depois das originais, com prefixos novos.
    extend.build_more(add, slot, particle, has_batchim, pick, rng, C)
    return questions


def validate(questions):
    ids = [q["id"] for q in questions]
    assert len(ids) == len(set(ids)), "IDs repetidos"
    for q in questions:
        assert q["answers"] and q["distractors"], q["id"]
        assert not set(q["answers"]) & set(q["distractors"]), q["id"]
        if q.get("slots"):
            assert q["text"].count("___") == len(q["slots"]) >= 2, q["id"]
            for s in q["slots"]:
                assert s["answers"] and s["distractors"], q["id"]
                assert not set(s["answers"]) & set(s["distractors"]), q["id"]
        elif "___" in q["text"]:
            assert q["text"].count("___") == 1, q["id"]
    # partículas: conferência independente da regra do batchim
    assert has_batchim("학생") and not has_batchim("가수") and batchim_is_rieul("지하철")


def listen_choice(questions):
    """Ouça e escolha: frases completas que diferem só na lacuna (partícula ou verbo)."""
    items = []
    for q in questions:
        if q["module"] not in ("verbos", "particulas") or q.get("slots") or q["text"].count("___") != 1:
            continue
        answer = q["text"].replace("___", q["answers"][0])
        options = [answer] + [q["text"].replace("___", d) for d in q["distractors"][:3]]
        options = list(dict.fromkeys(options))
        if len(options) >= 3 and has_syllable(answer):
            items.append({"answer": answer, "options": options, "explanation": q["explanation"]})
    return items


def roman_map(questions):
    """Pronúncia escrita das opções em hangul (mostrada abaixo de cada botão)."""
    out = {}
    for q in questions:
        if q["module"] in ("hangul", "leitura"):
            continue  # ali a romanização é a própria resposta
        options = q["answers"] + q["distractors"]
        for s in q.get("slots", []):
            options += s["answers"] + s["distractors"]
        for o in options:
            if has_syllable(o) and o not in out:
                out[o] = romanize(o.replace("?", "").replace("!", "").replace(",", ""))
    return out


MODULES = {
    "hangul": "Hangul (letras)", "leitura": "Leitura", "vocabulario": "Vocabulário", "escuta": "Escuta",
    "particulas": "Partículas", "verbos": "Verbos e adjetivos", "completar": "Completar frases (2–3 lacunas)", "numeros": "Números",
    "frases": "Frases do dia a dia",
}


def main():
    questions = build()
    validate(questions)
    data = {
        "questions": questions, "modules": MODULES, "guide": C.GUIDE,
        "consonants": C.CONSONANTS, "vowels": C.VOWELS, "roman": roman_map(questions),
    }
    choice = listen_choice(questions)
    data["skills"], _, _ = skills_bundle(SK.TEXTS, SK.PROMPTS, SK.ROLEPLAY, choice, romanize)
    for item in choice:
        for o in item["options"]:
            data["roman"].setdefault(o, romanize(o))
    build_app(PAGE, data, PUBLIC / "korean.html")
    counts = {}
    for q in questions:
        counts[q["module"]] = counts.get(q["module"], 0) + 1
    print(f"korean.html: {len(questions)} questões", counts)


if __name__ == "__main__":
    main()
