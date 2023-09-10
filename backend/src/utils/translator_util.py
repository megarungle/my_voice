"""Module for translating text"""

import re
from typing import List

import argostranslate.package
import argostranslate.translate

from src.structs import Data

# TODO: Convert this to r'' type of string
ENG_SYMBOLS_PATTERN = "^[a-zA-Z0-9$@$!%*?&=#^-_., +\(\[\{\}\]\)\|\-'\"\:\;\=\<\>]+$"


def translate_question_if_needed(question: str) -> str:
    """Translates question to russian if it's english"""
    try:
        if is_eng(question):
            question = translate_en_to_ru(question)
    except Exception as exc:
        print(f"ERROR: Translator translating question failed: {exc}")
    return question


def translate_data_if_needed(data: List[Data]) -> List[Data]:
    """Translates data answers to russian if multiple english words detected"""
    try:
        eng_answers_counter = 0
        for answer in data:
            if is_eng(answer.answer) and len(answer.answer) > 5:
                eng_answers_counter += 1

        if eng_answers_counter > len(data) / 2:
            for answer in data:
                if is_eng(answer.answer):
                    answer.answer = translate_en_to_ru(answer.answer)
    except Exception as exc:
        print(f"ERROR: Translator translating data failed: {exc}")
    return data


def is_eng(string: str):
    return bool(re.fullmatch(ENG_SYMBOLS_PATTERN, string))


def translate_en_to_ru(string: str):
    """Translate english to russian"""
    from_code = "en"
    to_code = "ru"

    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code,
            available_packages,
        )
    )
    if package_to_install not in argostranslate.package.get_installed_packages():
        argostranslate.package.install_from_path(package_to_install.download())

    return argostranslate.translate.translate(string, from_code, to_code)


if __name__ == "__main__":
    print(translate_en_to_ru("netherlands"))
    v = re.sub(
        r"[!@#$%^&*\(\)\-_=+\\\|\[\]\{\}\;\:\'\",<.>/?]+\ *", " ", "ответственности?"
    )
    print(re.sub(" +", " ", v))
