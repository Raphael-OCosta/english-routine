"""Publica o TextLab (textos por gramática): copia engine/histórias/página para public/assets/textlab/.

Rode: python textlab/build_textlab.py
"""
from pathlib import Path
import shutil

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "public" / "assets" / "textlab"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name in ("engine.js", "stories_en.js", "page.js"):
        shutil.copyfile(HERE / name, OUT / name)
        print("public/assets/textlab/" + name)


if __name__ == "__main__":
    main()
