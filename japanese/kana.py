"""Kana, leituras e romaji (Hepburn simplificado) do Japanese Routine.

- `to_romaji(kana)`: converte hiragana/katakana (っ dobra a consoante, ゃゅょ, ー repete a vogal,
  ん antes de vogal vira n').
- `reading(text)`: lê frases com kanji por dicionário (palavra mais longa primeiro); kanji sem
  leitura conhecida levanta erro, para não publicar pronúncia chutada.
- `romaji(text)`: romaji por palavra, separado por espaço; partículas は/へ/を como wa/e/o.
Vogais longas são escritas dobradas (kōhī → koohii) para facilitar a digitação.
"""
from __future__ import annotations

HIRAGANA = [
    ("あ", "a"), ("い", "i"), ("う", "u"), ("え", "e"), ("お", "o"), ("か", "ka"), ("き", "ki"), ("く", "ku"), ("け", "ke"), ("こ", "ko"),
    ("さ", "sa"), ("し", "shi"), ("す", "su"), ("せ", "se"), ("そ", "so"), ("た", "ta"), ("ち", "chi"), ("つ", "tsu"), ("て", "te"), ("と", "to"),
    ("な", "na"), ("に", "ni"), ("ぬ", "nu"), ("ね", "ne"), ("の", "no"), ("は", "ha"), ("ひ", "hi"), ("ふ", "fu"), ("へ", "he"), ("ほ", "ho"),
    ("ま", "ma"), ("み", "mi"), ("む", "mu"), ("め", "me"), ("も", "mo"), ("や", "ya"), ("ゆ", "yu"), ("よ", "yo"),
    ("ら", "ra"), ("り", "ri"), ("る", "ru"), ("れ", "re"), ("ろ", "ro"), ("わ", "wa"), ("を", "o"), ("ん", "n"),
]
DAKUTEN = [
    ("が", "ga"), ("ぎ", "gi"), ("ぐ", "gu"), ("げ", "ge"), ("ご", "go"), ("ざ", "za"), ("じ", "ji"), ("ず", "zu"), ("ぜ", "ze"), ("ぞ", "zo"),
    ("だ", "da"), ("ぢ", "ji"), ("づ", "zu"), ("で", "de"), ("ど", "do"), ("ば", "ba"), ("び", "bi"), ("ぶ", "bu"), ("べ", "be"), ("ぼ", "bo"),
    ("ぱ", "pa"), ("ぴ", "pi"), ("ぷ", "pu"), ("ぺ", "pe"), ("ぽ", "po"),
]
YOON = [
    ("きゃ", "kya"), ("きゅ", "kyu"), ("きょ", "kyo"), ("しゃ", "sha"), ("しゅ", "shu"), ("しょ", "sho"), ("ちゃ", "cha"), ("ちゅ", "chu"), ("ちょ", "cho"),
    ("にゃ", "nya"), ("にゅ", "nyu"), ("にょ", "nyo"), ("ひゃ", "hya"), ("ひゅ", "hyu"), ("ひょ", "hyo"), ("みゃ", "mya"), ("みゅ", "myu"), ("みょ", "myo"),
    ("りゃ", "rya"), ("りゅ", "ryu"), ("りょ", "ryo"), ("ぎゃ", "gya"), ("ぎゅ", "gyu"), ("ぎょ", "gyo"), ("じゃ", "ja"), ("じゅ", "ju"), ("じょ", "jo"),
    ("びゃ", "bya"), ("びゅ", "byu"), ("びょ", "byo"), ("ぴゃ", "pya"), ("ぴゅ", "pyu"), ("ぴょ", "pyo"),
]
# Combinações só do katakana (palavras estrangeiras).
KATAKANA_EXTRA = [("ティ", "ti"), ("ディ", "di"), ("ファ", "fa"), ("フィ", "fi"), ("フェ", "fe"), ("フォ", "fo"), ("ウィ", "wi"), ("ウェ", "we"),
                  ("ウォ", "wo"), ("シェ", "she"), ("ジェ", "je"), ("チェ", "che"), ("ヴァ", "va"), ("ヴ", "vu"), ("デュ", "dyu")]


def kata(h: str) -> str:
    return "".join(chr(ord(c) + 0x60) if "ぁ" <= c <= "ゖ" else c for c in h)


def hira(k: str) -> str:
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in k)


TABLE = {}
for k, r in HIRAGANA + DAKUTEN + YOON:
    TABLE[k] = r
    TABLE[kata(k)] = r
TABLE["を"] = TABLE["ヲ"] = "o"
for k, r in KATAKANA_EXTRA:
    TABLE[k] = r
VOWEL_OF = lambda r: r[-1] if r and r[-1] in "aeiou" else ""


def to_romaji(text: str) -> str:
    out = ""
    i = 0
    double = False
    while i < len(text):
        two, one = text[i:i + 2], text[i]
        if one in "っッ":
            double = True
            i += 1
            continue
        if one == "ー":
            out += VOWEL_OF(out)
            i += 1
            continue
        if two in TABLE:
            r, i = TABLE[two], i + 2
        elif one in TABLE:
            r, i = TABLE[one], i + 1
        else:
            r, i = one, i + 1
        if double and r:
            r = ("t" + r) if r.startswith("ch") else (r[0] + r)
            double = False
        out += r
    # ん antes de vogal ou y: n' (kin'en)
    return out


def _romaji_kana(kana: str) -> str:
    res, i = [], 0
    while i < len(kana):
        two, one = kana[i:i + 2], kana[i]
        if one in "んン" and i + 1 < len(kana) and to_romaji(kana[i + 1])[:1] in ("a", "i", "u", "e", "o", "y"):
            res.append("n'")
            i += 1
            continue
        step = 2 if two in TABLE else 1
        # っ e ー dependem do vizinho: converte em bloco
        j = i + step
        while j < len(kana) and kana[j] in "ー":
            j += 1
        if one in "っッ":
            j = min(len(kana), i + 1 + (2 if kana[i + 1:i + 3] in TABLE else 1))
        res.append(to_romaji(kana[i:j]))
        i = j
    return "".join(res)


# Leituras: palavras em kanji/kana -> kana. Partículas isoladas com a leitura de partícula.
PARTICLES = {"は": "wa", "へ": "e", "を": "o"}
# Saudações que terminam na partícula は (lida wa).
ROMAJI_OVERRIDE = {"こんにちは": "konnichiwa", "こんばんは": "konbanwa", "トイレはどこですか": "toire wa doko desu ka",
                   "これをください": "kore o kudasai", "いくらですか": "ikura desu ka"}
READINGS: dict[str, str] = {}


def add_readings(entries):
    for word, kana in entries:
        READINGS.setdefault(word, kana)


def is_kanji(ch: str) -> bool:
    return "一" <= ch <= "鿿" or ch == "々"


def is_kana(ch: str) -> bool:
    return "぀" <= ch <= "ヿ"


PUNCT = {"。": ".", "、": ",", "：": ":", "？": "?", "！": "!", "「": "“", "」": "”", "・": "·", "（": "(", "）": ")", "〜": "~", "…": "…"}


def _dict_match(text, i, maxlen):
    """Palavra do dicionário mais longa em i. Entradas de 1 kana só valem para partículas."""
    for size in range(min(maxlen, len(text) - i), 0, -1):
        w = text[i:i + size]
        if w in READINGS and (size > 1 or is_kanji(w)):
            return w
    return None


# Partículas que separam palavras quando aparecem soltas depois de outra palavra.
SPLIT_PARTICLES = ["から", "まで", "は", "が", "を", "に", "で", "へ", "と", "も", "の", "か", "ね", "よ"]
FINAL_ONLY = {"か", "ね", "よ"}  # só no fim da frase (ですか, ですね)


def _particle_at(text, i):
    for p in SPLIT_PARTICLES:
        if text.startswith(p, i):
            after = text[i + len(p):i + len(p) + 1]
            if p in FINAL_ONLY and after and after not in PUNCT:
                continue
            return p
    return None


def tokens(text: str):
    """Segmenta a frase em palavras, partículas e pontuação.

    1. Palavra do dicionário (kanji ou kana com 2+ caracteres), a mais longa primeiro.
    2. Partícula solta depois de uma palavra.
    3. Kana restante vira um bloco; se vier logo depois de um radical em kanji,
       é terminação (食べ+ます, 高+くない) e gruda nele.
    """
    maxlen = max(len(k) for k in READINGS) if READINGS else 1
    i, out, missing = 0, [], []
    while i < len(text):
        ch = text[i]
        if ch in PUNCT or ch.isspace():
            out.append(("punct", ch))
            i += 1
            continue
        if not (is_kanji(ch) or is_kana(ch)):
            j = i + 1  # trecho em letras latinas (K-POP, M) fica inteiro
            while j < len(text) and not (is_kanji(text[j]) or is_kana(text[j]) or text[j] in PUNCT or text[j].isspace()):
                j += 1
            out.append(("latin", text[i:j]))
            i = j
            continue
        w = _dict_match(text, i, maxlen)
        if w:
            out.append(("word", w, READINGS[w]))
            i += len(w)
            continue
        if is_kanji(ch):
            missing.append(ch)
            i += 1
            continue
        particle = _particle_at(text, i)
        if particle and out and out[-1][0] in ("word", "particle", "latin"):
            out.append(("particle", particle))
            i += len(particle)
            continue
        j = i + 1
        while j < len(text) and is_kana(text[j]) and not _dict_match(text, j, maxlen) \
                and not any(text.startswith(p, j) for p in SPLIT_PARTICLES):
            j += 1
        chunk = text[i:j]
        prev = out[-1] if out else None
        okurigana = all("ぁ" <= c <= "ゟ" for c in chunk)
        if okurigana and prev and prev[0] == "word" and any(is_kanji(c) for c in prev[1]):
            out[-1] = ("word", prev[1] + chunk, prev[2] + chunk)
        else:
            out.append(("word", chunk, chunk))
        i = j
    if missing:
        raise KeyError(f"Sem leitura para: {''.join(dict.fromkeys(missing))} (em “{text}”)")
    return out


def reading(text: str) -> str:
    return "".join(t[2] if t[0] == "word" else t[1] for t in tokens(text))



def romaji(text: str) -> str:
    if text in PARTICLES:  # partícula sozinha numa opção: は → wa, へ → e
        return PARTICLES[text]
    parts = []
    for t in tokens(text):
        if t[0] == "word":
            parts.append(ROMAJI_OVERRIDE.get(t[1]) or _romaji_kana(t[2]))
        elif t[0] == "particle":
            parts.append(PARTICLES.get(t[1], _romaji_kana(t[1])))
        elif t[0] == "latin":
            parts.append(t[1])
        elif t[1] in PUNCT:
            if parts:
                parts[-1] += PUNCT[t[1]]
    return " ".join(parts)
