"""Romanização revisada (RR) seguindo a pronúncia, para mostrar abaixo das opções.

Cobre as regras que aparecem no conteúdo TOPIK 1–2: ligação (연음), neutralização
do batchim, nasalização, ㄹ duplo, aspiração com ㅎ e palatalização (같이 → gachi).
Cada palavra (separada por espaço) é romanizada isoladamente, como na RR oficial.
"""
from __future__ import annotations

INITIALS = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
MEDIALS = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
FINALS = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ",
          "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

INITIAL_RR = {"ㄱ": "g", "ㄲ": "kk", "ㄴ": "n", "ㄷ": "d", "ㄸ": "tt", "ㄹ": "r", "ㅁ": "m", "ㅂ": "b", "ㅃ": "pp",
              "ㅅ": "s", "ㅆ": "ss", "ㅇ": "", "ㅈ": "j", "ㅉ": "jj", "ㅊ": "ch", "ㅋ": "k", "ㅌ": "t", "ㅍ": "p", "ㅎ": "h"}
VOWEL_RR = {"ㅏ": "a", "ㅐ": "ae", "ㅑ": "ya", "ㅒ": "yae", "ㅓ": "eo", "ㅔ": "e", "ㅕ": "yeo", "ㅖ": "ye", "ㅗ": "o",
            "ㅘ": "wa", "ㅙ": "wae", "ㅚ": "oe", "ㅛ": "yo", "ㅜ": "u", "ㅝ": "wo", "ㅞ": "we", "ㅟ": "wi", "ㅠ": "yu",
            "ㅡ": "eu", "ㅢ": "ui", "ㅣ": "i"}
# Batchim pronunciado quando não há ligação: representante sonoro.
FINAL_SOUND = {"ㄱ": "ㄱ", "ㄲ": "ㄱ", "ㅋ": "ㄱ", "ㄳ": "ㄱ", "ㄺ": "ㄱ", "ㄴ": "ㄴ", "ㄵ": "ㄴ", "ㄶ": "ㄴ",
               "ㄷ": "ㄷ", "ㅅ": "ㄷ", "ㅆ": "ㄷ", "ㅈ": "ㄷ", "ㅊ": "ㄷ", "ㅌ": "ㄷ", "ㅎ": "ㄷ", "ㄹ": "ㄹ",
               "ㄼ": "ㄹ", "ㄽ": "ㄹ", "ㄾ": "ㄹ", "ㅀ": "ㄹ", "ㅁ": "ㅁ", "ㄻ": "ㅁ", "ㅂ": "ㅂ", "ㅍ": "ㅂ",
               "ㅄ": "ㅂ", "ㄿ": "ㅂ", "ㅇ": "ㅇ"}
FINAL_RR = {"ㄱ": "k", "ㄴ": "n", "ㄷ": "t", "ㄹ": "l", "ㅁ": "m", "ㅂ": "p", "ㅇ": "ng"}
# Batchim duplo: (fica, passa para a próxima sílaba na ligação)
SPLIT = {"ㄳ": ("ㄱ", "ㅅ"), "ㄵ": ("ㄴ", "ㅈ"), "ㄶ": ("ㄴ", "ㅎ"), "ㄺ": ("ㄹ", "ㄱ"), "ㄻ": ("ㄹ", "ㅁ"),
         "ㄼ": ("ㄹ", "ㅂ"), "ㄽ": ("ㄹ", "ㅅ"), "ㄾ": ("ㄹ", "ㅌ"), "ㄿ": ("ㄹ", "ㅍ"), "ㅀ": ("ㄹ", "ㅎ"),
         "ㅄ": ("ㅂ", "ㅅ")}
ASPIRATE = {"ㄱ": "ㅋ", "ㄷ": "ㅌ", "ㅂ": "ㅍ", "ㅈ": "ㅊ"}


def _syllables(word):
    out = []
    for ch in word:
        code = ord(ch) - 0xAC00
        if 0 <= code < 11172:
            out.append([INITIALS[code // 588], MEDIALS[(code % 588) // 28], FINALS[code % 28]])
        else:
            out.append(ch)
    return out


def _word(word: str) -> str:
    syl = _syllables(word)
    # Regras entre o batchim de uma sílaba e a inicial da seguinte.
    for i in range(len(syl) - 1):
        a, b = syl[i], syl[i + 1]
        if isinstance(a, str) or isinstance(b, str) or not a[2]:
            continue
        final, initial = a[2], b[0]
        if initial == "ㅇ" and final != "ㅇ":
            if final in SPLIT:
                stay, move = SPLIT[final]
                a[2] = stay
                b[0] = "" if move == "ㅎ" else move
            elif final == "ㅎ":
                a[2] = ""
            else:
                a[2] = ""
                b[0] = final
            # palatalização: 같이 → 가치, 굳이 → 구지
            if b[1] == "ㅣ" and b[0] in ("ㄷ", "ㅌ"):
                b[0] = "ㅈ" if b[0] == "ㄷ" else "ㅊ"
            if not b[0]:
                b[0] = "ㅇ"
            continue
        if final in ("ㅎ", "ㄶ", "ㅀ") and initial in ASPIRATE:
            a[2] = "" if final == "ㅎ" else SPLIT[final][0]
            b[0] = ASPIRATE[initial]
            continue
        if final == "ㅎ" and initial == "ㄴ":
            a[2] = "ㄴ"
            continue
        sound = FINAL_SOUND.get(final, final)
        if initial == "ㅎ" and sound in ASPIRATE and final not in SPLIT:
            a[2] = ""
            b[0] = ASPIRATE[sound]
            continue
        a[2] = sound
        if initial == "ㄹ":
            if sound in ("ㄴ", "ㄹ"):
                a[2], b[0] = "ㄹ", "ㄹ"  # 신라 → 실라, 몰라 → 몰라
                b.append("l")
            elif sound in ("ㅁ", "ㅇ"):
                b[0] = "ㄴ"  # 종로 → 종노
            else:
                b[0] = "ㄴ"  # 독립 → 동닙
                a[2] = {"ㄱ": "ㅇ", "ㄷ": "ㄴ", "ㅂ": "ㅁ"}[sound]
        elif initial in ("ㄴ", "ㅁ") and sound in ("ㄱ", "ㄷ", "ㅂ"):
            a[2] = {"ㄱ": "ㅇ", "ㄷ": "ㄴ", "ㅂ": "ㅁ"}[sound]  # 합니다 → 함니다
        elif initial == "ㄴ" and sound == "ㄹ":
            b[0] = "ㄹ"
            b.append("l")
    out = []
    for s in syl:
        if isinstance(s, str):
            out.append(s)
            continue
        initial = "l" if len(s) > 3 else INITIAL_RR[s[0]]
        final = FINAL_RR.get(FINAL_SOUND.get(s[2], s[2]), "") if s[2] else ""
        out.append(initial + VOWEL_RR[s[1]] + final)
    return "".join(out)


def romanize(text: str) -> str:
    return " ".join(_word(w) for w in text.split(" "))


def has_syllable(text: str) -> bool:
    return any(0xAC00 <= ord(ch) <= 0xD7A3 for ch in text)
