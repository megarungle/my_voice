from src.core import Core

from typing import List
from src.structs import InferStatus, Data


class Infer:
    def get_redirect_url(self, _input):
        core = Core()
        print("Waiting for infer request")
        status, data = core.infer(_input)
        if status is InferStatus.status_ok:
            for answer in data:
                answer.data_print()
        return "new_url"


if __name__ == "__main__":
    infer = Infer()
    _input = {
        "question": "Вопрос 7. Что должны сделать Лидеры безопасности, чтобы снизить травматизм?",
        "id": 19749,
        "answers": [
            {
                "answer": "создание раб.групп для контрол",
                "count": 1,
            },
        ],
    }
    infer.get_redirect_url(_input)
